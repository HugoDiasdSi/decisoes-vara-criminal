

```json
{
  "filename": "SENTENCA_EXTINCAO_PUNIBILIDADE_PRESCRICAO_EXECUTÓRIA.md",
  "tags": [
    "sentença",
    "extinção de punibilidade",
    "prescrição",
    "prescrição intercorrente",
    "pretensão punitiva"
  ],
  "descricao": "Modelo de sentença que declara a extinção da punibilidade do agente pelo advento da prescrição da pretensão punitiva na modalidade intercorrente (após o recebimento da denúncia).",
  "titulo": "SENTENÇA DE EXTINÇÃO DA PUNIBILIDADE PELA PRESCRIÇÃO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Trata-se de Ação Penal, em que o Ministério Público imputa ao acusado {NOME_ACUSADO} a prática do delito previsto no art. 329, do Código de Penal Brasileiro.\n\nA denúncia foi recebida em {DATA_RECEBIMENTO} (ID {ID_RECEBIMENTO}).\n\nEis um relato, no essencial, do processo."
    },
    {
      "tipo": "fixo",
      "conteudo": "Com a ocorrência do fato delituoso, nasce para o Estado o direito/dever de punir. Esse direito, que se denomina pretensão punitiva, não pode se eternizar no tempo. Por isso, escoado o prazo que a própria lei estabelece, observadas suas causas modificadoras, prescreve o direito estatal à punição do infrator.\n\nO art. 329, do CPB, assim dispõe:\n\n> Art. 329 - Opor-se à execução de ato legal, mediante violência ou ameaça a funcionário competente para executá-lo ou a quem lhe esteja prestando auxílio:\n> Pena - detenção, de dois meses a dois anos.\n\nO art. 107 do CPB traz causas de extinção de punibilidade. Dentre tais causas, se encontra a prescrição:\n\n> Art. 107 - Extingue-se a punibilidade:\n> (...)\n> IV - pela prescrição, decadência ou perempção;\n\nO art. 109 do mesmo diploma legal traz os prazos prescricionais:\n\n> Art. 109. A prescrição, antes de transitar em julgado a sentença final, (...) regula-se pelo máximo da pena privativa de liberdade cominada ao crime, verificando-se:\n> (...)\n> V - em quatro anos, se o máximo da pena é igual a um ano ou, sendo superior, não excede a dois;\n\nNão houve outra causa interruptiva ou suspensiva da prescrição, fora o recebimento da denúncia. Concluo que, mostra-se presente nestes autos uma das causas de extinção da punibilidade, a prescrição da pretensão punitiva do Estado, matéria sempre de ordem pública em Direito Penal.\n\n> Art. 61 do Código de Processo Penal - Em qualquer fase do processo, o juiz, se reconhecer extinta a punibilidade, deverá declará-lo de ofício."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_punibilidade",
      "conteudo_base": "Diante destas considerações, **decreto a EXTINÇÃO DA PUNIBILIDADE, pelo advento da prescrição da pretensão punitiva do estado**, do autuado {NOME_ACUSADO} em relação aos fatos narrados nos presentes autos."
    },
    {
      "tipo": "condicional",
      "identificador": "recolhimento_mandado_prisao",
      "descricao": "Usar este bloco se houver mandado de prisão expedido nos autos.",
      "conteudo_base": "RECOLHA-SE, SEM CUMPRIMENTO, O MANDADO DE PRISÃO PORVENTURA EXPEDIDO EM DESFAVOR DO(A) ACUSADO(A)."
    },
    {
      "tipo": "condicional",
      "identificador": "devolucao_fianca",
      "descricao": "Usar este bloco se houver valor de fiança depositado nos autos.",
      "conteudo_base": "DEVOLVA-SE, AO(À) ACUSADO(A), O VALOR PORVENTURA RECOLHIDO COMO FIANÇA."
    },
    {
      "tipo": "fixo",
      "conteudo": "Demais expedientes necessários.\n\nSEM CUSTAS.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```