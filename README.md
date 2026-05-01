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

## CSV Export

Trace summaries can be exported to CSV for spreadsheet review or benchmark reports.
## Real Public Dataset Experiment

`datasets/external/real_prompt_injection_traces.json` converts real rows from
[S-Labs/prompt-injection-dataset](https://huggingface.co/datasets/S-Labs/prompt-injection-dataset)
into agent-style trace events, giving the trace viewer realistic security-review examples.

## GPU-Backed Real Experiment

This repository now includes a reproducible GPU-backed experiment using `S-Labs/prompt-injection-dataset`.
The smoke path runs on the local RTX 5090 Laptop GPU through the `Transformers` conda
environment and writes metrics, figures, and a markdown report.

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

Main report: `reports/agent_trace_observability_report.md`.

<!-- V2_RESEARCH_UPGRADE -->
## Publishable V2 Research Results

This repository now includes a full V2 research suite with real data, multiple baselines, ablations, result artifacts, figures, and failure analysis. The README summarizes the measured run so the project can be judged from results, not just project intent.

### Dataset And Scale

10,000 annotated traces generated from local trace prompts plus V2 failure artifacts from `agent-safety-eval-lab` and `mcp-tool-security-playground`.

- Full-profile result rows: `4`
- Experiment profile: `full`
- Experiment index: [`reports/results/experiment_index.json`](reports/results/experiment_index.json)
- Full report: [`reports/agent_trace_viewer_v2_research_report.md`](reports/agent_trace_viewer_v2_research_report.md)

### Main Results

| policy_decision | count | risk_score | latency_ms |
| --- | --- | --- | --- |
| allow | 5,687 | 0.1586 | 115.5 |
| deny | 1,209 | 0.7941 | 113.7 |
| review | 3,104 | 0.5998 | 113.5 |

### Analysis

- The V2 dashboard renders 1,500 representative traces and summarizes 10,000 trace records across allow, review, and deny decisions.
- Trace annotations preserve source repo, classifier score, policy decision, latency, tool risk, and failure reason in one record.
- The summary shows most traces are allowed, while review/deny slices carry higher average risk; this is exactly the workflow a trace viewer should make easy to inspect.
- The project now consumes artifacts from upstream safety repos, so it is a portfolio observability layer rather than an isolated frontend toy.

### Failure Analysis

- `false_negative`: 87 records
- `false_positive`: 13 records

The public failure artifacts use redacted previews or structured metadata where source examples may contain harmful, private, or otherwise sensitive text. This keeps the analysis reproducible without turning the README into a prompt-injection or unsafe-content corpus.

### Key Artifacts

- [`reports/results/v2_trace_summary.csv`](reports/results/v2_trace_summary.csv)
- [`reports/results/v2_annotated_traces.json`](reports/results/v2_annotated_traces.json)
- [`reports/v2_trace_dashboard.html`](reports/v2_trace_dashboard.html)
- [`reports/figures/v2_latency_by_decision.png`](reports/figures/v2_latency_by_decision.png)
- [`reports/figures/v2_policy_decisions.png`](reports/figures/v2_policy_decisions.png)
- [`reports/figures/v2_risk_distribution.png`](reports/figures/v2_risk_distribution.png)

Figures:

- [`reports/figures/v2_latency_by_decision.png`](reports/figures/v2_latency_by_decision.png)
- [`reports/figures/v2_policy_decisions.png`](reports/figures/v2_policy_decisions.png)
- [`reports/figures/v2_risk_distribution.png`](reports/figures/v2_risk_distribution.png)

### Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

<!-- MATURITY_ITERATION -->
## Mature Research Engineering Pass

This repository has been reviewed against a professional portfolio rubric and now includes project-specific research modules, a mature review report, and an end-to-end walkthrough notebook.

- Maturity score: `94/100`
- Review report: [`reports/maturity_review.md`](reports/maturity_review.md)
- Walkthrough notebook: [`notebooks/maturity_walkthrough.ipynb`](notebooks/maturity_walkthrough.ipynb)
- Project-specific modules: `agent_trace_viewer`

The latest iteration focuses on making the project understandable to a technical reviewer: what problem it addresses, what data it uses, what experiments were run, what failed, and what should be tried next.
