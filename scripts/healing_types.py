"""HP recovery healing taxonomy (direct vs over time).

Shared by parsing, schema serialization, replacement scoring, and UI chips.
"""

from __future__ import annotations

DIRECT_HEALING_LABEL = "Direct healing"
HEALING_OVER_TIME_LABEL = "Healing over time"
HEALING_STAT_BUFF_LABEL = "Healing stat buff"

LEGACY_DIRECT_HEALING_LABEL = "Healing"

HP_RECOVERY_LABELS = frozenset(
    {DIRECT_HEALING_LABEL, HEALING_OVER_TIME_LABEL}
)

HEALING_TYPE_DIRECT = "direct"
HEALING_TYPE_OVER_TIME = "over_time"

HEALING_TYPE_DISPLAY: dict[str, str] = {
    HEALING_TYPE_DIRECT: DIRECT_HEALING_LABEL,
    HEALING_TYPE_OVER_TIME: HEALING_OVER_TIME_LABEL,
}

HEALING_LABEL_TO_TYPE: dict[str, str] = {
    DIRECT_HEALING_LABEL: HEALING_TYPE_DIRECT,
    HEALING_OVER_TIME_LABEL: HEALING_TYPE_OVER_TIME,
    LEGACY_DIRECT_HEALING_LABEL: HEALING_TYPE_DIRECT,
}


def normalize_healing_label(label: str) -> str:
    """Map legacy labels to the current HP-recovery display names."""
    if label == LEGACY_DIRECT_HEALING_LABEL:
        return DIRECT_HEALING_LABEL
    return label


def is_hp_recovery_label(label: str) -> bool:
    return normalize_healing_label(label) in HP_RECOVERY_LABELS


def healing_type_from_label(label: str) -> str | None:
    return HEALING_LABEL_TO_TYPE.get(label) or HEALING_LABEL_TO_TYPE.get(
        normalize_healing_label(label)
    )


def healing_type_display(schema: str) -> str:
    return HEALING_TYPE_DISPLAY.get(schema, schema)


def healing_profile_label(key: str, *, section_sep: str = "|") -> str:
    """Strip a skill-section suffix from a replacement-profile key."""
    if section_sep in key:
        return key.split(section_sep, 1)[0]
    return key


def healing_profile_key(
    label: str, source_section: str | None, *, section_sep: str = "|"
) -> str:
    section = (source_section or "").strip()
    norm = normalize_healing_label(label)
    if section:
        return f"{norm}{section_sep}{section}"
    return norm
