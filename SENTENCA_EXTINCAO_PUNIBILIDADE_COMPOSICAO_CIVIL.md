

```json
{
  "filename": "SENTENCA_EXTINCAO_PUNIBILIDADE_COMPOSICAO_CIVIL.md",
  "tags": [
    "sentença",
    "extinção de punibilidade",
    "composição civil",
    "renúncia",
    "lei 9.099/95",
    "JECRIM"
  ],
  "descricao": "Modelo de sentença que homologa a composição civil dos danos e declara a extinção da punibilidade do autor do fato em razão da renúncia da vítima ao direito de representação, nos termos da Lei n. 9.099/95.",
  "titulo": "SENTENÇA DE EXTINÇÃO DA PUNIBILIDADE (COMPOSIÇÃO CIVIL)",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Trata-se de TCO instaurado em virtude da suposta prática do delito ali descrito.\n\nVerifico que as partes celebraram uma composição civil na audiência preliminar.\n\nAssim, a(s) vítima(s) renunciou(aram) expressamente à representação oferecida na delegacia de polícia."
    },
    {
      "tipo": "fixo",
      "conteudo": "Desse modo, nos termos do art. 104, parágrafo único, do CPB, resta inviabilizada condição de procedibilidade da ação penal."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_punibilidade",
      "conteudo_base": "Diante do exposto, **HOMOLOGO A RENÚNCIA e DECLARO EXTINTA A PUNIBILIDADE de {NOME_AUTOR_DO_FATO}**, qualificado(a) nos autos, quanto à infração capitulada nos autos, com fundamento nos artigos 102, 104, parágrafo único, e 107, V, todos do Código Penal, e artigos 25 e 61 do Código de Processo Penal."
    },
    {
      "tipo": "condicional",
      "identificador": "destinacao_valores_pecuniarios",
      "descricao": "Usar este bloco se, como parte da composição civil, foi acordado o pagamento de valor a ser destinado a fundos públicos.",
      "conteudo_base": "Em sendo pertinente, transfiram-se os valores depositados para a Conta Estadual de Destinação de Prestações Pecuniárias, instituída pelo Provimento Conjunto nº 02, de 14 de novembro de 2024 com dados bancários a seguir - Banco do Brasil S/A, Agência: 3234, Conta-Corrente Judicial: 3000116084860, Favorecido: Tribunal de Justiça de Pernambuco – UG Penas Pecuniárias, CNPJ: 11.431.327/0001-34."
    },
    {
      "tipo": "condicional",
      "identificador": "destinacao_bens_apreendidos",
      "descricao": "Usar este bloco se houver bens apreendidos (armas, munições e acessórios, veículos, aparelhos celulares, numerário, drogas, demais objetos) ou fiança sem destinação já dada e individualizada nos autos. Incluir só os parágrafos pertinentes. Cada item deve ser individualizado no corpo do ato com os dados constantes dos autos, sem fórmula genérica ('armas porventura apreendidas', 'bens apreendidos') e sem remissão a anexo ou planilha. Armas: espécie, marca, calibre, número de série, NIAF, número e ID do laudo e número do caso NIAF/CORE; sem laudo nos autos, requisitar ao Instituto de Criminalística em 48 horas e determinar a destruição após a juntada; proprietário com CRAF, restituição; demais regras na seção 'Destinação de Bens Apreendidos e Fiança' do SKILL.md (IN Conjunta TJPE n. 24/2020 e Ofício-Circular n. 09/2026-CGJ). Se o modelo já tiver bloco próprio sobre fiança, usar aquele para a fiança.",
      "conteudo_base": "Quanto ao armamento apreendido, juntado o laudo pericial ({NUMERO_E_ID_DO_LAUDO}) e não mais interessando à persecução penal, **determino o encaminhamento ao Comando do Exército, para destruição**, por intermédio do Núcleo de Identificação de Armas de Fogo do Comando de Operações e Recursos Especiais da Polícia Civil de Pernambuco (NIAF/CORE/PCPE), de {ESPECIE_MARCA_CALIBRE_NUMERO_DE_SERIE_NIAF_E_CASO_NIAF_CORE}, bem como de eventuais munições e acessórios correspondentes, nos termos do art. 25 da Lei n. 10.826/2003. Comunique-se imediatamente, por meio eletrônico, ao NIAF/CORE/PCPE e à Secretaria de Defesa Social (art. 5º, § 4º, da Instrução Normativa Conjunta TJPE n. 24/2020), com cópia deste ato, que servirá como ofício.\n\nQuanto ao veículo {MARCA_MODELO_COR_PLACA_CHASSI_E_RENAVAM} (ID {ID_DO_AUTO_DE_APREENSAO}), {DESTINACAO_DO_VEICULO}.\n\nQuanto aos demais bens apreendidos, {DESCRICAO_INDIVIDUALIZADA_DE_CADA_BEM_E_RESPECTIVA_DESTINACAO}.\n\nQuanto à fiança recolhida no valor de {VALOR} (ID {ID_DO_COMPROVANTE}), {DESTINACAO_DA_FIANCA}."
    },
    {
      "tipo": "fixo",
      "conteudo": "Após o trânsito em julgado, arquivem-se os presentes autos.\n\nObserve-se o Enunciado 105 do FONAJE.\n\nSem custas."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```