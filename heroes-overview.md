# Heroes Overview

Per-hero synergy picks first, then summaries from [Heroes.md](Heroes.md).
Synergy: stat buffs matching **Stats the unit benefits from**, and
enabler partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from Max HP/
shields). Rare conditional buffs score lower.
Regenerate with `scripts/generate-heroes-overview.py` after
`scripts/rewrite-summaries.py`.

## Aliceth - Radiant Wings

### Synergies

1. **Lyca - Keeper of Glades** — Enables Ranged damage from allies via ranged attacks; Enables Debuff on target via ATK debuff (all units)
2. **Lily May - Twilight Tracker** — Enables Debuff on target via Energy drain (all units)
3. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Enables Debuff on target via ATK debuff (multiple targets)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Enables Debuff on target via Max HP debuff (area)
5. **Hepler - Master of Forms** — Enables Debuff on target via Haste debuff (area)

### Summary

#### Stats the unit benefits from

- ATK
- DEF Penetration
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

#### Buffs

- Ally empower buff (base) — Single target — `high`
- Attack range buff (base) — Single target — `high`
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

#### Special Effects

##### Provides

- HP threshold strike (base) — Multiple targets
- Instant defeat (base) — Multiple targets
- Invincibility (base) — Single target
- Marked target (focus fire) (base) — Single target
- Reposition enemies (base) — Single target
- Untargetable (base) — Multiple targets
- Fatal blow save (Mythic+) — Area

##### Requires

- Cooldown-gated trigger (base) — Allies
- Ranged damage from allies (base) — Allies
- Debuff on target (Legendary+) — Enemies

## Alna - Frozen Mother

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
3. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))
4. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
5. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Healing
- Primary damage type (unit): **Physical**

#### Damage

- Physical — All units, Arc, Self, Single target

#### Buffs

- Healing (base) — Self — `low`
- Max HP buff (base) — Multiple targets — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Debuffs

- Haste debuff (base) — Arc — `high`
- Vitality debuff (Supreme+) — Area — `medium`

#### Crowd Control

- Freeze (Supreme+) — Area — `medium`

#### Special Effects

##### Provides

- Start-of-battle cast (base) — All units
- Summoning (base) — Self
- Damage and control immunity (Mythic+) — Self

## Alsa - Desert Flare

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
5. **Florabelle - Blooming Maiden** — Haste via Haste buff (multiple targets, high, conditional (frequent)); Max HP via Shield (single target, medium)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Area, Self, Single target

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

#### Special Effects

##### Requires

- Cooldown-gated trigger (base) — Enemies
- Form or stance active (base) — Enemies

## Antandra - Desert Fury

### Synergies

1. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- Max HP
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Arc, Area, Self, Single target

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

#### Special Effects

##### Requires

- Once per battle (Mythic+) — Allies

## Arden - Oak Sage

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
5. **Soren - Silent Fury** — Energy via Energy recovery (single target, high)

### Summary

#### Stats the unit benefits from

- ATK
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Multiple targets, Single target

#### Buffs

- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control

- Pin (base) — Multiple targets — `high`

#### Special Effects

##### Provides

- Summoning (base) — Multiple targets

## Atalanta - Fortune Finder

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
2. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high)
3. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
4. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)
5. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Physical DEF
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Multiple targets, Single target

#### Buffs

- Haste buff (Legendary+) — Self — `high` — conditional (frequent)
- Healing (Supreme+) — Single target — `low`

#### Debuffs

- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Move (base) — Single target — `high`
- Pin (base) — Single target — `medium`
- Stun (base) — Single target — `medium`

#### Special Effects

##### Provides

- Reposition enemies (base) — Single target
- Stat steal (EX+10) — Single target

## Athalia - Harbinger of Justice

### Synergies

1. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)
2. **Marilee - Forest's Arrow** — Crit via Crit buff (single target, low)

### Summary

#### Stats the unit benefits from

- Crit
- Execution
- Primary damage type (unit): **Physical**

#### Damage

- Physical — All units, Area, Single target
- True damage — All units, Single target

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

#### Special Effects

##### Provides

- Invincibility (base) — Area
- Transform (base) — Area

## Aurora - Celestial of Dreams

### Synergies

1. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
3. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)
5. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Multiple targets, Single target

#### Buffs

- ATK buff (base) — Multiple targets — `high`
- Haste buff (base) — Multiple targets — `high`
- Invincible (base) — Multiple targets — `high`

#### Debuffs

- Haste debuff (base) — Multiple targets — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Sleep (base) — Multiple targets — `high`

#### Special Effects

##### Provides

- Invincibility (base) — Multiple targets
- Start-of-battle cast (base) — Multiple targets
- Summoning (base) — Self

## Baelran - Dawnblade

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target
- True damage — Area, Single target
- True damage (HP-based) — Arc, Area

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

#### Special Effects

##### Provides

- Start-of-battle cast (base) — Arc
- Dispel debuffs (EX+15) — Area

##### Requires

- Form or stance active (base) — Enemies
- Boss encounter (Supreme+) — Enemies

## Berial - Sinister Jester

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Magic**

#### Damage

- DoT — Area
- Magic — Multiple targets, Single target

#### Buffs

- Healing (base) — Single target — `high`
- Invincible (base) — Self — `high`

#### Debuffs

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `low`

#### Crowd Control

- Frighten (base) — Area — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Single target
- Revive ally (base) — Single target
- Summoning (Mythic+) — Single target

## Bonnie - Obsidian Claws

### Synergies

1. **Lily May - Twilight Tracker** — Enables Debuff on target via Energy drain (all units); Enables Magic damage from allies via Magic damage (all units)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Enables Debuff on target via Max HP debuff (area); Enables Magic damage from allies via Magic damage (area)
3. **Natsu - Fire Dragon Slayer Mage** — Enables Debuff on target via Haste debuff (area); Enables Magic damage from allies via Magic damage (area)
4. **Lyca - Keeper of Glades** — Enables Debuff on target via ATK debuff (all units)
5. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Enables Debuff on target via ATK debuff (multiple targets)

### Summary

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Single target

#### Buffs

- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs

- ATK debuff (base) — Single target — `medium`
- Haste debuff (base) — Single target — `low`
- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Area
- Transform (base) — Area
- Magic damage amplification (Supreme+) — Single target

##### Requires

- Debuff on target (base) — Enemies
- Debuff on target (Aging) (base) — Enemies
- Form or stance active (base) — Enemies
- Magic damage from allies (base) — Allies

## Brutus - Blood Claw

### Synergies

1. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
2. **Ravion - Twilight's Burden** — Life Drain via Lifedrain buff (multiple targets, high)
3. **Satrana - Ember Enchantress** — Life Drain via Lifedrain buff (arc, high)
4. **Kruger - Dauntless Warrior** — Life Drain via Lifedrain buff (area, medium)
5. **Zorya - Watcher in Stone** — Life Drain via Lifedrain buff (area, medium, conditional (frequent))

### Summary

#### Stats the unit benefits from

- Life Drain
- Primary damage type (unit): **Physical**

#### Damage

