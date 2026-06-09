#!/usr/bin/env python3
"""Process heroes_data.json into heroes_data_processed.json.

This is the analysis step. It reconstructs the Yaphalla / fandom documents from
``heroes_data.json`` and runs the existing (unchanged) synergy/summary/behaviour
analysis, then serialises only the *derived* data — effects, special effects,
crowd control, damage magnitudes, behaviour, full synergy rankings and the
beneficiary index. Nothing already present in ``heroes_data.json`` (skill text,
identity) is duplicated here.

Static weights and thresholds are loaded from ``heroes_config.json`` and applied
to the analysis modules, so all tuning lives in one place.
"""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import asdict
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import hero_schema as hs


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


rs = _load_module("rewrite_summaries", "rewrite-summaries.py")
gen = _load_module("gen_overview", "generate-heroes-overview.py")


def apply_config(config: dict) -> None:
    """Push configurable weights/thresholds onto the analysis modules."""
    sw = config.get("synergy_weights", {})
    for key, attr in [
        ("targeting_weight", "TARGETING_WEIGHT"),
        ("mag_weight", "MAG_WEIGHT"),
        ("summon_targeting_weight", "SUMMON_TARGETING_WEIGHT"),
        ("haste_for_atk_spd_score_mult", "HASTE_FOR_ATK_SPD_SCORE_MULT"),
        ("frequent_conditional_score", "FREQUENT_CONDITIONAL_SCORE"),
        ("signature_fuel_speed_mult", "SIGNATURE_FUEL_SPEED_MULT"),
        ("signature_fuel_energy_mult", "SIGNATURE_FUEL_ENERGY_MULT"),
        ("energy_synergy_score_mult", "ENERGY_SYNERGY_SCORE_MULT"),
        ("implicit_fuel_base", "IMPLICIT_FUEL_BASE"),
        ("early_battle_energy_ult_mult", "EARLY_BATTLE_ENERGY_ULT_MULT"),
        ("defining_tier_score_mult", "DEFINING_TIER_SCORE_MULT"),
    ]:
        if key in sw:
            setattr(gen, attr, sw[key])

    dl = config.get("display_limits", {})
    if "max_synergies" in dl:
        gen.MAX_SYNERGIES = dl["max_synergies"]
    if "max_beneficiaries_display" in dl:
        gen.MAX_BENEFICIARIES_DISPLAY = dl["max_beneficiaries_display"]

    bt = config.get("behavior_thresholds", {})
    for key, attr in [
        ("energy_fill_rate", "ENERGY_FILL_RATE"),
        ("ult_energy_capacity", "ULT_ENERGY_CAPACITY"),
        ("initial_cd_skill_weight", "INITIAL_CD_SKILL_WEIGHT"),
        ("initial_cd_cap", "INITIAL_CD_CAP"),
        ("casting_speed_fast_threshold", "CASTING_SPEED_FAST_THRESHOLD"),
        ("casting_speed_slow_threshold", "CASTING_SPEED_SLOW_THRESHOLD"),
    ]:
        if key in bt:
            setattr(rs, attr, bt[key])

    rs_cfg = config.get("replacement_scoring", {})
    if "min_score" in rs_cfg:
        gen.REPLACEMENT_MIN_SCORE = rs_cfg["min_score"]
    if "max_replacements" in rs_cfg:
        gen.REPLACEMENT_MAX = rs_cfg["max_replacements"]


def rank_synergies_full(receiver, heroes, enabler_matchers, behavior_by_title):
    """Like gen.rank_synergies but without the top-N display cap."""
    receiver_behavior = behavior_by_title[receiver.title]
    receiver_movement = receiver_behavior.movement
    signature_speed = receiver_behavior.synergy_signature_speed or "normal"
    ranked: list[tuple[float, list[str], str]] = []
    for provider in heroes:
        score, reasons = gen.score_combined_synergy(
            provider,
            receiver,
            enabler_matchers,
            receiver_behavior,
            receiver_movement,
            signature_speed,
        )
        if score <= 0 or not reasons:
            continue
        ranked.append((score, reasons, provider.title))

    ranked.sort(key=lambda x: (-x[0], x[2]))
    filtered = [
        entry
        for entry in ranked
        if not gen.should_exclude_synergy(entry[1], receiver)
    ]
    return [
        {"provider": title, "reasons": reasons, "score": score}
        for score, reasons, title in filtered
    ]


