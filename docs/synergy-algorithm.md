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
If a receiver's signature skill is a **slow Ultimate**, providers who grant energy *immediately at the start of battle* (e.g., Lyca) receive a massive score boost.

### Positional & Proximity Restrictions
- **Positional Tiles**: Buffs that require standing on a specific tile are ignored for highly mobile receivers.
- **Proximity Auras**: Buffs tied to an aura around the provider (e.g., Shakir's Lupine Aura) only score for receivers who fight in melee range (attack range ≤ 3.5).

---

## Path 2: Summon Buffs

If the receiver summons units (e.g., Florabelle, Cecia), the algorithm looks for providers who specifically buff allied summons.
- **Summon Targeting Weight**: Fixed at 3.0.
- The score is calculated as `3.0 × Magnitude Weight`.

---

## Path 3: Enablers

Some heroes have unique mechanics listed under **"Requires"** (e.g., "Requires magic damage from allies" or "Requires knocked up enemies").

The algorithm scans the provider's kit to see if they fulfill these requirements. The score depends on how reliably and widely the provider applies the effect.

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