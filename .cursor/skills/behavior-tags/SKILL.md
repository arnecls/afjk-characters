---
name: update-behavior-tags
description: >-
  Audits and updates curated combat-role tags in data/hero_behavior_tags.json
  against hero skill data. Use when asked to update, refresh, audit, review, or
  fix behavior tags, hero_behavior_tags.json, similar-skills tags, or when
  following docs/ai-generated-data.md section 2.
---

# Update behavior tags

Curate `data/hero_behavior_tags.json` so each hero has a small set of tags
that describe how they are played in combat. Tags drive **Similar Skills**
replacement scoring (Jaccard overlap in `scripts/generate-heroes-overview.py`).

## Source files (read in this order)

1. `.cursor/AGENTS.md` — **Behavior tags** section (definitions + 3–5 tag rule)
2. `data/schema/tags.schema.json` — allowed tag enum (do not invent tags)
3. `data/hero_behavior_tags.json` — current assignments
4. `data/heroes_data.json` — `description`, `description_lite`, skill text
5. `data/heroes_data_skill_summary.json` — mechanic summaries per skill slot
6. `data/hero_play_overviews.json` — curated playstyle blurbs (good first pass
   for identity; cross-check against skill text before changing tags)

Optional context: `docs/ai-generated-data.md` section 2, `docs/replacement-algorithm.md`.

## Audit prompt

Compare `data/hero_behavior_tags.json` against skill descriptions in
`data/heroes_data.json`, using `heroes_data_skill_summary.json` and
`hero_play_overviews.json` to spot identity mismatches quickly.
Are there any characters where the tags do not describe the character's skills
sufficiently?
Look for misleading tags, missing tags or tags that are wrongly attributed.
When creating new tags, try to build groups of tags over single-use tags.

**Schema constraint:** only use tags from `tags.schema.json`. If no existing
tag fits, note the gap; do not add enum values unless the user requests a
schema change.

## Workflow

```
Task progress:
- [ ] 1. Load definitions, schema enum, current tags, hero list
- [ ] 2. Flag coverage gaps (missing heroes, name aliases)
- [ ] 3. Review heroes (all, or user-named subset)
- [ ] 4. Apply fixes to hero_behavior_tags.json
- [ ] 5. Validate JSON against schema enum
- [ ] 6. Summarize findings and edits
```

### 1. Load and inventory

- Hero count in `heroes_data.json` must match tag keys (alias: **Twins** in
  tags = **Elijah & Lailah** in `heroes_data.json`; pipeline uses `Twins`).
- Note heroes with fewer than 2 or more than 6 tags after edits.
- Prefer **3–5 tags** per hero; only exceed for genuinely multi-role kits.

### 2. Per-hero review

For each hero, read play overview + summaries + `description_lite` and ask:

1. **Missing** — defining mechanic with no matching tag?
2. **Misleading** — tag present but mechanic is minor, wrong target, or wrong
   type?
3. **Wrong attribution** — tag describes a one-off skill, not how the hero is
   played?

Assign tags that describe **playstyle identity**, not every skill effect.

### 3. Apply edits

- Edit only `data/hero_behavior_tags.json`.
- Keep tag arrays **sorted alphabetically**, **unique**, non-empty.
- Minimize diff: fix clear issues; do not retag the whole roster without cause.
- When adding tags, prefer **reusable group tags** already in the enum over
  hero-specific nuance.

### 4. Validate

After editing, verify programmatically:

- Every tag is in `tags.schema.json` `behaviorTag` enum
- No duplicate tags per hero
- Every hero in `heroes_data.json` has an entry (via `Twins` alias)

```bash
python3 - <<'PY'
import json
from pathlib import Path

root = Path("data")
tags = json.loads((root / "hero_behavior_tags.json").read_text())
heroes = json.loads((root / "heroes_data.json").read_text())
allowed = set(json.loads((root / "schema/tags.schema.json").read_text())
              ["$defs"]["behaviorTag"]["enum"])

names = {h["name"] for h in heroes["heroes"]} - {"Elijah & Lailah"} | {"Twins"}
assert names == set(tags), (names - set(tags), set(tags) - names)
for hero, tlist in tags.items():
    assert tlist, hero
    assert len(tlist) == len(set(tlist)), hero
    bad = set(tlist) - allowed
    assert not bad, (hero, bad)
print("OK:", len(tags), "heroes")
PY
```

