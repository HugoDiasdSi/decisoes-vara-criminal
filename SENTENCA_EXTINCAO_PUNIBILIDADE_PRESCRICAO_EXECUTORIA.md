

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
      "tipo": "condicional",
      "identificador": "destinacao_bens_apreendidos",
      "descricao": "Usar este bloco se houver bens apreendidos (armas, munições e acessórios, veículos, aparelhos celulares, numerário, drogas, demais objetos) ou fiança sem destinação já dada e individualizada nos autos. Incluir só os parágrafos pertinentes. Cada item deve ser individualizado no corpo do ato com os dados constantes dos autos, sem fórmula genérica ('armas porventura apreendidas', 'bens apreendidos') e sem remissão a anexo ou planilha. Armas: espécie, marca, calibre, número de série, NIAF, número e ID do laudo e número do caso NIAF/CORE; sem laudo nos autos, requisitar ao Instituto de Criminalística em 48 horas e determinar a destruição após a juntada; proprietário com CRAF, restituição; demais regras na seção 'Destinação de Bens Apreendidos e Fiança' do SKILL.md (IN Conjunta TJPE n. 24/2020 e Ofício-Circular n. 09/2026-CGJ). Se o modelo já tiver bloco próprio sobre fiança, usar aquele para a fiança.",
      "conteudo_base": "Quanto ao armamento apreendido, juntado o laudo pericial ({NUMERO_E_ID_DO_LAUDO}) e não mais interessando à persecução penal, **determino o encaminhamento ao Comando do Exército, para destruição**, por intermédio do Núcleo de Identificação de Armas de Fogo do Comando de Operações e Recursos Especiais da Polícia Civil de Pernambuco (NIAF/CORE/PCPE), de {ESPECIE_MARCA_CALIBRE_NUMERO_DE_SERIE_NIAF_E_CASO_NIAF_CORE}, bem como de eventuais munições e acessórios correspondentes, nos termos do art. 25 da Lei n. 10.826/2003. Comunique-se imediatamente, por meio eletrônico, ao NIAF/CORE/PCPE e à Secretaria de Defesa Social (art. 5º, § 4º, da Instrução Normativa Conjunta TJPE n. 24/2020), com cópia deste ato, que servirá como ofício.\n\nQuanto ao veículo {MARCA_MODELO_COR_PLACA_CHASSI_E_RENAVAM} (ID {ID_DO_AUTO_DE_APREENSAO}), {DESTINACAO_DO_VEICULO}.\n\nQuanto aos demais bens apreendidos, {DESCRICAO_INDIVIDUALIZADA_DE_CADA_BEM_E_RESPECTIVA_DESTINACAO}.\n\nQuanto à fiança recolhida no valor de {VALOR} (ID {ID_DO_COMPROVANTE}), {DESTINACAO_DA_FIANCA}."
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