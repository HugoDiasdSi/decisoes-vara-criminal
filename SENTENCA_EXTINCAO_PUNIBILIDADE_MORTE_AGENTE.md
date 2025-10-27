
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