# Exemplo preenchido: Descoberta Pública

Consolidação dos três exemplos preenchidos do kit (`03-implementation-pack/`), aplicados ao caso real: dataset "Inexigibilidades publicadas no PNCP", edição v0.1.2, da iniciativa Descoberta Pública (LuxVerso). Fatos lidos no README público do repositório (github.com/viniburilux/descoberta-publica) em 9 nov 2026 e no histórico da iniciativa. O que não tinha informação ficou marcado como LACUNA - nada foi inventado.

## Política de uso de IA (exemplo)

A iniciativa usa ferramentas de IA generativa no dia a dia de pesquisa, classificação e redação, incluindo assistentes públicos de vários fornecedores. O dado central é público por origem (PNCP, IBGE, Siconfi), o que muda o perfil de risco: o maior risco não é vazar segredo comercial, é republicar dado pessoal que aparece em texto livre dos registros de origem, e perder a titularidade do que a iniciativa cria (classificações, curadoria, documentação).

**Regra prática já aplicada (fato, não hipótese):** na edição v0.1.2, identificadores pessoais escritos pelos órgãos no texto livre (CPF, RG, e-mail pessoal, endereço residencial) foram mascarados antes da publicação, e nomes de famílias beneficiárias de programas sociais foram removidos. O material original e o histórico ficaram em repositório privado. Foi uma decisão de precaução, não exigência legal identificada.

## Política de dados (exemplo)

**Fontes:** PNCP (API de dados abertos, sem cadastro), IBGE (download público) e Siconfi/Tesouro Nacional (download público).

**Ciclo de vida:** coleta de registros publicados no PNCP entre 01/01/2025 e 06/11/2026 (o período de 22 a 31/08/2026 não está na base), 494.446 registros únicos, 27 UFs; brutos e material de trabalho em repositório privado, cópia tratada no repositório público; classificação do objeto por categorias com metodologia e validação abertas; publicação em Parquet com ferramentas de consulta, código sob MIT, curadoria/documentação/derivados sob CC BY 4.0.

**Dados pessoais (fato registrado):** o texto livre dos registros do PNCP carrega CPF, RG, e-mail pessoal, endereço residencial e nomes de famílias beneficiárias de programas sociais. A iniciativa mascarou esses identificadores na edição pública, manteve nomes de fornecedores, órgãos e municípios (substância pública dos atos), guardou o original em privado e declarou publicamente que isso é mascaramento, não anonimização, porque os registros de origem seguem públicos no PNCP. O episódio chegou a derrubar o acesso público por precaução e voltou no mesmo dia, com a cópia sanitizada.

**Integridade:** 621 arquivos brutos com SHA256 conferido (100%); contagens por UF/ano verificadas após cada transformação; hashes da edição em `manifest_v012.json`; limitações em `docs/LIMITACOES.md`.

## Ficha do dataset (exemplo, resumo)

- **Identificação:** Inexigibilidades publicadas no PNCP, v0.1.2 (novembro 2026). Mantenedor: Vinícius Buri Lux (LuxVerso). Licenças: código MIT; conteúdo e derivados CC BY 4.0. Citação: "Vinícius Buri Lux (LuxVerso), Descoberta Pública - Inexigibilidades publicadas no PNCP, v0.1.2".
- **Motivação:** tornar a informação pública brasileira usável - coletar, organizar, verificar e devolver em pacotes prontos, sem cadastro nem paywall. Para jornalismo de dados, pesquisa e produtos de transparência; não para quem precisa do valor pago (o dataset carrega valor estimado/homologado).
- **Composição:** 494.446 registros únicos, 27 UFs, modalidade inexigibilidade, publicação entre 01/01/2025 e 06/11/2026; recorte por data de publicação no portal; dimensão de municípios com população e PIB (IBGE) e receita (Siconfi).
- **Coleta e integridade:** API do PNCP + downloads públicos; 621 arquivos brutos com SHA256 conferido (100%); manifesto de hashes da edição.
- **Tratamento:** mascaramento de dados pessoais conforme acima; classificação do objeto declarada material de exploração, não conclusão nem acusação.
- **Usos demonstrados:** consultas por UF, município, esfera, tema e ano (`consultar.py`, duckdb); leitura por qualquer leitor Parquet; produção de histórias jornalísticas pelo canal Quem Pagou Isso?. Desencorajado: tratar valores estimado/homologado como pagos; tratar classificação derivada como conclusão; ignorar `docs/LIMITACOES.md`.
- **Distribuição e manutenção:** repositório público no GitHub, release v0.1.2; mantenedor único; versionamento por edições com manifesto de hashes.

## O que este exemplo mostra

A iniciativa já pratica integridade e precaução acima do comum (hashes, limitações documentadas, mascaramento declarado), e mesmo assim faltam peças formais - listadas em `identified-gaps.md`. É exatamente o tipo de lacuna que os templates existem para tornar visível.
