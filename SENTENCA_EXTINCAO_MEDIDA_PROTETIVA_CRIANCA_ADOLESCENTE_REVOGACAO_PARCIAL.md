Com base no JSON fornecido, realizei a catalogação completa, adicionando metadados, ajustando o conteúdo para seguir estritamente as regras de formatação e estilo (como a remoção da frase "Publique-se. Registre-se. Intimem-se.") e tornando os blocos mais claros e reutilizáveis.

O resultado está no formato JSON válido abaixo.

```json
{
  "filename": "SENTENCA_EXTINCAO_MEDIDA_PROTETIVA_CRIANCA_ADOLESCENTE_REVOGACAO_PARCIAL.md",
  "tags": [
    "sentença",
    "extinção do processo",
    "medida protetiva",
    "criança e adolescente",
    "lei 13.431/2017",
    "lei 14.344/2022",
    "lei henry borel",
    "revogação parcial"
  ],
  "descricao": "Modelo de sentença que extingue o procedimento de medida protetiva em favor de criança/adolescente, revogando parcialmente as medidas para um dos requeridos e mantendo-as por prazo determinado para o outro.",
  "titulo": "SENTENÇA - EXTINÇÃO DE MEDIDA PROTETIVA (LEI N. 13.431/2017)",
  "instrucao_llm": "Gerar sentença judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Trata-se de expediente relacionado à medida protetiva de urgência, contemplada na Lei n. 13.431/2017. As medidas de proteção foram deferidas e as partes devidamente intimadas.\n\nA requerida {NOME_REQUERIDA} pleiteou a revogação das medidas protetivas em relação a si.\n\nInstado a se manifestar, o representante ministerial foi favorável ao pedido de revogação (ID {ID_PARECER_MP}).\n\nVieram os autos conclusos.\n\nÉ o relatório. Decido."
    },
    {
      "tipo": "fixo",
      "identificador": "fundamentacao_legal",
      "conteudo": "A Lei n. 13.431/2017 normatiza e organiza o sistema de garantias de direitos da criança e do adolescente vítima ou testemunha de violência. Por sua vez, a Lei n. 14.344/2022 criou mecanismos para a prevenção e o enfrentamento da violência doméstica e familiar contra a criança e o adolescente, prevendo medidas protetivas de urgência.\n\nAs medidas protetivas de urgência têm natureza cautelar e visam instrumentalizar a eficácia do processo a partir da proteção da vítima. O fundamento norteador das medidas consiste na necessidade real de se contornar situações de urgência e garantir, de pronto, a integridade física e psicológica da vítima."
    },
    {
      "tipo": "fixo",
      "identificador": "fundamentacao_exaurimento_objeto",
      "conteudo": "No caso em exame, o objetivo principal do feito, qual seja, a proteção imediata da vítima, já foi alcançado, porquanto as medidas protetivas de urgência foram deferidas por este juízo.\n\nAdemais, a cognição completa será realizada durante o curso de eventual ação penal, podendo o juízo manter, revogar ou modificar a medida protetiva anteriormente deferida a qualquer tempo.\n\nSob esse influxo, inexiste justificativa para a tramitação deste procedimento, tendo em vista que seu objetivo já foi alcançado.\n\nRegistre-se, por fim, que não há impeditivo para que a vítima, em face de nova conduta agressiva, peça novamente a aplicação de medidas protetivas.\n\nTenho por encerrada a presente cautelar-crime, uma vez que as ações policiais já foram deflagradas, não tendo o Ministério Público ou a Autoridade Policial requerido outras medidas."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_e_revogacao",
      "conteudo_base": "Posto isso, **REVOGO** as medidas protetivas em relação à requerida {NOME_REQUERIDA}, na esteira da manifestação ministerial (ID {ID_PARECER_MP}), e, no mais, **confirmo a decisão** que concedeu as medidas em relação ao requerido {NOME_REQUERIDO}, e **julgo extinto o processo, com resolução do mérito**, nos termos do art. 3º do Código de Processo Penal c/c art. 487, I, do Código de Processo Civil."
    },
    {
      "tipo": "adaptavel",
      "identificador": "determinacao_validade",
      "conteudo_base": "A presente medida protetiva terá validade de 06 (seis) meses a contar desta decisão. Em caso de necessidade de prorrogação, a parte interessada deverá comparecer perante a secretaria deste juízo para requerer e justificar tal necessidade."
    },
    {
      "tipo": "adaptavel",
      "identificador": "determinacoes_finais",
      "conteudo_base": "Dê-se ciência ao autor do fato, {NOME_REQUERIDO}, de que o descumprimento da presente decisão pode configurar nova infração penal.\n\nCorrija a distribuição, se necessário for.\n\nSaliento que eventual ação principal deve ser distribuída no PJe e que incumbe à parte interessada inserir nos novos autos as provas produzidas.\n\nIntimadas as partes, arquivem-se os autos."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```
