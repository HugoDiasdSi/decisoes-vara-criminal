cando todas as regras de formatação e estilo. O resultado está no formato JSON abaixo.

```json
{
  "filename": "SENTENCA_EXTINCAO_PUNIBILIDADE_TRANSACAO_PENAL.md",
  "tags": [
    "sentença",
    "extinção de punibilidade",
    "transação penal",
    "lei 9.099/95",
    "JECRIM"
  ],
  "descricao": "Modelo de sentença que declara a extinção da punibilidade do agente em razão do integral cumprimento da Transação Penal, com base no art. 84, parágrafo único, da Lei n. 9.099/95.",
  "titulo": "SENTENÇA DE EXTINÇÃO DA PUNIBILIDADE (CUMPRIMENTO DE TRANSAÇÃO PENAL)",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Cuida-se de procedimento policial contra o(a) imputado(a) {NOME_ACUSADO}, apontando-o(a) como incurso(a) no delito previsto nos documentos informativos.\n\nFoi concedida a transação penal.\n\nO Ministério Público requereu a extinção da punibilidade pelo cumprimento das condições impostas (ID {ID_PARECER_MP}).\n\nRelatei. Decido."
    },
    {
      "tipo": "fixo",
      "conteudo": "O(A) ré(u) cumpriu as condições do benefício no período de prova tendo, portanto, direito à declaração, por sentença, da extinção da punibilidade, nos termos do art. 84, parágrafo único, da Lei n. 9.099/1995."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_punibilidade",
      "conteudo_base": "Posto isso, **declaro, por sentença, a extinção da punibilidade de {NOME_ACUSADO}**, em relação ao delito objeto deste processo."
    },
    {
      "tipo": "condicional",
      "identificador": "destinacao_fianca_transacao_penal",
      "descricao": "Usar este bloco se houver valor de fiança a ser destinado conforme a Transação Penal.",
      "conteudo_base": "Quanto aos valores porventura pagos pelo(a) autuado(a) a título de fiança, se estes tiverem sido objeto da transação penal celebrada nos autos, oficie-se à autoridade policial, caso ainda não tenha sido providenciado, para que remeta a este Juízo o comprovante de depósito correspondente, no prazo de 15 (quinze) dias.\n\nEm sendo pertinente, transfiram-se os valores depositados para a Conta Estadual de Destinação de Prestações Pecuniárias, instituída pelo Provimento Conjunto nº 02, de 14 de novembro de 2024 com dados bancários a seguir - Banco do Brasil S/A, Agência: 3234, Conta-Corrente Judicial: 3000116084860, Favorecido: Tribunal de Justiça de Pernambuco – UG Penas Pecuniárias, CNPJ: 11.431.327/0001-34."
    },
    {
      "tipo": "condicional",
      "identificador": "destinacao_bens_apreendidos",
      "descricao": "Usar este bloco se houver bens apreendidos (armas, munições e acessórios, veículos, aparelhos celulares, numerário, drogas, demais objetos) ou fiança sem destinação já dada e individualizada nos autos. Incluir só os parágrafos pertinentes. Cada item deve ser individualizado no corpo do ato com os dados constantes dos autos, sem fórmula genérica ('armas porventura apreendidas', 'bens apreendidos') e sem remissão a anexo ou planilha. Armas: espécie, marca, calibre, número de série, NIAF, número e ID do laudo e número do caso NIAF/CORE; sem laudo nos autos, requisitar ao Instituto de Criminalística em 48 horas e determinar a destruição após a juntada; proprietário com CRAF, restituição; demais regras na seção 'Destinação de Bens Apreendidos e Fiança' do SKILL.md (IN Conjunta TJPE n. 24/2020 e Ofício-Circular n. 09/2026-CGJ). Se o modelo já tiver bloco próprio sobre fiança, usar aquele para a fiança.",
      "conteudo_base": "Quanto ao armamento apreendido, juntado o laudo pericial ({NUMERO_E_ID_DO_LAUDO}) e não mais interessando à persecução penal, **determino o encaminhamento ao Comando do Exército, para destruição**, por intermédio do Núcleo de Identificação de Armas de Fogo do Comando de Operações e Recursos Especiais da Polícia Civil de Pernambuco (NIAF/CORE/PCPE), de {ESPECIE_MARCA_CALIBRE_NUMERO_DE_SERIE_NIAF_E_CASO_NIAF_CORE}, bem como de eventuais munições e acessórios correspondentes, nos termos do art. 25 da Lei n. 10.826/2003. Comunique-se imediatamente, por meio eletrônico, ao NIAF/CORE/PCPE e à Secretaria de Defesa Social (art. 5º, § 4º, da Instrução Normativa Conjunta TJPE n. 24/2020), com cópia deste ato, que servirá como ofício.\n\nQuanto ao veículo {MARCA_MODELO_COR_PLACA_CHASSI_E_RENAVAM} (ID {ID_DO_AUTO_DE_APREENSAO}), {DESTINACAO_DO_VEICULO}.\n\nQuanto aos demais bens apreendidos, {DESCRICAO_INDIVIDUALIZADA_DE_CADA_BEM_E_RESPECTIVA_DESTINACAO}.\n\nQuanto à fiança recolhida no valor de {VALOR} (ID {ID_DO_COMPROVANTE}), {DESTINACAO_DA_FIANCA}."
    },
    {
      "tipo": "fixo",
      "conteudo": "Com o cumprimento de todas as determinações, arquivem-se os autos com as cautelas de praxe."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```