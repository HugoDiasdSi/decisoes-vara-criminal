"""
Assessor Jurídico Virtual - Hugging Face Spaces
Sistema de análise de processos criminais com IA generativa

IMPORTANTE: Este arquivo é otimizado para Hugging Face Spaces
Para uso local, use app_refatorado.py
"""

import os
import json
import logging
import time
from pathlib import Path
from typing import Dict, Optional, Tuple, Generator

import google.generativeai as genai
import gradio as gr

# --- CONFIGURAÇÃO DE LOGGING ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# --- CLASSE DE CONFIGURAÇÃO ---
class Config:
    """Gerencia configurações da aplicação"""

    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """Carrega configurações do arquivo JSON"""
        try:
            config_path = Path(self.config_file)
            if not config_path.exists():
                logger.warning(f"Arquivo de configuração {self.config_file} não encontrado. Usando valores padrão.")
                return self._default_config()

            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Erro ao carregar configuração: {e}")
            return self._default_config()

    def _default_config(self) -> dict:
        """Retorna configuração padrão"""
        return {
            "paths": {
                "prompts_dir": "prompts",
                "base_conhecimento_dir": "base_conhecimento",
                "modelos_estilo_dir": "modelos_estilo"
            },
            "prompts": {
                "extracao_flash": "prompts/extracao_flash.md",
                "assessor_juridico": "prompts/assessor_juridico.md",
                "elaborar_sentenca": "prompts/elaborar_sentenca.md",
                "formato_saida": "prompts/formato_saida_duplo.md"
            },
            "base_conhecimento": {
                "template": "base_conhecimento/TEMPLATE.md",
                "dosimetria": "base_conhecimento/Dosimetria RAG.md",
                "agente_rag": "base_conhecimento/Agente RAG.md",
                "anti_dupla_punicao": "base_conhecimento/ANTI-dupla punição pelo mesmo fato na dosimetria da pena.md",
                "orientacoes": "base_conhecimento/Orientações para a base de conhecimento.md"
            },
            "models": {
                "flash": "models/gemini-flash-lite-latest",
                "pro": "models/gemini-2.5-pro"
            },
            "generation_config": {
                "flash": {"temperature": 0.0},
                "pro": {"timeout": 600}
            },
            "ui": {
                "title": "Assessor Jurídico Virtual ⚖️",
                "theme": "soft"
            }
        }

    def get(self, *keys, default=None):
        """Acessa valores aninhados na configuração"""
        value = self.config
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key, default)
            else:
                return default
        return value if value is not None else default


# --- CLASSE DE GERENCIAMENTO DE PROMPTS ---
class PromptManager:
    """Gerencia carregamento e cache de prompts"""

    def __init__(self, config: Config):
        self.config = config
        self._cache = {}

    def load_prompt(self, prompt_name: str) -> str:
        """Carrega um prompt do arquivo"""
        if prompt_name in self._cache:
            return self._cache[prompt_name]

        prompt_path = self.config.get("prompts", prompt_name)
        if not prompt_path:
            logger.error(f"Prompt '{prompt_name}' não encontrado na configuração")
            return ""

        try:
            full_path = Path(prompt_path)
            if not full_path.exists():
                logger.error(f"Arquivo de prompt não encontrado: {full_path}")
                return f"ERRO: Prompt {prompt_name} não encontrado"

            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self._cache[prompt_name] = content
                logger.info(f"Prompt '{prompt_name}' carregado com sucesso")
                return content
        except Exception as e:
            logger.error(f"Erro ao carregar prompt {prompt_name}: {e}")
            return f"ERRO ao carregar prompt: {e}"


