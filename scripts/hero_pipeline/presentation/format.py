"""Side-effect-free formatting over resolved presentation records."""

from __future__ import annotations

from typing import Any, Mapping

from effect_labels import BUFF_EFFECT_TYPES, DEBUFF_EFFECT_TYPES
from healing_types import (
    DIRECT_HEALING_LABEL,
    HEALING_OVER_TIME_LABEL,
)

from .project import SECTION_BY_CATEGORY, TIER_ORDER, TRUE_DAMAGE_TYPES

SKILL_CATEGORY_ORDER = (
    "ultimate",
    "skill1",
    "skill2",
    "skill3",
    "skill4",
    "skill5",
)
CATEGORY_LABELS = {
    "ultimate": "Ultimate",
    "skill1": "Skill 1",
    "skill2": "Skill 2",
    "skill3": "Legendary+",
    "skill4": "Mythic+",
    "skill5": "Supreme+",
}
SKILL_OVERVIEW_FIELDS = (
    ("speed", "speed"),
    ("first_cast_speed", "first cast speed"),
    ("heal", "heal"),
    ("buffs", "buffs"),
    ("debuffs", "debuffs"),
    ("damage", "damage"),
)
DAMAGE_TYPE_ORDER = (
    "Physical",
    "Magic",
    "Melee",
    "Ranged",
    "DoT",
    "HP loss",
    "Max HP-based damage",
    "True damage",
)
PRYDWEN_TIERS = (
    ("afk_stages", "AFK Stages"),
    ("dream_realm", "Dream Realm"),
    ("dream_realm_endless", "Dream Realm (Endless)"),
    ("pvp", "PVP"),
)
ALLY_TARGETINGS = {
    "Single target",
    "Multiple targets",
    "Arc",
    "Area",
    "All units",
}
REPLACEMENT_CATEGORY_LABELS = {
    "overall": "Best overall replacement",
    "buff": "Buffs on allies",
    "energy": "Energy provider",
    "healing": "Healing",
    "similar_skills": "Similar Skills",
    "damage": "Damage",
    "debuff": "Debuffs on enemies",
    "cc": "Crowd Control",
}
REPLACEMENT_CATEGORY_ORDER = tuple(REPLACEMENT_CATEGORY_LABELS)
REQUIRE_HANDLERS = (
    "Knock up from allies",
    "Magic damage from allies",
    "Continuous damage on enemies",
    "Damage over time",
    "Ranged damage from allies",
    "Debuff on target",
    "Multiple debuffs on target",
    "Ally on positioning link",
    "Ally Ultimate casts",
    "Enemy defeat",
    "Enemy grouping",
    "Adjacent allies",
    "Party composition",
    "Named ally on team",
    "Temporary ally stat buffs",
    "CC on enemies",
)
REQUIRE_FRAGMENTS = {
    "Knock up from allies": "units **providing knock up**",
    "Magic damage from allies": "units **dealing magic damage**",
    "Ranged damage from allies": "units **dealing ranged damage**",
    "Continuous damage on enemies": (
        "units **dealing continuous damage** to enemies"
    ),
    "Damage over time": "units **applying damage over time** to enemies",
    "Debuff on target": "units **putting debuffs** on enemies",
    "Multiple debuffs on target": (
        "units **putting multiple debuffs** on enemies"
    ),
    "Ally on positioning link": "units **positioned on their link**",
    "Ally Ultimate casts": "allies **casting ultimates**",
    "Enemy defeat": "enemies **to be defeated**",
    "Enemy grouping": "units **grouping enemies**",
    "Adjacent allies": "allies **adjacent** to them",
    "Party composition": "a party **with the right composition**",
    "Named ally on team": "specific **named allies**",
    "Temporary ally stat buffs": "units **buffing them**",
    "CC on enemies": "units **applying crowd control** to enemies",
}
SKIPPED_REQUIRES = {
    "Self condition",
    "Enemy condition",
    "Target condition",
}
PLACEMENT_REQUIRES = {"Ally on positioning link", "Adjacent allies"}
DIRECT_BUFF_LABELS = {
    "ATK": {"ATK", "Damage dealt"},
    "ATK SPD": {"ATK SPD"},
    "Max HP": {"Max HP"},
    "Shield": {"Shield"},
    "Physical DEF": {"DEF", "Phys DEF"},
    "Magic DEF": {"DEF", "Magic DEF"},
    "Haste": {"Haste"},
    "Crit": {"Crit"},
    "Crit DMG Boost": {"Crit DMG boost"},
    "Execution": {"Execution"},
    "Resilience": {"Resilience"},
    "Healing": {
        DIRECT_HEALING_LABEL,
        HEALING_OVER_TIME_LABEL,
        "Healing",
        "Lifedrain",
    },
    "Energy": {"Energy"},
    "DEF Penetration": {"DEF Penetration"},
}
ROLE_LABELS = {
    "damage_dealer": "Damage dealer",
    "specialist": "Specialist",
    "support": "Support",
    "tank": "Tank",
}
DAMAGE_COLUMNS = (
    ("Magic", "Magic DMG"),
    ("Physical", "Physical DMG"),
    ("True damage", "True DMG"),
    ("HP loss", "HP Loss DMG"),
    ("Max HP-based damage", "Max HP DMG"),
)
CC_TYPES = (
    "Stun",
    "Knock down",
    "Knock up",
    "Knock back",
    "Frighten",
    "Silence",
    "Charm",
    "Sleep",
    "Displace",
    "Bind",
    "Interrupt",
    "Taunt",
    "Blind",
    "Disarm",
)
ANTI_CC_TYPES = (
    "Unaffected",
    "Steadfast",
    "Immune",
    "Untargetable",
    "Cleanse",
)
CSV_COLUMNS = (
    "Name",
    "Faction",
    "Class",
    "Role",
    "AFK Stages tier",
    "Dream Realm tier",
    "Dream Realm Endless tier",
    "PVP tier",
    "Movement",
    "Behavior tags",
    "Signature skill speed",
    "Non-ultimate speed",
    "DoT",
    "HoT",
    "Summons",
    "Energy provider",
    *(column for _, column in DAMAGE_COLUMNS),
    "Healing",
    "Shields",
    "Crowd Control",
    "Crowd Control Counter",
    "Buffs",
    "Debuffs",
)


