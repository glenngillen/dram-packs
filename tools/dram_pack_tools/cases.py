"""Authoring rules for ``eval/cases.jsonl`` that the pinned schema cannot state.

* ``pos-N`` cases expect a recognition (``seen`` or ``continuous``) and
  ``neg-N`` cases expect ``opportunity`` or ``none``, so a positive can never
  be relabelled ``none`` to make a disabled detector pass.
* A pattern with no executable detection gives every case an
  ``unevaluable`` reason. The pinned evaluator reports such cases, never runs
  them and never counts them as passes.
* A packet stays inside ``eval/``. A packet with a ``#fragment`` names the
  Markdown scenario that holds a case no collected-history fixture can express.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .diagnostics import Diagnostic, PackContentError
from .docs import heading_slugs
from .references import resolve_reference

POSITIVE = {"seen", "continuous"}
NEGATIVE = {"opportunity", "none"}


def _scenario_ids(text: str) -> set[str]:
    """Case ids a scenario file declares: headings that start with the id."""
    out: set[str] = set()
    for slug in heading_slugs(text):
        head = "-".join(slug.split("-")[:2])
        out.add(head)
    return out


def case_diagnostics(cases: list[dict[str, Any]], eval_dir: Path, *, executable: bool, source: str) -> list[Diagnostic]:
    eval_dir = Path(eval_dir)
    out: list[Diagnostic] = []
    seen: set[str] = set()
    for line, case in enumerate(cases, start=1):
        cid = str(case.get("id", ""))

        def bad(code: str, message: str) -> None:
            out.append(Diagnostic(source, code, f"{cid}: {message}", line))

        if cid in seen:
            bad("case-duplicate", "case id used twice")
            continue
        seen.add(cid)
        expect = case.get("expect")
        if isinstance(expect, str):
            if cid.startswith("pos-") and expect not in POSITIVE:
                bad("case-polarity", f"a positive case expects {expect}; positives expect one of {sorted(POSITIVE)}")
            if cid.startswith("neg-") and expect not in NEGATIVE:
                bad("case-polarity", f"a negative case expects {expect}; negatives expect one of {sorted(NEGATIVE)}")
        if not str(case.get("why", "")).strip():
            bad("case-why", "every case explains itself in why")
        if not executable and not str(case.get("unevaluable", "")).strip():
            bad("case-unevaluable-missing", "this pattern names no block the pinned build runs, so the case must say why it is unevaluable")
        packet = case.get("packet")
        path_part, _, anchor = str(packet).partition("#")
        try:
            target = resolve_reference(eval_dir, path_part, base=eval_dir / "cases.jsonl")
        except PackContentError as err:
            bad("case-packet", err.diagnostics[0].message)
            continue
        if anchor:
            if target.suffix != ".md" or anchor not in _scenario_ids(target.read_text(encoding="utf-8")):
                bad("case-scenario-missing", f"{packet} names no scenario heading starting with {anchor}")
    return out
