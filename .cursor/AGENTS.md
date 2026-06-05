# AFK Journey context

## Factions

- Wilders
- Maulers
- Graveborn
- Lightbearer
- Celestials
- Hypogeans

## Classes

- Tank
- Support
- Marksman
- Mage
- Rogue
- Warrior

## Damage types

- Normal
- Melee
- Magic
- Ranged
- Physical
- True damage (classic, no HP scaling in the phrase)
- HP loss — extra/true damage scaling on **lost HP** (self or target)
- Max HP-based damage — damage scaling on **max HP**
- Damage over time (DoT)

Summaries list every type detected in skill text (not only the unit's
primary type). Detection rules live in `detect_damage_types()` in
`rewrite-summaries.py`.

**HP loss**, **Max HP-based damage**, and **True damage** lines add a
`high` / `medium` / `low` magnitude (vs the roster for that type), scored
from parsed damage %, targeting reach, and frequency (`assign_damage_magnitudes()`
in `rewrite-summaries.py`). Format: `- {type} — {targeting} — \`{magnitude}\``.

Damage over time needs to derived from text by look for indicators like "deals
damage for 2s". This needs to be done by the Agent, as text are too
fuzzy to define clear rules.

## Targeting

- Self
- Single target
- Multiple targets
- Arc
- Area
- All units

To detect these targeting types, the text needs to be searched for wordings like
"In an arc", "all", etc. This needs to be done by the Agent, as text are too
fuzzy to define clear rules.

## Crowd Control

- Stun
- Knock down
- Frighten
- Silence
- Charm
- Sleep
- Move (force new position)
- Pin (cannot move but still act)
- Interrupt

These types need to be derived from the text.
For example:

- "knocking them back" -> Knock down
- "hypnotizing all enemies" -> Sleep
- "stunning them" -> Stun
- "unable to move" -> Pin
- "pulling in enemies" -> Move

This needs to be done by the Agent, as text are too
fuzzy to define clear rules.

## Buffs (summary lines)

Buff lines use `{label} ({tier}) — {targeting} — {magnitude}`.

Optional suffix: `— conditional (frequent)` or `— conditional (rare)`.

- **conditional (frequent)** — gated but usually applies often in a fight
  (e.g. on cast, on kill, first proc). Magnitude is not reduced.
- **conditional (rare)** — not every battle or hard to proc (e.g. enemy
  monsters, ingredients, once per battle). Magnitude is lowered by two steps
  (`high`→`low`, `medium`→`low`).

Synergy picks in `heroes-overview.md` skip rare conditional ally buffs.

## Quality indicators

Summary lines mark relative strength with **`high`**, **`medium`**, or
**`low`** (backticks in output). These rank an effect against the roster, not
in isolation.

- **Buffs / debuffs** — parsed % compared within the same label across heroes
  (quantiles when enough data); debuffs also reward `all enemies` reach.
  `assign_magnitudes()` in `rewrite-summaries.py`.
- **Crowd control** — duration-based (≥5s → high, ≥2s → medium).
- **HP loss / max-HP / true damage** — composite score from %, targeting, and
  frequency; roster quantiles in `assign_damage_magnitudes()`.

**Tier** in parentheses (`Mythic+`, `Level 3`, …) is unlock level, not
strength. **Conditional (rare)** lowers magnitude by two steps; some labels
(Invincible, Fatal blow immunity) are always high.

Synergy scoring weights magnitude (high > medium > low). When auditing,
compare heroes with the same buff/debuff label — wrong targeting or clause
parsing often yields wrong indicators.

## Hero docs

- **Heroes.md** — skill text from Yaphalla (and manual edits). No `### Summary`
  sections.
- **heroes-overview.md** — generated synergies plus `### Summary` per hero.

Regenerate overview (and strip stray summaries from Heroes.md if present):

`python3 scripts/generate-heroes-overview.py`

Summary/synergy rules live in `scripts/rewrite-summaries.py` (library).

