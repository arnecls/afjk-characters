---
name: add-hero
description: >-
  Adds exactly one new AFK Journey hero to the current per-hero roster:
  source download, AI sidecar and metadata, local analysis, generated views,
  portrait assets, and structural, semantic, and presentation validation.
  Use when adding a new hero, character, or roster unit.
---

# Add one hero

Use this skill for **one new hero per run**. It is the orchestration workflow
for the current split-hero architecture. Detailed authoring rules live in the
specialized skills linked below; do not duplicate them here.

The run is complete only when the hero has source data, curated AI data,
fresh local analysis, generated views, a valid portrait, and passing
validation. A source or asset that is not available may be registered
provisionally, but the result must be reported as **BLOCKED / INCOMPLETE**.
Never report a blocked intake as complete.

Related skills:

- [extract-skill-effects](../extract-skill-effects/SKILL.md) — authoritative
  per-tier skill-effect sidecar extraction
- [behavior-tags](../behavior-tags/SKILL.md) — curated combat-role tags
- [counter](../counter/SKILL.md) — PVP counter overview and validation gates
- [hero-data](../hero-data/SKILL.md) — manual source-versus-analysis audit
- [web-ui](../web-ui/SKILL.md) — display-only site problems

Primary references:

- [data README](../../data/README.md)
- [pipeline reference](../../docs/skill-analysis-pipeline.md)
- [AI data rules](../../docs/ai-generated-data.md)
- [.cursor/AGENTS.md](../../.cursor/AGENTS.md)

## Completion checklist

Track this checklist for the named hero. Every checked item must have the
evidence described by its completion criterion.

```text
- [ ] 0. Scope and identity are confirmed.
- [ ] 1. Stable ID and four-file bundle are initialized.
- [ ] 2. Source data and external facts are downloaded and complete.
- [ ] 3. Skill-effect sidecar is complete, hashed, and schema-valid.
- [ ] 4. Curated AI metadata is complete in the hero bundle.
- [ ] 5. Local analysis is fresh and manually audited against skill text.
- [ ] 6. Full-roster views and portrait assets are generated.
- [ ] 7. Structural, semantic, automated, and presentation checks pass.
- [ ] 8. Final report distinguishes complete from blocked or deferred work.
```

## 0. Scope and identity

Before changing files, establish these values from the source pages and the
repository conventions:

| Value | Contract |
| --- | --- |
| Stable ID | Lowercase kebab-case; the directory and cross-hero identity |
| Display name | Site, overview, portrait filename, and curated metadata key |
| Source name | Downloaded `source.json` name; may differ from display name |
| Title | Source title stored in the roster manifest |
| Aliases | Fandom, Yaphalla, or Prydwen names that identify the same hero |

Check the Fandom hero list, Yaphalla hero index, and Prydwen character page.
Read the current manifest and the hero-name/alias maps before inventing a
slug. The known `Elijah & Lailah` / `Twins` split is the model for an alias,
not a reason to add a second roster hero.

**Completion criterion:** the ID, display name, source name, title, and aliases
are written down and there is no duplicate manifest identity.

## 1. Initialize the split-hero bundle

Initialize before downloading:

```bash
python3 scripts/hero_pipeline_cli.py init <hero-id> \
  --display-name "Display Name" \
  --title "Source Name - Subtitle" \
  --alias "Source Name"
```

This creates the manifest entry and:

```text
data/heroes/<hero-id>/source.json
data/heroes/<hero-id>/ai.json
data/heroes/<hero-id>/overrides.json
data/heroes/<hero-id>/analysis.json
```

`analysis.json` is a rebuildable cache. Do not author it manually.
`overrides.json` should remain at `{"schema_version": 1}` until a computed
behavior mismatch is observed.

If the hero has a Fandom page, add its source name to
`HERO_NAMES` in `scripts/sources_web.py`, and add only evidence-based
Prydwen slug/display aliases to `PRYDWEN_SLUG_ALIASES` or
`PRYDWEN_NAME_ALIASES`. A Yaphalla-only record still needs this initialized
bundle: source merging may discover it, but `write_source_roster()` rejects
downloaded heroes without a pre-existing bundle.

**Completion criterion:** `roster.json` contains one ordered entry and all four
files exist under the matching hero ID.

## 2. Download and inspect source data

Run the scoped command after initialization:

