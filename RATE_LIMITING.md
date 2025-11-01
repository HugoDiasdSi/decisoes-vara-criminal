# 📊 Rate Limiting - Gemini Tier Free

## Limites da API Gemini 2.0 Flash (Tier Free)

O aplicativo está configurado para usar o **Gemini 2.0 Flash** no tier gratuito, que possui os seguintes limites:

- **RPM (Requests Per Minute):** 15 requisições por minuto
- **TPM (Tokens Per Minute):** 1.000.000 tokens por minuto
- **RPD (Requests Per Day):** 1.500 requisições por dia

### Configuração Conservadora

Para garantir estabilidade, o aplicativo está configurado com **125 TPM** (mais conservador que o limite oficial).

Isso significa que:
- ✅ O sistema **nunca excederá** o limite da API
- ✅ Haverá **retry automático** em caso de erro 429 (rate limit)
- ⏳ Pode haver **tempo de espera** entre requisições
- 📊 O sistema **estima tokens** antes de fazer requisições

## Como Funciona

### 1. Estimativa de Tokens

Antes de enviar uma requisição, o sistema:
1. Estima o número de tokens no prompt
2. Verifica se há "saldo" disponível na janela de 60 segundos
3. Aguarda se necessário

```python
# Exemplo de estimativa
prompt = "texto muito longo..."
estimated_tokens = rate_limiter.estimate_tokens(prompt)
# Output: ~5000 tokens
```

### 2. Otimização Automática

Se o prompt for muito grande (>30.000 tokens):
1. Sistema trunca minutas em 3.000 caracteres
2. Limita autos em 15.000 caracteres
3. Re-estima tokens
4. Procede com prompt otimizado

### 3. Retry com Backoff Exponencial

Se mesmo assim houver erro de rate limit:
1. **Tentativa 1:** Aguarda 1 segundo
2. **Tentativa 2:** Aguarda 2 segundos
3. **Tentativa 3:** Aguarda 4 segundos
4. Se falhar 3 vezes, retorna erro ao usuário

## Tempo Estimado de Processamento

### Caso Simples (1 PDF pequeno)
- Extração: ~5-10 segundos
- RAG: ~2-3 segundos
- Gemini: ~10-30 segundos
- **Total: ~20-45 segundos**

### Caso Médio (2-3 PDFs)
- Extração: ~15-30 segundos
- RAG: ~3-5 segundos
- Gemini: ~30-60 segundos
- **Total: ~50-95 segundos**

### Caso Grande (5+ PDFs ou PDFs grandes)
- Extração: ~1-2 minutos (com OCR)
- RAG: ~5-10 segundos
- Otimização: ~5-10 segundos
- Gemini: ~60-120 segundos
- **Total: ~2-4 minutos**

## Melhorando Performance

### Para Usuários

1. **Use PDFs menores:** Divida autos muito grandes
2. **Minimize contexto:** Seja específico na tarefa
3. **Evite múltiplas requisições simultâneas:** Aguarde uma terminar
4. **Otimize PDFs:** Use PDFs nativos (não digitalizados) quando possível

### Para Deploy

Se você tiver um projeto com mais demanda, considere:

#### 1. Upgrade para Tier Pago

```python
# Em utils/rate_limiter.py, altere:
rate_limiter = RateLimiter(tokens_per_minute=125)
# Para:
rate_limiter = RateLimiter(tokens_per_minute=10000)  # Tier pago
```

#### 2. Usar Modelo Maior

```python
# Em app.py, altere:
model = genai.GenerativeModel('gemini-2.0-flash-exp')
# Para:
model = genai.GenerativeModel('gemini-1.5-pro')  # Mais potente
```

#### 3. Cache de Respostas

Implementar cache para evitar reprocessar os mesmos documentos.

## Monitoramento

### Status do Rate Limiter

```python
status = rate_limiter.get_status()
print(status)
# {
#   'tokens_used': 5000,
#   'tokens_remaining': 120000,
#   'time_until_reset': 35.2,
#   'tpm_limit': 125000
# }
```

### Logs de Requisições

O sistema imprime logs quando:
- ⏳ Aguardando rate limit
- ⚠️ Tentando novamente após erro
- 📊 Otimizando prompt grande

## Troubleshooting

### "Rate limit atingido. Aguardando..."

**Normal!** O sistema está respeitando os limites da API. Aguarde.

### "Erro 429: Quota exceeded"

1. Verifique se a API Key é válida
2. Aguarde alguns minutos
3. Tente novamente com um PDF menor

### Processamento muito lento

1. **Verifique tamanho do PDF:** PDFs grandes levam mais tempo
2. **OCR:** PDFs digitalizados são mais lentos
3. **Tier Free:** Considere upgrade se uso for frequente

## Referências

- [Gemini API Limits](https://ai.google.dev/pricing)
- [Rate Limiting Best Practices](https://cloud.google.com/apis/design/rate_limiting)

---

**Resumo:** O sistema está otimizado para tier free e funciona bem para uso
individual. Para uso em produção com alto volume, considere upgrade para tier pago.
