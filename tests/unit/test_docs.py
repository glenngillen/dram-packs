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


def test_heading_slugs_skip_suffixes_already_taken():
    # The third heading cannot reuse "a-1"; GitHub gives it "a-2".
    assert heading_slugs("# A\n# A-1\n# A\n") == {"a", "a-1", "a-2"}


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

    # Synthetic generators for the parser/transformer properties below.
    param_name = st.from_regex(r"[a-z0-9_]{1,12}", fullmatch=True)
    cell = st.from_regex(r"[A-Za-z0-9%.,]([A-Za-z0-9%., ]{0,10}[A-Za-z0-9%.,])?", fullmatch=True)
    row = st.tuples(cell, cell, cell, cell)
    heading_text = st.from_regex(r"[A-Za-z0-9]([A-Za-z0-9 _-]{0,15}[A-Za-z0-9])?", fullmatch=True)
    anchor = st.from_regex(r"[a-z0-9_-]{1,12}", fullmatch=True)
    param_path = st.sampled_from(["parameters.md", "../reference/parameters.md", "../../reference/parameters.md"])

    @given(st.dictionaries(param_name, row, min_size=1, max_size=8))
    def test_parameter_table_preserves_names_values_and_order(self, table):
        lines = ["| Parameter | Default | Origin | Used by | Status |", "| --- | --- | --- | --- | --- |"]
        lines += [f"| `{n}` | {d} | {o} | {u} | {s} |" for n, (d, o, u, s) in table.items()]
        rows = parse_parameter_table("\n".join(lines) + "\n", "p.md")
        assert list(rows) == list(table)
        for n, (d, o, u, s) in table.items():
            assert (rows[n].name, rows[n].default, rows[n].origin, rows[n].used_by, rows[n].status) == (n, d, o, u, s)

    @given(st.lists(param_name, min_size=1, max_size=6), st.data())
    def test_parameter_table_rejects_any_repeated_name(self, names, data):
        dup = data.draw(st.sampled_from(names))
        lines = [f"| `{n}` | a | b | c |" for n in names + [dup]]
        with pytest.raises(PackContentError) as err:
            parse_parameter_table("\n".join(lines) + "\n", "p.md")
        assert err.value.diagnostics[0].code == "parameter-duplicate"

    @given(heading_text, st.integers(min_value=1, max_value=8), st.integers(min_value=1, max_value=6))
    def test_repeated_identical_headings_get_distinct_anchors(self, title, repeats, level):
        text = "\n\n".join("#" * level + " " + title for _ in range(repeats)) + "\n"
        slugs = heading_slugs(text)
        assert len(slugs) == repeats
        assert slugify(title) in slugs

    @given(st.lists(st.tuples(heading_text, st.integers(min_value=0, max_value=3)), min_size=1, max_size=8))
    def test_every_heading_gets_its_own_anchor_even_with_suffix_collisions(self, specs):
        # Headings that already end in "-N" collide with generated suffixes;
        # every heading must still receive a distinct anchor.
        titles = [t if n == 0 else f"{t}-{n}" for t, n in specs]
        text = "\n\n".join("# " + t for t in titles) + "\n"
        slugs = heading_slugs(text)
        assert len(slugs) == len(titles)
        assert {slugify(t) for t in titles} <= slugs

    @given(st.lists(st.tuples(param_name, anchor, param_path), max_size=6))
    def test_parameter_links_preserve_names_anchors_and_order(self, links):
        text = " and ".join(f"[`{n}`]({p}#{a})" for n, a, p in links)
        assert parameter_links(f"Uses {text}.") == [(n, a) for n, a, _ in links]