## Detecting synergies between units

Synergy is **provider → receiver**: one hero supplies what another needs.
Automated ranking lives in `scripts/generate-heroes-overview.py`; when
reviewing or fixing matches, work through both heroes in this order.

1. **Summarize each hero** from `Heroes.md` skill text (see `### Summary` in
   `heroes-overview.md` or run `rewrite-summaries.py`). Extract:
   - **Stats the unit benefits from** — stats they self-buff or scale on
   - **Ally buffs** — buffs that hit allies (`Single target` through
     `All units`; not `Self`)
   - **Summon buffs** — buffs on allied summons only
   - **Requires** — partner-enabled special effects (not self-setup)

2. **Match provider → receiver** on three paths:
   - **Stat buffs** — ally buff label maps to a receiver benefit stat
     (e.g. `Haste buff` → Haste or ATK SPD; `Shield` → Max HP)
   - **Summon buffs** — summon buffs for heroes who field summons
   - **Enablers** — provider satisfies a receiver **Requires** label
     (DoT on enemies, magic damage from allies, party composition, etc.)

3. **Score and rank** — broader targeting and higher magnitude win; skip
   **rare conditional** ally buffs; sum stat + summon + enabler scores; keep
   the top five partners per receiver. Drop weak-only picks (generic ATK,
   Max HP / Shield when the receiver does not value those stats).

**Units benefited** at the end of each Synergies block is the reverse index:
heroes who list this unit in their top five.

**Parsing pitfalls** (bad summaries → false synergies): resolve targeting from
the **same sentence/clause** as the buff; do not treat self energy or self
stats as ally buffs; enemy debuffs are not benefit stats; situational ally
buffs (monster fights, ingredients, once per battle) should not rank.

Regenerate: `python3 scripts/generate-heroes-overview.py`

## Synergies (`heroes-overview.md`)

Generated by `scripts/generate-heroes-overview.py`. Up to five allies per hero, ranked by
combined score. **Units benefited** (end of Synergies) lists heroes who
include this unit in their top five.

