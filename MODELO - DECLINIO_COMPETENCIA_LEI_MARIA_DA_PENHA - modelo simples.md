**[DECISÃO]{.underline}**

Com base na decisão fornecida, realizei a catalogação, identificando as partes fixas e adaptáveis, e aplicando todas as regras de formatação e estilo. O resultado está no formato JSON abaixo.

```json
{
  "filename": "DECLINIO_COMPETENCIA_LEI_MARIA_DA_PENHA - modelo simples.md",
  "tags": [
    "declínio de competência",
    "lei maria da penha",
    "violência doméstica",
    "decisão",
    "prisão em flagrante"
  ],
  "descricao": "Modelo de decisão que declina da competência de um flagrante para a Vara de Violência Doméstica e Familiar Contra a Mulher, por reconhecer a incidência da Lei Maria da Penha.",
  "titulo": "DECLÍNIO DE COMPETÊNCIA - LEI MARIA DA PENHA",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_declinio_competencia",
      "conteudo_base": "Trata-se de comunicação de prisão em flagrante delito pelos fatos descritos no procedimento policial em desfavor de {NOME_FLAGRANTEADO}.\n\nO flagranteado foi posto em liberdade, com a imposição de medidas cautelares diversas da prisão pelo Juízo Plantonista (ID {ID_DECISAO_PLANTAO})."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_lei_maria_da_penha",
      "conteudo_base": "Entendo que os fatos narrados no caderno processual se inserem no âmbito da Lei Maria da Penha, tendo em vista que a vítima, do sexo feminino, é {TIPO_RELACIONAMENTO} do imputado, conforme disposto no art. 5º do referido diploma legal."
    },
    {
      "tipo": "fixo",
      "conteudo": "Assim, entendo que **este juízo não é o competente** para processar e julgar o feito.\n\nDetermino a imediata **redistribuição** **à Vara de Violência Doméstica e Familiar Contra Mulher desta comarca.**\n\nCumpra-se, **COM URGÊNCIA**."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```