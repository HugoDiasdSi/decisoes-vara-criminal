

```json
{
  "filename": "RECEBIMENTO_APELACAO_ART_600_CPP.md",
  "tags": [
    "recebimento de apelação",
    "art. 600 cpp",
    "razões em segunda instância",
    "carta de guia provisória",
    "decisão"
  ],
  "descricao": "Modelo de decisão para recebimento de recurso de apelação quando a defesa opta por apresentar as razões diretamente no Tribunal, conforme art. 600, § 4º, do CPP.",
  "titulo": "RECEBIMENTO DE RECURSO DE APELAÇÃO (ART. 600, § 4º, CPP)",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "fixo",
      "conteudo": "**Recebo o recurso de apelação** tempestivamente apresentado."
    },
    {
      "tipo": "condicional",
      "identificador": "razoes_segunda_instancia_art_600_cpp",
      "descricao": "Usar este bloco quando a defesa optar por apresentar as razões da apelação diretamente no Tribunal, conforme art. 600, § 4º, do CPP.",
      "conteudo_base": "Em razão da prerrogativa prevista no art. 600, § 4º, do CPP e utilizada pelo douto defensor, deixo de abrir vista dos presentes autos à parte apelada."
    },
    {
      "tipo": "fixo",
      "conteudo": "Certifique-se se todas as intimações foram providenciadas. Caso negativo, providenciem-se os expedientes faltantes."
    },
    {
      "tipo": "condicional",
      "identificador": "expedicao_carta_guia_provisoria",
      "descricao": "Usar este bloco se o réu estiver preso e a carta de guia provisória ainda não tiver sido expedida.",
      "conteudo_base": "**Expeça-se a competente carta de guia provisória caso o réu {NOME_REU} se encontre preso e ainda não tenha sido providenciada nos autos.**"
    },
    {
      "tipo": "fixo",
      "conteudo": "Remetam-se os autos ao egrégio Tribunal de Justiça do Estado de Pernambuco, com as cautelas de praxe."
    },
    {
      "tipo": "condicional",
      "identificador": "instrucao_retorno_autos_art_600_cpp",
      "descricao": "Usar este bloco como complemento quando a defesa optar por apresentar as razões da apelação diretamente no Tribunal (art. 600, § 4º, do CPP).",
      "conteudo_base": "Após a oferta das razões recursais na segunda instância e retorno dos autos a este juízo, abra-se vista ao MP para oferecimento de contrarrazões recursais e, após, voltem os autos ao e. TJPE."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "Cumpra-se.\n\n{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```