# --- CLASSE DE GERENCIAMENTO DE BASE DE CONHECIMENTO ---
class KnowledgeBaseManager:
    """Gerencia carregamento da base de conhecimento"""

    def __init__(self, config: Config):
        self.config = config

    def load_knowledge_files(self) -> Dict[str, str]:
        """Carrega arquivos da base de conhecimento"""
        knowledge_files = {}
        kb_config = self.config.get("base_conhecimento", default={})

        for name, filepath in kb_config.items():
            try:
                full_path = Path(filepath)
                if full_path.exists():
                    with open(full_path, 'r', encoding='utf-8') as f:
                        knowledge_files[name] = f.read()
                    logger.info(f"Base de conhecimento '{name}' carregada")
                else:
                    knowledge_files[name] = f"AVISO: Arquivo {filepath} não encontrado."
                    logger.warning(f"Arquivo da base de conhecimento não encontrado: {filepath}")
            except Exception as e:
                knowledge_files[name] = f"ERRO ao carregar {filepath}: {e}"
                logger.error(f"Erro ao carregar base de conhecimento {name}: {e}")

        return knowledge_files

    def load_style_models(self) -> str:
        """Carrega modelos de estilo de decisões da raiz do repositório"""
        # Busca na raiz do repositório por arquivos .md (exceto README.md e base_conhecimento/)
        root_dir = Path(".")
        content = ""

        try:
            arquivos_carregados = 0
            for file_path in root_dir.glob("*.md"):
                # Ignora README.md e arquivos de exemplo
                if file_path.name == "README.md" or "EXEMPLO" in file_path.name.upper():
                    continue

                content += f"\n\n--- MODELO DE ESTILO: {file_path.name} ---\n\n"
                content += file_path.read_text(encoding='utf-8')
                arquivos_carregados += 1

            if arquivos_carregados > 0:
                logger.info(f"Modelos de estilo carregados: {arquivos_carregados} arquivos da raiz")
            else:
                logger.warning("Nenhum modelo de estilo encontrado na raiz do repositório")

        except Exception as e:
            logger.error(f"Erro ao carregar modelos de estilo: {e}")

        return content


