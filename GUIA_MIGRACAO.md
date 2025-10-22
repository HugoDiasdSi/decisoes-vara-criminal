# Guia de Migração - Versão Antiga → Nova

Este documento explica as diferenças entre as versões e como migrar.

## 📊 Resumo das Mudanças

### O que mudou?

| Componente | Antes | Depois |
|------------|-------|---------|
| Prompts | Hardcoded no Python | Arquivos `.md` em `/prompts/` |
| Configuração | Espalhada no código | Centralizada em `config.json` |
| Estrutura | 1 arquivo Python monolítico | Código orientado a objetos |
| Manutenção | Editar código Python | Editar arquivos Markdown |
| Logging | `print()` | `logging` module |
| Erros | Tratamento genérico | Tratamento específico |

## 🔄 Passo a Passo da Migração

### 1. Estrutura de Arquivos

**ANTES:**
```
projeto/
├── app.py (tudo em um arquivo)
└── base_conhecimento/
```

**DEPOIS:**
```
projeto/
├── app_refatorado.py
├── config.json
├── requirements.txt
├── .gitignore
├── README_APP.md
├── prompts/
│   ├── extracao_flash.md
│   ├── assessor_juridico.md
│   ├── elaborar_sentenca.md
│   └── formato_saida_duplo.md
├── base_conhecimento/
└── modelos_estilo/
```

### 2. Migração dos Prompts

#### ANTES (app.py):
```python
PROMPT_EXTRACAO_FLASH = """
Adote como persona experiente analista judiciário...
# (COLE AQUI SEU PROMPT DE EXTRAÇÃO COMPLETO PARA O FLASH)
"""

PROMPT_ASSESSOR_JURIDICO = """
Você atuará como **assessor jurídico de magistrado criminal brasileiro**...
# (COLE AQUI SEU PROMPT COMPLETO PARA MINUTAS/DECISÕES)
"""
```

#### DEPOIS:
1. Copie o conteúdo de `PROMPT_EXTRACAO_FLASH` para `prompts/extracao_flash.md`
2. Copie `PROMPT_ASSESSOR_JURIDICO` para `prompts/assessor_juridico.md`
3. Copie `PROMPT_ELABORAR_SENTENCA` para `prompts/elaborar_sentenca.md`

### 3. Configuração

Crie `config.json` com suas preferências:

```json
{
  "repository": {
    "url": "https://github.com/HugoDiasdSi/decisoes-vara-criminal.git",
    "local_dir": "decisoes-vara-criminal"
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

### 4. Executar Nova Versão

```bash
# Versão antiga
python app.py

# Versão nova
python app_refatorado.py
```

## ✨ Vantagens da Nova Versão

### 1. **Edição Fácil de Prompts**

**ANTES:** Tinha que editar código Python
```python
PROMPT = """meu prompt aqui"""  # Arriscado!
```

**DEPOIS:** Apenas edite arquivos Markdown
```markdown
# Arquivo: prompts/assessor_juridico.md
Você atuará como assessor jurídico...
```

### 2. **Configuração Centralizada**

**ANTES:** Valores espalhados
```python
REPO_DIR = "decisoes-vara-criminal"  # Linha 50
flash_model = genai.GenerativeModel('models/gemini-flash-lite-latest')  # Linha 120
timeout = 600  # Linha 200
```

**DEPOIS:** Tudo em um lugar
```json
{
  "repository": {"local_dir": "decisoes-vara-criminal"},
  "models": {"flash": "models/gemini-flash-lite-latest"},
  "generation_config": {"pro": {"timeout": 600}}
}
```

### 3. **Código Organizado**

**ANTES:** Função gigante
```python
def analisar_processo(...):
    # 150+ linhas de código
    # Difícil de entender e manter
```

**DEPOIS:** Métodos pequenos e focados
```python
class AssessorJuridicoApp:
    def _extract_with_flash(self, pdf_file):
        # Apenas extração

    def _build_prompt_for_pro(self, ...):
        # Apenas construção de prompt

    def _generate_with_pro(self, ...):
        # Apenas geração
