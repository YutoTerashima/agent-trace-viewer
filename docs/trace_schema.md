# Trace Schema

Each step has `type`, `name`, `status`, and optional `latency_ms`. The viewer keeps
the schema intentionally small so traces from different agent frameworks can be
converted with a tiny adapter.
