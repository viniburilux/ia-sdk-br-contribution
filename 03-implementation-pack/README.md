# Implementation Pack pt-BR (kit de documentação de IA)

**Rascunho v0.1, 9 nov 2026.** Primeira peça proposta a partir do mapa: três documentos em português, montados sobre bases com licença aberta verificada, cada um com template e exemplo preenchido num caso real (Descoberta Pública - dataset aberto de inexigibilidades publicadas no PNCP).

## As três peças

| Peça | Arquivo | Base adaptada | Licença da base |
|---|---|---|---|
| Política de uso de IA | `ai-policy.md` | Open Source Generative AI Policy, Contrast Security | CC BY-SA 4.0 |
| Política de dados | `data-policy.md` | RIPD (ANPD), Programa de Governança em Privacidade (Governo Digital), GuIA | documentos públicos do governo brasileiro |
| Ficha de modelo/dataset | `dataset-card.md` | Model cards Hugging Face; Datasheets for Datasets (Gebru et al.); Data Cards Playbook (Google) | Apache-2.0 |

## Avisos de licença e de maturidade

- **A política de uso de IA é um derivado CC BY-SA 4.0:** ao publicar, manter atribuição à Contrast Security e compartilhar pela mesma licença. A atribuição está declarada no cabeçalho do arquivo.
- **Maturidade declarada de cada peça:** template informativo + checklist de autodeclaração. Não é parecer jurídico, não é certificação, não substitui RIPD formal quando exigido.
- **Convenção:** texto em colchetes `[...]` é ponto de preenchimento. `[LACUNA: ...]` marca informação que o caso real ainda não tem e que não foi inventada.

## Por que vem preenchido

Template vazio mostra formato; template preenchido com caso real mostra serviço. O exemplo deixa visíveis as decisões que uma organização brasileira pequena precisa tomar e que a base estrangeira não resolve (quem responde por privacidade sem estrutura formal, como tratar dado público de origem que carrega dado pessoal no texto livre). O exemplo consolidado e a lista de lacunas estão em `04-examples/descoberta-publica/`.
