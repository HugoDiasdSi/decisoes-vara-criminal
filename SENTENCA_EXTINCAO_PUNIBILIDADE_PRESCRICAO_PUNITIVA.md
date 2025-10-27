

```json
{
  "filename": "SENTENCA_EXTINCAO_PUNIBILIDADE_PRESCRICAO_PUNITIVA.json",
  "tags": [
    "sentença",
    "extinção de punibilidade",
    "prescrição",
    "pretensão punitiva"
  ],
  "descricao": "Modelo de sentença que declara a extinção da punibilidade do agente pelo advento da prescrição da pretensão punitiva do Estado, antes do oferecimento da denúncia, com providências sobre mandado de prisão e fiança.",
  "titulo": "SENTENÇA DE EXTINÇÃO DA PUNIBILIDADE PELA PRESCRIÇÃO DA PRETENSÃO PUNITIVA",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Trata-se de procedimento criminal contra o(a) autuado(a) {NOME_ACUSADO} pela suposta prática do delito ali capitulado.\n\nNão houve oferecimento da denúncia.\n\nO Ministério Público requereu o reconhecimento da prescrição (ID {ID_PARECER_MP}).\n\nEis um relato, no essencial, do processo."
    },
    {
      "tipo": "fixo",
      "conteudo": "Com a ocorrência do fato delituoso, nasce para o Estado o direito/dever de punir. Esse direito, que se denomina pretensão punitiva, não pode se eternizar no tempo. Por isso, escoado o prazo que a própria lei estabelece, observadas suas causas modificadoras, prescreve o direito estatal à punição do infrator.\n\nO art. 107 do CPB traz causas de extinção de punibilidade. Dentre tais causas, se encontra a prescrição:\n\n> Art. 107 - Extingue-se a punibilidade:\n> (...)\n> IV - pela prescrição, decadência ou perempção;\n\nO art. 109 do mesmo diploma legal traz os prazos prescricionais:\n\n> Art. 109. A prescrição, antes de transitar em julgado a sentença final, salvo o disposto no § 1o do art. 110 deste Código, regula-se pelo máximo da pena privativa de liberdade cominada ao crime, verificando-se:\n> I - em vinte anos, se o máximo da pena é superior a doze;\n> II - em dezesseis anos, se o máximo da pena é superior a oito anos e não excede a doze;\n> III - em doze anos, se o máximo da pena é superior a quatro anos e não excede a oito;\n> IV - em oito anos, se o máximo da pena é superior a dois anos e não excede a quatro;\n> V - em quatro anos, se o máximo da pena é igual a um ano ou, sendo superior, não excede a dois;\n> VI - em 3 (três) anos, se o máximo da pena é inferior a 1 (um) ano.\n\nO termo inicial da prescrição antes de transitar em julgado a sentença final se deu com a consumação dos delitos:\n\n> Art. 111 - A prescrição, antes de transitar em julgado a sentença final, começa a correr:\n> I - do dia em que o crime se consumou;\n\nNão houve causa interruptiva ou suspensiva da prescrição. Concluo que, sem essas, mostra-se presente nestes autos uma das causas de extinção da punibilidade, a prescrição da pretensão punitiva do Estado, matéria sempre de ordem pública em Direito Penal.\n\n> Art. 61 do Código de Processo Penal - Em qualquer fase do processo, o juiz, se reconhecer extinta a punibilidade, deverá declará-lo de ofício."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_punibilidade",
      "conteudo_base": "Diante destas considerações, **decreto a EXTINÇÃO DA PUNIBILIDADE, pelo advento da prescrição da pretensão punitiva do estado**, do(a) autuado(a) {NOME_ACUSADO} em relação aos fatos narrados nos presentes autos."
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