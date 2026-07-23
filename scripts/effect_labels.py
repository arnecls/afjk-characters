"""Canonical combat-effect names; polarity lives in category/type, not suffix."""

from __future__ import annotations

import re

# Legacy label -> canonical name (any category).
_LEGACY_TO_CANONICAL: dict[str, str] = {
    "Damage taken reduction": "Damage taken",
    "Damage taken debuff": "Damage taken",
    "Damage dealt buff": "Damage dealt",
    "Damage dealt debuff": "Damage dealt",
    "Magic damage reduction": "Magic damage",
    "Magic damage amplification": "Magic damage",
    "Energy recovery": "Energy",
    "Energy drain": "Energy",
    "Energy recovery debuff": "Energy",
    "Healing stat buff": "Healing",
    "Healing debuff": "Healing",
    "Ally empower buff": "Ally empower",
    "Exemption buff": "Exemption",
    "Basic stats buff": "Basic stats",
    "Basic stats debuff": "Basic stats",
    "ATK buff": "ATK",
    "ATK debuff": "ATK",
    "ATK SPD buff": "ATK SPD",
    "ATK SPD debuff": "ATK SPD",
    "Haste buff": "Haste",
    "Haste debuff": "Haste",
    "Crit buff": "Crit",
    "DEF Penetration buff": "DEF Penetration",
    "DEF buff": "DEF",
    "Phys DEF buff": "Phys DEF",
    "Phys DEF debuff": "Phys DEF",
    "Magic DEF buff": "Magic DEF",
    "Magic DEF debuff": "Magic DEF",
    "Ranged DEF buff": "Ranged DEF",
    "Max HP buff": "Max HP",
    "Max HP debuff": "Max HP",
    "Lifedrain buff": "Lifedrain",
    "Execution buff": "Execution",
    "Execution debuff": "Execution",
    "Attack range buff": "Attack range",
    "Vitality buff": "Vitality",
    "Vitality debuff": "Vitality",
    "Dodge chance buff": "Dodge chance",
    "Movement speed buff": "Movement speed",
    "Movement speed debuff": "Movement speed",
    "DoT debuff": "DoT",
    "Debuff duration debuff": "Debuff duration",
    "Crit Resist debuff": "Crit Resist",
    "Vulnerable debuff": "Vulnerable",
    "Tidal Strength buff": "Tidal Strength",
    "Resilience buff": "Resilience",
    "Poison debuff": "Poison",
    "Artifact buff": "Artifact",
    "Stacking buff": "Stacking",
}

BUFF_EFFECT_TYPES: list[str] = [
    "ATK",
    "Basic stats",
    "ATK SPD",
    "Haste",
    "Crit",
    "DEF Penetration",
    "DEF",
    "Damage taken",
    "Damage dealt",
    "Ranged damage",
    "Magic damage",
    "Energy",
    "Execution",
    "Fatal blow immunity",
    "Invincible",
    "Lifedrain",
    "Max HP",
    "Attack range",
    "Ranged DEF",
    "Crit DMG boost",
    "Vitality",
    "Dodge chance",
    "Movement speed",
]

DEBUFF_EFFECT_TYPES: list[str] = [
    "ATK",
    "Basic stats",
    "DoT",
    "Damage taken",
    "Damage dealt",
    "Debuff duration",
    "Magic damage",
    "Energy",
    "Execution",
    "Haste",
    "Magic DEF",
    "Max HP",
    "Movement speed",
    "Phys DEF",
    "Vitality",
    "Healing",
    "Crit Resist",
    "Vulnerable",
    "ATK SPD",
]


def _slug(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", text.casefold()).strip("_")
    return slug or "effect"


def canonical_effect_label(label: str, category: str) -> str:
    """Return storage/display name without redundant buff/debuff suffix."""
    text = (label or "").strip()
    if not text:
        return text
    if text in _LEGACY_TO_CANONICAL:
        return _LEGACY_TO_CANONICAL[text]
    if category == "buff" and text.casefold().endswith(" buff"):
        return text[: -len(" buff")].rstrip()
    if category == "debuff" and text.casefold().endswith(" debuff"):
        return text[: -len(" debuff")].rstrip()
    return text


def canonical_effect_name(label: str, category: str) -> str:
    """Alias for schema serialization."""
    return canonical_effect_label(label, category)


def display_effect_name(name: str, category: str) -> str:
    """Identity — canonical names are stored and round-tripped as-is."""
    return (name or "").strip()


def build_list_columns() -> list[dict[str, str]]:
    """Column registry for list view: unique id, display label, polarity."""
    columns: list[dict[str, str]] = []
    for label in BUFF_EFFECT_TYPES:
        columns.append(
            {
                "id": f"{_slug(label)}_buff",
                "label": label,
                "polarity": "buff",
                "group": "buff",
            }
        )
    for label in DEBUFF_EFFECT_TYPES:
        columns.append(
            {
                "id": f"{_slug(label)}_debuff",
                "label": label,
                "polarity": "debuff",
                "group": "debuff",
            }
        )
    return columns


def column_id_for_effect(label: str, *, polarity: str) -> str | None:
    """Map canonical effect label + polarity to list column id."""
    group = "buff" if polarity == "buff" else "debuff"
    expected = f"{_slug(label)}_{group}"
    for col in build_list_columns():
        if col["id"] == expected and col["label"] == label:
            return col["id"]
    return None
