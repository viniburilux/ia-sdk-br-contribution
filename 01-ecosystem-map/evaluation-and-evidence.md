# Frente 3 - Avaliação, confiabilidade e evidências: candidatos verificados + encaixe do acervo

**Data da verificação:** 09/11/2026. **Escopo:** somente a frente 3 (avaliação, proveniência, lineage, assurance e formato de evidência técnica). Não é inventário de componentes (frente 2) nem de padrões documentais (frente 1).

**Método e limites:** licenças e características dos projetos candidatos foram verificadas em fonte primária (página oficial do repositório ou do órgão), citada item a item. Onde só houve fonte secundária, o item está marcado como tal ou foi retirado. Não executei código, testes ou benchmarks; "verificado" significa fonte primária lida hoje. Este recorte é uma pesquisa de um dia: as lacunas apontadas na seção 5 são hipóteses deste recorte, a validar com o grupo, não levantamento exaustivo.

## 1. O que esta frente precisa responder (âncoras no material do IA SDK BR)

Lido hoje em https://github.com/Everton-baptista/iasdk-br (README público) e https://iasdkbr.org/:

- Pergunta de pesquisa "Avaliação e evidência": métricas comparáveis entre organizações para transparência, explicabilidade, viés, robustez e prontidão regulatória; e "que formato de evidência técnica atende, ao mesmo tempo, à governança interna, à diligência de parceiros e à fiscalização, com integridade, retenção e rastreabilidade adequadas ao contexto brasileiro".
- Princípio "Evidência por padrão": cada evento relevante gera rastreabilidade, retenção e possibilidade de inspeção.
- Padrões de arquitetura ligados a esta frente: Gestão de risco de modelos (MRM), Observabilidade e logs imutáveis, Catálogo e linhagem, HITL com registro de revisão.
- O próprio README ancora o projeto na LGPD, no ECA Digital, no Marco Civil e no PL 2338/2023. A tramitação e os efeitos jurídicos dessas normas não foram objeto de verificação nesta frente.

## 2. Candidatos verificados em fonte primária

### A. Avaliação de modelos (benchmarks)

| Projeto | Mantenedor | Licença (fonte primária) | O que faz |
|---|---|---|---|
| lm-evaluation-harness | EleutherAI | MIT | Harness de benchmarks acadêmicos para modelos; https://github.com/EleutherAI/lm-evaluation-harness |
| lighteval | Hugging Face | MIT | Harness integrado ao ecossistema HF; https://github.com/huggingface/lighteval |
| HELM | Stanford CRFM | Apache-2.0 | Relatórios multi-métrica de modelos; https://github.com/stanford-crfm/helm |

Observação: esses harnesses comparam modelos em tarefas padronizadas; não avaliam a aplicação final de uma organização.

### B. Avaliação de aplicações e agentes

| Projeto | Mantenedor | Licença (fonte primária) | O que faz |
|---|---|---|---|
| promptfoo | promptfoo | MIT | Testes de prompts/aplicações via configuração, com assertions e red teaming; https://github.com/promptfoo/promptfoo |
| DeepEval | Confident AI | Apache-2.0 | Testes estilo pytest, métricas de RAG, agentes e conversas; https://github.com/confident-ai/deepeval |
| Ragas | Vibrant Labs | Apache-2.0 | Métricas de RAG e geração de conjuntos de teste; https://github.com/vibrantlabsai/ragas |
| Inspect | UK AI Security Institute | MIT (copyright UK AISI no LICENSE) | Avaliações de modelos e agentes com sandboxes; https://github.com/UKGovernmentBEIS/inspect_ai |

