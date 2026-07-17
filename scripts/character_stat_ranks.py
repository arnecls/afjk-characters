"""Load and map character stat ranks for site + overview."""

from __future__ import annotations

import json
import re
from pathlib import Path

STAT_RANKS_PATH = (
    Path(__file__).resolve().parent.parent / "data" / "character_stat_ranks.json"
)

CATEGORY_LABELS = {
    "basic": "Basic Stats",
    "offensive": "Offensive Stats",
    "defensive": "Defensive Stats",
    "other": "Other Stats",
}

RANK_KEY_ALIASES = {
    "elijah-lailah": "twins",
    "smokey-meerky": "smokey-and-meerky",
}


def hero_slug(name: str) -> str:
    """URL slug from a hero display name."""
    slug = name.lower().strip()
    slug = slug.replace("&", "and")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def stats_overview_for_short(short: str, slug_ranks: dict[str, dict]) -> dict | None:
    """Return structured stats overview for a roster short name."""
    return slug_ranks.get(hero_slug(short))


def load_character_stat_ranks(path: Path | None = None) -> dict:
    """Load raw character stat ranks JSON."""
    source = path or STAT_RANKS_PATH
    return json.loads(source.read_text(encoding="utf-8"))


def _format_entry(entry: dict) -> dict:
    categories = [
        {
            "label": CATEGORY_LABELS.get(key, key.replace("_", " ").title()),
            "rank": rank,
        }
        for key, rank in entry.get("categories", {}).items()
    ]
    stats = [
        {"label": label, "rank": rank}
        for label, rank in entry.get("stats", {}).items()
    ]
    return {"categories": categories, "stats": stats}


def build_slug_ranks_map(
    ranks_payload: dict,
    roster_slugs: set[str],
) -> dict[str, dict]:
    """Map site slug to structured stats overview for roster heroes."""
    out: dict[str, dict] = {}
    for rank_key, entry in ranks_payload.get("characters", {}).items():
        slug = RANK_KEY_ALIASES.get(rank_key, rank_key)
        if slug not in roster_slugs:
            continue
        out[slug] = _format_entry(entry)
    return out


def format_stats_overview_markdown(stats_overview: dict) -> list[str]:
    """Text-only Stats overview block for heroes-overview.md."""
    lines = ["", "#### Stats overview", ""]

    def format_line(label: str, items: list[dict]) -> str:
        parts = [f"{item['label']} `{item['rank']}`" for item in items]
        return f"- **{label}**: " + ", ".join(parts)

    if stats_overview.get("categories"):
        lines.append(format_line("Categories", stats_overview["categories"]))
    if stats_overview.get("stats"):
        lines.append(format_line("Stats", stats_overview["stats"]))
    lines.append("")
    return lines
