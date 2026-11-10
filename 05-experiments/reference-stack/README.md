# Experimento 01 - Stack de referência mínima

**Status: registrado (9 nov 2026), modo mock - sem modelo real, sem chaves de API.**

Primeira tentativa de ligar três camadas do mapa na prática: **gateway** (LiteLLM), **avaliação** (mini-harness com asserções em PT-BR) e **trilha** (trace local em JSONL, substituto do Langfuse nesta rodada).

## O que este experimento prova (e o que não prova)

- **Prova a fiação:** um gateway LiteLLM real (endpoint OpenAI-compatível) sobe, recebe requisições autenticadas, o avaliador aplica asserções e detecta tanto acertos quanto falhas, e a trilha registra cada caso com latência.
- **Não prova qualidade de modelo:** as respostas vêm de `mock_response`, sem nenhum modelo de IA real. Validar com modelo de verdade exige chave de API e é o próximo passo.
- **Não é integração com o Descoberta Pública:** nenhum componente foi ligado ao dataset; essa integração é outro experimento.

## Como rodar

```bash
pip install 'litellm[proxy]'
export LITELLM_MASTER_KEY="sk-$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')"
litellm --config proxy-config.yaml --port 4100 &
python3 run_experiment.py   # escreve out/results.json e out/trace.jsonl
```

A chave é gerada localmente para cada execução e não deve ser publicada.

## Arquivos

- `proxy-config.yaml` - configuração mínima do gateway (modelo mockado).
- `run_experiment.py` - dispara 3 casos de teste PT-BR contra o gateway, aplica asserções, grava trilha e placar.
- `out/results.json`, `out/trace.jsonl` - saídas da execução registrada.
- `REGISTRO.md` - o que rodou, o que quebrou e o que falta (leia este primeiro).