```bash
python3 scripts/hero_pipeline_cli.py download --hero <hero-id>
```

`--hero` limits which initialized bundle is written; the downloader still
fetches the live Fandom, Yaphalla, and Prydwen pools. Use `just download` only
when refreshing the whole roster.

Inspect `data/heroes/<hero-id>/source.json` and confirm:

- the downloaded `source.name`, title, and display name resolve to the
  manifest entry;
- every available skill slot has raw text, active/passive text, upgrades,
  and expected metadata such as range, cooldown, and initial energy;
- `description_lite` is present where the source provides it;
- Prydwen tiers and role categories are present, or their absence is recorded
  as a release-source limitation;
- `external.walk_speed` is one of `zero`, `slow`, `normal`, `fast`, or
  `veryfast`; and
- `external.stat_ranks` is populated from the sibling `afkj-data` game-data
  documentation when available.

Do not invent walk speed, stat ranks, a missing skill, or a missing tier.
If the game data table has no walk-speed row, regenerate that table or report
the intake blocked. If a web source is not live yet, keep the bundle explicit
but stop the completion path and report the missing source.

**Completion criterion:** every expected skill and external fact is either
present and inspected or listed as a concrete blocked item; no placeholder
value is presented as sourced data.

## 3. Build the skill-effect sidecar

Invoke [extract-skill-effects](../extract-skill-effects/SKILL.md) for this
hero. Treat `data/heroes/<hero-id>/ai.json.skill_effects` as the source of
truth for effects. Read the full active/passive text and every ascension and
EX tier before authoring.

The sidecar must cover, where present:

- damage types, healing, shields, Energy, buffs, and debuffs;
- CC and anti-CC/immunity effects;
- targeting from the same clause as each effect;
- true-damage subtypes, DoT intervals, conditions, and durations;
- `special_provides` and `special_requires`;
- summon effects and summoning provides for a genuine battlefield summon;
- `persistence` on every positive ally stat buff; and
- `source_hash` and `is_max_known` for every skill.

Use schema vocabulary and the semantics in `.cursor/AGENTS.md`. Preserve
fully ascended values and do not copy area reach from a neighboring clause.
Do not edit regex tables or resurrect aggregate files for a new mechanic.
Most new-hero gaps are sidecar data. If the evidence instead exposes a
reusable downloader, schema, validator, or pipeline defect, fix that shared
defect only with a focused regression test and record it in the final report.

Validate the draft with the extraction skill, show the old-versus-new effect
diff, then save it. A missing or stale sidecar is not an acceptable
intermediate completion state.

**Completion criterion:** the sidecar validates, every source skill has a
matching hash and tier data, and its effects explain the mechanics in the
fully ascended text.

## 4. Complete hero-local AI metadata

Keep all curated metadata in this hero's `ai.json`. Do not create or update
the removed roster-keyed aggregate files.

### 4.1 Behavior tags and summons

Invoke [behavior-tags](../behavior-tags/SKILL.md). Choose a small,
alphabetically sorted set, normally three to five allowed enum values, that
describes how the hero is played. Check the full tag definitions, including
`temporary-stat-buffer`, `dot-specialist`, `summoner`, `battle-start-burst`,
`high-initial-energy`, and `non-ult-utility`.

If the hero is a genuine battlefield summoner, complete the `summon_profile`
and registry requirements. Transient spell effects are not summons.

### 4.2 Skill summaries

Add one generalized mechanic summary for every skill category that exists:
`ultimate`, `skill1` through `skill5`. Use `description_lite` as a
cross-check. Summaries contain mechanics, not numbers, hero names, skill
names, named companions, or visual flavor nouns.

These texts are the skill-card short descriptions on the site. Keep them
concise like the rest of the roster (~5–20 words, max ~120 characters): one
core beat per skill, not a full kit paraphrase. Prefer the shortest wording
that still names the main mechanic.

### 4.3 Play overview

Write the short play overview from the current skill data and, when useful,
the Prydwen review. Follow the AI data rules: explain setup, strengths, and
failure conditions without game modes, class/faction/rarity, investment
advice, or copied source prose.

### 4.4 Counter overview

Invoke [counter](../counter/SKILL.md) after the analysis data and play
overview are available. Apply all validation gates: hittability, role and
damage type, protected allies, threat/delete timing, high mobility, and
mid-fight placement. Resolve every named hero and filter marker.

