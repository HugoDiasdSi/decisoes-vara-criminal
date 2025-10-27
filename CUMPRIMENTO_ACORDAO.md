

```json
{
  "filename": "CUMPRIMENTO_ACORDAO",
  "tags": [
    "cumprimento de acórdão",
    "carta de guia",
    "regime semiaberto",
    "regime fechado",
    "decisão",
    "execução penal"
  ],
  "descricao": "Modelo de decisão para dar cumprimento a acórdão do Tribunal de Justiça, com instruções específicas para a secretaria expedir carta de guia e/ou mandado de prisão, a depender do regime prisional fixado (semiaberto ou fechado).",
  "titulo": "CUMPRIMENTO DE ACÓRDÃO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "Adaptavel",
      "conteudo": "Cumpra-se o acórdão proferido nos autos.{ID_ACŔDÃO}"
    },
    {
      "tipo": "condicional",
      "identificador": "condenacao_regime_semiaberto",
      "descricao": "Usar este bloco se o acórdão condenou ou manteve a condenação em regime semiaberto.",
      "conteudo_base": "Saliento que a secretaria, em caso de condenação ao regime semiaberto, deve expedir a competente carta de guia sem a expedição de mandado de prisão."
    },
    {
      "tipo": "condicional",
      "identificador": "condenacao_regime_fechado",
      "descricao": "Usar este bloco se o acórdão condenou ou manteve a condenação em regime fechado.",
      "conteudo_base": "Em caso de manutenção do regime fechado, expeça-se o competente mandado de prisão e, com a notícia da captura ou já estando o réu {NOME_REU} preso, expeça-se a competente carta de guia definitiva."
    },
    {
      "tipo": "fixo",
      "conteudo": "Diligências, expedientes e intimações necessárias.\n\nEm seguida e com as cautelas de praxe, cumpridas todas as determinações judiciais, arquivem-se os autos."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```