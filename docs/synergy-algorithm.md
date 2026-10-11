# Synergy Algorithm

This document explains how the system calculates and ranks synergy between heroes in AFK Journey. The algorithm determines which heroes work best together by matching what one hero provides (the **Provider**) with what another hero needs (the **Receiver**).

## High-Level Overview

Synergy is a one-way relationship: **Provider → Receiver**. A hero might be a great provider for another, but not necessarily vice versa. 

The algorithm evaluates every possible pair of heroes and scores their synergy based on three main paths:
1. **Stat Buffs**: The provider grants stat buffs that the receiver explicitly benefits from (e.g., granting ATK SPD to a hero whose damage scales with attack speed).
2. **Summon Buffs**: The provider buffs allied summons, and the receiver is a hero who fields summons.
3. **Enablers**: The provider satisfies a specific mechanical requirement of the receiver (e.g., applying debuffs for a hero who deals extra damage to debuffed targets).

The final synergy score is the sum of these three paths. The top 5 highest-scoring providers are listed under the receiver's **"Units improving X"** section.

---

## Deep Dive: Scoring Mechanics

The base score for any buff or effect is calculated using its **Targeting** and its **Magnitude**.

### 1. Targeting Weight
Effects that hit more allies or cover a larger area are worth more:
- **All units**: 5.0
- **Area**: 4.0
- **Arc / Multiple targets**: 3.0
- **Single target**: 1.5

