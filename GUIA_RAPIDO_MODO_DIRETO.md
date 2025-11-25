# 🚀 Guia Rápido - Modo Direto (PDF → Decisão)

## O que é?

Uma versão **ultra-simplificada** do Gem que funciona assim:

```
1. Você anexa PDFs
2. O Gem gera a decisão
3. Pronto.
```

**Sem templates complicados. Sem preencher formulários. Sem perguntas.**

---

## Como Configurar (2 minutos)

### 1. Criar o Gem
```
1. Acesse: gemini.google.com
2. Clique: "Gems" > "Criar novo Gem"
3. Nome: "Decisões Criminais - Direto"
4. Cole: TODO o arquivo GEM_INSTRUCOES_SIMPLES_PDF_DIRETO.md
5. Salve
```

### 2. Pronto!
Seu Gem está configurado. Agora pode usar.

---

## Como Usar (3 passos)

### Opção A - Mínima (só PDFs)
```
1. Abra o Gem
2. Anexe PDFs do processo
3. [Gem gera decisão automaticamente]
```

### Opção B - Com contexto
```
1. Abra o Gem
2. Anexe PDFs + escreva "Gerar decisão de recebimento de denúncia"
3. [Gem gera decisão do tipo especificado]
```

### Opção C - Com estilo
```
1. Abra o Gem
2. Anexe PDFs do processo
3. Anexe 1-3 minutas (.md) do repositório (referência de estilo)
4. Escreva: "Seguir estilo das minutas"
5. [Gem gera decisão no estilo das minutas]
```

---

## Exemplos Práticos

### Exemplo 1: Básico
```
[Usuário anexa: denuncia.pdf, certidao_antecedentes.pdf]

Gem:
📊 ANÁLISE AUTOMÁTICA
Processo: 0012345-67.2025.8.17.0001
Fase: Denúncia oferecida, aguardando recebimento
Ato Pendente: Recebimento da denúncia
Réu: José Silva - PRESO desde 1º/11/2024

⚖️ DECISÃO
[decisão completa gerada...]

⚠️ Para finalizar, qual o nome do juiz para assinatura?

[Usuário: "Dr. João Santos"]

[Gem atualiza a assinatura e apresenta decisão final]
```

### Exemplo 2: Com Minutas
```
[Usuário anexa: processo.pdf + RECEBIMENTO_DENUNCIA.md]

Gem:
📊 Minuta de referência detectada: RECEBIMENTO_DENUNCIA.md
Seguindo estilo identificado...

⚖️ DECISÃO
[decisão no estilo da minuta fornecida...]
```

### Exemplo 3: Específico
```
[Usuário anexa PDFs + escreve: "Elaborar decisão de liberdade provisória"]

Gem:
📊 Tipo de decisão: Liberdade provisória
Analisando requisitos do art. 312 CPP...

⚖️ DECISÃO
[decisão sobre liberdade provisória...]
```

---

## O que o Gem faz AUTOMATICAMENTE

### ✅ Extrai sozinho:
- IDs de todos os documentos
- Nomes das partes
- Fatos da denúncia
- Fase processual atual
- Situação prisional
- Teses da defesa
- Pedidos do MP

### ✅ Identifica sozinho:
- Qual tipo de decisão é necessária
- Se há réu preso > 90 dias (aplica art. 316 automaticamente)
- Se há prova ilícita
- Se é competência da vara
- Se há urgência

### ✅ Gera sozinho:
- Decisão completa (Relatório + Fundamentação + Dispositivo)
- Formatação correta (sem bullets, sem latim, datas corretas)
- Citações de IDs
- Comandos claros

### ⚠️ Só pergunta se for ESSENCIAL:
- Nome do juiz (se não estiver nos autos)
- Localidade (Recife ou Camaragibe)
- Tipo de decisão (se realmente ambíguo)

---

## Informações Opcionais (melhoram o resultado)

Você PODE fornecer, mas não é obrigatório:

### 1. Nome do Juiz
```
Anexe PDFs + "Juiz: Dr. João Santos"
```

### 2. Localidade
```
Anexe PDFs + "Vara: Camaragibe/PE"
```

### 3. Tipo Específico de Decisão
```
Anexe PDFs + "Elaborar sentença absolutória"
```

