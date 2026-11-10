# Frente 1 — Padrões, Governança e Documentação de IA
## Mapa do que já existe (insumo para síntese do IA SDK BR)

Data da pesquisa: 09/11/2026. Escopo: recursos reutilizáveis, formatos, grau de abertura e links oficiais para políticas de IA, políticas de dados, model cards, documentação de datasets, system cards, inventários e registros de impacto/risco. Leis, PLs, frameworks e guias ficam em blocos separados. Afirmações de ausência significam "não encontrado neste recorte", nunca inexistência.

---

## A) Model cards (documentação de modelos)

1. **Hugging Face Model Cards** — formato MD + metadados YAML (licença, datasets, métricas, usos, limitações). Templates no SDK huggingface_hub. **Licença: Apache 2.0 (confirmada nos metadados do repo).**
   - https://huggingface.co/docs/hub/model-cards
   - https://huggingface.co/docs/huggingface_hub/guides/model-cards
   - https://github.com/huggingface/huggingface_hub/tree/main/src/huggingface_hub/templates
2. **Google Model Card Toolkit** — templates Jinja modificáveis, exporta HTML/MD/JSON com esquema padronizado. **Licença: Apache 2.0 (confirmada). Atenção: repo marcado como ARCHIVED** — código utilizável, sem manutenção ativa.
   - https://www.tensorflow.org/responsible_ai/model_card_toolkit/guide/templates
   - https://github.com/tensorflow/model-card-toolkit
3. **BigScience Model Card + licenças OpenRAIL/RAIL** — licenciamento de modelos abertos com restrições de uso responsável embutidas; catalogado pela OECD.AI. Licença do template de card a confirmar no repo.
   - https://github.com/bigscience-workshop/model_card
   - https://www.licenses.ai/blog/2022/8/26/bigscience-open-rail-m-license
   - https://oecd.ai/en/catalogue/tools/bigscience-openrail-m-license

## B) System cards (documentação do sistema inteiro)

4. System cards da OpenAI (GPT-4o, o3/o4-mini) e da Meta documentam modelo + produto + mitigações, publicados como relatórios pelos próprios fornecedores. **Não encontrei neste recorte um formato aberto padronizado de system card** — é prática da indústria a observar, não template verificadamente reutilizável.
   - https://openai.com/pt-BR/index/gpt-4o-system-card/
   - https://ai.meta.com/tools/system-cards/

## C) Documentação de datasets

5. **Datasheets for Datasets** (Gebru et al.) — questionário canônico. Template Markdown pronto (JRMeyer): **sem licença identificada neste recorte — classificar como candidato pendente de verificação, não adaptável garantido.**
   - https://dl.acm.org/doi/10.1145/3458723
   - https://github.com/JRMeyer/markdown-datasheet-for-datasets
6. **Google PAIR Data Cards Playbook** — **Licença: Apache 2.0 (confirmada nos metadados do repo; repo arquivado, conteúdo aproveitável).**
   - https://sites.research.google/datacardsplaybook
   - https://github.com/PAIR-code/datacardsplaybook
7. **Hugging Face Dataset Cards** — padrão de facto para datasets abertos (mesma base Apache 2.0 do SDK).
   - https://huggingface.co/docs/hub/main/datasets-cards
8. **Croissant (MLCommons)** — metadados JSON-LD legíveis por máquina para datasets de ML; projeto open source da MLCommons, v1.1 de fev/2026. Licença do repo a confirmar.
   - https://docs.mlcommons.org/croissant/
   - https://github.com/mlcommons/croissant
9. **Open Datasheets** — framework machine-readable sobre Frictionless Datapackage com seção de Responsible AI.
   - https://arxiv.org/html/2312.06153v2

## D) Frameworks de governança e risco

**Gratuitos:**
10. **NIST AI RMF 1.0 + Playbook + Generative AI Profile** — PDFs livres.
    - https://www.nist.gov/itl/ai-risk-management-framework
    - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
    - https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
11. **AI Verify (Singapura)** — framework de governança + toolkit de testes; open-sourced oficialmente (fact sheet IMDA), código no GitHub.
    - https://www.imda.gov.sg/assets/c4b88a08-ea08-4334-a6ac-cdaafbebd3ce.pdf
    - https://github.com/aiverify-foundation/aiverify
12. **OECD.AI** — observatório de políticas + catálogo de ferramentas de governança (meta-mapa para curadoria).
    - https://oecd.ai/
13. **UNESCO Recomendação sobre Ética da IA** — camada de princípios, livre.

