# AFK Journey hero data pipeline.
# Run `just` (or `just -l`) to list recipes.

default:
    @just --list

# Fetch skill text from Yaphalla → Heroes.md
download:
    node scripts/generate-heroes-md.js

# Synergies + summaries → heroes-overview.md (strips stray summaries from Heroes.md)
overview:
    python3 scripts/generate-heroes-overview.py

# Download hero data, then regenerate overview
all: download overview
