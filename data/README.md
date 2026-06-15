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
| [heroes_data_skill_summary.json](heroes_data_skill_summary.json) | **AI-generated** | Short mechanic summary per hero and skill category (`ultimate`, `skill1`–`skill5`). Joined to processed skills by `category`; shown in Skill overview subsections. |
| [hero_play_overviews.json](hero_play_overviews.json) | **AI-generated** | Short playstyle summary per hero (3–5 sentences, ~900 chars max), sourced from Prydwen character reviews. Shown in the behavior section before Skill overview. Regenerate with `python3 scripts/generate_play_overviews.py`. |
| [placement_constraint_overrides.json](placement_constraint_overrides.json) | **Manual configuration** | Optional overrides when placement/composition rules cannot be parsed from skill text. |
| [movement_overrides.json](movement_overrides.json) | **Manual configuration** | Optional per-hero movement labels when automatic detection is wrong. |
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
- **`schema/`** — contract for processed JSON and allowed behavior-tag values.
  Update when adding new effect labels, tags, or processed fields.

## Pipeline flow

```
heroes_data.json
    + heroes_config.json
    + signature_skills.json
    + hero_behavior_tags.json
    + placement_constraint_overrides.json
        ↓  just analyze
heroes_data_processed.json
heroes_data_synergies.json
        ↓  just render
    + heroes_data_skill_summary.json
    + hero_play_overviews.json
Heroes.md · heroes-overview.md · heroes-overview.csv
```
