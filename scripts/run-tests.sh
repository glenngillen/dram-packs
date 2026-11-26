#!/usr/bin/env bash
# Repository test runner: unit tests plus read-only structural content checks.
# Structural checks are not detector evaluations; see specs/README.md.
set -euo pipefail
cd "$(dirname "$0")/.."
exec uv run --frozen pytest "$@"
