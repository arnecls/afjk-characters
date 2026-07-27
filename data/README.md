# Data directory

JSON inputs and outputs for the hero pipeline (`just download` → `just analyze` →
`just render`). See the root [README.md](../README.md) for the full workflow.

## File overview

| File | Category | Notes |
| --- | --- | --- |
| [heroes_data.json](heroes_data.json) | **Script-generated** | Merged roster from the Fandom wiki (baseline), Yaphalla (gap-fill), and Prydwen meta tiers. Each hero may include `prydwen_tiers` with `afk_stages`, `dream_realm`, `dream_realm_endless`, and `pvp` ratings. Regenerate with `just download`. Committed as the canonical skill source when offline. |
| [heroes_data_processed.json](heroes_data_processed.json) | **Script-generated** | Per-hero analysis: effects, behavior, synergy profile, magnitudes. Regenerate with `just analyze` (or `just views`). Do not edit by hand. |
| [heroes_data_synergies.json](heroes_data_synergies.json) | **Script-generated** | Roster-wide synergy rankings, beneficiaries, and replacements. Regenerate with `just analyze` or `just analyze-synergies`. Do not edit by hand. |
| [signature_skills.json](signature_skills.json) | **AI-generated** | Signature skill per hero by category (`signature_calculated`, optional `signature_override`, optional `speed_override`). Skill names come from `heroes_data.json`; edit when a hero’s identity skill is wrong. |
| [hero_behavior_tags.json](hero_behavior_tags.json) | **AI-generated** | Combat-role tags per hero for replacement scoring. |
| [hero_walk_speeds.json](hero_walk_speeds.json) | **Curated ()** | Base `Unit.WalkSpeed` tier per hero (`zero`/`slow`/`normal`/`fast`/`veryfast`). Keys match overview display names. |
| [heroes_data_skill_summary.json](heroes_data_skill_summary.json) | **AI-generated** | Short mechanic summary per hero and skill category (`ultimate`, `skill1`–`skill5`). Joined to processed skills by `category`; shown in Skill overview subsections. |
| [hero_play_overviews.json](hero_play_overviews.json) | **AI-generated** | Short playstyle summary per hero (4–6 sentences, ~900 chars max). Focuses on setup requirements, strengths, and weaknesses; uses **bold** for key phrases. Shown in the behavior section before Skill overview. |
| [placement_constraint_overrides.json](placement_constraint_overrides.json) | **Manual configuration** | Optional overrides when placement/composition rules cannot be parsed from skill text. |
| [movement_overrides.json](movement_overrides.json) | **Manual configuration** | Optional per-hero movement labels when automatic detection is wrong. |
| [melee_overrides.json](melee_overrides.json) | **Manual configuration** | Optional `is_melee` / `is_dual_range` flags when melee-floor or range weighting is wrong. |
| [heroes_config.json](heroes_config.json) | **Manual configuration** | Tunables: synergy weights, display limits, casting-speed thresholds, replacement scoring, proximity-aura reach (`proximity_synergy`). |
| [schema/](schema/) | **Manual configuration** | JSON Schema definitions used to validate processed data and tag enums. |

## Script-generated files

These are overwritten by the pipeline. Changes made directly in the files will
be lost on the next run.

```
just download          →  heroes_data.json
just analyze           →  heroes_data_processed.json
                         heroes_data_synergies.json
```

`heroes_data.json` is the only script-generated file that is normally committed
and reused without re-downloading (`just views` skips the download step).

## AI-generated files

These are **source data**, not pipeline outputs. They were produced with AI
assistance and are kept in git so behavior, signature skills, and replacement
tags stay stable across regenerations. Update them when roster logic changes or
a hero’s curated metadata is wrong — the analyze step reads them but never
rewrites them.

Keys use the hero **display name** from [heroes-overview.md](../heroes-overview.md)
(e.g. `Galahad`, `Twins`).

## Manual configuration

Edit these when tuning scoring, fixing edge cases, or extending validation:

- **`heroes_config.json`** — synergy/display/behavior/replacement parameters
  loaded by `process_config.py`. The `proximity_synergy` block sets
  `melee_max_range`, default aura radius, range slack, and optional
  receiver/provider overrides for local aura buff matching.
- **`placement_constraint_overrides.json`** — map display name → list of
  `{kind, text}` placement constraints; bypasses text detection for that hero.
- **`movement_overrides.json`** — map display name → `{movement, note}` when
  automatic movement detection is wrong.
- **`hero_walk_speeds.json`** — map display name → base walk-speed tier from
  game data (`afkj-data/docs/walking_speed.md`). Required for every roster
  hero; missing keys fail validation.
- **`melee_overrides.json`** — map display name → `{is_melee}` and/or
  `{is_dual_range}` for melee-floor and weighted-range edge cases.
- **`schema/`** — contract for processed JSON and allowed behavior-tag values.
  Update when adding new effect labels, tags, or processed fields.

## Pipeline flow

```
heroes_data.json
    + heroes_config.json
    + signature_skills.json
    + hero_behavior_tags.json
    + hero_walk_speeds.json
    + placement_constraint_overrides.json
    + movement_overrides.json
    + melee_overrides.json
        ↓  just analyze  (process_heroes.py → process_synergies.py)
heroes_data_processed.json
heroes_data_synergies.json
        ↓  just render  (render_heroes.py · render_overview.py · render_site.py)
    + heroes_data_skill_summary.json
    + hero_play_overviews.json
Heroes.md · heroes-overview.md · heroes-overview.csv · site/data/heroes.json
```

Ephemeral caches (gitignored): `prydwen_reviews_cache.json` (Prydwen review text for
`scripts/generate_play_overviews.py`), `.roster_analysis_cache.pkl` (speeds re-analysis).
