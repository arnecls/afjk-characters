"""Typed per-hero skill post-process corrections."""

from __future__ import annotations

from typing import Any, Mapping

from .records import Effect


def spec_from_overrides(overrides: Mapping[str, Any] | None) -> dict[str, Any]:
    return dict((overrides or {}).get("corrections") or {})


def apply_skill_corrections(
    hero: dict[str, Any], spec: Mapping[str, Any] | None
) -> None:
    """Apply schema-defined slice corrections after sidecar post-processing."""
    post = (spec or {}).get("skill_postprocess") or {}
    if not post:
        return
    for row in post.get("relabel") or []:
        source = row.get("from")
        target = row.get("to")
        if not source or not target:
            continue
        for sl in hero["skill_slices"].values():
            for effect in sl["effects"]:
                if effect["label"] == source:
                    effect["label"] = target
    path_spec = post.get("force_section_path") or {}
    section = path_spec.get("section")
    if section:
        sl = hero["skill_slices"].get(section)
        if sl:
            categories = set(path_spec.get("categories") or ())
            for effect in sl["effects"]:
                if categories and effect["category"] not in categories:
                    continue
                effect["targeting"] = path_spec.get("targeting", effect["targeting"])
                effect["area"] = path_spec.get("area", effect["area"])
                effect["area_direction"] = path_spec.get(
                    "area_direction", effect["area_direction"]
                )
                if path_spec.get("area_count") is not None:
                    effect["area_count"] = path_spec["area_count"]
    copy_spec = post.get("copy_unique_effects") or {}
    source_section = copy_spec.get("from_section")
    dest_section = copy_spec.get("to_section")
    if source_section and dest_section:
        source = hero["skill_slices"].get(source_section)
        dest = hero["skill_slices"].get(dest_section)
        if source and dest:
            wanted = set(copy_spec.get("categories") or ())
            for effect in source["effects"]:
                if wanted and effect["category"] not in wanted:
                    continue
                if any(
                    row["category"] == effect["category"]
                    and row["label"] == effect["label"]
                    and row["tier"] == effect["tier"]
                    for row in dest["effects"]
                ):
                    continue
                dest["effects"].append(
                    Effect(
                        category=effect["category"],
                        label=effect["label"],
                        tier=effect["tier"],
                        targeting=effect["targeting"],
                        area=effect["area"],
                        area_direction=effect["area_direction"],
                        area_count=effect["area_count"],
                        numeric=effect["numeric"],
                        conditions=list(effect["conditions"]),
                    )
                )
    drop_spec = post.get("drop_effects") or {}
    drop_category = drop_spec.get("category")
    drop_label = drop_spec.get("label")
    for section_name in drop_spec.get("sections") or []:
        sl = hero["skill_slices"].get(section_name)
        if not sl:
            continue
        sl["effects"] = [
            effect
            for effect in sl["effects"]
            if not (
                effect["category"] == drop_category
                and effect["label"] == drop_label
            )
        ]
