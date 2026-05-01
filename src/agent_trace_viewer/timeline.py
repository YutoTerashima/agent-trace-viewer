from __future__ import annotations


def timeline(trace: dict) -> list[dict[str, object]]:
    elapsed = 0
    rows = []
    for i, step in enumerate(trace.get("steps", []), start=1):
        latency = int(step.get("latency_ms", 0))
        elapsed += latency
        rows.append({**step, "index": i, "elapsed_ms": elapsed})
    return rows
