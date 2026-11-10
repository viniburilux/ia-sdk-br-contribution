# Experimento proposto - Núcleo de avaliação PT-BR (evaluation-core)

**Status: proposta. Não executado.**

## Origem da proposta

- **Imperador** (sistema multi-agente do Vini, investigação distribuída de 9 nov 2026): criar um `EvaluationManifest` (schema pydantic v2) e um núcleo de avaliação como primeira peça de código do grupo, com schemas de TraceFoundry/Lux-Radar como próxima ação imediata.
- **Mapa (Instinct):** presets técnicos - baterias de avaliação em PT-BR prontas para Promptfoo/DeepEval (datasets como o Poeta v2), entrando como adaptação, não padrão novo.

## O que seria

Um pacote mínimo que define, em formato aberto e versionado:

1. o manifesto de uma avaliação (o que se afirma, com que status: fato, inferência, hipótese, lacuna);
2. uma bateria inicial de casos PT-BR ligados a requisitos brasileiros (ex.: aviso de interação com IA, rotulagem de conteúdo sintético);
3. o registro reproduzível do resultado (o formato de `out/results.json` + trilha do experimento 01 é o embrião).

## Limites declarados desde já

Teste automatizado é evidência parcial, não prova de conformidade. Quais requisitos valem para cada organização pede validação jurídica. Esta proposta é hipótese do recorte de 9 nov 2026, a validar com o grupo.
