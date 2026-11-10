# Frente 2 — Componentes técnicos: mapa do que já existe para o IA SDK BR (v2 corrigida)

Data: 09/11/2026 · Escopo: somente componentes técnicos (ferramentas e blocos reutilizáveis de software). Padrões, políticas e templates de documentos são a frente 1; o estudo profundo de avaliação/evidências é de outra frente — aqui entram os componentes de avaliação e observabilidade apenas com suas interfaces.

Método e limites: licenças verificadas hoje via GitHub API (campo spdx_id) e arquivos LICENSE dos repositórios. "Sinais observados" = data do último push e estrelas no GitHub em 09/11/2026. São sinais de manutenção e interesse da comunidade, não prova de adoção em produção nem de adequação a um caso específico: nenhum componente foi instalado ou testado neste recorte. Versões/release de cada componente não foram coletadas (pendente). URLs são as observadas nas fontes oficiais durante a verificação.

Princípio aplicado: o que usar direto, o que adaptar ao contexto brasileiro, o que integrar numa arquitetura comum — e onde há hipótese de lacuna. Não é catálogo: por capacidade ficaram 1-4 componentes com papel claro.

---

## 1. Gateway / acesso unificado a modelos

Papel na arquitetura: camada de abstração entre a aplicação e os provedores de LLM. Permite trocar de modelo (internacional ou nacional) sem reescrever código e é o ponto natural para aplicar políticas de custo, logging e fallback.

| Componente | Sinais observados | Licença atual | Encaixe |
|---|---|---|---|
| LiteLLM — https://github.com/BerriAI/litellm | push hoje; ~63k stars | MIT no núcleo; diretório `enterprise/` sob licença própria (LICENSE observado no repo) | Usar direto. Proxy unificado para muitos provedores, com spend tracking e rate limiting. Candidato a gateway de referência do SDK. |
| Portkey AI Gateway — https://github.com/Portkey-AI/gateway | último push mai/2026; ~13k stars | MIT | Alternativa; guardrails e cache embutidos. Ritmo de commits menor observado — checar roadmap antes de padronizar. |
| Helicone — https://github.com/Helicone/helicone | push out/2026; ~6k stars | Apache-2.0 | Gateway + observabilidade combinados; self-hosted. |

Veredito: usar direto (LiteLLM como referência). A contribuição BR aqui não é software novo, é configuração opinada: perfis de provedores usados no Brasil e exemplos de logging cuidadosos com dados pessoais (o que não dispensa análise LGPD caso a caso).

## 2. Observabilidade e rastreamento de execuções

Papel: registrar prompts, respostas, latência, custo e a trilha de uma execução — insumo para governança e para a frente de avaliação.

