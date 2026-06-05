# Heroes Overview

Per-hero summaries from [Heroes.md](Heroes.md), plus synergy picks:
stat buffs matching **Stats the unit benefits from**, and **enabler**
partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from Max HP/
shields). Rare conditional buffs score lower.
Regenerate with `scripts/generate-heroes-overview.py` after
`scripts/rewrite-summaries.py`.

## Aliceth - Radiant Wings

### Summary

#### Buffs

- Attack range buff (base) — Single target — `high`
- Brightfeather ally buff (base) — Single target — `high`
- DEF Penetration buff (base) — Single target — `medium`
- Invincible (base) — Self — `high` — conditional (rare)
- ATK buff (Legendary+) — Multiple targets — `medium`
- Fatal blow immunity (Mythic+) — Area — `high` — conditional (rare)
- Healing (Mythic+) — Single target — `low` — conditional (rare)

#### Debuffs

- Execution debuff (base) — Multiple targets — `medium`
- Blind HP loss debuff (EX+15) — Area — `low`

#### Crowd Control

- Move (base) — Single target — `high`
- Stun (base) — Single target — `medium`

#### Special effects

##### Provides

- Brightfeather empower (base) — Single target
- HP threshold strike (base) — Multiple targets
- Instant defeat (base) — Multiple targets
- Invincibility (base) — Single target
- Mark (base) — Multiple targets
- Reposition enemies (base) — Single target
- Untargetable (base) — Multiple targets
- Fatal blow save (Mythic+) — Area

##### Requires

- Cooldown-gated proc (base) — Allies
- Ranged damage from allies (base) — Allies
- Debuff on target (Legendary+) — Enemies

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- DEF Penetration
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium); Enables Debuff on target via ATK debuff (area)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Enables Debuff on target via ATK debuff (multiple targets)
3. **Hepler - Master of Forms** — Max HP via Shield (multiple targets, low); Healing via Healing (multiple targets, medium); Enables Debuff on target via Haste debuff (area)
4. **Lyca - Keeper of Glades** — Enables Ranged damage from allies via ranged attacks; Enables Debuff on target via ATK debuff (all units)
5. **Koko - Wild Child** — Max HP via Shield (single target, low); Healing via Healing over time (single target, high); Enables Debuff on target via Damage taken debuff (area)

## Alna - Frozen Mother

### Summary

#### Buffs

- Healing (base) — Self — `low`
- Max HP buff (base) — Multiple targets — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs

- Haste debuff (base) — Arc — `high`
- Vitality debuff (Supreme+) — Area — `medium`

#### Crowd Control

- Freeze (Supreme+) — Area — `medium`

#### Special effects

##### Provides

- Named companion unit (base) — Self
- Start-of-battle cast (base) — All units
- Summoning (base) — All units
- Damage and control immunity (Mythic+) — Self

#### Damage

- Physical — All units, Arc, Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Alsa - Desert Flare

### Summary

#### Buffs

- Shield (base) — Self — `medium`
- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Movement speed debuff (base) — Area — `medium`
- Energy drain (EX+5) — Single target — `low`
- Magic DEF debuff (EX+5) — Area — `low`

#### Crowd Control

- Immune immunity (base) — Area — Once
- Move (base) — Single target — `high`
- Stun (base) — Single target — `medium`

#### Special effects

##### Requires

- Combat Stance active (base) — Enemies
- Cooldown-gated proc (base) — Enemies

#### Damage

- Magic — All units, Area, Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- Primary damage type (unit): **Magic**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high); Haste via Haste buff (multiple targets, high)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))

## Antandra - Desert Fury

### Summary

#### Buffs

- Damage taken reduction (base) — Area — `low` — conditional (rare)
- Healing (base) — Area — `medium`
- Shield (base) — Self — `low`
- Max HP buff (Legendary+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Area — On skill
- Knock down (base) — Area — `high`
- Stun (base) — Area — `high`
- Taunt (base) — Area — `low`

#### Special effects

##### Requires

- Once per battle (Mythic+) — Allies

#### Damage

- Physical — Arc, Area, Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Physical DEF
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Arden - Oak Sage

### Summary

#### Buffs

- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control

- Pin (base) — Multiple targets — `high`

#### Special effects

##### Provides

- Summoning (base) — Multiple targets

#### Damage

- Magic — Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Energy
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
5. **Soren - Silent Fury** — Energy via Energy recovery (single target, high)

## Atalanta - Fortune Finder

### Summary

#### Buffs

- Haste buff (Legendary+) — Self — `high` — conditional (frequent)
- Healing (Supreme+) — Single target — `low`

#### Debuffs

- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Move (base) — Single target — `high`
- Pin (base) — Single target — `medium`
- Stun (base) — Single target — `medium`

#### Special effects

##### Provides

- Reposition enemies (base) — Single target
- Stat steal (EX+10) — Single target

#### Damage

- Physical — Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Physical DEF
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Athalia - Harbinger of Justice

### Summary

#### Buffs

- Damage taken reduction (base) — Area — `medium` — conditional (frequent)
- Healing (base) — Area — `low` — conditional (frequent)
- Invincible (base) — Self — `high` — conditional (frequent)
- Crit buff (Legendary+) — Self — `low`
- Execution buff (EX+15) — Self — `low` — conditional (frequent)
- Shield (Supreme+) — Single target — `high`

#### Debuffs

- ATK debuff (base) — All units — `medium`

#### Crowd Control

- Unaffected immunity (base) — Area — On skill
- Knock down (base) — All units — `low`

#### Special effects

##### Provides

- Invincibility (base) — Area
- Transform (base) — Area

#### Damage

- Physical — All units, Area, Single target
- True damage — All units, Single target

#### Stats the unit benefits from

- ATK
- Crit
- Execution
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
2. **Evie - Royal Envoy** — ATK via ATK buff (multiple targets, high); Healing via Healing (single target, medium)
3. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
4. **Isabella - The Taken Soul** — Healing via Healing (area, high)
5. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)

## Aurora - Celestial of Dreams

### Summary

#### Buffs

- ATK buff (base) — Multiple targets — `high`
- Haste buff (base) — Multiple targets — `high`
- Invincible (base) — Multiple targets — `high`

#### Debuffs

- Haste debuff (base) — Multiple targets — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Sleep (base) — Multiple targets — `high`

#### Special effects

##### Provides

- Invincibility (base) — Multiple targets
- Start-of-battle cast (base) — Multiple targets
- Summoning (base) — Self

#### Damage

- Magic — Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Magic**

### Synergies

1. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
3. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)
5. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)

## Baelran - Dawnblade

### Summary

#### Buffs

- Healing (base) — Arc — `medium`
- Healing over time (base) — Single target — `low`
- Shield (base) — Self — `low`
- Haste buff (Legendary+) — Self — `low`
- ATK buff (EX+15) — Area — `low`

#### Debuffs

- Max HP debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — Area — `medium`

#### Special effects

##### Provides

- Start-of-battle cast (base) — Arc
- Dispel debuffs (EX+15) — Area

##### Requires

- Specific form active (base) — Enemies
- Boss encounter (Supreme+) — Enemies

#### Damage

- Physical — Area, Single target
- True damage — Area, Single target
- True damage (HP-based) — Arc, Area

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium)
3. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
4. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high); Haste via Haste buff (multiple targets, high)

## Berial - Sinister Jester

### Summary

#### Buffs

- Healing (base) — Single target — `high`
- Invincible (base) — Self — `high`

#### Debuffs

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control

- Frighten (base) — Area — `medium`

#### Special effects

##### Provides

- Invincibility (base) — Single target
- Revive ally (base) — Single target
- Named companion unit (Mythic+) — Single target
- Summoning (EX+5) — Single target

#### Damage

- DoT — Area
- Magic — Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Bonnie - Obsidian Claws

### Summary

#### Buffs

- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs

- ATK debuff (base) — Single target — `medium`
- Haste debuff (base) — Single target — `low`
- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Special effects

##### Provides

- Invincibility (base) — Area
- Transform (base) — Area
- Magic damage amplification (Supreme+) — Single target

##### Requires

- Aging on target (base) — Enemies
- Debuff on target (base) — Enemies
- Magic damage from allies (base) — Allies
- Specific form active (base) — Enemies

#### Damage

- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Magic**

### Synergies

1. **Lily May - Twilight Tracker** — Enables Debuff on target via Energy drain (all units); Enables Magic damage from allies via Magic damage (all units)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Enables Debuff on target via Max HP debuff (area); Enables Magic damage from allies via Magic damage (area)
3. **Natsu - Fire Dragon Slayer Mage** — Enables Debuff on target via Haste debuff (area); Enables Magic damage from allies via Magic damage (area)
4. **Lyca - Keeper of Glades** — Enables Debuff on target via ATK debuff (all units)
5. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Enables Debuff on target via ATK debuff (multiple targets)

