"""Rejection behaviour of the YAML and JSONL readers (synthetic input only)."""

from __future__ import annotations

import json

import pytest
import yaml
from hypothesis import given, settings
from hypothesis import strategies as st

from dram_pack_tools.diagnostics import PackContentError
from dram_pack_tools.readers import load_jsonl, load_yaml, parse_jsonl, parse_yaml


def codes(err: PackContentError) -> list[str]:
    return [d.code for d in err.diagnostics]


class TestParseYaml:
    def test_given_valid_mapping_when_parsed_then_returns_data(self):
        assert parse_yaml("a: 1\nb: [x, y]\n", "f.yaml") == {"a": 1, "b": ["x", "y"]}

    def test_given_duplicate_top_level_key_when_parsed_then_reports_line(self):
        with pytest.raises(PackContentError) as exc:
            parse_yaml("id: one\nname: x\nid: two\n", "f.yaml")
        [diag] = exc.value.diagnostics
        assert diag.code == "yaml-duplicate-key"
        assert diag.line == 3
        assert diag.path == "f.yaml"
        assert "'id'" in diag.message

    def test_given_nested_duplicate_key_when_parsed_then_rejected(self):
        with pytest.raises(PackContentError) as exc:
            parse_yaml("outer:\n  k: 1\n  k: 2\n", "f.yaml")
        assert codes(exc.value) == ["yaml-duplicate-key"]
        assert exc.value.diagnostics[0].line == 3

    def test_given_same_key_in_sibling_mappings_when_parsed_then_accepted(self):
        assert parse_yaml("a: {k: 1}\nb: {k: 2}\n", "f.yaml") == {"a": {"k": 1}, "b": {"k": 2}}

    def test_given_merge_key_override_when_parsed_then_not_a_duplicate(self):
        text = "base: &b {k: 1, j: 2}\nchild:\n  <<: *b\n  k: 3\n"
        assert parse_yaml(text, "f.yaml")["child"] == {"k": 3, "j": 2}

    @pytest.mark.parametrize("text, line, column", [
        ("x:\n  <<: {a: 1}\n  <<: {b: 2}\n", 3, 3),
        ("x: {<<: {<<: {a: 1}, <<: {b: 2}}}", 1, 22),
    ])
    def test_given_duplicate_merge_keys_when_parsed_then_rejected(self, text, line, column):
        with pytest.raises(PackContentError) as exc:
            parse_yaml(text, "f.yaml")
        [diag] = exc.value.diagnostics
        assert diag.code == "yaml-duplicate-key"
        assert (diag.path, diag.line, diag.column) == ("f.yaml", line, column)

    @pytest.mark.parametrize("timestamp", ["2026-99-99", "2026-02-30", "2026-11-27T25:00:00Z"])
    def test_given_invalid_timestamp_when_parsed_then_reports_position(self, timestamp):
        with pytest.raises(PackContentError) as exc:
            parse_yaml(f"date: {timestamp}\n", "f.yaml")
        [diag] = exc.value.diagnostics
        assert diag.code == "yaml-syntax"
        assert (diag.path, diag.line, diag.column) == ("f.yaml", 1, 7)

    def test_given_valid_timestamp_when_parsed_then_accepted(self):
        from datetime import date

        assert parse_yaml("date: 2026-11-27\n", "f.yaml") == {"date": date(2026, 11, 27)}

    def test_given_syntax_error_when_parsed_then_reports_position(self):
        with pytest.raises(PackContentError) as exc:
            parse_yaml("a: [1, 2\nb: 3\n", "f.yaml")
        [diag] = exc.value.diagnostics
        assert diag.code == "yaml-syntax"
        assert diag.line is not None and diag.line >= 1

    def test_given_multiple_documents_when_parsed_then_rejected(self):
        with pytest.raises(PackContentError) as exc:
            parse_yaml("a: 1\n---\nb: 2\n", "f.yaml")
        assert codes(exc.value) == ["yaml-syntax"]

    def test_given_python_tag_when_parsed_then_rejected_safely(self):
        with pytest.raises(PackContentError):
            parse_yaml("a: !!python/object/apply:os.system ['true']\n", "f.yaml")


