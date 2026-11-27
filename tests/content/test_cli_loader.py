"""The pinned Dram CLI itself loads, shows and evaluates the pack.

Runs the CLI built from the pinned checkout at ``.tmp/dram`` (see
reference/compatibility.md for the build command); skipped, with the reason,
when it has not been built. A red ``pack eval`` verdict is the expected,
honest result for disabled content: every case is unevaluable and none is
counted as a pass.
"""

from __future__ import annotations

import json
import shutil
import subprocess

import pytest

from dram_pack_tools.catalogue import coverage, load_catalogue
from dram_pack_tools.readers import load_jsonl
from tests.content.paths import CATALOGUE, PACK, PATTERNS, REPO

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


BUILT_IN = ["infracost/iac", "infracost/recommend"]


@pytest.fixture
def installed_state(tmp_path):
    """A throwaway state directory holding the pack as `dram pack install` lays it out.

    No network fetch happens: the tree is copied to ``<state>/packs/<id>`` and
    recorded in ``packs.json``, the two things the pinned ``registry.Dirs``
    reads. Repo, ref, sha and digest are synthetic and unchecked for installs.
    """
    state = tmp_path / "state"
    shutil.copytree(PACK, state / "packs" / "glenngillen" / "core")
    record = {"id": "glenngillen/core", "repo": "local/test", "ref": "test", "sha": "0" * 40, "digest": "test", "version": "0.1.0", "installed": "2026-11-27T00:00:00Z"}
    (state / "packs.json").write_text(json.dumps({"registries": [], "installed": [record]}))
    return state


def _show(state, *extra):
    out = run("--state-dir", str(state), "pack", "show", "--json", "--blocks", *extra)
    assert out.returncode == 0, out.stderr
    return {p["id"]: p for p in json.loads(out.stdout)}


def test_cli_loads_the_pack_beside_the_built_in_packs(installed_state):
    out = run("--state-dir", str(installed_state), "pack", "list", "--json")
    assert out.returncode == 0, out.stderr
    assert sorted(p["id"] for p in json.loads(out.stdout)) == sorted(["glenngillen/core", *BUILT_IN])
    packs = _show(installed_state)
    assert sorted(packs) == sorted(["glenngillen/core", *BUILT_IN])
    pattern_ids = [q["id"] for p in packs.values() for q in p["patterns"]]
    assert len(pattern_ids) == len(set(pattern_ids)), "fully qualified pattern IDs collide"
    assert {"glenngillen/right-size-it", "infracost/right-size-it"} <= set(pattern_ids)
    assert len(packs["glenngillen/core"]["patterns"]) == 41


def test_loading_the_pack_leaves_built_in_packs_unchanged(installed_state, tmp_path):
    empty = tmp_path / "empty-state"
    empty.mkdir()
    alone = _show(empty)
    beside = _show(installed_state)
    assert sorted(alone) == BUILT_IN
    for pid in BUILT_IN:
        assert beside[pid] == alone[pid], f"{pid} changed when glenngillen/core was loaded"