## Brutus - Blood Claw

### Summary

#### Buffs

- Lifedrain buff (base) — Single target — `high`

#### Debuffs

- Phys DEF debuff (base) — Area — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Taunt (base) — Area — `high`

#### Damage

- DoT — Area
- Physical — Arc, Area, Single target

#### Stats the unit benefits from

- ATK
- Life Drain
- Max HP
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)
5. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)

## Bryon - Evergreen Sentinel

### Summary

#### Buffs

- Haste buff (Legendary+) — Self — `low`
- Healing (EX+5) — Single target — `high`
- Healing over time (EX+5) — Single target — `high`

#### Debuffs

- Haste debuff (base) — Area — `low`

#### Crowd Control

- Interrupt (base) — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

#### Special effects

##### Provides

- Energy steal (base) — Single target
- Named companion unit (base) — Self
- Start-of-battle cast (base) — Single target
- Summoning (base) — Single target
- Untargetable (EX+5) — Single target

#### Damage

- DoT — Area
- Magic — Single target

#### Stats the unit benefits from

- ATK
- Energy
- Haste
- Max HP
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
3. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
4. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Callan - Grim Soulkeeper

### Summary

#### Buffs

- Shield (base) — Self — `low` — conditional (rare)
- Healing (Supreme+) — Single target — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — All units — `high`
- Pin (base) — Multiple targets — `high`
- Stun (Mythic+) — All units — `low`

#### Special effects

##### Provides

- Damage absorption (allies) (base) — Multiple targets
- Stored damage release (base) — Self

##### Requires

- Stored resource threshold (base) — Enemies

#### Damage

- Magic — Multiple targets
- Physical — All units, Area, Self, Single target

#### Stats the unit benefits from

- Max HP
- ATK
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); ATK via ATK buff (multiple targets, high)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Carolina - Candlelight Specter

### Summary

#### Buffs

- Crit buff (Legendary+) — Self — `low`

#### Debuffs

- Haste debuff (base) — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control

- Freeze (base) — Area — `high`

#### Damage

- Magic — Area, Self, Single target

#### Stats the unit benefits from

- ATK
- Crit
- Primary damage type (unit): **Magic**

### Synergies

1. **Marilee - Forest's Arrow** — ATK via ATK buff (area, high, conditional (frequent)); Crit via Crit buff (single target, low)
2. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)

## Cassadee - Azure Prodigy

### Summary

#### Buffs

- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Magic DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Move (base) — All units — `low`
- Stun (base) — Single target — `low`

#### Special effects

##### Provides

- Ally blessing (base) — Single target

##### Requires

- Blessed ally active (base) — Allies

#### Damage

- Magic — All units, Single target

#### Stats the unit benefits from

- ATK
- Haste
- DEF Penetration
- Primary damage type (unit): **Magic**

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

## Cecia - Requiem of Thorns

### Summary

#### Buffs

- ATK SPD buff (base) — Multiple targets — `high`
- Healing (base) — Arc — `high`
- Lifedrain buff (base) — Area — `low`
- Max HP buff (base) — Single target — `high`

#### Debuffs

- Damage taken debuff (EX+10) — Single target — `medium`

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special effects

##### Provides

- Named companion unit (base) — Self
- Summoning (base) — Arc
- Stat absorb (Mythic+) — Single target
- Permanent stat absorb (EX+5) — Single target

##### Requires

- Target not CC-immune (Mythic+) — Enemies

#### Damage

- DoT — Arc, Single target
- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- ATK SPD
- Life Drain
- DEF Penetration
- Physical DEF
- Magic DEF
- Energy
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
4. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
5. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)

## Chippy - Sidekick

### Summary

#### Damage

- Physical — Single target

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Physical**

### Synergies

_No synergy partners matched stat buffs or enablers._

## Contess - Abyssal Rulekeeper

### Summary

#### Buffs

- Energy recovery (base) — Self — `high`
- Healing (base) — Self — `high`
- Shield (base) — Self — `high`

#### Debuffs

- Energy drain (base) — Multiple targets — `low`
- Max HP debuff (base) — Multiple targets — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control

- Silence (Mythic+) — Single target — `medium`
- Stun (Supreme+) — Single target — `medium`

#### Special effects

##### Provides

- Start-of-battle cast (base) — All units

#### Damage

- Magic — All units, Multiple targets

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Cryonaia - Arctic Revenant

### Summary

#### Buffs

- Shield (base) — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs

- Damage taken debuff (EX+5) — Single target — `medium`

#### Crowd Control

- Immune immunity (base) — Self — Conditional
- Freeze (EX+15) — Self — `low`

#### Special effects

##### Provides

- Isolate enemies (domain) (base) — All units
- Summoning (base) — Area

##### Requires

- Boss encounter (base) — Enemies

#### Damage

- DoT — Area
- Magic — All units, Area, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Magic**

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

## Cyran - Umbral Weaver

### Summary

#### Buffs

- Crit buff (Legendary+) — Self — `low`
- ATK buff (EX+10) — Self — `low`

#### Debuffs

- ATK debuff (Mythic+) — All units — `low`

#### Crowd Control

- Steadfast immunity (base) — Area — Conditional
- Unaffected immunity (base) — Self — Start of battle
- Pin (base) — Area — `low`
- Silence (EX+10) — Single target — `low`

#### Special effects

##### Provides

- Summoning (base) — All units

#### Damage

- Magic — All units, Area, Single target
- True damage — All units

#### Stats the unit benefits from

- ATK
- Crit
- ATK SPD
- Energy
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Marilee - Forest's Arrow** — ATK via ATK buff (area, high, conditional (frequent)); Crit via Crit buff (single target, low)
4. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
5. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)

## Daimon - Forsaken Child

### Summary

#### Buffs

- Lifedrain buff (base) — Single target — `medium`
- Shield (base) — Area — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Crowd Control

- Frighten (Mythic+) — Area — `medium`

#### Damage

- Magic — Area, Self, Single target
- True damage (HP-based) — Area

#### Stats the unit benefits from

- ATK
- Max HP
- Life Drain
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)
5. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)

## Damian - Woody Wonder

### Summary

#### Buffs

- Energy recovery (base) — Area — `medium`
- Healing (base) — Self — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Multiple targets — `high`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Damage

- Magic — All units, Single target

#### Stats the unit benefits from

- ATK
- Energy
- Haste
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Haste via Haste buff (multiple targets, medium)
2. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
4. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)

## Dionel - Venus of Dawn

### Summary

#### Buffs

- ATK SPD buff (Legendary+) — Self — `low`
- Execution buff (Supreme+) — Self — `low`
- Shield (Supreme+) — Self — `low` — conditional (frequent)

#### Debuffs

- Vitality debuff (EX+10) — Single target — `low`

#### Special effects

##### Provides

- Untargetable (base) — Area
- Summoning (Mythic+) — All units
- Execution scaling (Supreme+) — Self

#### Damage

- Physical — Area, Self, Single target
- True damage — All units, Single target

#### Stats the unit benefits from

- ATK
- DEF Penetration
- ATK SPD
- Execution
- Max HP
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)
5. **Aliceth - Radiant Wings** — ATK via ATK buff (multiple targets, medium); DEF Penetration via DEF Penetration buff (single target, medium)

## Dunlingr - Eternal Voice

### Summary

#### Buffs

- Healing (base) — Single target — `high` — conditional (frequent)
- Shield (base) — Self — `medium` — conditional (frequent)
- Damage taken reduction (Legendary+) — Self — `low`
- ATK buff (EX+5) — Single target — `low`
- Haste buff (EX+15) — Single target — `low`
- Lifedrain buff (Supreme+) — All units — `low`

#### Debuffs

- ATK debuff (base) — Area — `medium`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control

- Silence (Supreme+) — All units — `high`

#### Special effects

##### Provides

- Battlefield order (base) — All units
- Heal lock (Curelock) (base) — All units
- Named companion unit (base) — Self
- Summoning (base) — All units
- Ultimate lock (Spellbind) (base) — All units

#### Damage

- Magic — All units, Area, Self, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Max HP
- Haste
- Life Drain
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high); Life Drain via Lifedrain buff (area, low); Healing via Healing (arc, high)
4. **Florabelle - Blooming Maiden** — Max HP via Shield (single target, medium); Haste via Haste buff (multiple targets, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, medium, conditional (frequent)); Healing via Healing (area, medium, conditional (frequent))
5. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)

## Eironn - Stormsword

### Summary

#### Buffs

- Shield (base) — Self — `medium`

#### Debuffs

- Haste debuff (base) — Arc — `medium`
- Magic DEF debuff (base) — Arc — `medium`

#### Crowd Control

- Move (base) — Area — `medium`
- Pin (base) — Single target — `high`

