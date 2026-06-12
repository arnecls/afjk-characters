# Replacement Algorithm

This document explains how the system calculates and ranks replacement suggestions for heroes in AFK Journey. When you don't have a specific hero, or need a substitute for a specific game mode, the replacement algorithm finds the closest matches based on kit similarity and absolute strength.

## High-Level Overview

Unlike Synergy (which looks for complementary pairs), Replacement looks for **substitutes**. The algorithm compares a **Source Hero** against all other **Candidate Heroes** to find units that fulfill the same role.

Replacements are grouped into up to 7 distinct categories:
1. **Similar Skills**: Heroes with similar overall playstyles and mechanics.
2. **Buff**: Heroes who provide similar buffs to allies.
3. **Healing**: Heroes with similar healing output and mechanics.
4. **Energy**: Heroes who provide similar energy generation for the team.
5. **Damage**: Heroes with similar damage profiles and damage types.
6. **Debuff**: Heroes who apply similar debuffs to enemies.
7. **Crowd Control (CC)**: Heroes who apply similar control effects.

For each category, the algorithm returns the top 3 candidates that meet a minimum similarity threshold and a competitive tier floor.

---

## Deep Dive: Scoring Mechanics

Replacement scoring relies on **Coverage**: how much of the Source Hero's output the Candidate Hero can replicate. 

Unlike Synergy, which compares heroes to their same-role peers, Replacement uses **Absolute Global Strength**. This means a Support hero's healing is directly compared to a Tank's healing using raw throughput numbers, ensuring that a suggested replacement can actually output the required numbers.

### 1. The Coverage Formula
For any given category (e.g., Buffs), the algorithm builds a "Profile" for both the Source and the Candidate. The profile assigns a weight to every effect (e.g., ATK buff, DEF buff).

The coverage score is calculated as:
`min(Candidate Output / Source Output, 1.0) × Source Weight`

This means:
- If the Candidate provides 100% or more of what the Source provides, they get full points for that effect.
- If the Candidate provides 50%, they get half points.
- If the Candidate provides something the Source doesn't, it is ignored (it doesn't help replace the Source's specific job).

The final score is a percentage (0.0 to 1.0) representing how well the Candidate covers the Source's profile. The minimum required score to be listed as a replacement is **0.5 (50%)**.

### 2. Meta Tier Floor (Prydwen Tiers)
A replacement is only useful if they are viable in the current meta. The algorithm checks the [Prydwen Tier List](https://www.prydwen.gg/afk-journey/tier-list) for overlapping game modes (AFK Stages, Dream Realm, PvP).

- **The Rule**: A candidate is excluded if they are **2 or more tiers below** the Source Hero across *all* overlapping game modes.
- Example: If the Source is S+ in Dream Realm, a candidate who is B tier in Dream Realm will be rejected, even if their skills are mathematically identical.

### 3. Similarity Boosts
To break ties and provide more cohesive team-building suggestions, candidates receive a score boost if they share traits with the Source:
- **Same Faction**: 1.2× multiplier.
- **Same Role Category** (e.g., Mage, Tank): 1.2× multiplier.

---

## Category-Specific Rules

### Similar Skills (Tags)
Instead of math-heavy profiles, this category uses curated **Behavior Tags** (e.g., `aoe-damage`, `summoner`, `cheat-death`). 
- The score is calculated using **Jaccard Similarity**: `(Shared Tags) / (Total Unique Tags)`.
- Candidates must share at least 1 tag with the Source to be considered.

### Damage
Damage profiles look at both the raw damage throughput and the *type* of damage (Physical, Magic, True Damage, DoT).
- **True Damage Boost**: True Damage (which ignores DEF) is highly valued. True damage output is multiplied by **1.5×** in the profile.
- **Blend**: The final damage replacement score is a blend: **65%** based on matching True Damage types, and **35%** based on general damage throughput coverage.

### Healing
Healing profiles look at raw HP restored and the *method* of healing (Direct Burst vs. Healing Over Time).
- **Blend**: The final healing replacement score is a blend: **65%** based on raw healing throughput coverage, and **35%** based on matching the specific healing methods.

### Crowd Control (CC)
CC profiles are weighted by the **duration** of the control effect in seconds (e.g., a 3-second stun is worth more than a 1-second stun).
- **Signature CC Boost**: If the CC effect is tied to the hero's Signature Skill (their defining ability), its weight is multiplied by **1.5×**.