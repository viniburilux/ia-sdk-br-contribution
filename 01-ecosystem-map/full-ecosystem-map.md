# IA SDK BR: usar, adaptar, criar
Pesquisa de 9 nov 2026

Este mapa reúne o que já existe no mundo para uma organização construir, adotar, operar, avaliar e governar sistemas de IA, e consolida o que usar direto, o que adaptar ao Brasil e onde faria sentido criar algo novo.

## A resposta curta
A base para construir, operar, avaliar e governar IA já existe e é aberta. O que não apareceu no recorte foi a versão brasileira dela.
- Documentação de modelos e datasets, avaliação, guardrails, observabilidade e frameworks de governança gratuitos já existem, com licenças permissivas verificadas em fonte primária.
- Não apareceram neste recorte: política de IA organizacional em português ancorada na LGPD com licença aberta, guardrails com regras brasileiras empacotadas, avaliação executável de requisitos da legislação brasileira e formação em implementação responsável de IA.
- Os modelos de adoção com evidência colocam o artefato aberto no centro e o valor nos anéis ao redor: autodeclaração, avaliação independente, certificação e treinamento.
- Cada lacuna apontada é uma hipótese deste recorte de pesquisa de um dia, a validar com o grupo. Nenhuma é prova de inexistência.

## O percurso: de entender a melhorar
- Entender: mapear o campo com o observatório da OECD.AI, medir prontidão com o toolkit do CGI.br e sondar modelos em benchmarks em português como o Poeta v2.
- Planejar: risco e governança com NIST AI RMF, GuIA e AI Verify; avaliação de impacto com RIPD (dados pessoais) e AIA do Canadá (candidato, licença a confirmar); política de uso na base da Contrast.
- Construir: gateway LiteLLM, orquestração LlamaIndex/LangGraph, busca vetorial pgvector/Qdrant, guardrails NeMo, MCP como contrato de ferramentas e vLLM/Ollama para servir modelos, incluindo os em português atrás do gateway.
- Operar: trilhas de execução com Langfuse e OpenTelemetry GenAI, registro e inventário de modelos com MLflow, drift com Evidently e versionamento de dados com DVC.
- Avaliar: aplicações com Promptfoo, DeepEval, Ragas e Inspect; modelos com lm-evaluation-harness, lighteval e HELM; viés com Fairlearn, AIF360 e Aequitas.
- Governar: documentação com model cards e datasheets, linhagem com Croissant/OpenLineage, inventário com CycloneDX ML-BOM, integridade com C2PA e transparência pública com registro de algoritmos (Algoritmeregister, candidato).
- Melhorar: evidência em cinco camadas, claim audit (TraceFoundry), presets de avaliação PT-BR e formação com portfólio, em revisão contínua à medida que frameworks e regulação evoluem.

## O que já pode ser utilizado
Bases abertas verificadas (documentação e governança):
- Model cards Hugging Face (Apache-2.0) e Model Card Toolkit do Google (Apache-2.0, repo arquivado): formatos prontos de documentação de modelos. Data Cards Playbook (Apache-2.0, arquivado) cobre datasets.
- Política de IA generativa da Contrast Security (CC BY-SA 4.0): política organizacional pronta, adaptável com atribuição e compartilhamento pela mesma licença.
- NIST AI RMF 1.0 + Perfil GenAI: framework gratuito e voluntário, em revisão segundo a página oficial. AI Verify (Singapura): método de autoavaliação e toolkit open source, com mapeamento publicado para NIST e ISO/IEC 42001.
- Peças brasileiras oficiais e gratuitas: RIPD e Programa de Governança em Privacidade do Governo Digital, GuIA para o setor público e o guia do TCU de uso de genAI.

