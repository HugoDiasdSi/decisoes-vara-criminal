Com base na decisão fornecida, realizei a catalogação, identificando os blocos fixos e adaptáveis, e aplicando todas as regras de formatação e estilo. O resultado está no formato JSON abaixo.

```json
{
  "filename": "INDEFERIMENTO_EXAME_TOXICOLOGICO.md",
  "tags": [
    "indeferimento",
    "exame toxicológico",
    "insanidade mental",
    "decisão interlocutória",
    "diligência"
  ],
  "descricao": "Modelo de decisão que indefere pedido de exame toxicológico formulado pela defesa, com base na discricionariedade motivada do magistrado e na ausência de dúvida razoável sobre a higidez mental do réu, conforme jurisprudência do STJ.",
  "titulo": "INDEFERIMENTO DE EXAME TOXICOLÓGICO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_pedido_exame",
      "conteudo_base": "Cuida-se de pedido da defesa para que seja realizado exame toxicológico no réu {NOME_REU}.\n\nEis o relato, em síntese."
    },
    {
      "tipo": "fixo",
      "conteudo": "Sobre o tema, veja-se o recente julgado da Quinta Turma do Superior Tribunal de Justiça:\n\n> AGRAVO REGIMENTAL EM HABEAS CORPUS. CÁRCERE PRIVADO. PLEITO DEFENSIVO DE REALIZAÇÃO DE EXAME TOXICOLÓGICO PARA AFERIÇÃO DE INIMPUTABILIDADE OU SEMI-IMPUTABILIDADE DO PACIENTE. INDEFERIMENTO. NULIDADE. NÃO OCORRÊNCIA. MODIFICAÇÃO DAS CONCLUSÕES DAS INSTÂNCIAS ORDINÁRIAS. IMPOSSIBILIDADE. REEXAME FÁTICO/PROBATÓRIO DOS AUTOS. AGRAVO REGIMENTAL A QUE SE NEGA PROVIMENTO. 1. **A realização do exame de insanidade mental não é automática ou obrigatória, devendo existir dúvida razoável acerca da higidez mental do acusado para o seu deferimento.** 2. A alegação de dependência química de substâncias entorpecentes por parte do réu não implica obrigatoriedade de realização do exame toxicológico, **ficando a análise de sua necessidade dentro do âmbito de discricionariedade motivada do Magistrado**. 3. No caso, as instâncias ordinárias firmaram entendimento no sentido de que não existiriam provas no caderno processual ou ao menos indícios, de que o réu, ao tempo da infração, tivesse a capacidade de autodeterminação comprometida, de maneira que não se fazia útil o exame toxicológico. Para modificar tal conclusão, seria necessário o aprofundado reexame do acervo probatório da ação penal, providência que, sabidamente, é inviável na via estreita do habeas corpus. 4. Agravo regimental a que se nega provimento. (AgRg no HC n. 895.926/GO, relator Ministro Reynaldo Soares da Fonseca, Quinta Turma, julgado em 13/5/2024, DJe de 15/5/2024.)"
    },
    {
      "tipo": "adaptavel",
      "identificador": "aplicacao_caso_concreto",
      "conteudo_base": "No presente caso, não há elementos nos autos que apontem comprometimento da capacidade de autodeterminação do réu em decorrência da alegada dependência química, inexistindo, portanto, dúvida razoável quanto à sua higidez mental."
    },
    {
      "tipo": "fixo",
      "conteudo": "Dessa forma, **indefiro o pedido de exame toxicológico**, na esteira do entendimento do STJ."
    },
    {
      "tipo": "adaptavel",
      "identificador": "determinacoes_finais",
      "conteudo_base": "Cumpra-se a decisão de ID {ID_DECISAO_ANTERIOR}.\n\nAguarde-se a realização da audiência, com as intimações necessárias."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```