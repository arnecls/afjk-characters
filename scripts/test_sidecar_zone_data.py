"""Read-back checks for buff zone sidecar data.

Covers zone_anchor on ally buff effects in ai.json, distinct_allies on
special_requires entries, and typed battlefield_position overrides.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

HEROES = Path(__file__).resolve().parent.parent / "data" / "heroes"


def _load(hero: str, name: str) -> dict:
    path = HEROES / hero / name
    return json.loads(path.read_text(encoding="utf-8"))


def _effects(hero: str):
    skills = _load(hero, "ai.json")["skill_effects"]["skills"]
    for skill, sdata in skills.items():
        for tier, tdata in sdata["tiers"].items():
            for effect in tdata.get("effects", []):
                yield skill, tier, effect


def _anchored(hero: str) -> dict[tuple[str, str], str]:
    """Map (skill, buff name) to the zone anchor for anchored effects."""
    out: dict[tuple[str, str], set[str]] = {}
    for skill, _tier, effect in _effects(hero):
        if "zone_anchor" in effect:
            key = (skill, effect["name"])
            out.setdefault(key, set()).add(effect["zone_anchor"])
    for key, anchors in out.items():
        assert len(anchors) == 1, (hero, key, anchors)
    return {k: next(iter(v)) for k, v in out.items()}


ANCHORS = {
    "estrilda": (
        "enemy_backline",
        {("Ex. Skill", "ATK"), ("Ex. Skill", "Damage taken")},
    ),
    "kordan": (
        "enemy_target",
        {
            ("Ultimate", "Lifedrain"),
            ("Ultimate", "ATK"),
            ("Ultimate", "Damage dealt"),
            ("Unlocks at Supreme+", "DEF Penetration"),
        },
    ),
    "shakir": (
        "caster",
        {("Ultimate", "Haste"), ("Ultimate", "Damage taken")},
    ),
    "mikola": (
        "caster",
        {("Ultimate", "Haste"), ("Ultimate", "Ranged DEF")},
    ),
    "perseus": (
        "caster",
        {("Skill2", "ATK"), ("Skill2", "Phys DEF"), ("Skill2", "Magic DEF")},
    ),
    "smokey-meerky": (
        "caster",
        {("Skill1", "ATK"), ("Ultimate", "Haste")},
    ),
    "peggy": ("summon", {("Ex. Skill", "Damage dealt")}),
    "damian": ("summon", {("Ex. Skill", "Haste")}),
    "hugin": ("fixed_tile", {("Skill2", "ATK")}),
}


@pytest.mark.parametrize("hero", sorted(ANCHORS))
def test_zone_anchor(hero: str) -> None:
    anchor, keys = ANCHORS[hero]
    assert _anchored(hero) == {key: anchor for key in keys}


def test_zone_anchor_only_on_ally_buffs() -> None:
    for hero in ANCHORS:
        for _skill, _tier, effect in _effects(hero):
            if "zone_anchor" in effect:
                assert effect["target"] == "ally"
                assert effect["type"] == "buff"


def test_global_buffs_have_no_anchor() -> None:
    # Mikola Honor Arena ATK is the Skill1 zone buff, not the Sphere.
    for _skill, _tier, effect in _effects("mikola"):
        if _skill == "Skill1":
            assert "zone_anchor" not in effect
    for hero in ("kazim", "kulu"):
        for _skill, _tier, effect in _effects(hero):
            assert "zone_anchor" not in effect


@pytest.mark.parametrize("hero", ["perseus", "orion"])
def test_distinct_allies(hero: str) -> None:
    skills = _load(hero, "ai.json")["skill_effects"]["skills"]
    found = []
    for sdata in skills.values():
        for tdata in sdata["tiers"].values():
            for req in tdata.get("special_requires", []):
                if req["label"] == "Temporary ally stat buffs":
                    found.append(req)
    assert found
    expected = [
        req for req in found if req.get("distinct_allies") == 2
    ]
    if hero == "perseus":
        assert [r["tier"] for r in expected] == ["mythic+"]
    else:
        assert len(expected) == len(found)


POSITIONS = {
    "frontline": [
        "seth", "kordan", "soren", "gerda", "chippy", "himmel", "kafra",
        "lenya", "sinbad",
    ],
    "ally_backline": ["nara", "niru", "lily-may"],
    "roaming": ["temesia", "igor", "berial", "harak"],
}


@pytest.mark.parametrize(
    ("hero", "position"),
    [(h, p) for p, heroes in POSITIONS.items() for h in heroes],
)
def test_battlefield_position(hero: str, position: str) -> None:
    data = _load(hero, "overrides.json")
    assert data["schema_version"] == 1
    assert data["battlefield_position"] == position
