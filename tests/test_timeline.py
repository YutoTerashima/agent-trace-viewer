from agent_trace_viewer.timeline import timeline


def test_timeline_accumulates_latency():
    rows = timeline({"steps": [{"latency_ms": 2}, {"latency_ms": 3}]})
    assert rows[-1]["elapsed_ms"] == 5