def build_processed(data: dict) -> dict:
    yaphalla_text = io.reconstruct_heroes_md(data)
    fandom_text = io.reconstruct_heroes2_md(data)

    import re

    blocks = [b for b in re.split(r"\n(?=## )", yaphalla_text) if b.startswith("## ")]
    heroes: list = []
    block_by_title: dict[str, str] = {}
    for block in blocks:
        hero = rs.parse_hero_block(block)
        heroes.append(hero)
        block_by_title[hero.title] = block

    hero_class_by_title: dict[str, str] = {}
    for hero in heroes:
        hero_class_by_title[hero.title] = gen._parse_hero_class(
            block_by_title[hero.title]
        )
        rs.analyze_hero(hero)

    rs.assign_magnitudes(heroes)
    enabler_matchers = gen._make_enabler_matchers(hero_class_by_title)

    display_by_title = {h.title: gen.short_name(h.title) for h in heroes}
    behavior_by_title = rs.build_behavior_for_heroes(
        heroes,
        display_by_title,
        heroes2_text=fandom_text,
        heroes_text=yaphalla_text,
    )
    beneficiaries_index = gen.build_beneficiaries_index(
        heroes, enabler_matchers, behavior_by_title
    )
    replacements_index = gen.compute_replacement_scores(
        heroes, behavior_by_title, hero_class_by_title
    )

    # Match overview-to-csv: energy providers are detected from freshly parsed
    # (un-analyzed) hero blocks, so only the battle-start text path counts.
    energy_provider_titles = {
        hero.title
        for hero in (rs.parse_hero_block(b) for b in blocks)
        if gen.is_energy_provider(hero)
    }

    data_by_title = {h["title"]: h for h in data["heroes"]}
    processed_heroes: dict[str, dict] = {}
    for hero in heroes:
        behavior = behavior_by_title[hero.title]
        synergies = rank_synergies_full(
            hero, heroes, enabler_matchers, behavior_by_title
        )
        benefited = beneficiaries_index.get(hero.title, [])
        hero_record = data_by_title[hero.title]
        processed_heroes[hero.title] = hs.serialize_processed_hero(
            hero,
            hero_record,
            is_supporting_unit=gen.is_supporting_unit(
                hero, hero_class_by_title.get(hero.title, "")
            ),
            is_energy_provider=hero.title in energy_provider_titles,
            behavior=asdict(behavior),
            synergies=synergies,
            beneficiaries=[
                {"score": score, "name": name} for score, name in benefited
            ],
            beneficiary_overflow_reasons=gen._beneficiary_overflow_reasons(hero),
            replacements=replacements_index.get(hero.title, {}),
        )

    result = {"heroes": processed_heroes}
    try:
        hs.validate_processed(result)
    except RuntimeError as exc:
        print(f"Warning: {exc}", file=sys.stderr)
    except Exception as exc:
        if type(exc).__name__ == "ValidationError":
            print(f"Warning: schema validation failed: {exc}", file=sys.stderr)
        else:
            raise
    return result


def main() -> None:
    config = io.load_config()
    apply_config(config)
    raw = io.load_heroes_data()
    processed = build_processed(raw)
    io.save_json(io.HEROES_DATA_PROCESSED, processed)
    print(
        f"Wrote {io.HEROES_DATA_PROCESSED.relative_to(io.ROOT)} "
        f"({len(processed['heroes'])} heroes, "
        f"{sum(1 for p in processed['heroes'].values() if p['is_energy_provider'])} energy providers)"
    )


if __name__ == "__main__":
    main()
