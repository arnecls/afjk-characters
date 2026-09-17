"""Pure Heroes.md serializer."""

from __future__ import annotations

from typing import Any, Mapping

META_LABELS = ("Cooldown", "Initial Cooldown", "Skill Range", "Initial Energy")


def _join(value: Any) -> str:
    if not value:
        return ""
    if isinstance(value, str):
        return value.strip()
    return " ".join(str(item).strip() for item in value if str(item).strip())


def _description(value: Any) -> str:
    if isinstance(value, str):
        return value.strip() or "_No description._"
    if not isinstance(value, Mapping):
        return "_No description._"
    raw = str(value.get("raw") or "").strip()
    if raw:
        return raw
    parts = []
    passive = _join(value.get("passive"))
    active = _join(value.get("active"))
    if passive:
        parts.append(f"Passive. {passive}")
    if active:
        parts.append(f"Active. {active}")
    return " ".join(parts) or "_No description._"


def _skill(skill: Mapping[str, Any]) -> str:
    lines = [f"### {skill['section']}", ""]
    if skill.get("name") is not None:
        lines.append(f"**{skill['name']}**")
    if skill.get("unlock") is not None:
        lines.append(f"*{skill['unlock']}*")
    lines.append("")
    meta = skill.get("meta") or {}
    meta_lines = [
        f"- {label}: {meta[label]}" for label in META_LABELS if label in meta
    ]
    if meta_lines:
        lines.extend((*meta_lines, ""))
    lines.extend((_description(skill.get("description")), ""))
    description = skill.get("description")
    upgrades = (
        description.get("upgrades") or []
        if isinstance(description, Mapping)
        else skill.get("levels") or []
    )
    for level in upgrades:
        if level.get("raw"):
            lines.append(f"- {level['text']}")
            continue
        label = f"Level {level['level']}"
        if level.get("unlock"):
            label += f" — {level['unlock']}"
        lines.append(f"- {label}: {_join(level.get('text'))}")
    if upgrades:
        lines.append("")
    return "\n".join(lines)


def _hero(hero: Mapping[str, Any]) -> str:
    lines = [f"## {hero['title']}", ""]
    if hero.get("tags"):
        lines.extend((f"*{hero['tags']}*", ""))
    if hero.get("description"):
        lines.extend((str(hero["description"]), ""))
    lines.extend(_skill(skill) for skill in hero.get("skills") or [])
    return "\n".join(lines)


def render_heroes(view: Mapping[str, Any]) -> str:
    """Serialize the public skill document from structured source records."""
    header = view["manifest"].get("headers", {}).get("heroes_header", "")
    parts = [header.rstrip("\n"), ""]
    parts.extend(_hero(hero["source"]) for hero in view["heroes"])
    return "\n".join(parts)
