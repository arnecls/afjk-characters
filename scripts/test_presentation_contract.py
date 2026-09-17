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
    list_column_semantics,
    load_contract,
    load_fixture_artifacts,
    normalize_text,
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
            "heroes_md": normalize_text(heroes_md),
            "overview_md": normalize_text(overview_md),
            "overview_csv": normalize_text(overview_csv),
            "site_heroes": site_without_timestamp(site_outputs["heroes"]),
            "site_csv": normalize_text(overview_csv),
            "mix_synergy_index": site_outputs["mix_synergy_index"],
            "mix_config": site_outputs["mix_config"],
            "mix_role_prominence": site_outputs["mix_role_prominence"],
            "list_columns": list_column_semantics(build_list_columns()),
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
