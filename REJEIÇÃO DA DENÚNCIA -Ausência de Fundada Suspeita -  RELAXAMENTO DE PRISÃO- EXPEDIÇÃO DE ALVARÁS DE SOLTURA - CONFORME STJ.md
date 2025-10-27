{
  "titulo": "DECISÃO (REJEIÇÃO DA DENÚNCIA - BUSCA PESSOAL ILÍCITA)",
  "instrucao_llm": "Gerar decisão judicial com base nos blocos a seguir. Blocos 'fixo' devem ser reproduzidos literalmente. Blocos 'adaptavel' devem ser usados como base, e o conteúdo adaptado ao caso concreto (nomes, IDs, fatos da denúncia, depoimentos específicos).",
  "estrutura_decisao": [
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_imputacao",
      "conteudo_base": "DECISÃO\n\nO Ministério Público, com base em autos de inquérito policial, ofereceu denúncia contra **{NOME_REU(S}**, qualificados nos autos, pela prática do crime descrito no art. 33, cabeça, da Lei n. 11.343/2006."
    },
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_fatos_denuncia",
      "conteudo_base": "Narra-se na denúncia:\n\n> {TRANSCRIÇÃO DOS FATOS DA DENÚNCIA}."
    },
    {
      "tipo": "adaptavel",
      "identificador": "relatorio_status_prisional",
      "conteudo_base": "Os acusados tiveram o auto de prisão em flagrante homologado, convertida a prisão em flagrante em prisão preventiva dos acusados {NOME_ACUSADOS_PRESOS} e concedida a liberdade provisória com imposição de medidas cautelares diversas da prisão a {NOME_ACUSADO_SOLTO}. (Id. {ID_DECISAO_CUSTODIA})\n\nEsse, em apertada síntese, é o relatório.\n\n**DECIDO**."
    },
    {
      "tipo": "fixo",
      "conteudo": "**Tenho que é caso de rejeição da denúncia.**\n\nExplico."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_fatos_abordagem",
      "conteudo_base": "Ao compulsar os autos, neste instante, constato que o APFD se iniciou por ação ordinária de Policiais Militares, posto que abordaram os acusados por os terem encontrado em atitudes suspeitas, segundo narra a exordial acusatória, após receberem denúncias anônimas."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_depoimentos_e_reus",
      "conteudo_base": "Os policiais, ouvidas em sede inquisitorial, afirmaram que estavam em rondas ordinárias quando receberam informações acerca da prática de tráfico de drogas e, ao chegar ao local indicado, teriam encontrado os acusados exercendo traficância.\n\nOs réus se valeram do direito ao silêncio na delegacia."
    },
    {
      "tipo": "fixo",
      "conteudo": "Antes de mais nada, convém destacar que os **depoimentos dos agentes públicos, apesar de plenamente válidos, não podem ser tomados por verdades incontestes**. Também é necessário ponderar a palavra dos agentes públicos envolvidos no flagrante, analisando a coerência e a verossimilhança de suas narrativas.\n\nCito precedente da Terceira Seção do STJ:\n\n> (...) 15.**Trata-se, portanto, de abandonar a cômoda e antiga prática de atribuir caráter quase que inquestionável a depoimentos prestados por testemunhas policiais, como se fossem absolutamente imunes à possibilidade de desviar-se da verdade; do contrário, deve-se submetê-los a cuidadosa análise de coerência - interna e externa -, verossimilhança e consonância com as demais provas dos autos**. (HC n. 877.943/MS, relator Ministro Rogerio Schietti Cruz, Terceira Seção, julgado em 18/4/2024, DJe de 15/5/2024)"
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_analise_fatos_suspeita",
      "conteudo_base": "Feitas essas considerações, verifico que as falas dos policiais não indicaram de maneira clara e precisa qual a \"fundada suspeita\" que teria motivado a busca pessoal nos acusados ou que atitudes ou ações praticadas denotariam a prática da referida traficância.\n\nA fundada suspeita, consoante se extrai da exordial acusatória, se resumiu a atitudes suspeitas as quais, segundo os policiais, seriam a prática de traficância -- sem maiores especificações."
    },
    {
      "tipo": "fixo",
      "identificador": "fundamentacao_tese_fundada_suspeita_stj",
      "conteudo": "Sobre o tema, a exigência de fundada suspeita está expressamente prevista no art. 240, §2º, do CPP:\n\n> \"Art. 240. A busca será domiciliar ou pessoal.\n> \n> (...)\n> \n> § 2o Proceder-se-á à busca pessoal quando houver fundada suspeita de que alguém oculte consigo arma proibida ou objetos mencionados nas letras b a f e letra h do parágrafo anterior.\"\n\nDe acordo com recente julgado do STJ, **a busca pessoal deve estar respaldada em fundadas suspeitas (justa causa**), baseada em um juízo de probabilidade, **descrita com a maior precisão possível, aferida de modo objetivo e devidamente justificada pelos indícios e circunstâncias do caso concreto, evidenciando-se a urgência de executar a diligência**, o que não ocorreu no presente caso.\n\nSenão, veja-se:\n\n> RECURSO EM HABEAS CORPUS. TRÁFICO DE DROGAS. BUSCA PESSOAL. **AUSÊNCIA DE FUNDADA SUSPEITA. ALEGAÇÃO VAGA DE \"ATITUDE SUSPEITA\". INSUFICIÊNCIA. ILICITUDE DA PROVA OBTIDA**. TRANCAMENTO DO PROCESSO. RECURSO PROVIDO.\n> \n> 1. Exige-se, em termos de standard probatório para busca pessoal ou veicular sem mandado judicial, a existência de fundada suspeita (justa causa) - baseada em um juízo de probabilidade, descrita com a maior precisão possível, aferida de modo objetivo e devidamente justificada pelos indícios e circunstâncias do caso concreto - de que o indivíduo esteja na posse de drogas, armas ou de outros objetos ou papéis que constituam corpo de delito, evidenciando-se a urgência de se executar a diligência.\n> \n> 2. Entretanto, a normativa constante do art. 244 do CPP não se limita a exigir que a suspeita seja fundada. É preciso, também, que esteja relacionada à \"posse de arma proibida ou de objetos ou papéis que constituam corpo de delito\". (...)\n> \n> 3. **Não satisfazem a exigência legal, por si sós, meras informações de fonte não identificada (e.g. denúncias anônimas) ou intuições e impressões subjetivas, intangíveis e não demonstráveis de maneira clara e concreta, apoiadas, por exemplo, exclusivamente, no tirocínio policial.** (...)\n> \n> 4. O **fato de haverem sido encontrados objetos ilícitos - independentemente da quantidade - após a revista não convalida a ilegalidade prévia**, pois é necessário que o elemento \"fundada suspeita de posse de corpo de delito\" seja aferido com base no que se tinha antes da diligência. (...)\n> \n> 5. **A violação dessas regras e condições legais para busca pessoal resulta na ilicitude das provas obtidas em decorrência da medida**, bem como das demais provas que dela decorrerem em relação de causalidade (...)\n> \n> 6. Há três razões principais para que se exijam elementos sólidos, objetivos e concretos para a realização de busca pessoal (...):\n> \n> a) evitar o uso excessivo desse expediente e, por consequência, a restrição desnecessária e abusiva dos direitos fundamentais à intimidade, à privacidade e à liberdade (art. 5º, caput, e X, da Constituição Federal) (...);\n> \n> b) **garantir a sindicabilidade da abordagem, isto é, permitir que tanto possa ser contrastada e questionada pelas partes, quanto ter sua validade controlada a posteriori por um terceiro imparcial** (Poder Judiciário) (...);\n> \n> c) evitar a repetição - ainda que nem sempre consciente - de práticas que reproduzem preconceitos estruturais arraigados na sociedade, como é o caso do perfilamento racial, reflexo direto do racismo estrutural.\n> \n> (...) 11. Mesmo que se considere que todos os flagrantes decorrem de busca pessoal (...), as estatísticas oficiais das Secretarias de Segurança Pública apontam que o índice de eficiência no encontro de objetos ilícitos em abordagens policiais é de apenas 1%; isto é, de cada 100 pessoas revistadas pelas polícias brasileiras, apenas uma é autuada por alguma ilegalidade. (...)\n> \n> (...) 15. Na espécie, a guarnição policial \"deparou com um indivíduo desconhecido em atitude suspeita\" e, ao abordá-lo e revistar sua mochila, encontrou porções de maconha e cocaína em seu interior, do que resultou a prisão em flagrante do recorrente. Não foi apresentada nenhuma justificativa concreta para a revista no recorrente além da vaga menção a uma suposta \"atitude suspeita\", algo insuficiente para tal medida invasiva, conforme a jurisprudência deste Superior Tribunal, do Supremo Tribunal Federal e da Corte Interamericana de Direitos Humanos.\n> \n> 16. Recurso provido para determinar o trancamento do processo.\n> \n> (RHC n. 158.580/BA, relator Ministro Rogerio Schietti Cruz, Sexta Turma, julgado em 19/4/2022, DJe de 25/4/2022.)"
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_conclusao_caso_concreto",
      "conteudo_base": "Assim, a narrativa contida na denúncia é vaga e carente de subsídios suficientes acerca dos motivos que ensejaram a busca pessoal sem qualquer respaldo judicial, **pois nenhum dado concreto, objetivo e aferível, motivou a abordagem policial**.\n\nMesmo considerando os depoimentos contidos nos autos, não é possível delimitar critérios objetivos para a prática das condutas pelos acusados."
    },
    {
      "tipo": "fixo",
      "conteudo": "Ademais, **eventuais denúncias devem ser investigadas e averiguadas** pelo efetivo policial antes de empreender a abordagem pessoal ou o ingresso ao domicílio. Sequer se pode considerar a fuga ou nervosismo do réu, como elemento autorizador de busca pessoal -- o que, por oportuno ressaltar, não ficou demonstrado no caso concreto. Nesse sentido, STJ. AgRg no HC n. 834.977/MG, relator Ministro Jesuíno Rissato (Desembargador Convocado do TJDFT), Sexta Turma, julgado em 10/6/2024, DJe de 20/6/2024.\n\n**As buscas pessoais não podem decorrer de um estado de ânimo do agente estatal no exercício do poder de polícia. Não se pode adivinhar essas coisas.**\n\nNeste ponto, reside o limite da atuação estatal, cujos agentes e autoridades estão sujeitos à observância dos direitos e prerrogativas que assistem aos cidadãos em geral, como fator condicionante da legitimidade de suas condutas.\n\nAo prometer o direito à segurança, o art. 5º da Constituição da República impõe que o Estado torna-se devedor desta prestação positiva, pelo que não se deve olvidar esforços em prestá-la, **porém na forma da lei e seguindo escrupulosamente os parâmetros constitucionais**.\n\nHá de se equacionar, pois, as garantias individuais e o direito à segurança, este último, como justificador da atuação policial, nos termos do permitido pela Constituição da República, a fim de impedir a consumação de crimes nas hipóteses em flagrante delito.\n\nIsso significa que, ao mesmo tempo em que ao Estado compete, como devedor que é, garantir a todos o direito à segurança, o resultado processual penal somente é lícito se respeitados os ditames constitucionais.\n\n**A atitude suspeita deveria estar presente desde a narrativa da denúncia**, não apenas por exigência do **art. 41 do CPP**, mas principalmente porque é ela que autoriza busca pessoal sem apresentação de mandado judicial, conforme exige o art. 240, §2º, do mesmo CPP."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fundamentacao_conclusao_ilegalidade",
      "conteudo_base": "Dessa forma, a abordagem pessoal dos acusados foi ilegal, uma vez que a fundada suspeita **não se encontra comprovada por elementos precisos e objetivos -- demonstráveis, que possam ser submetidos ao controle judicial.**"
    },
    {
      "tipo": "fixo",
      "conteudo": "Na esteira da jurisprudência ora colacionada, muito embora tenham sido apreendidas as drogas, isso não convalida a ilegalidade.\n\nA consequência lógica é que se invalidou acervo probatório, porque fruto de ato originalmente eivado de nulidade, conforme se extrai da norma disposta no texto do art. 157, cabeça, do Código de Processo Penal:\n\n> Art. 157. São inadmissíveis, devendo ser desentranhadas do processo, as provas ilícitas, assim entendidas as obtidas em violação a normas constitucionais ou legais.\n\nA materialidade dos crimes, nesse passo, decorreu de abordagem ilegal, **sem fundada suspeita**, sem ordem judicial ou autorização, por isso inválidas (art. 5º, LVI, CF), carecendo a exordial de **justa causa** para o exercício da ação penal."
    },
    {
      "tipo": "adaptavel",
      "identificador": "dispositivo_rejeicao",
      "conteudo_base": "Diante do exposto, e considerando ainda o quanto previsto, **rejeito a denúncia** em todos os seus termos em relação aos denunciados **{LISTA_NOMES_REUS}**, o que faço com base no art. 395, III, do CPP, pela ausência de justa causa (fato atípico), na esteira do entendimento do STJ."
    },
    {
      "tipo": "fixo",
      "identificador": "determinacoes_finais",
      "conteudo": "P.R.I. Demais expedientes necessários.\n\nSem custas.\n\nEXPEÇAM-SE OS ALVARÁS DE SOLTURA, CASO OS ACUSADOS SE ENCONTREM PRESOS POR ESTE PROCESSO, BEM COMO DETERMINO O RECOLHIMENTO DO MANDADO DE PRISÃO PORVENTURA EXPEDIDO NOS AUTOS.\n\nIntime-se o representante do MPPE e os denunciados, pois interessados.\n\nHavendo recurso, me voltem os autos conclusos.\n\nCertificado o trânsito em julgado, procedam-se às anotações e comunicações de estilo, inclusive ao IITB.\n\nDestrua-se a droga apreendida.\n\n**Restituam-se os bens pessoais e valores porventura apreendidos.**\n\nApós tudo cumprido e certificado, arquivem-se os presentes autos."
    },
    {
      "tipo": "adaptavel",
      "identificador": "fecho_assinatura",
      "conteudo_base": "{CIDADE}, data da assinatura eletrônica.\n\n**Lucas Tavares Coutinho**\n\nJuiz de Direito"
    }
  ]
}
