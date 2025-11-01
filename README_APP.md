# ⚖️ Assessor Jurídico Criminal - Sistema RAG

Sistema de inteligência artificial para apoio à elaboração de decisões judiciais criminais, baseado em banco de conhecimento com minutas de decisões anteriores.

## 🎯 Sobre o Projeto

Este aplicativo utiliza **Retrieval-Augmented Generation (RAG)** para auxiliar magistrados e assessores jurídicos na elaboração de decisões judiciais. O sistema:

- Processa autos digitais em PDF (com suporte a OCR)
- Busca minutas relevantes em um banco de conhecimento jurídico
- Gera decisões fundamentadas seguindo o estilo do magistrado
- Garante conformidade com as normas processuais e formatação judicial

## 🚀 Funcionalidades

### 📋 Processamento de Autos
- Upload de múltiplos PDFs
- Extração de texto nativo e via OCR
- Identificação automática de IDs de documentos
- Detecção de seções (denúncia, depoimentos, laudos, etc.)

### 🔍 Sistema RAG Inteligente
- Busca semântica por similaridade
- Filtro por tags e palavras-chave
- Ranking de relevância
- Mais de 70 minutas de decisões judiciais

### 🤖 Geração de Decisões
- Análise completa dos autos
- Seleção automática da minuta mais adequada
- Adaptação ao caso concreto
- Formatação conforme normas judiciais

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

## 🔧 Tecnologias Utilizadas

- **Interface:** Gradio
- **IA:** Google Gemini 1.5 Pro
- **Embeddings:** BERT em Português (neuralmind/bert-base-portuguese-cased)
- **PDF Processing:** PyPDF2, pdf2image, pytesseract
- **RAG:** sentence-transformers, scikit-learn

## 📖 Como Usar

### 1. Configure a API Key do Gemini

Você precisa de uma API Key do Google Gemini. Configure como secret no Hugging Face Spaces:

```
Nome: GEMINI_API_KEY
Valor: sua-api-key-aqui
```

[Como obter uma API Key do Gemini](https://ai.google.dev/)

### 2. Upload dos Autos

Faça upload dos PDFs dos autos processuais. O sistema suporta:
- PDFs nativos (texto selecionável)
- PDFs digitalizados (será aplicado OCR)
- Múltiplos arquivos

### 3. Descreva a Tarefa

Indique qual decisão você deseja elaborar:
- "Elaborar decisão de recebimento da denúncia"
- "Analisar pedido de liberdade provisória"
- "Decisão sobre absolvição sumária"
- etc.

### 4. Adicione Contexto (Opcional)

Forneça informações adicionais relevantes ao caso.

### 5. Processar

Clique em "Processar" e aguarde. O sistema irá:
1. Extrair texto dos PDFs
2. Buscar minutas relevantes
3. Analisar os autos
4. Gerar a decisão fundamentada

## ⚠️ Aviso Legal

**IMPORTANTE:** Este sistema é uma ferramenta de apoio à elaboração de decisões judiciais. Todas as decisões geradas devem ser **cuidadosamente revisadas** por um magistrado antes de serem publicadas.

O sistema:
- ✅ Auxilia na elaboração
- ✅ Sugere fundamentação
- ✅ Mantém uniformidade de estilo
- ❌ NÃO substitui a análise jurídica humana
- ❌ NÃO deve ser usado sem revisão

## 📄 Licença e Créditos

- **Repositório de Minutas:** [decisoes-vara-criminal](https://github.com/HugoDiasdSi/decisoes-vara-criminal)
- **Desenvolvido para:** Varas Criminais de Pernambuco

## 🤝 Contribuições

Este projeto é de código aberto. Contribuições são bem-vindas via Pull Request no repositório GitHub.

## 📞 Suporte

Para dúvidas ou sugestões, abra uma issue no repositório GitHub.

---

**Versão:** 1.0.0
**Última Atualização:** Novembro 2025