- DoT — Area
- Physical — Arc, Area, Single target

#### Buffs

- Lifedrain buff (base) — Single target — `high`

#### Debuffs

- Phys DEF debuff (base) — Area — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Taunt (base) — Area — `high`

## Bryon - Evergreen Sentinel

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
2. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)
5. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Primary damage type (unit): **Magic**

#### Damage

- DoT — Area
- Magic — Single target

#### Buffs

- Haste buff (Legendary+) — Self — `low`
- Healing (EX+5) — Single target — `high`
- Healing over time (EX+5) — Single target — `high`

#### Debuffs

- Haste debuff (base) — Area — `low`

#### Crowd Control

- Interrupt (base) — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

#### Special Effects

##### Provides

- Energy steal (base) — Single target
- Start-of-battle cast (base) — Single target
- Summoning (base) — Self
- Untargetable (EX+5) — Single target

## Callan - Grim Soulkeeper

### Synergies

1. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
3. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium)
4. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium)
5. **Athalia - Harbinger of Justice** — Max HP via Shield (single target, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Magic — Multiple targets
- Physical — All units, Area, Self, Single target

#### Buffs

- Shield (base) — Self — `low` — conditional (rare)
- Healing (Supreme+) — Single target — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Knock down (base) — All units — `high`
- Pin (base) — Multiple targets — `high`
- Stun (Mythic+) — All units — `low`

#### Special Effects

##### Provides

- Damage absorption (allies) (base) — Multiple targets
- Stored damage release (base) — Self

##### Requires

- Stored resource threshold (base) — Enemies

## Carolina - Candlelight Specter

### Synergies

1. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)
2. **Marilee - Forest's Arrow** — Crit via Crit buff (single target, low)

### Summary

#### Stats the unit benefits from

- Crit
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Self, Single target

#### Buffs

- Crit buff (Legendary+) — Self — `low`

#### Debuffs

- Haste debuff (base) — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control

- Freeze (base) — Area — `high`

## Cassadee - Azure Prodigy

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
2. **Florabelle - Blooming Maiden** — Haste via Haste buff (multiple targets, high, conditional (frequent)); Enables Ally blessing active via Ally blessing
3. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
4. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)
5. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Single target

#### Buffs

- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Magic DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Move (base) — All units — `low`
- Stun (base) — Single target — `low`

#### Special Effects

##### Provides

- Ally blessing (base) — Single target

##### Requires

- Ally blessing active (base) — Allies

## Cecia - Requiem of Thorns

### Synergies

1. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high)
2. **Fay - Colorful Dancer** — Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low)
3. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)
4. **Aliceth - Radiant Wings** — DEF Penetration via DEF Penetration buff (single target, medium)

### Summary

#### Stats the unit benefits from

- ATK SPD
- DEF Penetration
- Physical DEF
- Magic DEF
- Primary damage type (unit): **Physical**

#### Damage

- DoT — Arc, Single target
- Physical — Area, Single target

#### Buffs

- ATK SPD buff (base) — Multiple targets — `high`
- Lifedrain buff (base) — Area — `low`
- Max HP buff (base) — Single target — `high`

#### Debuffs

- Damage taken debuff (EX+10) — Single target — `medium`

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special Effects

##### Provides

- Summoning (base) — Self
- Stat absorb (Mythic+) — Single target
- Permanent stat absorb (EX+5) — Single target

##### Requires

- Enemy not CC-immune (Mythic+) — Enemies

## Chippy - Sidekick

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Physical**

#### Damage

- Physical — Single target

## Contess - Abyssal Rulekeeper

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Smokey & Meerky - Wasteland Apothecary** — Healing via Healing over time (area, medium); Energy via Energy recovery (area, medium)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
4. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

### Summary

#### Stats the unit benefits from

- Max HP
- Healing
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Multiple targets

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

#### Special Effects

##### Provides

- Start-of-battle cast (base) — All units

## Cryonaia - Arctic Revenant

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high)
5. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Max HP
- Primary damage type (unit): **Magic**

#### Damage

- DoT — Area
- Magic — All units, Area, Single target

#### Buffs

- Shield (base) — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs

- Damage taken debuff (EX+5) — Single target — `medium`

#### Crowd Control

- Immune immunity (base) — Self — Conditional
- Freeze (EX+15) — Self — `low`

#### Special Effects

##### Provides

- Enemy isolation (domain) (base) — All units
- Summoning (base) — Area

##### Requires

- Boss encounter (base) — Enemies

## Cyran - Umbral Weaver

### Synergies

1. **Marilee - Forest's Arrow** — ATK via ATK buff (area, high, conditional (frequent)); Crit via Crit buff (single target, low)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
3. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)
4. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Crit
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Area, Single target
- True damage — All units

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

#### Special Effects

##### Provides

- Summoning (base) — All units

## Daimon - Forsaken Child

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Self, Single target
- True damage (HP-based) — Area

#### Buffs

- Lifedrain buff (base) — Single target — `medium`
- Shield (base) — Area — `low`
- Damage taken reduction (Legendary+) — Self — `low`

#### Crowd Control

- Frighten (Mythic+) — Area — `medium`

## Damian - Woody Wonder

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Healing via Healing over time (area, medium); Energy via Energy recovery (area, medium)
4. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Healing
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Single target

#### Buffs

- Energy recovery (base) — Area — `medium`
- Healing (base) — Self — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Multiple targets — `high`

#### Crowd Control

- Stun (base) — Single target — `medium`

## Dionel - Venus of Dawn

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
4. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Max HP
- Execution
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target
- True damage — All units, Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `low`
- Execution buff (Supreme+) — Self — `low`
- Shield (Supreme+) — Self — `low` — conditional (frequent)

#### Debuffs

- Vitality debuff (EX+10) — Single target — `low`

#### Special Effects

##### Provides

- Untargetable (base) — Area
- Summoning (Mythic+) — All units
- Execution scaling (Supreme+) — Self

## Dunlingr - Eternal Voice

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high)
3. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
5. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Max HP
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Area, Self, Single target

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

#### Special Effects

##### Provides

- Heal lock (Curelock) (base) — All units
- Summoning (base) — Self
- Ultimate lock (Spellbind) (base) — All units

## Eironn - Stormsword

### Synergies

1. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
3. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium)
4. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium)
5. **Athalia - Harbinger of Justice** — Max HP via Shield (single target, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Arc, Area, Single target

#### Buffs

- Shield (base) — Self — `medium`

#### Debuffs

- Haste debuff (base) — Arc — `medium`
- Magic DEF debuff (base) — Arc — `medium`

#### Crowd Control

- Move (base) — Area — `medium`
- Pin (base) — Single target — `high`

## Elijah & Lailah - Celestial Twins

### Synergies

1. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
2. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
3. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
4. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
5. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Single target

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

#### Special Effects

##### Provides

- Ally positioning link (base) — Single target
- Shared HP and Energy (base) — All units

##### Requires

- Ally on positioning link (base) — —

## Evie - Royal Envoy

### Synergies

1. **Smokey & Meerky - Wasteland Apothecary** — Healing via Healing over time (area, medium); Energy via Energy recovery (area, medium)
2. **Isabella - The Taken Soul** — Healing via Healing (area, high); Energy via Energy recovery (single target, low, conditional (frequent))
3. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
4. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)
5. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)

