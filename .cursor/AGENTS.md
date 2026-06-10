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

- Stun (unable to move or act)
- Bind (immobilize, entangle, imprison; cannot move but may still act)
- Knock down (unable to move or act)
- Knock up (unable to move or act)
- Knock back (unable to move briefly; forced reposition backward)
- Frighten (run around in panic, no casting)
- Silence (no spell casting)
- Charm (cannot use ultimate)
- Sleep (hypnotized; cannot move or act)
- Displace (force new position; pull/teleport without knock immobility)
- Blind (cannot use normal attacks)
- Interrupt (stop ultimates)
- Taunt (force attack on caster)

Enemy freeze/frozen/freezing text maps to **Bind** (often paired with damage in
the same skill). Battle-time pause and freeze-and-defeat execute are special
mechanics, not standalone CC types.

These types need to be derived from the text.
For example:

- "knocking them back" -> Knock back
- "knocking them into the air" -> Knock up
- "knocking them down" / "knocks the enemy down" -> Knock down
- "hypnotizing all enemies" -> Sleep
- "stunning them" -> Stun
- "unable to move" / "immobilize" / "bind" -> Bind
- "freezing them" / "freeze enemies" -> Bind
- "pulling in enemies" -> Displace

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

## Fully ascended comparison

Synergy ranking and cross-hero magnitude bands assume every hero is **fully
ascended**: all skill slots unlock (Ultimate through Supreme+ / EX tiers), and
numeric comparison uses the **strongest parseable value** per effect label
across skill level lines — not the base unlock value. This is implemented in
`add_effect()` / `_merge_effects()` in `rewrite-summaries.py` (max numeric
wins). Processed JSON may set `is_max_known: false` when higher tiers still
use `(scaled)` placeholders in source text.

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

## Behavior (movement & casting speed)

Each hero in `heroes-overview.md` starts with `### <name>'s behavior`:

- **Movement** — `stationary`, `mostly stationary`, `moving`,
  `high movement`, or `moving / stationary` (dual units). Derived from
  per-skill `Skill Range`, cooldown-weighted attack ranges, and
  repositioning phrases in skill text. Special cases in
  `compute_movement()` in `rewrite-summaries.py`: off-battlefield heroes
  (Damian), summon controllers (Bryon), dual units (Twins), constant
  movers (Rhys), dormant/rooted cycles (Zorya, Ulmus), explicit hero
  repositioning (Rowan), brief aerial reposition (Scarlita), pull-to-self
  (Nara), normal-attack range priority (Walker). Range uses
  Ultimate/Skill1/Skill2 only (not Ex). Summon/companion movement and
  dormant sentences are excluded before range and repositioning analysis.
  Data from
  [heroes2.md](heroes2.md); falls back to [Heroes.md](Heroes.md) (aliases:
  Twins → Elijah & Lailah).
