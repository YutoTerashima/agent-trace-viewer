# Research Brief

## Problem

Agent evaluation reports are hard to debug when traces are stored as raw JSON. Reviewers
need to scan message flow, tool calls, policy status, and latency quickly.

## Method

This project renders a compact static HTML table from a normalized trace schema.

## Depth Signal

The viewer is intentionally static so it can be attached to benchmark reports, CI
artifacts, or GitHub Pages without a backend.

## Next Experiments

- Add collapsible message payloads.
- Add risk color coding.
- Add multi-trace comparison.
