# Roadmap - próximos experimentos e entregas possíveis

**Tudo aqui é proposta para o grupo decidir. Nada é compromisso assumido nem padrão oficial do IA SDK BR.** Atribuição por origem preservada: cada item marca de qual frente da investigação distribuída de 9 nov 2026 ele veio (Imperador, Instinct, ChatGPT, Grok, DeepSeek).

## Sequência sugerida

### Agora (já existe primeira execução)

1. **Stack de referência mínima** - `05-experiments/reference-stack/`: rodada em modo mock; próximos passos registrados no REGISTRO (modelo real, Promptfoo, Langfuse, caso real). (Origem: mapa; stack de referência também proposta por Grok e DeepSeek.)

### Em seguida (candidatos fortes)

2. **Núcleo de avaliação PT-BR** - `05-experiments/evaluation-core/`: EvaluationManifest + bateria PT-BR inicial. (Origem: Imperador; presets PT-BR pelo mapa.)
3. **Pacote de evidência no caso real** - `05-experiments/evidence-pack/`: 5 camadas aplicadas ao Descoberta Pública. (Origem: mapa + TraceFoundry; convergente com ChatGPT.)
4. **Trilha mínima de governança prática** - NIST AI RMF + GuIA + AI Verify em fluxo único para organizações médias. (Origem: mapa, segunda primeira-entrega.)

### Depois (ordem a decidir pelo grupo)

5. **Guardrails brasileiros empacotados** - regras LGPD/ECA Digital/setoriais sobre NeMo Guardrails, com testes. (Origem: mapa, lacuna 2.)
6. **Starter kits setoriais** - 5 kits por setor. (Origem: Imperador.)
7. **Avaliação de prontidão (readiness assessment)** - oferta experimental white-label; não há evidência de demanda pagante, testar como oferta gratuita/com desconto primeiro. (Origem: Imperador; cautela registrada pelo Instinct.)
8. **Mapa de adoção v0.1** - jornada + catálogo curado + esteira demonstrável; encontrar onde organizações travam. (Origem: ChatGPT.)
9. **Trilha de capacitação** - imersão prática de seleção + mentoria corporativa + contribuição estipendiada sobre os repositórios do próprio SDK; estruturas de referência na frente 5. (Origem: mapa, quarta primeira-entrega; Imperador propõe Talent Match BR como MVP.)
10. **Módulo de rastreabilidade com W3C PROV** - linhagem interoperável. (Origem: DeepSeek.)

## O que a investigação NÃO recomenda começar

- Pacote `pip install ia-sdk-br` agora (proposta do Imperador): seria salto do mapa para produto sem o grupo validar a primeira peça. Fica registrado como possibilidade, não como próximo passo.
- Repositório concorrente ao do Everton: este material é contribuição para a conversa, não um projeto paralelo.
- Repetir infra que já existe madura (gateway, observabilidade, avaliação): consenso das cinco frentes.
