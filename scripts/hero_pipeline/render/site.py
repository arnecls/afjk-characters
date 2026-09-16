"""Static-site JSON output adapter."""

from __future__ import annotations

from typing import Any, Mapping

from ..presentation.site_payload import build_site_payload


def render_site_data(
    view: Mapping[str, Any],
    config: Mapping[str, Any],
    *,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """Serialize site JSON from the presentation model."""
    return build_site_payload(
        view,
        config,
        generated_at=generated_at,
    )
