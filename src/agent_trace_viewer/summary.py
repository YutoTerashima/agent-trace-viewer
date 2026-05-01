from __future__ import annotations

from collections import Counter


def summarize_trace(trace: dict) -> dict[str, object]:
    steps = trace.get("steps", [])
    statuses = Counter(step.get("status", "unknown") for step in steps)
    tool_steps = [step for step in steps if step.get("type") == "tool"]
    return {
        "case_id": trace.get("case_id", "trace"),
        "steps": len(steps),
        "tool_steps": len(tool_steps),
        "latency_ms": sum(int(step.get("latency_ms", 0)) for step in steps),
        "statuses": dict(sorted(statuses.items())),
    }
