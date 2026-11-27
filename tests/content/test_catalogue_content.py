"""Structural checks over the real catalogue and pack tree.

These are content lint only. They never run a detector and their passing is
not an evaluation verdict for any pattern.
"""

from __future__ import annotations

import re

import pytest

from dram_pack_tools.catalogue import coverage, load_catalogue
from dram_pack_tools.references import find_executables, find_symlinks
from tests.content.paths import CATALOGUE, PACK, PATTERNS, SPECS

pytestmark = pytest.mark.content

EXPECTED_GROUPS = [
    ("Briefing", 4),
    ("Guides", 7),
    ("Context", 3),
    ("Checking the work", 11),
    ("Correcting course", 2),
    ("Delegation", 6),
    ("Economics", 4),
    ("Safety", 4),
]


@pytest.fixture(scope="module")
def catalogue():
    return load_catalogue(CATALOGUE)


def test_catalogue_has_41_ids_in_eight_ordered_groups(catalogue):
    assert [(g.name, len(g.patterns)) for g in catalogue.groups] == EXPECTED_GROUPS
    assert len(catalogue.ids) == len(set(catalogue.ids)) == 41


def test_every_catalogue_id_has_a_matching_spec(catalogue):
    for rung, pid in ((r, p) for g in catalogue.groups for r, p in enumerate(g.patterns, start=1)):
        spec = SPECS / f"{pid}.md"
        assert spec.is_file(), f"no spec for {pid}"
        overview = spec.read_text(encoding="utf-8")
        match = re.search(r"Source ID `([^`]+)`;(?: display name `[^`]+`;)? ([^,]+), rung (\d+)\.", overview)
        assert match, f"{spec.name} lacks a Source ID line"
        assert match.group(1) == pid
        assert match.group(2) == catalogue.group_of(pid)
        assert int(match.group(3)) == rung, f"{pid} rung order differs from the spec"


def test_every_pattern_spec_is_in_the_catalogue(catalogue):
    spec_ids = {p.stem for p in SPECS.glob("*.md") if "Source ID `" in p.read_text(encoding="utf-8")}
    assert spec_ids == set(catalogue.ids)


def test_catalogue_coverage_has_no_unknown_or_required_missing_patterns(catalogue):
    report = coverage(catalogue, PATTERNS)
    assert report.problems() == [], report.summary()


def test_packaged_tree_has_no_symlinks_or_executables():
    if not PACK.exists():
        pytest.skip("core/ pack tree not created yet (compatible-baseline slice pending)")
    assert find_symlinks(PACK) == []
    assert find_executables(PACK) == []
