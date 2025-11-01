"""
Aplicativo Hugging Face Spaces - Assessor Jurídico Criminal
Sistema RAG para elaboração de decisões judiciais baseado em banco de conhecimento
"""

import gradio as gr
import os
from pathlib import Path
import json
from typing import List, Dict, Tuple
import google.generativeai as genai
from utils.pdf_extractor import extract_text_from_pdf
from utils.rag_system import RAGSystem
from utils.prompt_builder import build_full_prompt
from utils.rate_limiter import RateLimiter, retry_with_exponential_backoff

# Configuração da API do Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Inicializar sistema RAG
rag_system = RAGSystem()

# Inicializar rate limiter (Gemini 2.0 Flash tier free: 15 RPM e 1M TPM)
# Sendo conservador com 125 TPM como mencionado pelo usuário
rate_limiter = RateLimiter(tokens_per_minute=125)

def load_knowledge_base():
    """Carrega todas as minutas e metadados no sistema RAG"""
    try:
        # Carregar metadados
        with open("minutas_metadata.json", "r", encoding="utf-8") as f:
            metadata = json.load(f)

        # Carregar todas as minutas
        minutas_dir = Path(".")
        for item in metadata:
            filename = item["filename"]
            filepath = minutas_dir / filename

            if filepath.exists():
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                # Adicionar ao sistema RAG
                rag_system.add_document(
                    filename=filename,
                    content=content,
                    tags=item.get("tags", []),
                    description=item.get("descricao", "")
                )

        return True, f"Base de conhecimento carregada: {len(metadata)} minutas"
    except Exception as e:
        return False, f"Erro ao carregar base de conhecimento: {str(e)}"

def process_case(pdf_files, task_description, user_context=""):
    """
    Processa os autos digitais e gera a decisão judicial

    Args:
        pdf_files: Lista de arquivos PDF dos autos
        task_description: Descrição da tarefa (ex: "elaborar decisão", "analisar denúncia")
        user_context: Contexto adicional fornecido pelo usuário
    """
    try:
        if not GEMINI_API_KEY:
            return "⚠️ API Key do Gemini não configurada. Configure a variável de ambiente GEMINI_API_KEY."

        # ETAPA 1: Extrair texto dos PDFs
        extracted_texts = []
        status_msg = "📄 Extraindo texto dos PDFs...\n"

        if pdf_files:
            for pdf_file in pdf_files:
                text = extract_text_from_pdf(pdf_file.name)
                extracted_texts.append({
                    "filename": os.path.basename(pdf_file.name),
                    "content": text
                })
                status_msg += f"✓ {os.path.basename(pdf_file.name)}\n"
        else:
            return "⚠️ Nenhum arquivo PDF foi fornecido."

        # ETAPA 2: Análise inicial e busca de minutas relevantes
        status_msg += "\n🔍 Analisando autos e buscando minutas relevantes...\n"

        # Concatenar todo o conteúdo extraído
        full_text = "\n\n---\n\n".join([
            f"### {doc['filename']}\n{doc['content']}"
            for doc in extracted_texts
        ])

        # Buscar minutas relevantes usando RAG
        relevant_minutas = rag_system.search_relevant_minutas(
            query=f"{task_description} {user_context}",
            top_k=3
        )

        status_msg += f"✓ {len(relevant_minutas)} minutas relevantes encontradas\n"
        for i, minuta in enumerate(relevant_minutas, 1):
            status_msg += f"  {i}. {minuta['filename']}\n"

        # ETAPA 3: Construir prompt completo
        status_msg += "\n⚙️ Preparando análise jurídica...\n"

        full_prompt = build_full_prompt(
            autos_text=full_text,
            task=task_description,
            context=user_context,
            relevant_minutas=relevant_minutas
        )

        # ETAPA 4: Processar com Gemini
        status_msg += "\n🤖 Processando com IA (isso pode levar alguns minutos)...\n"

        # Estimar tokens e aplicar rate limiting
        estimated_tokens = rate_limiter.estimate_tokens(full_prompt)
        status_msg += f"📊 Tokens estimados: ~{estimated_tokens}\n"

        # Verificar se excede o limite
        if estimated_tokens > 30000:  # Gemini 2.0 Flash aceita até 1M tokens, mas vamos ser conservadores
            status_msg += "⚠️ Prompt muito grande, otimizando...\n"
            # Reduzir conteúdo das minutas se necessário
            for minuta in relevant_minutas:
                if len(minuta['content']) > 3000:
                    minuta['content'] = minuta['content'][:3000] + "\n\n[... conteúdo truncado ...]"

            # Reconstruir prompt
            full_prompt = build_full_prompt(
                autos_text=full_text[:15000] if len(full_text) > 15000 else full_text,
                task=task_description,
                context=user_context,
                relevant_minutas=relevant_minutas
            )
            estimated_tokens = rate_limiter.estimate_tokens(full_prompt)
            status_msg += f"✓ Prompt otimizado: ~{estimated_tokens} tokens\n"

        # Aplicar rate limiting
        rate_limiter.wait_if_needed(estimated_tokens)

        # Usar Gemini 2.0 Flash (tier free)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')

        # Configuração otimizada para tier free
        generation_config = {
            "temperature": 0.3,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }

        # Função com retry
        @retry_with_exponential_backoff
        def generate_with_retry():
            return model.generate_content(
                full_prompt,
                generation_config=generation_config
            )

        # Gerar resposta com retry automático
        response = generate_with_retry()

        # ETAPA 5: Formatar resposta
        result = f"""
{status_msg}

{'='*80}
RESULTADO DA ANÁLISE
{'='*80}

{response.text}

{'='*80}
MINUTAS CONSULTADAS
{'='*80}

"""
        for i, minuta in enumerate(relevant_minutas, 1):
            result += f"\n{i}. **{minuta['filename']}**\n"
            result += f"   {minuta['description']}\n"

        return result

    except Exception as e:
        return f"❌ Erro ao processar: {str(e)}\n\nDetalhes técnicos: {type(e).__name__}"

