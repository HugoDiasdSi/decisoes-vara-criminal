

```json
{
  "filename": "ARQUIVAMENTO_IP_TCO_ACOLHENDO_MP.md",
  "tags": [
    "arquivamento",
    "inquérito policial",
    "TCO",
    "promoção ministerial",
    "decisão",
    "art. 28 cpp"
  ],
  "descricao": "Modelo de decisão que acolhe a promoção do Ministério Público e determina o arquivamento de Inquérito Policial ou Termo Circunstanciado de Ocorrência, adotando os fundamentos ministeriais como razão de decidir.",
  "titulo": "ARQUIVAMENTO DE INQUÉRITO POLICIAL / TCO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_pedido_mp",
      "conteudo_base": "O ilustre representante do Ministério Público requereu o arquivamento dos autos do inquérito policial/TCO epigrafado (ID {ID_PROMOCAO_MP})."
    },
    {
      "tipo": "fixo",
      "identificador": "fundamentacao_per_relationem",
      "conteudo": "Assiste razão ao Ministério Público.\n\nÉ necessário distinguir o motivo que fundamenta a decisão acolhedora do pedido de arquivamento, vez que, a depender das razões, a decisão ensejará, ou não, a formação de coisa julgada material, inviabilizando a reabertura das investigações na forma do art. 18 do CPP.\n\nNeste particular, para evitar repetições, tomo como base e razão de decidir a embasada promoção de arquivamento acostada aos autos, tornando-a parte integrante desta decisão."
    },
    {
      "tipo": "fixo",
      "identificador": "dispositivo_arquivamento",
      "conteudo": "Posto isso e atento ao que preceitua os arts. 18 e 28 do CPP, **determino o ARQUIVAMENTO** dos autos deste procedimento informativo."
    },
    {
      "tipo": "condicional",
      "identificador": "destruicao_droga",
      "descricao": "Usar este bloco se houver droga apreendida nos autos.",
      "conteudo_base": "Destrua-se a droga apreendida, caso pertinente."
    },
    {
      "tipo": "condicional",
      "identificador": "destinacao_bens_apreendidos",
      "descricao": "Usar este bloco se houver bens apreendidos (armas, munições e acessórios, veículos, aparelhos celulares, numerário, drogas, demais objetos) ou fiança sem destinação já dada e individualizada nos autos. Incluir só os parágrafos pertinentes. Cada item deve ser individualizado no corpo do ato com os dados constantes dos autos, sem fórmula genérica ('armas porventura apreendidas', 'bens apreendidos') e sem remissão a anexo ou planilha. Armas: espécie, marca, calibre, número de série, NIAF, número e ID do laudo e número do caso NIAF/CORE; sem laudo nos autos, requisitar ao Instituto de Criminalística em 48 horas e determinar a destruição após a juntada; proprietário com CRAF, restituição; demais regras na seção 'Destinação de Bens Apreendidos e Fiança' do SKILL.md (IN Conjunta TJPE n. 24/2020 e Ofício-Circular n. 09/2026-CGJ). Se o modelo já tiver bloco próprio sobre fiança, usar aquele para a fiança.",
      "conteudo_base": "Quanto ao armamento apreendido, juntado o laudo pericial ({NUMERO_E_ID_DO_LAUDO}) e não mais interessando à persecução penal, **determino o encaminhamento ao Comando do Exército, para destruição**, por intermédio do Núcleo de Identificação de Armas de Fogo do Comando de Operações e Recursos Especiais da Polícia Civil de Pernambuco (NIAF/CORE/PCPE), de {ESPECIE_MARCA_CALIBRE_NUMERO_DE_SERIE_NIAF_E_CASO_NIAF_CORE}, bem como de eventuais munições e acessórios correspondentes, nos termos do art. 25 da Lei n. 10.826/2003. Comunique-se imediatamente, por meio eletrônico, ao NIAF/CORE/PCPE e à Secretaria de Defesa Social (art. 5º, § 4º, da Instrução Normativa Conjunta TJPE n. 24/2020), com cópia deste ato, que servirá como ofício.\n\nQuanto ao veículo {MARCA_MODELO_COR_PLACA_CHASSI_E_RENAVAM} (ID {ID_DO_AUTO_DE_APREENSAO}), {DESTINACAO_DO_VEICULO}.\n\nQuanto aos demais bens apreendidos, {DESCRICAO_INDIVIDUALIZADA_DE_CADA_BEM_E_RESPECTIVA_DESTINACAO}.\n\nQuanto à fiança recolhida no valor de {VALOR} (ID {ID_DO_COMPROVANTE}), {DESTINACAO_DA_FIANCA}."
    },
    {
      "tipo": "fixo",
      "identificador": "determinacoes_finais",
      "conteudo": "Diligências e intimações necessárias.\n\nApós as anotações de estilo, arquivem-se com baixa na distribuição.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```
