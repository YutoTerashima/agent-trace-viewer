# Agent Trace Viewer

A lightweight static HTML viewer for agent traces: messages, tool calls, handoffs,
errors, latency, and grader results.

## Quick Start

```bash
pip install -e ".[dev]"
python examples/render_trace.py
pytest
```

The demo writes `reports/trace_view.html`.