### 4. Minutas de Referência (estilo)
```
Anexe: processo.pdf + minuta_modelo.md
```

### 5. Jurisprudência Aplicável
```
Anexe PDFs + cole: "Aplicar Súmula 52 do STJ: [texto]"
```

**Mas lembre-se: O Gem funciona MESMO SEM isso tudo.**

---

## Ajustes Iterativos

Depois de receber a decisão, você pode ajustar:

```
"Reduza o relatório para 2 parágrafos"
"Desenvolva mais a fundamentação sobre X"
"O réu é primário, não reincidente - corrija"
"Adicione menção à súmula Y"
"Remova o trecho Z"
"Refaça o dispositivo de forma mais direta"
```

O Gem ajusta sem perder o contexto.

---

## Comparação: Modo Completo vs Modo Direto

| Aspecto | Modo Completo | Modo Direto |
|---------|--------------|-------------|
| **Template** | Requer preencher | Não precisa |
| **Minutas** | Recomenda 3 | Opcional |
| **Perguntas** | Várias para confirmação | Mínimas |
| **Autonomia** | Média | Máxima |
| **Velocidade** | Média | Rápida |
| **Controle** | Alto | Médio |
| **Complexidade** | Média | Baixa |

**Escolha**:
- **Modo Completo** se você quer controle total
- **Modo Direto** se você quer velocidade

---

## Solução de Problemas

### "O Gem está perguntando muita coisa"
→ Forneça logo no início: nome do juiz + localidade

### "Não identificou o tipo de decisão"
→ Seja explícito: "Elaborar [tipo de decisão]"

### "Estilo diferente do que eu queria"
→ Anexe 2-3 minutas de referência junto com o PDF

### "Esqueceu informação do PDF"
→ PDFs muito grandes? Destaque: "Atenção para o documento ID XXXXX"

### "Usou latim / bullets / formatação errada"
→ Peça: "Corrigir formatação conforme regras"

---

## Fluxo Visual

```
┌─────────────────┐
│  Anexar PDFs    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Gem Analisa     │ ← Automático
│ Automaticamente │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Identifica Tipo │ ← Automático
│ de Decisão      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Gera Decisão    │ ← Automático
│ Completa        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Você Revisa     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Ajustes?        │
├─────────────────┤
│ Sim → Iterar    │
│ Não → Assinar   │
└─────────────────┘
```

---

## Checklist Rápido

Antes de usar a decisão:

- [ ] Nomes corretos?
- [ ] Datas corretas?
- [ ] IDs citados?
- [ ] Sem bullets/numeração?
- [ ] Sem latim?
- [ ] Fundamentação coerente?
- [ ] Dispositivo claro?
- [ ] Nome do juiz e localidade?

---

## Dica de Ouro 💡

**Para melhor resultado na primeira tentativa:**

```
[Anexar todos os PDFs do processo]
+ [Anexar 1 minuta de referência .md]
+ [Escrever]: "Elaborar [tipo de decisão]. Juiz: [nome]. Vara: [localidade]"
```

Pronto! Decisão completa e no estilo certo de primeira.

---

## Quando Usar Cada Modo

### Use MODO DIRETO se:
- ✅ Você quer velocidade
- ✅ O caso é relativamente padrão
- ✅ Você está confortável revisando e ajustando
- ✅ Quer fluxo de trabalho ágil

### Use MODO COMPLETO se:
- ✅ O caso é muito complexo
- ✅ Você quer controle total sobre cada etapa
- ✅ Precisa documentar o raciocínio passo a passo
- ✅ Quer verificação detalhada antes de gerar

**Você pode ter AMBOS os Gems criados e usar conforme o caso!**

---

## Arquivo a Usar

**Para criar este Gem, use:**
```
GEM_INSTRUCOES_SIMPLES_PDF_DIRETO.md
```

**Tamanho**: ~10KB (mais curto que o modo completo)

---

## Início Rápido (30 segundos)

1. gemini.google.com
2. Gems > Criar
3. Colar: `GEM_INSTRUCOES_SIMPLES_PDF_DIRETO.md`
4. Salvar
5. Anexar PDFs
6. **Pronto!**

---

**Modo Direto = Máxima Simplicidade + Máxima Velocidade**

🚀 Anexe PDF → 📄 Receba Decisão
