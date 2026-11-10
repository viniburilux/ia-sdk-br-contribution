# Política de dados (template pt-BR + exemplo preenchido)

**Peça 2 do kit de documentação de IA pt-BR - rascunho v0.1, 9 nov 2026.**

- **Base adaptada:** peças oficiais brasileiras gratuitas identificadas no mapa: RIPD - Relatório de Impacto à Proteção de Dados Pessoais (ANPD), Programa de Governança em Privacidade (Governo Digital) e, para o setor público, GuIA. Documentos públicos do governo; aqui reorganizados como política de dados para organizações em geral.
- **Maturidade declarada desta peça:** template informativo + checklist de autodeclaração. Não substitui RIPD formal quando ele for exigido, não é parecer jurídico, não é certificação.
- **Convenção:** texto em colchetes `[...]` é ponto de preenchimento. `[LACUNA: ...]` marca informação que o caso real ainda não tem e que não foi inventada.

---

## 1. Finalidade

Esta política define como `[ORGANIZAÇÃO]` coleta, trata, armazena, publica e descarta dados, com atenção especial a dados pessoais sob a LGPD (Lei nº 13.709/2018).

## 2. Escopo

Cobre `[SISTEMAS/PRODUTOS]` e todas as pessoas que trabalham com esses dados, incluindo terceiros.

## 3. Fontes de dados e licenças

Para cada fonte, registrar: origem, forma de acesso, natureza (pública ou não), licença ou termo de uso e restrições.

| Fonte | Acesso | Natureza | Licença/termo | Restrições |
|---|---|---|---|---|
| `[FONTE]` | `[API/download]` | `[pública]` | `[licença]` | `[restrições]` |

## 4. Bases legais do tratamento

Declarar a base legal de cada tratamento que envolva dado pessoal (LGPD, art. 7º e art. 11). `[LACUNA GENÉRICA: enquadrar o caso concreto exige validação jurídica; esta política não faz esse enquadramento.]`

## 5. Ciclo de vida dos dados

- **Coleta:** `[o que é coletado, de onde, com que frequência]`
- **Armazenamento:** `[onde ficam os brutos e os tratados; o que é público e o que é privado]`
- **Tratamento e transformação:** `[limpeza, enriquecimento, classificação; registrar regras]`
- **Publicação:** `[o que é publicado, em que formato, com que licença]`
- **Retenção e descarte:** `[prazos e critérios]`

## 6. Regras para dados pessoais

- Princípio da precaução: dado pessoal identificado em campo não estruturado (texto livre) é tratado como risco de publicação, mesmo quando a fonte é pública.
- Antes de cada publicação: verificar identificadores pessoais `[LISTA: CPF, RG, e-mail pessoal, endereço residencial, nomes de beneficiários de programas sociais, ...]` e aplicar mascaramento ou remoção conforme `[CRITÉRIO]`.
- Registrar o que foi mascarado/removido e onde fica o original (privado), para rastreabilidade.
- Distinguir mascaramento de anonimização: se o registro de origem segue público na fonte, o dado não foi anonimizado, e a política deve dizer isso.

## 7. Integridade e rastreabilidade

- Manter manifesto de hashes (ex.: SHA256) dos arquivos publicados.
- Verificar contagens após cada transformação e registrar.
- Documentar limitações conhecidas em arquivo próprio e apontá-lo em todo material de distribuição.

## 8. Incidentes e aprendizados

Registrar incidentes de dados (ex.: exposição indevida) com data, causa, ação tomada e mudança de processo resultante.

## 9. Papéis

- Responsável pela política: `[NOME/PAPEL]`
- Encarregado de proteção de dados (se aplicável): `[LACUNA: definir se a organização nomeia encarregado e quem]`

## 10. Revisão

Revisar a cada `[PERÍODO]` ou a cada nova fonte de dados, o que vier primeiro.

---

## Exemplo preenchido: Descoberta Pública / LuxVerso

Aplicado ao dataset "Inexigibilidades publicadas no PNCP", edição v0.1.2 (fatos lidos no README público do repositório e no histórico da iniciativa).

**Fontes (preenchido):**

| Fonte | Acesso | Natureza | Licença/termo | Restrições |
|---|---|---|---|---|
| PNCP | API de dados abertos, sem cadastro | pública | dados públicos governamentais | o pacote não concede nem restringe direitos sobre os registros |
| IBGE | download público | pública | `[LACUNA: registrar termo exato]` | - |
| Siconfi/Tesouro Nacional | download público | pública | `[LACUNA: registrar termo exato]` | - |

**Ciclo de vida (preenchido):**

- **Coleta:** registros de inexigibilidade publicados no PNCP entre 01/01/2025 e 06/11/2026 (o período de 22 a 31/08/2026 não está na base); 494.446 registros únicos, 27 UFs.
- **Armazenamento:** dados brutos e material de trabalho em repositório privado; cópia tratada no repositório público.
- **Tratamento:** classificação do objeto por categorias, com metodologia e validação abertas; dimensão de municípios com população e PIB (IBGE) e receita (Siconfi). `[LACUNA: declarar se a classificação usou modelo de IA, qual, e com que revisão humana.]`
- **Publicação:** pacote em Parquet com ferramentas de consulta, código sob MIT, curadoria/documentação/derivados sob CC BY 4.0, com atribuição definida no README.
- **Retenção:** `[LACUNA: sem política de retenção/descarte escrita.]`

**Dados pessoais (preenchido, fato registrado):** o texto livre escrito pelos órgãos nos registros do PNCP carrega CPF, RG, e-mail pessoal, endereço residencial e nomes de famílias beneficiárias de programas sociais. A iniciativa mascarou esses identificadores na edição pública, manteve nomes de fornecedores, órgãos e municípios (substância pública dos atos), guardou o original em privado e declarou publicamente que isso é mascaramento, não anonimização, porque os registros de origem seguem públicos no PNCP. O episódio chegou a derrubar o acesso público por precaução e voltou no mesmo dia, com a cópia sanitizada. `[LACUNA: transformar a decisão em critério escrito e reproduzível (o que mascara, o que mantém, quem revisa).]`

**Integridade (preenchido):** 621 arquivos brutos com SHA256 conferido (100%); contagens por UF/ano verificadas após cada transformação; hashes da edição em `manifest_v012.json`; limitações em `docs/LIMITACOES.md`.

**Bases legais:** `[LACUNA: o enquadramento formal na LGPD (incluindo a leitura de dados manifestamente públicos) não foi feito com validação jurídica. A iniciativa adotou precaução sem ter identificado obrigação legal.]`

**Papéis:** `[LACUNA: não há encarregado formal; iniciativa de uma pessoa com colaboradores eventuais.]`

**RIPD:** `[LACUNA: não existe RIPD formal. O mapa registra o dataset como candidato natural a receber a primeira documentação no padrão do kit; o RIPD seria o passo seguinte se houver exigência ou decisão do grupo.]`

**O que este exemplo mostra:** a iniciativa já pratica integridade e precaução acima do comum (hashes, limitações, mascaramento declarado), e mesmo assim faltam peças formais: bases legais validadas, critério escrito de mascaramento, retenção e papéis. É exatamente o tipo de lacuna que a política existe para tornar visível.
