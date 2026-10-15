```json
{
  "filename": "CUMPRIMENTO_CARTA_PRECATORIA.md",
  "tags": [
    "carta precatória",
    "cumpra-se",
    "despacho",
    "cooperação jurisdicional",
    "declínio de competência",
    "incompetência em razão da matéria"
  ],
  "descricao": "Modelo de despacho padrão ('cumpra-se') para processamento de carta precatória, com instruções detalhadas para a secretaria em caso de cumprimento positivo, negativo (por mudança de endereço ou outros motivos) e para designação de audiência; se o processo de origem versar sobre matéria para a qual a 2ª Vara Criminal de Camaragibe é incompetente (crimes dolosos contra a vida, crimes contra criança ou adolescente, violência doméstica e familiar contra a mulher), declina da competência para a vara competente da comarca.",
  "titulo": "DESPACHO - CUMPRA-SE (CARTA PRECATÓRIA)",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "condicional",
      "identificador": "declinio_competencia_materia",
      "descricao": "Incluir, EM SUBSTITUIÇÃO ao bloco fixo de cumprimento, quando o processo de origem do Juízo deprecante versar sobre matéria para a qual a 2ª Vara Criminal de Camaragibe é incompetente: crimes dolosos contra a vida (competência da 1ª Vara Criminal de Camaragibe, Tribunal do Júri); crimes contra criança ou adolescente e violência doméstica e familiar contra a mulher, Lei n. 11.340/2006 (competência da Vara de Violência Doméstica e Familiar contra a Mulher de Camaragibe); ou outra matéria de vara especializada da comarca. Verificar a matéria na denúncia, na decisão ou nos documentos que instruem a precatória (classe, assunto, tipo penal imputado, qualificação da vítima); se a matéria não constar dos documentos, aplicar o bloco fixo e registrar em PONTOS PARA REVISÃO.",
      "conteudo_base": "Trata-se de carta precatória expedida pelo {JUIZO_DEPRECANTE}, extraída dos autos n. {NPU_ORIGEM}, que apuram {DESCRICAO_DA_MATERIA}, para {ATO_DEPRECADO}.\n\nO cumprimento da carta precatória compete ao juízo da comarca deprecada com competência para a matéria do processo de origem. Nesta comarca, {FUNDAMENTO_COMPETENCIA_VARA_COMPETENTE}, de modo que este juízo não detém competência para o cumprimento do ato deprecado.\n\nAnte o exposto, **declino da competência** para o cumprimento desta carta precatória em favor da **{VARA_COMPETENTE}** e determino a **remessa imediata dos autos** àquele juízo, com as baixas necessárias.\n\nInforme-se ao Juízo deprecante."
    },
    {
      "tipo": "fixo",
      "conteudo": "Processe-se com isenção de custas.\n\nCumpra-se conforme requerido.\n\nEm caso de cumprimento positivo, devolva-se com as nossas homenagens.\n\nSe o cumprimento negativo se der em razão da mudança de endereço, deve a Secretaria proceder da seguinte forma: a) sendo conhecido novo endereço, renove-se o ato, caso seja nesta Comarca, ou remeta-se ao Juízo competente para execução do ato (caráter itinerante), devendo ser informado ao Juízo deprecante; b) sendo desconhecido outro endereço, devolva-se com as nossas homenagens.\n\nEm caso de cumprimento negativo por outro motivo, voltem-me conclusos, informando ao Juízo deprecante o motivo do não cumprimento.\n\nCaso o ato deprecado seja a realização de audiência, designe-se a data, com urgência, informando ao Juízo deprecante para que este promova as devidas intimações.",
      "descricao": "Aplicar quando este juízo for competente para a matéria do processo de origem; não incluir se aplicado o bloco declinio_competencia_materia."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```