#!/usr/bin/env python3
"""Refresh generated source hashes after the per-hero migration."""

from __future__ import annotations

import copy

import heroes_io as io
import skill_effects_store as sidecars
from hero_pipeline.storage import (
    canonical_hash,
    load_bundles,
    load_manifest,
    write_json_atomic,
)


def main() -> None:
    manifest = load_manifest()
    bundles = load_bundles(manifest)
    raw = io.load_heroes_data()
    by_title = {hero["title"]: hero for hero in raw["heroes"]}
    changed = 0
    for entry in manifest["heroes"]:
        hero_id = entry["id"]
        bundle = bundles[hero_id]
        source = by_title[entry["title"]]
        ai = copy.deepcopy(bundle["ai"])
        doc = ai.get("skill_effects")
        if doc:
            for section, skill_doc in doc.get("skills", {}).items():
                skill = next(
                    skill
                    for skill in source["skills"]
                    if skill["section"] == section
                )
                expected = sidecars.compute_skill_source_hash(skill)
                if skill_doc.get("source_hash") != expected:
                    skill_doc["source_hash"] = expected
                    changed += 1
            write_json_atomic(
                (
                    sidecars.DATA
                    / "heroes"
                    / hero_id
                    / "ai.json"
                ),
                ai,
            )
        generated = copy.deepcopy(bundle["generated"])
        provenance = generated.setdefault("provenance", {})
        provenance["source_hash"] = canonical_hash(
            generated.get("source")
        )
        provenance["ai_hash"] = canonical_hash(ai)
        provenance["overrides_hash"] = canonical_hash(
            bundle["overrides"]
        )
        provenance["analysis_inputs_hash"] = canonical_hash(
            {
                "source": generated.get("source"),
                "ai": ai,
                "overrides": bundle["overrides"],
            }
        )
        write_json_atomic(
            sidecars.DATA / "heroes" / hero_id / "generated.json",
            generated,
        )
    print(f"Refreshed {changed} skill source hashes")


if __name__ == "__main__":
    main()
