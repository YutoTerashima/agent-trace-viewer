from pathlib import Path

from agent_trace_viewer.render import render_trace


trace = {
    "case_id": "demo-agent-trace",
    "steps": [
        {"type": "message", "name": "user", "status": "received", "latency_ms": 0},
        {"type": "tool", "name": "search.docs", "status": "allowed", "latency_ms": 14},
        {"type": "grader", "name": "tool-policy", "status": "pass", "latency_ms": 1},
    ],
}

if __name__ == "__main__":
    out = Path("reports/trace_view.html")
    out.parent.mkdir(exist_ok=True)
    out.write_text(render_trace(trace), encoding="utf-8")
    print(out)
