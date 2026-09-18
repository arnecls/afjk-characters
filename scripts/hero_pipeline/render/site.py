"""Pure static-site payload serializers."""

from __future__ import annotations

from typing import Any, Mapping

from ..presentation.site_payload import (
    build_mix_config,
    build_mix_role_prominence,
    build_mix_synergy_index,
    build_site_payload,
)


def render_site_data(
    view: Mapping[str, Any],
    *,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """Serialize site JSON from the presentation model."""
    return build_site_payload(view, generated_at=generated_at)


def render_site_outputs(
    view: Mapping[str, Any],
    *,
    generated_at: str | None = None,
) -> dict[str, dict[str, Any]]:
    """Serialize every model-derived static-site JSON document."""
    return {
        "heroes": render_site_data(view, generated_at=generated_at),
        "mix_synergy_index": build_mix_synergy_index(view),
        "mix_config": build_mix_config(view),
        "mix_role_prominence": build_mix_role_prominence(view),
    }
