"""Replacement projection helpers."""

from __future__ import annotations

from typing import Any, Mapping


REPLACEMENT_CATEGORIES = (
    "overall",
    "buff",
    "energy",
    "healing",
    "similar_skills",
    "damage",
    "debuff",
    "cc",
)


def sanitize_replacements(
    replacements: Mapping[str, Any],
) -> dict[str, list[dict[str, Any]]]:
    """Keep the stable replacement categories and discard empty rows."""
    return {
        category: [
            row
            for row in (replacements.get(category) or [])
            if row.get("matches")
        ]
        for category in REPLACEMENT_CATEGORIES
    }