**Pagos (não são templates abertos):**
14. **ISO/IEC 42001:2023** (sistema de gestão de IA, certificável) e **ISO/IEC 23894** (gestão de risco de IA) — vendidos pela ISO/ABNT. Referência de maturidade, não base de template aberto.
    - https://www.iso.org/standard/42001

## E) Avaliação de impacto e registros de risco

15. **Algorithmic Impact Assessment (AIA) do Canadá** — questionário oficial com pontuação de risco, código aberto (canada-ca/aia-eia-js) e resultados publicados no portal de governo aberto. Modelo governamental mais completo deste recorte para avaliação de impacto algorítmico. Licença do código a confirmar.
    - https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/automated-decision-making/algorithmic-impact-assessment.html
    - https://github.com/canada-ca/aia-eia-js
    - https://open.canada.ca/data/en/dataset/5423054a-093c-4239-85be-fa0b36ae0b2e
16. **RIPD (LGPD)** — Guia de elaboração + Modelo de RIPD do Governo Digital (v1.0, jul/2026) e página oficial da ANPD. Peça brasileira, gratuita, reutilizável para registro de impacto envolvendo dados pessoais.
    - https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi-2.0/arquivos/guia-para-elaboracao-de-ripds-v0-1-31072026.pdf
    - https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi-2.0/arquivos/modelo-de-ripd-v1-0-31072026.pdf
    - https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/relatorio-de-impacto-a-protecao-de-dados-pessoais-ripd

> Nota: para registro contínuo de decisões e risk register no ciclo de vida, neste recorte encontrei cobertura apenas dentro de frameworks (NIST RMF, função Govern; ISO 31000/23894, pagos). Não encontrei template aberto dedicado a risk register de IA.

## F) Inventário / registro público de algoritmos

17. **Padrão holandês de registro de algoritmos (Algoritmeregister)** — padrão aberto no GitHub para registros públicos de transparência, adotado por municípios. Base para "inventário de sistemas de IA" publicável. Licença do repo a confirmar.
    - https://www.algorithmregister.org/
    - https://github.com/Algoritmeregister/standard

## G) Políticas de IA e termos de uso de genAI (organizacionais)

18. **Contrast Security Generative AI Policy** — política organizacional de genAI pronta. **Licença: CC BY-SA 4.0 (confirmada no README do repo)** — adaptável com atribuição e compartilhamento pela mesma licença.
    - https://github.com/Contrast-Security-OSS/GenerativeAIPolicy
19. **AI Policy Tracker — template de Acceptable Use Policy** — público; licença de reuso não identificada neste recorte (consulta/referência).
    - https://aipolicytracker.org/templates/acceptable-use-policy
20. **EU AI Act — Regulamento (UE) 2024/1689** (texto primário, EUR-Lex, em vigor). Art. 11 + Anexo IV definem conteúdo obrigatório da documentação técnica de sistemas de alto risco. É obrigação regulatória, não template; templates DOCX/MD de terceiros circulam sem status oficial.
    - https://eur-lex.europa.eu/eli/reg/2024/1689/oj
21. **Guia TCU de uso de IA generativa** — exemplo brasileiro de política interna de uso de genAI no setor público.
    - https://ia.tcu.gov.br/governanca.html

## H) Políticas de dados

**Governança e proteção organizacional (o sentido do pedido):**
22. **Modelo de Programa de Governança em Privacidade** (Governo Digital PPSI 2.0, jun/2026) — modelo oficial brasileiro gratuito.
    - https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi-2.0/arquivos/modelo-de-programa-de-governanca-em-privacidade-v1-0-30062026.pdf
23. **Decreto 10.046/2019 + Comitê Central de Governança de Dados + Cartilha de Governança de Dados (2026)** — estrutura e guias oficiais de governança de dados no setor público federal.
    - https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10046.htm
    - https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/governancadedados/comite-central-de-governanca-de-dados
24. **Guia CNMP/UEPDAP de Programa de Governança em Privacidade** — alternativa setorial (Ministério Público).
    - https://www.cnmp.mp.br/portal/images/uepdap/documentos/Guia_do_Programa_de_Governan%C3%A7a_em_Privacidade_-_UEPDAP_atualizado_1.pdf

**Dados abertos (escopo distinto: governo aberto; não equivale a governança interna):**
25. Sunlight Open Data Policy Hub + gerador (open source, GitHub; licença a confirmar).
    - https://github.com/sunlightpolicy/open-data-policy-hub
26. Kit do Plano de Dados Abertos (governo federal BR) — modelos oficiais para dados abertos.
    - https://github.com/dadosgovbr/kit

## I) Marco brasileiro (níveis distintos — não misturar)

