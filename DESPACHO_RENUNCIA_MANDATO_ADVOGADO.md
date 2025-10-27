

```json
{
  "filename": "DESPACHO_RENUNCIA_MANDATO_ADVOGADO.json",
  "tags": [
    "despacho",
    "renúncia de mandato",
    "intimação",
    "defensor público",
    "advogado"
  ],
  "descricao": "Modelo de despacho que trata da renúncia de mandato por advogado constituído, determinando a intimação pessoal do acusado para constituir novo patrono, com nomeação da Defensoria Pública em caso de inércia.",
  "titulo": "DESPACHO - RENÚNCIA DE MANDATO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_renuncia_mandato",
      "conteudo_base": "Compulsando os autos, verifico que o advogado constituído pelo acusado {NOME_ACUSADO}, {NOME_ADVOGADO}, requereu a renúncia ao mandato (ID {ID_PETICAO_RENUNCIA}).\n\nTodavia, observo que o causídico не se desincumbiu do dever de provar que cientificou o mandante de sua abdicação, com vistas a permitir a nomeação de novo procurador, como determina o comando legal do art. 112 do Código de Processo Civil."
    },
    {
      "tipo": "adaptavel",
      "identificador": "determinacao_intimacao_acusado",
      "conteudo_base": "Nada obstante, visando à celeridade processual, intime-se pessoalmente o acusado para constituir, no prazo de 10 (dez) dias, novo patrono para patrocinar sua defesa, cientificando-lhe da renúncia do seu anterior causídico."
    },
    {
      "tipo": "fixo",
      "conteudo": "Decorrido esse último prazo sem nenhuma manifestação, fica de logo designado o Defensor Público com atuação nesta Comarca para proceder à sua defesa, devendo ser este cientificado da audiência designada nos autos."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "Cumpra-se.\n\n{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```