#### Damage

- Magic — Arc, Area, Single target

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Magic**

### Synergies

_No synergy partners matched stat buffs or enablers._

## Elijah & Lailah - Celestial Twins

### Summary

#### Buffs

- Haste buff (base) — All units — `high`
- Healing (base) — Multiple targets — `low`
- Max HP buff (base) — Multiple targets — `high`
- Shield (base) — Single target — `medium`

#### Debuffs

- ATK debuff (base) — Multiple targets — `low`

#### Crowd Control

- Unaffected immunity (base) — Area — On skill
- Move (base) — Area — `high`

#### Special effects

##### Provides

- Ally link (Stellar Bond) (base) — Single target
- Shared HP and Energy (base) — All units

##### Requires

- Ally on bond line (base) — —

#### Damage

- Magic — Area, Single target

#### Stats the unit benefits from

- Haste
- Max HP
- ATK
- Energy
- Physical DEF
- Magic DEF
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)

## Evie - Royal Envoy

### Summary

#### Buffs

- ATK buff (base) — Multiple targets — `high`
- Healing (base) — Single target — `medium`
- Invincible (base) — Self — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Crowd Control

- Move (base) — All units — `high`
- Pin (base) — All units — `high`
- Silence (base) — All units — `high`

#### Special effects

##### Provides

- Invincibility (base) — All units
- Start-of-battle cast (base) — All units
- Summoning (base) — Single target

##### Requires

- Cooldown-gated proc (base) — Allies

#### Damage

- Magic — All units, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Energy
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
4. **Isabella - The Taken Soul** — Energy via Energy recovery (single target, low, conditional (frequent)); Healing via Healing (area, high)
5. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)

## Faramor - Silverfang Mantle

### Summary

#### Buffs

- ATK buff (base) — Area — `low`
- Shield (base) — Self — `high`
- Haste buff (Legendary+) — Self — `medium`

#### Debuffs

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (base) — Area — `low`

#### Special effects

##### Provides

- Summoning (base) — Single target
- Revive ally (Supreme+) — Single target

##### Requires

- Once per battle (EX+10) — Enemies

#### Damage

- Physical — Area, Single target
- True damage — Multiple targets
- True damage (HP-based) — Single target

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Physical**

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

## Fay - Colorful Dancer

### Summary

#### Buffs

- ATK buff (base) — Arc — `high`
- DEF buff (base) — Multiple targets — `low`
- Healing (base) — Arc — `high` — conditional (frequent)

#### Debuffs

- Magic DEF debuff (base) — Multiple targets — `low`
- Phys DEF debuff (base) — Multiple targets — `low`

#### Damage

- Magic — Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Physical DEF
- Magic DEF
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Healing via Healing (arc, high)
3. **Evie - Royal Envoy** — ATK via ATK buff (multiple targets, high); Healing via Healing (single target, medium)
4. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
5. **Isabella - The Taken Soul** — Healing via Healing (area, high)

## Florabelle - Blooming Maiden

### Summary

#### Buffs

- Healing (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Single target — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `medium`
- Haste buff (EX+10) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control

- Immune immunity (Supreme+) — Self — Form

#### Special effects

##### Provides

- Named companion unit (base) — Self
- Summoning (base) — Self
- Ally blessing (Mythic+) — Single target

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- Life Drain
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Frieren - The Legendary Mage

### Summary

#### Buffs

- ATK buff (Legendary+) — Self — `low`
- Haste buff (EX+10) — Self — `low`

#### Debuffs

- Vitality debuff (base) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `low`
- Knock down (Supreme+) — Single target — `medium`

#### Damage

- DoT — All units, Single target
- Magic — Area, Self, Single target
- True damage — All units, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- Primary damage type (unit): **Magic**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high); Haste via Haste buff (multiple targets, high)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))

## Gala - Daughter of Dawn

### Summary

#### Buffs

- Haste buff (base) — Self — `high` — conditional (frequent)
- Shield (base) — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Supreme+) — Single target — `medium`

#### Crowd Control

- Steadfast immunity (Supreme+) — Self — On skill
- Pin (base) — Single target — `medium`

#### Special effects

##### Provides

- Summoning (Mythic+) — Single target

##### Requires

- Boss encounter (base) — Enemies

#### Damage

- Magic — All units, Area, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Energy
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

## Gerda - Soothing Siren

### Summary

#### Buffs

- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — Area — `high`
- Shield (base) — Self — `medium`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Interrupt (base) — Single target — `medium`
- Pin (base) — Multiple targets — `low`
- Stun (base) — Single target — `medium`

#### Damage

- Physical — Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Granny Dahnie - Forest Guardian

### Summary

#### Buffs

- Healing (base) — Single target — `high`
- DEF buff (Mythic+) — Self — `high`
- Healing over time (Mythic+) — Self — `high`

#### Debuffs

- Haste debuff (base) — Single target — `low`
- ATK debuff (Supreme+) — Single target — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Pin (base) — Area — `medium`
- Taunt (base) — Single target — `high`

#### Special effects

##### Provides

- Summoning (base) — Area

#### Damage

- Physical — Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Physical DEF
- Magic DEF
- Haste
- Energy
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
5. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)

## Gunnar - Iron Doom

### Summary

#### Buffs

- Shield (base) — Self — `high`
- Healing (Mythic+) — Single target — `high`
- Invincible (EX+15) — Single target — `high`

#### Crowd Control

- Stun (base) — All units — `low`

#### Special effects

##### Provides

- Summoning (base) — Area
- Invincibility (EX+15) — Single target

#### Damage

- DoT — Area
- Physical — All units, Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- ATK SPD
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Cecia - Requiem of Thorns** — Max HP via Max HP buff (single target, high); ATK SPD via ATK SPD buff (multiple targets, high); Healing via Healing (arc, high)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
5. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)

## Gwyneth - Dragonslayer Knight

### Summary

#### Buffs

- ATK SPD buff (Legendary+) — Area — `low`

#### Debuffs

- Burn debuff (base) — Single target — `medium`

#### Crowd Control

- Pin (base) — Area — `medium`
- Silence (base) — Area — `low`
- Stun (base) — Area — `low`

#### Damage

- DoT — Single target
- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Haste
- Max HP
- Primary damage type (unit): **Physical**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))

## Hammie - Magician

### Summary

#### Buffs

- ATK buff (base) — Single target — `high`
- Healing (base) — Single target — `high`

#### Damage

- Magic — Single target

#### Stats the unit benefits from

- ATK
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
2. **Evie - Royal Envoy** — ATK via ATK buff (multiple targets, high); Healing via Healing (single target, medium)
3. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
4. **Isabella - The Taken Soul** — Healing via Healing (area, high)
5. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)

## Harak - Deepsea Ravager

### Summary

#### Buffs

- Crit buff (base) — Single target — `medium`
- Haste buff (base) — Single target — `high`
- Healing over time (base) — Single target — `medium` — conditional (frequent)
- Invincible (base) — Self — `high`
- Lifedrain buff (Legendary+) — Self — `low`
- Healing (EX+15) — Single target — `low`
- Energy recovery (Supreme+) — Single target — `low`

#### Debuffs

- Execution debuff (base) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle

#### Special effects

##### Provides

- Instant defeat (base) — Single target
- Invincibility (base) — Single target

##### Requires

- Boss encounter (base) — Allies

#### Damage

- Physical — Single target

#### Stats the unit benefits from

- ATK
- Haste
- Crit
- Life Drain
- Max HP
- Energy
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
3. **Florabelle - Blooming Maiden** — Haste via Haste buff (multiple targets, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, medium, conditional (frequent)); Max HP via Shield (single target, medium); Healing via Healing (area, medium, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)

## Hepler - Master of Forms

### Summary

#### Buffs

- Haste buff (base) — Single target — `low`
- Healing (base) — Multiple targets — `medium`
- Shield (base) — Multiple targets — `low`
- Damage taken reduction (Legendary+) — Self — `low`
- Invincible (Mythic+) — Area — `high` — conditional (frequent)

#### Debuffs

- Haste debuff (base) — Area — `high`

#### Crowd Control

- Stun (base) — Area — `medium`
- Taunt (base) — Area — `high`

#### Special effects

##### Provides

- Invincibility (Mythic+) — Area

##### Requires

- Specific form active (base) — Enemies

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- Magic DEF
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Hewynn - Tender Leaf

### Summary

#### Buffs

- Healing (base) — Single target — `high`
- ATK buff (Legendary+) — Self — `low`

#### Crowd Control

- Unaffected immunity (Mythic+) — Self — On skill

#### Special effects

##### Requires

- Cooldown-gated proc (base) — Allies

#### Damage

- Magic — All units

#### Stats the unit benefits from