### 4.5 Signature and sparse corrections

The signature is normally calculated by analysis. Add only an observed
correction in `overrides.json.signature`, using `signature_override` or
`speed_override`. Add movement, melee/range, or placement corrections only
when generated behavior is demonstrably wrong. Base walk speed belongs in
`source.json.external`, not in an override.

**Completion criterion:** `ai.json` has valid effects, tags, conditional
summon data, all summaries, play overview, and counter overview; any
override has an observed reason.

## 5. Analyze and manually audit

After changing `skill_effects`, `behavior_tags`, `summon_profile`, or
overrides, refresh the local cache:

```bash
python3 scripts/hero_pipeline_cli.py analyze --hero <hero-id>
```

Read the resulting `data/heroes/<hero-id>/analysis.json` and compare every
skill's raw/upgrade text with its `effects`, `skill_card_tags`, targeting,
benefit stats, movement, placement, signature, and special mechanics. Use
[hero-data](../hero-data/SKILL.md) in single-hero mode. Missing or wrong
effects are fixed in the hero sidecar first; shared code changes require a
literal-text regression test.

Run the roster-wide script checks that consume the new analysis:

```bash
python3 scripts/audit_non_ult_utility.py
```

Confirm the new hero's tag/utility result and investigate any contradiction
before continuing. Do not use `--apply` to let an audit silently replace
curated tags.

**Completion criterion:** local analysis is fresh, the manual text-to-analysis
audit has no unresolved mechanical discrepancy, and any shared fix has its
focused regression test.

## 6. Render views and assets

First publish local projections without asset-network work:

```bash
python3 scripts/hero_pipeline_cli.py views
```

Then run the complete site recipe:

```bash
just render-site
```

The site recipe regenerates views, downloads shared icons, resolves each
hero's Fandom gallery combat portrait, and rebuilds the JavaScript bundle.
Portraits are stored as:

```text
site/assets/portraits/<Display Name>.png
```

The portrait downloader requests the original Fandom image revision and
validates the resulting PNG/WebP/JPEG bytes. A missing or invalid new portrait
causes the recipe to fail. Do not substitute page art, full character art, or
an arbitrary CDN thumbnail.

**Completion criterion:** the hero appears exactly once in `Heroes.md`,
`heroes-overview.md`, `heroes-overview.csv`, and `site/data/heroes.json`; its
site slug, skill cards, behavior, relationships, and portrait all resolve.

## 7. Validate all boundaries

Run the checks in this order:

```bash
just validate
just validate-semantics
just typecheck
just test
just assert-rendered-outputs
```

Use `just test-serial` when a test failure needs readable debugging output.
`just validate` checks bundle schemas and cache freshness. The semantic
command additionally checks sidecar hashes, effect semantics, targeting,
stat-buff persistence, summaries, walk speed, counter markers, and
reanalysis parity. `assert-rendered-outputs` must be interpreted against the
intended new-hero diff, not bypassed.

Spot-check the hero in the site page, including skill chips, summary text,
counter pills, portrait loading, and list-view filters. If detection JSON is
correct but a chip is styled or worded incorrectly, use [web-ui](../web-ui/SKILL.md)
instead of altering sidecar semantics.

**Completion criterion:** all required commands pass, intended generated
outputs contain the hero, and the site spot-check has no hero-specific issue.

## 8. Report complete or blocked

Report:

1. hero ID, source name, display name, aliases, and source status;
2. files changed in the hero bundle and any shared code/regression test;
3. sidecar effects, tags, summaries, play overview, counter overview, and
   overrides completed;
4. local analysis, generated views, portrait, and validation evidence; and
5. open items such as missing source pages, unavailable Prydwen tiers,
   missing game-data facts, deferred mechanics, or blocked portraits.

Use **COMPLETE** only when the completion criteria above are satisfied. If
registration succeeded but any required source, external fact, AI field,
analysis, portrait, generated view, or validation check is missing, report
**BLOCKED / INCOMPLETE** and name the exact next action.

## Non-goals

- Adding more than one hero in a single run.
- Rebuilding the full-roster effect audit; use [hero-data](../hero-data/SKILL.md).
- Inventing schema enum values or provisional external facts.
- Editing generated aggregate files that no longer exist.
- Deployment or hosting changes.
