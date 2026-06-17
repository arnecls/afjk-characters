# Movement Detection

This document explains how the system determines a hero's movement pattern in AFK Journey. A hero's movement dictates how they navigate the battlefield, which in turn affects their synergy with other heroes—especially those who rely on positional buffs or proximity auras.

## High-Level Overview

In combat, heroes don't just stand still; they dash, teleport, walk into melee range, or stay rooted in the backline. The algorithm categorizes every hero into one of five movement labels:

- **`stationary`**: Rarely moves from their starting position (e.g., backline mages and snipers).
- **`mostly stationary`**: Moves slightly to get in range, but generally holds a position.
- **`moving`**: Actively walks or dashes across the battlefield to engage enemies (e.g., melee fighters).
- **`high movement`**: Constantly repositioning, teleporting, or diving deep into enemy lines.
- **`moving / stationary`**: A special label reserved for dual units (like the Celestials Twins) where one unit moves and the other stays put.

### Why Movement Matters
Movement is a critical factor in the synergy algorithm:
1. **Positional Tile Buffs**: Heroes that grant buffs to specific tiles (like Gunnar or Hugin) have terrible synergy with `moving` or `high movement` heroes, because those heroes will immediately walk off the buff tile. The algorithm automatically penalizes these pairings.
2. **Proximity Auras**: Heroes with short-range auras (like Shakir's Lupine Aura) only synergize with heroes whose movement and attack range naturally keep them close enough to benefit from the aura.

---

## Deep Dive: How Movement is Calculated

Determining a hero's movement isn't as simple as checking their class. The algorithm uses a multi-step process, combining text-based heuristics, mathematical range weighting, and class-based safety nets.

### 1. Text-Based Heuristics
Before looking at any numbers, the script (`scripts/rewrite-summaries.py`) scans the hero's skill text for specific phrases that dictate their movement behavior. 

- **Off-Battlefield**: If a hero leaves the battlefield entirely (e.g., Damian building his toy chariot), they are marked as `stationary`.
- **Constant Movers**: Phrases like "moves while attacking" or "cannot be targeted while moving" (e.g., Rhys) immediately flag the hero as `high movement`.
- **Summon Controllers**: Heroes who stand still while their summons do the fighting (e.g., Bryon) are flagged as `stationary`.
- **Explicit Repositioning**: Phrases like "leaps to the target," "teleports," or "dashes" flag the hero as `moving` or `high movement`.
- **Pull-to-Self**: If a hero forces enemies to come to them (e.g., Nara), they are flagged as `mostly stationary` because they don't need to walk to their target.

*Note: The script is smart enough to ignore movement phrases that apply to a hero's summons rather than the hero themselves.*

### 2. Weighted Attack Range
If the text doesn't explicitly define the hero's movement, the algorithm calculates their **Weighted Attack Range**. 

It looks at the `Skill Range` of the hero's core active skills (Ultimate, Skill 1, and Skill 2) and averages them based on their cooldowns. 

The resulting average range (in tiles) determines the movement label:
- **Average Range < 4 tiles**: `moving`
- **Average Range ≤ 6 tiles**: `mostly stationary`
- **Average Range > 6 tiles**: `stationary`

### 3. The Melee Class Floor
Sometimes, a melee hero's skill text doesn't explicitly state their range, or their skills have artificially large ranges (like a full-screen shockwave) that skew the math. 

To prevent a Warrior or Rogue from being incorrectly labeled as `stationary`, the algorithm applies a **Melee Floor**. If a hero belongs to a melee class (Warrior, Rogue, or Tank), the algorithm forces their label to `moving`.

**Exceptions to the Floor:**
The melee floor is skipped if the hero has specific behavior tags that imply they *should* stand still:
- `static-tile-buffer`: The hero is designed to stand on a specific tile.
- `summoner`: The hero is a tank/warrior who summons units to fight for them while they hang back.

### 4. Manual Overrides
If all automated detections fail or produce an inaccurate result due to a unique game mechanic, the system relies on manual override files:

- **`data/movement_overrides.json`** — force a movement label and note (e.g. Nara pulling enemies to her).
- **`data/melee_overrides.json`** — set `is_melee` or `is_dual_range` when the melee class floor or weighted range math is wrong.

Example movement override:

```json
{
  "Nara": {
    "movement": "mostly stationary",
    "note": "pulls enemies; moves on failed pull"
  }
}
```

This multi-layered approach ensures that every hero's movement profile accurately reflects how they actually play in the game, leading to smarter synergy recommendations.