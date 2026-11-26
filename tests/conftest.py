"""Report catalogue authoring coverage at the end of every run.

Pending patterns are always printed so incremental work never hides gaps.
This summary is authoring progress, not detector evaluation.
"""

from __future__ import annotations


def pytest_terminal_summary(terminalreporter):
    from dram_pack_tools.catalogue import coverage, load_catalogue
    from dram_pack_tools.diagnostics import PackContentError
    from tests.content.paths import CATALOGUE, PATTERNS

    terminalreporter.section("dram pack authoring coverage (structural only; not an evaluation)")
    try:
        report = coverage(load_catalogue(CATALOGUE), PATTERNS)
    except PackContentError as err:
        terminalreporter.write_line(f"catalogue unreadable: {err}")
        return
    terminalreporter.write_line(report.summary())
