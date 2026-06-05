#!/usr/bin/env python3
"""Build heroes-overview.md from Heroes.md summaries and stat synergies."""

from __future__ import annotations

import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEROES_MD = ROOT / "Heroes.md"
OVERVIEW_MD = ROOT / "heroes-overview.md"

_SPEC = importlib.util.spec_from_file_location(
    "rewrite_summaries", ROOT / "scripts" / "rewrite-summaries.py"
)
_rs = importlib.util.module_from_spec(_SPEC)
sys.modules["rewrite_summaries"] = _rs
assert _SPEC.loader is not None
_SPEC.loader.exec_module(_rs)

STAT_TO_BUFF_LABELS: dict[str, list[str]] = {
    "ATK": ["ATK buff"],
    "ATK SPD": ["ATK SPD buff"],
    "Haste": ["Haste buff"],
    "Max HP": ["Max HP buff", "Shield"],
    "Crit": ["Crit buff"],
    "Execution": ["Execution buff"],
    "Resilience": ["Resilience buff"],
    "Healing": ["Healing", "Healing over time", "Healing stat buff"],
    "Energy": ["Energy recovery"],
    "DEF Penetration": ["DEF Penetration buff"],
    "Life Drain": ["Lifedrain buff"],
    "Physical DEF": ["DEF buff"],
    "Magic DEF": ["DEF buff"],
}

ALLY_TARGETINGS = frozenset(
    {"Single target", "Multiple targets", "Arc", "Area", "All units"}
)

TARGETING_WEIGHT = {
    "All units": 5.0,
    "Area": 4.0,
    "Arc": 3.0,
    "Multiple targets": 3.0,
    "Single target": 1.5,
}

MAG_WEIGHT = {"high": 3.0, "medium": 2.0, "low": 1.0}

MAX_SYNERGIES = 5

FREQUENT_CONDITIONAL_SCORE = 0.85

# Receiver Requires labels that are self-setup, not partner-enabled.
SKIP_ENABLER_REQUIRES = frozenset(
    {
        "Aging on target",
        "Specific form active",
        "Combat Stance active",
        "Boss encounter",
        "Once per battle",
        "Cooldown-gated proc",
        "Enemy monsters present",
        "Monster ingredients",
        "Stacked resource",
        "Energy threshold",
        "Stored resource threshold",
        "Target not CC-immune",
    }
)

# Maps receiver Requires label -> provider matcher name (see score_enabler_match).
ENABLER_REQUIRE_HANDLERS = (
    "Magic damage from allies",
    "Continuous damage on enemies",
    "Damage over time",
    "Ranged damage from allies",
    "Debuff on target",
    "Multiple debuffs on target",
    "Blessed ally active",
    "Ally on bond line",
    "Ally Ultimate casts",
    "Enemy defeat",
    "Adjacent allies",
    "Party composition",
)

PARTY_COMPOSITION_CLASSES = frozenset({"Mage", "Tank", "Support"})


def short_name(title: str) -> str:
    return title.split(" - ", 1)[0].strip()


def extract_summary(block: str) -> str:
    m = re.search(r"### Summary\n([\s\S]*?)(?=\n## |\Z)", block)
    return m.group(1).strip() if m else ""


def receiver_stats(hero: _rs.Hero) -> list[str]:
    return [s for s in hero.benefit_stats if s != "Primary damage type (unit)"]


def provider_skill_text(hero: _rs.Hero) -> str:
    return " ".join(t for _, t, _ in hero.skill_chunks).lower()


def provider_damage_types(hero: _rs.Hero) -> set[str]:
    types: set[str] = set()
    if hero.damage_type:
        types.add(hero.damage_type)
    for dt, _ in hero.damage_entries:
        types.add(dt)
    return types


def provider_best_enemy_targeting(hero: _rs.Hero, damage_type: str) -> str:
    best = "single target"
    best_w = 0.0
    for dt, tgt in hero.damage_entries:
        if dt != damage_type:
            continue
        if tgt == "Self":
            continue
        for part in tgt.split(", "):
            w = TARGETING_WEIGHT.get(part, 1.0)
            if w > best_w:
                best_w = w
                best = part.lower()
    return best


def provider_has_start_of_battle_output(hero: _rs.Hero) -> bool:
    for se in hero.special_effects:
        if se.kind == "provides" and se.label == "Start-of-battle cast":
            return True
    for tier, text, section in hero.skill_chunks:
        if _rs.text_has_start_of_battle_ultimate(text, section):
            return True
    return False


