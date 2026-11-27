"""Shared read-only access to the pinned CLI compatibility source."""

from __future__ import annotations

import pytest

from dram_pack_tools.pinned import PINNED_REVISION, checkout_path, checkout_revision, load_pinned


@pytest.fixture(scope="session")
def pinned():
    checkout = checkout_path()
    if not (checkout / "internal/pack/schema.json").is_file():
        pytest.skip(f"pinned Dram CLI checkout not found at {checkout} (set DRAM_CLI_CHECKOUT); schema checks not run")
    revision = checkout_revision(checkout)
    assert revision in (None, PINNED_REVISION), f"CLI checkout is at {revision}, not the pinned {PINNED_REVISION}"
    return load_pinned(checkout, revision)
