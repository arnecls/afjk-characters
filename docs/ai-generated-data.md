# AI-Generated Data Files

The `data/` directory contains several JSON files that are considered **source data** rather than pipeline outputs. These files are generated and maintained with AI assistance. They are kept in version control so that hero behavior, signature skills, and replacement tags remain stable across pipeline regenerations.

This document summarizes the content and purpose of each AI-generated file, and provides the actual prompts used to generate and update them (sourced from the agent history). You can use these prompts to ask the AI to update the files when new heroes are added.

---

## 5. `skill_effects/<short_name>.json`

### Content

Per-hero AI-extracted combat effects keyed by skill section and ascension tier.
Each skill stores a `source_hash` of its `heroes_data.json` description for
staleness checks.

### Purpose

**Source of truth** for effect detection (buffs, debuffs, CC, damage, healing,
shields, energy, immunities, special provides/requires). The pipeline loads
these files in `analyze_hero()` instead of regex parsing.

### Prompt to Update

Use the [extract-skill-effects](../.cursor/skills/extract-skill-effects/SKILL.md)
skill workflow: read skill text, emit schema-valid JSON, validate, show diff,
get approval, save, run `just views` and `just validate`.

Do not patch regex rule tables in `rewrite-summaries.py` for effect fixes.

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

Contains an array of curated combat-role tags (e.g., `aoe-damage`, `summoner`, `cheat-death`, `backline-assassin`, `backline-inhibit`) for each hero. The allowed tags are strictly defined in `data/schema/tags.schema.json`.

### Purpose

Drives the **Similar Skills** category in the replacement algorithm. By comparing the overlap of these tags (Jaccard similarity), the algorithm can suggest substitute heroes that fulfill the same strategic role and playstyle in combat. Backline pressure is split: `backline-assassin` (substantial rear/far/highest-damage kills) vs `backline-inhibit` (soften/slow that same selector); plain `assassin` is non-positional selective picks.

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

Maps each hero's display name to a short playstyle summary (4–6 sentences, up to ~900 characters).

### Purpose

Shown in the behavior section as **Play overview** (before **Skill overview**) in `heroes-overview.md` and the site viewer. Summarizes how the hero is played: special setup requirements, when they shine, and when they underperform.

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

---

## 5. `hero_counter_overviews.json`

### Content

Maps each hero's display name to a short PVP counter summary (3–5 sentences, up to ~900 characters). Named units use `[[Display Name]]` markers (e.g. `[[Athalia]]`) for character pills. When kit-fit alternatives exist, use `[[filter:combo-id]] like [[Hero]]` so linked filter chips open list view with matching column filters (see `data/counter_filter_combos.json`).

### Purpose

Shown in the behavior section as **Counter proposal** (immediately after **Play overview**, before **Skill overview**) in `heroes-overview.md` and the site viewer. Explains what to watch for in PVP/Arena and suggests short counter-comp directions.

### Prompt to Update

```markdown
Regenerate entries in @data/hero_counter_overviews.json using hero skill data from @data/heroes_data_processed.json and @data/heroes_data_skill_summary.json. Use player-facing combat knowledge from afkj-data docs (faq-pvp, combat-*-pvp) but do NOT copy internal engine terms or implementation jargon into public text. Follow `.cursor/skills/counter/SKILL.md` for gates, Explicit counters, and naming.

RULES:
1. Three to five sentences per hero; one idea per sentence. Keep under ~900 characters.
2. Cover: PVP threat pattern, how the fight tends to play out, then short counter-comp hints with [[Hero]] markers for named units.
3. Use **bold markdown** sparingly for key threats and counter levers.
4. PVP and Arena may be named; do NOT mention class, faction, rarity, level breakpoints, or investment/dupes.
5. For single-ally buffers (Aliceth, Alna, Cassadee, etc.), assume they buff a hypercarry — often high-ultimate-damage dealers. Alna is more generic; typical partners include [[Sylphira]] and [[Frieren]].
6. Keys use display names from heroes-overview.md. Every [[Name]] must match a roster display name exactly.
7. Prefer Prydwen PVP tier **S+** and **S** heroes for named examples and counter units; use **A+** when needed, **A** only for matchup-specific picks (e.g. [[Lily May]] vs early-battle ultimates). Avoid B/C-tier names unless listed in Explicit counters or the user asks otherwise.
8. Early-battle / battle-start ultimates are usually answered with [[Lily May]] on the opening beat (not [[Pandora]] — too slow); see `.cursor/skills/counter/SKILL.md` **Explicit counters** for wind-up high-damage ults (Lily May + [[Pandora]] vs catchers), hypercarry speed-race buffers ([[Thador]], [[Hugin]], [[Rowan]]), and [[Dunlingr]] (non-ult kits + backline assassin on the **exempt carry**). **`heal-inhibitor` (graded):** use `[[filter:heal-inhibitor]]` for Vitality / healing-received cut vs HP-recovery sustain; [[Dunlingr]] Curelock vs ally-heal snowball — do not conflate the two levers (see counter skill Explicit table).
9. Against **ranged / backline hypercarries**, prefer `backline-assassin` or `backline-inhibit` tags — pick **1–2 kit-fit** names (see counter skill kit-fit cheat sheet), never a stock Athalia/Evie/Nerion list. Against **melee / frontline delete targets** (Warrior / Rogue / Tank melee floor), use the Explicit high-damage melee pool in Gate 2 — not `backline-assassin` on that hero. When alternatives exist, wrap as `[[filter:combo-id]] like [[Hero]]` (registry in `data/counter_filter_combos.json`); singleton picks with no alternative stay bare `[[Hero]]`; unfilterable levers use a free phrase with no link. Bias assassin `damage_type` by Phys DEF vs Magic DEF ranks in `data/character_stat_ranks.json` (any asymmetry); immunities override; both DEF high and/or heavy shields → prefer true-damage assassins (rotate — do not re-center on Athalia).
10. If any suggested **counter** is Celestial or Hypogean, also name a **non-Celestial, non-Hypogean** alternative for that lever **in the same clause**, prefer leading with the non-C/H name, and do not stack two C/H units for one lever.
11. Enemy-side-only buff/debuff amplification (stacks from *their* allies’ hits, etc.) is countered by pressuring the **providers** — never by telling the reader to “not feed” it with their own team composition.
12. Run the six **validation gates** in `.cursor/skills/counter/SKILL.md` before writing: (1) phase/hittability — including channel/chant maintenance: suggest **control CC** to break casts only when skill text shows S1 (`cannot maintain` under control), S2 (chanting + no cast immunity), or inferred `while channeling` without immunity; do **not** suggest control CC vs unaffected/immune casts; **ultimate Interrupt** ([[Lily May]]) stays Gate 4a only, (2) role match for kill/burst + DEF/true-damage variance, (3) protected/exempt allies, (4) timing — **4a** threat window and **4b** delete window, (5) high-mobility / late-ult targets need lasting wide ultimates (e.g. [[Shemira]], [[Frieren]]) — not assassin pins, (6) mid-fight position — **6a** `static-tile-buffer` displace buffed ally off tile (Steadfast → delete/inhibit), **6b** moving aura shove **receivers** with targeted displacement ([[Lumont]], [[Pippa]], …) — **not** enemy-grouping pulls ([[Cyran]], [[Eironn]]); peel provider only if not Steadfast/Unaffected. Against **enemy-grouping / displacement** *into your team*, prefer **Steadfast** / **Unaffected** (e.g. [[Gunnar]] Doomfield) — formation spread does not stop global pulls like Cyran’s black hole. Battle-start-only placement (Twins, Thador, Thoran) is not Gate 6.
```
