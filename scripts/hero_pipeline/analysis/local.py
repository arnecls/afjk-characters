"""Local-analysis seam over the existing semantic effect implementation."""

from __future__ import annotations

from typing import Any, Mapping

from .policy import thaw_policy


def analyze_local(
    raw_roster: Mapping[str, Any],
    config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Analyze hero-local inputs while preserving the current JSON contract.

    The legacy effect implementation is temporarily used behind this seam.
    Callers exchange schema-shaped mappings and do not depend on its classes.
    """
    if config is not None:
        from process_config import apply_config

        apply_config(thaw_policy(config))
    from process_heroes import build_processed

    return build_processed(dict(raw_roster))
