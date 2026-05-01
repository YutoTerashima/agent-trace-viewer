from agent_trace_viewer.export import export_summaries


def test_export_summaries(tmp_path):
    out = tmp_path / "summary.csv"
    export_summaries([{"case_id": "x", "steps": []}], out)
    assert out.read_text(encoding="utf-8").startswith("case_id")
