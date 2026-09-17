"""Shared helpers for skill-card tag assertions in tests."""

from __future__ import annotations

import types


def load_rewrite_summaries():
    """Return the combined effect/behavior analysis namespace used by tests."""
    from hero_pipeline.analysis import behavior, effects

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
    return namespace


def load_overview_facts(name: str = "gen_overview"):
    """Return analysis-fact helpers used by focused scoring tests."""
    from hero_pipeline.analysis import scoring_facts

    return scoring_facts


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
