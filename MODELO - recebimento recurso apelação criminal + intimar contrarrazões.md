

```json
{
  "filename": "RECEBIMENTO_DE_APELACAO.json",
  "tags": [
    "recebimento de apelação",
    "recurso",
    "decisão",
    "carta de guia provisória",
    "réu preso",
    "processual"
  ],
  "descricao": "Modelo de decisão para recebimento de recurso de apelação, com instruções para a secretaria e previsão para expedição de carta de guia provisória em caso de réu preso.",
  "titulo": "RECEBIMENTO DE RECURSO DE APELAÇÃO",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "fixo",
      "conteudo": "Recebo o recurso de apelação tempestivamente apresentado.\n\nDê-se vista dos presentes autos à parte apelante para que apresente, no prazo legal, suas razões de apelação, caso ainda não o tenha feito.\n\nEm seguida, intime-se a parte apelada para que apresente, no prazo legal, caso queira, suas contrarrazões recursais.\n\nCertifique-se se todas as intimações foram providenciadas. Caso negativo, providenciem-se os expedientes faltantes."
    },
    {
      "tipo": "condicional",
      "identificador": "expedicao_carta_guia_provisoria",
      "descricao": "Usar este bloco se o réu estiver preso e a carta de guia provisória ainda não tiver sido expedida.",
      "conteudo_base": "Expeça-se a competente carta de guia provisória caso o réu {NOME_REU} se encontre preso e ainda não tenha sido providenciada nos autos."
    },
    {
      "tipo": "fixo",
      "conteudo": "Após, remetam-se os autos ao egrégio Tribunal de Justiça do Estado de Pernambuco, com as cautelas de praxe.\n\nIntime-se.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```