- ATK
- Energy
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
4. **Isabella - The Taken Soul** — Energy via Energy recovery (single target, low, conditional (frequent)); Healing via Healing (area, high)
5. **Evie - Royal Envoy** — ATK via ATK buff (multiple targets, high); Healing via Healing (single target, medium)

## Himmel - The Legendary Hero

### Summary

#### Buffs

- Shield (base) — Area — `low` — conditional (frequent)
- Haste buff (Legendary+) — Self — `medium`
- ATK buff (Mythic+) — Self — `high`
- Max HP buff (Mythic+) — Multiple targets — `medium`

#### Crowd Control

- Unaffected immunity (base) — Multiple targets — On skill

#### Special effects

##### Requires

- Party composition (base) — Allies
- Boss encounter (Supreme+) — —

#### Damage

- Physical — Area, Multiple targets, Single target
- True damage (HP-based) — All units

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- DEF Penetration
- Primary damage type (unit): **Physical**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Enables Party composition via Support (party slot)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high); Enables Party composition via Mage (party slot)
3. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high); Haste via Haste buff (multiple targets, high); Enables Party composition via Support (party slot)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Enables Party composition via Tank (party slot)

## Hodgkin - Reviled Captain

### Summary

#### Buffs

- Healing over time (base) — Single target — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs

- Energy drain (Mythic+) — Area — `medium`
- Vitality debuff (EX+5) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `low`

#### Special effects

##### Provides

- Summoning (Mythic+) — Area

#### Damage

- Physical — Arc, Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Hugin - Maverick Smith

### Summary

#### Buffs

- ATK buff (base) — Single target — `high`
- Haste buff (base) — Multiple targets — `high`
- Shield (base) — Single target — `high`

#### Damage

- Physical — Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Energy
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

## Igor - Mad Dagger

### Summary

#### Buffs

- Healing (base) — Single target — `low`
- Lifedrain buff (Legendary+) — Self — `low`

#### Special effects

##### Provides

- Summoning (base) — Single target
- Untargetable (base) — Area

#### Damage

- Physical — All units, Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Life Drain
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Cecia - Requiem of Thorns** — Max HP via Max HP buff (single target, high); Life Drain via Lifedrain buff (area, low); Healing via Healing (arc, high)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Indris - Chain Breaker

### Summary

#### Buffs

- ATK buff (Legendary+) — Self — `low`
- ATK SPD buff (Mythic+) — Self — `high`

#### Debuffs

- Magic DEF debuff (base) — Single target — `high`
- Phys DEF debuff (EX+10) — Single target — `low`

#### Crowd Control

- Move (base) — Area — `high`
- Pin (base) — Area — `high`
- Silence (base) — Single target — `high`

#### Special effects

##### Requires

- Cooldown-gated proc (base) — Enemies
- Debuff on target (base) — Enemies
- Multiple debuffs on target (base) — Enemies

#### Damage

- Physical — Area, Self, Single target
- True damage — Multiple targets
- True damage (HP-based) — Single target

#### Stats the unit benefits from

- ATK
- Max HP
- ATK SPD
- Primary damage type (unit): **Physical**

### Synergies

1. **Pandora - Hope Unleashed** — Max HP via Max HP buff (single target, low); Enables Multiple debuffs on target via 5 debuff types; Enables Debuff on target via ATK debuff (all units)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Enables Multiple debuffs on target via 2 debuff types; Enables Debuff on target via ATK debuff (multiple targets)
3. **Sinbad - Seaside Savant** — Enables Multiple debuffs on target via 6 debuff types; Enables Debuff on target via ATK debuff (multiple targets)
4. **Lyca - Keeper of Glades** — Enables Multiple debuffs on target via 2 debuff types; Enables Debuff on target via ATK debuff (all units)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Enables Multiple debuffs on target via ATK debuff; Enables Debuff on target via ATK debuff (area)

## Isabella - The Taken Soul

### Summary

#### Buffs

- Haste buff (base) — Multiple targets — `low` — conditional (frequent)
- Healing (base) — Area — `high`
- Energy recovery (EX+10) — Single target — `low` — conditional (frequent)
- ATK SPD buff (Supreme+) — Self — `low`

#### Debuffs

- ATK debuff (base) — Single target — `low`

#### Crowd Control

- Unaffected immunity (base) — Single target — Once

#### Special effects

##### Requires

- Once per battle (base) — Allies

#### Damage

- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Energy
- Haste
- Physical DEF
- Magic DEF
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Haste via Haste buff (multiple targets, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)

## Kafra - Gale Rider

### Summary

#### Buffs

- Healing over time (base) — Area — `low`
- ATK buff (Legendary+) — Self — `medium`
- Shield (EX+5) — Self — `medium` — conditional (frequent)

#### Debuffs

- Phys DEF debuff (base) — Area — `low`
- ATK debuff (Mythic+) — Single target — `medium`
- Haste debuff (Mythic+) — Single target — `low`

#### Crowd Control

- Unaffected immunity (Mythic+) — Self — Conditional
- Move (base) — Single target — `medium`
- Stun (base) — Single target — `medium`

#### Damage

- Physical — Single target

#### Stats the unit benefits from

- ATK
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
2. **Evie - Royal Envoy** — ATK via ATK buff (multiple targets, high); Healing via Healing (single target, medium)
3. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
4. **Isabella - The Taken Soul** — Healing via Healing (area, high)
5. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)

## Koko - Wild Child

### Summary

#### Buffs

- Healing (base) — Single target — `high`
- Healing over time (base) — Single target — `high`
- Lifedrain buff (base) — Multiple targets — `medium`
- Haste buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `low`

#### Debuffs

- Damage taken debuff (base) — Area — `high`

#### Crowd Control

- Stun (base) — Area — `medium`

#### Damage

- Physical — All units, Area, Single target
- True damage — All units

#### Stats the unit benefits from

- ATK
- Energy
- Life Drain
- Haste
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
2. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, low); Haste via Haste buff (area, medium, conditional (frequent))
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Kordan - Ironblood Chieftain

### Summary

#### Buffs

- Lifedrain buff (base) — Area — `high`
- Shield (base) — Self — `medium`
- ATK buff (Legendary+) — Self — `medium`
- Healing over time (EX+10) — Self — `low`

#### Crowd Control

- Knock down (base) — Single target — `high`
- Move (base) — Area — `high`
- Pin (base) — Area — `high`

#### Special effects

##### Provides

- Summoning (base) — Area

#### Damage

- Physical — Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Life Drain
- Max HP
- Magic DEF
- DEF Penetration
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
3. **Cecia - Requiem of Thorns** — Life Drain via Lifedrain buff (area, low); Max HP via Max HP buff (single target, high); Healing via Healing (arc, high)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Korin - Wood Warden

### Summary

#### Buffs

- Shield (base) — Single target — `medium`
- Haste buff (Legendary+) — Self — `medium`
- ATK SPD buff (EX+5) — Self — `high`
- Damage taken reduction (Supreme+) — Self — `medium`

#### Crowd Control

- Pin (base) — Single target — `medium`

#### Damage

- Physical — Area, Self, Single target
- True damage — Single target
- True damage (HP-based) — Area, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- ATK SPD
- Primary damage type (unit): **Physical**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))

## Kruger - Dauntless Warrior

### Summary

#### Buffs

- Lifedrain buff (Mythic+) — Area — `medium`
- Shield (Mythic+) — Single target — `low`

#### Debuffs

- Phys DEF debuff (base) — Single target — `high`

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Life Drain
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)
5. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)

## Kulu - Blast Master

### Summary

#### Buffs

- Invincible (base) — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs

- Movement speed debuff (base) — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control

- Unaffected immunity (base) — Area — On ultimate
- Move (base) — Single target — `high`

#### Special effects

##### Provides

- Invincibility (base) — Single target
- Summoning (base) — Area

#### Damage

- Physical — All units, Area, Single target

#### Stats the unit benefits from

- ATK
- DEF Penetration
- ATK SPD
- Primary damage type (unit): **Physical**

### Synergies

1. **Aliceth - Radiant Wings** — ATK via ATK buff (multiple targets, medium); DEF Penetration via DEF Penetration buff (single target, medium)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
3. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)

## Laios - Dungeon Adventurer

### Summary

#### Buffs

- ATK buff (base) — Area — `low` — conditional (rare)
- DEF buff (base) — Area — `low` — conditional (rare)
- Energy recovery (base) — Area — `low` — conditional (rare)
- Haste buff (base) — Area — `low` — conditional (rare)
- Healing (base) — Area — `low` — conditional (rare)
- Healing over time (base) — Area — `low` — conditional (rare)
- Max HP buff (Supreme+) — Self — `low` — conditional (rare)

#### Crowd Control

- Pin (base) — Area — `medium`

#### Special effects

##### Provides