def provider_has_special(hero: _rs.Hero, label: str) -> bool:
    return any(
        se.kind == "provides" and se.label == label for se in hero.special_effects
    )


def provider_enemy_debuffs(hero: _rs.Hero) -> list[_rs.Effect]:
    return [
        e
        for e in hero.effects
        if e.category == "debuff" and e.targeting in ALLY_TARGETINGS
    ]


def match_magic_damage_allies(provider: _rs.Hero) -> tuple[float, str] | None:
    if "Magic" not in provider_damage_types(provider):
        return None
    tw = TARGETING_WEIGHT.get(provider_best_enemy_targeting(provider, "Magic"), 2.0)
    pts = tw * 2.5
    tags = ["Magic damage"]
    if provider_has_start_of_battle_output(provider):
        pts *= 1.35
        tags.append("early battle")
    tgt = provider_best_enemy_targeting(provider, "Magic")
    return pts, f"{' + '.join(tags)} ({tgt})"


def match_dot_damage(provider: _rs.Hero) -> tuple[float, str] | None:
    text = provider_skill_text(provider)
    has_dot = "DoT" in provider_damage_types(provider)
    has_burn = any(e.label == "Burn debuff" for e in provider_enemy_debuffs(provider))
    has_tick = bool(
        re.search(
            r"damage (?:every|per) (?:second|0\.\d+ s)|"
            r"(?:burn|poison|bleed)|"
            r"per second for \d+",
            text,
        )
    )
    if not (has_dot or has_burn or has_tick):
        return None
    tw = 3.0
    if "DoT" in provider_damage_types(provider):
        tw = TARGETING_WEIGHT.get(provider_best_enemy_targeting(provider, "DoT"), 3.0)
    parts = []
    if has_dot:
        parts.append("DoT")
    if has_burn:
        parts.append("Burn")
    if has_tick and not parts:
        parts.append("tick damage")
    detail = " + ".join(parts) if parts else "continuous damage"
    return tw * 2.5, detail


def match_ranged_damage_allies(
    provider: _rs.Hero, hero_class: str = ""
) -> tuple[float, str] | None:
    text = provider_skill_text(provider)
    if not (
        re.search(r"deals ranged damage|ranged damage", text)
        or hero_class == "Marksman"
    ):
        return None
    pts = 3.5
    if provider_has_start_of_battle_output(provider):
        pts *= 1.2
    return pts, "ranged attacks"


def match_debuff_on_target(provider: _rs.Hero) -> tuple[float, str] | None:
    debuffs = provider_enemy_debuffs(provider)
    if not debuffs:
        return None
    best = max(
        debuffs,
        key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1)
        * MAG_WEIGHT.get(e.magnitude, 1),
    )
    tw = TARGETING_WEIGHT.get(best.targeting, 1.0)
    mw = MAG_WEIGHT.get(best.magnitude, 1.0)
    return tw * mw * 1.5, f"{best.label} ({best.targeting.lower()})"