### Summary

#### Stats the unit benefits from

- Healing
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Multiple targets, Single target

#### Buffs

- ATK buff (base) — Multiple targets — `high`
- Healing (base) — Single target — `medium`
- Invincible (base) — Self — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Crowd Control

- Move (base) — All units — `high`
- Pin (base) — All units — `high`
- Silence (base) — All units — `high`

#### Special Effects

##### Provides

- Invincibility (base) — All units
- Start-of-battle cast (base) — All units
- Summoning (base) — Single target

##### Requires

- Cooldown-gated trigger (base) — Allies

## Faramor - Silverfang Mantle

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
5. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target
- True damage — Multiple targets
- True damage (HP-based) — Single target

#### Buffs

- ATK buff (base) — Area — `low`
- Shield (base) — Self — `high`
- Haste buff (Legendary+) — Self — `medium`

#### Debuffs

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (base) — Area — `low`

#### Special Effects

##### Provides

- Summoning (base) — Single target
- Revive ally (Supreme+) — Single target

##### Requires

- Once per battle (EX+10) — Enemies

## Fay - Colorful Dancer

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Multiple targets, Single target

#### Buffs

- ATK buff (base) — Arc — `high`
- DEF buff (base) — Multiple targets — `low`
- Healing (base) — Arc — `high` — conditional (frequent)

#### Debuffs

- Magic DEF debuff (base) — Multiple targets — `low`
- Phys DEF debuff (base) — Multiple targets — `low`

## Florabelle - Blooming Maiden

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

#### Buffs

- Lifedrain buff (base) — Single target — `medium` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `medium`
- Haste buff (EX+10) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control

- Immune immunity (Supreme+) — Self — Form

#### Special Effects

##### Provides

- Summoning (base) — Self
- Ally blessing (Mythic+) — Single target

## Frieren - The Legendary Mage

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Magic**

#### Damage

- DoT — All units, Single target
- Magic — Area, Self, Single target
- True damage — All units, Single target

#### Buffs

- ATK buff (Legendary+) — Self — `low`
- Haste buff (EX+10) — Self — `low`

#### Debuffs

- Vitality debuff (base) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `low`
- Knock down (Supreme+) — Single target — `medium`

## Gala - Daughter of Dawn

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Area, Single target

#### Buffs

- Haste buff (base) — Self — `high` — conditional (frequent)
- Shield (base) — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Supreme+) — Single target — `medium`

#### Crowd Control

- Steadfast immunity (Supreme+) — Self — On skill
- Pin (base) — Single target — `medium`

#### Special Effects

##### Provides

- Summoning (Mythic+) — Single target

##### Requires

- Boss encounter (base) — Enemies

## Gerda - Soothing Siren

### Synergies

1. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
3. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium)
4. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium)
5. **Athalia - Harbinger of Justice** — Max HP via Shield (single target, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Multiple targets, Single target

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

## Granny Dahnie - Forest Guardian

### Synergies

1. **Smokey & Meerky - Wasteland Apothecary** — Healing via Healing over time (area, medium); Energy via Energy recovery (area, medium)
2. **Isabella - The Taken Soul** — Healing via Healing (area, high); Energy via Energy recovery (single target, low, conditional (frequent))
3. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
4. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)
5. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)

### Summary

#### Stats the unit benefits from

- Healing
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Single target

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

#### Special Effects

##### Provides

- Summoning (base) — Area

## Gunnar - Iron Doom

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
4. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- DoT — Area
- Physical — All units, Self, Single target

#### Buffs

- Shield (base) — Self — `high`
- Healing (Mythic+) — Single target — `high`
- Invincible (EX+15) — Single target — `high`

#### Crowd Control

- Stun (base) — All units — `low`

#### Special Effects

##### Provides

- Summoning (base) — Area
- Invincibility (EX+15) — Single target

## Gwyneth - Dragonslayer Knight

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Primary damage type (unit): **Physical**

#### Damage

- DoT — Single target
- Physical — Area, Single target

#### Buffs

- ATK SPD buff (Legendary+) — Area — `low`

#### Debuffs

- Burn debuff (base) — Single target — `medium`

#### Crowd Control

- Pin (base) — Area — `medium`
- Silence (base) — Area — `low`
- Stun (base) — Area — `low`

## Hammie - Magician

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Single target

#### Buffs

- ATK buff (base) — Single target — `high`
- Healing (base) — Single target — `high`

## Harak - Deepsea Ravager

### Synergies

1. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high)
2. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
5. **Zorya - Watcher in Stone** — Energy via Energy recovery (area, low); Life Drain via Lifedrain buff (area, medium, conditional (frequent))

### Summary

#### Stats the unit benefits from

- Max HP
- Crit
- Energy
- Life Drain
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Single target

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

#### Special Effects

##### Provides

- Instant defeat (base) — Single target
- Invincibility (base) — Single target

##### Requires

- Boss encounter (base) — Allies

## Hepler - Master of Forms

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

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

#### Special Effects

##### Provides

- Invincibility (Mythic+) — Area

##### Requires

- Form or stance active (base) — Enemies

## Hewynn - Tender Leaf

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units

#### Buffs

- Healing (base) — Single target — `high`
- ATK buff (Legendary+) — Self — `low`

#### Crowd Control

- Unaffected immunity (Mythic+) — Self — On skill

#### Special Effects

##### Requires

- Cooldown-gated trigger (base) — Allies

## Himmel - The Legendary Hero

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Enables Party composition via Support (party slot)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high); Enables Party composition via Mage (party slot)
3. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high); Enables Party composition via Support (party slot)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Enables Party composition via Tank (party slot)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Multiple targets, Single target
- True damage (HP-based) — All units

#### Buffs

- Shield (base) — Area — `low` — conditional (frequent)
- Haste buff (Legendary+) — Self — `medium`
- ATK buff (Mythic+) — Self — `high`
- Max HP buff (Mythic+) — Multiple targets — `medium`

#### Crowd Control

- Unaffected immunity (base) — Multiple targets — On skill

#### Special Effects

##### Requires

- Party composition (base) — Allies
- Boss encounter (Supreme+) — —

## Hodgkin - Reviled Captain

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Arc, Area, Single target

#### Buffs

- Healing over time (base) — Single target — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `medium`

#### Debuffs

- Energy drain (Mythic+) — Area — `medium`
- Vitality debuff (EX+5) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `low`

#### Special Effects

##### Provides

- Summoning (Mythic+) — Area

## Hugin - Maverick Smith

### Synergies

1. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
3. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
4. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
5. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Multiple targets, Single target

#### Buffs

- ATK buff (base) — Single target — `high`
- Haste buff (base) — Multiple targets — `high`
- Shield (base) — Single target — `high`

## Igor - Mad Dagger

### Synergies

1. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
2. **Ravion - Twilight's Burden** — Life Drain via Lifedrain buff (multiple targets, high)
3. **Satrana - Ember Enchantress** — Life Drain via Lifedrain buff (arc, high)
4. **Kruger - Dauntless Warrior** — Life Drain via Lifedrain buff (area, medium)
5. **Zorya - Watcher in Stone** — Life Drain via Lifedrain buff (area, medium, conditional (frequent))

### Summary

#### Stats the unit benefits from

- Life Drain
- Primary damage type (unit): **Physical**

#### Damage

- Physical — All units, Area, Single target

#### Buffs

- Healing (base) — Single target — `low`
- Lifedrain buff (Legendary+) — Self — `low`

#### Special Effects

##### Provides

- Summoning (base) — Single target
- Untargetable (base) — Area

## Indris - Chain Breaker

### Synergies

1. **Pandora - Hope Unleashed** — Enables Multiple debuffs on target via 5 debuff types; Enables Debuff on target via ATK debuff (all units)
2. **Sinbad - Seaside Savant** — Enables Multiple debuffs on target via 6 debuff types; Enables Debuff on target via ATK debuff (multiple targets)
3. **Lyca - Keeper of Glades** — Enables Multiple debuffs on target via 2 debuff types; Enables Debuff on target via ATK debuff (all units)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Enables Multiple debuffs on target via 2 debuff types; Enables Debuff on target via Max HP debuff (area)
5. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Enables Multiple debuffs on target via 2 debuff types; Enables Debuff on target via ATK debuff (multiple targets)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target
- True damage — Multiple targets
- True damage (HP-based) — Single target

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

#### Special Effects

##### Requires

- Cooldown-gated trigger (base) — Enemies
- Debuff on target (base) — Enemies
- Multiple debuffs on target (base) — Enemies

## Isabella - The Taken Soul

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Haste
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Single target

#### Buffs

- Haste buff (base) — Multiple targets — `low` — conditional (frequent)
- Healing (base) — Area — `high`
- Energy recovery (EX+10) — Single target — `low` — conditional (frequent)
- ATK SPD buff (Supreme+) — Self — `low`

#### Debuffs

- ATK debuff (base) — Single target — `low`

#### Crowd Control

- Unaffected immunity (base) — Single target — Once

#### Special Effects

##### Requires

- Once per battle (base) — Allies

## Kafra - Gale Rider

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high)
5. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Single target

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

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Single target

## Koko - Wild Child

### Synergies

1. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high)
2. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
5. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)

### Summary

#### Stats the unit benefits from

- Haste
- Energy
- Life Drain
- Primary damage type (unit): **Physical**

#### Damage

- Physical — All units, Area, Single target
- True damage — All units

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

## Kordan - Ironblood Chieftain

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
3. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
5. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))

### Summary

#### Stats the unit benefits from

- ATK
- Max HP
- Healing
- DEF Penetration
- Life Drain
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Multiple targets, Single target

#### Buffs

- Lifedrain buff (base) — Area — `high`
- Shield (base) — Self — `medium`
- ATK buff (Legendary+) — Self — `medium`
- Healing over time (EX+10) — Self — `low`

#### Crowd Control

- Knock down (base) — Single target — `high`
- Move (base) — Area — `high`
- Pin (base) — Area — `high`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Korin - Wood Warden

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
2. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
3. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
4. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)
5. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target
- True damage — Single target
- True damage (HP-based) — Area, Single target

#### Buffs

- Shield (base) — Single target — `medium`
- Haste buff (Legendary+) — Self — `medium`
- ATK SPD buff (EX+5) — Self — `high`
- Damage taken reduction (Supreme+) — Self — `medium`

#### Crowd Control

- Pin (base) — Single target — `medium`

## Kruger - Dauntless Warrior

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

#### Buffs

- Lifedrain buff (Mythic+) — Area — `medium`
- Shield (Mythic+) — Single target — `low`

#### Debuffs

- Phys DEF debuff (base) — Single target — `high`

## Kulu - Blast Master

### Synergies

1. **Aliceth - Radiant Wings** — ATK via ATK buff (multiple targets, medium); DEF Penetration via DEF Penetration buff (single target, medium)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
3. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- DEF Penetration
- Primary damage type (unit): **Physical**

#### Damage

- Physical — All units, Area, Single target

#### Buffs

- Invincible (base) — Self — `high` — conditional (frequent)
- ATK buff (Legendary+) — Self — `low`

#### Debuffs

- Movement speed debuff (base) — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control

- Unaffected immunity (base) — Area — On ultimate
- Move (base) — Single target — `high`

#### Special Effects

##### Provides

- Invincibility (base) — Single target
- Summoning (base) — Area

## Laios - Dungeon Adventurer

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
5. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Haste
- Max HP
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Single target

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

#### Special Effects

##### Provides

- Summoning (base) — Single target

##### Requires

- Monster ingredients (base) — Enemies
- Stacked resource (base) — Enemies
- Enemy monsters present (Mythic+) — Enemies

## Lenya - Wild Cyclone

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Crit
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target

#### Buffs

- Crit buff (base) — Self — `high`
- Haste buff (Legendary+) — Self — `medium`
- Shield (EX+5) — Self — `medium` — conditional (frequent)
- Damage taken reduction (Supreme+) — Self — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Once
- Stun (base) — Area — `high`

## Lily May - Twilight Tracker

### Synergies

1. **Aliceth - Radiant Wings** — ATK via ATK buff (multiple targets, medium); DEF Penetration via DEF Penetration buff (single target, medium)

### Summary

#### Stats the unit benefits from

- ATK
- DEF Penetration
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Single target
- True damage (HP-based) — Self, Single target

#### Buffs

- ATK buff (base) — Self — `low`
- Invincible (base) — Self — `high`

#### Debuffs

- Energy drain (base) — All units — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle
- Interrupt (base) — All units — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Single target
- Untargetable (base) — All units

## Lorsan - Windweaver Protector

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Single target

#### Buffs

- Healing over time (base) — Single target — `medium`
- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Multiple targets — `high`

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — On skill
- Stun (EX+10) — Multiple targets — `high`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Lucca - Stalwart Fighter

### Synergies

1. **Lumont - Benign Horn** — Physical DEF via DEF buff (area, high); Magic DEF via DEF buff (area, high)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
4. **Fay - Colorful Dancer** — Physical DEF via DEF buff (multiple targets, low); Magic DEF via DEF buff (multiple targets, low)
5. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- Max HP
- Physical DEF
- Magic DEF
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target

#### Buffs

- Damage taken reduction (base) — Self — `high`
- Shield (base) — Self — `medium`
- Max HP buff (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control

- Immune immunity (base) — Self — On skill
- Interrupt (base) — Single target — `medium`
- Stun (base) — Area — `medium`

## Lucius - The Lightbringer

### Synergies

1. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
2. **Isabella - The Taken Soul** — Healing via Healing (area, high)
3. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)
4. **Mikola - Warbeat Compere** — Healing via Healing over time (all units, medium)
5. **Lorsan - Windweaver Protector** — Healing via Healing (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Healing
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

#### Buffs

- Healing (base) — Single target — `medium`
- Shield (base) — Area — `high`
- Healing stat buff (Legendary+) — Self — `low`

#### Debuffs

- ATK debuff (Mythic+) — Area — `high`

#### Crowd Control

- Move (base) — Single target — `high`
- Stun (base) — Single target — `low`

#### Special Effects

##### Provides

- Reposition enemies (base) — Single target

## Lucy - Celestial Spirit Mage

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
2. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
3. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
4. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)
5. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Single target

