
```json
{
  "filename": "SENTENCA_EXTINCAO_PUNIBILIDADE_MORTE_AGENTE.md",
  "tags": [
    "sentença",
    "extinção de punibilidade",
    "morte do agente",
    "art. 107 cpb"
  ],
  "descricao": "Modelo de sentença que declara a extinção da punibilidade do acusado em razão de seu falecimento, com base no art. 107, I, do Código Penal.",
  "titulo": "SENTENÇA DE EXTINÇÃO DA PUNIBILIDADE PELA MORTE DO AGENTE",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Trata-se de ação penal contra o(a) acusado(a) {NOME_ACUSADO} na qual se imputou a prática delituosa descrita da inicial.\n\nHá informações acerca do óbito do(a) acusado(a) (ID {ID_CERTIDAO_OBITO}).\n\nCom vista dos autos, o MP requereu a extinção da punibilidade (ID {ID_PARECER_MP}).\n\nEis um relato, no essencial, do processo.\n\nDecido."
    },
    {
      "tipo": "fixo",
      "conteudo": "O art. 107 do CPB traz causas de extinção de punibilidade. Encontra-se, dentre tais causas, a morte do agente:\n\n> Art. 107 - Extingue-se a punibilidade:\n> I - pela morte do agente;"
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_extincao_punibilidade",
      "conteudo_base": "Diante dessas considerações, decreto a **EXTINÇÃO DA PUNIBILIDADE** do(a) acusado(a) **{NOME_ACUSADO}** em relação aos fatos narrados nestes autos."
    },
    {
      "tipo": "condicional",
      "identificador": "providencias_adicionais",
      "descricao": "Usar este bloco se houver audiência designada ou apreensão de drogas/armas nos autos.",
      "conteudo_base": "Cancele-se a audiência porventura designada e remeta-se a droga/arma apreendida para destruição, caso pertinente."
    },
    {
      "tipo": "condicional",
      "identificador": "destinacao_bens_apreendidos",
      "descricao": "Usar este bloco se houver bens apreendidos (armas, munições e acessórios, veículos, aparelhos celulares, numerário, drogas, demais objetos) ou fiança sem destinação já dada e individualizada nos autos. Incluir só os parágrafos pertinentes. Cada item deve ser individualizado no corpo do ato com os dados constantes dos autos, sem fórmula genérica ('armas porventura apreendidas', 'bens apreendidos') e sem remissão a anexo ou planilha. Armas: espécie, marca, calibre, número de série, NIAF, número e ID do laudo e número do caso NIAF/CORE; sem laudo nos autos, requisitar ao Instituto de Criminalística em 48 horas e determinar a destruição após a juntada; proprietário com CRAF, restituição; demais regras na seção 'Destinação de Bens Apreendidos e Fiança' do SKILL.md (IN Conjunta TJPE n. 24/2020 e Ofício-Circular n. 09/2026-CGJ). Se o modelo já tiver bloco próprio sobre fiança, usar aquele para a fiança.",
      "conteudo_base": "Quanto ao armamento apreendido, juntado o laudo pericial ({NUMERO_E_ID_DO_LAUDO}) e não mais interessando à persecução penal, **determino o encaminhamento ao Comando do Exército, para destruição**, por intermédio do Núcleo de Identificação de Armas de Fogo do Comando de Operações e Recursos Especiais da Polícia Civil de Pernambuco (NIAF/CORE/PCPE), de {ESPECIE_MARCA_CALIBRE_NUMERO_DE_SERIE_NIAF_E_CASO_NIAF_CORE}, bem como de eventuais munições e acessórios correspondentes, nos termos do art. 25 da Lei n. 10.826/2003. Comunique-se imediatamente, por meio eletrônico, ao NIAF/CORE/PCPE e à Secretaria de Defesa Social (art. 5º, § 4º, da Instrução Normativa Conjunta TJPE n. 24/2020), com cópia deste ato, que servirá como ofício.\n\nQuanto ao veículo {MARCA_MODELO_COR_PLACA_CHASSI_E_RENAVAM} (ID {ID_DO_AUTO_DE_APREENSAO}), {DESTINACAO_DO_VEICULO}.\n\nQuanto aos demais bens apreendidos, {DESCRICAO_INDIVIDUALIZADA_DE_CADA_BEM_E_RESPECTIVA_DESTINACAO}.\n\nQuanto à fiança recolhida no valor de {VALOR} (ID {ID_DO_COMPROVANTE}), {DESTINACAO_DA_FIANCA}."
    },
    {
      "tipo": "fixo",
      "conteudo": "Demais expedientes necessários.\n\nApós, arquive-se, dando-se a devida baixa.\n\nSem custas.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```