### 2. Magnitude Weight
Effects are ranked across the full roster (same effect label; e.g. comparing one hero's shield to all shields):
- **High**: 3.0
- **Average**: 2.0
- **Low**: 1.0

**Base Effect Score** = `Targeting Weight × Magnitude Weight`

*Note: Buffs that apply frequently (but not always) receive a 0.85× penalty. Rare conditional buffs (e.g., only in certain game modes) are ignored entirely for synergy purposes.*

---

## Path 1: Stat Buffs

The algorithm checks the receiver's **"Stats the unit benefits from"** and looks for matching buffs from the provider.

### Special Stat Interactions
- **Haste & ATK SPD**: Haste increases attack speed. If a receiver wants ATK SPD, a Haste buff counts towards it and receives a **1.25× bonus multiplier**.
- **Shields vs Max HP**: Shields extend survivability (a unit can take more damage before dying) but do not change the unit's Max HP value. Effects that scale on Max HP are unaffected by shields. Ally **Shield** buffs only score for receivers who explicitly benefit from **Shield** (typically heroes who self-shield in their kit), not for heroes who only scale on **Max HP**.
- **Healing**: Heroes who consume or lose their own HP to cast skills (e.g., Talene) explicitly look for healers.

### Signature Skill Fuel (Casting Speed)
Heroes rely heavily on their "Signature Skill" (often their Ultimate). If a receiver's signature skill is slow to cast, buffs that speed it up (Haste, ATK SPD, Energy Recovery) are heavily boosted:
- **Speed Multiplier (Haste/ATK SPD)**: Slow (1.6×), Average (1.2×), Fast (1.0×)
- **Energy Multiplier**: Slow (1.3×), Average (1.05×), Fast (1.0×)

*Note: Energy recovery has a global 0.72× penalty to prevent "battery" heroes (like Rowan) from dominating every single synergy list.*

### High-Damage Ultimate Carries
Heroes tagged **`high-damage-ult`** whose ultimate is their main damage spike—but who lack **`high-initial-energy`** or **`battle-start-ult`**—benefit more from ally Energy than from comparable Haste. For these receivers only, ally Energy (ongoing buffs and battle-start grants) receives an extra **2.25×** multiplier so batteries rank above Haste providers when effects are otherwise similar. Stronger Haste buffs or multi-effect providers can still win overall.

Current tagged examples: Frieren, Marcille, Shemira. Natsu has both `high-damage-ult` and `high-initial-energy`, so this preference does not apply.

### Implicit Fuel
Even if a hero doesn't explicitly list Energy or ATK SPD as a needed stat, if their signature skill is slow or average, the algorithm will still value these buffs at a reduced rate (0.45× base) because every hero benefits from casting their main skill faster.

### Early Battle Energy
If a receiver's signature skill is a **slow Ultimate**, or its **first ultimate
cast** is slow (low effective Initial Energy, fill time above the fast
threshold, and not battle-start / free first cast), providers who grant energy
*immediately at the start of battle* (e.g., Lyca, Pandora, Thador) receive a
massive score boost. Recurring ult speed can still be fast after post-ult Haste
(e.g. Tasi); those receivers use the slow early-battle multiplier for the
first-cast path.

Early-battle Energy uses **flat single-target reach** for every provider (Units
improving scores one receiver, not roster-wide AoE). Numeric grants scale by
amount — lieutenant Energy at battle start (e.g. Thador's 350) uses the same
formula as other start-of-battle batteries. Picks with battle-start Energy
reasons stay visible in Units improving even when the provider is otherwise a
common roster-wide buffer.

### Positional & Proximity Restrictions
- **Positional Tiles**: Buffs that require standing on a specific tile are ignored for highly mobile receivers.
- **Proximity Auras**: Buffs tied to an aura around the provider (e.g., Shakir's Lupine Aura) only score for receivers who fight in melee range (attack range ≤ 3.5).

### Buff Zones
Ally buffs for a zone the provider places (e.g., Perseus fertile ground,
Estrilda's zone) carry a `zone_anchor` in `ai.json`. Global buffs have none.

- **Zone anchor**: `enemy_backline`, `enemy_target`, `caster`, `summon`, or
  `fixed_tile`. It resolves to a zone location: `enemy_backline` stays
  `enemy_backline`; `enemy_target` and `summon` are `frontline`; `fixed_tile`
  is `ally_backline`; `caster` takes the provider's battlefield position.
- **Receiver position**: `battlefield_position` is derived from range and tags.
  Ranged is `ally_backline`. Melee with `assassin`, `backline-assassin`, or
  `self-repositioner` is `enemy_backline`. Other melee is `frontline`.
  `roaming`, and any correction, comes only from `battlefield_position` in
  `overrides.json`. A receiver without a position counts as `frontline`.
- **Reach**: `BUFF_ZONE_REACH_WEIGHT` maps (zone location, receiver position)
  to the share of the zone the receiver stands in.

| Zone \ Receiver | enemy_backline | frontline | ally_backline | roaming |
|---|---|---|---|---|
| enemy_backline | 1.0 | 0.5 | 0.0 | 0.5 |
| frontline | 0.5 | 1.0 | 0.0 | 0.5 |
| ally_backline | 0.0 | 0.25 | 1.0 | 0.0 |
| roaming (caster) | 0.5 | 0.5 | 0.0 | 0.5 |

- **Scoring**: the stat path multiplies the buff score by the reach weight.
  Zero reach skips the buff. `score_buff_zone_synergy` adds presence credit
  for anchored buffs the stat path did not credit:
  `SYNERGY_STAT_BUFF_REACH_WEIGHT × magnitude × reach ×
  BUFF_ZONE_PRESENCE_MULT` (0.6). The reason reads
  `Enables Buff zone (<location>) via <label> (<targeting>, <magnitude>)`.
- **Direction**: scoring runs provider → receiver. The receiver's position
  picks the column, the provider's anchor picks the row. Perseus benefits
  from Estrilda's zone; Estrilda does not benefit from Perseus's.
- **Grouping uplift**: an enemy-backline zone reaches a frontline receiver at
  only 0.5. `synergy_pair_extras` rescores that pair with the weight raised
  to 1.0 and stores the gain as `zone_grouping_uplift` on the pick (Mix index
  field `groupingUplift`). Mix mode adds it when an enemy-grouping hero is on
  the team.

### Temporary Stat Buffs
Receivers that require `Temporary ally stat buffs` (e.g., Perseus) value
providers whose ally buffs are temporary.

- **Stat set**: the "Qualifying stats" table in `.cursor/MECHANICS.md`
  (`RUNTIME_QUALIFYING_STAT_LABELS` in `buff_persistence.py`), including
  Movement speed and rivalry DMG Boost / DMG Reduction. Skill-granted
  Damage dealt / Damage taken, Max HP, Attack range, Skill Power,
  Ultimate Power, Proficiency, shields, Energy grants, CC immunity, and
  extra-damage procs are excluded.
- **Persistence**: derived from skill text (`buff_persistence.py`). Only
  `temporary` buffs count. Finite durations, aura or zone exit, and
  "for N s" wording mean temporary; "permanently" and "during battle" mean
  permanent.
- **Label bonus**: `1 + TEMP_BUFF_LABEL_BONUS ×
  (min(n, TEMP_BUFF_LABEL_CAP) − 1)` for n distinct buff labels (0.25, cap 6).
- **Frequency bonus**: `1 + TEMP_BUFF_FREQUENCY_BONUS × (min(applications,
  TEMP_BUFF_FREQUENCY_CAP) − 1)` (0.15, cap 5). Applications are
  `round(TEMP_BUFF_WINDOW_SECONDS / cooldown)` (30 s window); a
  battle-start buff counts once and takes a 1.4× multiplier.
- **Require multiplier**: `TEMP_BUFF_REQUIRE_MULT` scales the enabler (1.0,
  neutral).
- **Distinct allies**: a require with `distinct_allies` set needs buffs from
  that many different allies. In Mix mode the second provider counts at 1.5×.
  The Mix index carries `tempBuff` (pick field `temp_buff_score`) and
  `distinctAllies`.

---

## Path 2: Summon Buffs

If the receiver summons units (e.g., Florabelle, Cecia), the algorithm looks for providers who specifically buff allied summons.
- **Summon Targeting Weight**: Fixed at 3.0.
- The score is calculated as `3.0 × Magnitude Weight`.

---

## Path 3: Enablers

Some heroes have unique mechanics listed under **"Requires"** (e.g., "Requires magic damage from allies" or "Requires knocked up enemies").

The algorithm scans the provider's kit to see if they fulfill these requirements. The score depends on how reliably and widely the provider applies the effect.

**Enemy grouping:** receivers with an **Enemy grouping** require (e.g. Faramor's
Sanctified Circle) value curated providers tagged `enemy-grouping`. Matching uses
structured displacement or area control reach, with extra weight for battle-start
openers. Untagged displacement alone does not qualify.

### Defining Tier Multipliers
If the receiver's requirement is unlocked at a high ascension tier (Ex-Weapon or Supreme+), it is considered a "unit-defining" mechanic and the synergy score is multiplied:
- **Mythic+ / EX+5**: 1.5×
- **EX+10**: 1.6×
- **Supreme+**: 1.7×
- **EX+15**: 1.8×

---

## Reverse Index: "Units benefitting most from X"

At the bottom of a hero's synergy section, you will see a list of heroes who benefit most from them. This is a simple reverse-lookup: it lists all the heroes who have this provider in their Top 5. 

If a provider is in more than 10 heroes' Top 5 lists, the algorithm caps the display at the top 10 strongest pairings and provides a short explanation of why this provider is so universally desired (e.g., "Haste buffs on multiple allies fuel slow signature skills").