def overview_header(max_synergies: int) -> list[str]:
    return [
        "# Heroes Overview",
        "",
        "Per-hero synergy picks and summaries derived from skill text in",
        "[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.",
        "Synergy: stat buff tags under **Units improving X**, and",
        "enabler partners matching **Requires** special effects.",
        f"Up to {max_synergies} partners by combined score. Omitted: "
        "ATK-only, Max HP",
        "buff-only, and Shield-only (unless the hero benefits from shields).",
        "Rare conditional buffs score lower.",
        "Meta tiers from "
        "[Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list).",
        "Regenerate: `python3 scripts/generate-heroes-overview.py`.",
        "",
    ]


def _tier_suffix(tier: str) -> str:
    return "" if tier == "base" else f" ({tier})"


def _effect_magnitude(effect: Mapping[str, Any]) -> str:
    magnitude = f"`{effect.get('magnitude', '')}`"
    conditional = effect.get("conditional")
    if conditional:
        return f"{magnitude} — conditional ({conditional})"
    return magnitude


def _buff_effects(
    hero: Mapping[str, Any], *, include_self: bool = False
) -> list[dict[str, Any]]:
    display = hero["display"]
    items = [
        effect
        for effect in (
            list(display["effects"]) + list(display["summon_effects"])
        )
        if effect["category"] == "buff"
        and (include_self or effect["targeting"] != "Self")
        and effect["targeting"] not in (
            "Owned summons",
            "Summons only",
            "Own summons",
        )
    ]
    return sorted(
        items,
        key=lambda effect: (
            TIER_ORDER.get(str(effect["tier"]), 9),
            effect["label"],
        ),
    )


def _summary_buff_effects(hero: Mapping[str, Any]) -> list[dict[str, Any]]:
    return _buff_effects(hero)