Componentes técnicos (software):
- Gateway de modelos: LiteLLM (MIT), candidato a gateway de referência. Observabilidade: Langfuse (MIT no núcleo; recursos enterprise separados). Testes: Promptfoo (MIT) e DeepEval (Apache-2.0). Guardrails: NeMo Guardrails (Apache-2.0) como motor.
- Linhagem e metadados: OpenLineage e Croissant (Apache-2.0). Viés: Fairlearn, AIF360, Aequitas. Contratos abertos que mantêm a arquitetura interoperável: OpenTelemetry GenAI e MCP. Servir modelos próprios: vLLM e Ollama.
- Avaliação de modelos: lm-evaluation-harness, lighteval e HELM comparam modelos em tarefas padronizadas, não a aplicação final. Integridade de artefatos: CycloneDX ML-BOM e C2PA já têm padrões abertos; o trabalho é adotar e perfilar, não inventar.

## O que adaptar ao contexto brasileiro
- Model card e dataset card em português sobre a base Hugging Face / Model Card Toolkit (Apache-2.0): adaptação de formato existente, não criação de padrão novo. Croissant já cobre a camada machine-readable de datasets.
- Trilha mínima de governança prática: NIST AI RMF + GuIA + AI Verify traduzidos em um fluxo para organizações brasileiras médias. A lacuna aparente não é de framework, é de tradução em prática.
- Presets técnicos: baterias de avaliação em PT-BR prontas para Promptfoo/DeepEval (datasets como o Poeta v2), Sabiá como provedor atrás do gateway e embeddings para PT-BR. Itens com verificação pendente entram como candidatos, não como padrão.
- Estruturas de formação replicáveis: seleção por imersão prática (Piscina da 42), mentoria executada por profissionais das empresas parceiras ({reprograma}), contribuição estipendiada em open source (Outreachy, GSoC), diretório público de projetos (AI4ALL), programa com âncora corporativa (Oracle ONE, Santander Coders) e módulo em residências públicas (Softex). São estruturas, não material: traduzir ou copiar conteúdo de terceiros exige checar licença caso a caso.

## Onde criar algo novo
Hipóteses de lacuna deste recorte, a validar com o grupo antes de comprometer trabalho.
1. Política de IA organizacional em português, aberta, com cláusulas ancoradas na LGPD. Os modelos brasileiros oficiais cobrem privacidade e dados (RIPD, PPSI) e uso de genAI no setor público (GuIA, TCU), não uma política de IA completa de organização.
2. Guardrails brasileiros empacotados: regras de LGPD, ECA Digital e normas setoriais sobre um motor existente como NeMo Guardrails, com testes. Não apareceu pacote equivalente no recorte.
3. Avaliação executável de requisitos brasileiros: conjuntos de teste públicos que transformem requisitos aplicáveis em casos de teste. Quais requisitos valem para cada organização depende da norma, do setor e do caso, e essa seleção pede validação jurídica. Exemplos de capacidades testáveis levantadas na pesquisa: explicação de decisões automatizadas, aviso de interação com IA e rotulagem de conteúdo sintético. Um teste automatizado é evidência parcial, não prova de conformidade.
4. Formato de evidência técnica em cinco camadas: documentos versionados, avaliação reproduzível, trilhas de execução, linhagem e integridade. O Sandbox Regulatório da ANPD já lista produção de evidências como eixo dos próximos ciclos, o que abre janela de diálogo.
5. Formação em implementação responsável com portfólio verificável: as formações existentes ensinam a usar ou construir IA; neste recorte não apareceu trilha gratuita de governança e implementação responsável com verificação do que a pessoa construiu.
6. Menor prioridade: formato aberto de system card e risk register de IA dedicado. System cards hoje são relatórios publicados pelos próprios fornecedores, sem formato aberto padronizado no recorte.