```

### 4. **Melhor Debugging**

**ANTES:**
```python
print("Iniciando...")
print(f"Erro: {e}")
```

**DEPOIS:**
```python
logger.info("Extração com Flash concluída")
logger.error(f"Erro na geração: {e}")
logger.warning("Arquivo não encontrado")
```

## 🎯 Casos de Uso

### Caso 1: Editar Prompt de Extração

**Versão Antiga:**
1. Abrir `app.py`
2. Procurar `PROMPT_EXTRACAO_FLASH`
3. Editar texto no meio do código Python
4. Cuidado para não quebrar as aspas/formatação
5. Reiniciar app

**Versão Nova:**
1. Abrir `prompts/extracao_flash.md`
2. Editar em Markdown (mais fácil!)
3. Salvar
4. Reiniciar app

### Caso 2: Mudar Timeout do Gemini Pro

**Versão Antiga:**
1. Procurar no código onde está `timeout`
2. Editar a linha de código
3. Torcer para não quebrar nada

**Versão Nova:**
1. Abrir `config.json`
2. Alterar `"timeout": 600` para `"timeout": 900`
3. Salvar

### Caso 3: Adicionar Novo Modelo de Estilo

**Versão Antiga:**
- Não tinha estrutura definida
- Tinha que modificar código

**Versão Nova:**
1. Copiar arquivo `.md` da decisão para `modelos_estilo/`
2. Pronto! O sistema carrega automaticamente

## 🔧 Personalizações Comuns

### Mudar Modelo do Gemini

Edite `config.json`:
```json
{
  "models": {
    "flash": "models/gemini-flash-2.0",  // ← Mude aqui
    "pro": "models/gemini-pro-latest"     // ← Ou aqui
  }
}
```

### Ajustar Temperature

```json
{
  "generation_config": {
    "flash": {
      "temperature": 0.2  // ← Aumenta criatividade
    }
  }
}
```

### Personalizar Interface

```json
{
  "ui": {
    "title": "Meu Assessor Jurídico ⚖️",
    "theme": "soft"  // ou "default", "glass", "monochrome"
  }
}
```

## ⚠️ Atenção ao Migrar

### ✅ FAZER:
- Mantenha backup da versão antiga
- Teste a nova versão antes de usar em produção
- Revise os prompts migrados
- Configure corretamente a API key

### ❌ NÃO FAZER:
- Apagar versão antiga antes de testar nova
- Misturar código das duas versões
- Esquecer de configurar `GOOGLE_API_KEY`

## 🆘 Problemas Comuns

### "Prompt não encontrado"
**Causa:** Arquivo `.md` no lugar errado ou nome incorreto

**Solução:**
1. Verifique se o arquivo está em `prompts/`
2. Verifique nome no `config.json`
3. Verifique se o caminho está correto

### "GOOGLE_API_KEY não encontrada"
**Causa:** Variável de ambiente não configurada

**Solução:**
```bash
export GOOGLE_API_KEY="sua-chave-aqui"
```

### "Erro ao carregar config.json"
**Causa:** JSON mal formatado

**Solução:**
1. Valide o JSON em https://jsonlint.com/
2. Verifique vírgulas, chaves, aspas

## 📈 Comparação de Performance

| Métrica | Versão Antiga | Versão Nova |
|---------|---------------|-------------|
| Tempo de inicialização | ~2s | ~2s (igual) |
| Uso de memória | ~150MB | ~150MB (igual) |
| Velocidade de resposta | Igual | Igual |
| **Facilidade de manutenção** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Facilidade de customização** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Organização do código** | ⭐⭐ | ⭐⭐⭐⭐⭐ |

## 🎓 Próximos Passos

Depois de migrar:

1. **Personalize os prompts** - Ajuste para seu estilo
2. **Adicione modelos de estilo** - Coloque suas decisões anteriores
3. **Configure atalhos** - Crie configurações pré-definidas
4. **Contribua** - Compartilhe melhorias com a comunidade

## 📞 Precisa de Ajuda?

- 📖 Leia o [README_APP.md](README_APP.md)
- 🐛 Abra uma [Issue no GitHub](https://github.com/HugoDiasdSi/decisoes-vara-criminal/issues)
- 💬 Entre em contato com o desenvolvedor

---

**Boa migração! 🚀**
