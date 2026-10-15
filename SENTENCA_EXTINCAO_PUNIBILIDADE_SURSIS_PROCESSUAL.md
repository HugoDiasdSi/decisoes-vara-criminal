

```json
{
  "filename": "SENTENCA_EXTINCAO_PUNIBILIDADE_SURSIS_PROCESSUAL.md",
  "tags": [
    "sentença",
    "extinção de punibilidade",
    "sursis processual",
    "suspensão condicional do processo",
    "lei 9.099/95"
  ],
  "descricao": "Modelo de sentença que declara a extinção da punibilidade do agente em razão do integral cumprimento da Suspensão Condicional do Processo, com base no art. 89, § 5º, da Lei n. 9.099/95.",
  "titulo": "SENTENÇA DE EXTINÇÃO DA PUNIBILIDADE (CUMPRIMENTO DE SURSIS PROCESSUAL)",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Cuida-se de ação penal instaurada pelo Ministério Público em face do(a) acusado(a) {NOME_ACUSADO} apontando-o(a) como incurso(a) no delito previsto na inicial.\n\nFoi concedida a suspensão condicional do processo (ID {ID_DECISAO_SURSIS}).\n\nConsta nos autos certidão de que o(a) acusado(a) cumpriu o período de prova sem qualquer descumprimento das condições estipuladas (ID {ID_CERTIDAO_CUMPRIMENTO}).\n\nRelatei. Decido."
    },
    {
      "tipo": "fixo",
      "conteudo": "O(A) autor(a) cumpriu as condições do benefício no período de prova tendo, portanto, direito à declaração, por sentença, da extinção da punibilidade, nos termos do art. 89, § 5º, da Lei n. 9.099/1995."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_punibilidade",
      "conteudo_base": "Posto isso, **declaro, por sentença, a EXTINÇÃO DA PUNIBILIDADE de {NOME_ACUSADO}**, em relação ao delito objeto deste Processo."
    },
    {
      "tipo": "condicional",
      "identificador": "restituicao_fianca",
      "descricao": "Usar este bloco se houver valor de fiança depositado nos autos e não houver notícia de quebra das condições.",
      "conteudo_base": "Não há notícias nos autos de conduta que configure quebra de fiança, assim, com o trânsito em julgado, expeça-se alvará para levantamento da fiança em nome do(a) autor(a) do fato, acaso existente."
    },
    {
      "tipo": "condicional",
      "identificador": "destinacao_bens_apreendidos",
      "descricao": "Usar este bloco se houver bens apreendidos (armas, munições e acessórios, veículos, aparelhos celulares, numerário, drogas, demais objetos) ou fiança sem destinação já dada e individualizada nos autos. Incluir só os parágrafos pertinentes. Cada item deve ser individualizado no corpo do ato com os dados constantes dos autos, sem fórmula genérica ('armas porventura apreendidas', 'bens apreendidos') e sem remissão a anexo ou planilha. Armas: espécie, marca, calibre, número de série, NIAF, número e ID do laudo e número do caso NIAF/CORE; sem laudo nos autos, requisitar ao Instituto de Criminalística em 48 horas e determinar a destruição após a juntada; proprietário com CRAF, restituição; demais regras na seção 'Destinação de Bens Apreendidos e Fiança' do SKILL.md (IN Conjunta TJPE n. 24/2020 e Ofício-Circular n. 09/2026-CGJ). Se o modelo já tiver bloco próprio sobre fiança, usar aquele para a fiança.",
      "conteudo_base": "Quanto ao armamento apreendido, juntado o laudo pericial ({NUMERO_E_ID_DO_LAUDO}) e não mais interessando à persecução penal, **determino o encaminhamento ao Comando do Exército, para destruição**, por intermédio do Núcleo de Identificação de Armas de Fogo do Comando de Operações e Recursos Especiais da Polícia Civil de Pernambuco (NIAF/CORE/PCPE), de {ESPECIE_MARCA_CALIBRE_NUMERO_DE_SERIE_NIAF_E_CASO_NIAF_CORE}, bem como de eventuais munições e acessórios correspondentes, nos termos do art. 25 da Lei n. 10.826/2003. Comunique-se imediatamente, por meio eletrônico, ao NIAF/CORE/PCPE e à Secretaria de Defesa Social (art. 5º, § 4º, da Instrução Normativa Conjunta TJPE n. 24/2020), com cópia deste ato, que servirá como ofício.\n\nQuanto ao veículo {MARCA_MODELO_COR_PLACA_CHASSI_E_RENAVAM} (ID {ID_DO_AUTO_DE_APREENSAO}), {DESTINACAO_DO_VEICULO}.\n\nQuanto aos demais bens apreendidos, {DESCRICAO_INDIVIDUALIZADA_DE_CADA_BEM_E_RESPECTIVA_DESTINACAO}.\n\nQuanto à fiança recolhida no valor de {VALOR} (ID {ID_DO_COMPROVANTE}), {DESTINACAO_DA_FIANCA}."
    },
    {
      "tipo": "fixo",
      "conteudo": "Intimações necessárias.\n\nCumpra-se.\n\nCertificado o trânsito em julgado, proceda-se à baixa na distribuição и ao arquivamento."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```