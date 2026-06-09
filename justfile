# AFK Journey hero data pipeline.
# Run `just` (or `just -l`) to list recipes.
#
# Pipeline: download -> process -> render
#   download : data/heroes_data.json          (merge fandom + Yaphalla)
#   process  : data/heroes_data_processed.json + heroes_data_synergies.json
#   render   : Heroes.md, heroes-overview.md, heroes-overview.csv

default:
    @just --list

# Refresh data/heroes_data.json from live sources (fandom + Yaphalla; needs network).
download:
    python3 scripts/download_heroes.py

# Analyse data/heroes_data.json -> processed + synergies JSON.
analyze:
    python3 scripts/process_heroes.py
    python3 scripts/process_synergies.py

# Recompute roster-wide synergies from existing processed data.
analyze-synergies:
    python3 scripts/process_synergies.py

# Render Heroes.md from data/heroes_data.json.
render-heroes:
    python3 scripts/render_heroes.py

# Render heroes-overview.md + heroes-overview.csv.
render-overview:
    python3 scripts/render_overview.py

# Render all view files.
render: render-heroes render-overview

# Regenerate views from the committed data/heroes_data.json (no network).
views: analyze render

# Full pipeline: refresh data from the web, then regenerate views.
all: download analyze render
