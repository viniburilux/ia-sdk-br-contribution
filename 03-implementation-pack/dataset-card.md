# Ficha de modelo/dataset (template pt-BR + exemplo preenchido)

**Peça 3 do kit de documentação de IA pt-BR - rascunho v0.1, 9 nov 2026.**

- **Bases adaptadas:** estrutura de model cards (Mitchell et al., 2018; template Hugging Face, Apache-2.0) e Datasheets for Datasets (Gebru et al., 2021; Data Cards Playbook do Google, Apache-2.0). Seções reorganizadas em português; ao publicar derivados, manter atribuição e respeitar as licenças das bases.
- **Maturidade declarada desta peça:** template informativo + checklist de autodeclaração. A ficha preenchida declara o que a organização afirma sobre o próprio artefato; não é avaliação independente nem certificação.
- **Convenção:** texto em colchetes `[...]` é ponto de preenchimento. `[LACUNA: ...]` marca informação que o caso real ainda não tem e que não foi inventada.
- **Nota:** este template cobre dataset e modelo. No caso real abaixo o artefato é um dataset (não há modelo de IA publicado), então as seções de modelo aparecem só como lembrete do que preencher quando houver.

---

## A. Identificação

- Nome do artefato: `[NOME + VERSÃO]`
- Mantenedor e contato: `[NOME, CONTATO]`
- Data da edição e cadência de atualização: `[DATA, CADÊNCIA]`
- Licenças: `[código / conteúdo / derivados]`
- Como citar: `[LINHA DE ATRIBUIÇÃO]`

## B. Motivação

- Para que o artefato foi criado? Que pergunta ou necessidade ele atende?
- Quem o criou e com que financiamento?
- Para quem ele é (e para quem ele não é)?

## C. Composição

- O que ele contém (campos, registros, recorte temporal e geográfico)?
- O que ele explicitamente não contém?
- Há dados pessoais ou sensíveis? Em que forma?
- Quais lacunas conhecidas existem no recorte?

## D. Processo de coleta

- De onde vêm os dados e como foram obtidos?
- O recorte é por qual data (evento, publicação, outra)?
- Que verificações de integridade foram feitas?

## E. Tratamento e classificação

- Que limpeza, mascaramento ou remoção foi aplicada?
- Há classificação derivada? Qual método? Houve IA? Houve revisão humana?
- O que do tratamento é material de exploração e não conclusão?

## F. Usos

- Usos previstos e usos já demonstrados.
- Usos desencorajados ou proibidos.
- O que ler antes de reutilizar (limitações documentadas)?

## G. Distribuição

- Onde e como obter; formato; ferramentas de consulta incluídas.
- Licenças e atribuição exigida.

## H. Manutenção

- Quem mantém, com que frequência, e como reportar erro.
- Versionamento e manifesto de integridade.
- Plano para correções e para aposentar versões.

## I. (Quando houver modelo de IA)

- Arquitetura/base, dados de treino, parâmetros relevantes.
- Avaliação: métricas, conjuntos de teste, resultados e data da avaliação.
- Usos pretendidos, usos fora de escopo, vieses conhecidos, considerações éticas.
- Declarar: avaliação automatizada é evidência parcial, não prova de conformidade.

---

## Exemplo preenchido: Descoberta Pública - Inexigibilidades publicadas no PNCP, v0.1.2

Fatos lidos no README público do repositório (github.com/viniburilux/descoberta-publica) em 9 nov 2026 e no histórico da iniciativa.

**A. Identificação**
- Nome: Inexigibilidades publicadas no PNCP, edição v0.1.2.
- Mantenedor: Vinícius Buri Lux (LuxVerso), iniciativa Descoberta Pública. Contato: `[LACUNA: canal de contato para reporte de erro não está declarado na ficha]`.
- Edição: v0.1.2 (novembro 2026). Cadência: `[LACUNA: sem cadência de atualização declarada; expansões em andamento (outros anos e modalidades) constam no histórico, sem compromisso de data]`.
- Licenças: código MIT; curadoria, documentação e derivados CC BY 4.0.
- Como citar: "Vinícius Buri Lux (LuxVerso), Descoberta Pública - Inexigibilidades publicadas no PNCP, v0.1.2". `[LACUNA: DOI (depósito no Zenodo) foi proposto e ainda não foi feito.]`

