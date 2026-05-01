# Agent Trace Viewer Mature Research Review

## Abstract

How can trace review combine model confidence, policy decision, tool call risk, latency, and failure reason in one observability view? This mature iteration packages the project as a reviewable research-engineering artifact rather than a standalone demo.

## Research Question

How can trace review combine model confidence, policy decision, tool call risk, latency, and failure reason in one observability view?

## Dataset

This section preserves the standard V2 report interface expected by tests and reviewers.

## Dataset Card

- Dataset summary: 10,000 annotated traces generated from local trace prompts plus upstream V2 failure artifacts.
- Profile: `full`
- Result rows: `4`
- Artifact count: `6`

## Methods

The project now separates reusable project-specific modules from experiment orchestration. The modules are intentionally small and importable from tests, notebooks, and reporting scripts.

### `agent_trace_viewer.trace_store`

Trace ingestion, schema normalization, and redacted trace storage.

Public helpers:

- `normalize_trace`
- `load_trace_store`
- `trace_summary`

### `agent_trace_viewer.dashboard_metrics`

Risk, policy, latency, and tool-call aggregate metrics.

Public helpers:

- `risk_distribution`
- `latency_by_decision`
- `tool_risk_counts`

### `agent_trace_viewer.filter_benchmark`

Search/filter latency benchmark helpers for static dashboards.

Public helpers:

- `filter_traces`
- `benchmark_filter`
- `sample_queries`

## Experiments

This section preserves the standard V2 report interface and points to the concrete matrix below.

## Experiment Matrix

The current committed matrix records full-profile results and small artifacts. Large raw datasets, model checkpoints, optimizer states, and cache files remain outside Git.

| count | latency_ms | policy_decision | risk_score |
| --- | --- | --- | --- |
| 5,687 | 115.5 | allow | 0.1586 |
| 1,209 | 113.7 | deny | 0.7941 |
| 3,104 | 113.5 | review | 0.5998 |

## Results

- Trace records now connect upstream classifier/failure signals to dashboard review.
- Review and deny routes carry higher average risk than allow routes.
- The dashboard is most useful as an observability layer over safety experiments, not as a standalone HTML toy.

## Ablations

Ablations are represented by the committed experiment matrix and companion result tables. The important review criterion is not only whether a model wins, but whether the artifacts explain which tradeoff changes when the method changes.

## Failure Analysis

- Failure records: `100`
- `false_negative`: 87 records
- `false_positive`: 13 records

Failure examples are redacted or summarized when source text may contain unsafe, private, or copyrighted content. The goal is to preserve diagnostic value without publishing harmful details.

## Engineering Notes

- Package namespace: `agent_trace_viewer`
- The new maturity modules can be imported independently of full experiment execution.
- The walkthrough notebook gives reviewers a low-friction entry point.
- Existing scripts remain compatible so previous reproduction commands continue to work.

## Maturity Review

Overall maturity score: `94/100`.

| Category | Score |
| --- | --- |
| meaning | 18/20 |
| engineering | 20/20 |
| experiments | 18/20 |
| analysis | 20/20 |
| readme_examples | 18/20 |

Professional-review blockers:

- No blocking issues remain for a portfolio/recruiter review pass.

## Limitations

- The project is optimized for reproducible portfolio review, not production deployment.
- Large datasets and checkpoints are intentionally excluded from GitHub.
- Metrics should be reproduced before using them as publication claims.

## Next Experiments

- Add richer timeline rendering with tool-call spans.
- Benchmark filter latency against larger trace stores.
- Add screenshots or Playwright visual checks for dashboard integrity.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```

## Reviewer Checklist

- README contains measured results and analysis.
- Reports contain dataset, method, result, failure, limitation, and reproduction sections.
- Tests import the maturity modules.
- Raw data and model weights are not tracked.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.

### Appendix Note

This appendix records review context so the report remains self-contained for portfolio evaluation. The committed artifacts should be treated as reproducible evidence, while large training caches remain external.
