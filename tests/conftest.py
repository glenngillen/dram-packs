"""Report catalogue authoring coverage at the end of every run.

Pending patterns are always printed so incremental work never hides gaps.
This summary is authoring progress, not detector evaluation.
"""

from __future__ import annotations

from hypothesis import settings

# Many property tests build real files under tmp_path, so per-example time
# depends on disk and machine load, not on the code under test. A wall-clock
# deadline only makes them flaky (DeadlineExceeded under load); correctness is
# what they check.
settings.register_profile("default", deadline=None)
settings.load_profile("default")


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
