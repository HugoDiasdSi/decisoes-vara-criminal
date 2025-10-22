# 🚀 Como Fazer Deploy no Hugging Face Spaces

Guia passo a passo para colocar o Assessor Jurídico Virtual no ar.

---

## 📋 Pré-requisitos

1. ✅ Conta no [Hugging Face](https://huggingface.co/)
2. ✅ Chave de API do Google Gemini ([obter aqui](https://ai.google.dev/))
3. ✅ Git instalado (para método 2)

---

## 🎯 Método 1: Interface Web (Mais Fácil)

### Passo 1: Criar um Space

1. Acesse [huggingface.co/spaces](https://huggingface.co/spaces)
2. Clique em **"Create new Space"**
3. Preencha:
   - **Space name**: `assessor-juridico-virtual` (ou seu nome preferido)
   - **License**: MIT
   - **Select the Space SDK**: **Gradio**
   - **Space hardware**: CPU basic (gratuito) - suficiente para este projeto
4. Marque **"Private"** se quiser que seja privado
5. Clique em **"Create Space"**

### Passo 2: Adicionar a API Key

1. No seu Space, vá em **"Settings"** (ícone de engrenagem)
2. Role até **"Repository secrets"**
3. Clique em **"New secret"**
4. Adicione:
   - **Name**: `GOOGLE_API_KEY`
   - **Value**: `sua-chave-da-api-do-google-gemini`
5. Clique em **"Add secret"**

### Passo 3: Upload dos Arquivos

Há duas formas:

#### Opção A: Upload Direto pela Interface

1. Volte à aba **"Files"** do seu Space
2. Clique em **"Add file"** → **"Upload files"**
3. Faça upload dos seguintes arquivos/pastas:

**Arquivos principais:**
```
app.py                    # ⭐ Arquivo principal
config.json               # Configurações
requirements.txt          # Dependências
README.md                 # Renomeie README_HUGGINGFACE.md para README.md
```

**Pastas (faça upload dos conteúdos):**
```
prompts/
├── extracao_flash.md
├── assessor_juridico.md
├── elaborar_sentenca.md
└── formato_saida_duplo.md

base_conhecimento/
├── TEMPLATE.md
├── Dosimetria RAG.md
├── Agente RAG.md
├── ANTI-dupla punição pelo mesmo fato na dosimetria da pena.md
└── Orientações para a base de conhecimento.md

modelos_estilo/
└── (suas decisões de exemplo, se tiver)
```

4. Clique em **"Commit changes to main"**

#### Opção B: Usar o Editor do HuggingFace

1. Na aba **"Files"**, clique em **"Edit repository"**
2. Crie os arquivos manualmente:
   - Clique em **"New file"**
   - Cole o conteúdo
   - Commit

### Passo 4: Aguardar o Build

1. Vá para a aba **"App"**
2. Aguarde o build (pode levar 2-5 minutos)
3. Você verá logs de instalação das dependências
4. Quando aparecer "Running on...", está pronto! 🎉

---

## 🎯 Método 2: Git (Para Desenvolvedores)

### Passo 1: Clonar o Space

```bash
# Clone o repositório do Space (substitua com seu username e space name)
git clone https://huggingface.co/spaces/seu-usuario/assessor-juridico-virtual
cd assessor-juridico-virtual
```

### Passo 2: Copiar os Arquivos

```bash
# Copie os arquivos do projeto para a pasta do Space
cp /caminho/para/decisoes-vara-criminal/app.py .
cp /caminho/para/decisoes-vara-criminal/config.json .
cp /caminho/para/decisoes-vara-criminal/requirements.txt .
cp /caminho/para/decisoes-vara-criminal/README_HUGGINGFACE.md README.md

# Copie as pastas
cp -r /caminho/para/decisoes-vara-criminal/prompts .
cp -r /caminho/para/decisoes-vara-criminal/base_conhecimento .
cp -r /caminho/para/decisoes-vara-criminal/modelos_estilo .
```

### Passo 3: Commit e Push

```bash
git add .
git commit -m "Deploy inicial do Assessor Jurídico Virtual"
git push
```

### Passo 4: Adicionar API Key

1. Vá para as configurações do Space
2. Adicione o secret `GOOGLE_API_KEY` como no Método 1

---

## 📁 Estrutura Final no Hugging Face

```
seu-space/
├── app.py                          # ⭐ Arquivo principal
├── config.json                     # Configurações
├── requirements.txt                # Dependências
├── README.md                       # Documentação do Space
│
├── prompts/                        # Prompts da IA
│   ├── extracao_flash.md
│   ├── assessor_juridico.md
│   ├── elaborar_sentenca.md
│   └── formato_saida_duplo.md
│
├── base_conhecimento/              # Base jurídica
│   ├── TEMPLATE.md
│   ├── Dosimetria RAG.md
│   ├── Agente RAG.md
│   ├── ANTI-dupla punição...md
│   └── Orientações...md
│
└── modelos_estilo/                 # (opcional)
    └── suas_decisoes.md
```

---

## ✅ Checklist Pré-Deploy

Antes de fazer o deploy, verifique:

- [ ] Arquivo `app.py` está presente
- [ ] Arquivo `config.json` está presente
- [ ] Arquivo `requirements.txt` está presente
- [ ] Arquivo `README.md` (renomeado de README_HUGGINGFACE.md)
- [ ] Pasta `prompts/` com 4 arquivos .md
- [ ] Pasta `base_conhecimento/` com 5 arquivos .md
- [ ] Pasta `modelos_estilo/` (pode estar vazia)
- [ ] Secret `GOOGLE_API_KEY` configurado no Space
- [ ] Chave de API do Google Gemini válida

---

## 🔧 Configurações Importantes

### requirements.txt

Verifique se contém:
```
google-generativeai>=0.3.0
gradio>=4.0.0
```

### config.json

Certifique-se de que os caminhos estão corretos:
```json
{
  "prompts": {
    "extracao_flash": "prompts/extracao_flash.md",
    ...
  },
  "base_conhecimento": {
    "template": "base_conhecimento/TEMPLATE.md",
    ...
  }
}
```

### README.md

Renomeie `README_HUGGINGFACE.md` para `README.md` no Space.

O cabeçalho YAML é importante:
```yaml
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
```

---

## 🐛 Problemas Comuns

### 1. "Error loading prompt"

**Causa:** Arquivos de prompt não foram encontrados.

**Solução:**
- Verifique se a pasta `prompts/` existe
- Verifique se os arquivos .md estão dentro dela
- Confira os nomes no `config.json`

### 2. "GOOGLE_API_KEY not found"

**Causa:** Secret não foi configurado.

**Solução:**
- Vá em Settings → Repository secrets
- Adicione `GOOGLE_API_KEY` com sua chave

### 3. Build falha com "Module not found"

**Causa:** `requirements.txt` incorreto ou ausente.

**Solução:**
- Verifique se `requirements.txt` existe
- Conteúdo mínimo:
  ```
  google-generativeai>=0.3.0
  gradio>=4.0.0
  ```

### 4. "App is running but not responding"

**Causa:** Erro na API key ou timeout.

**Solução:**
- Verifique os logs na aba "Logs"
- Teste a API key em outro ambiente
- Verifique se há quota disponível no Google AI Studio

### 5. "Base de conhecimento não encontrada"

**Causa:** Pasta `base_conhecimento/` não foi enviada.

**Solução:**
- Faça upload de todos os arquivos .md da base de conhecimento
- Verifique os nomes dos arquivos no `config.json`

---

## 📊 Monitoramento

### Logs

Acesse a aba **"Logs"** do seu Space para ver:
- Inicialização da app
- Carregamento de prompts e base de conhecimento
- Erros (se houver)

### Uso

O Space gratuito tem limitações:
- **CPU basic**: Suficiente para a maioria dos casos
- **Timeout**: 60 segundos (pode ser problema para PDFs muito grandes)
- **Uptime**: Dorme após inatividade

Se precisar de mais recursos:
- Considere upgrade para CPU enhanced ($5/mês)
- Ou GPU para processamento mais rápido

---

## 🔄 Atualizações

Para atualizar o Space depois de implantado:

### Via Interface Web:
1. Vá em "Files"
2. Clique no arquivo que quer editar
3. Faça as mudanças
4. Commit

### Via Git:
```bash
cd seu-space/
# Faça mudanças nos arquivos
git add .
git commit -m "Atualização: descrição das mudanças"
git push
```

O Space fará rebuild automaticamente.

---

## 🎉 Pronto!

Seu Assessor Jurídico Virtual está no ar!

**URL do Space:** `https://huggingface.co/spaces/seu-usuario/assessor-juridico-virtual`

Compartilhe com colegas magistrados! 🚀⚖️

---

## 📞 Suporte

- **Documentação HF Spaces**: https://huggingface.co/docs/hub/spaces
- **Issues do Projeto**: https://github.com/HugoDiasdSi/decisoes-vara-criminal/issues
- **Discord do HuggingFace**: https://hf.co/join/discord

---

## 🌟 Próximos Passos

Depois do deploy:

1. **Teste exaustivamente** com casos reais
2. **Ajuste os prompts** conforme necessário
3. **Adicione modelos de estilo** (suas decisões anteriores)
4. **Compartilhe feedback** via GitHub Issues
5. **Contribua** com melhorias ao projeto

**Bom deploy! 🚀**
