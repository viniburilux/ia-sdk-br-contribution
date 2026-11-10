# Experimentos

Experimentos são propostas executáveis que nasceram da investigação, registrados com evidência: o que rodou, o que quebrou e o que falta. Uma hipótese do mapa só vira afirmação depois de um registro destes. Falhas contam como resultado.

**Convenção de status:** `proposta` (não executado), `em andamento`, `registrado` (com evidência no diretório). Propostas são atribuídas à origem (qual investigação/agente as sugeriu) e nenhuma é padrão decidido pelo grupo.

| Experimento | Status | Origem da proposta |
|---|---|---|
| `reference-stack/` - stack mínima: gateway + avaliação + trilha | registrado (modo mock, 9 nov 2026) | mapa usar/adaptar/criar (componentes verificados); stack de referência também proposta por Grok e DeepSeek na investigação distribuída |
| `evaluation-core/` - núcleo de avaliação PT-BR (EvaluationManifest) | proposta | Imperador (EvaluationManifest + schemas pydantic); presets PT-BR pelo mapa |
| `evidence-pack/` - pacote de evidência em 5 camadas no caso real | proposta | mapa (lacuna 4) + TraceFoundry; convergente com a leitura do ChatGPT na investigação distribuída |

## Contexto de origem

Em 9 nov 2026, o mesmo prompt de investigação do ecossistema rodou em cinco frentes de IA (Imperador, Instinct, ChatGPT, Grok, DeepSeek). As propostas de experimento deste diretório vêm desse material e do mapa consolidado. Atribuição por origem preservada em cada pasta; convergências e divergências estão em `06-roadmap/next-experiments.md`.