def format_summary(hero: Mapping[str, Any]) -> str:
    name = hero["display_name"]
    display = hero["display"]
    lines = [f"### Summary for {name}", ""]
    provides = sorted(
        (
            effect
            for effect in display["special_effects"]
            if effect["kind"] == "provides"
        ),
        key=lambda effect: (
            TIER_ORDER.get(str(effect["tier"]), 9),
            effect["label"],
        ),
    )
    if provides:
        lines.extend((f"#### {name} Provides", ""))
        lines.extend(
            f"- {effect['label']}{_tier_suffix(effect['tier'])} — "
            f"{effect['targeting']}"
            for effect in provides
        )
        lines.append("")
    if display["damage_entries"]:
        lines.extend((f"#### Damage types dealt by {name}", ""))
        damage_effects = [
            effect
            for effect in display["effects"]
            if effect["category"] == "damage"
        ]
        for damage_type, targeting in display["damage_entries"]:
            conditional = sorted(
                {
                    effect["conditional"]
                    for effect in damage_effects
                    if effect["label"] == damage_type
                    and effect.get("conditional")
                }
            )
            suffix = "".join(
                f" — conditional ({value})" for value in conditional
            )
            magnitude = display["damage_magnitudes"].get(damage_type, "")
            if magnitude and damage_type in TRUE_DAMAGE_TYPES:
                lines.append(
                    f"- {damage_type} — {targeting} — "
                    f"`{magnitude}`{suffix}"
                )
            else:
                lines.append(f"- {damage_type} — {targeting}{suffix}")
        lines.append("")
    buffs = _summary_buff_effects(hero)
    if buffs:
        lines.extend((f"#### Buffs provided by {name}", ""))
        lines.extend(
            f"- {effect['label']}{_tier_suffix(effect['tier'])} — "
            f"{effect['targeting']} — {_effect_magnitude(effect)}"
            for effect in buffs
        )
        lines.append("")
    debuffs = sorted(
        (
            effect
            for effect in display["effects"]
            if effect["category"] == "debuff"
            and effect["targeting"] != "Self"
        ),
        key=lambda effect: (
            TIER_ORDER.get(str(effect["tier"]), 9),
            effect["label"],
        ),
    )
    if debuffs:
        lines.extend((f"#### Debuffs provided by {name}", ""))
        lines.extend(
            f"- {effect['label']}{_tier_suffix(effect['tier'])} — "
            f"{effect['targeting']} — {_effect_magnitude(effect)}"
            for effect in debuffs
        )
        lines.append("")
    crowd_control = sorted(
        (
            effect
            for effect in display["effects"]
            if effect["category"] == "cc"
        ),
        key=lambda effect: (
            TIER_ORDER.get(str(effect["tier"]), 9),
            effect["label"],
        ),
    )
    immunities = sorted(
        display["immunities"],
        key=lambda immunity: (
            TIER_ORDER.get(str(immunity["tier"]), 9),
            immunity["immunity_type"],
        ),
    )
    if crowd_control or immunities:
        lines.extend((f"#### Crowd Control provided by {name}", ""))
        lines.extend(
            f"- {immunity['immunity_type']}"
            f"{_tier_suffix(immunity['tier'])} — "
            f"{immunity['targeting']} — {immunity['timing']}"
            for immunity in immunities
        )
        lines.extend(
            f"- {effect['label']}{_tier_suffix(effect['tier'])} — "
            f"{effect['targeting']} — {_effect_magnitude(effect)}"
            for effect in crowd_control
        )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def damage_types(hero: Mapping[str, Any]) -> dict[str, str]:
    analysis = hero["analysis"]
    behavior = analysis.get("behavior") or {}
    overview = behavior.get("skill_overview") or {}
    keys = ["signature"]
    if not behavior.get("signature_skill_is_ult"):
        keys.append("ultimate")
    keys.append("non_ultimate")
    merged: dict[str, str] = {}
    score = {"none": 0, "low": 1, "average": 2, "high": 3}
    for key in keys:
        for damage_type, magnitude in (
            (overview.get(key) or {}).get("damage_types") or {}
        ).items():
            if score.get(magnitude, 0) > score.get(
                merged.get(damage_type, "none"), 0
            ):
                merged[damage_type] = magnitude
    result: dict[str, str] = {}
    display = hero["display"]
    for damage_type, _targeting in display["damage_entries"]:
        if damage_type in merged:
            result[damage_type] = merged[damage_type]
        elif damage_type in display["damage_magnitudes"]:
            result[damage_type] = display["damage_magnitudes"][damage_type]
    primary = hero["source"].get("damage_type")
    if primary and primary not in result:
        if primary in merged:
            result[primary] = merged[primary]
        elif primary in display["damage_magnitudes"]:
            result[primary] = display["damage_magnitudes"][primary]
        else:
            values = [
                score.get((overview.get(key) or {}).get("damage", "none"), 0)
                for key in ("signature", "ultimate", "non_ultimate")
            ]
            result[primary] = {
                0: "low",
                1: "low",
                2: "average",
                3: "high",
            }[max(values)]
    return result


def _behavior_bullet(label: str, body: str) -> str:
    return f"- **{label}**: {body}"


def _signature_category(hero: Mapping[str, Any]) -> str | None:
    behavior = hero["analysis"].get("behavior") or {}
    name = behavior.get("signature_skill_name")
    if not name:
        return None
    if behavior.get("signature_skill_is_ult"):
        return "ultimate"
    for skill_name, skill in hero["analysis"].get("skills", {}).items():
        if skill_name == name:
            return str(skill.get("category") or "") or None
    return None


def _skill_overview_line(label: str, metrics: Mapping[str, Any]) -> str:
    parts = [
        f"{display} `{metrics.get(key)}`"
        for key, display in SKILL_OVERVIEW_FIELDS
        if metrics.get(key, "none") != "none"
    ]
    return _behavior_bullet(label, ", ".join(parts) if parts else "—")


