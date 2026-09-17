"""Tests for the frozen hero-split presentation contract."""

from __future__ import annotations

import unittest

from hero_pipeline.analysis.policy import make_policy
from hero_pipeline.parity import (
    compare_contracts,
    contract_from_view,
    load_contract,
    relationship_invariant_errors,
)
from hero_pipeline.pipeline import score
from hero_pipeline.presentation.project import project_roster
from hero_pipeline.render.markdown import render_heroes
from hero_pipeline.render.overview import render_overview
from hero_pipeline.render.site import render_site_data
from hero_pipeline.storage import load_config


class PresentationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baseline = load_contract()
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
        cls.current = contract_from_view(
            cls.view,
            heroes_md=heroes_md,
            overview_md=overview_md,
            overview_csv=overview_csv,
            site_heroes=render_site_data(cls.view, generated_at="fixture"),
        )

    def test_contract_matches_frozen_hero_split(self) -> None:
        errors = compare_contracts(self.baseline, self.current)
        self.assertEqual(errors[:20], [], errors[:20])

    def test_relationship_invariants(self) -> None:
        errors = relationship_invariant_errors(self.view)
        self.assertEqual(errors, [])