def match_blessed_ally(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_special(provider, "Ally blessing"):
        return 4.0, "Ally blessing"
    return None


def match_stellar_bond(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_special(provider, "Ally link (Stellar Bond)"):
        return 4.5, "Stellar Bond link"
    return None


def match_multiple_debuffs(provider: _rs.Hero) -> tuple[float, str] | None:
    debuffs = provider_enemy_debuffs(provider)
    labels = {e.label for e in debuffs}
    if len(labels) >= 2:
        best = max(
            debuffs,
            key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1)
            * MAG_WEIGHT.get(e.magnitude, 1),
        )
        tw = TARGETING_WEIGHT.get(best.targeting, 1.0)
        return tw * len(labels) * 1.2, f"{len(labels)} debuff types"
    if provider_has_special(provider, "Debuff application"):
        return 3.5, "Debuff application"
    if debuffs:
        return 2.0, debuffs[0].label
    return None


def match_ally_ultimate_casts(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_start_of_battle_output(provider):
        return 4.5, "Start-of-battle Ultimate"
    energy_buffs = [
        e
        for e in provider.effects
        if e.category == "buff"
        and e.label == "Energy recovery"
        and e.targeting in ALLY_TARGETINGS
    ]
    if energy_buffs:
        best = max(
            energy_buffs,
            key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1)
            * MAG_WEIGHT.get(e.magnitude, 1),
        )
        return (
            TARGETING_WEIGHT.get(best.targeting, 2.0) * 2.0,
            "Energy recovery (Ultimate pace)",
        )
    return None


def match_enemy_defeat(provider: _rs.Hero) -> tuple[float, str] | None:
    if provider_has_special(provider, "Instant defeat"):
        return 5.0, "Instant defeat"
    if provider_has_special(provider, "HP threshold strike"):
        return 4.0, "HP threshold strike"
    if provider_has_special(provider, "Mark"):
        return 3.5, "Mark (focus fire)"
    dmg_type = "Magic" if "Magic" in provider_damage_types(provider) else "Physical"
    if dmg_type not in provider_damage_types(provider):
        return None
    tw = TARGETING_WEIGHT.get(provider_best_enemy_targeting(provider, dmg_type), 1.0)
    if tw >= 3.0:
        return tw * 1.5, f"AoE {dmg_type.lower()} (kills)"
    return None


def match_party_composition(
    provider: _rs.Hero, hero_class: str = ""
) -> tuple[float, str] | None:
    if hero_class not in PARTY_COMPOSITION_CLASSES:
        return None
    return 5.0, f"{hero_class} (party slot)"


def match_adjacent_allies(provider: _rs.Hero) -> tuple[float, str] | None:
    ally_buffs = [
        e
        for e in provider.effects
        if e.category == "buff" and e.targeting in ALLY_TARGETINGS
    ]
    if not ally_buffs:
        return None
    best = max(
        ally_buffs,
        key=lambda e: TARGETING_WEIGHT.get(e.targeting, 1)
        * MAG_WEIGHT.get(e.magnitude, 1),
    )
    tw = TARGETING_WEIGHT.get(best.targeting, 1.0)
    mw = MAG_WEIGHT.get(best.magnitude, 1.0)
    if len(ally_buffs) >= 2:
        return tw * mw * 1.5, "Multiple ally buffs"
    return tw * mw, f"{best.label} ({best.targeting.lower()})"


def _parse_hero_class(block: str) -> str:
    header = re.search(r"\*([^*]+)\*", block[:400])
    if not header:
        return ""
    parts = [p.strip() for p in header.group(1).split("·")]
    return parts[1] if len(parts) >= 2 else ""


def _make_enabler_matchers(
    hero_class_by_title: dict[str, str],
) -> dict[str, callable]:
    def ranged(p: _rs.Hero) -> tuple[float, str] | None:
        return match_ranged_damage_allies(p, hero_class_by_title.get(p.title, ""))

    def party(p: _rs.Hero) -> tuple[float, str] | None:
        return match_party_composition(
            p, hero_class_by_title.get(p.title, "")
        )

    return {
        "Magic damage from allies": match_magic_damage_allies,
        "Continuous damage on enemies": match_dot_damage,
        "Damage over time": match_dot_damage,
        "Ranged damage from allies": ranged,
        "Debuff on target": match_debuff_on_target,
        "Multiple debuffs on target": match_multiple_debuffs,
        "Blessed ally active": match_blessed_ally,
        "Ally on bond line": match_stellar_bond,
        "Ally Ultimate casts": match_ally_ultimate_casts,
        "Enemy defeat": match_enemy_defeat,
        "Adjacent allies": match_adjacent_allies,
        "Party composition": party,
    }


def receiver_requires(hero: _rs.Hero) -> list[_rs.SpecialEffect]:
    return [se for se in hero.special_effects if se.kind == "requires"]


def score_enabler_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    enabler_matchers: dict[str, callable],
) -> tuple[float, list[str]]:
    if provider.title == receiver.title:
        return 0.0, []

    reasons: list[str] = []
    total = 0.0
    seen: set[str] = set()

    for req in receiver_requires(receiver):
        if req.label in SKIP_ENABLER_REQUIRES:
            continue
        if req.label in seen:
            continue
        matcher = enabler_matchers.get(req.label)
        if not matcher:
            continue
        result = matcher(provider)
        if not result:
            continue
        pts, detail = result
        seen.add(req.label)
        total += pts
        reasons.append(f"Enables {req.label} via {detail}")

    return total, reasons


def _stat_synergy_reasons(reasons: list[str]) -> list[str]:
    return [r for r in reasons if " via " in r and not r.startswith("Enables ")]


def receiver_benefits_from_shields(receiver: _rs.Hero) -> bool:
    """Shield buffs map to Max HP stat; heroes with Max HP in benefits value shields."""
    return "Max HP" in receiver_stats(receiver)


