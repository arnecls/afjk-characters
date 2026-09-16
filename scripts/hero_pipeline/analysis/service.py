"""Deep analysis orchestration over hero-local inputs."""

from __future__ import annotations

from typing import Any, Mapping

from .calibrate import calibrate_roster
from .local import analyze_local
from .policy import make_policy


def analyze_roster(
    inputs: Mapping[str, Any],
    config: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Analyze and calibrate a roster represented by schema mappings."""
    if config is None:
        import heroes_io as io

        config = io.load_config()
    policy = make_policy(config)
    local = analyze_local(inputs["raw"], policy)
    return calibrate_roster(local, policy)
