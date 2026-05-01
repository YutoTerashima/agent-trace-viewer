# Agent Trace Viewer V2 Research Report

## Abstract

This V2 upgrade turns the repository into a reproducible project-level experiment suite. The run records the dataset, device, experiment matrix, metrics, figures, failure analysis, and reproduction commands in committed small artifacts.

## Dataset

- Source path: `data/raw/raw_dataset.jsonl`
- Profile: `full`
- Runtime: `0.656` seconds
- Device: `cuda` / `NVIDIA GeForce RTX 5090 Laptop GPU`

## Methods

Experiments declared in `configs/experiment_matrix.yaml`:

- `trace_risk_scoring`: `risk`
- `policy_timeline_latency`: `latency`
- `filter_benchmark`: `filter`
- `dashboard_export`: `dashboard`

## Experiments

The matrix produced `4` result rows. 

## Results

Key artifacts:

- `reports\results\v2_trace_summary.csv`
- `reports\results\v2_annotated_traces.json`
- `reports\v2_trace_dashboard.html`
- `reports\figures\v2_latency_by_decision.png`
- `reports\figures\v2_policy_decisions.png`
- `reports\figures\v2_risk_distribution.png`

## Ablations

Configured ablations: confidence_threshold, tool_risk, latency_bucket, policy_decision. The generated ablation files quantify threshold, perturbation, architecture, retrieval, or metric sensitivity depending on the project.

## Failure Analysis

Failure records: `100`.

Top clusters:

- `false_negative`: 87
- `false_positive`: 13

## Discussion

Trace observability is useful only when the viewer carries model confidence, policy decisions, and failure reasons into the same timeline. V2 creates thousands of annotated traces and measures dashboard/filter behavior.

## Limitations

- Full raw caches, model weights, and optimizer states are intentionally excluded from GitHub.
- Results are designed for reproducible portfolio research; they are not production safety, medical, or compliance guarantees.
- Some V2 experiments use compact local artifacts to keep the repository lightweight.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