- **Signature skill** — the one skill that most characterises how the
  hero is played. Stored in `data/signature_skills.json` (key =
  display name from `heroes-overview.md`). Each entry has
  `signature_calculated` (best repeatable, buffable skill by category:
  `ultimate`, `skill1`, `skill2`, `skill4`) and optional
  `signature_override` when the curated identity skill differs.
  Effective signature = `signature_override ?? signature_calculated`.
  Optional `speed_override` applies to the effective signature.
  Skill names resolve from `heroes_data.json`; shown in the behavior
  block as `**Signature skill**: {name} [(ultimate)]`.
  Often the Ultimate, but not always. Pick the skill that defines the
  unit's identity in combat.
  **Indicators:** enhanced by Ex / Supreme+ (`Enhance Force`); unique
  mechanic few others share; exceptional damage or buff; battle-start or
  formation setup.
  **Synergy fuel fallback** — when the effective signature is a
  non-buffable **Ultimate** that is still slow (not fast/battle-start),
  `signature_calculated` drives `synergy_signature_speed` instead.
  Non-ultimate signatures (e.g. Bonnie's Skill1) keep primary speed so
  fuel targets identity, not a side ult.
- **Placement constraints** — optional top-block bullets when skill text
  ties ally buffs to grid placement or auto-selected allies:
  **Ally composition** (`ally_placement` + `ally_composition` kinds) and
  **Self placement** (`self_placement`). Detected in
  `detect_placement_constraints()`; stored in
  `behavior.placement_constraints`. Overrides in
  `data/placement_constraint_overrides.json`.
- **Skill overview** — `#### Skill overview` subsection with rows for
  **Signature skill** (labeled **Signature skill (ultimate)** when the
  ultimate row is omitted), **Ultimate** (only when signature is not the
  ultimate), and **Non-ultimate**. Each row lists only non-`none`
  indicators among `speed`, `heal`, `buffs`, `debuffs`, `damage` (damage
  last; `high` / `medium` / `low`; speed `slow` / `normal` / `fast`).
  When any tier deals **HP loss**, **Max HP-based damage**, or **True
  damage**, a final `- **True damage**: {type} \`{mag}\`, …` line lists types
  (peak per type across tiers; p75 for non-ultimate).
  Computed in `compute_skill_overview()` in
  `rewrite-summaries.py`; stored in `behavior.skill_overview`. Speed uses
  `compute_per_skill_speeds()` thresholds. Damage scores per skill
  section from chunk text (roster quantiles). Heal/buffs/debuffs peak
  magnitudes from `skill_slices` effects. Non-ultimate row aggregates
  Skill1/Skill2/Ex with **p75** per metric type. Synergy fuel still uses
  `signature_skill_speed` / `synergy_signature_speed` in processed JSON
  (not shown in the markdown block).
  After the metric rows (and optional True damage line), **per-category
  summaries** appear as `##### {slot}` headers with a short paragraph
  underneath. Summaries come from `data/heroes_data_skill_summary.json`
  (key = display name, then `category` from processed JSON:
  `ultimate`, `skill1`–`skill5`). Labels: Ultimate, Skill 1, Skill 2,
  Legendary+, Ex. Skill, Supreme+.

**Skill summary authoring** (AI-generated, not scripted):

- Read fully ascended `description` from `heroes_data_processed.json`.
- Cross-check against `description_lite` in `heroes_data.json` for each
  skill slot — it is the preferred source for validating mechanics and
  catching missing or invented effects.
- Write a **short mechanic summary** using **generalized game vocabulary**
  from `data/schema/game_properties.schema.json` (damage types, CC,
  stats, immunities, battle phases) and effect labels in
  `data/schema/skills.schema.json`.
- **No numbers** (no `%`, tile counts, cooldowns, energy values).
- **No hero-specific wording** — no hero names, skill names, companion
  or grant names, or skill-only imagery (feather, lance, dark cloud,
  winged form, intel, party, etc.). Use generic terms instead:
  transformation, companion, summon, mark, ally grant, DoT zone,
  HP-loss, observation stacks, formation, bond, channeling.
- Use schema vocabulary in **display form**: `HP-loss`, `knock down`,
  `knock back`, `knock up` — not enum tokens like `hp_loss` or
  `knock_down`.
- Prefer established game terms over flavor nouns: **circular area** or
  **zone** (not magic circle), **melee buff state** (not combat stance),
  **area with most enemies** (not dense group), **counterattack** (not
  retaliate), **channel then single-target magic damage** (not charged
  fireball), **sequential single-target shots** (not artillery salvo),
  **line AoE** (not piercing stun line), **untargetable aerial AoE
  damage** (not repeated spear thrusts), **AoE zone** (not storm centered),
  **mobile aura zone follows caster** (not empowerment sphere follows),
  **removed from battlefield** (not separate dimension), **clone** (not
  illusion copy).
- Describe **what happens** (mechanics/effects), not ascension tier
  labels or flavor nouns tied to one hero.
- **Punctuation conventions** (avoid ambiguous phrasing):
  - **Passive / active:** prefix `Passive:` and `Active:` when both
    appear, or split into two sentences.
  - **Participial phrases:** comma before `-ing` clauses that describe
    the caster's action (`enemy, dealing …` not `enemy dealing …`).
  - **CC types:** separate CC from follow-up with comma or `then`
    (`knock back, then stun` not `knock back stun`).
  - **Abbreviations:** expand `regeneration` (not `regen`), `trigger` /
    `bonus effects` (not `proc`), `normal attacks` (not `normals`),
    `alternate form` (not `alt form`); keep ATK/DEF/HP/AoE/DoT.
  - **HP wording:** use **HP-loss** for the damage type; **max HP
    reduction** for cap penalties; **ally losing HP** for heal triggers.
  - **Lists:** Oxford commas for stat/effect lists (`HP drain, haste
    reduction, and vitality reduction`).
- Validate with `just validate` (`skill_summary` check group).

Regenerate: `python3 scripts/generate-heroes-overview.py` (or `just overview`).

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
   **Defining-tier enablers:** requirements from Ex-Skills (`Mythic+`,
   `EX+n`) and `Supreme+` skills are unit-defining and score higher via
   `DEFINING_TIER_SCORE_MULT` in `generate-heroes-overview.py`.
   **Early-battle energy:** providers that grant ally Energy at or right
   after battle start score extra only when the hero's **curated signature
   skill is a slow Ultimate** (`receiver_wants_early_battle_energy` in
   `generate-heroes-overview.py`). Units whose identity is a battle-start
   Skill1/Skill2 (Bonnie, Kulu, etc.) are excluded even if their side
   ultimate is slow.
   **Signature-skill fuel:** Haste/ATK SPD ally buffs are boosted by the
   receiver's effective synergy signature speed (`SIGNATURE_FUEL_SPEED_MULT`:
   slow 1.6×, normal 1.2×, fast 1.0×). Energy recovery uses a lighter
   `SIGNATURE_FUEL_ENERGY_MULT` (slow 1.3×) plus `ENERGY_SYNERGY_SCORE_MULT`
   (0.72×) so batteries do not dominate lists. Slow/normal effective speeds
   also implicitly value Energy and ATK SPD at `IMPLICIT_FUEL_BASE` (0.45×)
   when not in benefit stats.    Buffability
   is detected from skill text (`NON_BUFFABLE_SIGNATURE_RES` in
   `rewrite-summaries.py`).
   **Proximity aura buffs:** provider-attached auras/circles (e.g. Shakir's
   Lupine Aura) are detected in `rewrite-summaries.py`
   (`PROVIDER_PROXIMITY_AURA_PATTERNS`). Ally buffs tied to those zones only
   score for receivers whose **weighted attack range** is melee-close enough
   to stand in the aura (`receiver_can_reach_proximity_aura` in
   `generate-heroes-overview.py`; tunables in `heroes_config.json` →
   `proximity_synergy`). Global buffs (Twins dance, etc.) are unaffected.
   Complements the existing rule that skips **positional tile** buffs for
   **moving/high-movement** receivers.

