from __future__ import annotations

import csv
from pathlib import Path

from .summary import summarize_trace


def export_summaries(traces: list[dict], path: Path) -> None:
    rows = [summarize_trace(trace) for trace in traces]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["case_id", "steps", "tool_steps", "latency_ms", "statuses"])
        writer.writeheader()
        writer.writerows(rows)