def should_exclude_synergy(reasons: list[str], receiver: _rs.Hero) -> bool:
    """Drop weak or irrelevant synergy lines from the ranked list."""
    stat = _stat_synergy_reasons(reasons)
    has_enabler = any(r.startswith("Enables ") for r in reasons)

    if stat and not has_enabler:
        if all(r.startswith("ATK via ") for r in stat):
            return True
        if all(r.startswith("Max HP via ") for r in stat):
            if all("Max HP via Max HP buff" in r for r in stat):
                return True
            if all("Max HP via Shield" in r for r in stat):
                return not receiver_benefits_from_shields(receiver)
            # Only Max HP-bucket buffs (mix of buff + shield), no other stats.
            return True

    return False


def score_synergy(
    provider: _rs.Hero, receiver: _rs.Hero
) -> tuple[float, list[str]]:
    if provider.title == receiver.title:
        return 0.0, []

    reasons: list[str] = []
    total = 0.0
    seen_stats: set[str] = set()

    for stat in receiver_stats(receiver):
        labels = STAT_TO_BUFF_LABELS.get(stat, [])
        best_for_stat: tuple[float, str] | None = None

        for effect in provider.effects:
            if effect.category != "buff" or effect.label not in labels:
                continue
            if effect.targeting not in ALLY_TARGETINGS:
                continue
            if effect.conditional == "rare":
                continue
            tw = TARGETING_WEIGHT.get(effect.targeting, 1.0)
            mw = MAG_WEIGHT.get(effect.magnitude, 1.0)
            pts = tw * mw
            if effect.conditional == "frequent":
                pts *= FREQUENT_CONDITIONAL_SCORE
            cond = (
                f", conditional ({effect.conditional})"
                if effect.conditional
                else ""
            )
            detail = (
                f"{effect.label} ({effect.targeting.lower()}, "
                f"{effect.magnitude}{cond})"
            )
            if best_for_stat is None or pts > best_for_stat[0]:
                best_for_stat = (pts, detail)

        if best_for_stat:
            total += best_for_stat[0]
            if stat not in seen_stats:
                seen_stats.add(stat)
                reasons.append(f"{stat} via {best_for_stat[1]}")

    return total, reasons


def score_combined_synergy(
    provider: _rs.Hero,
    receiver: _rs.Hero,
    enabler_matchers: dict[str, callable],
) -> tuple[float, list[str]]:
    buff_score, buff_reasons = score_synergy(provider, receiver)
    en_score, en_reasons = score_enabler_synergy(
        provider, receiver, enabler_matchers
    )
    return buff_score + en_score, buff_reasons + en_reasons


def format_synergies(
    receiver: _rs.Hero,
    heroes: list[_rs.Hero],
    enabler_matchers: dict[str, callable],
) -> list[str]:
    ranked: list[tuple[float, list[str], str]] = []
    for provider in heroes:
        score, reasons = score_combined_synergy(
            provider, receiver, enabler_matchers
        )
        if score <= 0 or not reasons:
            continue
        ranked.append((score, reasons, provider.title))

    ranked.sort(key=lambda x: (-x[0], x[2]))
    filtered = [
        entry
        for entry in ranked
        if not should_exclude_synergy(entry[1], receiver)
    ]
    lines: list[str] = []
    for i, (_, reasons, title) in enumerate(filtered[:MAX_SYNERGIES], 1):
        why = "; ".join(reasons)
        lines.append(f"{i}. **{title}** — {why}")
    return lines


