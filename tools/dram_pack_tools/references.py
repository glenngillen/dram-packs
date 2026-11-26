"""Contained relative references and packaged-tree hygiene checks.

Packaged trees must contain no symlinks and no executable files; every
reference must stay inside the pack root.
"""

from __future__ import annotations

import os
import posixpath
import re
import stat
from pathlib import Path

from .diagnostics import Diagnostic, PackContentError

_WINDOWS_ABSOLUTE = re.compile(r"^(?:[A-Za-z]:[\\/]|\\\\)")


def _fail(ref: object, code: str, message: str) -> PackContentError:
    return PackContentError([Diagnostic(str(ref), code, message)])


def resolve_reference(root: Path, ref: object, *, base: Path | None = None) -> Path:
    """Resolve ``ref`` (relative POSIX path) against ``base``'s directory or ``root``.

    Raises :class:`PackContentError` if the reference is malformed, absolute,
    escapes ``root``, passes through a symlink or names a missing file.
    """
    root = Path(root)
    if not isinstance(ref, str) or not ref.strip() or "\x00" in ref:
        raise _fail(ref, "reference-invalid", "reference must be a non-empty relative path")
    if ref.startswith("/") or _WINDOWS_ABSOLUTE.match(ref):
        raise _fail(ref, "reference-absolute", "reference must be relative to the pack")
    if "\\" in ref:
        raise _fail(ref, "reference-invalid", "use '/' as the path separator")

    start = Path(base).parent if base is not None else root
    try:
        start_rel = start.relative_to(root).as_posix()
    except ValueError:
        raise _fail(ref, "reference-invalid", "base file is outside the pack root") from None
    joined = posixpath.normpath(posixpath.join(start_rel, ref))
    if joined == ".." or joined.startswith("../") or joined == ".":
        raise _fail(ref, "reference-escapes-root", "reference leaves the pack root")

    current = root
    for part in posixpath.join(start_rel, ref).split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if current == root:
                raise _fail(ref, "reference-escapes-root", "reference leaves the pack root")
            current = current.parent
            continue
        current = current / part
        if current.is_symlink():
            raise _fail(ref, "reference-symlink", f"path passes through symlink {current.relative_to(root).as_posix()}")
    if not current.is_file():
        raise _fail(ref, "reference-missing", f"referenced file {joined} does not exist")
    return current


def find_symlinks(root: Path) -> list[Diagnostic]:
    """Report every symlink (file, directory or dangling) under ``root``."""
    found: list[Diagnostic] = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        for name in sorted(dirnames + filenames):
            full = Path(dirpath) / name
            if full.is_symlink():
                found.append(Diagnostic(str(full), "tree-symlink", "packaged trees must not contain symlinks"))
    return found


def find_executables(root: Path) -> list[Diagnostic]:
    """Report regular files with any execute bit set under ``root``."""
    found: list[Diagnostic] = []
    exec_bits = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    for dirpath, _dirnames, filenames in os.walk(root, followlinks=False):
        for name in sorted(filenames):
            full = Path(dirpath) / name
            mode = full.lstat().st_mode
            if stat.S_ISREG(mode) and mode & exec_bits:
                found.append(Diagnostic(str(full), "tree-executable", "packaged trees must not contain executable files"))
    return found