def format_behavior(
    hero: Mapping[str, Any],
    *,
    include_skill_summaries: bool,
    include_stats_overview: bool,
    normalized_tiers: bool = False,
) -> str:
    name = hero["display_name"]
    source = hero["source"]
    analysis = hero["analysis"]
    behavior = analysis.get("behavior") or {}
    tiers = source.get("prydwen_tiers") or {}
    if normalized_tiers:
        tiers = {
            key: str(tiers.get(key) or "?").strip() or "?"
            for key, _label in PRYDWEN_TIERS
        }
    lines = [f"### {name}'s behavior", ""]
    tier_parts = [
        f"`{label} [{tiers[key]}]`"
        for key, label in PRYDWEN_TIERS
        if tiers.get(key)
    ]
    if tier_parts:
        lines.extend((", ".join(tier_parts), ""))
    signature_name = behavior.get("signature_skill_name")
    signature_category = _signature_category(hero)
    if signature_name:
        if behavior.get("signature_skill_is_ult"):
            signature_body = f"{signature_name} (ultimate)"
        else:
            signature_body = (
                f"{signature_name} "
                f"({CATEGORY_LABELS.get(signature_category or '', '')})"
            )
        lines.append(_behavior_bullet("Signature skill", signature_body))
    movement = (
        f"{behavior.get('movement', '')} "
        f"({behavior.get('movement_note', '')})"
    )
    if behavior.get("walk_speed"):
        movement += f"; walk speed {behavior['walk_speed']}"
    lines.append(_behavior_bullet("Movement", movement))
    tags = sorted(hero["curated"].get("behavior_tags") or [])
    if tags:
        lines.append(
            _behavior_bullet(
                "Behavior tags", " ".join(f"`{tag}`" for tag in tags)
            )
        )
    for constraint in behavior.get("placement_constraints") or []:
        if constraint["kind"] in ("ally_placement", "ally_composition"):
            lines.append(
                _behavior_bullet("Ally composition", constraint["text"])
            )
        elif constraint["kind"] == "self_placement":
            lines.append(
                _behavior_bullet("Self placement", constraint["text"])
            )
    typed_damage = damage_types(hero)
    damage_line = [
        f"{damage_type} `{typed_damage[damage_type]}`"
        for damage_type in DAMAGE_TYPE_ORDER
        if damage_type in typed_damage
    ]
    if damage_line:
        lines.append(_behavior_bullet("Damage types", ", ".join(damage_line)))
    play = hero["curated"].get("play_overview")
    if play and str(play).strip():
        lines.extend(("", "#### Play overview", "", str(play).strip()))
    counter = hero["curated"].get("counter_overview")
    if counter and str(counter).strip():
        lines.extend(("", "#### Counter proposal", "", str(counter).strip()))
    stats = hero["curated"].get("stat_ranks")
    if include_stats_overview and stats:
        lines.extend(("", "#### Stats overview", ""))
        if stats.get("categories"):
            values = ", ".join(
                f"{item['label']} `{item['rank']}`"
                for item in stats["categories"]
            )
            lines.append(f"- **Categories**: {values}")
        if stats.get("stats"):
            values = ", ".join(
                f"{item['label']} `{item['rank']}`"
                for item in stats["stats"]
            )
            lines.append(f"- **Stats**: {values}")
        lines.append("")
    overview = behavior.get("skill_overview") or {}
    lines.extend(("", "#### Skill overview", ""))
    signature_label = (
        "Signature skill (ult)"
        if behavior.get("signature_skill_is_ult")
        else "Signature skill"
    )
    lines.append(
        _skill_overview_line(signature_label, overview.get("signature") or {})
    )
    if not behavior.get("signature_skill_is_ult"):
        lines.append(
            _skill_overview_line("Ultimate", overview.get("ultimate") or {})
        )
    lines.append(
        _skill_overview_line(
            "Non-ultimate", overview.get("non_ultimate") or {}
        )
    )
    if include_skill_summaries:
        summaries = hero["curated"].get("skill_summaries") or {}
        categories = {
            skill.get("category")
            for skill in analysis.get("skills", {}).values()
        }
        for category in SKILL_CATEGORY_ORDER:
            summary = str(summaries.get(category, "")).strip()
            if category not in categories or not summary:
                continue
            lines.extend(
                (
                    "",
                    f"##### {CATEGORY_LABELS.get(category, category)}",
                    "",
                    summary,
                )
            )
    lines.append("")
    return "\n".join(lines)


def skill_cards(hero: Mapping[str, Any]) -> list[dict[str, Any]]:
    analysis = hero["analysis"]
    summaries = hero["curated"].get("skill_summaries") or {}
    by_category = {
        skill["category"]: skill for skill in analysis.get("skills", {}).values()
    }
    source_by_section = {
        skill["section"]: skill for skill in hero["source"].get("skills", [])
    }
    cards: list[dict[str, Any]] = []
    for category in SKILL_CATEGORY_ORDER:
        summary = str(summaries.get(category, "")).strip()
        if category not in by_category or not summary:
            continue
        card: dict[str, Any] = {
            "category": category,
            "label": CATEGORY_LABELS.get(category, category),
            "summary": summary,
            "tags": copy_list(by_category[category].get("skill_card_tags")),
        }
        source = source_by_section.get(SECTION_BY_CATEGORY[category])
        if source:
            description = source.get("description") or {}
            if isinstance(description, Mapping):
                raw = str(description.get("raw") or "")
                passive = " ".join(description.get("passive") or [])
                active = " ".join(description.get("active") or [])
                upgrades = description.get("upgrades") or []
            else:
                raw = str(description)
                passive = ""
                active = raw
                upgrades = source.get("levels") or []
            meta = source.get("meta") or {}
            card.update(
                {
                    "name": source.get("name") or "",
                    "unlock": source.get("unlock") or "",
                    "meta": {
                        label: meta[label]
                        for label in (
                            "Cooldown",
                            "Initial Cooldown",
                            "Skill Range",
                            "Initial Energy",
                        )
                        if label in meta
                    },
                    "description": raw or "_No description._",
                    "passive": passive,
                    "active": active,
                    "levels": [
                        {
                            "level": str(level.get("level", "")),
                            "unlock": level.get("unlock") or "",
                            "text": " ".join(level.get("text") or [])
                            if isinstance(level.get("text"), list)
                            else str(level.get("text") or ""),
                        }
                        for level in upgrades
                    ],
                }
            )
        cards.append(card)
    return cards


def copy_list(value: Any) -> list[Any]:
    return [dict(item) if isinstance(item, Mapping) else item for item in value or []]


