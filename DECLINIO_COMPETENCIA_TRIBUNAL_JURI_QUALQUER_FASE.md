

```json
{
  "filename": "DECLINIO_COMPETENCIA_TRIBUNAL_JURI_QUALQUER_FASE.json",
  "tags": [
    "declínio de competência",
    "tribunal do júri",
    "crime doloso contra a vida",
    "competência absoluta",
    "1ª Vara Criminal de Camaragibe",
    "inquérito policial",
    "medida cautelar pendente",
    "prisão temporária",
    "decisão"
  ],
  "descricao": "Modelo de decisão que declina da competência à vara do Tribunal do Júri da comarca (em Camaragibe, a 1ª Vara Criminal) sempre que o crime imputado for doloso contra a vida, EM QUALQUER FASE — inquérito, pré-processual ou processual. A competência é absoluta e fixada em razão da matéria: a fase do feito é irrelevante. Alcança também as medidas cautelares requeridas, que por isso não são apreciadas antes do declínio. Para crime comum em fase pré-processual, o declínio é ao juízo de garantias (arts. 3º-B e 3º-C do CPP) — usar outro modelo. Decisão de praxe: texto curto, sem digressão.",
  "titulo": "DECLÍNIO DE COMPETÊNCIA AO TRIBUNAL DO JÚRI",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável. REGRA DE SELEÇÃO: usar este modelo sempre que o crime imputado for doloso contra a vida, independentemente da fase do feito; não mencionar juízo de garantias nem os arts. 3º-B e 3º-C do CPP, que aqui não incidem. Manter o texto enxuto: dois parágrafos de fundamentação bastam. Não apreciar o mérito da medida cautelar pendente, sob pena de exercer a jurisdição de que se declina. Aplicar os negritos apenas onde indicados: nome do investigado e comandos do dispositivo.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_objeto",
      "descricao": "Adaptar conforme a fase: inquérito policial, ação penal já instaurada ou comunicação de flagrante.",
      "conteudo_base": "Trata-se de inquérito policial n. {NUMERO_IP}, instaurado em {DATA_INSTAURACAO}, no qual se apura a suposta prática, por **{NOME_INVESTIGADO}**, do crime {DESCRICAO_DO_CRIME}, fatos ocorridos em {DATA_DOS_FATOS}, {LOCAL_DOS_FATOS}."
    },
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_conclusao_e_ato_pendente",
      "conteudo_base": "Os autos foram distribuídos a este juízo em {DATA_DISTRIBUICAO} e vieram conclusos em {DATA_CONCLUSAO}, com {ATO_PENDENTE} (ID {ID_ATO_PENDENTE})."
    },
    {
      "tipo": "fixo",
      "identificador": "encerramento_relatorio",
      "conteudo": "Eis um relato, no essencial, do feito.\n\nDecido."
    },
    {
      "tipo": "fixo",
      "identificador": "fundamentacao_competencia_juri",
      "conteudo": "Os fatos apurados amoldam-se, em tese, a crime doloso contra a vida, cuja competência para o processo e julgamento é do Tribunal do Júri, nos termos do art. 5º, XXXVIII, \"d\", da Constituição Federal e do art. 74, § 1º, do Código de Processo Penal.\n\nTrata-se de competência absoluta, fixada em razão da matéria, que não se altera pela fase em que se encontra o feito, e que alcança as medidas cautelares nele requeridas."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_declinio",
      "descricao": "Quando não houver cautelar pendente, suprimir o trecho final a partir de 'deixando de apreciar'.",
      "conteudo_base": "Diante do exposto, **declino da competência** para a Vara do Tribunal do Júri desta comarca e determino a **remessa imediata dos autos** àquele juízo, deixando de apreciar {MEDIDA_PENDENTE} do investigado **{NOME_INVESTIGADO}**."
    },
    {
      "tipo": "condicional",
      "identificador": "prioridade_por_cautelar_pendente",
      "descricao": "Incluir quando houver medida cautelar pendente de apreciação (prisão temporária, preventiva, busca e apreensão, quebra de sigilo e afins), para que a remessa não retarde o exame da urgência pelo juízo competente.",
      "conteudo_base": "Considerando que {MEDIDA_PENDENTE} pende de análise e que se trata de medida de natureza urgente, dê-se à remessa caráter prioritário."
    },
    {
      "tipo": "fixo",
      "identificador": "determinacoes_finais",
      "conteudo": "Diligências e intimações necessárias.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}/PE, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```