Observação de método (fonte secundária, marcada): guias comparativos recentes recomendam, para métricas com juiz-LLM, fixar modelo/versão/prompt do juiz junto ao score, usar rubricas estreitas e calibrar contra amostra humana (https://vdf.ai/blog/llm-evaluation-tools/, 06/10/2026). A recomendação é consistente com a literatura de LLM-as-judge, mas os detalhes de versões citados nesses guias não foram revalidados projeto a projeto.

### C. Observabilidade e trilhas de execução

| Projeto | Mantenedor | Licença (fonte primária) | O que faz |
|---|---|---|---|
| Langfuse | ClickHouse | MIT Expat para o conteúdo fora das pastas `ee/`; o conteúdo sob `ee/` tem licença própria (LICENSE do repositório) | Tracing, datasets, avaliação sobre traces; https://github.com/langfuse/langfuse |
| Arize Phoenix | Arize AI | Elastic License 2.0 (LICENSE do repositório) | Tracing e avaliação local-first; https://github.com/Arize-ai/phoenix |

Ressalvas verificadas na fonte primária: a ELv2 do Phoenix restringe oferecer o software como serviço hospedado a terceiros - relevante se o SDK gerar produto. No Langfuse, a separação por diretórios `ee/` exige conferir, recurso a recurso, o que é MIT e o que é Enterprise antes de depender de funções como retenção e audit log.
Padronização de telemetria GenAI: as convenções semânticas GenAI do OpenTelemetry estão em processo de padronização em https://github.com/open-telemetry/semantic-conventions (Apache-2.0). O grau de estabilidade atual não foi verificado nesta missão; qualquer adoção deve fixar versões.

### D. Viés e IA tradicional/preditiva

| Projeto | Mantenedor | Licença (fonte primária) | O que faz |
|---|---|---|---|
| Fairlearn | comunidade fairlearn | MIT | Métricas e mitigação de desigualdade em ML; https://github.com/fairlearn/fairlearn |
| AIF360 | Trusted-AI (IBM) | Apache-2.0 | Métricas de fairness e algoritmos de mitigação; https://github.com/Trusted-AI/AIF360/ |
| Aequitas | dssg | MIT | Auditoria de viés com relatório; https://github.com/dssg/aequitas |

### E. Metadados, proveniência e linhagem

| Projeto | Mantenedor | Licença/status (fonte primária) | O que faz |
|---|---|---|---|
| Croissant | MLCommons | Apache-2.0 | Formato JSON-LD (sobre schema.org) que descreve dataset, arquivos, estrutura e semântica ML em um arquivo; https://github.com/mlcommons/croissant |
| OpenLineage | LF AI & Data | Apache-2.0 | Padrão de eventos de lineage em runtime (runs/jobs/datasets), integrações Spark/Airflow/dbt/Flink; https://github.com/openLineage/OpenLineage/ |
| W3C PROV-O | W3C | Recomendação W3C | Vocabulário semântico de proveniência (entidade-atividade-agente); https://www.w3.org/TR/prov-o/ |

Leitura do recorte: PROV-O é vocabulário para publicar proveniência; OpenLineage emite eventos de pipeline em execução. São complementares.

### F. Integridade de artefatos e conteúdo sintético

- **CycloneDX ML-BOM** (OWASP/CycloneDX): representa modelos, datasets, configurações e proveniência de datasets como inventário; há guia autoritativo. https://www.cyclonedx.org/capabilities/mlbom/
- **C2PA Content Credentials**: padrão aberto de proveniência de mídia com manifests assinados, SDKs open source (CAI) e um programa de conformidade lançado em 2025 para validar implementações. https://contentauthenticity.org/blog/raising-the-bar-for-trust-introducing-the-c2pa-conformance-program
- Uso para o SDK: a camada de integridade/autenticidade da evidência (hashes, assinaturas, inventário) já tem padrões abertos; o trabalho do SDK seria adotar e perfilar, não inventar.

### G. Assurance e auditoria

- **AI Verify** (AI Verify Foundation, Singapura): método de autoavaliação em 11 princípios, cada um desdobrado em outcomes, processos testáveis e **evidência documental esperada**, com mapeamento publicado para NIST AI RMF, GenAI Profile, Hiroshima CoC e ISO/IEC 42001. Exemplo lido hoje: o processo 1.1.1 de Transparência exige "evidência documental de política interna de comunicação". https://aiverifyfoundation.sg/tools/ai-verify-testing-framework/
- **NIST AI RMF 1.0** e **GenAI Profile (NIST-AI-600-1)**: framework voluntário de gestão de risco; a página oficial informa que o AI RMF está em revisão. https://www.nist.gov/itl/ai-risk-management-framework
- **ISO/IEC 42001**: padrão internacional de sistema de gestão de IA (AIMS), certificável por organismos acreditados. https://www.iso.org/insights/iso-42001-explained
- **ForHumanity** (organização sem fins lucrativos): esquemas de auditoria independente com critérios auditáveis, incluindo esquemas para o EU AI Act. https://forhumanity.center/projects/eu-ai-act/

Ressalva de interpretação: esses frameworks são insumos de método. Nenhum deles, isoladamente, constitui conformidade com a legislação brasileira; qualquer mapeamento deles para obrigações brasileiras é trabalho de pesquisa do próprio SDK, com validação jurídica.

## 3. Ecossistema brasileiro de avaliação (estado verificado)

- Existem benchmarks brasileiros recentes, publicados sobretudo pela Maritaca AI no anúncio do Sabiá-4 (19/01/2026): Leis Brasileiras (múltipla escolha sobre atos normativos federais), OAB-Bench (arXiv 2504.21202), Magis-Bench, BRACEval (arXiv 2403.09887), Pix-Bench, Ticket-Bench (arXiv 2509.14477), Multi-IF Português. Fonte: https://www.maritaca.ai/blog/sabia-4/. São benchmarks de **capacidade** (conhecimento jurídico, seguimento de instruções, tarefas agênticas), não de conformidade regulatória.
- O **Open Portuguese LLM Leaderboard** (Hugging Face, eduagarcia) aparece hoje com o título "Archived": https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard
- O projeto **Tucano** (Universidade de Bonn, Apache-2.0) documenta uma limitação relevante: o desempenho em vários benchmarks em português usados pela comunidade teve pouca ou nenhuma correlação com a escala de treinamento dos modelos, o que questiona o que esses benchmarks medem. Fonte: https://nkluge-correa.github.io/Tucano/
- A **ANPD** publicou em 02/07/2026 o 1o Relatório Parcial do seu Sandbox Regulatório em IA; o comunicado informa que os próximos ciclos vão aprofundar, entre outros eixos, "transparência, governança de dados, anonimização e produção de evidências". Fonte: https://www.gov.br/anpd/pt-br/assuntos/noticias/publicados-primeiros-resultados-do-sandbox-regulatorio-em-inteligencia-artificial

## 4. Formato de evidência: organização proposta por este recorte

Uma forma de organizar as peças verificadas é em cinco camadas de evidência (proposta de leitura deste recorte, a discutir):

1. **Artefatos documentais versionados** (Model Card, Datasheet, AIA, RIPD, inventário): dizem o que o sistema é.
2. **Resultados de avaliação reproduzíveis** (harness + conjunto de teste fixo + rubrica + juiz registrado): dizem o que o sistema faz em teste.
3. **Trilhas de execução** (traces, logs de decisão, registros de revisão humana): dizem o que o sistema fez em produção.
4. **Metadados de linhagem** (OpenLineage, PROV-O, Croissant): dizem de onde vieram dados e artefatos.
5. **Integridade** (manifests com hash, ML-BOM, assinaturas, C2PA): provam que 1-4 não foram alterados.

O AI Verify é, neste recorte, a referência mais diretamente estruturada de método que amarra princípio - outcome - processo - evidência documental. Serve de ponto de partida conceitual para o "formato de evidência técnica" da pergunta de pesquisa do SDK; não é, por si, prova de conformidade com norma brasileira.

## 5. Lacunas - hipóteses deste recorte, a validar

1. **Avaliação executável de obrigações brasileiras.** Neste recorte não encontrei conjuntos de teste públicos que transformem deveres como explicação de decisões automatizadas (LGPD art. 20), aviso de interação com IA ou rotulagem de conteúdo sintético em casos de teste executáveis. Se confirmada a lacuna, seria espaço para o SDK construir - com o escopo validado juridicamente, porque um teste automatizado é evidência parcial, não prova de conformidade.
2. **Formato de evidência técnica para o contexto brasileiro.** A pergunta é do próprio README do SDK e segue aberta neste recorte; o eixo "produção de evidências" do Sandbox da ANPD sugere que o regulador também está construindo essa resposta, o que abre janela de diálogo/contribuição.
3. **Trilha de auditoria de baixo custo.** Há ressalvas de licença e de tier pago nas ferramentas de observabilidade verificadas (seção 2C); se a adoção exigir retenção e audit log abertos, pode haver espaço para um padrão aberto de log de decisão. Hipótese a confirmar com levantamento mais amplo.
4. **Avaliação comunitária em português.** Com o leaderboard PT arquivado e a crítica documentada pelo Tucano, pode haver espaço para avaliação comunitária viva em PT-BR - possivelmente começando pelo recorte de conformidade (lacuna 1), onde a métrica é mais bem definida do que "capacidade geral".
5. **Material de calibração de juízes em PT-BR.** A prática de LLM-as-judge pede amostras humanas de calibração; não encontrei, neste recorte, conjunto público brasileiro para calibrar juízes de métricas de RAG/conformidade.

## 6. Acervo do Vini: exame vivo (via API do GitHub, hoje)

### 6.1 TraceFoundry - https://github.com/viniburilux/TraceFoundry

Verificado hoje: repositório público, README completo, e existem com conteúdo substantivo os arquivos docs/TEST_MATRIX.md (execução registrada em 19/08/2026), docs/BENCHMARK_V0_RESULTS.md, docs/CLAIM_AUDIT_PLAYBOOK.md e tests/run_offline_tests.py. **A suíte não foi executada nesta missão**; o que se afirma é que os artefatos existem e o que registram.

O que oferece a esta frente: não é avaliador de modelos; é uma disciplina de evidência sobre conclusões - separa FATO, INFERÊNCIA, HIPÓTESE, LACUNA, BLOQUEIO e CONTRADIÇÃO; preserva evidência negativa; gera manifests versionados com proveniência; e o Claim Audit Starter Kit transforma uma afirmação em objeto revisável (afirmação, status epistêmico, fonte primária, escopo, próximo passo). A TEST_MATRIX registra explicitamente o que os testes não estabelecem.

Encaixes candidatos (a validar, não equivalências):
- O vocabulário de status epistêmico (observed/inferred/hypothesis/insufficient/blocked/rejected/contradicted) é um **candidato reutilizável** para o formato de evidência do SDK: cada resultado de avaliação poderia carregar um status desse tipo, separando "medido" de "inferido" de "não verificado".
- O Research Move é um mecanismo documentado de próxima ação proposta com justificativa e critério de parada. Não é uma implementação de HITL; a semelhança conceitual com "revisão humana registrada" é um ponto de partida de desenho, não uma funcionalidade pronta.
- Limite declarado pelo próprio material: hoje cobre investigação sobre fontes públicas (DANDI, Zenodo, OpenAlex, PatentsView); não mede modelos, viés ou tráfego.

### 6.2 descoberta-publica - https://github.com/viniburilux/descoberta-publica

Verificado hoje: README da edição v0.1.2 (recorte PNCP 2025-2026 parcial). Práticas presentes segundo o README: manifest de integridade SHA256 sobre os arquivos brutos, contagens por UF/ano verificadas após cada transformação, docs/LIMITACOES.md, mascaramento de identificadores pessoais em texto livre, licenças separadas (código MIT; conteúdo CC BY 4.0). Busca no repositório: nenhuma ocorrência de "datasheet"; não há Datasheet formal nem RIPD.

Encaixes candidatos:
- Referência prática brasileira de **integridade de dataset** (camada 5 da seção 4) e de documentação de limitações.
- Candidato natural a receber o primeiro Datasheet no padrão que o SDK definir - servindo de caso de validação do template antes de ele ser proposto a terceiros.
- Base real que pode servir de conjunto de teste para avaliar classificadores contra a curadoria documentada.

### 6.3 TTI_Brazil_2017_2024 - https://github.com/viniburilux/TTI_Brazil_2017_2024

Verificado hoje: README (versão 0.6, CC-BY 4.0), preprint em PDF/MD, notebook reproduzível para Google Earth Engine, raster nacional, agregados por estado/município/grid, amostra de pixels com seed documentada e conjunto de validação com sensor independente (Sentinel-2). O README marca a hipótese explicativa principal como "candidata, não estabelecida".

Encaixe candidato: exemplo de publicação de métrica derivada com **validação por fonte independente** e declaração explícita de limites - alinhado ao que o padrão de gestão de risco de modelos (MRM) do SDK pede de "validação independente de modelos". Os números específicos da validação estão no README e no preprint para quem quiser o detalhe.

### 6.4 ghostworks - https://github.com/viniburilux/ghostworks

Verificado hoje: README descreve protótipo de pesquisa de inteligência territorial (embeddings AlphaEarth - índice TTI - serializer que prepara saídas em JSON para agentes Gemma), com notebook de demonstração. Busca no repositório não encontrou suíte de testes.

Encaixe candidato: projeto de pesquisa territorial; para esta frente, hoje não oferece ativos de avaliação ou evidência prontos. Se um dia for usado como demonstrador no contexto do SDK, precisaria antes de instrumentação de evidência (trilhas, testes, limites documentados).

## 7. Sugestões para a síntese (a decidir pelo grupo)

| Tipo | Sugestão |
|---|---|
| Aproveitar (verificado em fonte primária) | lm-evaluation-harness / lighteval / HELM (benchmarks de modelo); promptfoo / DeepEval / Ragas / Inspect (testes de aplicação); Fairlearn / AIF360 / Aequitas (fairness); OpenLineage + PROV-O (linhagem); Croissant (metadados de dataset); CycloneDX ML-BOM (inventário); C2PA (conteúdo sintético); AI Verify / NIST AI RMF / ISO 42001 / ForHumanity (método de assurance) |
| Aproveitar com ressalva de licença | Langfuse (núcleo MIT; conferir o que está sob `ee/`); Phoenix (ELv2 restringe oferta como serviço) |
| Não revalidado nesta missão | TruLens, MLflow, Evidently, OpenCompass, OpenAI Evals e demais opções citadas em guias comparativos - licenças e estado atuais pendentes de verificação primária |
| Papel candidato do acervo | TraceFoundry: vocabulário epistêmico + claim audit + manifests como insumo do formato de evidência; descoberta-publica: caso para o primeiro Datasheet-padrão e referência de manifest de integridade; TTI: caso documentado de validação independente; ghostworks: fora de escopo de evidência hoje |

## 8. Ressalvas

- Versões exatas, contagens de estrelas e datas de release de ferramentas foram retiradas deste relatório; quando necessárias para decisão, verificar na fonte primária no dia da decisão.
- Guias comparativos (vdf.ai, trueiq.si, ajayk.sh) foram usados só como indicação de método; nenhuma licença ou capacidade ficou dependendo deles.
- O status legislativo do PL 2338/2023 não foi verificado nesta missão e não é necessário para esta frente neste momento; confirmar em fonte oficial antes de qualquer citação externa.
- O que mudaria este quadro: publicação de orientação oficial da ANPD sobre evidências; estabilização das convenções GenAI do OpenTelemetry; surgimento de conjuntos de teste brasileiros de conformidade; mudança de licença de algum projeto listado.

## 9. Fontes

Primárias (verificadas em 09/11/2026):

- Contexto SDK: https://iasdkbr.org/ ; https://github.com/Everton-baptista/iasdk-br
- Acervo: https://github.com/viniburilux/TraceFoundry (incl. docs/TEST_MATRIX.md, docs/BENCHMARK_V0_RESULTS.md, docs/CLAIM_AUDIT_PLAYBOOK.md, tests/run_offline_tests.py) ; https://github.com/viniburilux/descoberta-publica ; https://github.com/viniburilux/TTI_Brazil_2017_2024 ; https://github.com/viniburilux/ghostworks
- Avaliação: https://github.com/EleutherAI/lm-evaluation-harness ; https://github.com/huggingface/lighteval ; https://github.com/stanford-crfm/helm ; https://github.com/promptfoo/promptfoo ; https://github.com/confident-ai/deepeval ; https://github.com/vibrantlabsai/ragas ; https://github.com/UKGovernmentBEIS/inspect_ai
- Observabilidade: https://github.com/langfuse/langfuse (LICENSE) ; https://github.com/Arize-ai/phoenix (LICENSE) ; https://github.com/open-telemetry/semantic-conventions
- Fairness: https://github.com/fairlearn/fairlearn ; https://github.com/Trusted-AI/AIF360/ ; https://github.com/dssg/aequitas
- Metadados/linhagem: https://github.com/mlcommons/croissant ; https://github.com/openLineage/OpenLineage/ ; https://www.w3.org/TR/prov-o/
- Integridade: https://www.cyclonedx.org/capabilities/mlbom/ ; https://contentauthenticity.org/blog/raising-the-bar-for-trust-introducing-the-c2pa-conformance-program
- Assurance: https://aiverifyfoundation.sg/tools/ai-verify-testing-framework/ ; https://www.nist.gov/itl/ai-risk-management-framework ; https://www.iso.org/insights/iso-42001-explained ; https://forhumanity.center/projects/eu-ai-act/
- Brasil: https://www.maritaca.ai/blog/sabia-4/ ; https://nkluge-correa.github.io/Tucano/ ; https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard ; https://www.gov.br/anpd/pt-br/assuntos/noticias/publicados-primeiros-resultados-do-sandbox-regulatorio-em-inteligencia-artificial

Secundária (método apenas, marcada): https://vdf.ai/blog/llm-evaluation-tools/
