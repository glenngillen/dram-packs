"""The pinned Dram CLI itself loads, shows and evaluates the pack.

Runs the CLI built from the pinned checkout at ``.tmp/dram`` (see
reference/compatibility.md for the build command); skipped, with the reason,
when it has not been built. A red ``pack eval`` verdict is the expected,
honest result for disabled content: every case is unevaluable and none is
counted as a pass.
"""

from __future__ import annotations

import json
import subprocess

import pytest

from dram_pack_tools.catalogue import coverage, load_catalogue
from dram_pack_tools.readers import load_jsonl
from tests.content.paths import CATALOGUE, PATTERNS, REPO

pytestmark = pytest.mark.content

DRAM = REPO / ".tmp" / "dram"


def run(*args):
    if not DRAM.is_file():
        pytest.skip(f"pinned CLI not built at {DRAM}; loader checks not run")
    return subprocess.run([str(DRAM), *args], cwd=REPO, capture_output=True, text=True, timeout=120)


@pytest.fixture(scope="module")
def authored():
    return coverage(load_catalogue(CATALOGUE), PATTERNS).authored


def test_cli_validates_the_index_and_pack(authored):
    out = run("pack", "validate", ".")
    assert out.returncode == 0, out.stderr
    assert "1 pack offered" in out.stdout
    assert f"glenngillen/core                  0.1.0  {len(authored)} pattern" in out.stdout


def test_cli_shows_every_pattern_disabled_with_no_blocks(authored):
    out = run("pack", "show", "--dir", "core", "--json")
    assert out.returncode == 0, out.stderr
    [pack] = json.loads(out.stdout)
    assert pack["id"] == "glenngillen/core"
    shown = {p["id"]: p for p in pack["patterns"]}
    assert sorted(shown) == sorted(f"glenngillen/{p}" for p in authored)
    for p in shown.values():
        assert p["enabled"] is False and p["status"] == "preview" and p["blocks"] == []


def test_cli_eval_judges_nothing_and_stays_red(authored):
    out = run("pack", "eval", "core", "--json")
    report = json.loads(out.stdout)
    total = sum(len(load_jsonl(PATTERNS / p / "eval" / "cases.jsonl")) for p in authored)
    assert out.returncode == 1
    assert (report["passed"], report["failed"], report["errors"]) == (0, 0, 0)
    assert report["unevaluable"] == total
    assert sorted(report["unheld"]) == sorted(f"glenngillen/{p}" for p in authored)