def _format_reason(reason: str) -> str:
    if reason.startswith("Enables ") or " via " not in reason:
        return reason
    stat, detail = reason.split(" via ", 1)
    effect_label = detail.split(" (", 1)[0]
    if effect_label in DIRECT_BUFF_LABELS.get(stat, set()):
        return detail
    return reason


def _stat_tags(stats: list[str]) -> list[str]:
    items = stats[:5]
    has_attack_speed = "ATK SPD" in items
    result: list[str] = []
    for stat in items:
        if stat == "Haste" and has_attack_speed:
            continue
        result.append("ATK SPD / Haste" if stat == "ATK SPD" else stat)
    return result


def _join_names(names: list[str]) -> str:
    bold = [f"**{name}**" for name in names]
    if len(bold) == 1:
        return bold[0]
    if len(bold) == 2:
        return f"{bold[0]} or {bold[1]}"
    return ", ".join(bold[:-1]) + f", or {bold[-1]}"


def _has_enabler(pick: Mapping[str, Any]) -> bool:
    return any(
        str(reason).startswith("Enables ")
        for reason in pick.get("reasons") or []
    )


def _has_stat_reason(pick: Mapping[str, Any]) -> bool:
    return any(" via " in str(reason) for reason in pick.get("reasons") or [])


def _has_early_energy(pick: Mapping[str, Any]) -> bool:
    markers = (
        "at battle start",
        "start of battle",
        "lieutenant",
        "energy potion",
        "early objective",
        "contract ally, start of battle",
    )
    for reason in pick.get("reasons") or []:
        text = str(reason)
        if not text.startswith("Energy via "):
            continue
        detail = text.removeprefix("Energy via ").split("`", 1)[0].lower()
        if any(marker in detail for marker in markers):
            return True
    return False


def _is_common_pick(
    pick: Mapping[str, Any],
    provider_counts: Mapping[str, int],
    threshold: int,
) -> bool:
    provider = str(pick.get("provider", ""))
    if provider_counts.get(provider, 0) <= threshold:
        return False
    if _has_enabler(pick) or _has_early_energy(pick):
        return False
    return _has_stat_reason(pick)


def _ranked_picks(
    picks: list[dict[str, Any]],
    provider_counts: Mapping[str, int],
    threshold: int,
) -> list[dict[str, Any]]:
    result = [
        pick
        for pick in picks
        if not _is_common_pick(pick, provider_counts, threshold)
    ]
    return sorted(
        result, key=lambda pick: (-pick.get("score", 0), pick["provider"])
    )


def _common_names(
    picks: list[dict[str, Any]],
    provider_counts: Mapping[str, int],
    threshold: int,
) -> list[str]:
    return [
        pick["provider"]
        for pick in picks
        if _is_common_pick(pick, provider_counts, threshold)
    ][:4]


def _display_picks(
    picks: list[dict[str, Any]],
    provider_counts: Mapping[str, int],
    threshold: int,
    limit: int,
) -> tuple[list[dict[str, Any]], bool]:
    ranked = _ranked_picks(picks, provider_counts, threshold)
    if ranked:
        return ranked[:limit], False
    names = _common_names(picks, provider_counts, threshold)
    by_provider = {pick["provider"]: pick for pick in picks}
    fallback = [by_provider[name] for name in names if name in by_provider]
    return fallback[:limit], bool(fallback)


def _requires_sentence(hero: Mapping[str, Any]) -> str | None:
    labels = {
        effect["label"]
        for effect in hero["display"]["special_effects"]
        if effect["kind"] == "requires"
        and effect["label"] not in SKIPPED_REQUIRES
        and effect["label"] not in PLACEMENT_REQUIRES
        and effect["label"] in REQUIRE_HANDLERS
    }
    fragments = [
        REQUIRE_FRAGMENTS[label] for label in REQUIRE_HANDLERS if label in labels
    ]
    if not fragments:
        return None
    if len(fragments) == 1:
        joined = fragments[0]
    elif len(fragments) == 2:
        joined = f"{fragments[0]} and/or {fragments[1]}"
    else:
        joined = ", ".join(fragments[:-1]) + f", and/or {fragments[-1]}"
    return f"{hero['display_name']} also requires {joined}"


def beneficiary_rating(
    score: float, receiver_synergies: list[Mapping[str, Any]]
) -> float:
    if not receiver_synergies:
        return 1.0
    top = max(float(item["score"]) for item in receiver_synergies)
    if top <= 0 or score <= 0:
        return 1.0
    return min(5.0, max(1.0, 1.0 + 4.0 * score / top))


def _buffs_provided(hero: Mapping[str, Any]) -> dict[str, Any] | None:
    buffs = _summary_buff_effects(hero)
    if not buffs:
        return None
    return {
        "hero": hero["display_name"],
        "buffs": [
            {
                "label": f"{effect['label']}{_tier_suffix(effect['tier'])}",
                "targetingType": effect["targeting"],
                "quality": effect.get("magnitude", ""),
                **(
                    {"conditional": effect["conditional"]}
                    if effect.get("conditional")
                    else {}
                ),
            }
            for effect in buffs
        ],
    }


