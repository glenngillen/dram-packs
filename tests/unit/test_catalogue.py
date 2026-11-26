"""Catalogue loading and incremental coverage tracking (synthetic catalogues)."""

from __future__ import annotations

import pytest
from hypothesis import given
from hypothesis import strategies as st

from dram_pack_tools.catalogue import Catalogue, coverage, load_catalogue, parse_catalogue
from dram_pack_tools.diagnostics import PackContentError
from tests.helpers.tree import write_tree

SMALL = {
    "require_complete": False,
    "groups": [
        {"name": "Alpha", "patterns": ["one", "two"]},
        {"name": "Beta", "patterns": ["three"]},
    ],
}


def cat(**overrides) -> Catalogue:
    return parse_catalogue({**SMALL, **overrides}, "catalogue.yaml")


class TestParseCatalogue:
    def test_given_groups_when_parsed_then_ids_keep_order(self):
        c = cat()
        assert c.ids == ("one", "two", "three")
        assert [g.name for g in c.groups] == ["Alpha", "Beta"]
        assert c.group_of("three") == "Beta"
        assert c.require_complete is False

    def test_given_duplicate_id_across_groups_when_parsed_then_rejected(self):
        with pytest.raises(PackContentError) as exc:
            cat(groups=[{"name": "A", "patterns": ["x"]}, {"name": "B", "patterns": ["x"]}])
        assert [d.code for d in exc.value.diagnostics] == ["catalogue-duplicate-id"]

    def test_given_duplicate_group_when_parsed_then_rejected(self):
        with pytest.raises(PackContentError) as exc:
            cat(groups=[{"name": "A", "patterns": ["x"]}, {"name": "A", "patterns": ["y"]}])
        assert [d.code for d in exc.value.diagnostics] == ["catalogue-duplicate-group"]

    @pytest.mark.parametrize("bad", ["Upper", "has space", "-lead", "trail-", "a--b", "", "a/b", "x\n"])
    def test_given_non_kebab_id_when_parsed_then_rejected(self, bad):
        with pytest.raises(PackContentError) as exc:
            cat(groups=[{"name": "A", "patterns": [bad]}])
        assert [d.code for d in exc.value.diagnostics] == ["catalogue-invalid-id"]

    @pytest.mark.parametrize(
        "data",
        [
            {"groups": []},
            {"require_complete": "yes", "groups": SMALL["groups"]},
            {"require_complete": False},
            {"require_complete": False, "groups": [{"name": "A"}]},
            {"require_complete": False, "groups": [{"name": "A", "patterns": []}]},
            {"require_complete": False, "groups": SMALL["groups"], "extra": 1},
            ["not", "a", "mapping"],
        ],
    )
    def test_given_malformed_catalogue_when_parsed_then_rejected(self, data):
        with pytest.raises(PackContentError):
            parse_catalogue(data, "catalogue.yaml")

    def test_given_file_when_loaded_then_parsed(self, tmp_path):
        write_tree(tmp_path, {"c.yaml": "require_complete: true\ngroups:\n  - name: A\n    patterns: [x]\n"})
        assert load_catalogue(tmp_path / "c.yaml").require_complete is True


class TestCoverage:
    def test_given_no_patterns_directory_then_everything_pending(self, tmp_path):
        report = coverage(cat(), tmp_path / "patterns")
        assert report.authored == ()
        assert report.pending == ("one", "two", "three")
        assert report.unknown == ()
        assert report.problems() == []
        assert "0/3 authored" in report.summary()
        assert "one, two, three" in report.summary()

    def test_given_partial_patterns_then_pending_remain_visible(self, tmp_path):
        write_tree(tmp_path, {"patterns/two/pattern.yaml": "x: 1\n"})
        report = coverage(cat(), tmp_path / "patterns")
        assert report.authored == ("two",)
        assert report.pending == ("one", "three")
        assert "1/3 authored" in report.summary()

    def test_given_directory_without_pattern_file_then_still_pending(self, tmp_path):
        (tmp_path / "patterns/one").mkdir(parents=True)
        report = coverage(cat(), tmp_path / "patterns")
        assert "one" in report.pending

    def test_given_unknown_pattern_directory_then_problem(self, tmp_path):
        write_tree(tmp_path, {"patterns/rogue/pattern.yaml": "x: 1\n"})
        report = coverage(cat(), tmp_path / "patterns")
        assert report.unknown == ("rogue",)
        assert [d.code for d in report.problems()] == ["catalogue-unknown-pattern"]

    def test_given_require_complete_and_pending_then_each_pending_is_a_problem(self, tmp_path):
        write_tree(tmp_path, {"patterns/one/pattern.yaml": "x: 1\n"})
        report = coverage(cat(require_complete=True), tmp_path / "patterns")
        assert [(d.code, d.message.split()[0]) for d in report.problems()] == [
            ("catalogue-pending-pattern", "two"),
            ("catalogue-pending-pattern", "three"),
        ]

    def test_given_require_complete_and_all_authored_then_no_problems(self, tmp_path):
        write_tree(tmp_path, {f"patterns/{i}/pattern.yaml": "x: 1\n" for i in ("one", "two", "three")})
        report = coverage(cat(require_complete=True), tmp_path / "patterns")
        assert report.pending == ()
        assert report.problems() == []


ids = st.lists(st.from_regex(r"[a-z]{1,6}(-[a-z]{1,4})?", fullmatch=True), min_size=1, max_size=8, unique=True)


class TestProperties:
    @given(ids, st.data())
    def test_authored_and_pending_partition_the_catalogue(self, tmp_path_factory, all_ids, data):
        authored = data.draw(st.sets(st.sampled_from(all_ids)))
        root = tmp_path_factory.mktemp("cov") / "patterns"
        write_tree(root.parent, {f"patterns/{i}/pattern.yaml": "x: 1\n" for i in authored})
        c = parse_catalogue({"require_complete": False, "groups": [{"name": "G", "patterns": all_ids}]}, "c.yaml")
        report = coverage(c, root)
        assert set(report.authored) | set(report.pending) == set(all_ids)
        assert not set(report.authored) & set(report.pending)
        assert len(report.authored) + len(report.pending) == len(all_ids)
        assert set(report.authored) == authored
        assert list(report.pending) == [i for i in all_ids if i not in authored]