# --- CLASSE PRINCIPAL DA APLICAÇÃO ---
class AssessorJuridicoApp:
    """Aplicação principal do Assessor Jurídico Virtual"""

    def __init__(self, config_file: str = "config.json"):
        self.config = Config(config_file)
        self.prompt_manager = PromptManager(self.config)
        self.kb_manager = KnowledgeBaseManager(self.config)
        self._configure_api()

    def _configure_api(self):
        """Configura a API do Google Gemini"""
        try:
            # Hugging Face Spaces usa HF_TOKEN, mas também suporta GOOGLE_API_KEY
            api_key = os.environ.get('GOOGLE_API_KEY') or os.environ.get('GEMINI_API_KEY')

            if not api_key:
                raise ValueError(
                    "Chave de API não encontrada. Configure GOOGLE_API_KEY nos Secrets do Space."
                )

            genai.configure(api_key=api_key)
            logger.info("API do Gemini configurada com sucesso")
        except Exception as e:
            logger.error(f"ERRO CRÍTICO: {e}")
            raise

    def _extract_with_flash(self, pdf_file) -> Tuple[bool, str]:
        """Extrai dados do PDF usando Gemini Flash"""
        try:
            prompt_extracao = self.prompt_manager.load_prompt("extracao_flash")

            with open(pdf_file.name, 'rb') as f:
                pdf_bytes = f.read()

            pdf_file_part = {"mime_type": "application/pdf", "data": pdf_bytes}

            flash_config = genai.GenerationConfig(
                temperature=self.config.get("generation_config", "flash", "temperature", default=0.0)
            )

            flash_model_name = self.config.get("models", "flash", default="models/gemini-flash-lite-latest")
            flash_model = genai.GenerativeModel(flash_model_name)

            logger.info("Iniciando extração com Gemini Flash...")
            response = flash_model.generate_content(
                [prompt_extracao, pdf_file_part],
                generation_config=flash_config
            )

            logger.info("Extração com Flash concluída com sucesso")
            return True, response.text

        except Exception as e:
            logger.error(f"Erro na extração com Flash: {e}")
            return False, f"Erro na extração: {e}"

    def _build_prompt_for_pro(self, tipo_tarefa: str, relatorio_previo: str,
                             texto_adicional: Optional[str] = None) -> list:
        """Constrói o prompt final para o Gemini Pro"""
        formato_saida = self.prompt_manager.load_prompt("formato_saida")

        if tipo_tarefa == "Elaborar Sentença":
            prompt_principal = self.prompt_manager.load_prompt("elaborar_sentenca")
            prompt_principal += "\n\n" + formato_saida

            kb = self.kb_manager.load_knowledge_files()

            prompt_parts = [
                prompt_principal,
                "\n--- CONTEÚDO DA BASE DE CONHECIMENTO OBRIGATÓRIA ---\n",
                f"\n## TEMPLATE.md\n{kb.get('template', 'NÃO ENCONTRADO')}",
                f"\n## Dosimetria.md\n{kb.get('dosimetria', 'NÃO ENCONTRADO')}",
                f"\n## Agente RAG.md\n{kb.get('agente_rag', 'NÃO ENCONTRADO')}",
                f"\n## ANTI-dupla punição.md\n{kb.get('anti_dupla_punicao', 'NÃO ENCONTRADO')}",
                f"\n## Orientações.md\n{kb.get('orientacoes', 'NÃO ENCONTRADO')}",
            ]
        else:
            prompt_principal = self.prompt_manager.load_prompt("assessor_juridico")
            prompt_principal += "\n\n" + formato_saida

            modelos_estilo = self.kb_manager.load_style_models()

            prompt_parts = [
                prompt_principal,
                "\n--- CONTEÚDO DOS MODELOS DE ESTILO ---\n",
                modelos_estilo if modelos_estilo else "AVISO: Nenhum modelo de estilo encontrado.",
            ]

        prompt_parts.extend([
            "\n--- DADOS DO PROCESSO (RELATÓRIO PRÉVIO) ---\n",
            relatorio_previo
        ])

        if texto_adicional and texto_adicional.strip():
            prompt_parts.append(
                f"\n--- INSTRUÇÕES DIRETAS DO USUÁRIO PARA A REDAÇÃO ---\n{texto_adicional}"
            )

        return prompt_parts

    def _generate_with_pro(self, prompt_parts: list) -> Tuple[bool, str, str]:
        """Gera decisão/sentença com Gemini Pro"""
        try:
            pro_model_name = self.config.get("models", "pro", default="models/gemini-2.5-pro")
            pro_model = genai.GenerativeModel(pro_model_name)

            timeout = self.config.get("generation_config", "pro", "timeout", default=600)

            logger.info("Enviando para Gemini Pro...")
            response = pro_model.generate_content(
                prompt_parts,
                request_options={"timeout": timeout}
            )

            full_text = response.text
            logger.info("Geração com Pro concluída com sucesso")

            if "### DOCUMENTOS FINAIS" in full_text:
                parts = full_text.split("### DOCUMENTOS FINAIS", 1)
                pensamento = parts[0].replace("### PENSAMENTO (CHAIN OF THOUGHT)", "").strip()
                documentos = parts[1].strip()
            else:
                documentos = f"AVISO: A IA não seguiu o formato de saída esperado.\n\n{full_text}"
                pensamento = "Formato de saída não seguido corretamente."
                logger.warning("IA não seguiu o formato de saída esperado")

            return True, pensamento, documentos

        except Exception as e:
            logger.error(f"Erro na geração com Pro: {e}")
            return False, "", f"Erro na geração: {e}"

    def _format_elapsed_time(self, seconds: int) -> str:
        """Formata tempo decorrido em formato legível"""
        if seconds < 60:
            return f"{seconds}s"
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}m {secs}s"

    def _create_progress_message(self, stage: str, elapsed: int) -> str:
        """Cria mensagem de progresso com spinner e tempo"""
        spinner = "⏳"
        return f"""
{spinner} **{stage}**

⏱️ Tempo decorrido: **{self._format_elapsed_time(elapsed)}**

*Aguarde, estou trabalhando...*
"""

    def analisar_processo(self, tipo_tarefa: str, pdf_file,
                         texto_adicional: str) -> Generator[Tuple[str, str], None, None]:
        """Função principal que orquestra a análise do processo"""
        if pdf_file is None and not (texto_adicional and texto_adicional.strip()):
            yield ("**Erro de Entrada**\n\nPor favor, envie um PDF ou insira dados na caixa de texto para começar.", "")
            return

        inicio_total = time.time()

        yield ("⏳ **Iniciando análise...**\n\n⏱️ Tempo: 0s\n\nPreparando ambiente...", "")

        relatorio_previo = ""

        if pdf_file is not None:
            inicio_extracao = time.time()
            yield ("📄 **PDF detectado**\n\n⏱️ Tempo: 0s\n\nExtraindo dados com Gemini Flash...", "")

            sucesso, resultado = self._extract_with_flash(pdf_file)

            if not sucesso:
                yield (f"❌ **Erro na Extração**\n\n{resultado}", "")
                return

            tempo_extracao = int(time.time() - inicio_extracao)
            relatorio_previo = resultado
            yield (
                f"✅ **Extração concluída em {self._format_elapsed_time(tempo_extracao)}**\n\n**RELATÓRIO EXTRAÍDO:**\n\n---\n{relatorio_previo[:500]}...\n---\n\n⏳ Preparando para redação...",
                ""
            )
        else:
            yield ("📝 **Modo texto detectado**\n\n⏱️ Tempo: 0s\n\nProcessando texto fornecido...", "")
            relatorio_previo = texto_adicional

        prompt_parts = self._build_prompt_for_pro(
            tipo_tarefa,
            relatorio_previo,
            texto_adicional if pdf_file is not None else None
        )

        inicio_geracao = time.time()
        yield (self._create_progress_message("Gerando decisão/sentença com Gemini Pro", 0), "")

        # Inicia geração em background e monitora progresso
        import threading
        resultado_geracao = {}

        def gerar():
            sucesso, pensamento, documentos = self._generate_with_pro(prompt_parts)
            resultado_geracao['sucesso'] = sucesso
            resultado_geracao['pensamento'] = pensamento
            resultado_geracao['documentos'] = documentos

        thread = threading.Thread(target=gerar)
        thread.start()

        # Atualiza progresso a cada 3 segundos
        while thread.is_alive():
            elapsed = int(time.time() - inicio_geracao)
            yield (self._create_progress_message("Gerando decisão/sentença com Gemini Pro", elapsed), "")
            thread.join(timeout=3)

        # Pega resultado
        if not resultado_geracao.get('sucesso', False):
            yield (f"❌ **Erro na Geração**\n\n{resultado_geracao.get('documentos', 'Erro desconhecido')}", "")
            return

        tempo_total = int(time.time() - inicio_total)
        tempo_geracao = int(time.time() - inicio_geracao)

        pensamento_final = f"""✅ **Processamento concluído!**

⏱️ **Tempo de geração:** {self._format_elapsed_time(tempo_geracao)}
⏱️ **Tempo total:** {self._format_elapsed_time(tempo_total)}

---

{resultado_geracao['pensamento']}
"""

        yield (pensamento_final, resultado_geracao['documentos'])

    def limpar_interface(self) -> Tuple:
        """Limpa a interface do Gradio"""
        return None, "", "Elaborar Minuta/Decisão", "", ""

    def criar_interface(self) -> gr.Blocks:
        """Cria e retorna a interface Gradio"""
        theme_name = self.config.get("ui", "theme", default="soft")
        title = self.config.get("ui", "title", default="Assessor Jurídico Virtual ⚖️")

        with gr.Blocks(theme=getattr(gr.themes, theme_name.capitalize())(), title=title) as app:
            gr.Markdown(f"# {title}")
            gr.Markdown(
                "Escolha a tarefa, forneça os dados do processo e clique em 'Analisar'. "
                "Use 'Limpar' para começar de novo."
            )

            gr.Markdown(
                """
                > ⚠️ **Aviso:** Este é um assistente de IA. Sempre revise e valide as decisões geradas.
                > A responsabilidade final é do magistrado.
                """
            )

            with gr.Row():
                # Coluna de inputs
                with gr.Column(scale=1):
                    tipo_tarefa = gr.Radio(
                        ["Elaborar Minuta/Decisão", "Elaborar Sentença"],
                        label="1. Escolha a Tarefa",
                        value="Elaborar Minuta/Decisão"
                    )
                    pdf_input = gr.File(
                        label="2. Envie o PDF (Opcional)",
                        file_types=[".pdf"]
                    )
                    texto_adicional_input = gr.Textbox(
                        label="3. Instruções e/ou Dados Adicionais (Opcional)",
                        lines=10,
                        placeholder="Cole aqui instruções, extratos, dados do processo, etc."
                    )

                    with gr.Row():
                        btn_limpar = gr.Button("Limpar")
                        btn_analisar = gr.Button("Analisar Processo", variant="primary")

                # Coluna de outputs - dividida em duas seções
                with gr.Column(scale=2):
                    # Seção 1: Chain of Thought e Relatório
                    with gr.Group():
                        gr.Markdown("### 🧠 Raciocínio da IA e Relatório Prévio")
                        output_pensamento = gr.Markdown()

                    # Seção 2: Decisão Final com botão de copiar
                    with gr.Group():
                        with gr.Row():
                            gr.Markdown("### ⚖️ Decisão Judicial Final")
                            btn_copiar = gr.Button("📋 Copiar Decisão", scale=0, size="sm")

                        output_decisao = gr.Textbox(
                            label="",
                            lines=20,
                            max_lines=50,
                            show_label=False,
                            interactive=True,
                            placeholder="A decisão aparecerá aqui após a análise..."
                        )

            # Conectar botões
            btn_analisar.click(
                fn=self.analisar_processo,
                inputs=[tipo_tarefa, pdf_input, texto_adicional_input],
                outputs=[output_pensamento, output_decisao]
            )

            btn_copiar.click(
                fn=lambda x: x,
                inputs=[output_decisao],
                outputs=[],
                js="(x) => {navigator.clipboard.writeText(x); alert('Decisão copiada para a área de transferência!');}"
            )

            btn_limpar.click(
                fn=self.limpar_interface,
                inputs=None,
                outputs=[pdf_input, texto_adicional_input, tipo_tarefa,
                        output_pensamento, output_decisao],
                queue=False
            )

            gr.Markdown(
                """
                ---
                ### 📚 Sobre este Sistema

                Sistema desenvolvido para auxiliar magistrados na elaboração de decisões judiciais e sentenças penais.
                Utiliza Google Gemini (Flash + Pro) para extração de dados e geração de minutas fundamentadas.

                **Funcionalidades:**
                - 📄 Extração automática de dados de PDFs processuais
                - ⚖️ Elaboração de decisões interlocutórias e despachos
                - 📋 Elaboração de sentenças penais completas com dosimetria
                - 🧠 Chain of Thought transparente
                - 📚 Base de conhecimento jurídica integrada

                **Código aberto:** [GitHub](https://github.com/HugoDiasdSi/decisoes-vara-criminal)
                """
            )

        return app

    def launch(self, **kwargs):
        """Lança a aplicação Gradio"""
        app = self.criar_interface()
        logger.info("Iniciando aplicação Gradio...")
        app.launch(**kwargs)


# --- PONTO DE ENTRADA ---
if __name__ == "__main__":
    try:
        assessor = AssessorJuridicoApp()
        # No Hugging Face Spaces, não precisa especificar share=True
        assessor.launch()
    except Exception as e:
        logger.critical(f"Erro fatal ao iniciar aplicação: {e}")
        raise
