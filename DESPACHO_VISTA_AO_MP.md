

```json
{
  "filename": "DESPACHO_VISTA_AO_MP.md",
  "tags": [
    "despacho",
    "vista ao MP",
    "ministério público",
    "expediente",
    "diligência frustrada",
    "ônus da acusação"
  ],
  "descricao": "Modelo canônico de despacho de expediente que abre vista ao Ministério Público. Peça sucinta: registra em uma frase o fato que motiva a remessa e determina a vista. Não comporta relatório, fundamentação, nem delimitação do que o órgão ministerial deve enfrentar.",
  "titulo": "DESPACHO - VISTA AO MINISTÉRIO PÚBLICO",
  "instrucao_llm": "Gerar despacho com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável. REGRA DE EXTENSÃO (vinculante): o despacho tem no máximo dois parágrafos de conteúdo, além do fecho. O primeiro registra em uma frase o fato processual que motiva a remessa, com o ID da peça. O segundo determina a vista e, quando for o caso, a diligência a cargo da acusação. É VEDADO acrescentar relatório do histórico do feito, síntese da denúncia, transcrição de certidões, fundamentação jurídica, citação de jurisprudência, ou parágrafo que delimite, oriente ou antecipe o teor da manifestação ministerial — a escolha da promoção cabe ao órgão acusador. O Ministério Público tem acesso aos autos e não precisa que o despacho lhe narre o que já consta deles.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "fato_motivador",
      "descricao": "Uma única frase, com o ID da peça, dizendo o que ocorreu e enseja a remessa. Exemplos de motivo: diligência ou mandado não cumprido; decurso de prazo; juntada de peça que reclama pronunciamento; certidão da secretaria; retorno de precatória.",
      "conteudo_base": "{FATO_PROCESSUAL_QUE_MOTIVA_A_REMESSA} (ID {ID_PECA})."
    },
    {
      "tipo": "adaptavel",
      "identificador": "determinacao_vista",
      "conteudo_base": "**Vista ao Ministério Público** para manifestação."
    },
    {
      "tipo": "condicional",
      "identificador": "diligencia_endereco",
      "descricao": "Usar apenas quando a remessa decorre da não localização do réu ou da vítima. Reflete o ônus da acusação de buscar o endereço. Substitui o bloco 'determinacao_vista', não se soma a ele.",
      "conteudo_base": "**Vista ao Ministério Público** para que empreenda as diligências necessárias à obtenção do endereço atualizado de **{NOME}**, com consulta aos sistemas pertinentes, e se manifeste."
    },
    {
      "tipo": "condicional",
      "identificador": "prazo",
      "descricao": "Usar somente quando houver prazo específico a assinalar, distinto do prazo legal. Não incluir por padrão.",
      "conteudo_base": "Prazo de {PRAZO}."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "Cumpra-se.\n\n{LOCALIDADE}/PE, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ],
  "exemplo_saida": "**DESPACHO**\n\nO mandado de intimação pessoal de **Matheus de Lima Ramos** não foi cumprido, conforme certidão negativa do oficial de justiça (ID 247587462).\n\n**Vista ao Ministério Público** para que empreenda as diligências necessárias à obtenção do endereço atualizado do réu, com consulta aos sistemas pertinentes, e se manifeste sobre a suspensão condicional do processo.\n\nCumpra-se.\n\nCamaragibe/PE, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\n\nJuiz de Direito"
}
```