**Units benefitting most from** at the end of each Synergies block is the reverse index:
heroes who list this unit among their top five synergy partners. When
more than ten such heroes exist, only the ten strongest pairings (by
score) are listed, with a short note on why the provider matches widely.

**Parsing pitfalls** (bad summaries → false synergies): resolve targeting from
the **same sentence/clause** as the buff; do not treat self energy or self
stats as ally buffs; enemy debuffs are not benefit stats; situational ally
buffs (monster fights, ingredients, once per battle) should not rank.

Regenerate: `python3 scripts/generate-heroes-overview.py`

## Synergies (`heroes-overview.md`)

Generated by `scripts/generate-heroes-overview.py`. Up to five allies per hero, ranked by
combined score. **Units benefitting most from** (end of Synergies) lists heroes who
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
   Mage/Tank/Support for Himmel's party composition, ally stat buffs for
   Perseus/Silven). Self-setup labels (Debuff on target (Aging), form/stance,
   boss gates, etc.) are skipped. Requirements on Ex/Supreme+ tiers get a
   defining-tier multiplier (`DEFINING_TIER_SCORE_MULT`). Synergy text uses
   `Enables {label} via {detail}`.

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
  **Ally empower:** when the empowered ally receives conditional immunity
  (e.g. Alna grants the Winter Warrior the same immunity effects), also list
  `Damage and control immunity` in the **Buffs** section (always `high`).
  **Marked target (focus fire):** also list in the **Debuffs** section so
  synergy matching can see which heroes debuff via marking (always `medium`).
  **Ally grants:** phrasing like `grants Sparks to allies` or `grants an ally
  Brightfeather` adds `Ally grant (name)`; when allies with that grant can
  inflict DoT or debuffs on enemies in the same skill text, also list
  `Ally DoT on enemies` / `Ally Vitality debuff on enemies` (see
  `detect_ally_grant_effects` in `rewrite-summaries.py`).