- Named companion unit (base) — Single target
- Summoning (base) — Single target

##### Requires

- Monster ingredients (base) — Enemies
- Stacked resource (base) — Enemies
- Enemy monsters present (Mythic+) — Enemies

#### Damage

- Physical — Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Energy
- Physical DEF
- Magic DEF
- Haste
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
3. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
5. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high); Healing via Healing (arc, high)

## Lenya - Wild Cyclone

### Summary

#### Buffs

- Crit buff (base) — Self — `high`
- Haste buff (Legendary+) — Self — `medium`
- Shield (EX+5) — Self — `medium` — conditional (frequent)
- Damage taken reduction (Supreme+) — Self — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Once
- Stun (base) — Area — `high`

#### Damage

- Physical — Area, Self, Single target

#### Stats the unit benefits from

- ATK
- Crit
- Haste
- Energy
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

## Lily May - Twilight Tracker

### Summary

#### Buffs

- ATK buff (base) — Self — `low`
- Invincible (base) — Self — `high`

#### Debuffs

- Energy drain (base) — All units — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Interrupt (base) — All units — `medium`

#### Special effects

##### Provides

- Invincibility (base) — Single target
- Untargetable (base) — All units

#### Damage

- Magic — All units, Single target
- True damage (HP-based) — Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- DEF Penetration
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)
4. **Aliceth - Radiant Wings** — ATK via ATK buff (multiple targets, medium); DEF Penetration via DEF Penetration buff (single target, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high)

## Lorsan - Windweaver Protector

### Summary

#### Buffs

- Healing over time (base) — Single target — `medium`
- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Multiple targets — `high`

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — On skill
- Stun (EX+10) — Multiple targets — `high`

#### Special effects

##### Provides

- Summoning (base) — Area

#### Damage

- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Lucca - Stalwart Fighter

### Summary

#### Buffs

- Damage taken reduction (base) — Self — `high`
- Shield (base) — Self — `medium`
- Max HP buff (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control

- Immune immunity (base) — Self — On skill
- Interrupt (base) — Single target — `medium`
- Stun (base) — Area — `medium`

#### Damage

- Physical — Area, Self, Single target

#### Stats the unit benefits from

- ATK
- Physical DEF
- Max HP
- Magic DEF
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
5. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)

## Lucius - The Lightbringer

### Summary

#### Buffs

- Healing (base) — Single target — `medium`
- Shield (base) — Area — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Debuffs

- ATK debuff (Mythic+) — Area — `high`

#### Crowd Control

- Move (base) — Single target — `high`
- Stun (base) — Single target — `low`

#### Special effects

##### Provides

- Reposition enemies (base) — Single target

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
2. **Evie - Royal Envoy** — ATK via ATK buff (multiple targets, high); Healing via Healing (single target, medium)
3. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
4. **Isabella - The Taken Soul** — Healing via Healing (area, high)
5. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)

## Lucy - Celestial Spirit Mage

### Summary

#### Buffs

- Haste buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `high`

#### Debuffs

- Damage taken debuff (base) — Single target — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Single target — `medium`

#### Damage

- Magic — All units, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- ATK SPD
- Energy
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high); Haste via Haste buff (multiple targets, high)
5. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)

## Ludovic - Wreathed Eternalist

### Summary

#### Buffs

- Healing (base) — Area — `high`
- Healing over time (base) — Area — `high`
- Healing stat buff (Legendary+) — Self — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (Supreme+) — Single target — `medium`

#### Special effects

##### Provides

- Revive ally (base) — Area

#### Damage

- Magic — All units, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Lumont - Benign Horn

### Summary

#### Buffs

- DEF buff (base) — Area — `high`
- Shield (base) — Self — `high`
- Haste buff (Legendary+) — Self — `low`
- Healing over time (Supreme+) — Single target — `low`

#### Debuffs

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Area — `low`
- Taunt (base) — Area — `medium`

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Physical DEF
- Haste
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Lyca - Keeper of Glades

### Summary

#### Buffs

- ATK SPD buff (base) — Self — `medium`

#### Debuffs

- ATK debuff (base) — All units — `high`
- Phys DEF debuff (base) — All units — `high`

#### Crowd Control

- Stun (EX+10) — Single target — `low`

#### Special effects

##### Provides

- Summoning (base) — Single target

#### Damage

- Physical — All units, Area, Self, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Energy
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

## Marcille - Elven Mage

### Summary

#### Buffs

- Haste buff (base) — Self — `low`
- Healing (base) — Single target — `low` — conditional (rare)

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — On skill
- Interrupt (Mythic+) — Single target — `high`

#### Special effects

##### Provides

- Summoning (base) — Area
- Revive ally (Mythic+) — Single target

##### Requires

- Once per battle (Mythic+) — Allies

#### Damage

- Magic — All units, Area, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Haste
- Energy
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
4. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
5. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Healing via Healing (arc, high)

## Marilee - Forest's Arrow

### Summary

#### Buffs

- ATK buff (base) — Area — `high` — conditional (frequent)
- Crit buff (Legendary+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `low`

#### Damage

- Physical — Multiple targets, Single target
- True damage — Multiple targets

#### Stats the unit benefits from

- ATK
- ATK SPD
- Crit
- Primary damage type (unit): **Physical**

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)
3. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)

## Mehira - Mind Cager

### Summary

#### Buffs

- Haste buff (base) — Single target — `medium`
- Lifedrain buff (Legendary+) — Self — `medium`
- Max HP buff (Legendary+) — Self — `high`
- Healing (Mythic+) — Self — `low`

#### Debuffs

- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Charm (base) — Area — `medium`

#### Special effects

##### Provides

- Summoning (base) — Self
- HP threshold strike (Mythic+) — Self
- Untargetable (Mythic+) — Self

#### Damage

- Magic — Area, Self, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- Life Drain
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
3. **Florabelle - Blooming Maiden** — Haste via Haste buff (multiple targets, high, conditional (frequent)); Max HP via Shield (single target, medium); Life Drain via Lifedrain buff (single target, medium, conditional (frequent)); Healing via Healing (area, medium, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)

## Mikola - Warbeat Compere

### Summary

#### Buffs

- ATK buff (base) — Self — `medium`
- Haste buff (base) — Multiple targets — `high`
- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — All units — `medium`

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — Conditional

#### Damage

- Physical — Area, Multiple targets

#### Stats the unit benefits from

- ATK
- Haste
- Magic DEF
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)

## Mirael - Scarlet Sorceress

### Summary

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`

#### Special effects

##### Provides

- Summoning (base) — Single target

#### Damage

- DoT — Single target
- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Primary damage type (unit): **Magic**

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)

## Nara - Wrathful Wraith

### Summary

#### Buffs

- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Single target — `low`
- Energy recovery (Supreme+) — Single target — `low`

#### Debuffs

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — Permanent

#### Damage

- Physical — Area, Single target
- True damage — Single target

#### Stats the unit benefits from

- ATK
- Energy
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Natsu - Fire Dragon Slayer Mage

### Summary

#### Buffs

- Crit buff (base) — Self — `low` — conditional (rare)
- ATK buff (Legendary+) — Self — `low`
- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Haste debuff (base) — Area — `high`
- Max HP debuff (Mythic+) — Single target — `medium`

#### Crowd Control

- Knock down (base) — Area — `low`
- Stun (base) — Single target — `medium`

#### Damage

- DoT — Single target
- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Crit
- Haste
- Primary damage type (unit): **Magic**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high); Haste via Haste buff (multiple targets, high)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))

## Nazrik - Soulstalker

### Summary

#### Buffs

- Crit buff (Legendary+) — Self — `low`

#### Debuffs

- Max HP debuff (base) — Single target — `low`
- Damage taken debuff (EX+10) — Self — `low`
- Vitality debuff (EX+10) — Self — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Damage

- Physical — Self, Single target
- True damage — Single target
- True damage (HP-based) — Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Crit
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Marilee - Forest's Arrow** — ATK via ATK buff (area, high, conditional (frequent)); Crit via Crit buff (single target, low)
4. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high)

## Nerion - Bereaved Tide

### Summary

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`
- Shield (EX+10) — Self — `medium`

#### Debuffs

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Damage

- Magic — Area, Self, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Energy
- DEF Penetration
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Aliceth - Radiant Wings** — ATK via ATK buff (multiple targets, medium); DEF Penetration via DEF Penetration buff (single target, medium)
5. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)

## Niru - Soul Collector

### Summary

#### Buffs

- Healing (base) — Single target — `low` — conditional (rare)
- DEF buff (EX+5) — Self — `low`

#### Special effects

##### Provides

- Spirit form ally (base) — Single target
- Start-of-battle cast (Mythic+) — Self

##### Requires

- Blessed ally active (base) — Allies
- Enemy defeat (base) — Allies

#### Damage