#### Buffs

- Haste buff (Legendary+) — Self — `medium`
- Shield (Mythic+) — Single target — `high`

#### Debuffs

- Damage taken debuff (base) — Single target — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Single target — `medium`

## Ludovic - Wreathed Eternalist

### Synergies

1. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
2. **Isabella - The Taken Soul** — Healing via Healing (area, high)
3. **Mikola - Warbeat Compere** — Healing via Healing over time (all units, medium)
4. **Lorsan - Windweaver Protector** — Healing via Healing (multiple targets, high)
5. **Antandra - Desert Fury** — Healing via Healing (area, medium)

### Summary

#### Stats the unit benefits from

- Healing
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Single target

#### Buffs

- Healing (base) — Area — `high`
- Healing over time (base) — Area — `high`
- Healing stat buff (Legendary+) — Self — `high`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (Supreme+) — Single target — `medium`

#### Special Effects

##### Provides

- Revive ally (base) — Area

## Lumont - Benign Horn

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
5. **Florabelle - Blooming Maiden** — Haste via Haste buff (multiple targets, high, conditional (frequent)); Max HP via Shield (single target, medium)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

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

## Lyca - Keeper of Glades

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Primary damage type (unit): **Physical**

#### Damage

- Physical — All units, Area, Self, Single target

#### Buffs

- ATK SPD buff (base) — Self — `medium`

#### Debuffs

- ATK debuff (base) — All units — `high`
- Phys DEF debuff (base) — All units — `high`

#### Crowd Control

- Stun (EX+10) — Single target — `low`

#### Special Effects

##### Provides

- Summoning (base) — Single target

## Marcille - Elven Mage

### Synergies

1. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
3. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
4. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
5. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Area, Single target

#### Buffs

- Haste buff (base) — Self — `low`
- Healing (base) — Single target — `low` — conditional (rare)

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — On skill
- Interrupt (Mythic+) — Single target — `high`

#### Special Effects

##### Provides

- Summoning (base) — Area
- Revive ally (Mythic+) — Single target

##### Requires

- Once per battle (Mythic+) — Allies

## Marilee - Forest's Arrow

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)
3. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Crit
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Multiple targets, Single target
- True damage — Multiple targets

#### Buffs

- ATK buff (base) — Area — `high` — conditional (frequent)
- Crit buff (Legendary+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `low`

## Mehira - Mind Cager

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
2. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
3. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Healing
- Life Drain
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Self, Single target

#### Buffs

- Haste buff (base) — Single target — `medium`
- Lifedrain buff (Legendary+) — Self — `medium`
- Max HP buff (Legendary+) — Self — `high`
- Healing (Mythic+) — Self — `low`

#### Debuffs

- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Charm (base) — Area — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Self
- HP threshold strike (Mythic+) — Self
- Untargetable (Mythic+) — Self

## Mikola - Warbeat Compere

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Healing
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Multiple targets

#### Buffs

- ATK buff (base) — Self — `medium`
- Haste buff (base) — Multiple targets — `high`
- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — All units — `medium`

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — Conditional

## Mirael - Scarlet Sorceress

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Primary damage type (unit): **Magic**

#### Damage

- DoT — Single target
- Magic — Area, Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Single target

## Nara - Wrathful Wraith

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
5. **Soren - Silent Fury** — Energy via Energy recovery (single target, high)

### Summary

#### Stats the unit benefits from

- ATK
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target
- True damage — Single target

#### Buffs

- ATK buff (Legendary+) — Self — `low`
- Healing (Mythic+) — Single target — `low`
- Energy recovery (Supreme+) — Single target — `low`

#### Debuffs

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (Supreme+) — Self — Permanent

## Natsu - Fire Dragon Slayer Mage

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Crit
- Primary damage type (unit): **Magic**

#### Damage

- DoT — Single target
- Magic — Area, Single target

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

## Nazrik - Soulstalker

### Synergies

1. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)
2. **Marilee - Forest's Arrow** — Crit via Crit buff (single target, low)

### Summary

#### Stats the unit benefits from

- Crit
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Self, Single target
- True damage — Single target
- True damage (HP-based) — Single target

#### Buffs

- Crit buff (Legendary+) — Self — `low`

#### Debuffs

- Max HP debuff (base) — Single target — `low`
- Damage taken debuff (EX+10) — Self — `low`
- Vitality debuff (EX+10) — Self — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

## Nerion - Bereaved Tide

### Synergies

1. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
5. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Max HP
- Energy
- DEF Penetration
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Self, Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`
- Shield (EX+10) — Self — `medium`

#### Debuffs

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

## Niru - Soul Collector

### Synergies

1. **Aliceth - Radiant Wings** — Enables Enemy defeat via Instant defeat
2. **Harak - Deepsea Ravager** — Enables Enemy defeat via Instant defeat
3. **Cassadee - Azure Prodigy** — Enables Ally blessing active via Ally blessing
4. **Florabelle - Blooming Maiden** — Enables Ally blessing active via Ally blessing
5. **Mehira - Mind Cager** — Enables Enemy defeat via HP threshold strike

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Self, Single target

#### Buffs

- Healing (base) — Single target — `low` — conditional (rare)
- DEF buff (EX+5) — Self — `low`

#### Special Effects

##### Provides

- Spirit form protection (base) — Single target
- Start-of-battle cast (Mythic+) — Self

##### Requires

- Ally blessing active (base) — Allies
- Enemy defeat (base) — Allies

## Odie - Desert Defender

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Primary damage type (unit): **Magic**

#### Damage

- DoT — Single target
- Magic — Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`

## Pandora - Hope Unleashed

### Synergies

1. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
2. **Ravion - Twilight's Burden** — Energy via Energy recovery (multiple targets, high)
3. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
4. **Smokey & Meerky - Wasteland Apothecary** — Energy via Energy recovery (area, medium)
5. **Soren - Silent Fury** — Energy via Energy recovery (single target, high)

### Summary

#### Stats the unit benefits from

- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Single target

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

#### Special Effects

##### Provides

- Invincibility (base) — Single target

## Pang - Bamboo Guardian

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Energy
- DEF Penetration
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

#### Buffs

- Haste buff (base) — Self — `high` — conditional (frequent)
- Shield (base) — Single target — `high`
- ATK buff (Legendary+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Stun (base) — Area — `low`

#### Special Effects

##### Provides

- Transform (base) — Single target

## Parisa - Ode to Flowers

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Energy via Energy recovery (area, medium)
4. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Multiple targets, Self, Single target

#### Buffs

- ATK SPD buff (base) — Self — `low`
- ATK buff (Legendary+) — Self — `medium`

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Area

## Perseus - Chosen Champion

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high)
5. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target
- True damage — Multiple targets

