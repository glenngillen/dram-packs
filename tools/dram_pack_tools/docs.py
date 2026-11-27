"""Markdown helpers for the pack's authoring references.

Link and anchor checks keep the shared contracts navigable; the parameter
table parser lets tests hold every pattern to the single parameter reference
instead of a restated number. None of this is detector evaluation.
"""

from __future__ import annotations

import posixpath
import re
from dataclasses import dataclass
from pathlib import Path

from .diagnostics import Diagnostic, PackContentError

_FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
_CODE_SPAN = re.compile(r"(`+)(?:(?!\1).)+?\1")
_LINK = re.compile(r"\[(?:[^\[\]]|\[[^\]]*\])*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
_SCHEME = re.compile(r"^(?:[A-Za-z][A-Za-z0-9+.-]*:|//)")
_HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
_PARAM_ROW = re.compile(r"^\|\s*`([a-z0-9_]+)`\s*\|(.*)\|\s*$")
_PARAM_LINK = re.compile(r"\[`([a-z0-9_]+)`\]\(([^)\s#]*parameters\.md)#([^)\s]+)\)")
_PLACEHOLDER = re.compile(r"(?<!\{)\{([^{}]*)\}(?!\})")


def _prose_lines(text: str):
    """Yield ``(line_number, line)`` outside fenced code blocks."""
    fence: str | None = None
    for number, line in enumerate(text.split("\n"), start=1):
        m = _FENCE.match(line)
        if m:
            marker = m.group(1)[0]
            if fence is None:
                fence = marker
                continue
            if marker == fence:
                fence = None
                continue
        if fence is None:
            yield number, line


def markdown_links(text: str) -> list[tuple[str, int]]:
    """Local link targets with their 1-based line, skipping code and URLs."""
    out: list[tuple[str, int]] = []
    for number, line in _prose_lines(text):
        for m in _LINK.finditer(_CODE_SPAN.sub("", line)):
            target = m.group(1)
            if target and not _SCHEME.match(target):
                out.append((target, number))
    return out


def slugify(heading: str) -> str:
    """GitHub-style anchor for a heading, restricted to ASCII."""
    kept = re.sub(r"[^a-z0-9 _-]", "", heading.lower())
    return kept.replace(" ", "-")


def heading_slugs(text: str) -> set[str]:
    """Anchors GitHub assigns to the headings in ``text``.

    Mirrors github-slugger: a repeated slug takes the next ``-N`` suffix that
    no earlier heading (suffixed or not) already holds, so ``A``, ``A-1``,
    ``A`` yields ``a``, ``a-1``, ``a-2``.
    """
    occurrences: dict[str, int] = {}
    for _number, line in _prose_lines(text):
        m = _HEADING.match(line)
        if not m:
            continue
        base = result = slugify(m.group(2).strip())
        while result in occurrences:
            occurrences[base] += 1
            result = f"{base}-{occurrences[base]}"
        occurrences[result] = 0
    return set(occurrences)


def check_links(md_path: Path, root: Path) -> list[Diagnostic]:
    """Every local link in ``md_path`` resolves inside ``root``; anchors exist."""
    md_path, root = Path(md_path), Path(root)
    text = md_path.read_text(encoding="utf-8")
    rel_dir = md_path.parent.relative_to(root).as_posix()
    out: list[Diagnostic] = []
    for target, line in markdown_links(text):
        path_part, _, anchor = target.partition("#")
        if not path_part:
            dest, dest_text = md_path, text
        else:
            joined = posixpath.normpath(posixpath.join(rel_dir, path_part))
            if joined == ".." or joined.startswith("../") or path_part.startswith("/"):
                out.append(Diagnostic(str(md_path), "link-escapes", f"{target} leaves {root.name}/", line))
                continue
            dest = root / joined
            if not dest.exists():
                out.append(Diagnostic(str(md_path), "link-missing", f"{target} does not exist", line))
                continue
            dest_text = dest.read_text(encoding="utf-8") if dest.is_file() and dest.suffix == ".md" else None
        if anchor and dest_text is not None and anchor not in heading_slugs(dest_text):
            out.append(Diagnostic(str(md_path), "link-anchor", f"{target}: no heading #{anchor}", line))
    return out


@dataclass(frozen=True)
class ParameterRow:
    name: str
    default: str
    origin: str
    used_by: str
    line: int
    status: str = ""


def parse_parameter_table(text: str, source: str) -> dict[str, ParameterRow]:
    """Rows of any table whose first cell is a backticked parameter name."""
    rows: dict[str, ParameterRow] = {}
    for number, line in _prose_lines(text):
        m = _PARAM_ROW.match(line.strip())
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) < 3:
            raise PackContentError([Diagnostic(source, "parameter-row", f"{m.group(1)} needs default, origin and used-by cells", number)])
        name = m.group(1)
        if name in rows:
            raise PackContentError([Diagnostic(source, "parameter-duplicate", f"{name} is defined twice", number)])
        rows[name] = ParameterRow(name, cells[0], cells[1], cells[2], number, cells[3] if len(cells) > 3 else "")
    return rows


def parameter_links(text: str) -> list[tuple[str, str]]:
    """``(name, anchor)`` for every ``[`name`](…parameters.md#anchor)`` link."""
    return [(m.group(1), m.group(3)) for m in _PARAM_LINK.finditer(text)]


def placeholders(text: str) -> list[str]:
    """Names inside single ``{…}`` braces; doubled braces are literal."""
    return [m.group(1) for m in _PLACEHOLDER.finditer(text)]
