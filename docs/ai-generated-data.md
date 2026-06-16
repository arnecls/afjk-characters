# AI-Generated Data Files

The `data/` directory contains several JSON files that are considered **source data** rather than pipeline outputs. These files are generated and maintained with AI assistance. They are kept in version control so that hero behavior, signature skills, and replacement tags remain stable across pipeline regenerations.

This document summarizes the content and purpose of each AI-generated file, and provides the actual prompts used to generate and update them (sourced from the agent history). You can use these prompts to ask the AI to update the files when new heroes are added.

---

## 1. `signature_skills.json`

### Content

Maps each hero's display name to their signature skill category (`signature_calculated`, optional `signature_override`, and optional `speed_override`). Skill names are resolved from `heroes_data.json`.

### Purpose

Identifies the core "identity" skill of a hero. This is crucial for the synergy algorithm, as the casting speed of the signature skill dictates what kind of "fuel" (Haste, Energy) the hero needs from their teammates.

### Prompt to Update

```markdown
The website https://www.prydwen.gg/afk-journey/characters has a review section per character.
The @data/heroes_data.json contains the skills of each character.
Use the prydwen review to check if any of the signature skills in @data/signature_skills.json require an override (using the signature skill definition found in agents.md).
Do not adjust the detection script.
```

---

## 2. `hero_behavior_tags.json`

### Content

Contains an array of curated combat-role tags (e.g., `aoe-damage`, `summoner`, `cheat-death`) for each hero. The allowed tags are strictly defined in `data/schema/tags.schema.json`.

### Purpose

Drives the **Similar Skills** category in the replacement algorithm. By comparing the overlap of these tags (Jaccard similarity), the algorithm can suggest substitute heroes that fulfill the same strategic role and playstyle in combat.

### Prompt to Update

```markdown
Compare @data/hero_behavior_tags.json against the skill descriptions in @data/heroes_data.json.
Are there any characters where the tags do not describe the character's skills sufficiently?
Look for misleading tags, missing tags or tags that are wrongly attributed.
When creating new tags, try to build groups of tags over single-use tags.
```

---

## 3. `heroes_data_skill_summary.json`

### Content

Contains short, human-readable mechanic summaries for each skill category (`ultimate`, `skill1`–`skill5`) of a hero. 

### Purpose

Provides generalized descriptions of what skills do, stripped of specific numbers, percentages, or hero-specific flavor text (e.g., using "circular area" instead of "magic circle"). These summaries are joined to the processed skills and displayed in the "Skill overview" subsections of the generated markdown and web viewer.

### Prompt to Update

```markdown
Rewrite ALL missing or new entries in @data/heroes_data_skill_summary.json using generalized, game-mechanic based wording.

Read skill data and hero names from @data/heroes_data.json.

Read terminology hints from:

- @data/schema/game_properties.schema.json (damageType, ccType, stat, immunityType, battlePhase)
- @data/schema/skills.schema.json (effect labels)

RULES (critical):

1. Describe MECHANICS only — never hero names, skill names, companion/grant names (Brightfeather, Winter Warrior, falcon, ghost lance, dark cloud, winged form, plushies, etc.). The only exception are references between skills of the same character.
2. NO digits or numbers
3. Use schema vocabulary: AoE, DoT, HP Loss, true damage, stun, bind, knock back, knock down, knock up, frighten, silence, charm, sleep, displace, taunt, blind, invincible, unaffected, steadfast, untargetable, cleanse, mark, transformation, companion, summon, shield, heal, buff, debuff, energy recovery, etc.
4. Replace skill-specific imagery with generic effects. Examples:
   - "ghost lance fights on after death" → "persists after defeat with reduced ATK; active leap true damage scaling on recorded hp_loss"
   - "feather procs stack extra volley count on ultimate" → "empowered allies stack extra ultimate volleys"
   - "AoE lightning zone creates persistent dark cloud for DoT" → "AoE strike leaves persistent DoT zone on controlled enemies"
   - "winged form adds true damage per hit" → "transformation adds true damage per hit"
5. Keep summaries concise (~5-20 words are acceptable if needed for clarity; max 120 chars)
6. One summary per category that exists for each hero (ultimate, skill1-skill5)

The @data/heroes_data.json contains a field "description_lite", which provides an alternative short description. Use them to validate the statements in @data/heroes_data_skill_summary.json. Correct ambiguities and improve wording. Keep in mind to prefer game mechanical terms over game unspecific, descriptive terms.
```

---

## 4. `hero_play_overviews.json`

### Content

Maps each hero's display name to a short playstyle summary (3–5 sentences, up to ~900 characters).

### Purpose

Shown at the bottom of each hero's **behavior** section (before Skill overview) in `heroes-overview.md` and the site viewer. Summarizes how the hero is played: special setup requirements, when they shine, and when they underperform.

### Prompt to Update

```markdown
Regenerate entries in @data/hero_play_overviews.json using hero skill data from @data/heroes_data_processed.json and @data/heroes_data_skill_summary.json. Prydwen reviews (via `python3 scripts/generate_play_overviews.py`) may inform tone but must not be copied verbatim.

RULES:
1. Four to six sentences per hero; one idea per sentence — avoid dense multi-clause sentences. Keep under ~900 characters so the block fits 5–6 lines in the web UI.
2. Cover: special requirements (placement, timing, pairing), strengths (situations where they shine), weaknesses (when they underperform).
3. Use **bold markdown** sparingly (about 5–7 phrases per hero) for setup requirements, signature strengths, and clear failure conditions. Rendered as bold in the site viewer.
4. Do NOT mention game modes (AFK, PvP, Dream Realm, Arena, etc.), class, faction, rarity, level breakpoints, or investment/dupes.
5. Match each hero's existing entry length within ±30 characters when refreshing in place.
6. Keys use display names from heroes-overview.md (e.g. Twins, Galahad).
```
