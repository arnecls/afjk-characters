"""Pytest hooks and session fixtures for scripts/ tests."""

from __future__ import annotations

import pytest


@pytest.fixture(scope="session", autouse=True)
def _preload_hero_blocks():
    from test_roster_cache import hero_blocks

    hero_blocks()
