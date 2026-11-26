"""Pack and index validation against a (synthetic) pinned schema and registry.

These are structural checks mirroring the pinned loader. They never run a
detector, and a pass is not an evaluation verdict.
"""

from __future__ import annotations

import json

import pytest

from dram_pack_tools.pack import (
    IMPLEMENTED_CHECKS,
    IMPLEMENTED_GATES,
    block_refs,
    executable_refs,
    validate_index,
    validate_pack,
)
from tests.helpers.pinned import pinned
from tests.helpers.tree import write_tree

PACK = {
    "core/pack.yaml": "id: acme/core\nname: Core\nversion: 0.1.0\n",
    "core/groups.yaml": "groups:\n  - id: guides\n    name: Guides\n    patterns: [give-it]\n",
    "core/patterns/give-it/pattern.yaml": "id: acme/give-it\nstatus: preview\ngroup: guides\nrung: 1\nenabled: false\n",
    "core/patterns/give-it/text.yaml": "name: Give it\nreport:\n  seen: Seen in {cases} of {applicable}.\n",
}


def codes(diags):
    return [d.code for d in diags]


def make(tmp_path, **overrides):
    files = dict(PACK)
    files.update({k.replace("__", "/"): v for k, v in overrides.items()})
    return write_tree(tmp_path, {k: v for k, v in files.items() if v is not None})


def test_valid_disabled_pack_has_no_diagnostics(tmp_path):
    root = make(tmp_path)
    assert validate_pack(root / "core", pinned()) == []


def test_unknown_pattern_field_is_rejected_even_when_disabled(tmp_path):
    root = make(tmp_path, **{"core__patterns__give-it__pattern.yaml": PACK["core/patterns/give-it/pattern.yaml"] + "stages: {}\n"})
    diags = validate_pack(root / "core", pinned())
    assert codes(diags) == ["schema"]
    assert "pattern.yaml" in diags[0].path and "stages" in diags[0].message


def test_unknown_block_is_rejected_even_when_disabled(tmp_path):
    body = PACK["core/patterns/give-it/pattern.yaml"] + "detection:\n  code:\n    - block: instruction_loaded\n"
    root = make(tmp_path, **{"core__patterns__give-it__pattern.yaml": body})
    diags = validate_pack(root / "core", pinned())
    assert codes(diags) == ["block-unknown"]
    assert "detection.code[0]" in diags[0].message


def test_block_parameter_the_block_does_not_take_is_rejected(tmp_path):
    body = PACK["core/patterns/give-it/pattern.yaml"] + "applies_to:\n  block: tool_call_matches\n  min_sessions: 3\n"
    root = make(tmp_path, **{"core__patterns__give-it__pattern.yaml": body})
    assert codes(validate_pack(root / "core", pinned())) == ["block-params"]


def test_block_of_the_wrong_kind_is_rejected(tmp_path):
    body = PACK["core/patterns/give-it/pattern.yaml"] + "applies_to:\n  block: shell\n"
    root = make(tmp_path, **{"core__patterns__give-it__pattern.yaml": body})
    assert codes(validate_pack(root / "core", pinned())) == ["block-kind"]


def test_pattern_id_must_be_scoped_by_the_pack_org(tmp_path):
    body = PACK["core/patterns/give-it/pattern.yaml"].replace("acme/give-it", "other/give-it")
    root = make(tmp_path, **{"core__patterns__give-it__pattern.yaml": body})
    assert codes(validate_pack(root / "core", pinned())) == ["pattern-unscoped"]


def test_group_must_be_defined(tmp_path):
    body = PACK["core/patterns/give-it/pattern.yaml"].replace("group: guides", "group: nowhere")
    root = make(tmp_path, **{"core__patterns__give-it__pattern.yaml": body})
    assert codes(validate_pack(root / "core", pinned())) == ["ref-group"]


def test_groups_must_list_existing_pattern_directories(tmp_path):
    root = make(tmp_path, **{"core__groups.yaml": "groups:\n  - id: guides\n    patterns: [give-it, missing]\n"})
    assert codes(validate_pack(root / "core", pinned())) == ["ref-group-pattern"]


def test_unsupported_placeholder_is_rejected(tmp_path):
    root = make(tmp_path, **{"core__patterns__give-it__text.yaml": "name: Give it\nnext_step: Add one to {repo}.\n"})
    diags = validate_pack(root / "core", pinned())
    assert codes(diags) == ["placeholder"]
    assert "{repo}" in diags[0].message


