# Agent notes

- Run tests with `bash scripts/run-tests.sh` (uv + pytest; `uv sync` first if `.venv` is missing). Pytest `pythonpath` covers `tools/` and the repo root.
- `tools/catalogue.yaml` lists the 41 source IDs; `require_complete: false` until the complete-catalogue slice. Pending patterns print in the terminal summary.
- `tests/unit/` must use synthetic `tmp_path` trees only; `tests/content/` reads real repo content read-only.
- The Dram schema/loader is not vendored here: read it from the CLI checkout at `/Volumes/Development/infracost/dram` (pinned `bdea6f6`, read-only; `internal/pack/schema.json`, `blocks.json`, `packs/`). Do not invent schema fields; `dram_pack_tools.schema` converts that schema's errors to diagnostics.
- Structural checks are never evaluation verdicts; keep that distinction in docs and output.
