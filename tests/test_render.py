from agent_trace_viewer.render import render_trace


def test_render_contains_steps():
    html = render_trace({"case_id": "x", "steps": [{"type": "tool", "name": "search", "status": "pass"}]})
    assert "search" in html
    assert "<table>" in html
