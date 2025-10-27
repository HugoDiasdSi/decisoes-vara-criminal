

```json
{
  "filename": ".json",
  "tags": [
    "sentença",
    "extinção do processo",
    "litispendência",
    "sentença terminativa"
  ],
  "descricao": "Modelo de sentença que extingue o processo sem resolução do mérito devido à litispendência, por já existir outra ação penal sobre os mesmos fatos.",
  "titulo": "SENTENÇA DE EXTINÇÃO DO PROCESSO POR LITISPENDÊNCIA",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto. Blocos 'condicional' só devem ser incluídos se a condição descrita no 'identificador' ou 'descricao' for aplicável, e seu conteúdo deve ser adaptado.",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio",
      "conteudo_base": "Trata-se de ação penal contra {NOME_ACUSADO} pela prática do crime/contravenção previsto na exordial.\n\nO mesmo fato gerou o processo nº {NUMERO_PROCESSO_LITISPENDENTE}, que tramita também perante este juízo e, naqueles autos, já consta decisão de recebimento de denúncia devidamente proferida.\n\nÉ o breve relatório.\n\nDECIDO."
    },
    {
      "tipo": "fixo",
      "identificador": "fundamentacao_litispendencia",
      "conteudo": "Tal contexto processual enseja a extinção desta ação sem resolução do mérito, porquanto restou comprovada a litispendência.\n\nNo caso vertente, restaria patente a inutilidade do provimento oferecido pelo Estado-Juiz ao final deste processo."
    },
    {
      "tipo": "fixo",
      "identificador": "dispositivo_extincao",
      "conteudo": "Posto isso, com base nos art. 3º do CPP, 337, § 1º, e 485, V, ambos do CPC, **decreto a extinção do processo sem apreciação do mérito**."
    },
    {
      "tipo": "condicional",
      "identificador": "cancelamento_mandado_prisao",
      "descricao": "Usar este bloco se houver mandado de prisão expedido nestes autos que precise ser cancelado.",
      "conteudo_base": "Caso necessário, dê-se baixa no mandado de prisão porventura expedido em desfavor do acusado nestes autos, expedindo-se o competente alvará de soltura."
    },
    {
      "tipo": "fixo",
      "identificador": "determinacoes_finais",
      "conteudo": "Demais expedientes necessários. Após, ao arquivo.\n\nCumpra-se."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{LOCALIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\nJuiz de Direito"
    }
  ]
}
```