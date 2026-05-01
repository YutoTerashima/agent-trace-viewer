from __future__ import annotations

import html


def render_trace(trace: dict) -> str:
    title = html.escape(trace.get("case_id", "trace"))
    rows = []
    for step in trace.get("steps", []):
        rows.append(
            "<tr>"
            f"<td>{html.escape(step.get('type', ''))}</td>"
            f"<td>{html.escape(step.get('name', ''))}</td>"
            f"<td>{html.escape(step.get('status', ''))}</td>"
            f"<td>{html.escape(str(step.get('latency_ms', '')))}</td>"
            "</tr>"
        )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>body{{font-family:system-ui;margin:2rem}}table{{border-collapse:collapse}}td,th{{border:1px solid #ddd;padding:.5rem}}</style>
</head><body><h1>{title}</h1><table><tr><th>Type</th><th>Name</th><th>Status</th><th>Latency</th></tr>{''.join(rows)}</table></body></html>"""
