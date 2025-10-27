

```json
{
  "filename": "INSTAURACAO_INCIDENTE_INSANIDADE_MENTAL.json",
  "tags": [
    "incidente de insanidade mental",
    "exame pericial",
    "suspensão do processo",
    "art. 149 cpp",
    "decisão"
  ],
  "descricao": "Modelo de decisão que instaura incidente de insanidade mental a pedido da defesa, suspendendo o processo principal e nomeando curador ao acusado, com as devidas determinações para a realização do exame pericial.",
  "titulo": "INSTAURAÇÃO DE INCIDENTE DE INSANIDADE MENTAL",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Cuida-se procedimento policial, que atribui ao acusado os delitos previstos no {ARTIGO_CRIME}.\n\nA defesa pugnou pela instauração de incidente de insanidade mental do réu (ID {ID_PETICAO_DEFESA}).\n\nÉ o relatório, passo a decidir."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_e_instauracao",
      "conteudo_base": "Compulsando os autos, entendo que pairam dúvidas sobre a higidez mental do acusado à época dos fatos.\n\nConsiderando o que expressamente dispõe o § 1º, do art. 149 do Código de Processo Penal, **determino a instauração do competente INCIDENTE DE INSANIDADE MENTAL** de {QUALIFICACAO_COMPLETA_ACUSADO}, a fim de que o(a) mesmo(a) seja submetido(a) ao competente exame para configuração ou não de sua imputabilidade, bem como da incapacidade de reger sua própria vida."
    },
    {
      "tipo": "fixo",
      "conteudo": "Determino, para tanto, que o(a) acusado(a) seja encaminhado ao Instituto Médico Legal, onde deverá ser submetido aos competentes exames.\n\nOutrossim, nomeio CURADOR(A) ao(à) acusado(a) o(a) DEFENSOR(A) PÚBLICO(A) que deverá ser intimado(a) da presente nomeação e, prestando o compromisso, deverá se pronunciar sobre o presente incidente, desde já apresentando os questionamentos que considerar necessários, caso ainda não o tenha feito.\n\nIgualmente, determino a intimação do representante do MINISTÉRIO PÚBLICO do presente incidente, ora instaurado, para que apresente os questionamentos que considerar necessários.\n\n**Suspendo o processo** nos termos do § 2º, do art. 149 do Código de Processo Penal, até final solução do incidente.\n\nDetermino a autuação do incidente em apartado.\n\nOs quesitos a serem esclarecidos por perito legal no competente laudo do exame pericial serão apresentados pelo Promotor de Justiça e pela DEFENSORIA PÚBLICA, sendo adotados por este Juízo.\n\nNo mais, aguarde-se em arquivo e, com a homologação do laudo pericial condizente, juntem-se aos presentes autos e voltem-se conclusos."
    },
    {
      "tipo": "fixo",
      "conteudo": "Expedientes e intimações necessárias.\n\nCiência ao Ministério Público e ao defensor.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```