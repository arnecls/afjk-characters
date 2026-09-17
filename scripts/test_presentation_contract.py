"""Tests for the frozen hero-split presentation contract."""

from __future__ import annotations

import json
import unittest

from effect_labels import build_list_columns
from hero_pipeline.analysis.policy import make_policy
from hero_pipeline.parity import (
    compare_contracts,
    compare_view_artifacts,
    contract_from_view,
    load_contract,
    load_fixture_artifacts,
    relationship_invariant_errors,
    site_without_timestamp,
)
from hero_pipeline.pipeline import score
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.render.markdown import render_heroes
from hero_pipeline.render.overview import render_overview
from hero_pipeline.render.site import render_site_outputs
from hero_pipeline.storage import load_config


class PresentationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baseline = load_contract()
        cls.artifacts = load_fixture_artifacts()
        config = load_config()
        processed, relationships, snapshot = score()
        cls.view = project_roster(
            snapshot,
            policy=make_policy(config),
            config=config,
            analyses=processed["heroes"],
            relationships=relationships,
        )
        heroes_md = render_heroes(cls.view)
        overview_md, overview_csv = render_overview(cls.view)
        from hero_pipeline.repository import current_repository

        site_outputs = render_site_outputs(cls.view, generated_at="fixture")
        cls.current = contract_from_view(
            cls.view,
            heroes_md=heroes_md,
            overview_md=overview_md,
            overview_csv=overview_csv,
            site_heroes=site_outputs["heroes"],
        )
        counter_path = current_repository().data / "counter_filter_combos.json"
        cls.current_artifacts = {
            "heroes_md": heroes_md,
            "overview_md": overview_md,
            "overview_csv": overview_csv,
            "site_heroes": site_without_timestamp(site_outputs["heroes"]),
            "site_csv": overview_csv.replace("\r\n", "\n"),
            "mix_synergy_index": site_outputs["mix_synergy_index"],
            "mix_config": site_outputs["mix_config"],
            "mix_role_prominence": site_outputs["mix_role_prominence"],
            "list_columns": build_list_columns(),
            "counter_filter_combos": (
                json.loads(counter_path.read_text(encoding="utf-8"))
                if counter_path.is_file()
                else {}
            ),
        }

    def test_contract_matches_frozen_hero_split(self) -> None:
        errors = compare_contracts(self.baseline, self.current)
        self.assertEqual(errors[:20], [], errors[:20])

    def test_public_artifacts_match_frozen_hero_split(self) -> None:
        errors = compare_view_artifacts(
            self.artifacts,
            self.current_artifacts,
        )
        self.assertEqual(errors[:20], [], errors[:20])

    def test_relationship_invariants(self) -> None:
        errors = relationship_invariant_errors(self.view)
        self.assertEqual(errors, [])

    def test_condition_and_soul_pact_contract_clusters(self) -> None:
        by_id = {hero["id"]: hero for hero in self.current["heroes"]}
        arden = by_id["arden"]
        storm = arden["analysis"]["skills"]["Spring Thunderstorm"]["effects"][0]
        self.assertEqual(
            {c.get("type") for c in storm["conditions"]},
            {"status_condition"},
        )
        natsu = by_id["natsu"]
        roar = natsu["analysis"]["skills"][
            "Lightning Fire Dragon's Roar/Fire Dragon King's Roar"
        ]["effects"][1]
        self.assertEqual(
            [c.get("mode") for c in roar["conditions"]],
            ["lightning_fire_dragon", "fire_dragon_king"],
        )
        vala = by_id["vala"]
        checkmate = vala["analysis"]["skills"]["Checkmate"]["effects"][1]
        self.assertEqual(
            [c.get("mode") for c in checkmate["conditions"]],
            ["skyblaster", "sword"],
        )
        viperian = by_id["viperian"]
        fang = viperian["analysis"]["skills"]["Enchantment Fang"]["effects"][0]
        self.assertEqual(fang["conditions"][0]["type"], "duration_gate")
        self.assertEqual(fang["conditions"][0]["interval"], 3.0)
        thoran = by_id["thoran"]
        heals = [
            effect
            for effect in thoran["analysis"]["skills"]["Soul Pact"]["effects"]
            if effect.get("type") == "heal"
        ]
        self.assertEqual(len(heals), 1, heals)
        self.assertEqual(heals[0]["value"][0]["value"], 35)
        self.assertEqual(heals[0]["tier"], "ex+5")
        energy_idx = [
            index
            for index, effect in enumerate(thoran["display"]["effects"])
            if effect.get("label") == "Energy"
        ]
        self.assertEqual(energy_idx, [5])
        self.assertEqual(
            thoran["analysis"]["summary_effect_magnitudes"]["effects"][5],
            "low",
        )
        self.assertEqual(thoran["display"]["effects"][5]["magnitude"], "low")

    def test_sinbad_debuff_replacements_keep_cassadee(self) -> None:
        sinbad = next(
            hero
            for hero in self.current_artifacts["site_heroes"]["heroes"]
            if hero["slug"] == "sinbad"
        )
        debuffs = next(
            row
            for row in sinbad["sections"]["replacements"]
            if row["category"] == "Debuffs on enemies"
        )
        slugs = [entry["slug"] for entry in debuffs["entries"]]
        self.assertEqual(slugs, ["cassadee", "shadewing", "evie"])
        self.assertEqual(debuffs["entries"][0]["score"], 0.5486)
