# Oportunidades de arquitetura

Onde a investigação aponta que uma arquitetura comum agregaria valor, sem criar software novo onde já existe componente maduro. Detalhes e verificações em `01-ecosystem-map/technical-components.md` e `01-ecosystem-map/evaluation-and-evidence.md`.

## Camadas candidatas (compondo o que já existe)

1. **Gateway de referência** - LiteLLM (MIT) como camada de abstração entre aplicação e provedores de LLM. A contribuição BR não é software novo, é configuração opinada: perfis de provedores usados no Brasil (incluindo modelos nacionais atrás do gateway) e exemplos de logging cuidadosos com dados pessoais.
2. **Observabilidade e trilhas de execução** - Langfuse (MIT no núcleo) + OpenTelemetry GenAI como contrato aberto. Insumo para governança e para a frente de avaliação.
3. **Avaliação executável** - Promptfoo (MIT) / DeepEval (Apache-2.0) para aplicações; lm-evaluation-harness, lighteval e HELM para modelos; Fairlearn, AIF360 e Aequitas para viés. A oportunidade BR: presets e baterias em PT-BR prontas.
4. **Guardrails** - NeMo Guardrails (Apache-2.0) como motor; a oportunidade BR é o pacote de regras (LGPD, ECA Digital, normas setoriais), não o motor.
5. **Evidência em camadas** - documentos versionados (model/dataset cards), avaliação reproduzível, trilhas de execução, linhagem (OpenLineage, Croissant) e integridade (CycloneDX ML-BOM, C2PA). O vocabulário de status epistêmico do TraceFoundry (fato, inferência, hipótese, lacuna, bloqueio, contradição) é candidato reutilizável para separar o medido do inferido do não verificado em cada camada.

## Princípios de desenho que a investigação sustenta

- **Contratos abertos mantêm a arquitetura interoperável** (OpenTelemetry GenAI, MCP): o SDK não prende ninguém a fornecedor.
- **Adotar e perfilar, não inventar:** integridade e inventário já têm padrões abertos; o trabalho é perfil de uso brasileiro.
- **Toda peça declara até onde vai:** template informativo, checklist de autodeclaração ou preparação para avaliação por terceiros. Autodeclaração não é certificado; teste automatizado é evidência parcial, não prova de conformidade.
- **Evidência por padrão:** cada evento relevante gera rastreabilidade, retenção e possibilidade de inspeção (princípio do README do IA SDK BR).

## O que está proposto para testar essas camadas

Os experimentos que tentam ligar essas camadas na prática - com o que rodou e o que quebrou registrado - estão em `05-experiments/`. O primeiro (gateway + avaliação + trilha mínima) já tem registro de execução em `05-experiments/reference-stack/REGISTRO.md`.
