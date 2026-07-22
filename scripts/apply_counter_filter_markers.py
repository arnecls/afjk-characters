#!/usr/bin/env python3
"""Apply [[filter:id]] like [[Hero]] markers to hero_counter_overviews.json."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COUNTER_PATH = ROOT / "data" / "hero_counter_overviews.json"
CSV_PATH = ROOT / "heroes-overview.csv"
TAGS_PATH = ROOT / "data" / "hero_behavior_tags.json"

HERO_RE = re.compile(r"\[\[([^\]]+)\]\]")
FILTER_RE = re.compile(r"\[\[filter:([a-z0-9-]+)\]\]")

ENERGY = ("Thador", "Hugin", "Rowan")
LASTING = ("Shemira", "Frieren", "Gwyneth", "Pandora")

# Explicit (hero tuple) -> combo id for pairs/triples in "A or B" clauses.
EXPLICIT_COMBOS: dict[tuple[str, ...], str] = {
    ("Ravion", "Nerion"): "backline-assassin",
    ("Ravion", "Evie"): "backline-assassin",
    ("Ravion", "Vala"): "assassin-delete",
    ("Ravion", "Pippa"): "backline-assassin",
    ("Ravion", "Nara"): "assassin-delete",
    ("Himmel", "Ravion"): "phys-backline-assassin",
    ("Himmel", "Nerion"): "backline-assassin",
    ("Himmel", "Athalia"): "phys-backline-assassin",
    ("Evie", "Bonnie"): "backline-inhibit",
    ("Evie", "Pippa"): "backline-assassin",
    ("Nerion", "Bonnie"): "backline-inhibit",
    ("Gwyneth", "Ravion"): "backline-assassin",
    ("Pippa", "Ravion"): "backline-assassin",
    ("Lumont", "Pippa"): "enemy-grouping",
    ("Lumont", "Eironn"): "enemy-grouping",
    ("Eironn", "Lumont"): "enemy-grouping",
    ("Thador", "Hugin"): "energy-provider",
    ("Thador", "Rowan"): "energy-provider",
    ("Hugin", "Rowan"): "energy-provider",
}


def load_csv() -> dict[str, dict[str, str]]:
    if not CSV_PATH.is_file():
        return {}
    with CSV_PATH.open(encoding="utf-8", newline="") as fh:
        return {row["Name"]: dict(row) for row in csv.DictReader(fh)}


def load_tags() -> dict[str, list[str]]:
    return json.loads(TAGS_PATH.read_text(encoding="utf-8"))


def combo_for_hero(hero: str, tags: dict[str, list[str]], rows: dict) -> str | None:
    hero_tags = tags.get(hero, [])
    row = rows.get(hero, {})
    if "backline-assassin" in hero_tags:
        magic = bool((row.get("Magic DMG") or "").strip())
        phys = bool((row.get("Physical DMG") or "").strip())
        true = bool((row.get("True DMG") or "").strip())
        if true and not magic and not phys:
            return "true-dmg-backline-assassin"
        if magic and not phys:
            return "magic-backline-assassin"
        if phys and not magic:
            return "phys-backline-assassin"
        return "backline-assassin"
    if "backline-inhibit" in hero_tags:
        magic = bool((row.get("Magic DMG") or "").strip())
        phys = bool((row.get("Physical DMG") or "").strip())
        if magic and not phys:
            return "magic-backline-inhibit"
        if phys and not magic:
            return "phys-backline-inhibit"
        return "backline-inhibit"
    if "assassin" in hero_tags:
        return "assassin"
    if hero in ENERGY and "energy-provider" in hero_tags:
        return "energy-provider"
    if "enemy-grouping" in hero_tags:
        return "enemy-grouping"
    return None


def combo_for_group(heroes: tuple[str, ...]) -> str | None:
    key = tuple(sorted(heroes))
    for pattern, combo in EXPLICIT_COMBOS.items():
        if tuple(sorted(pattern)) == key:
            return combo
    if all(h in ENERGY for h in heroes):
        return "energy-provider"
    if all(h in LASTING for h in heroes) and len(heroes) >= 2:
        return None  # unlinked lasting phrase
    return None


def wrap_group(text: str, heroes: list[str], combo: str) -> str:
    if FILTER_RE.search(text):
        return text
    old = " or ".join(f"[[{h}]]" for h in heroes[:-1])
    if len(heroes) > 1:
        old = ", ".join(f"[[{h}]]" for h in heroes[:-1]) + f", or [[{heroes[-1]}]]"
    else:
        old = f"[[{heroes[0]}]]"
    new = f"[[filter:{combo}]] like {old}"
    if old not in text:
        # try simple or chain
        old = " or ".join(f"[[{h}]]" for h in heroes)
        new = f"[[filter:{combo}]] like {old}"
    return text.replace(old, new, 1)


def lasting_phrase(text: str) -> str:
    patterns = [
        (
            r"lasting \[\[Shemira\]\] or \[\[Frieren\]\] coverage",
            "lasting wide ultimates like [[Shemira]] or [[Frieren]]",
        ),
        (
            r"lasting \[\[Shemira\]\] or \[\[Gwyneth\]\] coverage",
            "lasting wide ultimates like [[Shemira]] or [[Gwyneth]]",
        ),
        (
            r"lasting \[\[Shemira\]\] or \[\[Frieren\]\]",
            "lasting wide ultimates like [[Shemira]] or [[Frieren]]",
        ),
        (
            r"lasting \[\[Shemira\]\] or \[\[Gwyneth\]\]",
            "lasting wide ultimates like [[Shemira]] or [[Gwyneth]]",
        ),
        (
            r"lasting \[\[Gwyneth\]\] or \[\[Shemira\]\]",
            "lasting wide ultimates like [[Gwyneth]] or [[Shemira]]",
        ),
        (
            r"lasting \[\[Shemira\]\] / \[\[Gwyneth\]\]",
            "lasting wide ultimates like [[Shemira]] or [[Gwyneth]]",
        ),
        (
            r"lasting \[\[Shemira\]\] / \[\[Frieren\]\]",
            "lasting wide ultimates like [[Shemira]] or [[Frieren]]",
        ),
        (
            r"long, wide ultimates from \[\[Shemira\]\] or \[\[Frieren\]\]",
            "lasting wide ultimates like [[Shemira]] or [[Frieren]]",
        ),
        (
            r"long, wide ultimates\*\* from \[\[Shemira\]\] or \[\[Frieren\]\]",
            "**lasting wide ultimates like [[Shemira]] or [[Frieren]]",
        ),
        (
            r"\[\[Shemira\]\]'s ghost barrage or \[\[Frieren\]\]'s rectangular channel",
            "lasting wide ultimates like [[Shemira]] or [[Frieren]]",
        ),
        (
            r"lasting \[\[Shemira\]\] or amp'd \[\[Frieren\]\]",
            "lasting wide ultimates like [[Shemira]] or amp'd [[Frieren]]",
        ),
        (
            r"lasting \[\[Shemira\]\] or amp\u2019d \[\[Frieren\]\]",
            "lasting wide ultimates like [[Shemira]] or amp'd [[Frieren]]",
        ),
    ]
    for pat, repl in patterns:
        text = re.sub(pat, repl, text)
    return text


def apply_or_chains(text: str, tags: dict, rows: dict) -> str:
    if "[[filter:" in text:
        # still process unwrapped chains
        pass
    pattern = re.compile(
        r"(\[\[[^\]]+\]\](?:\s*,\s*\[\[[^\]]+\]\])*(?:\s+or\s+\[\[[^\]]+\]\])+)"
    )

    def repl(match: re.Match[str]) -> str:
        chunk = match.group(1)
        if "[[filter:" in chunk:
            return chunk
        # skip if already prefixed
        start = match.start()
        prefix = text[max(0, start - 40) : start]
        if "[[filter:" in prefix and "like" in prefix:
            return chunk
        heroes = [
            h for h in HERO_RE.findall(chunk) if not h.startswith("filter:")
        ]
        if len(heroes) < 2:
            return chunk
        if all(h in LASTING for h in heroes):
            return chunk
        combo = combo_for_group(tuple(heroes))
        if not combo:
            return chunk
        return f"[[filter:{combo}]] like {chunk}"

    return pattern.sub(repl, text)


def apply_energy_triple(text: str) -> str:
    replacements = [
        (
            "[[Thador]], [[Hugin]], or [[Rowan]]",
            "[[filter:energy-provider]] like [[Thador]], [[Hugin]], or [[Rowan]]",
        ),
        (
            "([[Thador]], [[Hugin]], [[Rowan]])",
            "([[filter:energy-provider]] like [[Thador]], [[Hugin]], or [[Rowan]])",
        ),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def apply_singleton_deletes(text: str, tags: dict, rows: dict) -> str:
    """Wrap lone counter picks in delete/inhibit clauses when a combo fits."""
    if "[[filter:" in text:
        pass
    triggers = [
        r"\bdelete [^.\n]*?\[\[([^\]]+)\]\]",
        r"\bDelete [^.\n]*?\[\[([^\]]+)\]\]",
        r"\bKill [^.\n]*?\[\[([^\]]+)\]\]",
        r"\bkill [^.\n]*?\[\[([^\]]+)\]\]",
        r"\bBurst [^.\n]*?\[\[([^\]]+)\]\]",
        r"\bFinish [^.\n]*?\[\[([^\]]+)\]\]",
    ]
    for trig in triggers:
        for match in re.finditer(trig, text):
            hero = match.group(1)
            if hero.startswith("filter:") or " or " in match.group(0):
                continue
            if hero in ("Lily May", "Dunlingr", "Callan", "Hewynn", "Niru", "Bryon"):
                continue
            combo = combo_for_hero(hero, tags, rows)
            if not combo:
                continue
            old = f"[[{hero}]]"
            new = f"[[filter:{combo}]] like [[{hero}]]"
            # only replace within this match span once
            start, end = match.span()
            segment = text[start:end]
            if "[[filter:" in segment:
                continue
            if old in segment and new not in segment:
                text = text[:start] + segment.replace(old, new, 1) + text[end:]
                break
    return text


def transform_text(text: str, tags: dict, rows: dict) -> str:
    text = lasting_phrase(text)
    text = apply_energy_triple(text)
    text = apply_or_chains(text, tags, rows)
    # Bonnie / inhibit phrasing
    text = text.replace(
        "Aging-inhibit with [[Bonnie]]",
        "[[filter:backline-inhibit]] like [[Bonnie]]",
    )
    text = text.replace(
        "Aging-inhibit that slot with [[Bonnie]]",
        "[[filter:backline-inhibit]] like [[Bonnie]]",
    )
    text = text.replace(
        "[[Bonnie]]'s Aging inhibit",
        "[[filter:backline-inhibit]] like [[Bonnie]]'s Aging inhibit",
    )
    text = text.replace(
        "[[Mehira]]'s fast pull",
        "[[filter:enemy-grouping]] like [[Mehira]]'s fast pull",
    )
    return text


def main() -> None:
    tags = load_tags()
    rows = load_csv()
    data = json.loads(COUNTER_PATH.read_text(encoding="utf-8"))
    updated = {
        hero: transform_text(text, tags, rows) for hero, text in data.items()
    }
    COUNTER_PATH.write_text(
        json.dumps(updated, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Updated {len(updated)} entries in {COUNTER_PATH.name}")


if __name__ == "__main__":
    main()
