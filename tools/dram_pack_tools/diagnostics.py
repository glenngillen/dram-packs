"""Structured diagnostics for structural pack-content problems."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Diagnostic:
    """One structural problem in a file. ``line``/``column`` are 1-based."""

    path: str
    code: str
    message: str
    line: int | None = None
    column: int | None = None

    def __str__(self) -> str:
        where = self.path
        if self.line is not None:
            where += f":{self.line}"
            if self.column is not None:
                where += f":{self.column}"
        return f"{where}: [{self.code}] {self.message}"


class PackContentError(Exception):
    """Raised when content cannot be read or is structurally unacceptable."""

    def __init__(self, diagnostics: list[Diagnostic]):
        if not diagnostics:
            raise ValueError("PackContentError requires at least one diagnostic")
        self.diagnostics = list(diagnostics)
        super().__init__("\n".join(str(d) for d in self.diagnostics))