- Magic — All units, Self, Single target

#### Stats the unit benefits from

- Max HP
- ATK
- Physical DEF
- Magic DEF
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
3. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent)); Enables Blessed ally active via Ally blessing
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Odie - Desert Defender

### Summary

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`

#### Damage

- DoT — Single target
- Magic — Single target

#### Stats the unit benefits from

- ATK
- Energy
- ATK SPD
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

## Pandora - Hope Unleashed

### Summary

#### Buffs

- Healing (base) — Single target — `low`
- Invincible (base) — Single target — `high`
- Max HP buff (Legendary+) — Single target — `low`
- Energy recovery (Mythic+) — Single target — `low`

#### Debuffs

- ATK debuff (base) — All units — `medium`
- Damage taken debuff (base) — Single target — `medium`
- Energy drain (base) — Single target — `low`
- Haste debuff (base) — Single target — `medium`
- Vitality debuff (base) — Single target — `high`

#### Crowd Control

- Move (base) — Single target — `medium`

#### Special effects

##### Provides

- Invincibility (base) — Single target

#### Damage

- Magic — Single target

#### Stats the unit benefits from

- ATK
- Energy
- Max HP
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Pang - Bamboo Guardian

### Summary

#### Buffs

- Haste buff (base) — Self — `high` — conditional (frequent)
- Shield (base) — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Area — `low`

#### Special effects

##### Provides

- Transform (base) — Single target

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Energy
- DEF Penetration
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

## Parisa - Ode to Flowers

### Summary

#### Buffs

- ATK SPD buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`

#### Damage

- Magic — Area, Multiple targets, Self, Single target

#### Stats the unit benefits from

- ATK
- Energy
- ATK SPD
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

## Perseus - Chosen Champion

### Summary

#### Buffs

- Max HP buff (base) — Area — `low`
- Shield (base) — Self — `medium`
- ATK buff (Legendary+) — Multiple targets — `medium`
- Damage taken reduction (Mythic+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Multiple targets — On skill
- Stun (base) — Area — `medium`

#### Damage

- Physical — Area, Self, Single target
- True damage — Multiple targets

#### Stats the unit benefits from

- ATK
- ATK SPD
- Max HP
- Magic DEF
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Magic DEF via DEF buff (multiple targets, low)
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
5. **Lumont - Benign Horn** — Magic DEF via DEF buff (area, high)

## Phraesto - Misty Scorpion

### Summary

#### Buffs

- Healing (base) — Single target — `low`
- Max HP buff (base) — Single target — `low`
- Shield (base) — Self — `high`

#### Crowd Control

- Stun (Mythic+) — Single target — `medium`
- Taunt (Mythic+) — Single target — `medium`

#### Special effects

##### Provides

- Summoning (base) — Self

#### Damage

- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Magic DEF
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Pippa - The Muddled Magician

### Summary

#### Buffs

- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Energy drain (base) — Area — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Knock down (base) — Single target — `low`
- Move (base) — Single target — `low`
- Pin (base) — Single target — `medium`

#### Special effects

##### Provides

- Summoning (base) — Area

#### Damage

- Magic — Area, Multiple targets, Single target
- True damage — Area

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- Primary damage type (unit): **Magic**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))

## Ravion - Twilight's Burden

### Summary

#### Buffs

- ATK buff (base) — Multiple targets — `high`
- Energy recovery (base) — Multiple targets — `high`
- Haste buff (Mythic+) — Multiple targets — `medium`
- Lifedrain buff (EX+10) — Multiple targets — `high`
- Shield (EX+10) — Multiple targets — `medium`

#### Debuffs

- ATK debuff (base) — Multiple targets — `high`
- Phys DEF debuff (base) — Multiple targets — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — Multiple targets — `high`
- Move (base) — Multiple targets — `high`

#### Special effects

##### Provides

- Position swap (EX+10) — Multiple targets

##### Requires

- Boss encounter (base) — Allies

#### Damage

- Physical — Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Energy
- Haste
- Life Drain
- Primary damage type (unit): **Physical**

### Synergies

1. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium); Haste via Haste buff (multiple targets, high)
4. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

## Reinier - Symmetric Sin

### Summary

#### Buffs

- Healing (base) — Single target — `medium`
- ATK buff (Legendary+) — Single target — `low`

#### Debuffs

- ATK debuff (Legendary+) — Single target — `low`
- Damage taken debuff (Mythic+) — Single target — `high`

#### Crowd Control

- Steadfast immunity (base) — Single target — Conditional
- Unaffected immunity (base) — Single target — Conditional
- Interrupt (base) — Single target — `high`
- Move (base) — Multiple targets — `high`
- Knock down (Mythic+) — Single target — `low`

#### Damage

- Magic — Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
2. **Evie - Royal Envoy** — ATK via ATK buff (multiple targets, high); Healing via Healing (single target, medium)
3. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
4. **Isabella - The Taken Soul** — Healing via Healing (area, high)
5. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)

## Rhys - Fiery Cavalier

### Summary

#### Buffs

- Healing (base) — Single target — `medium`
- Crit buff (Legendary+) — Self — `low`

#### Crowd Control

- Move (base) — Single target — `high`

#### Damage

- Physical — Arc, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Crit
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Healing via Healing (arc, high)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Evie - Royal Envoy** — ATK via ATK buff (multiple targets, high); Healing via Healing (single target, medium)
4. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
5. **Isabella - The Taken Soul** — Healing via Healing (area, high)

## Rowan - The Roamer

### Summary

#### Buffs

- Healing (base) — Single target — `low` — conditional (rare)
- Haste buff (Legendary+) — Self — `low`
- DEF buff (Mythic+) — Single target — `low` — conditional (rare)
- Max HP buff (Mythic+) — Single target — `low` — conditional (rare)
- ATK buff (EX+5) — Single target — `low`

#### Debuffs

- Energy drain (base) — Single target — `medium`

#### Special effects

##### Provides

- Energy steal (base) — Single target

##### Requires

- Once per battle (Mythic+) — Allies

#### Damage

- Magic — Single target

#### Stats the unit benefits from

- Energy
- ATK
- Max HP
- Haste
- Physical DEF
- Magic DEF
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — Energy via Energy recovery (multiple targets, high); ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium)
2. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high); Healing via Healing over time (single target, low)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
5. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)

## Saida - Vampiric Vine

### Summary

#### Buffs

- Healing (base) — Area — `medium`
- Shield (base) — Multiple targets — `high`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs

- Energy drain (base) — Single target — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Conditional
- Interrupt (base) — Area — `high`
- Move (base) — Single target — `medium`

#### Special effects

##### Provides

- Revive ally (base) — Single target

##### Requires

- Boss encounter (base) — Enemies

#### Damage

- Magic — All units, Area, Multiple targets, Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
3. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
4. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))
5. **Cecia - Requiem of Thorns** — Max HP via Max HP buff (single target, high); Healing via Healing (arc, high)

## Salazer - Lash of Bantus

### Summary

#### Buffs

- Lifedrain buff (base) — Single target — `low`
- Damage taken reduction (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `high`
- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special effects

##### Provides

- Summoning (base) — Single target

#### Damage

- Physical — Single target

#### Stats the unit benefits from

- ATK
- Life Drain
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Cecia - Requiem of Thorns** — Life Drain via Lifedrain buff (area, low); Max HP via Max HP buff (single target, high); Healing via Healing (arc, high)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Satrana - Ember Enchantress

### Summary

#### Buffs

- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Arc — `high`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs

- Vitality debuff (base) — Area — `low`

#### Crowd Control

- Charm (base) — Single target — `medium`

#### Special effects

##### Provides

- Invincibility (base) — Area

#### Damage

- Magic — Arc, Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Life Drain
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)
5. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)

## Scarlita - Herald of Compassion

### Summary

#### Buffs

- Energy recovery (base) — Area — `low`
- Invincible (base) — Self — `high`
- Shield (base) — Single target — `low` — conditional (rare)
- Execution buff (Legendary+) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Conditional
- Knock down (base) — Arc — `medium`
- Move (base) — All units — `low`
- Stun (base) — Area — `medium`

#### Special effects

##### Provides

- Invincibility (base) — Area

#### Damage

- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets

#### Stats the unit benefits from

- ATK
- Energy
- Max HP
- Execution
- Physical DEF
- Magic DEF
- Primary damage type (unit): **Physical**

### Synergies

1. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Max HP via Shield (multiple targets, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low)
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
5. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)

## Seth - Swift Shadow

### Summary

#### Buffs

- Haste buff (base) — Self — `low`
- Healing (base) — Single target — `medium`
- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Single target — `low`

#### Debuffs

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Freeze (base) — Single target — `low`

#### Special effects

##### Provides

- Invincibility (base) — Single target

#### Damage

