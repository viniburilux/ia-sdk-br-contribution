# Política de uso de IA (template pt-BR + exemplo preenchido)

**Peça 1 do kit de documentação de IA pt-BR - rascunho v0.1, 9 nov 2026.**

- **Base adaptada:** "Open Source Generative AI Policy", Contrast Security (github.com/Contrast-Security-OSS/GenerativeAIPolicy), licença CC BY-SA 4.0. Esta adaptação é um derivado: ao publicar, manter licença CC BY-SA 4.0 e atribuição à Contrast Security.
- **Adaptação ao Brasil:** referências a GDPR e APPI substituídas pela LGPD (Lei nº 13.709/2018); papéis de CISO/DPO traduzidos para a realidade de organizações pequenas.
- **Maturidade declarada desta peça:** template informativo + checklist de autodeclaração. Não é parecer jurídico, não é certificação.
- **Convenção:** texto em colchetes `[...]` é ponto de preenchimento. `[LACUNA: ...]` marca informação que o caso real ainda não tem e que não foi inventada.

---

## 1. Visão geral

A política de IA de `[ORGANIZAÇÃO]` existe para proteger pessoas, dados e o trabalho da organização contra usos prejudiciais, antiéticos ou ilegais de IA, por acidente ou intenção. A organização acredita que ferramentas de IA ajudam o trabalho e quer disponibilizá-las de forma segura e em conformidade com a legislação brasileira, em especial a LGPD.

Preocupações centrais (adaptadas da base):

- criar propriedade intelectual ou software cuja titularidade não possa ser defendida depois;
- código gerado por IA contendo componentes maliciosos ou com licença incompatível;
- sistemas públicos de IA aprenderem com dados não públicos da organização, de clientes ou de terceiros;
- acesso indevido a dados sensíveis por usuários sem privilégio.

## 2. Definições

- **IA generativa:** técnicas de IA que geram dados novos e originais (texto, código, imagem), em vez de apenas classificar ou prever sobre dados existentes.
- **Ferramenta de IA aprovada:** aquela com relação contratual ou licença avaliada por `[RESPONSÁVEL]`, com garantias sobre confidencialidade dos dados fornecidos. Lista mantida em `[LOCAL DA LISTA]` e revisada a cada `[PERÍODO, sugestão da base: 180 dias]`.
- **Ferramenta de IA não aprovada:** qualquer outra. Nela só entra informação já pública.
- **deve:** requisito; não conformidade exige registro formal de exceção.
- **deveria:** requisito; não conformidade exige justificativa de negócio por escrito, apresentável quando solicitada.
- **pode:** explicitamente permitido, mesmo que pareça conflitar com outro requisito.

## 3. Escopo

Aplica-se a empregados, contratados, consultores, temporários e terceiros que trabalhem para a organização ou usem seus recursos computacionais, contas ou dados.

## 4. Política

**O responsável por `[PAPEL, na base: CISO]` deve:**

- manter a lista de ferramentas de IA aprovadas, com: nome da ferramenta, tipos de dado permitidos como entrada e tipo de hospedagem (SaaS público, SaaS privado, local);
- atualizar a lista no mínimo a cada `[180] dias`.

**O responsável por privacidade `[PAPEL, na base: DPO/encarregado]` deve:** informar ao time as novidades de legislação e regulação sobre IA e proteção de dados.

**Todas as pessoas cobertas devem:**

- usar apenas ferramentas licenciadas, fornecidas ou construídas pela organização, conforme esta política e a LGPD;
- usar identidade oficial da organização para acessar sistemas de IA;
- em ferramenta não aprovada: inserir somente informação pública;
- em ferramenta aprovada: inserir apenas os tipos de dado que ela está autorizada a receber, e respeitar controle de acesso por privilégio mínimo.

**Uma ferramenta é considerada não aprovada até que `[RESPONSÁVEL]` a aprove.** Fluxo de aprovação: `[LACUNA: descrever fluxo]`.

## 5. Aceite de risco

Somente `[PAPEL, na base: dono da política/CEO/CISO/CTO]` pode conceder exceções por escrito a esta política.

## 6. Exceções

- Nenhuma exceção registrada.

## 7. Conformidade

Violações podem gerar medidas disciplinares. A organização coopera com autoridades quando legalmente exigido. Leis aplicáveis prevalecem sobre esta política. É proibida retaliação contra quem reporta violação de boa fé. Dúvidas e relatos: `[CONTATO]`.

## 8. Histórico de revisão

| Data | Versão | Alteração |
|---|---|---|
| `[DATA]` | 0.1 | Rascunho inicial adaptado da base Contrast Security |

## 9. Referências

- Base: Contrast Security, Open Source Generative AI Policy, CC BY-SA 4.0.
- LGPD: Lei nº 13.709/2018.
- Complementos brasileiros sugeridos pelo mapa: RIPD (ANPD), Programa de Governança em Privacidade (Governo Digital), guia de genAI do TCU (setor público), GuIA.

---

## Exemplo preenchido: Descoberta Pública / LuxVerso

Como a peça fica quando aplicada ao caso real (iniciativa de dados públicos mantida por Vinícius Buri Lux, com colaboradores eventuais). Serve para demonstrar o template e para expor o que falta.

**Visão geral (preenchida):** a iniciativa usa ferramentas de IA generativa no dia a dia de pesquisa, classificação e redação, incluindo assistentes públicos de vários fornecedores. O dado central da iniciativa é público por origem (PNCP, IBGE, Siconfi), o que muda o perfil de risco: o maior risco não é vazar segredo comercial, é republicar dado pessoal que aparece em texto livre dos registros de origem, e perder a titularidade do que a iniciativa cria (classificações, curadoria, documentação).

**Lista de ferramentas aprovadas:** `[LACUNA: não existe lista formal. Hoje são usados assistentes públicos de IA de vários fornecedores (conversas com ChatGPT, Grok, DeepSeek e outros constam no histórico da iniciativa). Definir lista, tipos de dado permitidos e hospedagem.]`

**Regra prática já aplicada (fato, não hipótese):** na edição v0.1.2 do dataset, identificadores pessoais escritos pelos órgãos no texto livre (CPF, RG, e-mail pessoal, endereço residencial) foram mascarados antes da publicação, e nomes de famílias beneficiárias de programas sociais foram removidos. O material original e o histórico ficaram em repositório privado. Foi uma decisão de precaução, não exigência legal identificada. Esta regra deveria virar cláusula escrita da política de dados (peça 2 do kit).

**Papéis:** `[LACUNA: iniciativa de uma pessoa; não há CISO nem encarregado formal. A LGPD prevê encarregado; a necessidade e a forma para uma iniciativa deste porte é ponto a validar juridicamente.]`

**Fluxo de aprovação e exceções:** `[LACUNA: inexistentes hoje; para uma pessoa, o mínimo é um registro escrito no próprio repositório.]`

**O que este exemplo mostra:** o template funciona para organização pequena, mas expõe decisões reais que a base estrangeira não resolve: quem responde por privacidade sem estrutura formal, e como tratar dado público de origem que carrega dado pessoal no texto livre. Essas lacunas visíveis são parte da entrega.
