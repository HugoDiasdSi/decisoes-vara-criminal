"""
Assessor Jurídico Virtual - Sistema de Análise de Processos Criminais
Desenvolvido para auxiliar magistrados com IA generativa (Google Gemini)
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, Optional, Tuple, Generator
import shutil

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
            "repository": {
                "url": "https://github.com/HugoDiasdSi/decisoes-vara-criminal.git",
                "local_dir": "decisoes-vara-criminal"
            },
            "paths": {
                "prompts_dir": "prompts",
                "base_conhecimento_dir": "base_conhecimento",
                "modelos_estilo_dir": "modelos_estilo"
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

    def load_all_prompts(self) -> Dict[str, str]:
        """Carrega todos os prompts definidos na configuração"""
        prompts = {}
        prompt_configs = self.config.get("prompts", default={})

        for name in prompt_configs.keys():
            prompts[name] = self.load_prompt(name)

        return prompts


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
        """Carrega modelos de estilo de decisões"""
        modelos_dir = Path(self.config.get("paths", "modelos_estilo_dir", default="modelos_estilo"))
        content = ""

        if not modelos_dir.exists():
            logger.warning(f"Diretório de modelos de estilo não encontrado: {modelos_dir}")
            return ""

        try:
            for file_path in modelos_dir.rglob("*.md"):
                content += f"\n\n--- MODELO DE ESTILO: {file_path.name} ---\n\n"
                content += file_path.read_text(encoding='utf-8')

            logger.info(f"Modelos de estilo carregados de {modelos_dir}")
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
            api_key = os.environ.get('GOOGLE_API_KEY')
            if not api_key:
                raise ValueError("Chave de API não encontrada em GOOGLE_API_KEY")

            genai.configure(api_key=api_key)
            logger.info("API do Gemini configurada com sucesso")
        except Exception as e:
            logger.error(f"ERRO CRÍTICO: {e}")
            raise

    def _extract_with_flash(self, pdf_file) -> Tuple[bool, str]:
        """
        Extrai dados do PDF usando Gemini Flash

        Returns:
            Tuple[bool, str]: (sucesso, conteúdo_extraído_ou_erro)
        """
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
        """
        Constrói o prompt final para o Gemini Pro

        Args:
            tipo_tarefa: "Elaborar Minuta/Decisão" ou "Elaborar Sentença"
            relatorio_previo: Dados extraídos ou fornecidos
            texto_adicional: Instruções adicionais do usuário

        Returns:
            Lista de elementos do prompt
        """
        # Carrega prompts base
        formato_saida = self.prompt_manager.load_prompt("formato_saida")

        if tipo_tarefa == "Elaborar Sentença":
            prompt_principal = self.prompt_manager.load_prompt("elaborar_sentenca")
            prompt_principal += "\n\n" + formato_saida

            # Carrega base de conhecimento para sentenças
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

            # Carrega modelos de estilo para decisões
            modelos_estilo = self.kb_manager.load_style_models()

            prompt_parts = [
                prompt_principal,
                "\n--- CONTEÚDO DOS MODELOS DE ESTILO ---\n",
                modelos_estilo if modelos_estilo else "AVISO: Nenhum modelo de estilo encontrado.",
            ]

        # Adiciona dados do processo
        prompt_parts.extend([
            "\n--- DADOS DO PROCESSO (RELATÓRIO PRÉVIO) ---\n",
            relatorio_previo
        ])

        # Adiciona instruções adicionais se fornecidas
        if texto_adicional and texto_adicional.strip():
            prompt_parts.append(
                f"\n--- INSTRUÇÕES DIRETAS DO USUÁRIO PARA A REDAÇÃO ---\n{texto_adicional}"
            )

        return prompt_parts

    def _generate_with_pro(self, prompt_parts: list) -> Tuple[bool, str, str]:
        """
        Gera decisão/sentença com Gemini Pro

        Returns:
            Tuple[bool, str, str]: (sucesso, pensamento, documentos)
        """
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

            # Separa pensamento de documentos finais
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

    def analisar_processo(self, tipo_tarefa: str, pdf_file,
                         texto_adicional: str) -> Generator[Tuple[str, str, str], None, None]:
        """
        Função principal que orquestra a análise do processo

        Yields:
            Tuple[str, str, str]: (pensamento, documentos, texto_para_copiar)
        """
        # Validação de entrada
        if pdf_file is None and not (texto_adicional and texto_adicional.strip()):
            yield ("Erro de Entrada",
                   "Por favor, envie um PDF ou insira dados na caixa de texto para começar.",
                   "")
            return

        yield ("Iniciando análise...", "Preparando ambiente...", "")

        relatorio_previo = ""

        # Se há PDF, extrai com Flash
        if pdf_file is not None:
            yield ("PDF detectado", "Extraindo dados com Gemini Flash...", "")

            sucesso, resultado = self._extract_with_flash(pdf_file)

            if not sucesso:
                yield ("Erro na Extração", resultado, "")
                return

            relatorio_previo = resultado
            yield (
                f"Extração concluída\n\n**RELATÓRIO EXTRAÍDO:**\n---\n{relatorio_previo[:500]}...\n---",
                "Aguardando redação com Gemini Pro...",
                ""
            )
        else:
            yield ("Modo texto detectado", "Processando texto fornecido...", "")
            relatorio_previo = texto_adicional

        # Constrói prompt para o Pro
        prompt_parts = self._build_prompt_for_pro(
            tipo_tarefa,
            relatorio_previo,
            texto_adicional if pdf_file is not None else None
        )

        # Gera decisão/sentença com Pro
        yield ("Gerando decisão/sentença", "Gemini Pro trabalhando...", "")

        sucesso, pensamento, documentos = self._generate_with_pro(prompt_parts)

        if not sucesso:
            yield ("Erro na Geração", documentos, "")
            return

        # Retorna resultado final
        yield (pensamento, documentos, documentos)

    def limpar_interface(self) -> Tuple:
        """Limpa a interface do Gradio"""
        return None, "", "Elaborar Minuta/Decisão", "", "", ""

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

            with gr.Row():
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

                with gr.Column(scale=2):
                    gr.Markdown("### Raciocínio da IA (Chain of Thought)")
                    output_pensamento = gr.Markdown()

                    with gr.Row():
                        gr.Markdown("### Documentos Finais")
                        copy_btn = gr.Clipboard(label="Copiar Texto", scale=0)

                    output_documentos = gr.Markdown()

            # Define as ações dos botões
            btn_analisar.click(
                fn=self.analisar_processo,
                inputs=[tipo_tarefa, pdf_input, texto_adicional_input],
                outputs=[output_pensamento, output_documentos, copy_btn]
            )

            btn_limpar.click(
                fn=self.limpar_interface,
                inputs=None,
                outputs=[pdf_input, texto_adicional_input, tipo_tarefa,
                        output_pensamento, output_documentos, copy_btn],
                queue=False
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
        assessor.launch()
    except Exception as e:
        logger.critical(f"Erro fatal ao iniciar aplicação: {e}")
        raise
