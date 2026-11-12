

```json
{
  "filename": "DECISAO_INTIMACAO_ASSISTENTE_ACUSACAO_ALEGACOES_FINAIS_OMISSAO.md",
  "tags": [
    "decisão",
    "assistente de acusação",
    "alegações finais",
    "memoriais",
    "omissão de intimação",
    "nulidade",
    "art. 271 do CPP",
    "art. 403, § 3º, do CPP",
    "nova vista à defesa",
    "antecedentes criminais",
    "TJPE"
  ],
  "descricao": "Modelo de decisão que, após o encerramento da instrução e a abertura de vista para memoriais, constata que o assistente de acusação habilitado não foi intimado (apenas o Ministério Público e a defesa o foram), sana a omissão antes da sentença e determina a intimação das advogadas do assistente para alegações finais em 5 dias, com nova vista à defesa para novas alegações ou ratificação, certidão de antecedentes e conclusão para sentença.",
  "titulo": "DECISÃO",
  "instrucao_llm": "Gerar decisão com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, com o conteúdo adaptado ao caso concreto e IDs conferidos nos autos. Usar apenas quando o assistente de acusação estiver regularmente habilitado e não tiver sido intimado para os memoriais. Se a defesa ainda não tiver apresentado alegações finais, ajustar o bloco de relatório e suprimir a referência à ratificação.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_acao_penal",
      "descricao": "Identifica a ação penal, o acusado e os crimes imputados.",
      "conteudo_base": "Trata-se de ação penal movida pelo Ministério Público do Estado de Pernambuco em face de {NOME_ACUSADO}, pela imputação dos crimes {CRIMES_IMPUTADOS}."
    },
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_instrucao_e_memoriais",
      "descricao": "Narra o encerramento da instrução, a determinação de memoriais e as peças já apresentadas.",
      "conteudo_base": "Encerrada a instrução na audiência realizada em {DATA_AUDIENCIA} (ID {ID_TERMO_AUDIENCIA}), as partes requereram a apresentação de alegações finais por memoriais, e este juízo determinou, no respectivo termo, a abertura de vista ao Ministério Público, ao assistente de acusação e à defesa para esse fim."
    },
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_omissao_intimacao_assistente",
      "descricao": "Registra os memoriais já ofertados, a habilitação regular do assistente (poderes especiais) e a omissão de sua intimação.",
      "conteudo_base": "O Ministério Público ofereceu seus memoriais (ID {ID_MEMORIAIS_MP}) e {DEFESA_QUE_APRESENTOU} apresentou os da defesa (ID {ID_MEMORIAIS_DEFESA}). {NOME_ASSISTENTE}, contudo, habilitou-se regularmente como assistente de acusação, por intermédio de advogadas constituídas com procuração dotada de poderes especiais (ID {ID_PROCURACAO_1} e ID {ID_PROCURACAO_2}), tendo acompanhado a instrução na condição de assistente, conforme o termo de audiência (ID {ID_TERMO_AUDIENCIA}). Não obstante a determinação expressa de vista também ao assistente, foram expedidas apenas as intimações do Ministério Público (ID {ID_INTIMACAO_MP}) e da defesa (ID {ID_INTIMACAO_DEFESA}), sem que se intimasse o assistente de acusação, vindo os autos conclusos para julgamento."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_saneamento",
      "descricao": "Fundamenta o saneamento da omissão antes da sentença.",
      "conteudo_base": "Impõe-se sanar a omissão antes da sentença, assegurando ao assistente a oportunidade de se manifestar na forma do art. 271 e do art. 403, § 3º, do Código de Processo Penal, sob pena de nulidade."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_intimacao_assistente",
      "descricao": "Determina a intimação das advogadas do assistente para memoriais em 5 dias.",
      "conteudo_base": "Diante disso, intimem-se as advogadas constituídas pela assistente de acusação {NOME_ASSISTENTE} (ID {ID_PROCURACAO_1} e ID {ID_PROCURACAO_2}) para, no prazo de 5 (cinco) dias, apresentarem alegações finais por memoriais."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_nova_vista_defesa_e_conclusao",
      "descricao": "Determina nova vista à defesa após os memoriais do assistente, certidão de antecedentes e conclusão para sentença.",
      "conteudo_base": "Apresentadas as alegações finais pela assistente de acusação, dê-se nova vista à defesa para, no prazo legal, apresentar novas alegações finais ou ratificar as já ofertadas (ID {ID_MEMORIAIS_DEFESA}); após, certifiquem-se os antecedentes criminais {DO_ACUSADO_OU_DA_ACUSADA} e venham os autos conclusos para sentença."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_inercia_assistente",
      "descricao": "Providência em caso de inércia do assistente no prazo.",
      "conteudo_base": "Não apresentadas alegações finais pela assistente de acusação no prazo assinalado, certifiquem-se os antecedentes criminais {DO_ACUSADO_OU_DA_ACUSADA} e venham os autos conclusos para sentença."
    },
    {
      "tipo": "fixo",
      "identificador": "fecho_padrao",
      "conteudo": "Cumpra-se.\n\n{LOCALIDADE}/PE, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\n\nJuiz de Direito"
    }
  ],
  "exemplo_saida": "DECISÃO\n\nTrata-se de ação penal movida pelo Ministério Público do Estado de Pernambuco em face de Fulana de Tal, pela imputação dos crimes do art. 140, § 3º, do art. 331, do art. 163, parágrafo único, III, e do art. 147-A, na forma do art. 69, todos do Código Penal.\n\nEncerrada a instrução na audiência realizada em 16/9/2026 (ID 254859799), as partes requereram a apresentação de alegações finais por memoriais, e este juízo determinou, no respectivo termo, a abertura de vista ao Ministério Público, ao assistente de acusação e à defesa para esse fim.\n\nO Ministério Público ofereceu seus memoriais (ID 255405690) e a Defensoria Pública apresentou os da defesa (ID 263445343). A vítima Beltrana de Tal, contudo, habilitou-se regularmente como assistente de acusação, por intermédio de advogadas constituídas com procuração dotada de poderes especiais (ID 250581472 e ID 250584135), tendo acompanhado a instrução na condição de assistente, conforme o termo de audiência (ID 254859799). Não obstante a determinação expressa de vista também ao assistente, foram expedidas apenas as intimações do Ministério Público (ID 254923860) e da defesa (ID 258606030), sem que se intimasse o assistente de acusação, vindo os autos conclusos para julgamento.\n\nImpõe-se sanar a omissão antes da sentença, assegurando ao assistente a oportunidade de se manifestar na forma do art. 271 e do art. 403, § 3º, do Código de Processo Penal, sob pena de nulidade.\n\nDiante disso, intimem-se as advogadas constituídas pela assistente de acusação Beltrana de Tal (ID 250581472 e ID 250584135) para, no prazo de 5 (cinco) dias, apresentarem alegações finais por memoriais.\n\nApresentadas as alegações finais pela assistente de acusação, dê-se nova vista à defesa para, no prazo legal, apresentar novas alegações finais ou ratificar as já ofertadas (ID 263445343); após, certifiquem-se os antecedentes criminais da acusada e venham os autos conclusos para sentença.\n\nNão apresentadas alegações finais pela assistente de acusação no prazo assinalado, certifiquem-se os antecedentes criminais da acusada e venham os autos conclusos para sentença.\n\nCumpra-se.\n\nCamaragibe/PE, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\n\nJuiz de Direito"
}
```