def scan_enabler_patterns_in_heroes(heroes: list[_rs.Hero]) -> dict[str, list[str]]:
    """Find skill-text phrases that look like ally/enemy requirements."""
    candidates: dict[str, list[str]] = defaultdict(list)
    patterns: tuple[tuple[str, str], ...] = (
        (
            r"whenever an allied hero .{0,80}(?:deals|casts|uses)",
            "ally action trigger",
        ),
        (
            r"whenever .{0,40}allied .{0,40}(?:deals|casts)",
            "ally action trigger",
        ),
        (
            r"each time an ally .{0,60}(?:deals|casts|uses)",
            "ally action trigger",
        ),
        (
            r"allied hero(?:es)? .{0,50}deals? .{0,30}(?:magic|physical|true)",
            "typed ally damage",
        ),
        (
            r"when .{0,40}ally .{0,40}casts? (?:their )?ultimate",
            "ally ultimate trigger",
        ),
        (
            r"continuous damage .{0,40}(?:they|enemies) take",
            "continuous damage gate",
        ),
        (
            r"converts? .{0,30}continuous damage",
            "continuous damage gate",
        ),
        (
            r"for every .{0,30}(?:non-summoned )?enemy (?:defeated|killed)",
            "kill trigger",
        ),
        (
            r"when(?:ever)? .{0,50}(?:defeated|killed|slain)",
            "kill trigger",
        ),
        (
            r"if .{0,40}ally .{0,40}(?:is |has |casts)",
            "ally condition",
        ),
        (
            r"linked through|stellar bond",
            "bond positioning",
        ),
        (
            r"blessed ally|ally blessed",
            "blessing dependency",
        ),
        (
            r"afflicted by \w+",
            "debuff name gate",
        ),
        (
            r"within \d+ tiles? of (?:her|him|the ally)",
            "proximity to ally",
        ),
        (
            r"at least \d+ different stat reduction debuffs",
            "multiple debuffs gate",
        ),
        (
            r"whenever an allied hero casts their ultimate.{0,40}(?:increases|gains)",
            "ally ultimate benefit",
        ),
        (
            r"every time a non-summoned enemy is defeated",
            "enemy defeat scaling",
        ),
        (
            r"if an ally is within \d+ tile",
            "adjacent ally gate",
        ),
    )
    for hero in heroes:
        for _tier, text, _section in hero.skill_chunks:
            tl = text.lower()
            for pat, tag in patterns:
                if re.search(pat, tl) and hero.title not in candidates[tag]:
                    snip = text[:100].replace("\n", " ")
                    candidates[tag].append(f"{short_name(hero.title)}: …{snip}…")
    return dict(candidates)


def build_overview() -> str:
    text = HEROES_MD.read_text(encoding="utf-8")
    blocks = re.split(r"\n(?=## )", text)
    heroes: list[_rs.Hero] = []
    block_by_title: dict[str, str] = {}

    for block in blocks:
        if not block.startswith("## "):
            continue
        hero = _rs.parse_hero_block(block)
        heroes.append(hero)
        block_by_title[hero.title] = block

    hero_class_by_title: dict[str, str] = {}
    for hero in heroes:
        hero_class_by_title[hero.title] = _parse_hero_class(
            block_by_title[hero.title]
        )
        _rs.analyze_hero(hero)

    _rs.assign_magnitudes(heroes)
    enabler_matchers = _make_enabler_matchers(hero_class_by_title)

    parts = [
        "# Heroes Overview",
        "",
        "Per-hero summaries from [Heroes.md](Heroes.md), plus synergy picks:",
        "stat buffs matching **Stats the unit benefits from**, and **enabler**",
        "partners matching **Requires** special effects.",
        "Up to five partners by combined score. Omitted: ATK-only, Max HP",
        "buff-only, and Shield-only (unless the hero benefits from Max HP/",
        "shields). Rare conditional buffs score lower.",
        "Regenerate with `scripts/generate-heroes-overview.py` after",
        "`scripts/rewrite-summaries.py`.",
        "",
    ]

    for hero in heroes:
        block = block_by_title[hero.title]
        summary = extract_summary(block)
        syn_lines = format_synergies(hero, heroes, enabler_matchers)

        parts.append(f"## {hero.title}")
        parts.append("")
        parts.append("### Summary")
        parts.append("")
        parts.append(summary)
        parts.append("")
        parts.append("### Synergies")
        parts.append("")
        if syn_lines:
            parts.extend(syn_lines)
        else:
            parts.append("_No synergy partners matched stat buffs or enablers._")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    text = HEROES_MD.read_text(encoding="utf-8")
    blocks = [b for b in re.split(r"\n(?=## )", text) if b.startswith("## ")]
    heroes = [_rs.parse_hero_block(b) for b in blocks]
    for h in heroes:
        _rs.analyze_hero(h)

    content = build_overview()
    OVERVIEW_MD.write_text(content, encoding="utf-8")
    print(f"Wrote {OVERVIEW_MD.relative_to(ROOT)} ({len(content.splitlines())} lines)")

    candidates = scan_enabler_patterns_in_heroes(heroes)
    print("\n--- Enabler pattern scan (skill text) ---")
    for tag, examples in sorted(candidates.items()):
        print(f"\n{tag} ({len(examples)} heroes):")
        for ex in examples[:5]:
            print(f"  - {ex}")
        if len(examples) > 5:
            print(f"  … and {len(examples) - 5} more")


if __name__ == "__main__":
    main()
