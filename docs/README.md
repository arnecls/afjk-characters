# Documentation

Guides for the hero data pipeline, scoring algorithms, and curated metadata.

## Getting started

- [Skill analysis pipeline](skill-analysis-pipeline.md) — end-to-end flow from web sources to markdown and the site viewer
- [AI-generated data](ai-generated-data.md) — curated JSON files (`signature_skills.json`, behavior tags, skill summaries, play overviews) and prompts to refresh them
- [Data directory](../data/README.md) — file roles, what is script-generated vs hand-edited

## Algorithms

- [Synergy algorithm](synergy-algorithm.md) — how **Units improving X** partners are ranked
- [Replacement algorithm](replacement-algorithm.md) — similar-skills and role-based substitutes
- [Signature skill algorithm](signature-skill-algorithm.md) — identity skill selection and casting-speed fuel
- [Movement detection](movement-detection-algorithm.md) — movement labels and synergy impact

## Validation snapshots

Point-in-time audit reports from roster validation runs (for regression context; run `just validate` for current checks):

- [High-level 2026-06-16](validation-high-level-2026-06-16.md) (latest high-level)
- [Detailed 2026-06-16](validation-detailed-2026-06-16.md) (latest detailed)
- Older: [2026-06-15](validation-high-level-2026-06-15.md), [2026-06-11](validation-high-level-2026-06-11.md)

## Agent reference

Parsing rules, effect taxonomy, and editing conventions for AI-assisted work live in [`.cursor/AGENTS.md`](../.cursor/AGENTS.md).
