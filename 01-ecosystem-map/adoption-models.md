# Frente 4 - Produtos e modelos de adoção (IA SDK BR) - v2 corrigida
Data: 09/11/2026. Escopo: casos reais de transformar padrões/frameworks/templates/open-source em adoção, produtos e serviços. Grátis vs pago, quem adota, mecanismo de adoção, fontes primárias. Distinções mantidas: autodeclaração != certificado por organismo != acreditação de organismo; norma ISO é documento pago; licenças com restrição de uso (RAIL) não equivalem a open source irrestrito.

## Leitura transversal
Nos casos verificados, o núcleo técnico costuma ser aberto (framework público, toolkit open-source, template, checklist), e a monetização se concentra em anéis ao redor: certificação/conformidade, membership de fundação, treinamento/certificado de pessoas, subscrição/suporte, SaaS e consultoria. Há exceções importantes: a norma ISO/IEC 42001 é um documento pago, e licenças RAIL são abertas com restrições de uso, não permissivas irrestritas. Mecanismos de adoção observados: convenção comunitária (model cards), fundação neutra (MCP na Linux Foundation), credenciamento de prestadores (CNCF KCSP/KTP; AI Verify Tester Accreditation) e mercado de serviços sobre framework público (NIST AI RMF).

## Casos (fontes primárias)

1. OpenChain (Linux Foundation) - padrão aberto com 3 níveis de conformidade
- Grátis: normas ISO/IEC 5230 e 18974 baixáveis do GitHub do projeto; checklists online de autodeclaração.
- Pago: versão formal da norma no site da ISO; certificação de terceira parte é opção, não exigência.
- Mecanismo: três caminhos explícitos - autodeclaração (checklist sim/não, responsabilidade da organização), avaliação independente, certificação de terceiros; o projeto recomenda começar por autodeclaração de escopo estreito.
- https://openchainproject.org/get-started | https://openchainproject.org/news/2025/08/12/updates-to-openchain-self-certification

2. ISO/IEC 42001 - norma paga + distinção certificado/acreditação
- A norma é documento pago vendido pela ISO (página oficial do padrão). A própria ISO não emite certificados: certificação é feita por organismos externos de certificação; acreditação é o reconhecimento independente desses organismos e, segundo a ISO, não é obrigatória.
- https://www.iso.org/standard/81230.html | https://www.iso.org/certification.html

3. EU AI Act (Art. 43) - conformidade regulatória em dois níveis
- Alto risco do Anexo III (pontos 2-8): avaliação de conformidade por controle interno (autoavaliação do provedor). Biometria (ponto 1): escolha entre controle interno e organismo notificado quando normas harmonizadas aplicadas; organismo notificado obrigatório se normas não aplicadas/inexistentes. Normas harmonizadas (Art. 40, desenvolvidas por CEN-CENELEC JTC 21) conferem presunção de conformidade.
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-43 | https://jtc21.eu/

4. NIST AI RMF - framework público gratuito, adoção via serviços
- Grátis e voluntário (FAQ oficial do NIST): AI RMF 1.0 (jan/2023), Perfil GenAI (NIST-AI-600-1, jul/2024), Playbook, Crosswalk e AI Resource Center com casos de uso publicados.
- Mecanismo: adoção apoiada por mercado de consultorias e plataformas de governança; a FAQ não descreve programa de certificação do NIST para o framework.
- https://www.nist.gov/itl/ai-risk-management-framework | https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-faqs

5. Singapura: Model AI Governance Framework + AI Verify Foundation - esteira pública completa
- Grátis: framework voluntário (IMDA, 2019; versão GenAI mai/2024); toolkit AI Verify open-source no GitHub (inclui Project Moonshot para avaliação de LLMs); Global AI Assurance Sandbox conectando deployers e firmas de teste.
- Membership: camadas Premier (por convite, assento no comitê governante) e General; AI Tester Accreditation Programme credencia prestadores terceiros de teste - o modelo público cria padrão e ferramenta abertos e credencia o mercado de verificação.
- https://aiverifyfoundation.sg/ | https://aiverifyfoundation.sg/about-aivf/foundation-members/ | https://github.com/aiverify-foundation/aiverify | https://oecd.ai/en/dashboards/policy-initiatives/model-ai-governance-framework-1337

6. FinOps Foundation - membership financia certificação
- Certificação de ferramenta/prestador sem taxa separada, mas restrita a membros em dia: "membership funds the certification program".
- https://www.finops.org/certification-for-organizations/finops-tool-services-certification-faq/