#### Buffs

- Max HP buff (base) — Area — `low`
- Shield (base) — Self — `medium`
- ATK buff (Legendary+) — Multiple targets — `medium`
- Damage taken reduction (Mythic+) — Self — `medium`

#### Crowd Control

- Unaffected immunity (base) — Multiple targets — On skill
- Stun (base) — Area — `medium`

## Phraesto - Misty Scorpion

### Synergies

1. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- Max HP
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Single target

#### Buffs

- Healing (base) — Single target — `low`
- Max HP buff (base) — Single target — `low`
- Shield (base) — Self — `high`

#### Crowd Control

- Stun (Mythic+) — Single target — `medium`
- Taunt (Mythic+) — Single target — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Self

## Pippa - The Muddled Magician

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
2. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)
5. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Multiple targets, Single target
- True damage — Area

#### Buffs

- Haste buff (Legendary+) — Self — `low`

#### Debuffs

- Energy drain (base) — Area — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Knock down (base) — Single target — `low`
- Move (base) — Single target — `low`
- Pin (base) — Single target — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Ravion - Twilight's Burden

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
3. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
4. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Multiple targets, Single target

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

#### Special Effects

##### Provides

- Position swap (EX+10) — Multiple targets

##### Requires

- Boss encounter (base) — Allies

## Reinier - Symmetric Sin

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Multiple targets, Single target

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

## Rhys - Fiery Cavalier

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)
3. **Harak - Deepsea Ravager** — Crit via Crit buff (single target, medium)
4. **Marilee - Forest's Arrow** — Crit via Crit buff (single target, low)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Crit
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Arc, Single target

#### Buffs

- Healing (base) — Single target — `medium`
- Crit buff (Legendary+) — Self — `low`

#### Crowd Control

- Move (base) — Single target — `high`

## Rowan - The Roamer

### Synergies

1. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
3. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
4. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
5. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Single target

#### Buffs

- Healing (base) — Single target — `low` — conditional (rare)
- Haste buff (Legendary+) — Self — `low`
- DEF buff (Mythic+) — Single target — `low` — conditional (rare)
- Max HP buff (Mythic+) — Single target — `low` — conditional (rare)
- ATK buff (EX+5) — Single target — `low`

#### Debuffs

- Energy drain (base) — Single target — `medium`

#### Special Effects

##### Provides

- Energy steal (base) — Single target

##### Requires

- Once per battle (Mythic+) — Allies

## Saida - Vampiric Vine

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Area, Multiple targets, Self, Single target

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

#### Special Effects

##### Provides

- Revive ally (base) — Single target

##### Requires

- Boss encounter (base) — Enemies

## Salazer - Lash of Bantus

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Physical**

#### Damage

- Physical — Single target

#### Buffs

- Lifedrain buff (base) — Single target — `low`
- Damage taken reduction (Legendary+) — Self — `medium`
- Healing (Supreme+) — Single target — `high`
- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special Effects

##### Provides

- Summoning (base) — Single target

## Satrana - Ember Enchantress

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- Primary damage type (unit): **Magic**

#### Damage

- Magic — Arc, Area, Single target

#### Buffs

- Invincible (base) — Self — `high`
- Lifedrain buff (base) — Arc — `high`
- Damage taken reduction (Legendary+) — Self — `medium`

#### Debuffs

- Vitality debuff (base) — Area — `low`

#### Crowd Control

- Charm (base) — Single target — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Area

## Scarlita - Herald of Compassion

### Synergies

1. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
2. **Ravion - Twilight's Burden** — Energy via Energy recovery (multiple targets, high)
3. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
4. **Smokey & Meerky - Wasteland Apothecary** — Energy via Energy recovery (area, medium)
5. **Soren - Silent Fury** — Energy via Energy recovery (single target, high)

### Summary

#### Stats the unit benefits from

- Execution
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets

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

#### Special Effects

##### Provides

- Invincibility (base) — Area

## Seth - Swift Shadow

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent)); Life Drain via Lifedrain buff (single target, low)
3. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
4. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Crit
- Energy
- Life Drain
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Self, Single target

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

#### Special Effects

##### Provides

- Invincibility (base) — Single target

## Shadewing - Undying Vow

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Life Drain via Lifedrain buff (multiple targets, high); Enables Debuff on target via ATK debuff (multiple targets)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Enables Debuff on target via ATK debuff (area)
3. **Hepler - Master of Forms** — Max HP via Shield (multiple targets, low); Enables Debuff on target via Haste debuff (area); Enables Continuous damage on enemies via tick damage
4. **Koko - Wild Child** — Max HP via Shield (single target, low); Life Drain via Lifedrain buff (multiple targets, medium); Enables Debuff on target via Damage taken debuff (area)
5. **Natsu - Fire Dragon Slayer Mage** — Enables Debuff on target via Haste debuff (area); Enables Continuous damage on enemies via DoT

### Summary

#### Stats the unit benefits from

- ATK
- Max HP
- Energy
- Life Drain
- Primary damage type (unit): **Magic**

#### Damage

- DoT — Single target
- Magic — All units, Single target
- True damage — Single target

#### Buffs

- Invincible (base) — Self — `high`
- ATK buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Single target — `low`
- Lifedrain buff (Supreme+) — Self — `low`
- Shield (Supreme+) — Self — `low`

#### Debuffs

- Magic DEF debuff (base) — All units — `low`

#### Special Effects

##### Provides

- Debuff application (base) — Single target
- DoT conversion (base) — All units
- Invincibility (base) — All units
- Damage leech from allies (Supreme+) — Self

##### Requires

- Continuous damage on enemies (base) — Enemies
- Debuff on target (base) — Enemies

## Shakir - Furious Howl

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
2. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)
5. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Arc, Area, Multiple targets, Single target

#### Buffs

- Damage taken reduction (base) — Multiple targets — `low` — conditional (frequent)
- Haste buff (base) — Multiple targets — `low`
- Lifedrain buff (base) — Single target — `medium`

#### Debuffs

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Form

#### Special Effects

##### Provides

- Transform (base) — Area

##### Requires

- Form or stance active (base) — Enemies

## Shemira - Corpsemaker

### Synergies

1. **Smokey & Meerky - Wasteland Apothecary** — Healing via Healing over time (area, medium); Energy via Energy recovery (area, medium)
2. **Isabella - The Taken Soul** — Healing via Healing (area, high); Energy via Energy recovery (single target, low, conditional (frequent))
3. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
4. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)
5. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)

### Summary

#### Stats the unit benefits from

- Healing
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Area, Self, Single target
- True damage (HP-based) — Area, Single target

#### Buffs

- Healing (base) — Self — `medium` — conditional (frequent)
- Shield (base) — Single target — `medium`

#### Special Effects

##### Provides

- Summoning (base) — Self

## Silven - Heir of Glory

### Synergies

1. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
3. **Ravion - Twilight's Burden** — Energy via Energy recovery (multiple targets, high)
4. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
5. **Smokey & Meerky - Wasteland Apothecary** — Energy via Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Energy
- DEF Penetration
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Single target
- True damage (HP-based) — Self, Single target

