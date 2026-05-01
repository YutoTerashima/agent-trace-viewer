from agent_trace_viewer.summary import summarize_trace


def test_summarize_trace():
    summary = summarize_trace({"steps": [{"type": "tool", "status": "pass", "latency_ms": 5}]})
    assert summary["tool_steps"] == 1
    assert summary["latency_ms"] == 5
