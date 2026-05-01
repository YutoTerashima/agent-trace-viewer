import json
from pathlib import Path
from agent_trace_viewer.render import render_trace

traces = json.loads(Path("datasets/external/real_prompt_injection_traces.json").read_text(encoding="utf-8"))
html = "\n".join(render_trace(trace) for trace in traces[:5])
Path("reports/real_trace_dataset_preview.html").write_text(html, encoding="utf-8")
print("reports/real_trace_dataset_preview.html")
