"""Structured synergy seam over provider and receiver scoring."""

from __future__ import annotations

from typing import Any, Mapping

from ..analysis.policy import make_policy, thaw_policy


def score_roster(
    raw_roster: Mapping[str, Any],
    processed: Mapping[str, Any],
    config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Score provider-to-receiver relationships for a complete roster."""
    if config is None:
        import heroes_io as io

        config = io.load_config()
    policy = make_policy(config)
    from process_config import apply_config

    apply_config(thaw_policy(policy))
    from process_synergies import build_synergies

    return build_synergies(dict(raw_roster), dict(processed))
