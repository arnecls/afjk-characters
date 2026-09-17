"""Shared helpers for skill-card tag assertions in tests."""

from __future__ import annotations

import types


def load_working_analysis():
    """Return detector and behavior helpers for working-analysis tests."""
    import json
    from pathlib import Path

    import skill_effects_store as ses
    from hero_pipeline.analysis import behavior, effects
    from hero_pipeline.analysis.skill_corrections import spec_from_overrides

    namespace = types.SimpleNamespace()
    namespace.__dict__.update(
        {key: value for key, value in effects.__dict__.items() if key != "__builtins__"}
    )
    namespace.__dict__.update(
        {
            key: value
            for key, value in behavior.__dict__.items()
            if key != "__builtins__"
        }
    )

    def analyze_hero(hero, sidecar=None):
        if sidecar is None:
            sidecar = ses.load_sidecar(hero["title"])
        if not hero.get("skill_corrections"):
            short = (
                hero["title"].split(" - ", 1)[0].strip().lower().replace(" ", "-")
            )
            override_path = (
                Path(__file__).resolve().parents[1]
                / "data"
                / "heroes"
                / short
                / "overrides.json"
            )
            if override_path.is_file():
                hero["skill_corrections"] = spec_from_overrides(
                    json.loads(override_path.read_text(encoding="utf-8"))
                )
        effects.analyze_working(hero, sidecar)

    namespace.analyze_hero = analyze_hero
    return namespace


def tag_labels(tags: list) -> list[str]:
    """Display labels from skill_card_tags (strings or {label, polarity?})."""
    out: list[str] = []
    for tag in tags:
        if isinstance(tag, dict):
            out.append(tag["label"])
        else:
            out.append(tag)
    return out


def tag_polarity(tag) -> str | None:
    if isinstance(tag, dict):
        return tag.get("polarity") or None
    return None


def tags_with_label(tags: list, label: str, *, polarity: str | None = None) -> list:
    matches = []
    for tag in tags:
        if isinstance(tag, dict):
            if tag.get("label") != label:
                continue
            if polarity is not None and tag.get("polarity") != polarity:
                continue
            matches.append(tag)
        elif tag == label or tag.startswith(label):
            if polarity is None:
                matches.append(tag)
    return matches


def assert_tag_in(test_case, label: str, tags: list, *, polarity: str | None = None):
    found = tags_with_label(tags, label, polarity=polarity)
    test_case.assertTrue(
        found,
        msg=f"{label!r} (polarity={polarity!r}) not in {tags!r}",
    )


def assert_tag_not_in(
    test_case, label: str, tags: list, *, polarity: str | None = None
):
    found = tags_with_label(tags, label, polarity=polarity)
    test_case.assertFalse(
        found,
        msg=f"{label!r} (polarity={polarity!r}) unexpectedly in {tags!r}",
    )
