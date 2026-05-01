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

## Research Brief

See [`docs/research_brief.md`](docs/research_brief.md) for the trace-review
motivation, schema choices, and next experiments.

## Portfolio Notes

This project adds a visual systems layer for agent evaluation reports.
