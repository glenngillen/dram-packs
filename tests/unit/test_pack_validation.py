"""Pack and index validation against a (synthetic) pinned schema and registry.

These are structural checks mirroring the pinned loader. They never run a
detector, and a pass is not an evaluation verdict.
"""

from __future__ import annotations

import json

import pytest
from hypothesis import assume, given
from hypothesis import strategies as st

from dram_pack_tools.pack import (
    IMPLEMENTED_CHECKS,
    IMPLEMENTED_GATES,
    PLACEHOLDERS,
    _check_params,
    _check_text,
    _schema_errors,
    _validator,
    _entry_path_problem,
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


def outcomes(body):
    return {"core__outcomes.yaml": "outcomes:\n  - id: survival\n" + body}


def test_known_outcome_measure_with_valid_params_is_accepted(tmp_path):
    root = make(tmp_path, **outcomes("    measure: reverted_within\n    params: {days: 14}\n"))
    assert validate_pack(root / "core", pinned()) == []


def test_unknown_outcome_measure_is_rejected(tmp_path):
    root = make(tmp_path, **outcomes("    measure: imaginary_measure\n"))
    diags = validate_pack(root / "core", pinned())
    assert codes(diags) == ["block-unknown"]
    assert "outcomes[0].measure" in diags[0].message and "outcomes.yaml" in diags[0].path


def test_outcome_measure_of_the_wrong_kind_is_rejected(tmp_path):
    root = make(tmp_path, **outcomes("    measure: saved_turns\n"))
    assert codes(validate_pack(root / "core", pinned())) == ["block-kind"]


@pytest.mark.parametrize("params", ["{weeks: 2}", "{days: 0}", "{days: two}"])
def test_outcome_params_the_measure_does_not_take_are_rejected(tmp_path, params):
    root = make(tmp_path, **outcomes(f"    measure: reverted_within\n    params: {params}\n"))
    assert codes(validate_pack(root / "core", pinned())) == ["block-params"]


def effects(body):
    return {"core__patterns__give-it__effects.yaml": "effects:\n  - id: e\n" + body}


def test_known_effect_block_and_signal_are_accepted(tmp_path):
    root = make(tmp_path, **effects("    block: saved_turns\n    signal: shell\n"))
    assert validate_pack(root / "core", pinned()) == []


@pytest.mark.parametrize(
    ("body", "code", "field"),
    [
        ("    block: imaginary_savings\n", "block-unknown", "effects[0].block"),
        ("    block: saved_turns\n    signal: imaginary_signal\n", "block-unknown", "effects[0].signal"),
        ("    block: shell\n", "block-kind", "effects[0].block"),
        ("    block: saved_turns\n    signal: saved_turns\n", "block-kind", "effects[0].signal"),
    ],
)
def test_unknown_or_misplaced_effect_blocks_are_rejected(tmp_path, body, code, field):
    root = make(tmp_path, **effects(body))
    diags = validate_pack(root / "core", pinned())
    assert codes(diags) == [code]
    assert field in diags[0].message and "effects.yaml" in diags[0].path


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


class TestProperties:
    """Synthetic block-bearing slots: block_refs preserves names, kinds and order."""

    name = st.from_regex(r"[a-z][a-z0-9_]{0,12}", fullmatch=True)
    names = st.lists(name, max_size=4)
    cites = st.lists(st.tuples(name, st.booleans()), max_size=4)

    @given(st.one_of(st.none(), name), names, st.one_of(st.none(), name), cites, names, names)
    def test_block_refs_preserve_names_kinds_and_order(self, gate, code, model, cites, mechanisms, moments):
        raw: dict = {"detection": {"code": [{"block": n} for n in code]}}
        expected = []
        if gate is not None:
            raw["applies_to"] = {"block": gate}
            expected.append(("applies_to", gate, "check"))
        expected += [(f"detection.code[{i}]", n, "check") for i, n in enumerate(code)]
        m: dict = {"may_cite": [n if bare else {n: {}} for n, bare in cites]}
        if model is not None:
            m["block"] = model
            expected.append(("detection.model", model, "model"))
        raw["detection"]["model"] = m
        expected += [(f"detection.model.may_cite[{i}]", n, "signal") for i, (n, _) in enumerate(cites)]
        raw["continuous"] = {"mechanisms": [{"block": n} for n in mechanisms]}
        expected += [(f"continuous.mechanisms[{i}]", n, "check") for i, n in enumerate(mechanisms)]
        raw["moments"] = [{"signal": n} for n in moments]
        expected += [(f"moments[{i}]", n, "moment") for i, n in enumerate(moments)]
        assert [(r.field, r.name, r.kind) for r in block_refs(raw)] == expected

    # Synthetic path segments and text fields for the path and placeholder rules.
    segment = st.from_regex(r"[A-Za-z0-9_-][A-Za-z0-9_.-]{0,8}", fullmatch=True).filter(lambda x: x not in (".", ".."))
    rel_path = st.lists(segment, min_size=1, max_size=5).map("/".join)

    @given(rel_path)
    def test_contained_relative_paths_are_accepted(self, path):
        assert _entry_path_problem(path) is None

    @given(rel_path)
    def test_absolute_paths_are_rejected(self, path):
        assert _entry_path_problem("/" + path) == f"/{path} is absolute"

    @given(st.lists(segment, max_size=3), st.sampled_from([".", ".."]), st.lists(segment, max_size=3))
    def test_dot_segments_anywhere_are_rejected(self, before, dot, after):
        path = "/".join(before + [dot] + after)
        assert _entry_path_problem(path) == f"{path} leaves the repository"

    field_paths = st.sampled_from(sorted(PLACEHOLDERS) + [("name",), ("summary",), ("report", "other"), ("guide", "intro")])
    ph_name = st.from_regex(r"[a-z_]{1,10}", fullmatch=True)

    @staticmethod
    def _nest(path, value):
        for key in reversed(path):
            value = {key: value}
        return value

    @given(field_paths, st.lists(ph_name, max_size=4))
    def test_placeholders_pass_only_where_supported(self, path, names):
        allowed = PLACEHOLDERS.get(path, set())
        text = self._nest(path, "x " + " ".join("{" + n + "}" for n in names))
        diags = _check_text(text, "text.yaml")
        unsupported = [n for n in names if n not in allowed]
        assert len(diags) == len(unsupported)
        assert all(d.code == "placeholder" and d.path == "text.yaml" for d in diags)
        for d, n in zip(diags, unsupported):
            assert "{" + n + "}" in d.message and ".".join(path) in d.message

    @given(field_paths)
    def test_supported_placeholders_alone_never_produce_diagnostics(self, path):
        allowed = sorted(PLACEHOLDERS.get(path, set()))
        text = self._nest(path, " ".join("{" + n + "}" for n in allowed) or "plain text")
        assert _check_text(text, "text.yaml") == []

    # _schema_errors is the transformer pack validation actually uses for
    # pack, pattern, case and index files. Synthetic schema only.
    json_values = st.recursive(
        st.none() | st.booleans() | st.integers() | st.text(max_size=6),
        lambda inner: st.lists(inner, max_size=3) | st.dictionaries(st.text(max_size=6), inner, max_size=3),
        max_leaves=8,
    )
    definitions = st.sampled_from(["packFile", "groupsFile", "check"])

    @given(definitions, json_values, st.text(min_size=1, max_size=20), st.one_of(st.none(), st.integers(1, 500)))
    def test_schema_errors_preserve_count_source_code_and_line(self, definition, value, source, line):
        import json as _json

        p = pinned()
        expected = list(_validator(_json.dumps(p.schema, sort_keys=True), definition).iter_errors(value))
        diags = _schema_errors(p, definition, value, source, line)
        assert len(diags) == len(expected)
        assert all(d.path == source and d.code == "schema" and d.line == line for d in diags)
        messages = sorted(f'{".".join(map(str, e.absolute_path)) or "<root>"}: {e.message}' for e in expected)
        assert sorted(d.message for d in diags) == messages

    @given(st.dictionaries(st.sampled_from(["id", "name", "version"]), st.text(max_size=8)))
    def test_schema_errors_empty_exactly_when_valid(self, value):
        import json as _json

        p = pinned()
        valid = _validator(_json.dumps(p.schema, sort_keys=True), "packFile").is_valid(value)
        assert (_schema_errors(p, "packFile", value, "pack.yaml") == []) == valid


    # _check_params transforms a registry block's params schema (adding the
    # slot keys id/block/signal unless slot_keys is False) and turns validation
    # failures into one diagnostic. Synthetic closed schemas shaped like the
    # pinned registry's (type object, additionalProperties false).
    SLOTS = ("id", "block", "signal")
    param_name = st.from_regex(r"[a-z][a-z_]{0,8}", fullmatch=True).filter(lambda n: n not in ("id", "block", "signal"))
    param_types = st.sampled_from(["string", "integer", "boolean"])
    VALUES = {"string": st.text(max_size=6), "integer": st.integers(), "boolean": st.booleans()}
    WRONG = {"string": 7, "integer": "seven", "boolean": "yes"}

    @st.composite
    def block_and_params(draw):
        names = draw(st.lists(TestProperties.param_name, min_size=1, max_size=4, unique=True))
        types = {n: draw(TestProperties.param_types) for n in names}
        required = draw(st.lists(st.sampled_from(names), unique=True))
        params_schema = {
            "type": "object",
            "additionalProperties": False,
            "properties": {n: {"type": t} for n, t in types.items()},
        }
        if required:
            params_schema["required"] = required
        present = set(required) | set(draw(st.lists(st.sampled_from(names), unique=True)))
        params = {n: draw(TestProperties.VALUES[types[n]]) for n in sorted(present)}
        return {"kind": "check", "params": params_schema}, types, required, params

    @given(block_and_params(), st.booleans(), st.dictionaries(st.sampled_from(SLOTS), st.text(max_size=6), max_size=3))
    def test_check_params_accepts_valid_params_and_preserves_the_schema(self, drawn, slot_keys, slots):
        import copy

        block, _, _, params = drawn
        before = copy.deepcopy(block)
        if slot_keys:
            params = {**params, **slots}
        assert _check_params(block, "detection.code[0]", "blk", params, "pattern.yaml", slot_keys=slot_keys) == []
        assert block == before

    @given(block_and_params(), st.booleans(), param_name)
    def test_check_params_rejects_unknown_keys(self, drawn, slot_keys, extra):
        import copy

        block, types, _, params = drawn
        assume(extra not in types)
        before = copy.deepcopy(block)
        diags = _check_params(block, "detection.code[0]", "blk", {**params, extra: "x"}, "pattern.yaml", slot_keys=slot_keys)
        assert [(d.path, d.code) for d in diags] == [("pattern.yaml", "block-params")]
        assert diags[0].message.startswith("detection.code[0] (blk): ")
        assert block == before

    @given(block_and_params(), st.booleans(), st.data())
    def test_check_params_rejects_missing_or_mistyped_required_values(self, drawn, slot_keys, data):
        block, types, required, params = drawn
        assume(required)
        target = data.draw(st.sampled_from(required))
        broken = dict(params)
        if data.draw(st.booleans()):
            del broken[target]
        else:
            broken[target] = TestProperties.WRONG[types[target]]
        diags = _check_params(block, "f", "blk", broken, "p.yaml", slot_keys=slot_keys)
        assert len(diags) == 1 and diags[0].code == "block-params"

    @given(block_and_params(), st.sampled_from(SLOTS), st.text(max_size=6), st.booleans())
    def test_check_params_slot_keys_follow_the_flag(self, drawn, slot, value, slot_keys):
        block, _, _, params = drawn
        diags = _check_params(block, "f", "blk", {**params, slot: value}, "p.yaml", slot_keys=slot_keys)
        assert (diags == []) == slot_keys
        if slot_keys:
            bad = _check_params(block, "f", "blk", {**params, slot: 1}, "p.yaml", slot_keys=True)
            assert [d.code for d in bad] == ["block-params"]

    @given(st.sampled_from(SLOTS), st.sampled_from(["integer", "boolean"]))
    def test_check_params_block_schema_overrides_a_slot_key(self, slot, typ):
        block = {"kind": "check", "params": {"type": "object", "additionalProperties": False, "properties": {slot: {"type": typ}}}}
        value = 3 if typ == "integer" else True
        assert _check_params(block, "f", "blk", {slot: value}, "p.yaml") == []
        assert block["params"]["properties"] == {slot: {"type": typ}}


def test_schema_errors_report_a_missing_definition():
    diags = _schema_errors(pinned(), "noSuchFile", {}, "x.yaml", 3)
    assert [(d.path, d.code, d.line) for d in diags] == [("x.yaml", "schema", 3)]
    assert "noSuchFile" in diags[0].message
