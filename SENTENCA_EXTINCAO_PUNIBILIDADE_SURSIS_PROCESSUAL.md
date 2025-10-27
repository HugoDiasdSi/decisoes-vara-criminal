

```json
{
  "filename": "SENTENCA_EXTINCAO_PUNIBILIDADE_SURSIS_PROCESSUAL.md",
  "tags": [
    "sentença",
    "extinção de punibilidade",
    "sursis processual",
    "suspensão condicional do processo",
    "lei 9.099/95"
  ],
  "descricao": "Modelo de sentença que declara a extinção da punibilidade do agente em razão do integral cumprimento da Suspensão Condicional do Processo, com base no art. 89, § 5º, da Lei n. 9.099/95.",
  "titulo": "SENTENÇA DE EXTINÇÃO DA PUNIBILIDADE (CUMPRIMENTO DE SURSIS PROCESSUAL)",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Cuida-se de ação penal instaurada pelo Ministério Público em face do(a) acusado(a) {NOME_ACUSADO} apontando-o(a) como incurso(a) no delito previsto na inicial.\n\nFoi concedida a suspensão condicional do processo (ID {ID_DECISAO_SURSIS}).\n\nConsta nos autos certidão de que o(a) acusado(a) cumpriu o período de prova sem qualquer descumprimento das condições estipuladas (ID {ID_CERTIDAO_CUMPRIMENTO}).\n\nRelatei. Decido."
    },
    {
      "tipo": "fixo",
      "conteudo": "O(A) autor(a) cumpriu as condições do benefício no período de prova tendo, portanto, direito à declaração, por sentença, da extinção da punibilidade, nos termos do art. 89, § 5º, da Lei n. 9.099/1995."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_punibilidade",
      "conteudo_base": "Posto isso, **declaro, por sentença, a EXTINÇÃO DA PUNIBILIDADE de {NOME_ACUSADO}**, em relação ao delito objeto deste Processo."
    },
    {
      "tipo": "condicional",
      "identificador": "restituicao_fianca",
      "descricao": "Usar este bloco se houver valor de fiança depositado nos autos e não houver notícia de quebra das condições.",
      "conteudo_base": "Não há notícias nos autos de conduta que configure quebra de fiança, assim, com o trânsito em julgado, expeça-se alvará para levantamento da fiança em nome do(a) autor(a) do fato, acaso existente."
    },
    {
      "tipo": "fixo",
      "conteudo": "Intimações necessárias.\n\nCumpra-se.\n\nCertificado o trânsito em julgado, proceda-se à baixa na distribuição и ao arquivamento."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```