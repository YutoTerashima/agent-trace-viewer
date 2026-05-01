import json
from pathlib import Path


def test_real_trace_dataset_has_policy_events():
    traces = json.loads(Path("datasets/external/real_prompt_injection_traces.json").read_text(encoding="utf-8"))
    assert len(traces) >= 50
    assert any(step["type"] == "tool_call" for trace in traces for step in trace["steps"])
    assert all(trace["source"] == "S-Labs/prompt-injection-dataset" for trace in traces)
