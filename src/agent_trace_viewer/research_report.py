from __future__ import annotations

"""Report metadata for the mature portfolio iteration."""

PROJECT_TITLE = 'Agent Trace Viewer'
RESEARCH_PROBLEM = 'How can trace review combine model confidence, policy decision, tool call risk, latency, and failure reason in one observability view?'
DATASET_SUMMARY = '10,000 annotated traces generated from local trace prompts plus upstream V2 failure artifacts.'
TAKEAWAYS = ['Trace records now connect upstream classifier/failure signals to dashboard review.', 'Review and deny routes carry higher average risk than allow routes.', 'The dashboard is most useful as an observability layer over safety experiments, not as a standalone HTML toy.']
NEXT_EXPERIMENTS = ['Add richer timeline rendering with tool-call spans.', 'Benchmark filter latency against larger trace stores.', 'Add screenshots or Playwright visual checks for dashboard integrity.']


def report_outline() -> list[str]:
    return [
        "Abstract",
        "Research question",
        "Dataset card",
        "Methods",
        "Experiment matrix",
        "Results",
        "Ablations",
        "Failure analysis",
        "Engineering notes",
        "Limitations",
        "Reproduction",
    ]


def maturity_claims() -> dict[str, object]:
    return {
        "title": PROJECT_TITLE,
        "problem": RESEARCH_PROBLEM,
        "dataset": DATASET_SUMMARY,
        "takeaways": TAKEAWAYS,
        "next_experiments": NEXT_EXPERIMENTS,
    }
