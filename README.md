# IA SDK BR - Contribuição: investigação, mapa, decisões, artefatos e experimentos

**Documento de trabalho privado, 9 nov 2026. Proposta de contribuição para discussão no grupo IA SDK BR - não é padrão oficial.**

## Conclusão principal

A base para construir, operar, avaliar e governar IA já existe e é aberta. O que não apareceu no recorte da investigação foi a versão brasileira dela: documentação, guardrails e avaliação ancorados na legislação e na prática do Brasil. Esse espaço é a oportunidade do grupo - e este repositório mostra o caminho completo que levou a essa conclusão e o que já saiu dela.

## A cadeia completa (como navegar)

```
investigação -> mapa do ecossistema -> decisões -> artefatos -> experimentos -> resultados
```

| Etapa | Onde | O que tem |
|---|---|---|
| Investigação | `01-ecosystem-map/` | As 5 frentes completas (governança/documentação, componentes técnicos, avaliação/evidência, modelos de adoção, capacitação), com licenças verificadas em fonte primária, mais o índice de fontes |
| Mapa | `01-ecosystem-map/executive-map.md` (1 página) e `full-ecosystem-map.md` (síntese) | O que usar direto, adaptar ao Brasil e onde criar |
| Decisões | `02-decisions/` | A decisão usar/adaptar/criar, as lacunas identificadas (hipóteses, não provas) e as oportunidades de arquitetura |
| Artefatos | `03-implementation-pack/` | Kit de documentação pt-BR: política de IA, política de dados, ficha de modelo/dataset - templates + exemplo preenchido |
| Exemplo real | `04-examples/descoberta-publica/` | O kit aplicado a um dataset público real, com as lacunas do caso visíveis (nada inventado) |
| Experimentos | `05-experiments/` | Propostas executáveis com registro honesto: o que rodou, o que quebrou, o que falta |
| Resultados | `05-experiments/reference-stack/REGISTRO.md` | Primeiro experimento executado (stack mínima em modo mock) |
| Próximos passos | `06-roadmap/next-experiments.md` | Propostas atribuídas por origem, para o grupo priorizar |

## Como este material nasceu

Em 9 nov 2026, o mesmo prompt de investigação ("o que já existe no mundo que pode ser reutilizado, adaptado ou integrado, e onde existem lacunas") rodou em cinco frentes de IA - Imperador (sistema multi-agente do autor), Instinct, ChatGPT, Grok e DeepSeek - e foi consolidado com verificação de licenças e características em fontes primárias. As divergências e convergências entre as frentes estão preservadas nas propostas atribuídas por origem.

## Avisos

- **Recorte de um dia** com fontes primárias: "não encontrado" vale para o recorte, nunca como inexistência. Nada aqui é aconselhamento jurídico.
- **Licenças:** verificadas em 9 nov 2026; revalidar antes de cada release. A política de IA do kit é derivada de uma base CC BY-SA 4.0 (Contrast Security) - ao publicar, manter atribuição e mesma licença. Detalhes em `03-implementation-pack/README.md`.
- **Experimentos:** resultados são registrados com evidência e incluem falhas; modo mock não valida qualidade de modelo.