#### Buffs

- ATK SPD buff (Legendary+) — Self — `medium`
- Energy recovery (Mythic+) — Self — `low`

#### Special Effects

##### Provides

- Summoning (base) — Single target

## Silvina - The Taken Breath

### Synergies

1. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
3. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium)
4. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium)
5. **Athalia - Harbinger of Justice** — Max HP via Shield (single target, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Crit
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Single target

#### Buffs

- Crit buff (Legendary+) — Self — `low`
- Shield (Mythic+) — Self — `high`

#### Debuffs

- Energy drain (base) — Single target — `high`
- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (base) — Single target — `low`
- Frighten (EX+10) — Area — `low`

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Single target

## Sinbad - Seaside Savant

### Synergies

1. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
2. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
3. **Ravion - Twilight's Burden** — Energy via Energy recovery (multiple targets, high)
4. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
5. **Smokey & Meerky - Wasteland Apothecary** — Energy via Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Multiple targets, Self, Single target

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

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Multiple targets

## Smokey & Meerky - Wasteland Apothecary

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Energy via Energy recovery (multiple targets, high)
2. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
3. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)
4. **Soren - Silent Fury** — Energy via Energy recovery (single target, high)
5. **Scarlita - Herald of Compassion** — Energy via Energy recovery (area, low)

### Summary

#### Stats the unit benefits from

- ATK
- Energy
- Primary damage type (unit): **Magic**

#### Buffs

- Energy recovery (base) — Area — `medium`
- Healing (base) — Multiple targets — `medium`
- Healing over time (base) — Area — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control

- Interrupt (base) — Area — `medium`
- Stun (EX+10) — Single target — `low`

## Solise - Floral Wonder

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Multiple targets, Single target

#### Buffs

- Healing (base) — Multiple targets — `high` — conditional (frequent)
- Shield (base) — Multiple targets — `medium`
- ATK buff (Legendary+) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle

#### Special Effects

##### Provides

- Summoning (base) — Single target
- Ally blessing (Mythic+) — Single target

## Sonja - Crimson Queenpin

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

#### Buffs

- ATK buff (base) — Multiple targets — `low` — conditional (frequent)
- Haste buff (Legendary+) — Self — `low`
- Damage taken reduction (EX+10) — Self — `low`

#### Crowd Control

- Stun (base) — Area — `low`

## Soren - Silent Fury

### Synergies

1. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
3. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
4. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
5. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Multiple targets, Self, Single target

#### Buffs

- Damage taken reduction (base) — Self — `low`
- Haste buff (Legendary+) — Self — `low` — conditional (rare)
- Healing over time (Mythic+) — Single target — `low` — conditional (rare)
- Energy recovery (Supreme+) — Single target — `high`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control

- Move (base) — Multiple targets — `high`
- Stun (base) — Area — `medium`

## Sylphira - Sovereign of Song

### Synergies

1. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
2. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)
3. **Isabella - The Taken Soul** — Haste via Haste buff (multiple targets, low, conditional (frequent)); Healing via Healing (area, high)
4. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)
5. **Ludovic - Wreathed Eternalist** — Healing via Healing over time (area, high)

### Summary

#### Stats the unit benefits from

- Haste
- Healing
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Single target
- True damage (HP-based) — Single target

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

#### Special Effects

##### Provides

- Dispel debuffs (Mythic+) — Self

## Talene - Resurging Flame

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Perseus - Chosen Champion** — ATK via ATK buff (multiple targets, medium); Max HP via Max HP buff (area, low)
4. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Max HP via Shield (single target, high)
5. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Max HP
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Single target

#### Buffs

- Healing (base) — Area — `low` — conditional (frequent)
- Healing over time (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Area — `low`
- ATK buff (Legendary+) — Self — `low`

#### Special Effects

##### Provides

- Summoning (base) — Area
- Transform (base) — Area

## Tasi - Fairy of Dreams

### Synergies

1. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
2. **Sylphira - Sovereign of Song** — ATK via ATK buff (area, high, conditional (frequent)); Haste via Haste buff (area, medium, conditional (frequent))
3. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
4. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium)
5. **Hugin - Maverick Smith** — ATK via ATK buff (single target, high); Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Primary damage type (unit): **Magic**

#### Damage

- DoT — All units, Single target
- Magic — Area, Single target

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

#### Special Effects

##### Provides

- Invincibility (base) — Area
- Sleep (area) (base) — Single target
- Summoning (base) — All units
- Transform (base) — Area

## Temesia - Lightsavior

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Healing via Healing over time (area, medium); Energy via Energy recovery (area, medium)
3. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
4. **Fay - Colorful Dancer** — ATK via ATK buff (arc, high); Healing via Healing (arc, high, conditional (frequent))
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)

### Summary

#### Stats the unit benefits from

- ATK
- ATK SPD
- Max HP
- Healing
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — All units, Area, Single target
- True damage — Single target

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

#### Special Effects

##### Provides

- Summoning (base) — All units

## Thador - Ironsworn General

### Synergies

1. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high); Healing via Healing (area, medium)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Healing via Healing (single target, medium)
3. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium); Healing via Healing (multiple targets, high, conditional (frequent))
4. **Elijah & Lailah - Celestial Twins** — Max HP via Max HP buff (multiple targets, high); Healing via Healing (multiple targets, low)
5. **Gerda - Soothing Siren** — Healing via Healing over time (area, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Crit
- Healing
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target

#### Buffs

- Shield (base) — Self — `medium`
- Damage taken reduction (Legendary+) — Self — `medium`
- Healing (Supreme+) — Self — `low`
- Healing over time (Supreme+) — Self — `low`

#### Debuffs

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control

- Knock down (base) — Single target — `low`

#### Special Effects

##### Provides

- Summoning (Mythic+) — Single target

## Thoran - Fallen King

### Synergies

1. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- Max HP
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Self, Single target

#### Buffs

- Healing (base) — Single target — `low` — conditional (rare)
- Lifedrain buff (base) — Single target — `high` — conditional (frequent)
- Max HP buff (base) — Self — `low`

#### Crowd Control

- Unaffected immunity (base) — Self — On skill
- Interrupt (base) — Single target — `low`

## Tilaya - Wild Blade

### Synergies

1. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
2. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
3. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium)
4. **Solise - Floral Wonder** — Max HP via Shield (multiple targets, medium)
5. **Athalia - Harbinger of Justice** — Max HP via Shield (single target, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Arc, Area, Single target

#### Buffs

- Damage taken reduction (base) — Arc — `high` — conditional (frequent)
- Healing over time (base) — Arc — `high` — conditional (frequent)
- Shield (base) — Self — `medium` — conditional (frequent)
- Healing (Mythic+) — Single target — `medium`
- Max HP buff (EX+10) — Area — `low`

#### Crowd Control

- Unaffected immunity (base) — Arc — Start of battle

#### Special Effects

##### Provides

- Start-of-battle cast (base) — Arc

## Ulmus - Grove Keeper

### Synergies

1. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
3. **Temesia - Lightsavior** — Energy via Energy recovery (area, high)
4. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)
5. **Damian - Woody Wonder** — Energy via Energy recovery (area, medium)

