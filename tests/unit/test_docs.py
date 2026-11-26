"""Markdown link, anchor, placeholder and parameter-table helpers."""

from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis import strategies as st

from dram_pack_tools.diagnostics import PackContentError
from dram_pack_tools.docs import (
    check_links,
    heading_slugs,
    markdown_links,
    parameter_links,
    parse_parameter_table,
    placeholders,
    slugify,
)
from tests.helpers.tree import write_tree


def test_markdown_links_skip_code_and_external_targets():
    text = "See [a](a.md) and [b](https://x.io).\n\n```\n[c](c.md)\n```\n\nInline `[d](d.md)` and [e](#top).\n"
    assert [t for t, _ in markdown_links(text)] == ["a.md", "#top"]


def test_slugify_matches_github_style():
    assert slugify("Stage-dependent completion") == "stage-dependent-completion"
    assert slugify("`cache_gap`") == "cache_gap"
    assert slugify("Gate \"done\" & friends!") == "gate-done--friends"


def test_heading_slugs_number_repeats():
    assert heading_slugs("# A\n## A\n```\n# B\n```\n") == {"a", "a-1"}


def test_check_links_reports_missing_escaping_and_bad_anchor(tmp_path):
    write_tree(
        tmp_path,
        {
            "pack/ref/a.md": "# Title\n\n[ok](b.md#section) [self](#title) [gone](c.md) [out](../../x.md) [bad](b.md#nope)\n",
            "pack/ref/b.md": "# B\n\n## Section\n",
            "x.md": "# X\n",
        },
    )
    diags = check_links(tmp_path / "pack/ref/a.md", tmp_path / "pack")
    assert [d.code for d in diags] == ["link-missing", "link-escapes", "link-anchor"]


TABLE = """# Parameters

| Parameter | Default | Origin | Used by |
| --- | --- | --- | --- |
| `cache_gap` | More than 1 hour | Source example | Mind the cache |
| `most` | At least 60% | Approved proposal | Several |
"""


def test_parse_parameter_table():
    rows = parse_parameter_table(TABLE, "p.md")
    assert list(rows) == ["cache_gap", "most"]
    assert rows["most"].default == "At least 60%"
    assert rows["cache_gap"].origin == "Source example"


def test_parse_parameter_table_rejects_duplicates():
    with pytest.raises(PackContentError) as err:
        parse_parameter_table(TABLE + "| `most` | x | y | z |\n", "p.md")
    assert err.value.diagnostics[0].code == "parameter-duplicate"


def test_parameter_links_read_names_from_links_to_the_parameter_reference():
    text = "Uses [`most`](../../reference/parameters.md#most) and [`x`](other.md#x) and [`kept_window`](parameters.md#kept_window)."
    assert parameter_links(text) == [("most", "most"), ("kept_window", "kept_window")]


def test_placeholders():
    assert placeholders("In {cases} of {applicable}; {{literal}}") == ["cases", "applicable"]


class TestProperties:
    @given(st.text())
    def test_slugify_output_is_anchor_safe_and_idempotent(self, text):
        slug = slugify(text)
        assert all(c.isalnum() or c in "-_" for c in slug)
        assert slug == slug.lower()
        assert slugify(slug) == slug

    @given(st.text())
    def test_markdown_links_never_crash_and_return_known_lines(self, text):
        lines = text.count("\n") + 1
        for target, line in markdown_links(text):
            assert target
            assert 1 <= line <= lines

    @given(st.text())
    def test_placeholders_are_found_inside_single_braces(self, text):
        for name in placeholders(text):
            assert "{" + name + "}" in text
