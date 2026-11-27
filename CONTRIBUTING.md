# Contributing

This repository contains declarative Dram pack content and local authoring tools. It has no CLI application, no executable detectors and no deployment workflow. See [specs/README.md](specs/README.md) for the architecture and the boundary between pack content and Dram CLI capabilities.

## Local environment

Requires [uv](https://docs.astral.sh/uv/) and Python 3.11 or later. Dependencies are pinned in `uv.lock`.

```sh
uv sync                    # create .venv with PyYAML, jsonschema, pytest, hypothesis
bash scripts/run-tests.sh  # unit tests + read-only structural content checks
```

`scripts/run-tests.sh` passes extra arguments to pytest, for example `bash scripts/run-tests.sh tests/unit -q`.

## What the checks mean

- `tests/unit/` exercises the tools in `tools/dram_pack_tools/` against synthetic temporary files only.
- `tests/content/` reads this repository's real content and checks structure: the catalogue, spec index, references and tree hygiene.
- The run ends with an authoring-coverage line listing every pattern that is still pending. Coverage and structural passes are **not** detector evaluations; no local check here reports whether a pattern is recognized in real work.

## Content rules

- Keep tooling outside `core/`. Packaged trees may not contain symlinks or executable files.
- Fixtures must be invented, deterministic data. Never commit real session histories, personal configuration or credentials.
- Do not invent Dram schema fields or blocks. Preserve unsupported behaviour in prose and keep the pattern disabled.
