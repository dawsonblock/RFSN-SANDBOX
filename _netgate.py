"""Helpers for gating network-dependent tests.

Default test runs should be offline-safe.
Set RFSN_ENABLE_NETWORK_TESTS=1 to enable tests that require outbound network.
"""

from __future__ import annotations

import os

import pytest


def require_network() -> None:
    """Skip the current test unless network tests are explicitly enabled."""
    if os.environ.get("RFSN_ENABLE_NETWORK_TESTS", "").strip() != "1":
        pytest.skip(
            "network tests disabled (set RFSN_ENABLE_NETWORK_TESTS=1 to enable)"
        )
