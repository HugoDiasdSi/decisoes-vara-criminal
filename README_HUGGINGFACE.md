---
title: Assessor Jurídico Criminal - Sistema RAG
emoji: ⚖️
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.19.2
app_file: app.py
pinned: false
license: apache-2.0
---

# ⚖️ Assessor Jurídico Criminal - Sistema RAG

Sistema de inteligência artificial para apoio à elaboração de decisões judiciais criminais, baseado em banco de conhecimento com minutas de decisões anteriores.

## 🎯 Sobre o Projeto

Este aplicativo utiliza **Retrieval-Augmented Generation (RAG)** para auxiliar magistrados e assessores jurídicos na elaboração de decisões judiciais. O sistema:

- ✅ Processa autos digitais em PDF (com suporte a OCR)
- ✅ Busca minutas relevantes em um banco de conhecimento jurídico
- ✅ Gera decisões fundamentadas seguindo o estilo do magistrado
- ✅ Garante conformidade com as normas processuais e formatação judicial

## 🚀 Como Usar

### 1. **Upload dos Autos**
Faça upload dos PDFs dos autos processuais. O sistema suporta PDFs nativos e digitalizados (com OCR).

### 2. **Descreva a Tarefa**
Indique qual decisão você deseja elaborar:
- "Elaborar decisão de recebimento da denúncia"
- "Analisar pedido de liberdade provisória"
- "Decisão sobre absolvição sumária"

### 3. **Adicione Contexto (Opcional)**
Forneça informações adicionais relevantes ao caso.

### 4. **Processar**
Clique em "Processar" e aguarde. O sistema irá:
1. Extrair texto dos PDFs
2. Buscar minutas relevantes
3. Analisar os autos
4. Gerar a decisão fundamentada

## 📚 Base de Conhecimento

O sistema possui acesso a mais de **70 minutas** de decisões judiciais, incluindo:

- Recebimento e rejeição de denúncia
- Decisões sobre prisão preventiva e liberdade provisória
- Medidas protetivas de urgência
- Absolvição sumária
- Extinção de punibilidade
- Acordos de não persecução penal (ANPP)
- Transação penal
- E muito mais...

## 🔧 Tecnologias

- **Interface:** Gradio
- **IA:** Google Gemini 1.5 Pro
- **Embeddings:** BERT em Português
- **PDF Processing:** PyPDF2, pytesseract
- **RAG:** sentence-transformers, scikit-learn

## ⚠️ Aviso Legal

**IMPORTANTE:** Este sistema é uma ferramenta de apoio à elaboração de decisões judiciais. Todas as decisões geradas devem ser **cuidadosamente revisadas** por um magistrado antes de serem publicadas.

O sistema:
- ✅ Auxilia na elaboração
- ✅ Sugere fundamentação
- ✅ Mantém uniformidade de estilo
- ❌ NÃO substitui a análise jurídica humana
- ❌ NÃO deve ser usado sem revisão

## 📖 Documentação Completa

Para mais detalhes sobre deployment, configuração e uso avançado, consulte:
- [README_APP.md](README_APP.md) - Documentação completa
- [DEPLOY.md](DEPLOY.md) - Guia de deploy
- [Repositório GitHub](https://github.com/HugoDiasdSi/decisoes-vara-criminal)

## 🤝 Contribuições

Este projeto é de código aberto. Contribuições são bem-vindas via Pull Request no repositório GitHub.

---

**Versão:** 1.0.0
**Desenvolvido para:** Varas Criminais de Pernambuco
**Repositório:** [decisoes-vara-criminal](https://github.com/HugoDiasdSi/decisoes-vara-criminal)
