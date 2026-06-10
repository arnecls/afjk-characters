# AFK Journey Hero Reference

**Start here: [heroes-overview.md](heroes-overview.md)** — per-hero synergies, combat
behavior, structured skill summaries, and replacement suggestions for the full
roster.

This repository collects and analyzes hero skill data for [AFK Journey](https://afk-journey.fandom.com/wiki/AFK_Journey). Skill text is sourced primarily from the [AFK Journey Fandom wiki](https://afk-journey.fandom.com/wiki/Hero/List), with gaps filled from [Yaphalla](https://www.yaphalla.com/heroes). Meta tier ratings (S+, S, A, etc. per game mode) come from the [Prydwen tier list](https://www.prydwen.gg/afk-journey/tier-list). Skill text is parsed to extract buffs, debuffs, crowd control, damage types, and team synergies.

## What is in this repository

| File / folder | Purpose |
| --- | --- |
| **[heroes-overview.md](heroes-overview.md)** | Main reference: synergy partners, behavior, and parsed summaries per hero |
| **[heroes-overview.csv](heroes-overview.csv)** | Same roster data in spreadsheet form (damage, CC, buffs, movement, etc.) |
| **[Heroes.md](Heroes.md)** | Raw skill descriptions only — no summaries |
| **`data/`** | Canonical JSON (`heroes_data.json`) plus processed analysis and JSON schemas |
| **`scripts/`** | Python pipeline: download, analyze, validate, and render views |
| **[`site/`](site/)** | Static web viewer (GitHub Pages) — hero grid with synergy details |
| **[`.cursor/AGENTS.md`](.cursor/AGENTS.md)** | Detailed rules for parsing skills, scoring synergies, and editing summaries |

### What each hero entry contains

Each section in [heroes-overview.md](heroes-overview.md) includes:

- **Behavior** — movement pattern, signature skill, casting speed, placement constraints
- **Units improving X** — up to five ranked synergy partners (stat buffs, enablers, summon support)
- **Units benefitting most from X** — reverse index of heroes who synergize with this unit
- **Replacements** — similar heroes grouped by role (damage, crowd control, buffs, etc.)
- **Summary** — structured breakdown of stats benefited, damage types, buffs, debuffs, crowd control, and special effects

Magnitude labels (`high`, `medium`, `low`) rank an effect against the full roster, not in isolation. See [`.cursor/AGENTS.md`](.cursor/AGENTS.md) for the full taxonomy.

## How to use it

### Browse the reference

Open [heroes-overview.md](heroes-overview.md) and jump to a hero by name. Use your editor's outline or search (`Ctrl/Cmd+F`) to navigate.

For filtering or pivot tables, open [heroes-overview.csv](heroes-overview.csv) in a spreadsheet application.

For verbatim skill wording (levels, cooldowns, unlock tiers), see [Heroes.md](Heroes.md).

### Web viewer

Browse the roster in a browser at **[https://arnecls.github.io/afjk-characters/](https://arnecls.github.io/afjk-characters/)** (deployed from the [`site/`](site/) directory via GitHub Pages).

Each hero has a shareable URL, e.g. `/hero/aliceth`. Synergy partners link to their own pages.

Hero portraits and faction/class icons in the web viewer are from [Yaphalla](https://www.yaphalla.com/heroes).

Rebuild site data locally:

```bash
just render-site
```

This refreshes `heroes-overview.md` / `heroes-overview.csv`, copies the CSV into `site/data/`, writes `site/data/heroes.json`, and downloads any missing portrait images from Yaphalla into `site/assets/`. Running `just views` also refreshes the site data.

Preview locally (required — the site loads data via `fetch`):

```bash
cd site && python3 -m http.server
```

Then open `http://localhost:8000/` in your browser.

Enable GitHub Pages once in the repository settings: source **Deploy from a branch**, branch **`gh-pages`**, folder **`/` (root)**. Pushes to `main` or `webview` trigger [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml).

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

This runs analysis (`data/heroes_data_processed.json`, `data/heroes_data_synergies.json`) and renders `Heroes.md`, `heroes-overview.md`, `heroes-overview.csv`, and `site/data/heroes.json` + `site/data/heroes-overview.csv`.

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
             site/data/heroes.json
```

Configuration for synergy scoring and display limits lives in `data/heroes_config.json`. Curated metadata (signature skills, behavior tags, placement overrides) is in other files under `data/`.

Core parsing and synergy logic is in `scripts/rewrite-summaries.py` and `scripts/generate-heroes-overview.py`.

## Requirements

- Python 3.12+
- [just](https://github.com/casey/just) (optional, for convenience recipes)
- Dependencies: `jsonschema` (installed into `.venv` by `just setup`)

---

<sup>*This repository and its contents were generated with the assistance of AI.*</sup>
