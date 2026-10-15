

```json
{
  "filename": "SENTENCA_EXTINCAO_DECADENCIA_E_ARQUIVAMENTO.md",
  "tags": [
    "sentença",
    "extinção de punibilidade",
    "decadência",
    "arquivamento",
    "TCO",
    "crimes contra a honra",
    "ameaça"
  ],
  "descricao": "Modelo de sentença que, em um mesmo ato, declara a extinção da punibilidade por decadência em relação a um crime de ação penal privada e, em seguida, determina o arquivamento do feito quanto a outro delito, acolhendo a promoção do Ministério Público.",
  "titulo": "SENTENÇA - EXTINÇÃO POR DECADÊNCIA E ARQUIVAMENTO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Trata-se de TCO, no qual consta como autoras dos fatos {NOME_ACUSADO_1} e {NOME_ACUSADO_2}, às quais se atribui a prática dos delitos previstos no art. 140 e 147, ambos do CPB.\n\nEis, em apertada síntese, um breve relato do fato."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_decadencia",
      "conteudo_base": "O crime previsto no art. 140, do CPB, é de ação penal privada. A queixa/representação deveria ser feita no prazo decadencial de 06 (seis) meses. Consulto a legislação:\n\n> Art. 103 - Salvo disposição expressa em contrário, o ofendido decai do direito de queixa ou de representação se não o exerce dentro do prazo de 6 (seis) meses, contado do dia em que veio a saber quem é o autor do crime, ou, no caso do § 3º do art. 100 deste Código, do dia em que se esgota o prazo para oferecimento da denúncia.\n\nO art. 107 do CPB traz causas de extinção de punibilidade. Dentre tais causas, encontra-se a decadência:\n\n> Art. 107 - Extingue-se a punibilidade:\n> (...)\n> IV - pela prescrição, decadência ou perempção;"
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_decadencia",
      "conteudo_base": "Posto isso, **decreto a EXTINÇÃO DA PUNIBILIDADE, pelo advento da decadência**, das imputadas {NOME_ACUSADO_1} e {NOME_ACUSADO_2} em relação ao delito tipificado no art. 140, do CPB."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_arquivamento",
      "conteudo_base": "Demais disso, o ilustre representante do Ministério Público requereu o arquivamento dos autos do TCO epigrafado em relação ao delito do art. 147, do CPB.\n\nAssiste razão ao MP.\n\nEntretanto, é necessário distinguir bem o motivo que fundamenta a decisão acolhedora do pedido de arquivamento de autos de inquéritos policiais, vez que, a depender das razões suscitadas e aceitas, tal decisão ensejará, ou não, a formação de coisa julgada material, inviabilizando por completo a reabertura das investigações na forma autorizada no art. 18 do CPP.\n\nNeste particular, para evitar maiores repetições, tomo como base e razão de decidir a embasada promoção de arquivamento acostada aos autos, tornando-a parte desta decisão."
    },
    {
      "tipo": "fixo",
      "identificador": "dispositivo_arquivamento",
      "conteudo": "Posto isso e atento ao que preceitua os arts. 18 e 28 do CPP, **determino o ARQUIVAMENTO** dos autos deste procedimento informativo."
    },
    {
      "tipo": "condicional",
      "identificador": "destinacao_bens_apreendidos",
      "descricao": "Usar este bloco se houver bens apreendidos (armas, munições e acessórios, veículos, aparelhos celulares, numerário, drogas, demais objetos) ou fiança sem destinação já dada e individualizada nos autos. Incluir só os parágrafos pertinentes. Cada item deve ser individualizado no corpo do ato com os dados constantes dos autos, sem fórmula genérica ('armas porventura apreendidas', 'bens apreendidos') e sem remissão a anexo ou planilha. Armas: espécie, marca, calibre, número de série, NIAF, número e ID do laudo e número do caso NIAF/CORE; sem laudo nos autos, requisitar ao Instituto de Criminalística em 48 horas e determinar a destruição após a juntada; proprietário com CRAF, restituição; demais regras na seção 'Destinação de Bens Apreendidos e Fiança' do SKILL.md (IN Conjunta TJPE n. 24/2020 e Ofício-Circular n. 09/2026-CGJ). Se o modelo já tiver bloco próprio sobre fiança, usar aquele para a fiança.",
      "conteudo_base": "Quanto ao armamento apreendido, juntado o laudo pericial ({NUMERO_E_ID_DO_LAUDO}) e não mais interessando à persecução penal, **determino o encaminhamento ao Comando do Exército, para destruição**, por intermédio do Núcleo de Identificação de Armas de Fogo do Comando de Operações e Recursos Especiais da Polícia Civil de Pernambuco (NIAF/CORE/PCPE), de {ESPECIE_MARCA_CALIBRE_NUMERO_DE_SERIE_NIAF_E_CASO_NIAF_CORE}, bem como de eventuais munições e acessórios correspondentes, nos termos do art. 25 da Lei n. 10.826/2003. Comunique-se imediatamente, por meio eletrônico, ao NIAF/CORE/PCPE e à Secretaria de Defesa Social (art. 5º, § 4º, da Instrução Normativa Conjunta TJPE n. 24/2020), com cópia deste ato, que servirá como ofício.\n\nQuanto ao veículo {MARCA_MODELO_COR_PLACA_CHASSI_E_RENAVAM} (ID {ID_DO_AUTO_DE_APREENSAO}), {DESTINACAO_DO_VEICULO}.\n\nQuanto aos demais bens apreendidos, {DESCRICAO_INDIVIDUALIZADA_DE_CADA_BEM_E_RESPECTIVA_DESTINACAO}.\n\nQuanto à fiança recolhida no valor de {VALOR} (ID {ID_DO_COMPROVANTE}), {DESTINACAO_DA_FIANCA}."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "Demais expedientes necessários.\n\nApós, arquive-se.\n\nCumpra-se.\n\n{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```