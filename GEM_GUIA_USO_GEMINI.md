# Guia de Uso - Gem Assessor Jurídico para Gemini 3.0 Pro

## O que é este Gem?

Este é um assistente especializado para elaboração de decisões judiciais criminais, configurado como um **Gem** do Google Gemini 3.0 Pro.

## Como Configurar o Gem

### 1. Acesse o Gemini
- Vá para [gemini.google.com](https://gemini.google.com)
- Faça login com sua conta Google

### 2. Crie um Novo Gem
- Clique no ícone de **"Gems"** (menu lateral ou superior)
- Clique em **"Criar novo Gem"**
- Dê um nome: **"Assessor Jurídico Criminal"**

### 3. Cole as Instruções
- No campo de instruções do Gem, cole todo o conteúdo do arquivo `GEM_INSTRUCOES_GEMINI.md`
- O Gemini 3.0 Pro suporta instruções longas, então pode colar tudo

### 4. Configure Parâmetros (Opcional)
- **Temperatura**: 0.3-0.5 (para respostas mais consistentes e técnicas)
- **Contexto**: Longo (o Gemini 3.0 Pro tem janela de até 2 milhões de tokens)

### 5. Salve o Gem
- Clique em **"Salvar"**
- Seu Gem estará disponível na lista de Gems

## Como Usar o Gem

### Estrutura de Consulta Recomendada

Para obter melhores resultados, estruture sua consulta assim:

```
CASO: [Nome/número do processo]

FASE PROCESSUAL: [Ex: Recebimento da denúncia, Resposta à acusação, etc.]

DOCUMENTOS DO PROCESSO:

[Cole aqui o conteúdo extraído dos PDFs, incluindo:]
- Denúncia (com ID)
- Despachos anteriores
- Manifestações das partes
- Laudos periciais
- Certidões
- Qualquer outra peça relevante

MINUTAS DISPONÍVEIS (CATÁLOGO):

[Cole o conteúdo do arquivo minutas_metadata.json, OU indique as minutas mais relevantes]

MINUTAS SELECIONADAS (Conteúdo Completo):

[Cole o conteúdo completo das 3 minutas mais relevantes do repositório]

JURISPRUDÊNCIA/SÚMULAS APLICÁVEIS:

[Cole apenas jurisprudência e súmulas que você já pesquisou e quer que sejam consideradas]

PEDIDO:

Elaborar [tipo de decisão] considerando [orientações específicas se houver]
```

### Exemplo de Consulta Simplificada

Se você não quiser fornecer tudo de uma vez:

```
CASO: Processo 0012345-67.2025.8.17.0001

SITUAÇÃO: Réu apresentou resposta à acusação em processo de tráfico de drogas.
Alega inépcia da denúncia e ausência de justa causa.

DOCUMENTOS:
- Denúncia (ID 215703324): [transcrever]
- Resposta à Acusação (ID 215703890): [transcrever]
- Antecedentes: Certidão (ID 215704001) - réu primário

PEDIDO: Elaborar decisão após resposta à acusação
```

## Dicas de Uso

### 1. Upload de PDFs
O Gemini 3.0 Pro **aceita upload de PDFs diretamente**. Você pode:
- Anexar PDFs do processo
- O modelo lerá e extrairá informações automaticamente
- Isso é ideal para processos digitais

### 2. Conversas Longas
- O Gemini 3.0 Pro mantém contexto de conversas muito longas
- Você pode fazer ajustes iterativos: "Altere o fundamento...", "Adicione menção a..."
- Não precisa reiniciar do zero

### 3. Forneça Minutas de Referência
Para melhores resultados:
- Sempre forneça ao menos 1-3 minutas do repositório como referência de estilo
- O modelo adaptará o estilo do magistrado baseado nas minutas

### 4. Jurisprudência
- **IMPORTANTE**: Forneça apenas jurisprudência que você já pesquisou
- O Gem NÃO buscará jurisprudência externa
- Cole o teor completo do acórdão/súmula

### 5. Iteração e Refinamento
Após receber a primeira versão:
- Peça ajustes: "Reduza o relatório", "Desenvolva mais a fundamentação sobre X"
- Corrija fatos: "O réu é primário, não reincidente"
- Solicite reformulação de trechos específicos

## Limitações do Gem

### O Gem NÃO pode:
❌ Buscar jurisprudência em bancos externos
❌ Acessar o repositório GitHub diretamente
❌ Consultar legislação atualizada automaticamente
❌ Fazer pesquisas na internet
❌ Acessar sistemas processuais (PJe, SAJ, etc.)

### O Gem PODE:
✅ Ler PDFs anexados diretamente
✅ Processar textos muito longos (até 2M tokens)
✅ Manter contexto de conversas extensas
✅ Seguir rigorosamente o estilo das minutas fornecidas
✅ Aplicar jurisprudência que você fornecer
✅ Adaptar decisões conforme feedback iterativo

## Fluxo de Trabalho Recomendado

1. **Preparação**
   - Identifique a fase processual
   - Extraia textos dos PDFs principais (ou anexe diretamente)
   - Selecione 2-3 minutas relevantes do repositório
   - Pesquise jurisprudência aplicável (se necessário)

2. **Primeira Consulta**
   - Forneça todos os documentos ao Gem
   - Faça o pedido inicial
   - Aguarde a decisão completa

3. **Revisão**
   - Leia a decisão gerada
   - Verifique fatos, nomes, datas, IDs
   - Confirme se a jurisprudência foi corretamente transcrita

4. **Ajustes**
   - Solicite alterações pontuais
   - O Gem manterá o contexto e ajustará

5. **Finalização**
   - Copie a decisão final
   - Cole no sistema processual
   - Faça assinatura eletrônica

## Otimizações para Gemini 3.0 Pro

O Gemini 3.0 Pro tem vantagens específicas:

### Grande Janela de Contexto
- Pode processar processos inteiros com centenas de páginas
- Cole múltiplas minutas de uma vez
- Forneça todo o histórico processual se necessário

### Multimodalidade
- Anexe PDFs digitalizados
- O modelo extrairá textos, mesmo de documentos escaneados
- Identifica carimbos, selos, assinaturas em imagens

### Melhor Compreensão Jurídica
- O Gemini 3.0 Pro tem melhor capacidade de raciocínio jurídico
- Compreende nuances processuais complexas
- Mantém consistência argumentativa em textos longos

## Solução de Problemas

### "O Gem esqueceu informações"
- Forneça novamente os dados na mesma mensagem do pedido
- Use conversas mais curtas para decisões pontuais

### "O estilo não está correto"
- Forneça mais minutas de referência (3-5)
- Indique explicitamente: "Siga rigorosamente o estilo da minuta X"

### "Inventou jurisprudência"
- Reforce: "Use APENAS a jurisprudência que forneci"
- Cole novamente as súmulas/acórdãos específicos

### "Formatação incorreta"
- Lembre: "Sem enumeração, sem bullets, sem latim"
- Peça reformatação: "Refaça o dispositivo em parágrafos corridos"

## Exemplos de Comandos Úteis

```
"Elabore decisão de recebimento da denúncia com base nos documentos anexos"

"Analise a resposta à acusação e produza decisão designando audiência"

"Refaça o relatório de forma mais sucinta (máximo 2 parágrafos)"

"Na fundamentação, desenvolva melhor o argumento sobre fundada suspeita"

"Adicione menção à Súmula X do STJ que forneci"

"O nome do réu está errado, é João, não José. Corrija em toda a decisão"

"Reduza o dispositivo, está muito prolixo"
```

## Recursos Adicionais

### Arquivos de Suporte Disponíveis
- `minutas_metadata.json` - Catálogo de todas as minutas
- `GEM_CONTEXTO_BASE.md` - Contexto para copiar/colar
- Minutas individuais em `.md` - Modelos de referência

### Manutenção do Gem
- Atualize as instruções conforme mudanças legislativas
- Adicione novas minutas ao catálogo
- Mantenha jurisprudência atualizada em arquivo separado para referência

## Dúvidas Frequentes

**P: Posso usar o Gem em múltiplos processos?**
R: Sim, mas inicie nova conversa para cada processo diferente para evitar confusão.

**P: O Gem aprende com meu uso?**
R: Não. Gems não têm memória entre sessões. Use as minutas do repositório como base de "aprendizado".

**P: Posso compartilhar meu Gem?**
R: Sim, através do recurso de compartilhamento de Gems do Gemini.

**P: O Gem funciona offline?**
R: Não. Requer conexão com a internet.

**P: Há limite de uso?**
R: Depende do seu plano do Google. O Gemini 3.0 Pro pode ter limites de uso no plano gratuito.
