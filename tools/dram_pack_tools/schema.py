"""Convert JSON Schema validation results into diagnostics.

No Dram schema is bundled here. Callers must supply a pinned schema obtained
from a verified CLI revision; this module never invents one.
"""

from __future__ import annotations

from typing import Any

import jsonschema
from jsonschema.exceptions import SchemaError

from .diagnostics import Diagnostic, PackContentError


def schema_diagnostics(instance: Any, schema: dict[str, Any], source: str) -> list[Diagnostic]:
    try:
        validator_cls = jsonschema.validators.validator_for(schema)
        validator_cls.check_schema(schema)
    except SchemaError as err:
        raise PackContentError([Diagnostic(source, "schema-invalid", f"schema is invalid: {err.message}")]) from None
    validator = validator_cls(schema)
    out: list[Diagnostic] = []
    for error in sorted(validator.iter_errors(instance), key=lambda e: list(map(str, e.absolute_path))):
        location = "/".join(str(p) for p in error.absolute_path) or "<root>"
        out.append(Diagnostic(source, "schema", f"{location}: {error.message}"))
    return out
