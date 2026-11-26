"""JSON Schema diagnostics helper, exercised with an invented test schema.

The schema here is synthetic: it is not, and does not approximate, the Dram
pack schema, which this repository does not yet contain.
"""

from __future__ import annotations

import pytest

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