- **Requires** — e.g. continuous damage on enemies, magic damage from allies,
  debuff on target (Aging), form or stance active, ally blessing active,
  passive with internal cooldown, enemy not CC-immune, party composition,
  **Ally stat buffs** (needs temporary stat buffs from allies; matched by
  providers granting many/wide ally buffs, start-of-battle preferred; see
  `match_ally_stat_buffs` in `generate-heroes-overview.py`).

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

Hero stats can be buffed (increased) or debuffed (decreased). Grouping follows
[Hero Stats](https://afk-journey.fandom.com/wiki/Hero_Stats) on the Fandom wiki.

### Basic

- **HP** — health pool; a unit is defeated at zero.
- **ATK** — increases damage dealt.
- **Phys DEF** — reduces physical damage received.
- **Magic DEF** — reduces magic damage received.

### Offensive

- **ATK SPD** — +1% normal attack frequency and attack animation speed per point.
- **Crit** — crit *rate* when dealing damage; each point above the target's
  Crit Resist adds 1% crit rate (not crit damage — see Crit DMG Boost).
- **Haste** — +1% normal attack and skill frequency, and attack animation
  speed, per point. Also affects ATK SPD
- **DEF Penetration** — ignores 1% of the target's Phys DEF and Magic DEF per
  point when dealing damage.
- **Execution** — +1% damage vs targets below 50% HP per point.
- **Crit DMG Boost** — crit damage multiplier when dealing crits; default 150%,
  adjusted ±1% per point vs target Crit DMG DEF (range 120%–300%).

### Defensive

- **Vitality** — +1% effectiveness of received shields and healing (including
  self-heals) per point.
- **Life Drain** — restores HP equal to 1% of actual damage dealt per point.
- **Crit Resist** — reduces incoming crit rate; each point above the attacker's
  Crit subtracts 1% from their crit rate.
- **Ranged DEF** — reduces damage from non-adjacent enemies by 1% per point.
- **Crit DMG DEF** — reduces incoming crit damage multiplier; each point above
  the attacker's Crit DMG Boost lowers the multiplier by 1%.

### Other

- **Healing** — +1% effectiveness of shields and healing *provided by* the unit
  per point (distinct from heal/shield skill effects; see **Healing** above).
- **Assistance** — +1% duration of most buffs the unit provides per point.
- **Energy Regen on Hit** — +1% Energy recovered when the unit takes damage per
  point.
- **Debuff Focus** — +1% duration of most debuffs the unit inflicts per point.
- **Resilience** — −1% duration of most debuffs inflicted on the unit per point.
- **Proficiency** — when lower than enemy level, some skill effects are weakened.

### Rivalry-only stats

These appear on rivalry builds and in rivalry-mode tooltips; omit from normal
hero summaries unless skill text names them explicitly.

- **DMG Boost** / **DMG Reduction** — damage dealt/taken multiplier (100%
  base; ±1% per point of difference).
- **Energy Regen Reduction** — reduces Energy recovered by targets when they
  take damage from the unit.

### Not roster stats (skill effects)

Do not list these as hero stat types; detect them as buffs, debuffs, or special
effects instead.

- **Damage taken** — combat modifier (e.g. damage taken reduction, damage taken
  debuff), not a character-sheet stat.
- **Max HP** — scaling phrase in skills (`max HP`, `% of max HP`); not a
  separate wiki stat column (use **HP** for the health pool).
- **Dodge chance** — skill-granted avoidance (e.g. Eironn's shield), not a base
  stat.
- **Movement speed** — repositioning / slow effects in skill text, not a base
  stat.

When looking for stat effects in skill text, wording is often indirect. For
example, "reducing their Magic DEF" is a **Magic DEF** debuff; "increasing her
Crit DMG Boost" is an offensive buff; "Crit" alone refers to crit rate.

## Anti Crowd-control

- Unaffected (immune to all control effects)
- Steadfast (immune to knock down/up/back and displacement)
- Dispell ("removes all their dispellable debuffs"; summaries label **Cleanse**)
- Untargetable (cannot be targeted by spells)
- Immune ("immune to control effects")
- Invincible (immune to damage and cc, untargetable)

Summary lines use `{type} ({tier}) — {targeting} — {timing}` (e.g. Unaffected,
Immune, Steadfast, Cleanse — no extra "immunity" suffix).
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