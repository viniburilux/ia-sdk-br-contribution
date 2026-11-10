# IA SDK BR: o mapa em uma página

Versão executiva do mapa completo "IA SDK BR: usar, adaptar, criar" (pesquisa de 9 nov 2026). Documento de trabalho privado, preparado para apoiar a conversa com o Everton. Proposta de contribuição para discussão no grupo, não padrão oficial do IA SDK BR.

## Conclusão central

A base para construir, operar, avaliar e governar IA já existe e é aberta. O que não apareceu no recorte foi a versão brasileira dela: documentação, guardrails e avaliação ancorados na legislação e na prática do Brasil. Esse espaço é a oportunidade do grupo.

## Três movimentos

**1. Usar direto.** Componentes maduros com licença aberta verificada em fonte primária:
- Documentação: model cards (Hugging Face, Apache-2.0), Model Card Toolkit e Data Cards Playbook (Google, Apache-2.0), política de IA generativa (Contrast Security, CC BY-SA 4.0).
- Governança: NIST AI RMF, AI Verify (Singapura), e as peças oficiais brasileiras gratuitas: RIPD e Programa de Governança em Privacidade (Governo Digital), GuIA (setor público), guia de genAI do TCU.
- Software: LiteLLM (gateway), Langfuse (observabilidade), Promptfoo e DeepEval (testes), NeMo Guardrails, OpenTelemetry GenAI e MCP (contratos abertos).

**2. Adaptar para o Brasil.**
- Model card e dataset card em português sobre as bases Apache-2.0: adaptação de formato existente, não padrão novo.
- Trilha mínima de governança prática: NIST AI RMF + GuIA + AI Verify traduzidos em um fluxo único para organizações brasileiras médias.
- Presets técnicos: baterias de avaliação em PT-BR prontas para Promptfoo/DeepEval; itens com verificação pendente entram como candidatos.

**3. Criar onde falta (hipóteses a validar com o grupo, não prova de inexistência):**
- Política de IA organizacional em português, aberta, ancorada na LGPD.
- Guardrails com regras brasileiras empacotadas sobre motor existente.
- Avaliação executável de requisitos brasileiros (teste automatizado é evidência parcial, não prova de conformidade).
- Formato de evidência técnica em camadas (documentos versionados, avaliação reproduzível, trilhas de execução, linhagem, integridade).
- Formação em implementação responsável com portfólio verificável.

## Primeira peça proposta

**Kit de documentação de IA em português**: política de uso de IA + política de dados + ficha de modelo/dataset, montado sobre as bases com licença aberta verificada e entregue já preenchido num caso real: o dataset aberto Descoberta Pública (inexigibilidades publicadas no PNCP, v0.1.2, 494 mil registros).

O caso real é o diferencial: mostra o template funcionando, deixa visíveis as lacunas que uma organização precisa resolver e nasce de um ativo que o grupo pode inspecionar. Cada peça declara até onde vai: template informativo, checklist de autodeclaração ou preparação para avaliação por terceiros. Autodeclaração aqui é governança de documentação e testes, não parecer jurídico nem certificação.

Próximas entregas possíveis depois do kit (ordem a decidir pelo grupo): trilha mínima de governança prática, piloto do formato de evidência aplicado a um caso real, desenho da trilha de capacitação.

## Limites

Recorte de um dia (9 nov 2026) com fontes primárias. "Não encontrado" vale para o recorte, nunca como inexistência. Licenças verificadas em 9 nov 2026; revalidar antes de cada release. PL 2338/2023 é proposta, não lei. Nada aqui é aconselhamento jurídico.
