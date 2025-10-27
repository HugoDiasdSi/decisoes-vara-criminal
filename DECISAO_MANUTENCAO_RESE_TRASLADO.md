{
  "filename": "DECISAO_MANUTENCAO_RESE_TRASLADO.md",
  "tags": [
    "recurso em sentido estrito",
    "RESE",
    "juízo de retratação",
    "manutenção da decisão",
    "traslado",
    "audiência de instrução",
    "depoimento acolhedor"
  ],
  "descricao": "Modelo de decisão que mantém a decisão recorrida em sede de juízo de retratação de Recurso em Sentido Estrito (RESE), determina a formação de traslado para remessa ao Tribunal e designa continuação de audiência.",
  "titulo": "DECISÃO - JUÍZO DE RETRATAÇÃO EM RESE",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_rese",
      "conteudo_base": "Recurso em sentido estrito tempestivamente apresentado e recebido por este Juízo.\n\nO Ministério Público apresentou as respectivas razões (ID {ID_RAZOES_MP}).\n\nA defesa técnica, por seu turno, apresentou as contrarrazões devidamente (ID {ID_CONTRARRAZOES_DEFESA}).\n\nO(A) assistente de acusação não se manifestou, apesar de devidamente intimado(a).\n\nEis o breve relato. Decido."
    },
    {
      "tipo": "fixo",
      "conteudo": "Mantenho a decisão recorrida, por seus próprios fundamentos."
    },
    {
      "tipo": "adaptavel",
      "identificador": "formacao_traslado_remessa",
      "conteudo_base": "Forme-se o traslado com as folhas indicadas no recurso (ID {ID_INDICACAO_PECAS}), conforme requerido pelo MP, e remetam-se os autos deste ao egrégio TJPE."
    },
    {
      "tipo": "condicional",
      "identificador": "designacao_continuacao_audiencia",
      "descricao": "Usar este bloco se houver necessidade de designar continuação de audiência de instrução.",
      "conteudo_base": "À secretaria para que designe data e horário para a continuação da audiência de instrução, com a oitiva da vítima por meio de depoimento acolhedor, e o interrogatório do réu, caso ainda não providenciado."
    },
    {
      "tipo": "fixo",
      "conteudo": "Ciência ao Ministério Público e ao Defensor.\n\nIntime-se.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}