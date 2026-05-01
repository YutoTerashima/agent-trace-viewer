# Agent Trace Observability Report

Trace dashboard generated from real prompt-injection classifier outputs.

## Dataset

- Source: `S-Labs/prompt-injection-dataset`
- Config: `default`
- Split: `train`

## Reproducibility

```powershell
conda run -n Transformers python scripts/download_data.py --smoke
conda run -n Transformers python scripts/preprocess_data.py --max-samples 384
conda run -n Transformers python scripts/run_experiment.py --device cuda --smoke
conda run -n Transformers python scripts/make_report.py
```

## Generated Artifacts

- Result JSON: `results/trace_summary.json`
- Result CSV: `results/trace_metrics.csv`
- Figure: `figures/trace_policy_decisions.png`

## Result Snapshot

```json
{
  "device": {
    "requested_device": "cuda",
    "actual_device": "cuda",
    "cuda_available": true,
    "gpu_name": "NVIDIA GeForce RTX 5090 Laptop GPU",
    "torch_version": "2.10.0+cu128",
    "cuda_runtime": "12.8"
  },
  "traces": 5000,
  "policy_counts": {
    "allow": 4196,
    "review": 804
  }
}
```

## Failure Analysis

The experiment stores model disagreements, retrieval misses, or policy-risk examples in the result JSON/CSV files when available. These examples are intentionally kept as previews or structured metadata where the source data can contain unsafe or sensitive text.

## Limitations

- Smoke mode prioritizes reproducibility and runtime over leaderboard-scale performance.
- Raw datasets are downloaded to `data/raw/` and are not committed.
- Metrics should be interpreted as portfolio research baselines, not production claims.