| Componente | Sinais observados | Licença atual | Encaixe |
|---|---|---|---|
| Langfuse — https://github.com/langfuse/langfuse | push hoje; ~37k stars | MIT no núcleo; diretórios `ee/` com licença enterprise. LICENSE observado com copyright "ClickHouse, Inc." (projeto adquirido; segue ativo) | Usar direto. Tracing LLM, datasets de teste, prompt management, scores. Self-host disponível. |
| Comet Opik — https://github.com/comet-ml/opik | push hoje; ~23k stars | Apache-2.0 no repositório. Não verifiquei se existe edição comercial separada. | Alternativa de licença integralmente permissiva no repo. Avaliação + tracing. |
| OpenTelemetry GenAI + OpenLLMetry | convenções em consolidação; OpenLLMetry (https://github.com/traceloop/openllmetry) push hoje, ~7,5k stars | Apache-2.0 | Integrar como interface comum: instrumentar uma vez, despejar em qualquer backend compatível. Convenções: https://opentelemetry.io/docs/specs/semconv/gen-ai/ (página oficial, acessada hoje). |
| Arize Phoenix — https://github.com/Arize-ai/phoenix | push hoje; ~12k stars | Elastic License 2.0 (LICENSE observado) — source-available, não OSI: proíbe oferecer o software como serviço gerenciado a terceiros | Usar com a restrição clara; se o IA SDK BR um dia hospedar serviços para terceiros, ELv2 limita. |

Veredito: usar + integrar — adotar as convenções OpenTelemetry GenAI como contrato e um backend de referência (Langfuse ou Opik). Self-host dá controle sobre onde os dados de telemetria ficam, mas não equivale por si só a conformidade LGPD.

## 3. Avaliação e testes de sistemas de IA

Papel: testar prompts e pipelines em CI, medir qualidade de RAG, detectar regressão e drift. (Interfaces listadas; profundidade é de outra frente.)

| Componente | Sinais observados | Licença | Encaixe |
|---|---|---|---|
| Promptfoo — https://github.com/promptfoo/promptfoo | push hoje; ~27k stars | MIT | Testes de prompt/agente em CI e red-teaming. Formato YAML simples, adequado a templates reutilizáveis. |
| DeepEval — https://github.com/confident-ai/deepeval | push nov/2026; ~19k stars | Apache-2.0 | Métricas estilo pytest (faithfulness, relevância, toxicidade). |
| Ragas — https://github.com/vibrantlabsai/ragas | **atenção:** repo redirecionado da org explodinggradients; último push fev/2026 (~9 meses); ~16k stars | Apache-2.0 | Métricas de RAG. Confirmar manutenção atual antes de fixar como padrão. |
| Evidently — https://github.com/evidentlyai/evidently | push set/2026; ~8k stars | Apache-2.0 | Drift de dados e monitoramento de qualidade em produção. |
| Giskard — https://github.com/Giskard-AI/giskard-oss | push hoje; ~6k stars; redirecionado de giskard-ai/giskard | Apache-2.0 | Testes de risco/robustez e scan de modelos. |

Veredito: usar Promptfoo + DeepEval como base; adaptar com baterias de testes em PT-BR.

## 4. Guardrails e segurança em tempo de execução

Papel: validar entradas/saídas contra regras (PII, conteúdo proibido, escopo do assistente) antes de chegar ao usuário.

| Componente | Sinais observados | Licença | Encaixe |
|---|---|---|---|
| NeMo Guardrails — https://github.com/NVIDIA-NeMo/Guardrails | push hoje; ~7,5k stars | Apache-2.0 (LICENSE.md observado, SPDX Apache-2.0) | Trilhos programáveis (tópicos permitidos, fact-checking, PII). Candidato a motor sobre o qual empacotar regras brasileiras pré-configuradas. |
| Guardrails AI — https://github.com/guardrails-ai/guardrails | push nov/2026; ~7,6k stars | Apache-2.0 | Validação estrutural e semântica de saídas. |
| Llama Guard — https://github.com/meta-llama/PurpleLlama | push hoje; ~4,5k stars | Meta Llama Community License — não OSI, com restrições de uso (não li o texto integral nesta verificação) | Classificador de segurança, com ressalva de licença. |

Veredito: usar NeMo Guardrails como motor. Hipótese de lacuna (não é levantamento exaustivo): no recorte pesquisado não encontrei pacotes prontos de regras brasileiras (LGPD, ECA Digital, normas setoriais) para esses motores. Se confirmada, é um bom candidato de "criar novo" para o IA SDK BR — regras e testes sobre motor existente, não motor novo.

## 5. Orquestração, RAG e agentes

| Componente | Sinais observados | Licença | Encaixe |
|---|---|---|---|
| LangChain — https://github.com/langchain-ai/langchain / LangGraph — https://github.com/langchain-ai/langgraph | push hoje; ~149k/~45k stars | MIT | Orquestração geral e agentes com estado. |
| LlamaIndex — https://github.com/run-llama/llama_index | push nov/2026; ~53k stars | MIT | Especializado em RAG/ingestão de dados. |
| Haystack — https://github.com/deepset-ai/haystack | push hoje; ~27k stars | Apache-2.0 | Pipelines modulares explícitos — útil para arquiteturas de referência documentadas. |
| MCP (Model Context Protocol) — https://github.com/modelcontextprotocol/modelcontextprotocol | push hoje; ~9,7k stars | Em transição: novos códigos/especificação sob Apache-2.0; contribuições antigas permanecem MIT até relicenciamento (fonte: LICENSE observado em https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/LICENSE) | Protocolo aberto para expor ferramentas e dados a agentes. Interoperabilidade real depende de cada cliente/servidor implementar o protocolo — não é automática entre fornecedores. Vale como contrato de ferramentas do SDK. |

Veredito: usar LlamaIndex ou LangGraph como base de exemplos; integrar MCP como contrato de ferramentas. Não reconstruir framework de orquestração.

## 6. Dados e busca vetorial

| Componente | Sinais observados | Licença | Encaixe |
|---|---|---|---|
| pgvector — https://github.com/pgvector/pgvector | push hoje; ~24k stars | PostgreSQL License (permissiva; LICENSE observado) | Busca vetorial dentro do Postgres que a organização já opera — tende a reduzir barreira de entrada. |
| Qdrant — https://github.com/qdrant/qdrant | push hoje; ~35k stars | Apache-2.0 | Banco vetorial dedicado, self-host simples. |
| Milvus — https://github.com/milvus-io/milvus | push hoje; ~47k stars | Apache-2.0 | Voltado a escala grande. |
| Weaviate — https://github.com/weaviate/weaviate | push hoje; ~17k stars | Mista: BSD-3-Clause e "Weaviate License" conforme a parte do código (LICENSE observado) | Verificar qual parte importa antes de recomendar; preferir os três acima no padrão. |

## 7. Servir e operar modelos (self-host)

| Componente | Sinais observados | Licença | Encaixe |
|---|---|---|---|
| vLLM — https://github.com/vllm-project/vllm | página do repo observada hoje; ~97k stars | Apache-2.0 | Serving de alta performance. Permite rodar modelos próprios/nacionais em infraestrutura da organização — ajuda no controle de onde os dados trafegam, o que não dispensa análise LGPD. |
| Ollama — https://github.com/ollama/ollama | push hoje; ~186k stars | MIT | Prototipagem local; porta de entrada útil para capacitação. |
| TGI — https://github.com/huggingface/text-generation-inference | último push mar/2026; ~11k stars | Apache-2.0 (verificado hoje via API) | Alternativa; ritmo de manutenção observado é menor. |
| BentoML — https://github.com/bentoml/BentoML | push nov/2026; ~9k stars | Apache-2.0 | Empacotamento de serviços de modelo em produção. |

## 8. MLOps, registro e dados

| Componente | Sinais observados | Licença | Encaixe |
|---|---|---|---|
| MLflow — https://github.com/mlflow/mlflow | push hoje; ~29k stars | Apache-2.0 | Registro de experimentos e modelos; cobre boa parte do "inventário de modelos" que governança precisa. |
| ZenML — https://github.com/zenml-io/zenml | push hoje; ~5,6k stars | Apache-2.0 | Pipelines MLOps portáteis. |
| Label Studio — https://github.com/HumanSignal/label-studio | push hoje; ~29k stars | Apache-2.0 | Rotulagem de dados. |
| Argilla — https://github.com/argilla-io/argilla | push nov/2026; ~5k stars | Apache-2.0 | Feedback humano e curadoria de dados. |

## 9. Versionamento de dados (capacidade pedida no recorte)

| Componente | Sinais observados | Licença | Encaixe |
|---|---|---|---|
| DVC — https://github.com/treeverse/dvc | push hoje; ~16k stars; **o repositório migrou da org iterative para treeverse** (redirecionamento observado) | Apache-2.0 | Versionamento de datasets e artefatos sobre Git/storage existente. Usar direto. |
| lakeFS — https://github.com/treeverse/lakeFS | push hoje; ~5,6k stars | **Business Source License 1.1** (LICENSE observado) — source-available, restringe oferecer como serviço concorrente | Versionamento estilo "git para dados" em object storage; usar com ressalva de licença. |

## 10. Identidade, permissões, segredos e deployment

Capacidades solicitadas no recorte que não são específicas de IA: autenticação/autorização (SSO, RBAC), gestão de segredos e deployment costumam vir da infraestrutura compartilhada da organização (ex.: Keycloak ou Ory para identidade, HashiCorp Vault ou SOPS para segredos, Kubernetes para deployment). Não verifiquei licenças nem estado atual desses projetos neste recorte — são ponteiros, não recomendação verificada. Sugestão: tratá-los como pré-requisito documentado da arquitetura de referência do SDK ("o SDK assume SSO e gestão de segredos existentes") em vez de ampliar o catálogo, ou abrir recorte próprio se a frente quiser cobri-los.

## 11. Camada Brasil: modelos, benchmarks e recursos em português

- Tucano / TucanoBR — modelos pré-treinados nativamente em português. Repo https://github.com/nkluge-correa/tucano (Apache-2.0; **arquivado** — o README aponta a continuação no projeto Polygl0t, não verificado). Pesos em https://huggingface.co/TucanoBR/Tucano-2b4 (observado). Corpus GigaVerbo (200B tokens PT) liberado junto, segundo o README.
- Sabiá (Maritaca AI) — modelos de fornecedor brasileiro via API proprietária. Ser fornecedor nacional não comprova processamento em território nacional: isso depende de documentação contratual que não verifiquei. Opção de provedor atrás do gateway LiteLLM.
- Open Portuguese LLM Leaderboard — https://huggingface.co/spaces/eduagarcia/open_pt_llm_leaderboard (Apache-2.0, README observado): ranking de modelos em PT.
- Poeta v2 — https://github.com/PoETaV2/PoETaV2 (observado): benchmark PT com 40+ tarefas e 12k+ exemplos; leaderboard inclui modelos nacionais (Curió, Sabiá).
- Encoders/embeddings para PT-BR: BERTimbau (org neuralmind no Hugging Face — URL exata não verificada neste recorte) e embeddings multilíngues (BGE-M3, multilingual-e5 — não verificados). Pendente de verificação antes de incluir como recomendação formal.

Veredito: adaptar — empacotar esses recursos como presets (avaliação PT-BR pronta no Promptfoo/DeepEval, exemplos RAG com embeddings para PT-BR, Sabiá como provedor no gateway), após verificar os itens pendentes acima.

## 12. Interfaces com documentação e governança (sem duplicar a frente 1)

- Croissant — https://github.com/mlcommons/croissant (Apache-2.0, MLCommons; push hoje): formato machine-readable de metadados de datasets; ponte técnica entre a documentação de dataset (frente 1) e o pipeline real.
- Model cards Hugging Face — formato amplamente usado para documentação de modelos (observação geral do ecossistema; não verifiquei especificação formal neste recorte).
- OpenTelemetry GenAI e MCP (acima) como os dois contratos que mantêm a arquitetura aberta.

## Hipóteses de lacuna onde criar algo novo faria sentido

São hipóteses apoiadas no recorte pesquisado, não levantamento exaustivo nem certificação:

1. Guardrails BR prontos: regras LGPD/ECA Digital/setoriais empacotadas para motores como NeMo Guardrails, com testes. Não encontrei pacote equivalente no recorte.
2. Presets de avaliação PT-BR em CI: baterias Promptfoo/DeepEval com datasets nacionais (Poeta, entre outros) prontos para pipeline.
3. Conector conformidade → evidência: componente que organiza execuções registradas (Langfuse/OpenTelemetry) em trilhas de evidência para processos de conformidade. Aqui entra o TraceFoundry (https://github.com/viniburilux/TraceFoundry): a trilha claim → evidência → proveniência conecta telemetria técnica a documentação de governança. Apoio à produção de evidências, não certificação legal.
4. Rascunho assistido de documentação BR: gerar rascunho de model card/documentação a partir do estado observado do sistema (registro + traces), com revisão humana obrigatória antes de valer como documento oficial — o trace é insumo, não verdade automática. Fecha o ciclo com a frente 1.

## Ressalvas

- Licenças verificadas em 09/11/2026 nas fontes citadas; relicenciamento acontece (MCP está em transição agora; TGI já mudou no passado). Revalidar antes de cada release do SDK.
- Phoenix (ELv2), lakeFS (BSL 1.1), Llama Guard (Meta Community) e Weaviate (mista) têm restrições relevantes para um SDK que venha a servir terceiros.
- Ragas mudou de organização e está sem push desde fev/2026: confirmar manutenção antes de adotar.
- Langfuse foi adquirida pela ClickHouse (copyright observado no LICENSE); o projeto segue ativo, mas vale monitorar a governança.
- Versões/releases por componente não foram coletadas neste recorte (pendente para a síntese, se necessário).
- Nenhum componente foi instalado ou executado; encaixes arquiteturais são avaliação de design, não teste de adoção.
