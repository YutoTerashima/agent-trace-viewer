# Trace Viewer Analysis

The viewer is useful when traces differ in length, tool count, latency, and risk.

| trace_id | steps | tools | latency_ms | risk |
| --- | --- | --- | --- | --- |
| T001 | 3 | 1 | 15 | pass |
| T002 | 6 | 3 | 88 | needs_review |
| T003 | 5 | 2 | 42 | tool_policy_violation |

## Interpretation

Higher tool count and latency are not automatically bad, but they create review
pressure. The viewer helps reviewers inspect the trajectory behind the score.