def _buffs_intro(hero: Mapping[str, Any]) -> str | None:
    buffs = _summary_buff_effects(hero)
    if not buffs:
        return None
    targeting_phrases = {
        "All summons": "to all summons",
        "Owned summons": "to owned summons",
        "Summons only": "to owned summons",
        "Own summons": "to owned summons",
        "Single target": "to single targets",
        "Multiple targets": "to multiple targets",
        "All units": "to all units",
        "Area": "in an area",
        "Allies": "to allies",
        "Enemies": "to enemies",
        "Self": "to self",
    }
    fragments = []
    for effect in buffs:
        targeting = targeting_phrases.get(
            effect["targeting"], f"to {str(effect['targeting']).lower()}"
        )
        fragment = (
            f"{effect['label']}{_tier_suffix(effect['tier'])} "
            f"{targeting} `{effect.get('magnitude', '')}`"
        )
        if effect.get("conditional"):
            fragment += f" — conditional ({effect['conditional']})"
        fragments.append(fragment)
    if len(fragments) == 1:
        joined = fragments[0]
    elif len(fragments) == 2:
        joined = f"{fragments[0]} and {fragments[1]}"
    else:
        joined = ", ".join(fragments[:-1]) + f", and {fragments[-1]}"
    return f"{hero['display_name']} provides {joined}."


