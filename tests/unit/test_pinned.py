"""Reading the pinned CLI schema and block registry from a checkout tree."""

from __future__ import annotations

import json

import pytest

from dram_pack_tools.diagnostics import PackContentError
from dram_pack_tools.pinned import PINNED_REVISION, checkout_revision, load_pinned
from tests.helpers.tree import write_tree


def test_pinned_revision_is_the_recorded_full_sha():
    assert PINNED_REVISION == "bdea6f678399b3684519d41cc65645b4a42d53ef"


def test_load_pinned_reads_schema_and_registry(tmp_path):
    write_tree(
        tmp_path,
        {
            "internal/pack/schema.json": json.dumps({"$defs": {"packFile": {}}}),
            "internal/pack/blocks.json": json.dumps({"blocks": {"x": {"kind": "check", "params": {}}}}),
        },
    )
    p = load_pinned(tmp_path)
    assert "packFile" in p.schema["$defs"]
    assert p.registry["blocks"]["x"]["kind"] == "check"


def test_load_pinned_reports_a_missing_checkout(tmp_path):
    with pytest.raises(PackContentError) as err:
        load_pinned(tmp_path / "nowhere")
    assert err.value.diagnostics[0].code == "pinned-missing"


def test_load_pinned_rejects_a_registry_without_blocks(tmp_path):
    write_tree(tmp_path, {"internal/pack/schema.json": "{\"$defs\": {}}", "internal/pack/blocks.json": "{}"})
    with pytest.raises(PackContentError) as err:
        load_pinned(tmp_path)
    assert err.value.diagnostics[0].code == "pinned-invalid"


def test_checkout_revision_reads_a_detached_head(tmp_path):
    write_tree(tmp_path, {".git/HEAD": PINNED_REVISION + "\n"})
    assert checkout_revision(tmp_path) == PINNED_REVISION


def test_checkout_revision_follows_a_loose_ref(tmp_path):
    write_tree(tmp_path, {".git/HEAD": "ref: refs/heads/main\n", ".git/refs/heads/main": "abc123\n"})
    assert checkout_revision(tmp_path) == "abc123"


def test_checkout_revision_falls_back_to_packed_refs(tmp_path):
    write_tree(
        tmp_path,
        {".git/HEAD": "ref: refs/heads/main\n", ".git/packed-refs": "# pack-refs with: peeled\ndef456 refs/heads/main\n"},
    )
    assert checkout_revision(tmp_path) == "def456"


def test_checkout_revision_is_none_without_git_metadata(tmp_path):
    assert checkout_revision(tmp_path) is None
