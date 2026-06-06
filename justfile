# AFK Journey hero data pipeline.
# Run `just` (or `just -l`) to list recipes.

default:
    @just --list

# Fetch skill text from Yaphalla → Heroes.md
download:
    node scripts/generate-heroes-md.js

# Fetch skill text from fandom wiki → heroes2.md
download2:
    node scripts/generate-heroes2-md.js

# Synergies + summaries → heroes-overview.md (strips stray summaries from Heroes.md)
overview:
    python3 scripts/generate-heroes-overview.py

# heroes-overview.md → heroes-overview.csv
csv:
    python3 scripts/overview-to-csv.py

# Download hero data, then regenerate overview and CSV
all: download download2 overview csv