def create_interface():
    """Cria a interface Gradio"""

    with gr.Blocks(
        title="Assessor Jurídico Criminal - IA",
        theme=gr.themes.Soft()
    ) as demo:

        gr.Markdown("""
        # ⚖️ Assessor Jurídico Criminal - Sistema RAG

        Sistema de inteligência artificial para apoio à elaboração de decisões judiciais criminais,
        baseado em banco de conhecimento com minutas de decisões anteriores.

        ### 📋 Como usar:
        1. Faça upload dos PDFs dos autos processuais
        2. Descreva a tarefa que deseja realizar
        3. Adicione contexto adicional se necessário
        4. Clique em "Processar" e aguarde a análise

        ⏱️ **Tier Free**: Este app usa Gemini 2.0 Flash tier gratuito (125 TPM).
        Pode haver tempo de espera entre requisições para respeitar os limites da API.
        """)

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📎 Upload de Autos")
                pdf_input = gr.File(
                    label="Autos Digitais (PDFs)",
                    file_count="multiple",
                    file_types=[".pdf"],
                    type="filepath"
                )

                gr.Markdown("### 📝 Tarefa")
                task_input = gr.Textbox(
                    label="Descrição da tarefa",
                    placeholder="Ex: Elaborar decisão de recebimento da denúncia\nAnalise preliminar para absolvição sumária\nDecisão sobre pedido de liberdade provisória",
                    lines=3
                )

                context_input = gr.Textbox(
                    label="Contexto adicional (opcional)",
                    placeholder="Informações adicionais sobre o caso, peculiaridades, observações...",
                    lines=3
                )

                process_btn = gr.Button(
                    "🚀 Processar",
                    variant="primary",
                    size="lg"
                )

            with gr.Column(scale=2):
                gr.Markdown("### 📄 Resultado")
                output = gr.Textbox(
                    label="Análise e Decisão",
                    lines=30,
                    max_lines=50,
                    show_copy_button=True
                )

        gr.Markdown("""
        ---
        ### ℹ️ Informações Importantes

        - **Sistema RAG**: Utiliza Retrieval-Augmented Generation para buscar minutas relevantes
        - **Base de conhecimento**: Mais de 70 minutas de decisões judiciais
        - **Modelo de IA**: Google Gemini 2.0 Flash (Tier Free - 125 TPM)
        - **OCR**: Suporta PDFs digitalizados e nativos
        - **Rate Limiting**: Sistema automático de controle de taxa para respeitar limites da API

        ⚠️ **Aviso Legal**: Este sistema é uma ferramenta de apoio. Todas as decisões devem ser revisadas
        por um magistrado antes de serem publicadas.

        ⏳ **Tempo de Processamento**: Devido aos limites do tier gratuito, o processamento pode levar
        alguns minutos, especialmente para PDFs grandes ou múltiplos autos.

        📚 **Base de Conhecimento**: [GitHub Repository](https://github.com/HugoDiasdSi/decisoes-vara-criminal)
        """)

        # Event handlers
        process_btn.click(
            fn=process_case,
            inputs=[pdf_input, task_input, context_input],
            outputs=output
        )

        # Carregar base de conhecimento ao iniciar
        demo.load(
            fn=load_knowledge_base,
            outputs=None
        )

    return demo

# Inicializar e lançar aplicativo
if __name__ == "__main__":
    # Carregar base de conhecimento
    success, message = load_knowledge_base()
    print(message)

    # Criar e lançar interface
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
