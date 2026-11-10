# Registro de execução - Experimento 01 (9 nov 2026)

## Hipótese

As camadas gateway + avaliação + trilha do mapa se ligam com componentes abertos em uma tarde, sem escrever software novo.

## Ambiente

- Máquina Linux sandbox, Python 3, sem chaves de API de modelo.
- LiteLLM 1.108.4 (`pip install 'litellm[proxy]'`).

## O que aconteceu, em ordem

1. **Quebra 1 - proxy não subiu:** `ImportError: No module named 'backoff'`. O pacote base `litellm` não inclui as dependências do proxy; corrigido instalando o extra `litellm[proxy]`.
2. **Quebra 2 - proxy recusou iniciar:** `UnsafeMasterKeyError` - o gateway exige `LITELLM_MASTER_KEY` para não aceitar requisições sem autenticação. Corrigido exportando a variável e enviando `Authorization: Bearer` nas chamadas. (Comportamento correto do componente, vale documentar no perfil de referência.)
3. **Rodou:** proxy no ar em ~6s. Três casos PT-BR disparados contra `http://127.0.0.1:4100/chat/completions`.

## Resultado

| Caso | Asserções | Resultado |
|---|---|---|
| c1-dado-nao-publico | resposta contém "LGPD" e "aprovada" | passou (109 ms) |
| c2-ferramenta-aprovada | resposta contém "LGPD" | passou (10 ms) |
| c3-falha-intencional | resposta contém "RIPD" (o mock não menciona) | **falhou como esperado** - prova que o avaliador detecta asserção não atendida |

Placar: 2/3 passando, 1 falha intencional detectada. Evidência: `out/results.json` e `out/trace.jsonl` (trilha com timestamp, latência, prompt, trecho da resposta e asserções por caso).

## O que ficou de fora (honestamente)

- **Nenhum modelo real:** respostas são `mock_response` estático. O teste é de fiação, não de qualidade.
- **Langfuse não executado:** requer servidor/docker próprio; a trilha local em JSONL é o substituto honesto desta rodada, não um equivalente.
- **Promptfoo/DeepEval não executados:** o avaliador é um script mínimo, não o componente do mapa.
- **Nenhuma integração com o Descoberta Pública:** não houve tentativa; afirmar o contrário seria overclaim.

## Próximos passos deste experimento

1. Rodar com um modelo real atrás do gateway (exige chave; candidato: provedor gratuito ou modelo nacional, a decidir).
2. Trocar o script mínimo por Promptfoo apontado para o gateway, com bateria PT-BR inicial.
3. Adicionar Langfuse self-hosted e ligar a trilha do gateway nele.
4. Só então: aplicar a stack a um caso real (candidate: assistente que responde sobre a política de IA do kit).
