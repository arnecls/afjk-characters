"""Markdown output adapter."""

from __future__ import annotations

from typing import Any, Mapping


def render_heroes(view: Mapping[str, Any]) -> str:
    """Render the public skill document from the structured view."""
    import heroes_io as io

    return io.render_md(
        [hero["source"] for hero in view["heroes"]],
        header=view["manifest"].get("headers", {}).get("heroes_header", ""),
    )