- Physical — Self, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Life Drain
- Magic DEF
- Crit
- Energy
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
3. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
4. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)

## Shadewing - Undying Vow

### Summary

#### Buffs

- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Single target — `low`
- Lifedrain buff (Supreme+) — Self — `low`
- Shield (Supreme+) — Self — `low`

#### Debuffs

- Magic DEF debuff (base) — All units — `low`

#### Special effects

##### Provides

- Debuff application (base) — Single target
- DoT conversion (base) — All units
- Invincibility (base) — All units
- Ally HP drain (self-buff) (Supreme+) — Self

##### Requires

- Continuous damage on enemies (base) — Enemies
- Debuff on target (base) — Enemies

#### Damage

- DoT — Single target
- Magic — All units, Single target
- True damage — Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Life Drain
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Enables Debuff on target via ATK debuff (multiple targets)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Enables Debuff on target via ATK debuff (area)
3. **Hepler - Master of Forms** — Max HP via Shield (multiple targets, low); Enables Debuff on target via Haste debuff (area); Enables Continuous damage on enemies via tick damage
4. **Koko - Wild Child** — Max HP via Shield (single target, low); Life Drain via Lifedrain buff (multiple targets, medium); Enables Debuff on target via Damage taken debuff (area)
5. **Natsu - Fire Dragon Slayer Mage** — Enables Debuff on target via Haste debuff (area); Enables Continuous damage on enemies via DoT

## Shakir - Furious Howl

### Summary

#### Buffs

- Damage taken reduction (base) — Multiple targets — `low` — conditional (frequent)
- Haste buff (base) — Multiple targets — `low`
- Lifedrain buff (base) — Single target — `medium`

#### Debuffs

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Form

#### Special effects

##### Provides

- Transform (base) — Area

##### Requires

- Specific form active (base) — Enemies

#### Damage

- Physical — Arc, Area, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Life Drain
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

## Shemira - Corpsemaker

### Summary

#### Buffs

- Healing (base) — Self — `medium` — conditional (frequent)
- Shield (base) — Single target — `medium`

#### Special effects

##### Provides

- Summoning (base) — Self

#### Damage

- Magic — All units, Area, Self, Single target
- True damage (HP-based) — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Silven - Heir of Glory

### Summary

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Self — `low`

#### Special effects

##### Provides

- Summoning (base) — Single target

#### Damage

- Magic — Single target
- True damage (HP-based) — Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- ATK SPD
- Energy
- DEF Penetration
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Cecia - Requiem of Thorns** — Max HP via Max HP buff (single target, high); ATK SPD via ATK SPD buff (multiple targets, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
5. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)

## Silvina - The Taken Breath

### Summary

#### Buffs

- Crit buff (Legendary+) — Self — `low`
- Shield (Mythic+) — Self — `high`

#### Debuffs

- Energy drain (base) — Single target — `high`
- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `low`
- Frighten (EX+10) — Area — `low`

#### Damage

- Physical — Single target

#### Stats the unit benefits from

- ATK
- Crit
- Primary damage type (unit): **Physical**

### Synergies

1. **Marilee - Forest's Arrow** — ATK via ATK buff (area, high, conditional (frequent)); Crit via Crit buff (single target, low)
2. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)

## Sinbad - Seaside Savant

### Summary

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`

#### Debuffs

- Damage taken debuff (base) — Multiple targets — `medium`
- ATK debuff (Mythic+) — Multiple targets — `high`
- Energy drain (Mythic+) — Multiple targets — `medium`
- Magic DEF debuff (Mythic+) — Multiple targets — `medium`
- Phys DEF debuff (Mythic+) — Multiple targets — `medium`
- Vitality debuff (Mythic+) — Multiple targets — `high`

#### Crowd Control

- Unaffected immunity (base) — Multiple targets — Conditional

#### Damage

- Physical — Multiple targets, Self, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Energy
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

## Smokey & Meerky - Wasteland Apothecary

### Summary

#### Buffs

- Energy recovery (base) — Area — `medium`
- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — Area — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control

- Interrupt (base) — Area — `medium`
- Stun (EX+10) — Single target — `low`

#### Stats the unit benefits from

- ATK
- Energy
- Max HP
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Solise - Floral Wonder

### Summary

#### Buffs

- Healing (base) — Multiple targets — `high` — conditional (frequent)
- Shield (base) — Multiple targets — `medium`
- ATK buff (Legendary+) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle

#### Special effects

##### Provides

- Named companion unit (base) — Single target
- Ally blessing (Mythic+) — Single target

#### Damage

- Magic — All units, Multiple targets, Single target

#### Stats the unit benefits from

- ATK
- Magic DEF
- Max HP
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Magic DEF via DEF buff (multiple targets, low); Healing via Healing (arc, high, conditional (frequent))
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
5. **Cecia - Requiem of Thorns** — Max HP via Max HP buff (single target, high); Healing via Healing (arc, high)

## Sonja - Crimson Queenpin

### Summary

#### Buffs

- ATK buff (base) — Multiple targets — `low` — conditional (frequent)
- Haste buff (Legendary+) — Self — `low`
- Damage taken reduction (EX+10) — Self — `low`

#### Crowd Control

- Stun (base) — Area — `low`

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Magic DEF
- Haste
- Energy
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

## Soren - Silent Fury

### Summary

#### Buffs

- Damage taken reduction (base) — Self — `low`
- Haste buff (Legendary+) — Self — `low` — conditional (rare)
- Healing over time (Mythic+) — Single target — `low` — conditional (rare)
- Energy recovery (Supreme+) — Single target — `high`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control

- Move (base) — Multiple targets — `high`
- Stun (base) — Area — `medium`

#### Damage

- Physical — Area, Multiple targets, Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- Energy
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
4. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Sylphira - Sovereign of Song

### Summary

#### Buffs

- ATK buff (base) — Area — `high` — conditional (frequent)
- Haste buff (base) — Area — `medium` — conditional (frequent)
- Healing (Mythic+) — Self — `low`
- Lifedrain buff (Supreme+) — Single target — `low`

#### Debuffs

- Energy drain (base) — Single target — `medium`
- Max HP debuff (base) — Area — `medium`

#### Crowd Control

- Immune immunity (base) — Self — On skill
- Unaffected immunity (base) — Area — Conditional
- Cleanse immunity (Mythic+) — Self — On skill
- Interrupt (base) — Area — `low`
- Knock down (base) — Area — `medium`
- Silence (base) — Area — `low`

#### Special effects

##### Provides

- Dispel debuffs (Mythic+) — Self

#### Damage

- Magic — Area, Single target
- True damage (HP-based) — Single target

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- Life Drain
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
3. **Florabelle - Blooming Maiden** — Haste via Haste buff (multiple targets, high, conditional (frequent)); Max HP via Shield (single target, medium); Life Drain via Lifedrain buff (single target, medium, conditional (frequent)); Healing via Healing (area, medium, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Talene - Resurging Flame

### Summary

#### Buffs

- Healing (base) — Area — `low` — conditional (frequent)
- Healing over time (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Area — `low`
- ATK buff (Legendary+) — Self — `low`

#### Special effects

##### Provides

- Summoning (base) — Area
- Transform (base) — Area

#### Damage

- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Life Drain
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Cecia - Requiem of Thorns** — Max HP via Max HP buff (single target, high); Life Drain via Lifedrain buff (area, low); Healing via Healing (arc, high)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

## Tasi - Fairy of Dreams

### Summary

#### Buffs

- Healing over time (base) — Area — `medium`
- Invincible (base) — Area — `high`
- ATK buff (Legendary+) — Self — `medium`
- Damage taken reduction (Mythic+) — Self — `high`
- Haste buff (Mythic+) — Self — `high`

#### Crowd Control

- Pin (base) — All units — `low`
- Sleep (base) — Single target — `high`
- Stun (base) — Area — `low`

#### Special effects

##### Provides

- Invincibility (base) — Area
- Mass sleep (base) — Single target
- Summoning (base) — All units
- Transform (base) — Area

#### Damage

- DoT — All units, Single target
- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- DEF Penetration
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium)
3. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
4. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high); Haste via Haste buff (multiple targets, high)

## Temesia - Lightsavior

### Summary

#### Buffs

- Energy recovery (base) — Area — `high`
- Healing (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`
- Healing over time (EX+5) — Self — `low`
- Shield (Supreme+) — Self — `low`

#### Debuffs

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Unaffected immunity (Mythic+) — Self — Permanent
- Interrupt (base) — Single target — `high`
- Knock down (base) — All units — `low`

#### Special effects

##### Provides

- Summoning (base) — All units

#### Damage

- Physical — All units, Area, Single target
- True damage — Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Haste
- Energy
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
3. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high); Healing via Healing (arc, high)
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)

## Thador - Ironsworn General

### Summary