class TestLoadYaml:
    def test_given_file_when_loaded_then_path_used_in_diagnostics(self, tmp_path):
        f = tmp_path / "x.yaml"
        f.write_text("k: 1\nk: 2\n", encoding="utf-8")
        with pytest.raises(PackContentError) as exc:
            load_yaml(f)
        assert exc.value.diagnostics[0].path == str(f)

    def test_given_missing_file_when_loaded_then_reports_missing(self, tmp_path):
        with pytest.raises(PackContentError) as exc:
            load_yaml(tmp_path / "absent.yaml")
        assert codes(exc.value) == ["missing-file"]

    def test_given_non_utf8_file_when_loaded_then_reports_encoding(self, tmp_path):
        f = tmp_path / "x.yaml"
        f.write_bytes(b"k: \xff\xfe\n")
        with pytest.raises(PackContentError) as exc:
            load_yaml(f)
        assert codes(exc.value) == ["encoding"]


class TestParseJsonl:
    def test_given_object_lines_when_parsed_then_returns_records(self):
        assert parse_jsonl('{"a": 1}\n{"b": [2]}\n', "c.jsonl") == [{"a": 1}, {"b": [2]}]

    def test_given_no_trailing_newline_when_parsed_then_accepted(self):
        assert parse_jsonl('{"a": 1}', "c.jsonl") == [{"a": 1}]

    def test_given_empty_text_when_parsed_then_no_records(self):
        assert parse_jsonl("", "c.jsonl") == []

    def test_given_bad_lines_when_parsed_then_reports_every_line(self):
        text = '{"a": 1}\n{oops\n[1, 2]\n\n{"a": 1, "a": 2}\n{"n": NaN}\n'
        with pytest.raises(PackContentError) as exc:
            parse_jsonl(text, "c.jsonl")
        found = [(d.line, d.code) for d in exc.value.diagnostics]
        assert found == [
            (2, "jsonl-syntax"),
            (3, "jsonl-not-object"),
            (4, "jsonl-blank-line"),
            (5, "jsonl-duplicate-key"),
            (6, "jsonl-syntax"),
        ]
        assert all(d.path == "c.jsonl" for d in exc.value.diagnostics)

    def test_given_missing_file_when_loaded_then_reports_missing(self, tmp_path):
        with pytest.raises(PackContentError) as exc:
            load_jsonl(tmp_path / "cases.jsonl")
        assert codes(exc.value) == ["missing-file"]


json_scalars = st.none() | st.booleans() | st.integers() | st.text(max_size=20)
json_values = st.recursive(
    json_scalars,
    lambda inner: st.lists(inner, max_size=3) | st.dictionaries(st.text(max_size=8), inner, max_size=3),
    max_leaves=10,
)
json_objects = st.dictionaries(st.text(max_size=8), json_values, max_size=4)


class TestProperties:
    @given(st.text())
    def test_parse_jsonl_never_raises_unexpected_errors(self, text):
        try:
            records = parse_jsonl(text, "c.jsonl")
        except PackContentError as err:
            assert err.diagnostics
            assert all(d.line is not None and d.line >= 1 for d in err.diagnostics)
        else:
            assert all(isinstance(r, dict) for r in records)

    @given(st.lists(json_objects, max_size=5))
    def test_jsonl_roundtrip(self, records):
        text = "".join(json.dumps(r) + "\n" for r in records)
        assert parse_jsonl(text, "c.jsonl") == records

    @given(st.text())
    @settings(max_examples=200)
    def test_parse_yaml_never_raises_unexpected_errors(self, text):
        try:
            parse_yaml(text, "f.yaml")
        except PackContentError as err:
            assert err.diagnostics

    @given(st.dictionaries(st.text(min_size=1, max_size=8), json_values, max_size=4))
    def test_yaml_roundtrip_of_unique_mappings(self, data):
        assert parse_yaml(yaml.safe_dump(data), "f.yaml") == data

    @given(st.from_regex(r"[a-z][a-z_]{0,7}", fullmatch=True), st.integers(), st.integers())
    def test_repeated_key_is_always_rejected(self, key, v1, v2):
        with pytest.raises(PackContentError) as exc:
            parse_yaml(f"{key}: {v1}\n{key}: {v2}\n", "f.yaml")
        assert codes(exc.value) == ["yaml-duplicate-key"]
