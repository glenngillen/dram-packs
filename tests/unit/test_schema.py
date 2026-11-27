"""JSON Schema diagnostics helper, exercised with an invented test schema.

The schema here is synthetic: it is not, and does not approximate, the Dram
pack schema, which this repository does not yet contain.
"""

from __future__ import annotations

import jsonschema
import pytest
from hypothesis import given
from hypothesis import strategies as st

from dram_pack_tools.diagnostics import PackContentError
from dram_pack_tools.schema import schema_diagnostics

SYNTHETIC = {
    "type": "object",
    "additionalProperties": False,
    "required": ["name"],
    "properties": {"name": {"type": "string"}, "items": {"type": "array", "items": {"type": "integer"}}},
}


def test_given_conforming_instance_then_no_diagnostics():
    assert schema_diagnostics({"name": "x", "items": [1]}, SYNTHETIC, "f.yaml") == []


def test_given_violations_then_each_reported_with_location():
    diags = schema_diagnostics({"items": [1, "two"], "extra": True}, SYNTHETIC, "f.yaml")
    assert {d.code for d in diags} == {"schema"}
    assert all(d.path == "f.yaml" for d in diags)
    messages = " | ".join(d.message for d in diags)
    assert "items/1" in messages
    assert "'name' is a required property" in messages
    assert "extra" in messages


def test_given_invalid_schema_then_raises():
    with pytest.raises(PackContentError) as exc:
        schema_diagnostics({}, {"type": "nonsense"}, "f.yaml")
    assert [d.code for d in exc.value.diagnostics] == ["schema-invalid"]


json_values = st.recursive(
    st.none() | st.booleans() | st.integers() | st.floats(allow_nan=False, allow_infinity=False) | st.text(max_size=20),
    lambda inner: st.lists(inner, max_size=4) | st.dictionaries(st.text(max_size=10), inner, max_size=4),
    max_leaves=15,
)
# Include shaped objects to exercise nested error locations as well as root errors.
instances = json_values | st.fixed_dictionaries({"name": json_values, "items": st.lists(json_values, max_size=5)})


class TestProperties:
    @given(instances, st.text(min_size=1, max_size=30))
    def test_validation_errors_preserve_count_source_code_and_location(self, instance, source):
        validator = jsonschema.validators.validator_for(SYNTHETIC)(SYNTHETIC)
        errors = list(validator.iter_errors(instance))
        diags = schema_diagnostics(instance, SYNTHETIC, source)
        assert len(diags) == len(errors)
        assert all(d.path == source and d.code == "schema" for d in diags)
        expected = [
            f"{'/'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
            for error in sorted(errors, key=lambda error: list(map(str, error.absolute_path)))
        ]
        assert [d.message for d in diags] == expected
