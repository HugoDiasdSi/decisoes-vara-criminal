---
title: Assessor Jurídico Virtual
emoji: ⚖️
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# Assessor Jurídico Virtual ⚖️

Sistema inteligente para auxiliar magistrados na elaboração de decisões judiciais e sentenças penais, utilizando IA generativa (Google Gemini).

## 🎯 Funcionalidades

- **📄 Extração Automática de PDFs**: Upload de autos processuais e extração inteligente de dados relevantes
- **⚖️ Elaboração de Decisões**: Minutas de decisões interlocutórias, despachos e decisões judiciais
- **📋 Sentenças Completas**: Sentenças penais com dosimetria fundamentada segundo art. 68 do CP
- **🧠 Chain of Thought**: Visualização transparente do raciocínio da IA
- **📚 Base de Conhecimento**: Integração com templates, dosimetria, jurisprudência e orientações

## 🚀 Como Usar

### 1. Escolha a Tarefa
- **Elaborar Minuta/Decisão**: Para despachos e decisões interlocutórias
- **Elaborar Sentença**: Para sentenças penais completas

### 2. Forneça os Dados

**Opção A - Upload de PDF:**
- Faça upload do PDF dos autos processuais
- A IA extrairá automaticamente os dados relevantes

**Opção B - Texto Direto:**
- Cole dados do processo direto na caixa de texto
- Útil para análises rápidas ou dados já extraídos

**Opção C - Combinado:**
- Upload de PDF + instruções adicionais na caixa de texto
- A IA considera ambos

### 3. Clique em "Analisar Processo"

A IA processará em duas etapas:
1. **Extração** (se houver PDF): Gemini Flash extrai dados estruturados
2. **Geração**: Gemini Pro elabora a decisão/sentença fundamentada

### 4. Revise o Resultado

Você verá duas seções:
- **Raciocínio da IA**: Como ela chegou à conclusão (Chain of Thought)
- **Documentos Finais**: Texto pronto para copiar e colar

## 🏗️ Arquitetura

```
┌─────────────┐
│   Usuário   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│   Interface Gradio      │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ PDF? ──Yes──► Flash     │
│              (extração)  │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│   Prompt Builder        │
│   + Base Conhecimento   │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│   Gemini Pro            │
│   (geração)             │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ Pensamento + Documentos │
└─────────────────────────┘
```

## 📚 Base de Conhecimento

O sistema utiliza:

1. **TEMPLATE.md**: Estrutura padrão de sentenças penais
2. **Dosimetria RAG.md**: Regras completas de dosimetria da pena
3. **Agente RAG.md**: Metodologia de análise jurídica
4. **ANTI-dupla punição.md**: Prevenção de bis in idem
5. **Orientações.md**: Diretrizes gerais de redação

## ⚠️ Avisos Importantes

- ⚖️ **Use com responsabilidade**: A IA é um ASSISTENTE, não substitui o magistrado
- 🔍 **Sempre revise**: Decisões judiciais afetam direitos fundamentais
- 📚 **Mantenha atualizado**: Jurisprudência e legislação mudam constantemente
- 🔒 **Segurança**: Não compartilhe dados sensíveis de processos sob sigilo

## 🛠️ Tecnologias

- **IA**: Google Gemini (Flash Lite + Pro 2.5)
- **Interface**: Gradio 4.x
- **Linguagem**: Python 3.10+
- **Framework**: Programação orientada a objetos

## 📖 Documentação Completa

- [Código Fonte](https://github.com/HugoDiasdSi/decisoes-vara-criminal)
- [Guia de Instalação](https://github.com/HugoDiasdSi/decisoes-vara-criminal/blob/main/README_APP.md)
- [Guia de Migração](https://github.com/HugoDiasdSi/decisoes-vara-criminal/blob/main/GUIA_MIGRACAO.md)

## 🤝 Contribuindo

Contribuições são bem-vindas! Visite o [repositório no GitHub](https://github.com/HugoDiasdSi/decisoes-vara-criminal).

## 📄 Licença

MIT License - Código aberto para fins educacionais e de auxílio ao Poder Judiciário.

---

**Desenvolvido com ❤️ para auxiliar o Poder Judiciário brasileiro**
