"""A small synthetic stand-in for the pinned Dram schema and block registry.

Unit tests must not read the real CLI checkout, so this mirrors only the
*shape* the validator relies on: a closed ``$defs`` per pack file and a block
registry of ``{kind, params}`` entries. Field names here are ones the pinned
schema already uses; nothing new is invented.
"""

from __future__ import annotations

from dram_pack_tools.pinned import Pinned

SCOPED = {"type": "string", "pattern": "^[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*$"}
LOCAL = {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]*$"}

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "$defs": {
        "scopedId": SCOPED,
        "localName": LOCAL,
        "check": {
            "type": "object",
            "required": ["block"],
            "properties": {"id": {"$ref": "#/$defs/localName"}, "block": {"$ref": "#/$defs/localName"}},
            "additionalProperties": True,
        },
        "packFile": {
            "type": "object",
            "required": ["id", "name", "version"],
            "additionalProperties": False,
            "properties": {
                "id": {"$ref": "#/$defs/scopedId"},
                "name": {"type": "string"},
                "version": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"},
                "min_cli": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"},
                "description": {"type": "string"},
            },
        },
        "groupsFile": {
            "type": "object",
            "required": ["groups"],
            "additionalProperties": False,
            "properties": {
                "groups": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["id"],
                        "additionalProperties": False,
                        "properties": {
                            "id": {"$ref": "#/$defs/localName"},
                            "name": {"type": "string"},
                            "patterns": {"type": "array", "items": {"$ref": "#/$defs/localName"}},
                        },
                    },
                }
            },
        },
        "outcomesFile": {"type": "object"},
        "progressFile": {"type": "object"},
        "patternFile": {
            "type": "object",
            "required": ["id"],
            "additionalProperties": False,
            "properties": {
                "id": {"$ref": "#/$defs/scopedId"},
                "status": {"enum": ["stable", "preview"]},
                "group": {"$ref": "#/$defs/localName"},
                "rung": {"type": "integer"},
                "enabled": {"type": "boolean"},
                "applies_to": {"$ref": "#/$defs/check"},
                "detection": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "code": {"type": "array", "items": {"$ref": "#/$defs/check"}},
                        "model": {"$ref": "#/$defs/check"},
                    },
                },
                "continuous": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {"mechanisms": {"type": "array", "items": {"$ref": "#/$defs/check"}}},
                },
                "moments": {"type": "array", "items": {"type": "object"}},
            },
        },
        "textFile": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "name": {"type": "string"},
                "summary": {"type": "string"},
                "preview_note": {"type": "string"},
                "report": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {k: {"type": "string"} for k in ("seen", "not_seen", "continuous", "slipped")},
                },
                "next_step": {"type": "string"},
                "advice": {"type": "string"},
                "fix_prompt": {"type": "string"},
            },
        },
        "kindsFile": {"type": "object"},
        "effectsFile": {"type": "object"},
        "writesFile": {"type": "object"},
        "caseLine": {
            "type": "object",
            "required": ["id", "packet", "expect"],
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string", "pattern": "^(pos|neg)-[0-9]+$"},
                "packet": {"type": "string"},
                "why": {"type": "string"},
                "unevaluable": {"type": "string"},
                "expect": {"enum": ["seen", "continuous", "opportunity", "none"]},
            },
        },
        "patternDir": {
            "type": "object",
            "required": ["pattern"],
            "additionalProperties": False,
            "properties": {
                "pattern": {"$ref": "#/$defs/patternFile"},
                "text": {"$ref": "#/$defs/textFile"},
                "cases": {"type": "array", "items": {"$ref": "#/$defs/caseLine"}},
            },
        },
        "registryIndex": {
            "type": "object",
            "required": ["index", "packs"],
            "additionalProperties": False,
            "properties": {
                "index": {"type": "integer", "minimum": 1},
                "name": {"type": "string"},
                "packs": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["id", "path"],
                        "additionalProperties": False,
                        "properties": {
                            "id": {"$ref": "#/$defs/scopedId"},
                            "path": {"type": "string", "pattern": "^[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*$"},
                            "description": {"type": "string"},
                        },
                    },
                },
            },
        },
    },
}

REGISTRY = {
    "blocks": {
        "tool_call_matches": {
            "kind": "check",
            "params": {
                "type": "object",
                "additionalProperties": False,
                "properties": {"tool": {"type": "string"}, "command_matches": {"type": "string"}},
            },
        },
        "repo_file_matches": {
            "kind": "check",
            "params": {"type": "object", "additionalProperties": False, "properties": {"glob": {"type": "string"}}},
        },
        "propose": {"kind": "model", "params": {"type": "object", "additionalProperties": False}},
        "shell": {"kind": "signal", "params": {"type": "object", "additionalProperties": False}},
    }
}


def pinned() -> Pinned:
    return Pinned(schema=SCHEMA, registry=REGISTRY, revision="synthetic")
