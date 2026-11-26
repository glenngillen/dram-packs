"""specs/README.md indexes every specification and only existing ones."""

from __future__ import annotations

import re

import pytest

from tests.content.paths import SPECS

pytestmark = pytest.mark.content

LINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")


def test_readme_links_every_spec_and_no_missing_file():
    readme = (SPECS / "README.md").read_text(encoding="utf-8")
    linked = set(LINK.findall(readme))
    specs = {p.name for p in SPECS.glob("*.md") if p.name != "README.md"}
    assert len(specs) == 50
    assert specs - linked == set(), "specs missing from the index"
    assert linked - specs == set(), "index links to files that do not exist"


def test_readme_has_no_checkout_paths_or_tracker_ids():
    readme = (SPECS / "README.md").read_text(encoding="utf-8")
    assert not re.search(r"/Users/|/Volumes/|\.worktrees|dram-packs-[a-z0-9]{3}\b", readme)
