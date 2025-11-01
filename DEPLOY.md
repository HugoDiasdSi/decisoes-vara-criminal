# 🚀 Deploy no Hugging Face Spaces

Este guia explica como fazer o deploy do Assessor Jurídico Criminal no Hugging Face Spaces.

## Pré-requisitos

1. Conta no [Hugging Face](https://huggingface.co/)
2. API Key do Google Gemini ([obter aqui](https://ai.google.dev/))
3. Git instalado localmente

## Passo a Passo

### 1. Criar um novo Space

1. Acesse https://huggingface.co/new-space
2. Preencha as informações:
   - **Owner:** Seu usuário ou organização
   - **Space name:** `assessor-juridico-criminal` (ou nome de sua escolha)
   - **License:** Apache 2.0 (ou outra de sua preferência)
   - **SDK:** Gradio
   - **SDK version:** 4.19.2
   - **Visibility:** Public ou Private

3. Clique em "Create Space"

### 2. Clonar o Space localmente

```bash
# Clone o space vazio
git clone https://huggingface.co/spaces/SEU_USUARIO/assessor-juridico-criminal
cd assessor-juridico-criminal

# Adicione o repositório remoto do projeto
git remote add origin https://github.com/HugoDiasdSi/decisoes-vara-criminal.git

# Faça pull dos arquivos
git pull origin main
```

### 3. Configurar Secrets

No Hugging Face Spaces, vá em **Settings** → **Repository secrets** e adicione:

- **Nome:** `GEMINI_API_KEY`
- **Valor:** Sua API Key do Google Gemini

### 4. Estrutura de Arquivos

Certifique-se de que os seguintes arquivos estão presentes:

```
.
├── app.py                      # Aplicativo principal
├── requirements.txt            # Dependências Python
├── packages.txt               # Dependências do sistema
├── README_APP.md              # Documentação do app
├── minutas_metadata.json      # Metadados das minutas
├── *.md                       # Todas as minutas
└── utils/
    ├── __init__.py
    ├── pdf_extractor.py
    ├── prompt_builder.py
    └── rag_system.py
```

### 5. Fazer Push para o Hugging Face

```bash
# Adicionar todos os arquivos
git add .

# Commit
git commit -m "Deploy inicial do Assessor Jurídico Criminal"

# Push para o Hugging Face Space
git push
```

### 6. Aguardar Build

O Hugging Face irá automaticamente:
1. Instalar as dependências do `requirements.txt`
2. Instalar pacotes do sistema do `packages.txt`
3. Executar o `app.py`
4. Disponibilizar a interface web

O build pode levar de 5 a 10 minutos.

### 7. Testar o Aplicativo

Após o build, o app estará disponível em:
```
https://huggingface.co/spaces/SEU_USUARIO/assessor-juridico-criminal
```

## Configurações Adicionais

### Aumentar Recursos (Hardware)

Se o aplicativo estiver lento, você pode:

1. Ir em **Settings** → **Resource**
2. Selecionar um hardware melhor (pode ter custo)
   - CPU Upgrade
   - GPU (para processamento mais rápido)

### Definir Timeout

Para processos longos, aumente o timeout:

1. Crie um arquivo `config.yaml`:

```yaml
timeout: 3600  # 1 hora em segundos
```

### Adicionar Persistência

Para cachear modelos e evitar downloads repetidos:

1. Em **Settings** → **Repository secrets**, adicione:
   - `HF_HOME=/data/.cache/huggingface`

2. No código, os modelos serão baixados apenas uma vez

## Troubleshooting

### Erro: "GEMINI_API_KEY not found"

**Solução:** Verifique se a secret foi configurada corretamente em Settings → Repository secrets.

### Erro: "tesseract not found"

**Solução:** Certifique-se de que o arquivo `packages.txt` contém:
```
tesseract-ocr
tesseract-ocr-por
poppler-utils
```

### Build muito lento

**Solução:**
1. Considere usar GPU hardware
2. Reduza o tamanho do modelo de embeddings
3. Otimize o `requirements.txt` removendo dependências não utilizadas

### Timeout durante processamento

**Solução:**
1. Aumente o timeout no `config.yaml`
2. Processe PDFs menores ou em lotes
3. Use hardware mais potente

## Atualizações

Para atualizar o aplicativo:

```bash
# Fazer alterações nos arquivos
git add .
git commit -m "Descrição da atualização"
git push
```

O Hugging Face irá automaticamente rebuildar o Space.

## Monitoramento

- **Logs:** Disponíveis em Settings → Logs
- **Métricas:** Settings → Analytics
- **Versões:** Settings → Files and versions

## Custos

- **Spaces gratuitos:** CPU básico, pode ter fila de espera
- **Spaces pagos:** Hardware dedicado, sem fila
- **Veja preços:** https://huggingface.co/pricing#spaces

## Suporte

- Documentação oficial: https://huggingface.co/docs/hub/spaces
- Community: https://discuss.huggingface.co/
- Issues do projeto: GitHub

---

**Boa sorte com o deploy! 🚀**
