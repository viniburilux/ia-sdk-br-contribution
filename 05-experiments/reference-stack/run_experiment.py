#!/usr/bin/env python3
"""Experimento 01 - stack de referencia minima do mapa IA SDK BR.

O que este script prova (e o que nao prova):
- PROVA a fiacao: gateway LiteLLM (endpoint OpenAI-compativel) recebe
  requisicoes, o avaliador aplica assercoes e a trilha local registra tudo.
- NAO PROVA qualidade de modelo: as respostas vem de mock_response,
  sem nenhum modelo de IA real atras do gateway (nenhuma chave usada).

Saidas:
- out/trace.jsonl  : trilha minima local (substituto do Langfuse nesta rodada)
- out/results.json : placar da mini-avaliacao (casos, assercoes, falhas)
"""
import datetime
import json
import os
import time
import urllib.request

BASE = "http://127.0.0.1:4100"
MODEL = "assistente-politica-ia"

CASES = [
    {
        "id": "c1-dado-nao-publico",
        "prompt": "Posso colar cadastro de clientes num assistente publico de IA?",
        "must_contain": ["LGPD", "aprovada"],
    },
    {
        "id": "c2-ferramenta-aprovada",
        "prompt": "O que e uma ferramenta de IA aprovada pela organizacao?",
        "must_contain": ["LGPD"],
    },
    {
        "id": "c3-falha-intencional",
        "prompt": "Cite o RIPD da ANPD na resposta.",
        # Falha intencional: o mock nao menciona RIPD. Serve para provar
        # que o avaliador realmente detecta assercao nao atendida.
        "must_contain": ["RIPD"],
    },
]


def chat(prompt: str) -> dict:
    key = os.environ["LITELLM_MASTER_KEY"]
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE}/chat/completions", data=body,
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {key}"},
        method="POST")
    started = time.monotonic()
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    return {"payload": payload, "latency_ms": round((time.monotonic() - started) * 1000)}


def main() -> None:
    trace, results = [], []
    for case in CASES:
        try:
            out = chat(case["prompt"])
            text = out["payload"]["choices"][0]["message"]["content"]
            missing = [w for w in case["must_contain"] if w.lower() not in text.lower()]
            passed = not missing
            record = {
                "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "case": case["id"], "model": MODEL, "latency_ms": out["latency_ms"],
                "prompt": case["prompt"], "response_excerpt": text[:160],
                "assertions": case["must_contain"], "missing": missing, "passed": passed,
            }
        except Exception as exc:  # falha de fiacao tambem e resultado
            record = {
                "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "case": case["id"], "model": MODEL, "prompt": case["prompt"],
                "error": f"{type(exc).__name__}: {exc}", "passed": False,
            }
        trace.append(record)
        results.append({"case": record["case"], "passed": record["passed"],
                        "missing": record.get("missing"), "error": record.get("error")})

    summary = {
        "experiment": "experimento-01-stack-referencia",
        "mode": "mock (sem modelo real, sem chaves)",
        "total": len(results),
        "passed": sum(1 for r in results if r["passed"]),
        "failed": sum(1 for r in results if not r["passed"]),
        "results": results,
    }
    with open("out/trace.jsonl", "w", encoding="utf-8") as fh:
        for row in trace:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open("out/results.json", "w", encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
