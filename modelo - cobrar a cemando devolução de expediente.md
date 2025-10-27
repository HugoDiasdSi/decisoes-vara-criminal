Com base no despacho fornecido, realizei a catalogação, identificando as partes fixas e adaptáveis e aplicando as regras de formatação. O resultado está no formato JSON abaixo.

```json
{
  "filename": "modelo - cobrar a cemando devolução de expediente.md",
  "tags": [
    "despacho",
    "cobrança de mandado",
    "CEMANDO",
    "cumprimento de ordem",
    "processual"
  ],
  "descricao": "Modelo de despacho para cobrar a devolução de mandado não cumprido pela Central de Mandados (CEMANDO), com previsão de comunicação à Corregedoria em caso de inércia.",
  "titulo": "DESPACHO - COBRANÇA DE DEVOLUÇÃO DE MANDADO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "cobranca_mandado_cemando",
      "conteudo_base": "Oficie-se à chefia da CEMANDO desta comarca cobrando a devolução do mandado de ID {ID_MANDADO}.\n\nEm não sendo devolvido com a diligência feita no prazo de 48h, informe-se à CGJ acerca do não cumprimento no prazo para as providências cabíveis."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```