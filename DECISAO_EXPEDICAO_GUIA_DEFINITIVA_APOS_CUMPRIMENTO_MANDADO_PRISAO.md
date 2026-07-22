
```json
{
  "filename": "DECISAO_EXPEDICAO_GUIA_DEFINITIVA_APOS_CUMPRIMENTO_MANDADO_PRISAO.md",
  "tags": [
    "guia de recolhimento definitiva",
    "carta de guia",
    "cumprimento de mandado de prisão",
    "trânsito em julgado",
    "execução penal",
    "regime fechado",
    "arquivamento",
    "decisão"
  ],
  "descricao": "Modelo de decisão proferida nos autos principais já sentenciados e transitados em julgado que, diante da notícia de cumprimento do mandado de prisão definitiva, determina a expedição da guia de recolhimento definitiva, sua remessa ao juízo da execução penal por malote digital e o subsequente arquivamento dos autos.",
  "titulo": "DECISÃO - EXPEDIÇÃO DE GUIA DEFINITIVA APÓS CUMPRIMENTO DE MANDADO DE PRISÃO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado. Substituir integralmente todos os dados entre chaves pelos do caso concreto, sem manter qualquer informação do processo de origem. Manter o relatório enxuto: a decisão é de mero cumprimento de título executivo penal, não comportando fundamentação analítica sobre a prisão nem sobre matéria afeta ao juízo da execução.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_sentenca_transito",
      "descricao": "Sintetizar a sentença condenatória e o trânsito em julgado. Havendo corréus, descrever a situação de cada um em período próprio da mesma frase, como no conteúdo base.",
      "conteudo_base": "Trata-se de ação penal em que foi proferida sentença condenatória (ID {ID_SENTENCA}), transitada em julgado em {DATA_TRANSITO_DEFESA} para a defesa e em {DATA_TRANSITO_MP} para o Ministério Público, na qual {NOME_REU_PRESO} foi condenado nas penas do art. {DISPOSITIVO_LEGAL_REU_PRESO}, à pena definitiva de {PENA_REU_PRESO} e {MULTA_REU_PRESO}, em regime inicial {REGIME_REU_PRESO}, e {NOME_CORREU} foi condenado nas penas do art. {DISPOSITIVO_LEGAL_CORREU}, à pena de {PENA_CORREU} e {MULTA_CORREU}, em regime inicial {REGIME_CORREU}, substituída a pena privativa de liberdade por {SUBSTITUICAO_CORREU}."
    },
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_mandado_expedido",
      "conteudo_base": "Com o trânsito em julgado, quanto a {NOME_REU_PRESO}, por se manter o regime {REGIME_REU_PRESO}, expediu-se em {DATA_EXPEDICAO_MANDADO} o mandado de prisão definitiva n. {NUMERO_MANDADO} (ID {ID_MANDADO}), permanecendo os autos no aguardo da captura, conforme certificado em {DATA_CERTIDAO} (ID {ID_CERTIDAO})."
    },
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_noticia_captura",
      "conteudo_base": "Sobreveio agora ofício {ORGAO_COMUNICANTE} (ID {ID_OFICIO_CUMPRIMENTO}), noticiando o cumprimento do mandado. Extrai-se do boletim de ocorrência n. {NUMERO_BOLETIM} que o sentenciado foi capturado em {DATA_CAPTURA}, às {HORA_CAPTURA}."
    },
    {
      "tipo": "fixo",
      "conteudo": "Este é, em apertada síntese, o relatório.\n\nDecido."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_guia_definitiva",
      "conteudo_base": "Determino a expedição da guia de recolhimento definitiva em desfavor de {NOME_REU_PRESO}, instruída com as peças pertinentes, remetendo-se ao juízo da execução penal competente, por malote digital."
    },
    {
      "tipo": "condicional",
      "identificador": "corregu_guia_pendente",
      "descricao": "Incluir apenas se ainda estiver pendente a expedição de guia ou de outra providência executória em relação a corréu.",
      "conteudo_base": "Expeça-se, igualmente, a guia de execução definitiva em desfavor de {NOME_CORREU}, remetendo-a ao juízo da execução penal competente."
    },
    {
      "tipo": "fixo",
      "conteudo": "Cumpridas todas as determinações e nada mais sendo requerido, arquivem-se os autos com as cautelas de praxe.\n\nDiligências, expedientes e intimações necessárias.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}/PE, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```
