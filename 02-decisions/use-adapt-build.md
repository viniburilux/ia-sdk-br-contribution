# Decisão: usar, adaptar, criar

Extraído da síntese da investigação (ver `01-ecosystem-map/full-ecosystem-map.md`). Esta é a decisão de contribuição que nasce do mapa: o que o grupo pode usar direto, o que precisa adaptar ao Brasil e onde faria sentido criar algo novo. Proposta para discussão no grupo, não padrão decidido.

## Conclusão central

A base para construir, operar, avaliar e governar IA já existe e é aberta. O que não apareceu no recorte foi a versão brasileira dela: documentação, guardrails e avaliação ancorados na legislação e na prática do Brasil. Esse espaço é a oportunidade do grupo.

## 1. Usar direto

Componentes maduros com licença aberta verificada em fonte primária (detalhes e URLs nas frentes):

- **Documentação:** model cards (Hugging Face, Apache-2.0), Model Card Toolkit e Data Cards Playbook (Google, Apache-2.0), política de IA generativa (Contrast Security, CC BY-SA 4.0).
- **Governança:** NIST AI RMF, AI Verify (Singapura), e as peças oficiais brasileiras gratuitas: RIPD e Programa de Governança em Privacidade (Governo Digital), GuIA (setor público), guia de genAI do TCU.
- **Software:** LiteLLM (gateway), Langfuse (observabilidade), Promptfoo e DeepEval (testes), NeMo Guardrails, OpenTelemetry GenAI e MCP (contratos abertos).

## 2. Adaptar para o Brasil

- Model card e dataset card em português sobre as bases Apache-2.0: adaptação de formato existente, não padrão novo.
- Trilha mínima de governança prática: NIST AI RMF + GuIA + AI Verify traduzidos em um fluxo único para organizações brasileiras médias.
- Presets técnicos: baterias de avaliação em PT-BR prontas para Promptfoo/DeepEval; itens com verificação pendente entram como candidatos.

## 3. Criar onde falta

Hipóteses a validar com o grupo, não prova de inexistência (detalhadas em `identified-gaps.md`):

1. Política de IA organizacional em português, aberta, ancorada na LGPD.
2. Guardrails com regras brasileiras empacotadas sobre motor existente.
3. Avaliação executável de requisitos brasileiros (teste automatizado é evidência parcial, não prova de conformidade).
4. Formato de evidência técnica em camadas (documentos versionados, avaliação reproduzível, trilhas de execução, linhagem, integridade).
5. Formação em implementação responsável com portfólio verificável.

## Primeira peça decidida para prototipar

**Kit de documentação de IA em português** (política de uso de IA + política de dados + ficha de modelo/dataset), montado sobre as bases com licença aberta verificada e entregue já preenchido num caso real: o dataset aberto Descoberta Pública. Está em `03-implementation-pack/`, com o exemplo em `04-examples/descoberta-publica/`.

O caso real é o diferencial: mostra o template funcionando, deixa visíveis as lacunas que uma organização precisa resolver e nasce de um ativo que o grupo pode inspecionar. Cada peça declara até onde vai: template informativo, checklist de autodeclaração ou preparação para avaliação por terceiros. Autodeclaração aqui é governança de documentação e testes, não parecer jurídico nem certificação.

Próximas entregas possíveis depois do kit (ordem a decidir pelo grupo): trilha mínima de governança prática, piloto do formato de evidência aplicado a um caso real, desenho da trilha de capacitação. Ver `06-roadmap/next-experiments.md`.