def test_placeholder_outside_its_report_field_is_rejected(tmp_path):
    root = make(tmp_path, **{"core__patterns__give-it__text.yaml": "report:\n  not_seen: Seen in {cases}.\n"})
    assert codes(validate_pack(root / "core", pinned())) == ["placeholder"]


def test_case_lines_are_validated_with_line_numbers(tmp_path):
    line = json.dumps({"id": "case-1", "packet": "x.md", "expect": "seen"})
    root = make(tmp_path, **{"core__patterns__give-it__eval__cases.jsonl": line + "\n"})
    diags = validate_pack(root / "core", pinned())
    assert codes(diags) == ["schema"]
    assert diags[0].line == 1


def test_missing_pack_yaml_is_reported(tmp_path):
    root = make(tmp_path, **{"core__pack.yaml": None})
    assert codes(validate_pack(root / "core", pinned())) == ["missing-file"]


def test_block_refs_cover_every_slot():
    raw = {
        "applies_to": {"block": "a"},
        "detection": {"code": [{"block": "b"}], "model": {"block": "c", "may_cite": ["d", {"e": {}}]}},
        "continuous": {"mechanisms": [{"block": "f"}]},
        "moments": [{"signal": "g"}],
    }
    assert [(r.field, r.name) for r in block_refs(raw)] == [
        ("applies_to", "a"),
        ("detection.code[0]", "b"),
        ("detection.model", "c"),
        ("detection.model.may_cite[0]", "d"),
        ("detection.model.may_cite[1]", "e"),
        ("continuous.mechanisms[0]", "f"),
        ("moments[0]", "g"),
    ]


def test_executable_refs_only_name_blocks_the_pinned_build_runs():
    assert IMPLEMENTED_CHECKS == frozenset({"tool_call_matches", "tool_call_sequence"})
    assert IMPLEMENTED_GATES == frozenset({"tool_call_matches"})
    raw = {"detection": {"code": [{"block": "tool_call_sequence"}, {"block": "repo_file_matches"}]}}
    assert [(r.field, r.name) for r in executable_refs(raw)] == [("detection.code[0]", "tool_call_sequence")]
    gated = {"applies_to": {"block": "tool_call_matches"}, **raw}
    assert [r.name for r in executable_refs(gated)] == ["tool_call_matches", "tool_call_sequence"]


def test_an_unrun_gate_leaves_nothing_executable():
    # The pinned evaluator narrows a pattern with an unrun gate to nothing.
    raw = {"applies_to": {"block": "repo_file_matches"}, "detection": {"code": [{"block": "tool_call_sequence"}]}}
    assert executable_refs(raw) == []


def test_a_gate_alone_is_not_executable_detection():
    assert executable_refs({"applies_to": {"block": "tool_call_matches"}}) == []


INDEX = "index: 1\nname: Acme\npacks:\n  - id: acme/core\n    path: core\n"


def test_index_matching_its_pack_is_valid(tmp_path):
    root = make(tmp_path, **{"dram.yaml": INDEX})
    assert validate_index(root, pinned()) == []


def test_index_id_must_equal_manifest_id(tmp_path):
    root = make(tmp_path, **{"dram.yaml": INDEX.replace("acme/core", "acme/other")})
    assert codes(validate_index(root, pinned())) == ["index-id-mismatch"]


@pytest.mark.parametrize("path", ["../core", "/core", "core/../../x"])
def test_index_path_may_not_leave_the_repository(tmp_path, path):
    root = make(tmp_path, **{"dram.yaml": INDEX.replace("path: core", f"path: '{path}'")})
    assert "index-path" in codes(validate_index(root, pinned())) or "schema" in codes(validate_index(root, pinned()))


def test_index_lists_a_pack_once(tmp_path):
    root = make(tmp_path, **{"dram.yaml": INDEX + "  - id: acme/core\n    path: core\n"})
    assert "index-duplicate" in codes(validate_index(root, pinned()))


def test_index_must_be_a_supported_format_version(tmp_path):
    root = make(tmp_path, **{"dram.yaml": INDEX.replace("index: 1", "index: 2")})
    assert codes(validate_index(root, pinned())) == ["index-version"]