#### Buffs

- Shield (base) — Self — `medium`
- Damage taken reduction (Legendary+) — Self — `medium`
- Healing (Supreme+) — Self — `low`
- Healing over time (Supreme+) — Self — `low`

#### Debuffs

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control

- Knock down (base) — Single target — `low`

#### Special effects

##### Provides

- Summoning (Mythic+) — Single target

#### Damage

- Physical — Area, Self, Single target

#### Stats the unit benefits from

- ATK
- Crit
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Thoran - Fallen King

### Summary

#### Buffs

- Healing (base) — Single target — `low` — conditional (rare)
- Lifedrain buff (base) — Single target — `high` — conditional (frequent)
- Max HP buff (base) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Interrupt (base) — Single target — `low`

#### Damage

- Physical — Self, Single target

#### Stats the unit benefits from

- ATK
- Life Drain
- Max HP
- Energy
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
3. **Cecia - Requiem of Thorns** — Life Drain via Lifedrain buff (area, low); Max HP via Max HP buff (single target, high); Healing via Healing (arc, high)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
5. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))

## Tilaya - Wild Blade

### Summary

#### Buffs

- Damage taken reduction (base) — Arc — `high` — conditional (frequent)
- Healing over time (base) — Arc — `high` — conditional (frequent)
- Shield (base) — Self — `medium` — conditional (frequent)
- Healing (Mythic+) — Single target — `medium`
- Max HP buff (EX+10) — Area — `low`

#### Crowd Control

- Unaffected immunity (base) — Arc — Start of battle

#### Special effects

##### Provides

- Start-of-battle cast (base) — Arc

#### Damage

- Physical — Arc, Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

## Ulmus - Grove Keeper

### Summary

#### Buffs

- Healing (base) — Area — `low`
- Healing over time (base) — Single target — `low`
- Shield (base) — Self — `low`
- Max HP buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Knock down (Mythic+) — Single target — `high`
- Move (Supreme+) — Area — `low`

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Life Drain
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high)
2. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
3. **Cecia - Requiem of Thorns** — Max HP via Max HP buff (single target, high); Life Drain via Lifedrain buff (area, low); Healing via Healing (arc, high)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
5. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))

## Vala - Phantom of Oakenfell

### Summary

#### Buffs

- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Multiple targets — `high`
- Healing (EX+10) — Self — `low`

#### Debuffs

- Haste debuff (base) — Single target — `high`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Special effects

##### Provides

- Untargetable (Mythic+) — Multiple targets

##### Requires

- Enemy defeat (Legendary+) — Enemies

#### Damage

- Physical — Single target
- True damage — Single target

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- Energy
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
3. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
4. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)

## Valen - Roving Swordsman

### Summary

#### Buffs

- ATK buff (base) — Area — `high`
- Invincible (base) — Self — `high`

#### Debuffs

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (Supreme+) — Single target — `medium`

#### Special effects

##### Provides

- Invincibility (base) — Area

#### Damage

- Physical — Area, Single target

#### Stats the unit benefits from

- ATK
- Energy
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
5. **Soren - Silent Fury** — Energy via Energy recovery (single target, high)

## Valka - Forsaken Blade

### Summary

#### Buffs

- Healing (base) — Area — `low` — conditional (frequent)
- Shield (base) — Self — `low` — conditional (frequent)
- ATK SPD buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Single target — `medium` — conditional (frequent)
- Lifedrain buff (EX+10) — Single target — `low`
- Haste buff (Supreme+) — Self — `low` — conditional (frequent)

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Knock down (base) — Area — `high`
- Stun (base) — Area — `high`

#### Special effects

##### Requires

- Adjacent allies (base) — Allies

#### Damage

- Physical — Area, Self, Single target
- True damage (HP-based) — Area

#### Stats the unit benefits from

- ATK
- Max HP
- ATK SPD
- Energy
- Life Drain
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Enables Adjacent allies via Multiple ally buffs
2. **Cecia - Requiem of Thorns** — Max HP via Max HP buff (single target, high); ATK SPD via ATK SPD buff (multiple targets, high); Life Drain via Lifedrain buff (area, low); Healing via Healing (arc, high); Enables Adjacent allies via Multiple ally buffs
3. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low); Enables Adjacent allies via Multiple ally buffs
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium); Enables Adjacent allies via Multiple ally buffs
5. **Isabella - The Taken Soul** — Energy via Energy recovery (single target, low, conditional (frequent)); Healing via Healing (area, high); Enables Adjacent allies via Multiple ally buffs

## Velara - Pale Votary

### Summary

#### Buffs

- Haste buff (base) — Self — `low`
- Healing (base) — Multiple targets — `low`
- Shield (Mythic+) — Self — `high`

#### Debuffs

- Haste debuff (base) — Single target — `medium`

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special effects

##### Provides

- Start-of-battle cast (base) — All units
- Summoning (base) — All units

##### Requires

- Boss encounter (base) — Allies

#### Damage

- Magic — Area, Single target

#### Stats the unit benefits from

- ATK
- Haste
- Energy
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium)
4. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)

## Viperian - Shadow Serpent

### Summary

#### Buffs

- Healing (base) — Single target — `high`
- Haste buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+5) — Single target — `low`

#### Debuffs

- Energy drain (base) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle

#### Damage

- Magic — All units, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Haste
- Life Drain
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Florabelle - Blooming Maiden** — Max HP via Shield (single target, medium); Haste via Haste buff (multiple targets, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, medium, conditional (frequent)); Healing via Healing (area, medium, conditional (frequent))
4. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)

## Walker - Wildland Outlaw

### Summary

#### Buffs

- Damage taken reduction (base) — Self — `medium`
- Crit buff (Legendary+) — Self — `high`
- Lifedrain buff (Supreme+) — Self — `medium`
- Shield (Supreme+) — Self — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Damage

- Physical — Arc, Area, Self, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Crit
- Life Drain
- Primary damage type (unit): **Physical**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Marilee - Forest's Arrow** — ATK via ATK buff (area, high, conditional (frequent)); Crit via Crit buff (single target, low)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)

## Zandrok - Watchful Edge

### Summary

#### Buffs

- Haste buff (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Area — `low` — conditional (frequent)
- Max HP buff (Legendary+) — Self — `low`

#### Crowd Control

- Stun (base) — Area — `low`

#### Special effects

##### Provides

- Summoning (base) — Area

#### Damage

- Physical — Area, Multiple targets, Self, Single target

#### Stats the unit benefits from

- Max HP
- Haste
- Life Drain
- Primary damage type (unit): **Physical**

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high)
2. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Haste via Haste buff (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
3. **Hugin - Maverick Smith** — Max HP via Shield (single target, high); Haste via Haste buff (multiple targets, high)
4. **Florabelle - Blooming Maiden** — Max HP via Shield (single target, medium); Haste via Haste buff (multiple targets, high, conditional (frequent)); Life Drain via Lifedrain buff (single target, medium, conditional (frequent))
5. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)

## Zanie - Timeless Tinkerer

### Summary

#### Buffs

- ATK SPD buff (base) — Self — `low` — conditional (rare)
- Healing (base) — Single target — `low` — conditional (rare)
- Shield (base) — Single target — `low` — conditional (rare)
- Max HP buff (Mythic+) — Single target — `low` — conditional (rare)

#### Debuffs

- ATK debuff (Supreme+) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Stun (base) — Single target — `low`

#### Damage

- Physical — Area, Self, Single target

#### Stats the unit benefits from

- ATK
- ATK SPD
- Max HP
- DEF Penetration
- Healing
- Primary damage type (unit): **Physical**

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high); Healing via Healing (arc, high)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
5. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)

## Zorya - Watcher in Stone

### Summary

#### Buffs

- Damage taken reduction (base) — Arc — `high`
- Energy recovery (base) — Area — `low`
- Healing (base) — Area — `low` — conditional (frequent)
- Healing over time (base) — Area — `low`
- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Area — `medium` — conditional (frequent)
- Haste buff (Mythic+) — Self — `medium` — conditional (frequent)

#### Crowd Control

- Steadfast immunity (base) — Self — Start of battle
- Unaffected immunity (EX+10) — Single target — On skill
- Knock down (base) — Arc — `medium`
- Stun (base) — Area — `medium`

#### Special effects

##### Provides

- Invincibility (base) — Area
- Summoning (base) — Arc

##### Requires

- Ally Ultimate casts (Mythic+) — Allies

#### Damage

- Magic — Arc, Area, Single target

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Life Drain
- Haste
- Healing
- Primary damage type (unit): **Magic**

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
2. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium); Healing via Healing over time (area, medium); Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
4. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium); Haste via Haste buff (multiple targets, high); Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
5. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high); Enables Ally Ultimate casts via Start-of-battle Ultimate