1. **Stat buffs** — provider buffs match the hero's **Stats the unit benefits
   from** (magnitude, targeting, conditional weighting). Omitted when that is
   the only value: ATK-only buffs, Max HP buff-only, Shield-only (unless the
   hero benefits from Max HP/shields). Rare conditional buffs score lower.
   **Haste vs ATK SPD:** Haste also increases attack speed. For heroes that
   benefit from **ATK SPD**, ally **Haste buff** counts toward that need and
   is scored above **ATK SPD buff** at equal reach/magnitude (see
   `HASTE_FOR_ATK_SPD_SCORE_MULT` in `generate-heroes-overview.py`).
   **Healing need:** heroes who **consume or lose their own max HP** during
   skills (e.g. Talene's Ultimate channel) get **Healing** in benefit stats
   and match ally healers. **Wide magic for Bonnie:** providers with **Magic**
   damage and battlefield-wide patterns (`center of the battlefield`, `all
   enemies`, etc.) score higher for Bonnie's *Magic damage from allies*
   enabler.
2. **Enablers** — provider satisfies the hero's **Requires** special effects
   (e.g. magic damage from allies for Bonnie, DoT on enemies for Shadewing,
   Mage/Tank/Support for Himmel's party composition). Self-setup labels
   (Debuff on target (Aging), form/stance, boss gates, etc.) are skipped.
   Synergy text
   uses `Enables {label} via {detail}`.

Matchers and skip lists live in `scripts/generate-heroes-overview.py`.
`main()` prints an enabler pattern scan for skill phrases not yet in
`SPECIAL_REQUIRES_RULES`.

## Special effects (summary lines)

Notable mechanics outside buff/debuff/CC stat lines. Summary section order:
Stats the unit benefits from → Damage (includes primary damage type) →
Buffs → Debuffs → Crowd Control → Special Effects. Under `#### Special Effects`, use separate `##### Provides`
and `##### Requires` subsections.
Line format (no Provides/Requires prefix on each bullet):

`{label} ({tier}) — {targeting}`

- **Provides** — use descriptive labels (not skill names): e.g. instant defeat,
  invincibility, summoning (includes named companions), marked target (focus
  fire), ally empower, DoT conversion, dispel, fatal-blow save, stat steal,
  ally positioning link, ally blessing, sleep (area), spirit form protection.
  **Ally grants:** phrasing like `grants Sparks to allies` or `grants an ally
  Brightfeather` adds `Ally grant (name)`; when allies with that grant can
  inflict DoT or debuffs on enemies in the same skill text, also list
  `Ally DoT on enemies` / `Ally Vitality debuff on enemies` (see
  `detect_ally_grant_effects` in `rewrite-summaries.py`).
- **Requires** — e.g. continuous damage on enemies, magic damage from allies,
  debuff on target (Aging), form or stance active, ally blessing active,
  cooldown-gated trigger, enemy not CC-immune, party composition.

Patterns live in `scripts/rewrite-summaries.py` (`SPECIAL_PROVIDES_RULES`,
`SPECIAL_REQUIRES_RULES`, `BUFF_RULES` including ally ATK SPD phrasing like
`grants all allies N ATK SPD` / `increases the ATK SPD of these allies`,
`DOT_INTERVAL_RE`, and companion/summon helpers). When merging buffs from
several skill chunks, ally-wide targeting is kept over self-only. Regenerate
`heroes-overview.md` after changing them.

## Healing

Some units can _heal_ other units and/or provide shields.
Healing is not to be mistaking with the "healing" stat, but can rather be detected
from texts like "restoring 45% HP" or "restoring HP". If the text includes an
over time" (HoT) phrasing like "over 2s" it counts as "Healing over time".

## Stats the unit benefits from

Listed in each hero summary for synergy matching. Derived from self-buffs
and explicit self-scaling in skill text (`refine_benefit_stats` in
`rewrite-summaries.py`). Omitted as noise: **ATK** from `(ATK-based)` damage
only, companion-only **Max HP** / **Life Drain**, **Healing** that only
restores a summon, and one-off **Initial Energy** lines.

## Stats

Stats can be buffed (increased) or debuffed (decreased).

- Attack (ATK)
- Attack Speed (ATK Spd)
- Haste
- Critical damage (Crit)
- Defense Penetration (DEF Penetration)
- Resilience (Res)
- Vitality (Vit)
- Max HP
- HP
- Lifedrain
- Ranged Defense (Ranged DEF)
- Magic Defense (Magic DEF)
- Physical Defense (Phys DEF)
- Critical Damage Defense (Crit DEF)
- Critical Resistance (Crit Resist)
- Assistance
- Damage taken
- Execution
- Energy on hit
- Healing

When looking for stat effects on skills, the text has to be analyzed as they
are somtimes not easy to spot. For example "reducing their Magic DEF" inidicates
a Magic Defense debuff.



## Anti Crowd-control

- Unaffected
- Steadfast
- Immune
- Resillience / Cleanse
- Dispell (need to be derived from text)

Summary lines use `{type} immunity ({tier}) — {targeting} — {timing}`.
Timing labels:

- Start of battle
- Permanent
- Once (e.g. once per battle, first time only)
- Form (while in a named form or mode)
- On ultimate
- On skill
- Conditional

## Ascension

- Epic
- Epic+
- Legendary
- Legendary+ (new skill)
- Mythic
- Mythic+ (new skill)
- Supreme
- Supreme+ (new skill)
- Paragon 1
- Paragon 2
- Paragon 3
- Paragon 4

## Ex-Weapon levels

New exlusive skills are unlocked at the following levels:

- Ex5
- Ex10
- Ex15
- Ex20
- Ex25
- R2 (Paragon 2)
- R4 (Paragon 4)