### Summary

#### Stats the unit benefits from

- Max HP
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

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

## Vala - Phantom of Oakenfell

### Synergies

1. **Ravion - Twilight's Burden** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
2. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high); Healing via Healing over time (all units, medium)
3. **Smokey & Meerky - Wasteland Apothecary** — ATK via ATK buff (multiple targets, low); Healing via Healing over time (area, medium); Energy via Energy recovery (area, medium)
4. **Aurora - Celestial of Dreams** — ATK via ATK buff (multiple targets, high); Haste via Haste buff (multiple targets, high)
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Healing via Healing (multiple targets, low)

### Summary

#### Stats the unit benefits from

- ATK
- Haste
- Healing
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Single target
- True damage — Single target

#### Buffs

- ATK buff (Legendary+) — Self — `medium`
- Haste buff (Mythic+) — Multiple targets — `high`
- Healing (EX+10) — Self — `low`

#### Debuffs

- Haste debuff (base) — Single target — `high`

#### Crowd Control

- Stun (base) — Single target — `medium`

#### Special Effects

##### Provides

- Marked target (focus fire) (base) — Self
- Untargetable (Mythic+) — Multiple targets

##### Requires

- Enemy defeat (Legendary+) — Enemies

## Valen - Roving Swordsman

### Synergies

_No synergy partners matched stat buffs or enablers._

### Summary

#### Stats the unit benefits from

- ATK
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Single target

#### Buffs

- ATK buff (base) — Area — `high`
- Invincible (base) — Self — `high`

#### Debuffs

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control

- Stun (Supreme+) — Single target — `medium`

#### Special Effects

##### Provides

- Invincibility (base) — Area

## Valka - Forsaken Blade

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high); Enables Adjacent allies via Multiple ally buffs
2. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Enables Adjacent allies via Multiple ally buffs
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium); Enables Adjacent allies via Multiple ally buffs
4. **Lucius - The Lightbringer** — Max HP via Shield (area, high); Enables Adjacent allies via Multiple ally buffs
5. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high); Max HP via Max HP buff (single target, high); Enables Adjacent allies via Multiple ally buffs

### Summary

#### Stats the unit benefits from

- ATK SPD
- Haste
- Max HP
- Energy
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target
- True damage (HP-based) — Area

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

#### Special Effects

##### Requires

- Adjacent allies (base) — Allies

## Velara - Pale Votary

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium); Energy via Energy recovery (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium)
4. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
5. **Lucius - The Lightbringer** — Max HP via Shield (area, high)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Area, Single target

#### Buffs

- Haste buff (base) — Self — `low`
- Healing (base) — Multiple targets — `low`
- Shield (Mythic+) — Self — `high`

#### Debuffs

- Haste debuff (base) — Single target — `medium`

#### Crowd Control

- Pin (base) — Single target — `high`

#### Special Effects

##### Provides

- Start-of-battle cast (base) — All units
- Summoning (base) — All units

##### Requires

- Boss encounter (base) — Allies

## Viperian - Shadow Serpent

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)
2. **Aurora - Celestial of Dreams** — Haste via Haste buff (multiple targets, high)
3. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high)
4. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high)
5. **Mikola - Warbeat Compere** — Haste via Haste buff (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Haste
- Primary damage type (unit): **Magic**

#### Damage

- Magic — All units, Single target

#### Buffs

- Healing (base) — Single target — `high`
- Haste buff (Legendary+) — Self — `medium`
- Lifedrain buff (EX+5) — Single target — `low`

#### Debuffs

- Energy drain (base) — Single target — `medium`

#### Crowd Control

- Unaffected immunity (base) — Self — Start of battle

## Walker - Wildland Outlaw

### Synergies

1. **Ravion - Twilight's Burden** — Max HP via Shield (multiple targets, medium); Life Drain via Lifedrain buff (multiple targets, high)
2. **Kordan - Ironblood Chieftain** — Life Drain via Lifedrain buff (area, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Kruger - Dauntless Warrior** — Max HP via Shield (single target, low); Life Drain via Lifedrain buff (area, medium)
5. **Saida - Vampiric Vine** — Max HP via Shield (multiple targets, high)

### Summary

#### Stats the unit benefits from

- Max HP
- Crit
- Life Drain
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Arc, Area, Self, Single target

#### Buffs

- Damage taken reduction (base) — Self — `medium`
- Crit buff (Legendary+) — Self — `high`
- Lifedrain buff (Supreme+) — Self — `medium`
- Shield (Supreme+) — Self — `low`

#### Crowd Control

- Stun (base) — Single target — `medium`

## Zandrok - Watchful Edge

### Synergies

1. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high); Max HP via Max HP buff (multiple targets, high)
2. **Hugin - Maverick Smith** — Haste via Haste buff (multiple targets, high); Max HP via Shield (single target, high)
3. **Lucius - The Lightbringer** — Max HP via Shield (area, high)
4. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Max HP via Shield (multiple targets, medium)
5. **Florabelle - Blooming Maiden** — Haste via Haste buff (multiple targets, high, conditional (frequent)); Max HP via Shield (single target, medium)

### Summary

#### Stats the unit benefits from

- Haste
- Max HP
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Multiple targets, Self, Single target

#### Buffs

- Haste buff (base) — Area — `medium` — conditional (frequent)
- Lifedrain buff (base) — Area — `low` — conditional (frequent)
- Max HP buff (Legendary+) — Self — `low`

#### Crowd Control

- Stun (base) — Area — `low`

#### Special Effects

##### Provides

- Summoning (base) — Area

## Zanie - Timeless Tinkerer

### Synergies

1. **Cecia - Requiem of Thorns** — ATK SPD via ATK SPD buff (multiple targets, high)
2. **Gwyneth - Dragonslayer Knight** — ATK SPD via ATK SPD buff (area, low)

### Summary

#### Stats the unit benefits from

- ATK SPD
- Primary damage type (unit): **Physical**

#### Damage

- Physical — Area, Self, Single target

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

## Zorya - Watcher in Stone

### Synergies

1. **Damian - Woody Wonder** — Haste via Haste buff (multiple targets, high); Energy via Energy recovery (area, medium); Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
2. **Ravion - Twilight's Burden** — Haste via Haste buff (multiple targets, medium); Energy via Energy recovery (multiple targets, high); Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
3. **Temesia - Lightsavior** — Energy via Energy recovery (area, high); Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
4. **Smokey & Meerky - Wasteland Apothecary** — Energy via Energy recovery (area, medium); Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
5. **Elijah & Lailah - Celestial Twins** — Haste via Haste buff (all units, high)

### Summary

#### Stats the unit benefits from

- Haste
- Energy
- Primary damage type (unit): **Magic**

#### Damage

- Magic — Arc, Area, Single target

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

#### Special Effects

##### Provides

- Invincibility (base) — Area
- Summoning (base) — Arc

##### Requires

- Ally Ultimate casts (Mythic+) — Allies
