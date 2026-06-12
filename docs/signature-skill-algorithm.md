# Signature Skills

This document explains how the system identifies a hero's **Signature Skill** and how that skill's speed and mechanics influence team building and synergy rankings in AFK Journey.

## High-Level Overview

In AFK Journey, every hero has a kit full of different abilities, but the algorithm identifies one specific ability as their **Signature Skill**. This is the single skill that most characterizes how the hero is played and defines their identity in combat. 

While this is often the hero's Ultimate, it isn't always. For some heroes, their identity revolves around a battle-start effect, a core active skill, or a unique passive. 

The Signature Skill is crucial because its **casting speed** (Slow, Average, or Fast) dictates what kind of support the hero needs. Heroes with slow signature skills desperately need "fuel" (Haste, Attack Speed, and Energy) to come online, and the algorithm heavily rewards teammates who provide it.

---

## Deep Dive: Determining the Signature Skill

The algorithm determines a hero's Signature Skill through a mix of automated calculation and manual curation.

### 1. Indicators of a Signature Skill
When determining which skill defines a hero, the system looks for:
- **Enhancements**: Skills that receive major upgrades from Exclusive Weapons (EX) or Supreme+ unlocks.
- **Unique Mechanics**: Abilities that introduce mechanics few other heroes share (e.g., summoning a specific companion, creating a unique battlefield zone).
- **Core Output**: The skill that provides the vast majority of the hero's exceptional damage, healing, or buffs.
- **Battle-Start Setup**: Skills that dictate the team's formation or apply massive effects the moment the battle begins.

### 2. Calculated vs. Override
By default, the system calculates the "best repeatable, buffable skill" (Ultimate, Skill 1, Skill 2, etc.). However, manual overrides are applied when a hero's true identity lies elsewhere. The final result is the **Effective Signature Skill**.

---

## Deep Dive: Synergy Fuel (Casting Speed)

Once the Signature Skill is identified, the algorithm evaluates its **Speed** (Fast, Average, or Slow). This speed directly impacts the hero's synergy scores with support units.

### 1. Fueling Slow Signatures
Heroes with "Slow" signature skills need help casting them. The algorithm applies a **Signature Fuel Multiplier** to buffs that accelerate casting (Haste, ATK SPD) or generate Energy.

**Speed Multipliers (Haste & ATK SPD buffs):**
- **Slow**: 1.6× score boost
- **Average**: 1.2× score boost
- **Fast**: 1.0× (no boost)

**Energy Multipliers (Energy Recovery buffs):**
- **Slow**: 1.3× score boost
- **Average**: 1.05× score boost
- **Fast**: 1.0× (no boost)

*(Note: Energy recovery has a global 0.72× penalty applied before these multipliers to prevent "battery" heroes from dominating every single synergy list).*

### 2. Implicit Fuel
Normally, a hero only scores synergy points for stats they explicitly benefit from. However, because casting speed is universally important, the algorithm uses **Implicit Fuel**. 

Even if a hero's stat profile doesn't explicitly list Energy or ATK SPD as a needed stat, if their signature skill is Slow or Average, the algorithm will implicitly value these stats at a baseline of **0.45×**. This ensures slow heroes always appreciate a battery or haste-buffer, even if their damage doesn't scale directly with those stats.

### 3. Early Battle Energy
If a hero's signature skill is a **Slow Ultimate**, getting to that first cast is the most dangerous part of the fight. 

Providers who grant energy *immediately at the start of battle* (or right after) receive a massive, specialized score boost when paired with these heroes:
- **Slow Ultimate**: 1.25× multiplier
- **Average Ultimate**: 1.0× multiplier
- **Fast Ultimate**: 0.85× multiplier (penalty, as they don't need the early rush)

---

## Fallback Mechanics (Non-Buffable Signatures)

Sometimes, a hero's curated Signature Skill is an Ultimate that **cannot be buffed** (e.g., it has a fixed cast time, triggers automatically at a certain threshold, or doesn't benefit from Haste). 

If a signature skill is non-buffable but still slow, the algorithm uses a **Synergy Fuel Fallback**:
- It looks at the hero's calculated *repeatable* skills (like their Skill 1 or Skill 2) to determine their "synergy speed."
- This ensures that "fuel" buffs (like Haste) are targeted at the skills that can actually benefit from them, rather than wasting synergy points trying to speed up an un-speedable Ultimate.