## Primeiras entregas
1. Kit de documentação pt-BR: política de IA + política de dados + model card/dataset card, sobre as bases com licença verificada (Hugging Face, Model Card Toolkit, Contrast, RIPD/PPSI). Cada peça declara até onde vai: template informativo, checklist de autodeclaração ou preparação para avaliação por terceiros. É uma analogia de maturidade de adoção inspirada no OpenChain, não níveis de conformidade jurídica: autodeclaração e certificação aqui dizem respeito à governança de testes e documentação, não a parecer legal. É a entrega que o grupo já enxerga como primeira.
2. Trilha mínima de governança prática: NIST RMF + GuIA + AI Verify em fluxo único para organizações médias.
3. Piloto do formato de evidência: proposta de aplicar as cinco camadas num caso real. A sugestão é o descoberta-publica receber o primeiro Datasheet no padrão definido, validando o template antes de ele ser proposto a terceiros. É proposta para o grupo decidir, não compromisso assumido.
4. Desenho da trilha de capacitação: imersão prática de seleção + mentoria corporativa + contribuição estipendiada sobre os repositórios do próprio SDK.

A prioridade entre elas é decisão do grupo; a conversa inicial apontou os padrões de documentos como primeira entrega.

## Encaixe real dos projetos do Vini
- TraceFoundry: vocabulário de status epistêmico (fato, inferência, hipótese, lacuna, bloqueio, contradição), claim audit e manifests com proveniência. Candidato reutilizável para o formato de evidência: cada resultado de avaliação carrega um status que separa o medido do inferido do não verificado. O Research Move é um mecanismo documentado de próxima ação proposta; a semelhança com revisão humana registrada é ponto de partida de desenho, não funcionalidade pronta.
- descoberta-publica: referência prática brasileira de integridade de dataset (manifest SHA256, limitações documentadas, licenças separadas: código MIT, conteúdo CC BY 4.0). Candidato natural a receber o primeiro Datasheet-padrão; hoje não tem Datasheet formal nem RIPD.
- TTI Brazil 2017-2024: caso documentado de métrica publicada com validação por fonte independente (Sentinel-2) e hipótese explicativa marcada como candidata, alinhado ao que gestão de risco de modelos pede de validação independente.
- ghostworks: pesquisa de inteligência territorial; não oferece hoje ativos de avaliação ou evidência prontos.

## Como padrões viram produto
OpenChain (Linux Foundation) é a melhor referência: padrão aberto com três caminhos explícitos, autodeclaração, avaliação independente e certificação de terceiros, começando pela autodeclaração de escopo estreito.
- Núcleo aberto, receita nos anéis: certificação e membership de fundação (FinOps, CNCF), treinamento pago (Creative Commons), subscrição sobre código aberto (Red Hat, GitLab), credenciamento de prestadores de teste (AI Verify Foundation).
- Convenção comunitária adota sem certificação: model cards viraram padrão no Hugging Face Hub por convenção.
- Distinção a preservar em toda entrega: autodeclaração não é certificado por organismo, que não é acreditação de organismo. A norma ISO/IEC 42001 é um documento pago e a ISO não emite certificados.

## Limites desta pesquisa
Como ler este mapa: recorte de um dia (9 nov 2026) com fontes primárias. Não encontrado vale para o recorte, nunca como inexistência. Nada aqui é aconselhamento jurídico: frameworks e métodos estrangeiros são insumos, não prova de conformidade com a legislação brasileira.
- PL 2338/2023: proposta, não lei. Aprovado no Senado em dez/2024; a situação atual na Câmara não foi verificada em fonte primária nesta execução (ficha: camara.leg.br, proposição 2487262).
- Licenças verificadas em 9 nov 2026; relicenciamento acontece (o MCP está em transição agora). Revalidar antes de cada release. Candidatos com licença pendente (template de Datasheet JRMeyer, Algoritmeregister, AIA do Canadá, Sunlight) ficam candidatos até a verificação.
- Restrições relevantes para servir terceiros: Phoenix (Elastic License 2.0), lakeFS (BSL 1.1), Llama Guard (licença Meta Community), recursos ee/ do Langfuse.
- Benchmarks brasileiros recentes (Leis Brasileiras, OAB-Bench, Poeta v2) medem capacidade, não conformidade; o leaderboard comunitário em português aparece arquivado.

Síntese consolidada em 9 nov 2026, com licenças e características verificadas em fontes primárias no dia. Documento de trabalho privado.
