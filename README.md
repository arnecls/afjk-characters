# AFK Journey Hero Reference

**Start here: [heroes-overview.md](heroes-overview.md)** — per-hero synergies, combat
behavior, structured skill summaries, and replacement suggestions for the full
roster.

This repository collects and analyzes hero skill data for [AFK Journey](https://afk-journey.fandom.com/wiki/AFK_Journey). Skill text is sourced primarily from the [AFK Journey Fandom wiki](https://afk-journey.fandom.com/wiki/Hero/List), with gaps filled from [Yaphalla](https://www.yaphalla.com/heroes), then parsed to extract buffs, debuffs, crowd control, damage types, and team synergies.

## What is in this repository

| File / folder | Purpose |
| --- | --- |
| **[heroes-overview.md](heroes-overview.md)** | Main reference: synergy partners, behavior, and parsed summaries per hero |
| **[heroes-overview.csv](heroes-overview.csv)** | Same roster data in spreadsheet form (damage, CC, buffs, movement, etc.) |
| **[Heroes.md](Heroes.md)** | Raw skill descriptions only — no summaries |
| **`data/`** | Canonical JSON (`heroes_data.json`) plus processed analysis and JSON schemas |
| **`scripts/`** | Python pipeline: download, analyze, validate, and render views |
| **[`.cursor/AGENTS.md`](.cursor/AGENTS.md)** | Detailed rules for parsing skills, scoring synergies, and editing summaries |

### What each hero entry contains

Each section in [heroes-overview.md](heroes-overview.md) includes:

- **Behavior** — movement pattern, signature skill, casting speed, placement constraints
- **Units X benefits from** — up to five ranked synergy partners (stat buffs, enablers, summon support)
- **Units benefitting most from X** — reverse index of heroes who synergize with this unit
- **Replacements** — similar heroes grouped by role (damage, crowd control, buffs, etc.)
- **Summary** — structured breakdown of stats benefited, damage types, buffs, debuffs, crowd control, and special effects

Magnitude labels (`high`, `medium`, `low`) rank an effect against the full roster, not in isolation. See [`.cursor/AGENTS.md`](.cursor/AGENTS.md) for the full taxonomy.

## How to use it

### Browse the reference

Open [heroes-overview.md](heroes-overview.md) and jump to a hero by name. Use your editor's outline or search (`Ctrl/Cmd+F`) to navigate.

For filtering or pivot tables, open [heroes-overview.csv](heroes-overview.csv) in a spreadsheet application.

For verbatim skill wording (levels, cooldowns, unlock tiers), see [Heroes.md](Heroes.md).

### Regenerate the views

The committed JSON in `data/heroes_data.json` is the source of truth. Views are rebuilt from it with [just](https://github.com/casey/just) (or the equivalent Python commands).

**One-time setup:**

```bash
just setup
```

**Regenerate from committed data (no network):**

```bash
just views
```

This runs analysis (`data/heroes_data_processed.json`, `data/heroes_data_synergies.json`) and renders `Heroes.md`, `heroes-overview.md`, and `heroes-overview.csv`.

**Full refresh from live sources (requires network):**

```bash
just all
```

Downloads merged data from Yaphalla and the Fandom wiki, then runs the full pipeline.

**Validate processed data against schemas and parity checks:**

```bash
just validate
```

Run `just` (or `just --list`) to see all available recipes.

### Pipeline overview

```
download  →  data/heroes_data.json
analyze   →  data/heroes_data_processed.json
             data/heroes_data_synergies.json
render    →  Heroes.md
             heroes-overview.md
             heroes-overview.csv
```

Configuration for synergy scoring and display limits lives in `data/heroes_config.json`. Curated metadata (signature skills, behavior tags, placement overrides) is in other files under `data/`.

Core parsing and synergy logic is in `scripts/rewrite-summaries.py` and `scripts/generate-heroes-overview.py`.

## Requirements

- Python 3.12+
- [just](https://github.com/casey/just) (optional, for convenience recipes)
- Dependencies: `jsonschema` (installed into `.venv` by `just setup`)

---

<sup>*This repository and its contents were generated with the assistance of AI.*</sup>
