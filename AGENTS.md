# Agent notes

- Run tests with `bash scripts/run-tests.sh` (uv + pytest; `uv sync` first if `.venv` is missing). Pytest `pythonpath` covers `tools/` and the repo root.
- `tools/catalogue.yaml` lists the 41 source IDs; `require_complete: false` until the complete-catalogue slice. Pending patterns print in the terminal summary.
- `tests/unit/` must use synthetic `tmp_path` trees only; `tests/content/` reads real repo content read-only.
- The Dram schema/loader is not vendored here: read it from the CLI checkout at `/Volumes/Development/infracost/dram` (pinned `bdea6f6`, read-only; `internal/pack/schema.json`, `blocks.json`, `packs/`). Do not invent schema fields; `dram_pack_tools.schema` converts that schema's errors to diagnostics.
- Structural checks are never evaluation verdicts; keep that distinction in docs and output.
- Build the pinned CLI for loader checks: `mkdir -p .tmp/gotmp && (cd /Volumes/Development/infracost/dram && GOTMPDIR=$OLDPWD/.tmp/gotmp TMPDIR=$OLDPWD/.tmp/gotmp go build -buildvcs=false -o $OLDPWD/.tmp/dram ./cmd/dram)`. `tests/content/test_cli_loader.py` skips without `.tmp/dram`; git on that checkout needs `git -c safe.directory='*'`.
- Pattern layout and rules: `core/reference/authoring.md`. Copy `core/patterns/give-it-instructions/` as the reference. Disabled patterns name no blocks; every case gets `unevaluable` and `packet: scenarios.md#<id>` unless a real fixture in the pinned shape can express it. Add the pattern to `core/groups.yaml` and flip its row in `core/reference/readiness.md`.
- Expected `.tmp/dram pack eval core`: exit 1 (red), all cases unevaluable. Never "fix" that by relabelling cases `none`.
- No tagged Dram release contains the pack loader, so `core/pack.yaml` has no `min_cli` (see `core/reference/compatibility.md`).
- All 41 patterns are authored (as of the second pattern-content batch); `.tmp/dram pack eval core` reports 605 unevaluable cases and no totals line, so sum the per-pattern counts. Mind the cache reuses the CLI's real `cache-rebuild` recommendation signal (`docs/recommendations.md` at `bdea6f6`) for cost wording only.
- `tests/content/test_pattern_batch_content.py` holds per-pattern required phrases (spec distinctions) for authored patterns; extend it when authoring new patterns. After adding patterns, update `core/groups.yaml`, readiness rows (case counts from `.tmp/dram pack eval core`) and the `compatibility.md` checks-run table.
