

```json
{
  "filename": "decisão - restituição de coisa apreendida e intimação de réu solto da sentença por seu advogado constituído (exceto defensoria)",
  "tags": [
    "restituição de coisa apreendida",
    "arma de fogo",
    "intimação de sentença",
    "réu solto",
    "decisão interlocutória"
  ],
  "descricao": "Modelo de decisão que, em um primeiro momento, defere o pedido de restituição de arma de fogo e, em seguida, determina a intimação de réu solto sobre a sentença condenatória por meio de seu defensor, com base em jurisprudência do STJ.",
  "titulo": "DECISÃO - RESTITUIÇÃO DE BEM E INTIMAÇÃO DE SENTENÇA",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_pedido_restituicao",
      "conteudo_base": "Trata-se de pedido de restituição da {DESCRICAO_DO_BEM_APREENDIDO}, formulado por {NOME_REQUERENTE}, ocasião em que juntou os documentos pertinentes.\n\nDeu-se vista ao Ministério Público e, em cota exarada no ID {ID_PARECER_MP}, o órgão ministerial anuiu ao requerimento do autor.\n\nDECIDO"
    },
    {
      "tipo": "fixo",
      "conteudo": "A documentação acostada aos autos demonstra que o requerente é proprietário da arma apreendida, inexistindo qualquer dúvida a respeito.\n\nO Ministério Público concordou com o pleito.\n\nA arma não interessa ao deslinde do processo."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_deferimento_restituicao",
      "conteudo_base": "Ante o exposto, nos termos do art. 120 do CPP, **defiro o pedido de restituição** da {DESCRICAO_COMPLETA_DA_ARMA_COM_NUMERO_SERIE}, formulado por {NOME_REQUERENTE}, conforme descrição de ID {ID_DOCUMENTO_DESCRICAO}.\n\nQue a serventia proceda com a restituição dos referidos bens, mediante assinatura de termo ou qualquer outro instrumento equivalente.\n\nDou a presente decisão força de mandado/ofício.\n\nAutorizo que o advogado subscritor do pedido seja portador do ofício de liberação, determinando que o mesmo, no prazo de 05 (cinco) dias, informe nestes o resultado obtido."
    },
    {
      "tipo": "condicional",
      "identificador": "transicao_para_intimacao_sentenca",
      "descricao": "Usar este bloco para conectar a decisão de restituição com a deliberação subsequente sobre a intimação da sentença do réu.",
      "conteudo_base": "Superada essa questão, verifico que o réu {NOME_REU} ainda não fora intimado da sentença prolatada nos autos."
    },
    {
      "tipo": "fixo",
      "conteudo": "O Superior Tribunal de Justiça já possui entendimento pacificado pela prescindibilidade da intimação pessoal do réu solto acerca da sentença condenatória, quando possui defesa técnica habilitada:\n\n> AGRAVO REGIMENTAL EM RECURSO ORDINÁRIO EM HABEAS CORPUS. TRÁFICO DE DROGAS E ASSOCIAÇÃO PARA O TRÁFICO. ALEGAÇÃO DE AUSÊNCIA DE INTIMAÇÃO PESSOAL DA CONDENAÇÃO. RÉU SOLTO. ADVOGADO CONSTITUÍDO DEVIDAMENTE INTIMADO. ART. 392, INCISO II, DO CPP. AUSÊNCIA DE CONSTRANGIMENTO ILEGAL. PRECEDENTES DO STJ. 1. Nos termos do art. 392, inciso II, do Código de Processo Penal, tratando-se de réu solto, como na espécie, é suficiente a intimação do defensor constituído a respeito da sentença condenatória. Precedentes do STJ. 2. Agravo regimental desprovido.\n> (AgRg no RHC n. 183.908/SP, relator Ministro Sebastião Reis Júnior, Sexta Turma, julgado em 13/5/2024, DJe de 15/5/2024.)"
    },
    {
      "tipo": "adaptavel",
      "identificador": "determinacao_intimacao_finalizacao_processo",
      "conteudo_base": "Portanto, sem maiores delongas, determino a intimação do acusado {NOME_REU}, por meio da respectiva defesa, sobre os termos da sentença prolatada nos autos.\n\nNão sobrevindo a interposição de recursos, certifique-se o trânsito em julgado.\n\nEm seguida, cumpridas todas as determinações da sentença em questão, com as cautelas de praxe, arquive-se o processo.\n\nExpedientes e intimações necessárias.\n\nCiência ao Ministério Público."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```