## Definition guardrails

Apply `.cursor/AGENTS.md` definitions strictly. Common mistakes:

| Tag | Requires | Reject when |
|-----|----------|-------------|
| `mass-cc` | Reliable CC on **multiple** enemies or wide areas | Single-target stun/bind/knock |
| `ally-buffer` / `ally-healer` / `ally-shielder` | Meaningful effect on **allies** | Self-only, or buffs/shields on summons/turrets |
| `energy-provider` | Grants Energy to **allies** or accelerates ally ulimates | Self energy recovery only |
| `battlefield-modification` | Physical obstacles or map layout changes | Buff/debuff/terrain **zones** alone |
| `summoner` | **Persistent** companions on the battlefield (targetable, can be destroyed) | Brief ult animations (flying blades, swords); **spell-form** summons (Mehira voidlings, Shemira ghosts) that cannot be targeted or destroyed |
| `dot-specialist` | Recurring tick damage as a **primary** pattern | Stat debuffs without DoT; bind damage alone |
| `life-drain` | HP sustain tied to **dealing damage** | Stat steal, shield regen, heal-on-shield |
| `fire-attack` | Burning or scorched-ground damage | Cannon/artillery theming without burn |
| `revive` | Brings **defeated allies** back | Self-survival (`cheat-death` instead) |
| `aoe-damage` | Substantial multi-target damage **regularly** | Occasional summon detonation |
| `aoe-healing` | Heals **wide ally groups** | Single-target or post-channel one-off heal |
| `assassin` | Picks isolated/backline with burst | General focus-fire marksmen |
| `self-repositioner` | **Regularly** jumps/dashes/teleports self | One incidental leap |
| `hp-scaling` | Scales on **HP values** | Shield-value scaling |
| `invincibility` | Meaningful immunity windows | Brief immunity already covered by `transformation`; do not drop when a skill grants a **post-trigger damage + control immunity window** (e.g. Brutus Indomitable after fatal blow) |
| `battle-start-burst` | Deals damage in the **first ~2–3s** of battle | Buff/shield/debuff/energy/summon setup at battle start without immediate damage; delayed openers (Frieren 15s); terrain bombs without a damage clause (Kulu debris); sequential battle-start cycles where damage is not the first effect (Cyran Mythic+) |

## Reporting

Summarize for the user:

1. **Findings** — misleading / missing / wrongly attributed (grouped by theme)
2. **Changes** — heroes edited with before → after tags
3. **Left unchanged** — heroes reviewed and already accurate
4. **Gaps** — kits that lack a good enum tag (e.g. self-shield tanks); propose
   schema additions only if asked

Do not regenerate `heroes-overview.md` or the site unless the user asks.

## Examples

**Bonnie** — debuff-spread mage with opening hit: `enemy-debuffer`,
`transformation`, `aoe-damage`, `battle-start-burst` (Aging deals damage at
battle start). Not `mass-cc` (ult stun only on debuffed targets),
`dot-specialist` (debuff stacking ≠ DoT), or `invincibility` when mist form is
already `transformation`.

**Perseus** — terrain tile buffs: `ally-buffer`, `aoe-damage`. Not
`battlefield-modification` (buff zones do not count).

**Cecia** — `summoner`, `mass-cc` (area entangle on summon), `enemy-debuffer`
(stat steal). Not `life-drain` (stat absorb ≠ lifesteal).

**Florabelle** — buffs/shields **summons**, not allies: `summoner`,
`aoe-damage`. Not `battle-start-burst` (battle-start Spiny summon is setup,
not burst), `ally-buffer` / `ally-shielder`.

**Mehira / Shemira** — voidlings and ghosts are **spell-form** damage, not
battlefield companions: keep `aoe-damage`, `life-drain`, etc. Not `summoner`
(cannot be targeted or destroyed; exist only briefly).

For more edge cases, see [pitfalls.md](pitfalls.md).