7. Linux Foundation / Agentic AI Foundation - fundação neutra como infra de adoção
- Projetos permanecem abertos; funding via membership/fundo dirigido com separação declarada entre financiamento e direção técnica; LF fornece governança, IP, treinamento e eventos. Caso IA: Anthropic doou o MCP à Agentic AI Foundation (fundo dirigido LF, cofundada por Anthropic, Block e OpenAI, anunciada dez/2025), junto com goose (Block) e AGENTS.md (OpenAI).
- https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ | https://www.linuxfoundation.org/blog/blog/the-linux-foundation-its-not-just-the-linux-operating-system

8. CNCF - membership em camadas + credenciamento de prestadores
- Camadas Silver/End User/Academic-Nonprofit; Certified Kubernetes é grátis para membros e permite uso da marca; programas KCSP (prestador de serviço) e KTP (parceiro de treinamento) credenciam terceiros.
- https://www.cncf.io/about/join/

9. OWASP - comunidade aberta sustentada por dues
- Projetos e eventos abertos a não-membros; membership pago (dues) dá voto e benefícios; receita por dues, doações e patrocínio de eventos, com finanças publicadas.
- https://owasp.org/policy/membership | https://github.com/OWASP/owasp.github.io/blob/master/pages/finance.md

10. MLCommons - benchmark aberto, participação por membership
- Benchmark AILuminate (segurança) público; participação em working groups e submissão de resultados exige membership ou Non-member Test Agreement.
- https://mlcommons.org/benchmarks/

11. Model cards -> Hugging Face - template adotado por convenção
- Grátis: template de documentação (Mitchell et al., 2018); HF publica Model Card Guidebook e ferramenta Model Card Creator; virou prática padrão no Hub, sem certificação associada.
- https://huggingface.co/docs/hub/model-card-guidebook

12. Datasheets for Datasets - template aberto de documentação de dados
- Questionário aberto (Gebru et al.) para documentar motivação, composição e usos de datasets; instanciado livremente pela comunidade (ex.: mlr3fairness).
- https://mlr3fairness.mlr-org.com/articles/datasheet/datasheet.html

13. Creative Commons - padrão grátis, capacitação paga
- Grátis: licenças e treinamentos básicos (CC BY). Pago: CC Certificate (curso de 10 semanas) e cursos com badges; treinamento institucional customizado sob demanda.
- https://creativecommons.org/cc-training-center/

14. OpenRAIL - licenças abertas com restrições de uso
- Grátis, mas com cláusulas de restrição de uso (não são open source permissivo irrestrito); adoção orgânica no Hugging Face Hub (>8.000 repos com licenças RAIL em 2023, segundo a RAIL Initiative).
- https://www.licenses.ai/license-adoption | https://huggingface.co/blog/open_rail

15. Red Hat - subscrição sobre código aberto
- Código aberto; o produto pago é build testado/certificado + patches + suporte + gestão de ciclo de vida, por subscrição.
- https://www.redhat.com/en/about/subscription-model-faq

16. GitLab - open core documentado
- Modelo open core declarado no handbook: código open source + features source-available pagas; receita majoritariamente de subscrições dos tiers pagos; promessas públicas sobre o que permanece aberto.
- https://about.gitlab.com/company/stewardship/

17. Plataformas de governança de IA (SaaS) - framework vira workflow
- Produto = operacionalizar NIST AI RMF/ISO/EU AI Act em inventário, riscos e evidências. Saidot publica planos por subscrição no próprio site (biblioteca de riscos/controles/políticas); IBM watsonx.governance e outros vendem no mesmo modelo.
- https://www.saidot.ai/pricing

## Insumos para a síntese (apenas o verificado)
- Cada entrega do IA SDK BR deve declarar o nível de conformidade que suporta: template informativo / checklist de autodeclaração (modelo OpenChain) / preparação para avaliação por terceiros (modelo ISO/EU AI Act). As fontes primárias distinguem explicitamente autodeclaração, certificado por organismo e acreditação de organismo.
- Os mecanismos de adoção com evidência: convenção comunitária (model cards, Datasheets), fundação neutra (LF/AAIF), credenciamento de prestadores (CNCF KCSP/KTP, AI Verify Tester Accreditation), mercado de serviços sobre framework público (NIST AI RMF) e subscrição sobre artefato aberto (Red Hat, GitLab, SaaS de governança).

## Ressalvas
- Valores monetários de vendors/ISO foram removidos por virem de agregadores; confirmar nas fontes primárias antes de citar números.
- Bloco sobre regulação brasileira removido: extrapolava o escopo da frente sem sustentação primária atual no contexto deste estudo.