**B. Motivação**
- Tornar a informação pública brasileira usável: coletar, organizar, verificar e devolver em pacotes prontos, sem cadastro nem paywall.
- Criador: iniciativa independente de uma pessoa, sem financiamento declarado. `[LACUNA: confirmar se há qualquer apoio a declarar.]`
- Para quem: jornalismo de dados, pesquisa, ferramentas e produtos de transparência. Não é para quem precisa do valor pago: o dataset carrega valor estimado e homologado do registro público, não valor pago.

**C. Composição**
- 494.446 registros únicos das 27 UFs, modalidade inexigibilidade de licitação, publicados no PNCP entre 01/01/2025 e 06/11/2026.
- Lacuna conhecida declarada: o período de 22 a 31/08/2026 não está na base.
- O recorte é por data de publicação no portal, não pelo ano do ato; há compras de 2022 a 2026 entre os registros.
- Dimensão de municípios com população e PIB (IBGE) e receita (Siconfi) para cruzamento (junção por `cod_ibge`).
- Dados pessoais: presentes na fonte em texto livre; tratados conforme seção E. Valores visivelmente inconsistentes preservados como vieram da fonte.

**D. Processo de coleta**
- Fontes: API de dados abertos do PNCP (sem cadastro), IBGE, Siconfi/Tesouro Nacional.
- Integridade: 621 arquivos brutos com SHA256 conferido (100%); contagens por UF/ano verificadas após cada transformação; hashes da edição em `manifest_v012.json`.

**E. Tratamento e classificação**
- Mascaramento antes da publicação: CPF, RG, e-mail pessoal e endereço residencial escritos pelos órgãos no texto livre; nomes de famílias beneficiárias de programas sociais removidos. Nomes de fornecedores, órgãos e municípios mantidos como substância pública dos atos. Declarado como mascaramento, não anonimização; original preservado em privado.
- Classificação do objeto por categorias, com metodologia e validação abertas. `[LACUNA: a ficha deveria declarar se a classificação usou modelo de IA, qual, parâmetros e cobertura de revisão humana - informação não publicada no README.]`
- A classificação derivada é declarada material de exploração, não conclusão nem acusação.

**F. Usos**
- Demonstrados: consultas por UF, município, esfera, tema e ano com a ferramenta incluída (`consultar.py`, duckdb); leitura direta por qualquer leitor Parquet com partições Hive; produção de histórias jornalísticas pelo canal Quem Pagou Isso?.
- Desencorajado: tratar valores estimado/homologado como pagos; tratar classificação derivada como conclusão; ignorar `docs/LIMITACOES.md`.

**G. Distribuição**
- Repositório público no GitHub (release v0.1.2 com pacote completo; pacotes por UF em `dados/`). Licenças e atribuição conforme seção A.

**H. Manutenção**
- Mantenedor único. Versionamento por edições com manifesto de hashes. `[LACUNA: sem processo escrito de correção, de reporte de erro e de aposentadoria de versões.]`

**I. Modelo de IA**
- Não se aplica: não há modelo publicado. Se a classificação por categorias usar IA, a ficha do modelo/classificador passa a ser obrigatória nesta seção. `[LACUNA a resolver junto com a seção E.]`

**O que este exemplo mostra:** o dataset real já cobre bem integridade, limitações e dados pessoais, e a ficha expõe o que falta: contato/correção, cadência, DOI, declaração do método de classificação e dos papéis formais. Template preenchido com caso real mostra serviço; template vazio, não.
