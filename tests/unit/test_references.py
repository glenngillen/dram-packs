"""Contained relative references and packaged-tree hygiene (synthetic trees)."""

from __future__ import annotations

import os

import pytest
from hypothesis import given
from hypothesis import strategies as st

from dram_pack_tools.diagnostics import PackContentError
from dram_pack_tools.references import find_executables, find_symlinks, resolve_reference
from tests.helpers.tree import write_tree


def code_of(exc_info) -> str:
    [diag] = exc_info.value.diagnostics
    return diag.code


@pytest.fixture
def pack(tmp_path):
    root = tmp_path / "pack"
    write_tree(root, {"pack.yaml": "x: 1\n", "patterns/p/pattern.yaml": "x: 1\n", "patterns/p/text.yaml": "x: 1\n"})
    return root


class TestResolveReference:
    def test_given_relative_sibling_when_resolved_then_returns_path(self, pack):
        base = pack / "patterns/p/pattern.yaml"
        assert resolve_reference(pack, "text.yaml", base=base) == pack / "patterns/p/text.yaml"

    def test_given_reference_from_root_when_resolved_then_returns_path(self, pack):
        assert resolve_reference(pack, "patterns/p/text.yaml") == pack / "patterns/p/text.yaml"

    def test_given_dotdot_within_root_when_resolved_then_accepted(self, pack):
        base = pack / "patterns/p/pattern.yaml"
        assert resolve_reference(pack, "../../pack.yaml", base=base) == pack / "pack.yaml"

    @pytest.mark.parametrize("ref", ["../outside.yaml", "patterns/../../outside.yaml"])
    def test_given_escaping_reference_when_resolved_then_rejected(self, pack, ref):
        (pack.parent / "outside.yaml").write_text("x: 1\n")
        with pytest.raises(PackContentError) as exc:
            resolve_reference(pack, ref)
        assert code_of(exc) == "reference-escapes-root"

    @pytest.mark.parametrize("ref", ["/etc/passwd", "C:\\x.yaml", "C:/x.yaml", "\\\\host\\share"])
    def test_given_absolute_reference_when_resolved_then_rejected(self, pack, ref):
        with pytest.raises(PackContentError) as exc:
            resolve_reference(pack, ref)
        assert code_of(exc) == "reference-absolute"

    @pytest.mark.parametrize("ref", ["", "   ", None, 3, "a\\b.yaml", "a\x00b"])
    def test_given_malformed_reference_when_resolved_then_rejected(self, pack, ref):
        with pytest.raises(PackContentError) as exc:
            resolve_reference(pack, ref)
        assert code_of(exc) == "reference-invalid"

    def test_given_missing_target_when_resolved_then_rejected(self, pack):
        with pytest.raises(PackContentError) as exc:
            resolve_reference(pack, "patterns/p/guide.md")
        assert code_of(exc) == "reference-missing"

    def test_given_symlinked_file_when_resolved_then_rejected(self, pack):
        os.symlink(pack / "pack.yaml", pack / "patterns/p/link.yaml")
        with pytest.raises(PackContentError) as exc:
            resolve_reference(pack, "patterns/p/link.yaml")
        assert code_of(exc) == "reference-symlink"

    def test_given_symlinked_directory_component_when_resolved_then_rejected(self, pack):
        os.symlink(pack / "patterns/p", pack / "patterns/q")
        with pytest.raises(PackContentError) as exc:
            resolve_reference(pack, "patterns/q/text.yaml")
        assert code_of(exc) == "reference-symlink"

    @pytest.mark.parametrize("target", ["patterns/p", "pack.yaml", "missing"])
    @pytest.mark.parametrize("use_base", [False, True])
    def test_given_canceled_symlink_component_when_resolved_then_rejected(self, pack, target, use_base):
        os.symlink(pack / target, pack / "patterns/p/link")
        base = pack / "patterns/p/pattern.yaml" if use_base else None
        ref = "link/../../p/text.yaml" if use_base else "patterns/p/link/../../../pack.yaml"
        with pytest.raises(PackContentError) as exc:
            resolve_reference(pack, ref, base=base)
        assert code_of(exc) == "reference-symlink"

    def test_given_symlink_escaping_root_when_resolved_then_rejected(self, pack):
        (pack.parent / "secret.txt").write_text("s")
        os.symlink(pack.parent / "secret.txt", pack / "inside.txt")
        with pytest.raises(PackContentError) as exc:
            resolve_reference(pack, "inside.txt")
        assert code_of(exc) == "reference-symlink"


class TestTreeHygiene:
    def test_given_clean_tree_then_no_findings(self, pack):
        assert find_symlinks(pack) == []
        assert find_executables(pack) == []

    def test_given_symlinks_anywhere_then_each_is_reported(self, pack):
        os.symlink(pack / "pack.yaml", pack / "patterns/p/a.yaml")
        os.symlink(pack / "patterns", pack / "dirlink")
        os.symlink(pack / "nowhere", pack / "dangling")
        found = sorted(d.path for d in find_symlinks(pack))
        assert found == sorted(str(pack / p) for p in ["patterns/p/a.yaml", "dirlink", "dangling"])
        assert {d.code for d in find_symlinks(pack)} == {"tree-symlink"}

    def test_given_executable_file_then_reported(self, pack):
        script = pack / "patterns/p/detect.sh"
        script.write_text("#!/bin/sh\n")
        script.chmod(0o755)
        [diag] = find_executables(pack)
        assert diag.code == "tree-executable"
        assert diag.path == str(script)


segment = st.sampled_from(["a", "b", "..", ".", "patterns", "p", "text.yaml", ""])


class TestProperties:
    @given(st.lists(segment, max_size=6))
    def test_resolved_reference_is_always_inside_root(self, tmp_path_factory, parts):
        root = tmp_path_factory.getbasetemp() / "prop-pack"
        write_tree(root, {"patterns/p/text.yaml": "x: 1\n", "a/b": "x"})
        ref = "/".join(parts)
        try:
            resolved = resolve_reference(root, ref)
        except PackContentError as err:
            assert len(err.diagnostics) == 1
        else:
            assert resolved.is_file()
            assert resolved.resolve().is_relative_to(root.resolve())

    @given(st.text(max_size=30))
    def test_arbitrary_reference_never_raises_unexpected_errors(self, tmp_path_factory, ref):
        root = tmp_path_factory.getbasetemp() / "prop-pack-2"
        root.mkdir(exist_ok=True)
        try:
            resolve_reference(root, ref)
        except PackContentError:
            pass
