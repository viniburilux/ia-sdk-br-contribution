# Lacunas identificadas (hipóteses do recorte)

Hipóteses de lacuna levantadas na investigação de 9 nov 2026, **a validar com o grupo antes de comprometer trabalho**. "Não encontrado" vale para este recorte de um dia, nunca como prova de inexistência.

## Lacunas candidatas (da síntese)

1. **Política de IA organizacional em português, aberta, com cláusulas ancoradas na LGPD.** Os modelos brasileiros oficiais cobrem privacidade e dados (RIPD, PPSI) e uso de genAI no setor público (GuIA, TCU), não uma política de IA completa de organização.
2. **Guardrails brasileiros empacotados:** regras de LGPD, ECA Digital e normas setoriais sobre um motor existente como NeMo Guardrails, com testes. Não apareceu pacote equivalente no recorte.
3. **Avaliação executável de requisitos brasileiros:** conjuntos de teste públicos que transformem requisitos aplicáveis em casos de teste. Quais requisitos valem para cada organização depende da norma, do setor e do caso, e essa seleção pede validação jurídica. Exemplos de capacidades testáveis levantadas: explicação de decisões automatizadas, aviso de interação com IA e rotulagem de conteúdo sintético. Um teste automatizado é evidência parcial, não prova de conformidade.
4. **Formato de evidência técnica em cinco camadas:** documentos versionados, avaliação reproduzível, trilhas de execução, linhagem e integridade. O Sandbox Regulatório da ANPD já lista produção de evidências como eixo dos próximos ciclos, o que abre janela de diálogo.
5. **Formação em implementação responsável com portfólio verificável:** as formações existentes ensinam a usar ou construir IA; neste recorte não apareceu trilha gratuita de governança e implementação responsável com verificação do que a pessoa construiu.
6. **Menor prioridade:** formato aberto de system card e risk register de IA dedicado. System cards hoje são relatórios publicados pelos próprios fornecedores, sem formato aberto padronizado no recorte.

## Limites da investigação (para ler junto)

- Recorte de um dia (9 nov 2026) com fontes primárias.
- PL 2338/2023: proposta, não lei. Aprovado no Senado em dez/2024; a situação atual na Câmara não foi verificada em fonte primária nesta execução (ficha: camara.leg.br, proposição 2487262).
- Licenças verificadas em 9 nov 2026; relicenciamento acontece (o MCP está em transição agora). Revalidar antes de cada release. Candidatos com licença pendente (template de Datasheet JRMeyer, Algoritmeregister, AIA do Canadá, Sunlight) ficam candidatos até a verificação.
- Restrições relevantes para servir terceiros: Phoenix (Elastic License 2.0), lakeFS (BSL 1.1), Llama Guard (licença Meta Community), recursos ee/ do Langfuse.
- Benchmarks brasileiros recentes (Leis Brasileiras, OAB-Bench, Poeta v2) medem capacidade, não conformidade; o leaderboard comunitário em português aparece arquivado.
- Nada aqui é aconselhamento jurídico: frameworks e métodos estrangeiros são insumos, não prova de conformidade com a legislação brasileira.

## Lacunas do caso real (Descoberta Pública)

As lacunas que o exemplo preenchido expôs estão consolidadas em `04-examples/descoberta-publica/identified-gaps.md`. Elas são a demonstração prática de por que os templates importam.
