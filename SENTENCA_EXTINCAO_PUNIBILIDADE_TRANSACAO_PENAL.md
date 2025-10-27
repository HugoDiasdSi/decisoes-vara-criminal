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