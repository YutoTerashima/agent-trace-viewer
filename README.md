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

## Experiment Artifacts

- Sample metrics: [`reports/trace_viewer_sample_metrics.csv`](reports/trace_viewer_sample_metrics.csv)
- Rendered view: [`reports/trace_view.html`](reports/trace_view.html)
- Analysis: [`reports/trace_viewer_analysis.md`](reports/trace_viewer_analysis.md)

## Timeline Analysis

The viewer includes cumulative timeline helpers so trace review can connect
latency spikes to specific tool or grader steps.

## Full Trace Set

The repository includes 18 sample traces in
[`examples/full_trace_set.json`](examples/full_trace_set.json), with metrics in
[`reports/full_trace_viewer_report.md`](reports/full_trace_viewer_report.md).