- **PL 2338/2023: proposta, não lei.** Aprovado no Senado em dez/2024. Situação atual na Câmara **não verificada em fonte primária nesta execução** (ficha não renderizou; monitoramentos secundários indicam tramitação sem votação, tratado como não confirmado). Verificar antes de citar: https://www.camara.leg.br/proposicoesWeb/fichadetramitacao/?idProposicao=2487262
- **EBIA** (Portaria MCTI 4.617/2021): estratégia, não norma.
  - https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/transformacaodigital/ebia.pdf
- **LGPD** (Lei 13.709/2018): lei vigente, ancora políticas de dados. ANPD mantém sandbox regulatório de IA com manual público.
  - https://www.gov.br/anpd/pt-br/assuntos/projetos-acoes-iniciativas/sandbox/manual-do-sandbox/@@display-file/file
- **GuIA** — Guia Unificado de IA para o setor público: guia prático oficial gratuito.
  - https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/guia-unificado-de-inteligencia-artificial-para-o-setor-publico-1/GuIA
- **Resolução CNJ 615/2025** — norma setorial vigente no Judiciário, **com alterações da Resolução CNJ 674/2026** (confirmado em domínio oficial; usar o texto compilado).
  - https://atos.cnj.jus.br/atos/detalhar/6001
  - https://atos.cnj.jus.br/atos/detalhar/6836
- **Toolkit CGI.br de prontidão/capacidade em IA** (G20 2024, bilíngue) e **Cartilha CERT.br de Segurança em IA** — gratuitos.
  - https://www.cgi.br/publicacao/toolkit-para-avaliacao-da-prontidao-e-da-capacidade-em-inteligencia-artificial/
  - https://cartilha.cert.br/fasciculos/ia/fasciculo-ia.pdf

## J) Verificação de licença dos candidatos à primeira entrega

| Recurso | Licença | Fonte | Status para reuso |
| --- | --- | --- | --- |
| HF Model Cards / Dataset Cards (templates no huggingface_hub) | Apache 2.0 | metadados do repo GitHub | Adaptável |
| Google Model Card Toolkit | Apache 2.0 | metadados do repo GitHub | Adaptável (repo ARCHIVED, sem manutenção ativa) |
| Google PAIR Data Cards Playbook | Apache 2.0 | metadados do repo GitHub | Adaptável (repo arquivado) |
| Contrast Generative AI Policy | CC BY-SA 4.0 | README do repo | Adaptável com atribuição + share-alike |
| JRMeyer markdown datasheet | não identificada | — | Candidato pendente de verificação |
| AI Policy Tracker (acceptable use) | não identificada | — | Consulta/referência |
| Croissant, Sunlight, Algoritmeregister, AIA Canadá | código aberto, licença específica a confirmar | — | Candidato pendente de verificação |

## K) Leitura de lacunas (insumo para a síntese)

1. Neste recorte não encontrei template organizacional de política de IA em pt-BR ancorado na LGPD com licença aberta explícita. Os modelos brasileiros oficiais cobrem privacidade/governança de dados (RIPD, PPSI, CCGD) e guias de uso (GuIA, TCU), não uma política de IA completa de organização. Pode existir fora do recorte.
2. Neste recorte não encontrei model cards nem dataset cards em português; a base HF/MCT é em inglês. Há artigos de blog BR explicando, não templates.
3. Croissant emerge como padrão machine-readable de datasets; adotar evita criar padrão novo.
4. Governança gratuita já existe (NIST RMF, AI Verify); a lacuna aparente é traduzir em fluxo prático para organizações brasileiras médias, não criar framework novo.
5. System cards: não encontrei padrão aberto no recorte — possível espaço para o IA SDK BR propor formato, se fizer sentido.
6. Onde "criar algo novo" se justifica nesta frente (hipótese para a síntese): política de IA aberta pt-BR com cláusulas LGPD; model card/dataset card pt-BR sobre a base HF/MCT (Apache 2.0); trilha mínima NIST RMF + GuIA; formato aberto de system card; risk register de IA dedicado.

## Incertezas assumidas

- Status atual do PL 2338/2023 na Câmara: não verificado em fonte primária.
- Licenças marcadas "a confirmar": código aberto verificado, termos de reuso específicos não.
- iasdkbr.org e o repo Everton-baptista/iasdk-br não tinham conteúdo de padrões publicado nesta data.
- Todas as URLs acima foram retornadas por busca/fetch nesta execução; páginas dinâmicas (gov.br, EUR-Lex, Câmara) nem sempre renderizaram conteúdo completo no fetch, mas os links foram confirmados via resultados de busca.