def build_synergy_section(
    hero: Mapping[str, Any],
    heroes_by_name: Mapping[str, Mapping[str, Any]],
    provider_counts: Mapping[str, int],
    *,
    max_synergies: int,
    max_beneficiaries: int,
    obvious_threshold: int,
) -> tuple[list[str], dict[str, Any]]:
    refs = hero["references"]
    picks, from_common = _display_picks(
        refs["synergies"],
        provider_counts,
        obvious_threshold,
        max_synergies,
    )
    common_names = _common_names(
        refs["synergies"], provider_counts, obvious_threshold
    )
    markdown: list[str] = []
    intro_lines: list[str] = []
    common_buffers: list[dict[str, str]] = []
    benefit_stats = hero["display"]["benefit_stats"]
    if benefit_stats:
        tags = " ".join(f"`{tag}`" for tag in _stat_tags(benefit_stats))
        line = f"Look for units providing: {tags}"
        if common_names and not from_common:
            markdown.append(line + "  ")
            markdown.append(f"Common buffers are {_join_names(common_names)}.")
            intro_lines.extend(
                (line, f"Common buffers are {_join_names(common_names)}.")
            )
            common_buffers = [
                {
                    "name": name,
                    "slug": heroes_by_name[name]["slug"],
                }
                for name in common_names
            ]
        else:
            markdown.append(line)
            intro_lines.append(line)
        markdown.append("")
    requires = _requires_sentence(hero)
    if requires:
        markdown.extend((requires, ""))
    if picks:
        for pick in picks:
            markdown.append(f"- **{pick['provider']}**")
            markdown.extend(
                f"  - {_format_reason(reason)}"
                for reason in pick.get("reasons") or []
            )
    else:
        markdown.append(
            "_No synergy partners matched stat buffs or enablers._"
        )
    receiver_synergies = refs["synergies"]
    partners = [
        {
            "name": pick["provider"],
            "slug": pick["slug"],
            "reasons": [
                _format_reason(reason) for reason in pick.get("reasons") or []
            ],
            "score": pick["score"],
            "scoreRating": beneficiary_rating(
                float(pick["score"]), receiver_synergies
            ),
            "scoreDisplay": "",
        }
        for pick in picks
    ]
    for partner in partners:
        stars = "⭐" * max(1, min(5, int(partner["scoreRating"] // 1)))
        partner["scoreDisplay"] = f"{stars} ({partner['scoreRating']:.1f})"
    partners.sort(key=lambda item: (-item["scoreRating"], item["name"]))
    ranked = _ranked_picks(
        refs["synergies"], provider_counts, obvious_threshold
    )
    more_partners = [
        {
            "name": pick["provider"],
            "slug": pick["slug"],
            "score": pick["score"],
            "scoreRating": beneficiary_rating(
                float(pick["score"]), receiver_synergies
            ),
        }
        for pick in ranked[max_synergies:]
    ]
    more_partners.sort(
        key=lambda item: (-item["scoreRating"], item["name"].lower())
    )
    benefited = refs["beneficiaries"]
    buffs_intro = _buffs_intro(hero)
    buffs_data = _buffs_provided(hero)
    benefited_by: dict[str, Any] = {
        "buffs_provided": buffs_data,
        "intro": None,
        "overflow_reasons": [],
        "heroes": [],
    }
    if benefited or buffs_intro:
        markdown.extend(("", f"### Units benefitting most from {hero['display_name']}", ""))
        if buffs_intro:
            markdown.extend((buffs_intro, ""))
        total = len(benefited)
        if total > max_beneficiaries:
            intro = (
                f"**{total}** units include this provider among their "
                f"top {max_synergies} synergy partners. Why the match is common:"
            )
            markdown.extend((intro, ""))
            markdown.extend(
                f"- {reason}"
                for reason in refs["beneficiary_overflow_reasons"]
            )
            markdown.append("")
            strongest = (
                f"These are the **{max_beneficiaries}** strongest pairings:"
            )
            markdown.extend((strongest + " ", ""))
            benefited_by["intro"] = intro
            benefited_by["overflow_reasons"] = list(
                refs["beneficiary_overflow_reasons"]
            )
            benefited_by["strongest_note"] = strongest
            displayed_beneficiaries = benefited[:max_beneficiaries]
        else:
            displayed_beneficiaries = benefited
        ranked_beneficiaries = []
        for beneficiary in displayed_beneficiaries:
            receiver = heroes_by_name[beneficiary["name"]]
            receiver_picks = receiver["references"]["synergies"]
            rating = beneficiary_rating(
                float(beneficiary["score"]), receiver_picks
            )
            reasons = next(
                (
                    [
                        _format_reason(reason)
                        for reason in pick.get("reasons") or []
                    ]
                    for pick in receiver_picks
                    if pick["provider"] == hero["display_name"]
                ),
                [],
            )
            ranked_beneficiaries.append(
                {
                    "name": beneficiary["name"],
                    "slug": beneficiary["slug"],
                    "score": beneficiary["score"],
                    "scoreRating": rating,
                    "scoreDisplay": (
                        f"{'⭐' * max(1, min(5, int(rating // 1)))} "
                        f"({rating:.1f})"
                    ),
                    "reasons": reasons,
                }
            )
        ranked_beneficiaries.sort(
            key=lambda item: (-item["scoreRating"], item["name"])
        )
        markdown.extend(
            f"- {item['name']} ({item['scoreRating']:.1f} / 5)"
            for item in ranked_beneficiaries
        )
        benefited_by["heroes"] = ranked_beneficiaries
    site = {
        "intro": "\n".join(intro_lines) if intro_lines else None,
        "requires": {"text": requires} if requires else None,
        "common_buffers": common_buffers,
        "partners": partners,
        "more_partners": more_partners,
        "benefited_by": benefited_by if (benefited or buffs_data) else None,
    }
    return markdown, site


def format_replacements(
    hero: Mapping[str, Any], max_replacements: int
) -> tuple[list[str], list[dict[str, Any]]]:
    replacements = hero["references"].get("replacements") or {}
    if not any(replacements.values()):
        return [], []
    markdown = [
        "",
        f"### Units that can act as a replacement for {hero['display_name']}",
        "",
    ]
    site: list[dict[str, Any]] = []
    for category in REPLACEMENT_CATEGORY_ORDER:
        entries = replacements.get(category) or []
        if not entries:
            continue
        label = REPLACEMENT_CATEGORY_LABELS[category]
        markdown.extend((f"**{label}**", ""))
        site_entries = []
        for entry in entries[:max_replacements]:
            if category == "energy":
                markdown.append(f"- {entry['name']}")
                site_entries.append(
                    {
                        "name": entry["name"],
                        "slug": entry["slug"],
                        "detail": "",
                    }
                )
                continue
            score = float(entry["score"])
            tags = " ".join(
                f"`{tag}`" for tag in (entry.get("matches") or [])[:5]
            )
            pct = int(score * 100)
            markdown.append(
                f"- {entry['name']} ({pct}%{f' {tags}' if tags else ''})"
            )
            site_entries.append(
                {
                    "name": entry["name"],
                    "slug": entry["slug"],
                    "detail": tags,
                    "score": score,
                    "scoreRating": min(5.0, max(1.0, 1.0 + 4.0 * score)),
                }
            )
        site.append({"category": label, "entries": site_entries})
        markdown.append("")
    return markdown, site


def build_csv_row(hero: Mapping[str, Any]) -> list[str]:
    source = hero["source"]
    analysis = hero["analysis"]
    behavior = analysis.get("behavior") or {}
    tiers = source.get("prydwen_tiers") or {}
    movement = str(behavior.get("movement") or "")
    walk_speed = str(behavior.get("walk_speed") or "")
    if movement and walk_speed:
        movement = f"{movement} | {walk_speed}"
    cells: dict[str, list[str]] = {}
    flags: dict[str, bool] = {}

    def add(column: str, value: str) -> None:
        if value:
            cells.setdefault(column, []).append(value)

    def value(effect: Mapping[str, Any]) -> str:
        trailing = str(effect.get("magnitude") or "")
        if effect.get("conditional"):
            trailing = (
                f"{trailing} — conditional ({effect['conditional']})"
            )
        targeting = str(effect.get("targeting") or "")
        return (
            f"{targeting} — {trailing}"
            if targeting and trailing
            else targeting or trailing
        )

    display = hero["display"]
    for damage_type, targeting in display["damage_entries"]:
        if damage_type == "DoT":
            flags["DoT"] = True
            continue
        column = dict(DAMAGE_COLUMNS).get(damage_type)
        if not column:
            continue
        trailing = ""
        magnitude = display["damage_magnitudes"].get(damage_type, "")
        if magnitude and damage_type in TRUE_DAMAGE_TYPES:
            conditional = sorted(
                {
                    effect["conditional"]
                    for effect in display["effects"]
                    if effect["category"] == "damage"
                    and effect["label"] == damage_type
                    and effect.get("conditional")
                }
            )
            trailing = str(magnitude) + "".join(
                f" — conditional ({item})" for item in conditional
            )
        add(
            column,
            f"{targeting} — {trailing}" if trailing else str(targeting),
        )
    buff_types = set(BUFF_EFFECT_TYPES)
    debuff_types = set(DEBUFF_EFFECT_TYPES)
    for effect in _buff_effects(hero, include_self=True):
        label = str(effect["label"])
        if label == HEALING_OVER_TIME_LABEL:
            flags["HoT"] = True
        elif label == DIRECT_HEALING_LABEL:
            add("Healing", value(effect))
        elif label == "Shield":
            add("Shields", value(effect))
        elif label in buff_types:
            add("Buffs", f"{label} — {value(effect)}")
    for effect in sorted(
        (
            item
            for item in display["effects"]
            if item["category"] == "debuff"
            and item["targeting"] != "Self"
        ),
        key=lambda item: (
            TIER_ORDER.get(str(item["tier"]), 9),
            item["label"],
        ),
    ):
        if effect["label"] in debuff_types:
            add("Debuffs", f"{effect['label']} — {value(effect)}")
    for immunity in display["immunities"]:
        if immunity["immunity_type"] in ANTI_CC_TYPES:
            add(
                "Crowd Control Counter",
                f"{immunity['immunity_type']} — "
                f"{immunity['targeting']} — {immunity['timing']}",
            )
    for effect in sorted(
        (
            item
            for item in display["effects"]
            if item["category"] == "cc"
        ),
        key=lambda item: (
            TIER_ORDER.get(str(item["tier"]), 9),
            item["label"],
        ),
    ):
        if effect["label"] in CC_TYPES:
            add(
                "Crowd Control",
                f"{effect['label']} — {value(effect)}",
            )
    if display["summon_effects"] or any(
        effect["kind"] == "provides"
        and str(effect["label"]).startswith("Summoning")
        for effect in display["special_effects"]
    ):
        flags["Summons"] = True

    def ordered(column: str, order: tuple[str, ...]) -> str:
        values = list(enumerate(cells.get(column, [])))
        positions = {label: index for index, label in enumerate(order)}
        values.sort(
            key=lambda pair: (
                positions.get(pair[1].split(" — ", 1)[0], 999),
                pair[0],
            )
        )
        return "; ".join(item for _index, item in values)

    signature_speed = ""
    if not behavior.get("signature_skill_is_ult"):
        signature_speed = str(
            (
                (behavior.get("skill_overview") or {}).get("signature")
                or {}
            ).get("speed", "")
        )
    non_ultimate_speed = str(
        (
            (behavior.get("skill_overview") or {}).get("non_ultimate")
            or {}
        ).get("speed", "")
    ).replace("none", "")
    return [
        hero["display_name"],
        source.get("faction") or "",
        source.get("class") or "",
        ROLE_LABELS.get(analysis.get("role_category") or "", ""),
        tiers.get("afk_stages", ""),
        tiers.get("dream_realm", ""),
        tiers.get("dream_realm_endless", ""),
        tiers.get("pvp", ""),
        movement,
        "; ".join(sorted(hero["curated"].get("behavior_tags") or [])),
        signature_speed,
        non_ultimate_speed,
        "yes" if flags.get("DoT") else "",
        "yes" if flags.get("HoT") else "",
        "yes" if flags.get("Summons") else "",
        "yes" if analysis.get("is_energy_provider") else "",
        *["; ".join(cells.get(column, [])) for _name, column in DAMAGE_COLUMNS],
        "; ".join(cells.get("Healing", [])),
        "; ".join(cells.get("Shields", [])),
        ordered("Crowd Control", CC_TYPES),
        ordered("Crowd Control Counter", ANTI_CC_TYPES),
        ordered("Buffs", tuple(BUFF_EFFECT_TYPES)),
        ordered("Debuffs", tuple(DEBUFF_EFFECT_TYPES)),
    ]


def build_overview_markdown(
    view: Mapping[str, Any],
    *,
    max_synergies: int,
    max_beneficiaries: int,
    obvious_threshold: int,
    max_replacements: int,
) -> str:
    heroes_by_name = {
        hero["display_name"]: hero for hero in view["heroes"]
    }
    provider_counts = {
        hero["display_name"]: len(hero["references"]["beneficiaries"])
        for hero in view["heroes"]
    }
    parts = overview_header(max_synergies)
    for hero in sorted(
        view["heroes"], key=lambda item: item["display_name"]
    ):
        synergy, _site = build_synergy_section(
            hero,
            heroes_by_name,
            provider_counts,
            max_synergies=max_synergies,
            max_beneficiaries=max_beneficiaries,
            obvious_threshold=obvious_threshold,
        )
        replacements, _site_replacements = format_replacements(
            hero, max_replacements
        )
        parts.extend((f"## {hero['display_name']}", ""))
        parts.extend(
            format_behavior(
                hero,
                include_skill_summaries=True,
                include_stats_overview=True,
            ).splitlines()
        )
        parts.append("")
        parts.extend(
            (
                f"### Units improving {hero['display_name']}",
                "",
                *synergy,
                *replacements,
                format_summary(hero).rstrip(),
                "",
            )
        )
    return "\n".join(parts).rstrip() + "\n"
