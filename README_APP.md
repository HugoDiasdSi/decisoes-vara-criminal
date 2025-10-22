# Assessor Jurídico Virtual ⚖️

Sistema inteligente para auxiliar magistrados na elaboração de decisões judiciais e sentenças penais, utilizando IA generativa (Google Gemini).

## 📋 Índice

- [Características](#características)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Melhorias Implementadas](#melhorias-implementadas)
- [Arquitetura](#arquitetura)
- [Contribuindo](#contribuindo)

## ✨ Características

- 🤖 **Extração Inteligente**: Usa Gemini Flash para extrair dados de PDFs processuais
- ⚖️ **Redação Jurídica**: Gemini Pro elabora decisões e sentenças fundamentadas
- 📚 **Base de Conhecimento**: Sistema RAG com dosimetria, templates e orientações
- 🎨 **Modelos de Estilo**: Aprende com decisões anteriores do magistrado
- 🔄 **Duas Modalidades**: Minutas/Decisões ou Sentenças Completas
- 💡 **Chain of Thought**: Mostra o raciocínio da IA
- 📋 **Interface Amigável**: Interface web com Gradio

## 📁 Estrutura do Projeto

```
decisoes-vara-criminal/
├── app_refatorado.py          # Aplicação principal (NOVA VERSÃO)
├── config.json                 # Configurações centralizadas
├── requirements.txt            # Dependências Python
├── README_APP.md              # Esta documentação
│
├── prompts/                    # 🆕 Prompts organizados
│   ├── extracao_flash.md      # Prompt para extração de PDFs
│   ├── assessor_juridico.md   # Prompt para decisões/minutas
│   ├── elaborar_sentenca.md   # Prompt para sentenças
│   └── formato_saida_duplo.md # Formato de resposta da IA
│
├── base_conhecimento/          # Base de conhecimento jurídica
│   ├── TEMPLATE.md            # Template de sentenças
│   ├── Dosimetria RAG.md      # Regras de dosimetria
│   ├── Agente RAG.md          # Metodologia de análise
│   ├── ANTI-dupla punição...  # Evitar bis in idem
│   └── Orientações...         # Diretrizes gerais
│
├── modelos_estilo/             # Modelos de decisões (estilo do magistrado)
│   └── *.md                   # Decisões anteriores como referência
│
└── *.md                        # Decisões de exemplo
```

## 🚀 Instalação

### Pré-requisitos

- Python 3.8+
- Conta Google Cloud com acesso à API Gemini
- Chave de API do Google AI Studio

### Passos

1. **Clone o repositório:**
```bash
git clone https://github.com/HugoDiasdSi/decisoes-vara-criminal.git
cd decisoes-vara-criminal
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure a chave de API:**

**Opção A - Variável de Ambiente (Recomendado):**
```bash
export GOOGLE_API_KEY="sua-chave-aqui"
```

**Opção B - Arquivo .env:**
```bash
echo "GOOGLE_API_KEY=sua-chave-aqui" > .env
```

**Opção C - GitHub Secrets (para deploy):**
- Vá em Settings > Secrets > Actions
- Adicione `GOOGLE_API_KEY` com sua chave

## ⚙️ Configuração

Edite o arquivo `config.json` para personalizar:

```json
{
  "repository": {
    "url": "https://github.com/seu-usuario/seu-repo.git",
    "local_dir": "nome-do-diretorio"
  },
  "models": {
    "flash": "models/gemini-flash-lite-latest",
    "pro": "models/gemini-2.5-pro"
  },
  "generation_config": {
    "flash": {
      "temperature": 0.0
    },
    "pro": {
      "timeout": 600
    }
  }
}
```

### Personalizando Prompts

Edite os arquivos em `prompts/` para ajustar o comportamento da IA:

- `extracao_flash.md`: Como a IA extrai dados do PDF
- `assessor_juridico.md`: Instruções para elaborar decisões
- `elaborar_sentenca.md`: Instruções para elaborar sentenças
- `formato_saida_duplo.md`: Estrutura da resposta

## 📖 Uso

### Executar a Aplicação

```bash
python app_refatorado.py
```

Acesse: `http://localhost:7860`

### Fluxo de Trabalho

1. **Escolha a tarefa:**
   - "Elaborar Minuta/Decisão" - Para despachos e decisões interlocutórias
   - "Elaborar Sentença" - Para sentenças penais completas

2. **Forneça os dados:**
   - **PDF**: Upload de autos, petições, decisões
   - **Texto**: Cole dados extraídos ou instruções diretas

3. **Clique em "Analisar Processo"**

4. **Visualize o resultado:**
   - **Raciocínio da IA**: Como ela chegou à conclusão
   - **Documentos Finais**: Texto pronto para copiar e colar

### Exemplos de Uso

#### Exemplo 1: Sentença com PDF
1. Upload do PDF dos autos
2. Escolha "Elaborar Sentença"
3. (Opcional) Adicione instruções específicas na caixa de texto
4. Clique em "Analisar"

#### Exemplo 2: Decisão Rápida (sem PDF)
1. Cole os dados do processo na caixa de texto
2. Escolha "Elaborar Minuta/Decisão"
3. Clique em "Analisar"

## 🆕 Melhorias Implementadas

### Comparação: Versão Antiga vs. Nova

| Aspecto | Versão Antiga | Versão Nova ✅ |
|---------|---------------|----------------|
| **Prompts** | Hardcoded no código | Arquivos `.md` separados |
| **Configuração** | Variáveis espalhadas | `config.json` centralizado |
| **Organização** | Função única de 150+ linhas | Classes e métodos organizados |
| **Logging** | `print()` básico | `logging` estruturado |
| **Tratamento de Erros** | Genérico | Específico por tipo |
| **Manutenção** | Difícil | Fácil e modular |
| **Reutilização** | Baixa | Alta (classes separadas) |
| **Testabilidade** | Difícil | Fácil (métodos isolados) |

### Principais Melhorias

#### 1. **Arquitetura Orientada a Objetos**
- `Config`: Gerencia configurações
- `PromptManager`: Carrega e cacheia prompts
- `KnowledgeBaseManager`: Gerencia base de conhecimento
- `AssessorJuridicoApp`: Lógica principal da aplicação

#### 2. **Prompts Externalizados**
- Fácil edição sem alterar código
- Versionamento independente
- Reutilização em outros projetos

#### 3. **Logging Estruturado**
```python
logger.info("Extração com Flash concluída")
logger.error(f"Erro na geração: {e}")
```

#### 4. **Tratamento de Erros Robusto**
- Try-catch em cada método
- Mensagens de erro claras
- Graceful degradation

#### 5. **Configuração Flexível**
- JSON editável
- Valores padrão (fallback)
- Fácil adaptação para produção

#### 6. **Cache de Prompts**
- Carregamento único na memória
- Melhor performance

## 🏗️ Arquitetura

### Fluxo de Dados

```
┌─────────────┐
│   Usuário   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│   Interface Gradio              │
│  (criar_interface)              │
└──────┬──────────────────────────┘
       │
       ▼
┌─────────────────────────────────┐
│  analisar_processo()            │
│  - Valida entrada               │
│  - Decide fluxo (PDF ou texto)  │
└──────┬──────────────────────────┘
       │
       ├─────► PDF? ──Yes──► _extract_with_flash()
       │                      │
       │                      ▼
       │                  Gemini Flash
       │                      │
       │                      ▼
       │              Relatório Prévio
       │                      │
       └──────────────────────┘
                              │
                              ▼
                    _build_prompt_for_pro()
                    - Carrega prompts
                    - Carrega base conhecimento
                    - Monta prompt completo
                              │
                              ▼
                    _generate_with_pro()
                              │
                              ▼
                         Gemini Pro
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Pensamento + Docs   │
                    └─────────────────────┘
                              │
                              ▼
                        ┌─────────┐
                        │ Usuário │
                        └─────────┘
```

### Componentes

#### Config
- Carrega `config.json`
- Fornece acesso a configurações
- Fallback para valores padrão

#### PromptManager
- Carrega prompts de arquivos `.md`
- Mantém cache em memória
- Retorna mensagens de erro claras

#### KnowledgeBaseManager
- Carrega base de conhecimento
- Carrega modelos de estilo
- Organiza conteúdo para IA

#### AssessorJuridicoApp
- Orquestra todo o fluxo
- Gerencia modelos Gemini
- Cria interface Gradio

## 🎯 Próximos Passos

### Melhorias Futuras Sugeridas

- [ ] **Histórico de conversas** (salvar análises anteriores)
- [ ] **Upload múltiplo** (processar vários PDFs)
- [ ] **Exportação** (PDF, DOCX da decisão gerada)
- [ ] **Templates personalizados** por tipo de decisão
- [ ] **Feedback do usuário** (thumbs up/down na resposta)
- [ ] **Modo offline** (cache de modelos locais)
- [ ] **API REST** (integração com outros sistemas)
- [ ] **Testes automatizados** (pytest)
- [ ] **CI/CD** (GitHub Actions)
- [ ] **Docker** (containerização)

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/melhoria`)
3. Commit suas mudanças (`git commit -m 'Adiciona melhoria X'`)
4. Push para a branch (`git push origin feature/melhoria`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é de código aberto para fins educacionais e de auxílio ao Poder Judiciário.

## ⚠️ Avisos Importantes

- ⚖️ **Use com responsabilidade**: A IA é um ASSISTENTE, não substitui o magistrado
- 🔍 **Sempre revise**: Decisões judiciais afetam direitos fundamentais
- 📚 **Mantenha atualizado**: Jurisprudência e legislação mudam constantemente
- 🔒 **Segurança**: Não compartilhe dados sensíveis de processos sob sigilo

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma [Issue no GitHub](https://github.com/HugoDiasdSi/decisoes-vara-criminal/issues)
- Entre em contato com o desenvolvedor

---

**Desenvolvido com ❤️ para auxiliar o Poder Judiciário brasileiro**
