Com base no despacho fornecido, realizei a catalogação, identificando as partes fixas e adaptáveis e aplicando as regras de formatação. O resultado está no formato JSON abaixo.

```json
{
  "filename": "INDEFERIMENTO_HABILITACAO_ASSISTENTE_ACUSACAO.md",
  "tags": [
    "assistente de acusação",
    "habilitação",
    "indeferimento",
    "decisão interlocutória",
    "fase pré-processual"
  ],
  "descricao": "Modelo de decisão que indefere o pedido de habilitação de advogado como assistente de acusação, seja por ser em momento processual inadequado (antes da ação penal), seja por ausência de poderes especiais na procuração.",
  "titulo": "INDEFERIMENTO DE HABILITAÇÃO DE ASSISTENTE DE ACUSAÇÃO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_indeferimento",
      "conteudo_base": "Não cabe intervenção do advogado como assistente de acusação nesse momento. A habilitação do assistente do Ministério Público ocorre após o recebimento da denúncia, durante a Ação Penal.\n\nAdemais, não foram outorgados poderes especiais na procuração para atuar neste processo, de natureza sigilosa."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_indeferimento",
      "conteudo_base": "Ante o exposto, **INDEFIRO** a habilitação do advogado {NOME_ADVOGADO} nos presentes autos."
    },
    {
      "tipo": "adaptavel",
      "identificador": "instrucoes_finais",
      "conteudo_base": "Intimadas as partes da sentença de extinção, arquivem-se os autos."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "Cumpra-se.\n\n{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```
