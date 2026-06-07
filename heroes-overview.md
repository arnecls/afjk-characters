# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buffs matching **Stats the unit benefits from**, and
enabler partners matching **Requires** special effects.
Up to five partners by combined score. Omitted: ATK-only, Max HP
buff-only, and Shield-only (unless the hero benefits from Max HP/
shields). Rare conditional buffs score lower.
Regenerate: `python3 scripts/generate-heroes-overview.py`.

## Aliceth

### Aliceth's behavior

- Movement: stationary (avg attack range 8.0 tiles)
- Signature skill: Radiant Rain (ultimate) — aerial area arrow rain
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Aliceth benefits from

Look for units providing: `ATK` `DEF Penetration`  
Common buffers are **Lyca**, **Ravion**, or **Lucius**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
- **Lily May**
  - DEF Penetration buff (single target, low)
  - Enables Debuff on target via Energy drain (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Debuff on target via Haste debuff (area)
- **Hepler**
  - ATK SPD via Haste buff (single target, low) [signature fuel]
  - Enables Debuff on target via Haste debuff (area)
- **Frieren**
  - Enables Debuff on target via DoT (area)

### Units that can act as a replacement for Aliceth

**Damage**

- Kordan (89% `Physical` `HP loss`)
- Ravion (89% `Physical` `HP loss`)
- Harak (77% `Physical` `HP loss`)

**Crowd Control**

- Bonnie (50% `Stun`)
- Lucius (50% `Move` `Stun`)
- Lyca (50% `Stun`)

### Summary for Aliceth

#### Stats Aliceth benefits from

- ATK
- DEF Penetration

#### Damage types dealt by Aliceth

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`

#### Buffs provided by Aliceth

- Ally empower buff — Single target — `low`
- Attack range buff — Single target — `low`
- DEF Penetration buff — Multiple targets — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`
- Fatal blow immunity (Mythic+) — Single target — `high` — conditional (rare)
- Healing (Mythic+) — Single target — `low`

#### Debuffs provided by Aliceth

- Execution debuff — Multiple targets — `medium`
- Marked target (focus fire) — Single target — `medium`
- Blind HP loss debuff (EX+15) — Area — `low`

#### Crowd Control provided by Aliceth

- Move — Single target — `low`
- Stun — Single target — `low`

#### Aliceth's Special Effects

#### Aliceth Provides

- Ally grant (Brightfeather) — Single target
- Instant defeat — Multiple targets
- Invincibility — Single target
- Marked target (focus fire) — Single target
- Reposition enemies — Single target
- Fatal blow save (Mythic+) — Area

#### Aliceth Requires

- Passive with internal cooldown — Allies
- Ranged damage from allies — Allies
- Debuff on target (Legendary+) — Enemies

## Alna

### Alna's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Winter Anthem (ultimate) — battle-start area blizzard
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Alna benefits from

Look for units providing: `Max HP`  
Common buffers are **Lucius** or **Hugin**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Gala**
  - Max HP via Shield (single target, high)

### Units benefitting from Alna

- Shadewing
- Aliceth

### Units that can act as a replacement for Alna

**Damage**

- Thador (55% `Physical` `DoT`)
- Zanie (55% `DoT` `Physical`)
- Igor (50% `Physical`)

### Summary for Alna

#### Stats Alna benefits from

- Max HP

#### Damage types dealt by Alna

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Self, Single target
- DoT — All units

#### Buffs provided by Alna

- Ally empower buff — Single target — `low`
- Healing — Single target — `low`
- Healing over time — Single target — `high`
- Max HP buff — Single target — `low`
- Damage and control immunity (EX+15) — Single target — `high`
- ATK buff (Supreme+) — Single target — `medium`

#### Debuffs provided by Alna

- Haste debuff — Area — `high`
- Vitality debuff (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Freeze (Supreme+) — Area — `medium`

#### Alna's Special Effects

#### Alna Provides

- Ally empower — Single target
- Start-of-battle cast — All units
- Damage and control immunity (Mythic+) — Self
- Damage and control immunity (ally) (EX+15) — Single target

## Alsa

### Alsa's behavior

- Movement: mostly stationary (avg attack range 6.0 tiles)
- Signature skill: Twirling Rocks (ultimate) — area physical rock damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Alsa benefits from

Look for units providing: `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]

### Units that can act as a replacement for Alsa

**Similar Skills**

- Kulu (100% `battlefield-modification`)

**Damage**

- Lily May (93% `Magic`)
- Sylphira (84% `Magic`)
- Shemira (77% `Magic`)

**Crowd Control**

- Kafra (75% `Stun` `Move`)
- Lucy (75% `Stun`)
- Soren (73% `Stun` `Move`)

### Summary for Alsa

#### Stats Alsa benefits from

- Haste
- Max HP

#### Damage types dealt by Alsa

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Self

#### Debuffs provided by Alsa

- Movement speed debuff — Area — `medium`
- Energy drain (EX+5) — Single target — `low`
- Magic DEF debuff (EX+5) — Area — `low`

#### Crowd Control provided by Alsa

- Immune — Area — Once
- Move — Single target — `low`
- Stun — Single target — `high`

#### Alsa's Special Effects

#### Alsa Provides

- Enhanced form — Area

#### Alsa Requires

- Form or stance active — Enemies
- Passive with internal cooldown — Enemies

## Antandra

### Antandra's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Shield Assault (ultimate) — charge + area knockback
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Antandra benefits from

Look for units providing: `Max HP` `Energy`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]

### Units that can act as a replacement for Antandra

**Buffs on allies**

- Marcille (100% `Healing`)
- Solise (66% `Healing`)
- Hewynn (60% `Healing`)

**Damage**

- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)
- Hepler (100% `Physical`)

**Crowd Control**

- Lumont (57% `Stun` `Taunt`)
- Hepler (52% `Taunt` `Stun`)

### Summary for Antandra

#### Stats Antandra benefits from

- Max HP
- Energy

#### Damage types dealt by Antandra

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target

#### Buffs provided by Antandra

- Healing — Multiple targets — `high`

#### Crowd Control provided by Antandra

- Unaffected — Area — On skill
- Knock down — Area — `medium`
- Stun — Area — `medium`
- Taunt — Area — `high`

#### Antandra's Special Effects

#### Antandra Provides

- Stacking buff (Supreme+) — Single target

#### Antandra Requires

- Once per battle (Mythic+) — Allies

## Arden

### Arden's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Force of Nature (ultimate) — area nature damage burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Arden benefits from

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion**, **Lyca**, or **Hugin**.

- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]

### Units that can act as a replacement for Arden

**Damage**

- Berial (87% `Magic` `DoT`)
- Bryon (87% `Magic` `DoT`)
- Bonnie (78% `Magic` `DoT`)

**Crowd Control**

- Laios (88% `Pin`)
- Cecia (50% `Pin`)
- Korin (50% `Pin`)

### Summary for Arden

#### Stats Arden benefits from

- ATK
- Energy

#### Damage types dealt by Arden

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Multiple targets

#### Crowd Control provided by Arden

- Pin — Multiple targets — `high`

## Atalanta

### Atalanta's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Wild Sniper (ultimate) — dash + line stun shot
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Atalanta benefits from

Look for units providing: `Haste` `Physical DEF`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units that can act as a replacement for Atalanta

**Buffs on allies**

- Igor (100% `Healing`)
- Lucca (100% `Healing`)
- Talene (100% `Healing`)

**Damage**

- Antandra (100% `Physical`)
- Gerda (100% `Physical`)
- Hepler (100% `Physical`)

**Crowd Control**

- Soren (66% `Move` `Stun`)
- Cassadee (60% `Move` `Stun`)
- Kafra (56% `Stun` `Move`)

### Summary for Atalanta

#### Stats Atalanta benefits from

- Haste
- Physical DEF

#### Damage types dealt by Atalanta

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Atalanta

- Healing (Supreme+) — Single target — `low`

#### Debuffs provided by Atalanta

- Phys DEF debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Atalanta

- Move — Single target — `high`
- Pin — Single target — `medium`
- Stun — Single target — `medium`

#### Atalanta's Special Effects

#### Atalanta Provides

- Reposition enemies — Single target
- Stat steal (EX+10) — Single target

## Athalia

### Athalia's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Unbroken Retribution (ultimate) — post-death attacking lance
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: normal

### Units Athalia benefits from

Look for units providing: `Max HP` `Crit` `Execution`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Cecia**
  - Max HP buff (single target, high)
  - ATK SPD buff (single target, low) [signature fuel]

### Units that can act as a replacement for Athalia

**Buffs on allies**

- Nara (75% `Healing`)
- Berial (66% `Healing`)
- Rhys (66% `Healing`)

**Damage**

- Dionel (91% `True damage` `Physical`)
- Scarlita (85% `Physical` `True damage`)
- Perseus (82% `Physical` `True damage`)

**Crowd Control**

- Baelran (93% `Knock down`)
- Temesia (62% `Knock down`)
- Thador (60% `Knock down`)

### Summary for Athalia

#### Stats Athalia benefits from

- Max HP
- Crit
- Execution

#### Damage types dealt by Athalia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- True damage — All units, Single target — `medium`

#### Buffs provided by Athalia

- Healing — Single target — `medium` — conditional (frequent)

#### Debuffs provided by Athalia

- ATK debuff — All units — `medium`

#### Crowd Control provided by Athalia

- Unaffected — Area — On skill
- Knock down — All units — `low`

#### Athalia's Special Effects

#### Athalia Provides

- Invincibility — Area
- Transformation — Self

## Aurora

### Aurora's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Starlit Slumber (ultimate) — sleep all enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Aurora benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Aurora

- Berial
- Bryon
- Damian
- Florabelle
- Gala
- Hodgkin
- Phraesto
- Zanie

### Units that can act as a replacement for Aurora

**Damage**

- Carolina (100% `Magic`)
- Eironn (100% `Magic`)
- Fay (100% `Magic`)

### Summary for Aurora

#### Stats Aurora benefits from

- ATK
- Haste

#### Damage types dealt by Aurora

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Aurora

- Haste buff — Summons only — `high`
- Invincible — Single target — `high`
- Summon damage buff (Mythic+) — Summons only — `low`

#### Debuffs provided by Aurora

- Haste debuff — Multiple targets — `low`

#### Crowd Control provided by Aurora

- Unaffected — Self — On skill
- Sleep — Single target — `high`

#### Aurora's Special Effects

#### Aurora Provides

- Invincibility — Multiple targets
- Start-of-battle cast — Multiple targets
- Summoning — Single target

## Baelran

### Baelran's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Celestial Rise (ultimate) — HP-based shield + transform
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Baelran benefits from

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)

### Units that can act as a replacement for Baelran

**Buffs on allies**

- Harak (66% `Healing`)
- Atalanta (50% `Healing`)
- Igor (50% `Healing`)

**Damage**

- Korin (87% `Max HP-based damage` `Physical` `True damage`)
- Indris (86% `True damage` `Physical` `Max HP-based damage`)
- Nara (85% `Max HP-based damage` `True damage` `Physical`)

**Crowd Control**

- Athalia (93% `Knock down`)
- Temesia (60% `Knock down`)
- Thador (56% `Knock down`)

### Summary for Baelran

#### Stats Baelran benefits from

- ATK
- Haste
- Max HP

#### Damage types dealt by Baelran

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Arc, Area, Single target — `high`
- True damage — Area, Single target — `medium`

#### Buffs provided by Baelran

- Healing — Single target — `low`
- Healing over time — Single target — `low`

#### Debuffs provided by Baelran

- Max HP debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Baelran

- Unaffected — Self — Start of battle
- Knock down — Area — `medium`

#### Baelran's Special Effects

#### Baelran Provides

- Start-of-battle cast — Arc
- Enhanced form (Mythic+) — Area
- Dispel debuffs (EX+15) — Area

#### Baelran Requires

- Form or stance active — Enemies
- Boss encounter (Supreme+) — Enemies

## Berial

### Berial's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Scared Swamp (ultimate) — shadow dive + area frighten
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Berial benefits from

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Units that can act as a replacement for Berial

**Buffs on allies**

- Nara (88% `Healing`)
- Solise (75% `Healing`)
- Viperian (75% `Healing`)

**Damage**

- Bryon (100% `DoT` `Magic`)
- Lorsan (88% `DoT` `Magic`)
- Arden (87% `Magic` `DoT`)

### Summary for Berial

#### Damage types dealt by Berial

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area

#### Buffs provided by Berial

- Healing — Single target — `high`

#### Debuffs provided by Berial

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `medium`

#### Crowd Control provided by Berial

- Frighten — Area — `medium`

#### Berial's Special Effects

#### Berial Provides

- Invincibility — Single target
- Revive ally — Single target
- Summoning (Mythic+) — Single target

## Bonnie

### Bonnie's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Decay's Reach — battle-start aging debuff
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Bonnie benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Lucius**, or **Ravion**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
  - Enables Magic damage from allies via Magic damage + early battle + all enemies (all units)
- **Lily May**
  - Enables Debuff on target via Energy drain (all units)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Natsu**
  - Enables Debuff on target via Haste debuff (area)
  - Enables Magic damage from allies via Magic damage + wide area (area)
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Magic damage from allies via Magic damage + all enemies (all units)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Debuff on target via Haste debuff (area)

### Units that can act as a replacement for Bonnie

**Damage**

- Mirael (100% `Magic` `DoT`)
- Arden (78% `Magic` `DoT`)
- Aurora (72% `Magic`)

**Crowd Control**

- Lyca (100% `Stun`)
- Marilee (100% `Stun`)
- Zanie (100% `Stun`)

### Summary for Bonnie

#### Stats Bonnie benefits from

- ATK

#### Damage types dealt by Bonnie

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Bonnie

- ATK debuff — Single target — `medium`
- Haste debuff — Single target — `low`
- Damage taken debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Bonnie

- Stun — Single target — `low`

#### Bonnie's Special Effects

#### Bonnie Provides

- Invincibility — Area
- Transformation — Self
- Magic damage amplification (Supreme+) — Single target

#### Bonnie Requires

- Debuff on target — Enemies
- Debuff on target (Aging) — Enemies
- Form or stance active — Enemies
- Magic damage from allies — Allies

## Brutus

### Brutus's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Whirlwind Wrath (ultimate) — area spin damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Brutus benefits from

Look for units providing: `Life Drain`  
Common buffers are **Lyca**, **Twins**, or **Rowan**.

- **Zandrok**
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Kordan**
  - Lifedrain buff (multiple targets, high)
- **Dunlingr**
  - Lifedrain buff (all units, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - Lifedrain buff (single target, low)
  - ATK SPD buff (multiple targets, high) [signature fuel]

### Units that can act as a replacement for Brutus

**Buffs on allies**

- Kruger (75% `Life Drain`)
- Walker (66% `Life Drain`)
- Daimon (50% `Life Drain`)

**Damage**

- Cecia (97% `Max HP-based damage` `Physical` `DoT`)
- Gunnar (90% `Max HP-based damage` `DoT` `Physical`)
- Florabelle (88% `Max HP-based damage` `Physical`)

**Crowd Control**

- Hepler (54% `Taunt`)
- Lumont (50% `Taunt`)

### Summary for Brutus

#### Stats Brutus benefits from

- Life Drain

#### Damage types dealt by Brutus

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Arc, Single target — `high`

#### Buffs provided by Brutus

- Lifedrain buff — Single target — `medium`

#### Debuffs provided by Brutus

- DoT — Area — `medium`
- Phys DEF debuff — Area — `low`

#### Crowd Control provided by Brutus

- Unaffected — Self — On skill
- Taunt — Area — `high`

## Bryon

### Bryon's behavior

- Movement: stationary (summon moves)
- Signature skill: Falcon Raid (ultimate) — falcon area dive damage
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: slow

### Units Bryon benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Bryon

**Buffs on allies**

- Harak (66% `Healing`)
- Hodgkin (66% `Healing`)
- Tasi (66% `Healing`)

**Similar Skills**

- Niru (100% `battle-start-ult`)

**Damage**

- Berial (100% `DoT` `Magic`)
- Lorsan (88% `DoT` `Magic`)
- Arden (87% `Magic` `DoT`)

**Crowd Control**

- Damian (66% `Stun`)
- Ludovic (66% `Stun`)
- Nazrik (66% `Stun`)

### Summary for Bryon

#### Stats Bryon benefits from

- Haste

#### Damage types dealt by Bryon

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area

#### Buffs provided by Bryon

- Healing (EX+5) — Single target — `low` — conditional (rare)
- Healing over time (EX+5) — Single target — `medium`

#### Debuffs provided by Bryon

- Haste debuff — Area — `low`

#### Crowd Control provided by Bryon

- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

#### Bryon's Special Effects

#### Bryon Provides

- Energy steal — Single target
- Stacking buff — Single target
- Start-of-battle cast — Single target
- Summoning — Self
- Untargetable (EX+5) — Single target
- Counterattack (EX+10) — Single target

## Callan

### Callan's behavior

- Movement: moving (avg attack range 1.7 tiles)
- Signature skill: Restless Guardian (ultimate) — absorb ally damage shield
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Callan benefits from

Look for units providing: `Healing`  
Common buffers are **Mikola**, **Rowan**, or **Damian**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Callan

- Alna
- Daimon
- Eironn
- Gerda
- Saida
- Thoran
- Ulmus

### Units that can act as a replacement for Callan

**Buffs on allies**

- Saida (62% `Max HP` `Healing`)
- Lucy (60% `Max HP`)
- Hepler (55% `Max HP` `Healing`)

**Damage**

- Igor (62% `Physical`)
- Koko (62% `Physical`)
- Kulu (62% `Physical`)

**Crowd Control**

- Valka (60% `Knock down` `Stun`)
- Natsu (58% `Stun` `Knock down`)

### Summary for Callan

#### Stats Callan benefits from

- Healing

#### Damage types dealt by Callan

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Magic — Multiple targets

#### Buffs provided by Callan

- Shield — Multiple targets — `medium`
- Healing (Supreme+) — Single target — `low`

#### Crowd Control provided by Callan

- Unaffected — Self — Start of battle
- Knock down — All units — `low`
- Pin — Multiple targets — `low`
- Stun (Mythic+) — All units — `low`

#### Callan's Special Effects

#### Callan Provides

- Damage absorption (allies) — Multiple targets
- Stored damage release — Self

#### Callan Requires

- Stored resource threshold — Enemies

## Carolina

### Carolina's behavior

- Movement: mostly stationary (avg attack range 4.0 tiles)
- Signature skill: Frozen Grave (ultimate) — freeze + bury area
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Carolina benefits from

Look for units providing: `Crit`  
Common buffers are **Lyca**, **Twins**, or **Damian**.

- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Enables CC on enemies via Stun (area, high)
- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Indris**
  - Enables CC on enemies via Pin (area, high)
- **Kordan**
  - Enables CC on enemies via Pin (area, high)
- **Lumont**
  - Enables CC on enemies via Stun (area, high)

### Units benefitting from Carolina

- Nerion

### Units that can act as a replacement for Carolina

**Damage**

- Aurora (100% `Magic`)
- Eironn (100% `Magic`)
- Fay (100% `Magic`)

### Summary for Carolina

#### Stats Carolina benefits from

- Crit

#### Damage types dealt by Carolina

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- DoT — Self

#### Debuffs provided by Carolina

- Haste debuff — Area — `low`
- Magic DEF debuff (Mythic+) — Area — `low`

#### Crowd Control provided by Carolina

- Freeze — Area — `high`

#### Carolina's Special Effects

#### Carolina Provides

- Stacking buff — Area

#### Carolina Requires

- CC on enemies — Allies

## Cassadee

### Cassadee's behavior

- Movement: stationary (avg attack range 10.0 tiles)
- Signature skill: Running Tide (ultimate) — tidal wave knockback
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Cassadee benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units that can act as a replacement for Cassadee

**Damage**

- Contess (100% `Magic`)
- Damian (100% `Magic`)
- Evie (100% `Magic`)

**Crowd Control**

- Soren (66% `Move` `Stun`)
- Atalanta (60% `Move` `Stun`)
- Kafra (56% `Stun` `Move`)

### Summary for Cassadee

#### Stats Cassadee benefits from

- Haste

#### Damage types dealt by Cassadee

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Debuffs provided by Cassadee

- Magic DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Cassadee

- Move — All units — `low`
- Stun — Single target — `high`

#### Cassadee's Special Effects

#### Cassadee Provides

- Ally blessing — Single target

#### Cassadee Requires

- Ally blessing active (EX+5) — Allies

## Cecia

### Cecia's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Queen's Summons (ultimate) — summon AoE damage unit
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Cecia benefits from

Look for units providing: `ATK SPD / Haste` `DEF Penetration` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Lyca**, or **Rowan**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)

### Units that can act as a replacement for Cecia

**Damage**

- Brutus (97% `Max HP-based damage` `Physical` `DoT`)
- Florabelle (90% `Max HP-based damage` `Physical`)
- Hodgkin (90% `Max HP-based damage` `Physical`)

**Crowd Control**

- Korin (100% `Pin`)
- Velara (100% `Pin`)
- Gala (66% `Pin`)

### Summary for Cecia

#### Stats Cecia benefits from

- ATK SPD
- DEF Penetration
- Physical DEF
- Magic DEF

#### Damage types dealt by Cecia

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Single target
- Max HP-based damage — Arc — `high`

#### Buffs provided by Cecia

- ATK SPD buff — Single target — `low`
- DEF Penetration buff — Single target — `medium`
- Lifedrain buff — Area — `low`
- Max HP buff — Single target — `high`

#### Debuffs provided by Cecia

- Damage taken debuff (EX+10) — Single target — `medium`

#### Crowd Control provided by Cecia

- Pin — Single target — `high`

#### Cecia's Special Effects

#### Cecia Provides

- Summoning — Self
- Stat absorb (Mythic+) — Single target
- Permanent stat absorb (EX+5) — Single target

#### Cecia Requires

- Enemy not CC-immune (Mythic+) — Enemies

## Chippy

### Chippy's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Brothers-in-arms (ultimate) — summon support ally
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Chippy benefits from

- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Thador**
  - Energy recovery (lieutenant, start of battle) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Chippy

**Damage**

- Salazer (100% `Physical`)
- Silvina (100% `Physical`)
- Thoran (100% `Physical`)

### Summary for Chippy

#### Damage types dealt by Chippy

- Primary damage type (unit): **Physical**
- Physical — Single target

## Contess

### Contess's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Detention Pass (ultimate) — stealth start + punish
- Signature skill speed: fast
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Contess benefits from

Look for units providing: `Healing` `Energy`  
Common buffers are **Mikola**, **Rowan**, or **Ravion**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Contess

- Talene
- Smokey & Meerky

### Units that can act as a replacement for Contess

**Buffs on allies**

- Antandra (54% `Healing`)
- Marcille (54% `Healing`)
- Fay (50% `Healing` `ATK`)

**Damage**

- Cassadee (100% `Magic`)
- Damian (100% `Magic`)
- Evie (100% `Magic`)

**Crowd Control**

- Damian (50% `Stun`)
- Ludovic (50% `Stun`)
- Nazrik (50% `Stun`)

### Summary for Contess

#### Stats Contess benefits from

- Healing
- Energy

#### Damage types dealt by Contess

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs provided by Contess

- ATK buff — Single target — `high`
- Healing — Multiple targets — `high`
- Shield — Single target — `medium`

#### Debuffs provided by Contess

- Energy drain — Multiple targets — `low`
- Max HP debuff — Multiple targets — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Silence (Mythic+) — Single target — `medium`
- Stun (Supreme+) — Single target — `medium`

#### Contess's Special Effects

#### Contess Provides

- Start-of-battle cast — All units

## Cryonaia

### Cryonaia's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Frostveil Domain (ultimate) — area frost slow field
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Cryonaia benefits from

Look for units providing: `ATK` `Max HP`  
Common buffers are **Hugin**, **Twins**, or **Lyca**.

- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)

### Units that can act as a replacement for Cryonaia

**Damage**

- Tasi (100% `DoT` `Magic`)
- Lorsan (90% `Magic` `DoT`)
- Berial (80% `DoT` `Magic`)

### Summary for Cryonaia

#### Stats Cryonaia benefits from

- ATK
- Max HP

#### Damage types dealt by Cryonaia

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units

#### Debuffs provided by Cryonaia

- Damage taken debuff (EX+5) — Single target — `high`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional
- Freeze (EX+15) — Self — `low`

#### Cryonaia's Special Effects

#### Cryonaia Provides

- Enemy isolation (domain) — All units

#### Cryonaia Requires

- Boss encounter — Enemies

## Cyran

### Cyran's behavior

- Movement: mostly stationary (avg attack range 6.0 tiles)
- Signature skill: Gravitic Requiem (ultimate) — pull all + execute low HP
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Cyran benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Crit`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Cyran

**Similar Skills**

- Eironn (100% `enemy-grouping`)
- Mehira (100% `enemy-grouping`)

**Damage**

- Frieren (85% `True damage` `Magic`)
- Athalia (80% `True damage`)
- Dionel (77% `True damage`)

### Summary for Cyran

#### Stats Cyran benefits from

- ATK
- ATK SPD
- Crit

#### Damage types dealt by Cyran

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- True damage — All units — `medium`

#### Debuffs provided by Cyran

- ATK debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Cyran

- Steadfast — Area — Conditional
- Unaffected — Self — Start of battle
- Pin — Self — `high`
- Silence (EX+10) — Single target — `low`

#### Cyran's Special Effects

#### Cyran Provides

- Artifact mimic (Mythic+) — All units
- Enemy artifact block (EX+10) — Single target

## Daimon

### Daimon's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Buddy Barrier — shield + ATK buff ally behind
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Daimon benefits from

Look for units providing: `Max HP`  
Common buffers are **Lucius** or **Hugin**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Gala**
  - Max HP via Shield (single target, high)

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Brutus (50% `Life Drain`)
- Korin (50% `Max HP`)
- Scarlita (50% `Max HP`)

**Damage**

- Satrana (100% `Max HP-based damage` `DoT` `Magic`)
- Shemira (90% `Max HP-based damage` `Magic`)
- Natsu (88% `Max HP-based damage` `Magic` `DoT`)

**Crowd Control**

- Silvina (72% `Frighten`)

### Summary for Daimon

#### Stats Daimon benefits from

- Max HP

#### Damage types dealt by Daimon

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area
- Max HP-based damage — Area, Self, Single target — `high`

#### Buffs provided by Daimon

- Lifedrain buff — Single target — `medium`
- Shield — Multiple targets — `low`

#### Crowd Control provided by Daimon

- Frighten (Mythic+) — Area — `low`

## Damian

### Damian's behavior

- Movement: stationary (off battlefield)
- Signature skill: Inventor's Will — chariot haste aura for allies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Damian benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Hugin**, **Twins**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]

### Units benefitting from Damian

**39** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Lumont
- Sylphira
- Vala
- Alsa
- Atalanta
- Aurora
- Cassadee
- Frieren
- Hepler
- Koko

### Units that can act as a replacement for Damian

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Evie (100% `Magic`)

**Crowd Control**

- Ludovic (100% `Stun`)
- Nazrik (100% `Stun`)
- Nerion (100% `Stun`)

### Summary for Damian

#### Stats Damian benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Damian

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Damian

- Healing — Single target — `medium`
- Haste buff (Mythic+) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control provided by Damian

- Stun — Single target — `medium`

#### Damian's Special Effects

#### Damian Provides

- Summoning — All units

## Dionel

### Dionel's behavior

- Movement: moving (avg attack range 0.0 tiles)
- Signature skill: Dawn Light (ultimate) — airborne multi-hit AoE
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Dionel benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Execution`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Hepler**
  - ATK SPD via Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)

### Units that can act as a replacement for Dionel

**Damage**

- Athalia (91% `True damage` `Physical`)
- Scarlita (80% `Physical` `True damage`)
- Frieren (80% `True damage`)

### Summary for Dionel

#### Stats Dionel benefits from

- ATK SPD
- Max HP
- Execution

#### Damage types dealt by Dionel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- True damage — All units, Single target — `high`

#### Buffs provided by Dionel

- DEF Penetration buff — Single target — `high`

#### Debuffs provided by Dionel

- Vitality debuff (EX+10) — Single target — `low`

#### Dionel's Special Effects

#### Dionel Provides

- Stacking buff — Single target
- Untargetable — Area
- Execution scaling (Supreme+) — Self

## Dunlingr

### Dunlingr's behavior

- Movement: stationary (avg attack range 6.4 tiles)
- Signature skill: Echo of Silence (ultimate) — forbid heals or ultimates
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Dunlingr benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)

### Units that can act as a replacement for Dunlingr

**Damage**

- Niru (79% `Magic` `HP loss`)
- Walker (67% `HP loss`)
- Zorya (57% `HP loss` `Magic`)

### Summary for Dunlingr

#### Stats Dunlingr benefits from

- ATK SPD
- Haste
- Max HP
- Healing

#### Damage types dealt by Dunlingr

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- HP loss — Area — `medium`
- Max HP-based damage — Self

#### Buffs provided by Dunlingr

- Healing — Single target — `low`
- ATK buff (EX+5) — Single target — `low`
- Haste buff (EX+15) — Single target — `low`
- ATK SPD buff (Supreme+) — All units — `low`
- Lifedrain buff (Supreme+) — All units — `low`

#### Debuffs provided by Dunlingr

- ATK debuff — Area — `low`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence — All units — `low`

#### Dunlingr's Special Effects

#### Dunlingr Provides

- Heal lock (Curelock) — All units
- Summoning — Self
- Ultimate lock (Spellbind) — All units

## Eironn

### Eironn's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Howling Hurricane — free area pull at start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Eironn benefits from

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Lucius**, **Hugin**, or **Rowan**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Lumont**
  - DEF buff (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Units that can act as a replacement for Eironn

**Similar Skills**

- Cyran (100% `enemy-grouping`)
- Mehira (100% `enemy-grouping`)

**Damage**

- Aurora (100% `Magic`)
- Carolina (100% `Magic`)
- Fay (100% `Magic`)

**Crowd Control**

- Evie (61% `Move` `Pin`)
- Indris (56% `Move` `Pin`)

### Summary for Eironn

#### Stats Eironn benefits from

- Max HP
- Physical DEF

#### Damage types dealt by Eironn

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target

#### Buffs provided by Eironn

- Dodge chance buff — Single target — `high`

#### Debuffs provided by Eironn

- Haste debuff — Arc — `medium`
- Magic DEF debuff — Arc — `high`

#### Crowd Control provided by Eironn

- Move — Area — `medium`
- Pin — Single target — `high`

## Twins

### Twins's behavior

- Movement: moving / stationary (two units)
- Signature skill: Starlight Waltz (ultimate) — high haste buff all allies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Twins benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Hugin**, **Mikola**, or **Damian**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units benefitting from Twins

**90** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Valka
- Lumont
- Mehira
- Zorya
- Alsa
- Hepler
- Lenya
- Soren

### Units that can act as a replacement for Twins

**Damage**

- Aurora (100% `Magic`)
- Carolina (100% `Magic`)
- Eironn (100% `Magic`)

**Crowd Control**

- Lucius (66% `Move`)
- Rhys (59% `Move`)
- Ulmus (57% `Move`)

### Summary for Twins

#### Stats Twins benefits from

- Haste
- Energy

#### Damage types dealt by Twins

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Twins

- Haste buff — All units — `high`
- Healing — Single target — `medium`
- Max HP buff — Multiple targets — `high`
- Shield — Single target — `medium`
- Vitality buff (Mythic+) — Multiple targets — `low`

#### Crowd Control provided by Twins

- Unaffected — Area — On skill
- Move — Area — `low`

#### Twins's Special Effects

#### Twins Provides

- Ally positioning link — Single target
- Shared HP and Energy — All units

#### Twins Requires

- Ally on positioning link (Supreme+) — —

## Evie

### Evie's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Intel Chase (ultimate) — stealth + trigger burst
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Evie benefits from

Look for units providing: `Healing` `Energy`  
Common buffers are **Mikola**, **Rowan**, or **Ravion**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Evie

- Perseus
- Silven
- Bonnie
- Shadewing
- Aliceth
- Isabella
- Kordan
- Smokey & Meerky
- Talene
- Himmel

### Units that can act as a replacement for Evie

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

**Crowd Control**

- Eironn (61% `Move` `Pin`)
- Indris (54% `Move` `Pin` `Silence`)

### Summary for Evie

#### Stats Evie benefits from

- Healing
- Energy

#### Damage types dealt by Evie

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Evie

- ATK buff — Multiple targets — `high`
- Healing — Multiple targets — `high`
- Invincible — Area — `high`

#### Debuffs provided by Evie

- DoT — All units — `medium`

#### Crowd Control provided by Evie

- Move — All units — `low`
- Pin — All units — `low`
- Silence — All units — `low`

#### Evie's Special Effects

#### Evie Provides

- Invincibility — All units
- Start-of-battle cast — All units

#### Evie Requires

- Passive with internal cooldown — Allies

## Faramor

### Faramor's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Sanctified Circle (ultimate) — no-heal zone + true DoT
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Faramor benefits from

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]

### Units that can act as a replacement for Faramor

**Damage**

- Vala (79% `True damage` `Physical` `HP loss`)
- Aliceth (54% `Physical` `HP loss`)
- Athalia (51% `True damage` `Physical`)

**Crowd Control**

- Koko (100% `Stun`)
- Lorsan (88% `Stun`)
- Lucy (84% `Stun`)

### Summary for Faramor

#### Stats Faramor benefits from

- ATK
- Haste
- Max HP

#### Damage types dealt by Faramor

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`
- True damage — Multiple targets — `medium`

#### Debuffs provided by Faramor

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `medium`

#### Faramor's Special Effects

#### Faramor Provides

- Revive ally (Supreme+) — Single target

#### Faramor Requires

- Once per battle (EX+10) — Enemies

## Fay

### Fay's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Vibrant Dance (ultimate) — arc heal + ATK buff
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Fay benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Fay

- Granny Dahnie

### Units that can act as a replacement for Fay

**Buffs on allies**

- Contess (50% `Healing` `ATK`)

**Damage**

- Aurora (100% `Magic`)
- Carolina (100% `Magic`)
- Eironn (100% `Magic`)

### Summary for Fay

#### Stats Fay benefits from

- ATK SPD

#### Damage types dealt by Fay

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Multiple targets, Single target

#### Buffs provided by Fay

- ATK SPD buff — Multiple targets — `low`
- ATK buff — Multiple targets — `low`
- DEF buff — Multiple targets — `low`
- Healing — Arc — `high` — conditional (frequent)
- Vitality buff (EX+5) — Single target — `low`

#### Debuffs provided by Fay

- Magic DEF debuff — Multiple targets — `low`
- Phys DEF debuff — Multiple targets — `low`

## Florabelle

### Florabelle's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Pounding Blow (ultimate) — summon stomper ally
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Florabelle benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Hugin**, **Twins**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]

### Units benefitting from Florabelle

- Mehira
- Dunlingr
- Laios
- Berial
- Bryon
- Damian
- Gala
- Phraesto
- Zanie

### Units that can act as a replacement for Florabelle

**Damage**

- Hodgkin (100% `Max HP-based damage` `Physical`)
- Cecia (90% `Max HP-based damage` `Physical`)
- Himmel (89% `Physical` `Max HP-based damage`)

### Summary for Florabelle

#### Stats Florabelle benefits from

- ATK
- Haste

#### Damage types dealt by Florabelle

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs provided by Florabelle

- Lifedrain buff — Summons only — `high` — conditional (frequent)
- Shield (Mythic+) — Summons only — `medium`
- Haste buff (EX+10) — Summons only — `medium` — conditional (frequent)
- Summon damage buff (Supreme+) — Summons only — `medium`

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Self — Form

#### Florabelle's Special Effects

#### Florabelle Provides

- Summoning — Self

## Frieren

### Frieren's behavior

- Movement: stationary (avg attack range 7.0 tiles)
- Signature skill: Zoltraak (ultimate) — high-damage magic beam
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Frieren benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units benefitting from Frieren

- Bonnie

### Units that can act as a replacement for Frieren

**Similar Skills**

- Shemira (100% `high-damage-ult`)

**Damage**

- Cyran (85% `True damage` `Magic`)
- Dionel (80% `True damage`)
- Athalia (75% `True damage`)

**Crowd Control**

- Natsu (52% `Knock down` `Stun`)
- Thador (50% `Knock down`)

### Summary for Frieren

#### Stats Frieren benefits from

- ATK
- Haste

#### Damage types dealt by Frieren

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- DoT — All units, Area, Single target
- True damage — All units, Single target — `high`

#### Debuffs provided by Frieren

- DoT — Area — `high`
- Vitality debuff — Single target — `low`

#### Crowd Control provided by Frieren

- Stun — Single target — `low`
- Knock down (Supreme+) — Single target — `medium`

## Gala

### Gala's behavior

- Movement: stationary (avg attack range 10.0 tiles)
- Signature skill: Time Recast — summon shadow copy of ally
- Signature skill speed: fast
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Gala benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Hugin**, **Twins**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]

### Units benefitting from Gala

- Faramor
- Gunnar
- Harak
- Sonja
- Velara
- Zandrok
- Athalia
- Silvina

### Units that can act as a replacement for Gala

**Buffs on allies**

- Lucy (50% `Max HP`)
- Mehira (50% `Haste`)
- Vala (50% `Haste`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

**Crowd Control**

- Cecia (66% `Pin`)
- Korin (66% `Pin`)
- Velara (66% `Pin`)

### Summary for Gala

#### Stats Gala benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Gala

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Gala

- Haste buff — Single target — `high`
- Shield — Single target — `high`

#### Crowd Control provided by Gala

- Steadfast (Supreme+) — Self — On skill
- Pin — Single target — `medium`

#### Gala's Special Effects

#### Gala Provides

- Summoning (Mythic+) — Single target
- Artifact amplification (EX+10) — Single target
- Artifact echo (EX+10) — Single target

#### Gala Requires

- Boss encounter — Enemies
- Artifact buffs active (Supreme+) — Self

## Gerda

### Gerda's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Spring Therapy — battle-start heal zone
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Gerda benefits from

Look for units providing: `Max HP`  
Common buffers are **Lucius** or **Hugin**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Gala**
  - Max HP via Shield (single target, high)

### Units that can act as a replacement for Gerda

**Buffs on allies**

- Ludovic (65% `Healing`)
- Smokey & Meerky (60% `Healing`)
- Granny Dahnie (53% `Healing`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Hepler (100% `Physical`)

### Summary for Gerda

#### Stats Gerda benefits from

- Max HP

#### Damage types dealt by Gerda

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Gerda

- Healing — Multiple targets — `medium`
- Healing over time — Area — `medium`

#### Crowd Control provided by Gerda

- Unaffected — Self — Start of battle
- Interrupt — Single target — `medium`
- Pin — Multiple targets — `low`
- Stun — Single target — `high`

## Granny Dahnie

### Granny Dahnie's behavior

- Movement: moving (avg attack range 2.0 tiles)
- Signature skill: Threshold of Jade (ultimate) — root zone + HP drain
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Granny Dahnie benefits from

Look for units providing: `Healing` `Energy` `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Mikola**, or **Lyca**.

- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units that can act as a replacement for Granny Dahnie

**Buffs on allies**

- Harak (60% `Healing`)
- Hodgkin (60% `Healing`)
- Ludovic (60% `Healing`)

**Damage**

- Lumont (100% `Physical` `Max HP-based damage`)
- Soren (92% `Physical`)
- Gwyneth (92% `Physical` `Max HP-based damage`)

### Summary for Granny Dahnie

#### Stats Granny Dahnie benefits from

- Healing
- Energy
- Physical DEF
- Magic DEF

#### Damage types dealt by Granny Dahnie

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Granny Dahnie

- Healing — Single target — `medium`
- Healing over time (Mythic+) — Single target — `high`

#### Debuffs provided by Granny Dahnie

- Haste debuff — Single target — `low`
- ATK debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — On skill
- Pin — Area — `low`
- Taunt — Single target — `high`

## Gunnar

### Gunnar's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Annihilation Directive (ultimate) — long-range area bombing
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Gunnar benefits from

Look for units providing: `ATK SPD / Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Hepler**
  - ATK SPD via Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)

### Units that can act as a replacement for Gunnar

**Buffs on allies**

- Pandora (54% `Healing` `Invincible`)

**Damage**

- Brutus (90% `Max HP-based damage` `DoT` `Physical`)
- Cecia (88% `Max HP-based damage` `Physical` `DoT`)
- Daimon (83% `Max HP-based damage` `DoT`)

**Crowd Control**

- Lenya (90% `Stun`)
- Vala (90% `Stun`)
- Walker (90% `Stun`)

### Summary for Gunnar

#### Stats Gunnar benefits from

- ATK SPD
- Max HP

#### Damage types dealt by Gunnar

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- DoT — Area
- Max HP-based damage — All units — `high`

#### Buffs provided by Gunnar

- ATK SPD buff — Single target — `low`
- Ranged DEF buff (Legendary+) — Single target — `low`
- Vitality buff (Legendary+) — Single target — `low`
- Healing (Mythic+) — Single target — `high`
- Invincible (EX+15) — Single target — `high`

#### Crowd Control provided by Gunnar

- Stun — All units — `low`

#### Gunnar's Special Effects

#### Gunnar Provides

- Invincibility (EX+15) — Single target

## Gwyneth

### Gwyneth's behavior

- Movement: stationary (avg attack range 8.0 tiles)
- Signature skill: Hailing Arrows (ultimate) — area arrow rain
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Gwyneth benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Gwyneth

**Damage**

- Granny Dahnie (92% `Physical` `Max HP-based damage`)
- Lumont (92% `Physical` `Max HP-based damage`)
- Soren (86% `Physical`)

### Summary for Gwyneth

#### Stats Gwyneth benefits from

- ATK SPD

#### Damage types dealt by Gwyneth

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- DoT — Single target
- Max HP-based damage — Single target — `low`

#### Debuffs provided by Gwyneth

- DoT — Single target — `high`

#### Crowd Control provided by Gwyneth

- Pin — Area — `medium`
- Silence — Area — `low`
- Stun — Area — `low`

## Hammie

### Hammie's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Pretty Fireball (ultimate) — AoE magic fireball
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Hammie benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Hugin**, or **Ravion**.

- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]

### Units that can act as a replacement for Hammie

**Buffs on allies**

- Berial (60% `Healing`)
- Nara (53% `Healing`)
- Solise (50% `Healing`)

**Damage**

- Rowan (100% `Magic`)
- Odie (50% `Magic`)

### Summary for Hammie

#### Stats Hammie benefits from

- ATK

#### Damage types dealt by Hammie

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Hammie

- ATK buff — Multiple targets — `low`
- Healing — Single target — `high`

## Harak

### Harak's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Flesh Feast — instantly defeat weakest unit
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Harak benefits from

Look for units providing: `Haste` `Max HP` `Crit` `Energy` `Life Drain`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, medium, conditional (frequent))
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Kordan**
  - Lifedrain buff (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, low)

### Units that can act as a replacement for Harak

**Buffs on allies**

- Baelran (66% `Healing`)
- Bryon (66% `Healing`)
- Granny Dahnie (60% `Healing`)

**Damage**

- Seth (85% `Physical`)
- Kordan (82% `Physical` `HP loss`)
- Ravion (82% `Physical` `HP loss`)

### Summary for Harak

#### Stats Harak benefits from

- Haste
- Max HP
- Crit
- Energy
- Life Drain

#### Damage types dealt by Harak

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`

#### Buffs provided by Harak

- Healing over time — Single target — `medium` — conditional (frequent)
- Healing (EX+15) — Single target — `low`

#### Debuffs provided by Harak

- Execution debuff — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — Start of battle

#### Harak's Special Effects

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Single target

#### Harak Requires

- Boss encounter — Allies

## Hepler

### Hepler's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Form Shift (ultimate) — toggle attack/support form
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Hepler benefits from

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Hepler

- Shadewing
- Alna
- Daimon
- Gerda
- Saida
- Thoran
- Ulmus

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Callan (55% `Max HP` `Healing`)
- Saida (54% `Max HP` `Healing`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Brutus (54% `Taunt`)
- Lumont (53% `Taunt` `Stun`)
- Antandra (52% `Taunt` `Stun`)

### Summary for Hepler

#### Stats Hepler benefits from

- ATK
- Haste
- Max HP

#### Damage types dealt by Hepler

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Hepler

- Haste buff — Single target — `low`
- Healing — Multiple targets — `medium`
- Shield — Multiple targets — `medium`

#### Debuffs provided by Hepler

- Haste debuff — Area — `high`

#### Crowd Control provided by Hepler

- Stun — Area — `low`
- Taunt — Area — `high`

#### Hepler's Special Effects

#### Hepler Provides

- Invincibility (Mythic+) — Area

#### Hepler Requires

- Form or stance active (Legendary+) — Enemies

## Hewynn

### Hewynn's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Rain Prayer (ultimate) — AoE team healing
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Hewynn benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Hugin**, or **Ravion**.

- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]

### Units benefitting from Hewynn

**12** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Callan
- Contess
- Evie
- Igor
- Isabella
- Lucius
- Ludovic
- Phraesto
- Smokey & Meerky
- Talene

### Units that can act as a replacement for Hewynn

**Buffs on allies**

- Lorsan (71% `Healing`)
- Isabella (66% `Healing`)
- Antandra (60% `Healing`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

### Summary for Hewynn

#### Stats Hewynn benefits from

- ATK

#### Damage types dealt by Hewynn

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Hewynn

- Healing — All units — `high`

#### Crowd Control provided by Hewynn

- Unaffected (Mythic+) — Self — On skill

#### Hewynn's Special Effects

#### Hewynn Requires

- Passive with internal cooldown — Allies

## Himmel

### Himmel's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Hero Party — buff needing Mage+Tank+Support
- Signature skill speed: fast
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Himmel benefits from

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Party composition via Support (party slot)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - Enables Party composition via Mage (party slot)
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)
  - Enables Party composition via Support (party slot)
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)
  - Enables Party composition via Tank (party slot)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
  - Enables Party composition via Tank (party slot)

### Units benefitting from Himmel

- Baelran

### Units that can act as a replacement for Himmel

**Damage**

- Valka (93% `Physical` `Max HP-based damage`)
- Florabelle (89% `Physical` `Max HP-based damage`)
- Hodgkin (89% `Physical` `Max HP-based damage`)

### Summary for Himmel

#### Stats Himmel benefits from

- ATK
- Haste
- Max HP

#### Damage types dealt by Himmel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets, Single target
- Max HP-based damage — All units — `low`

#### Buffs provided by Himmel

- Shield — Single target — `low`
- ATK buff (Mythic+) — Multiple targets — `low`
- Max HP buff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Himmel

- Unaffected — Multiple targets — On skill

#### Himmel's Special Effects

#### Himmel Requires

- Party composition — Allies
- Boss encounter (Supreme+) — —

## Hodgkin

### Hodgkin's behavior

- Movement: moving (avg attack range 3.0 tiles)
- Signature skill: Cannon Fire (ultimate) — AoE cannon salvo
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Hodgkin benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Ravion**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Units that can act as a replacement for Hodgkin

**Buffs on allies**

- Tasi (100% `Healing`)
- Bryon (66% `Healing`)
- Granny Dahnie (60% `Healing`)

**Damage**

- Florabelle (100% `Max HP-based damage` `Physical`)
- Cecia (90% `Max HP-based damage` `Physical`)
- Himmel (89% `Physical` `Max HP-based damage`)

### Summary for Hodgkin

#### Stats Hodgkin benefits from

- ATK

#### Damage types dealt by Hodgkin

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- Max HP-based damage — Area — `medium`

#### Buffs provided by Hodgkin

- Healing over time — Single target — `high`

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Area — `low`
- Vitality debuff (EX+5) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `low`

#### Hodgkin's Special Effects

#### Hodgkin Provides

- Summoning (Mythic+) — Area
- Stacking buff (Supreme+) — Single target

## Hugin

### Hugin's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Unstoppable! (ultimate) — charge + shield assault
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Hugin benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Damian**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, low) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, low) [signature fuel]

### Units benefitting from Hugin

**86** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Tasi
- Valka
- Alsa
- Frieren
- Hepler
- Lenya
- Lumont
- Mehira

### Units that can act as a replacement for Hugin

**Damage**

- Rhys (100% `Physical`)
- Sinbad (100% `Physical`)
- Antandra (75% `Physical`)

### Summary for Hugin

#### Stats Hugin benefits from

- Haste
- Energy

#### Damage types dealt by Hugin

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target

#### Buffs provided by Hugin

- ATK buff — Multiple targets — `high`
- Haste buff — Multiple targets — `high`
- Shield (Mythic+) — Multiple targets — `high`

## Igor

### Igor's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Funereal Ring (ultimate) — tombstone zone damage
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Igor benefits from

Look for units providing: `Healing` `Life Drain`  
Common buffers are **Mikola**, **Rowan**, or **Damian**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
- **Kafra**
  - Healing over time (area, high)
- **Koko**
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)

### Units that can act as a replacement for Igor

**Buffs on allies**

- Atalanta (100% `Healing`)
- Lucca (100% `Healing`)
- Talene (100% `Healing`)

**Damage**

- Koko (100% `Physical`)
- Kulu (100% `Physical`)
- Lyca (100% `Physical`)

### Summary for Igor

#### Stats Igor benefits from

- Healing
- Life Drain

#### Damage types dealt by Igor

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Igor

- Healing — Single target — `low`

#### Igor's Special Effects

#### Igor Provides

- Untargetable — Area

## Indris

### Indris's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Spellbane Shot (ultimate) — silence + multi-debuff shot
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Indris benefits from

Look for units providing: `ATK` `ATK SPD / Haste`  
Common buffers are **Lyca**, **Ravion**, or **Twins**.

- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
  - Enables Multiple debuffs on target via 5 debuff types
  - Enables Debuff on target via ATK debuff (all units)
- **Sinbad**
  - Enables Multiple debuffs on target via 6 debuff types
  - Enables Debuff on target via ATK debuff (multiple targets)
- **Natsu**
  - Enables Multiple debuffs on target via 3 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Alna**
  - ATK buff (single target, medium)
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Haste debuff (area)
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
  - Enables Multiple debuffs on target via 2 debuff types
  - Enables Debuff on target via Energy drain (all units)

### Units benefitting from Indris

- Nerion
- Carolina

### Units that can act as a replacement for Indris

**Damage**

- Baelran (86% `True damage` `Physical` `Max HP-based damage`)
- Temesia (83% `Physical` `Max HP-based damage` `True damage`)
- Korin (82% `Physical` `Max HP-based damage` `True damage`)

**Crowd Control**

- Eironn (56% `Move` `Pin`)
- Evie (54% `Move` `Pin` `Silence`)

### Summary for Indris

#### Stats Indris benefits from

- ATK
- ATK SPD

#### Damage types dealt by Indris

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Multiple targets — `high`

#### Debuffs provided by Indris

- Damage taken debuff — Single target — `medium`
- Magic DEF debuff — Single target — `low`
- Phys DEF debuff (EX+10) — Single target — `low`

#### Crowd Control provided by Indris

- Move — Area — `high`
- Pin — Area — `high`
- Silence — Single target — `low`

#### Indris's Special Effects

#### Indris Requires

- Debuff on target — Enemies
- Multiple debuffs on target — Enemies
- Passive with internal cooldown — Enemies

## Isabella

### Isabella's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Grimoire Pact (ultimate) — permanent stat buff to companion
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Isabella benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Twins**, or **Hugin**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)

### Units benefitting from Isabella

- Dunlingr
- Callan
- Contess
- Evie
- Igor
- Phraesto

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Hewynn (66% `Healing`)
- Antandra (60% `Healing`)
- Marcille (60% `Healing`)

**Damage**

- Aurora (100% `Magic`)
- Carolina (100% `Magic`)
- Eironn (100% `Magic`)

### Summary for Isabella

#### Stats Isabella benefits from

- ATK
- ATK SPD
- Haste
- Healing
- Energy

#### Damage types dealt by Isabella

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Isabella

- Haste buff — Multiple targets — `low` — conditional (frequent)
- Healing — Area — `high`

#### Debuffs provided by Isabella

- ATK debuff — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected — Single target — Once

#### Isabella's Special Effects

#### Isabella Requires

- Once per battle — Allies

## Kafra

### Kafra's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Gale Thrust (ultimate) — mark + high single-target hit
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Kafra benefits from

Look for units providing: `ATK` `Max HP`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)

### Units benefitting from Kafra

- Callan
- Contess
- Evie
- Igor

### Units that can act as a replacement for Kafra

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Alsa (75% `Stun` `Move`)
- Lenya (66% `Stun`)
- Vala (66% `Stun`)

### Summary for Kafra

#### Stats Kafra benefits from

- ATK
- Max HP

#### Damage types dealt by Kafra

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Kafra

- Healing over time — Area — `high`

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `medium`
- Phys DEF debuff — Area — `low`
- ATK debuff (Mythic+) — Single target — `medium`
- Haste debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — Conditional
- Move — Single target — `low`
- Stun — Single target — `high`

#### Kafra's Special Effects

#### Kafra Provides

- Marked target (focus fire) — Single target

## Koko

### Koko's behavior

- Movement: mostly stationary (avg attack range 4.0 tiles)
- Signature skill: Full Energy (ultimate) — DMG reduction + true damage return
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Koko benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units benefitting from Koko

- Perseus
- Silven
- Valka
- Talene
- Tilaya
- Igor
- Saida

### Units that can act as a replacement for Koko

**Damage**

- Igor (100% `Physical`)
- Kulu (100% `Physical`)
- Lyca (100% `Physical`)

**Crowd Control**

- Faramor (100% `Stun`)
- Lorsan (88% `Stun`)
- Lucy (84% `Stun`)

### Summary for Koko

#### Stats Koko benefits from

- Haste
- Energy

#### Damage types dealt by Koko

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Koko

- Damage taken reduction — All units — `high`
- Healing — Multiple targets — `high`
- Healing over time — Single target — `high`
- Lifedrain buff — Multiple targets — `low`
- Shield (Mythic+) — All units — `low`
- Vitality buff (Supreme+) — Single target — `low`

#### Debuffs provided by Koko

- Damage taken debuff — Area — `high`

#### Crowd Control provided by Koko

- Stun — Area — `medium`

## Kordan

### Kordan's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Dominance Ring (ultimate) — immobilize + zone damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Kordan benefits from

Look for units providing: `ATK` `Max HP` `Healing` `DEF Penetration` `Life Drain`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)
  - Healing (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)

### Units benefitting from Kordan

- Nerion
- Carolina

### Units that can act as a replacement for Kordan

**Damage**

- Ravion (100% `Physical` `HP loss`)
- Aliceth (89% `Physical` `HP loss`)
- Harak (82% `Physical` `HP loss`)

### Summary for Kordan

#### Stats Kordan benefits from

- ATK
- Max HP
- Healing
- DEF Penetration
- Life Drain

#### Damage types dealt by Kordan

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- HP loss — Single target — `low`

#### Buffs provided by Kordan

- Lifedrain buff — Multiple targets — `high`
- DEF Penetration buff (Supreme+) — Multiple targets — `low`

#### Crowd Control provided by Kordan

- Knock down — Single target — `high`
- Move — Area — `low`
- Pin — Area — `high`

## Korin

### Korin's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Demonseal Spear (ultimate) — pierce-through spear strike
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Korin benefits from

Look for units providing: `ATK SPD / Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Dunlingr**
  - ATK SPD buff (all units, low) [signature fuel]
  - Haste buff (single target, low) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units that can act as a replacement for Korin

**Buffs on allies**

- Scarlita (100% `Max HP`)
- Lucy (66% `Max HP`)
- Daimon (50% `Max HP`)

**Damage**

- Nara (90% `Max HP-based damage` `True damage` `Physical`)
- Baelran (87% `Max HP-based damage` `Physical` `True damage`)
- Temesia (84% `Physical` `Max HP-based damage` `True damage`)

**Crowd Control**

- Cecia (100% `Pin`)
- Velara (100% `Pin`)
- Gala (66% `Pin`)

### Summary for Korin

#### Stats Korin benefits from

- ATK SPD
- Haste
- Max HP

#### Damage types dealt by Korin

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area, Single target — `medium`
- True damage — Single target — `medium`

#### Buffs provided by Korin

- Shield — Single target — `medium`

#### Crowd Control provided by Korin

- Pin — Single target — `medium`

## Kruger

### Kruger's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Devastating Axe (ultimate) — stack Phys DEF debuff
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Kruger benefits from

Look for units providing: `Max HP` `Physical DEF`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Lumont**
  - DEF buff (multiple targets, medium)

### Units that can act as a replacement for Kruger

**Buffs on allies**

- Walker (88% `Life Drain`)
- Brutus (75% `Life Drain`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

### Summary for Kruger

#### Stats Kruger benefits from

- Max HP
- Physical DEF

#### Damage types dealt by Kruger

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Kruger

- Lifedrain buff (Mythic+) — Area — `low`

#### Debuffs provided by Kruger

- Damage taken debuff — Area — `medium`
- Phys DEF debuff — Single target — `low`
- Vulnerable debuff — Area — `medium`

#### Kruger's Special Effects

#### Kruger Provides

- Stacking buff — Single target

#### Kruger Requires

- Vulnerable enemy (EX+10) — Enemies

## Kulu

### Kulu's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Demolition Zone — battle-start movement-blocking wall
- Signature skill speed: fast
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Kulu benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `DEF Penetration`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, medium)
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]

### Units that can act as a replacement for Kulu

**Buffs on allies**

- Lily May (100% `DEF Penetration`)
- Silven (100% `DEF Penetration`)
- Pang (50% `DEF Penetration`)

**Similar Skills**

- Alsa (100% `battlefield-modification`)

**Damage**

- Igor (100% `Physical`)
- Koko (100% `Physical`)
- Lyca (100% `Physical`)

**Crowd Control**

- Twins (56% `Move`)

### Summary for Kulu

#### Stats Kulu benefits from

- ATK
- ATK SPD
- DEF Penetration

#### Damage types dealt by Kulu

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Kulu

- DEF Penetration buff (EX+15) — Single target — `low`

#### Debuffs provided by Kulu

- Movement speed debuff — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected — Area — On ultimate
- Move — Single target — `low`

#### Kulu's Special Effects

#### Kulu Provides

- Invincibility — Single target
- Enhanced form (EX+15) — Single target

## Laios

### Laios's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Dungeon Gourmet — cook ingredients for random ally buffs
- Signature skill speed: slow
- Ultimate speed: fast
- Non-ultimate speed: slow

### Units Laios benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)
  - Healing (multiple targets, high)
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
  - Healing (single target, low)

### Units that can act as a replacement for Laios

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Arden (88% `Pin`)
- Cecia (56% `Pin`)
- Korin (56% `Pin`)

### Summary for Laios

#### Stats Laios benefits from

- ATK
- ATK SPD
- Haste
- Max HP
- Healing
- Energy

#### Damage types dealt by Laios

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Laios

- ATK buff — Multiple targets — `low` — conditional (rare)
- DEF buff — Single target — `low` — conditional (rare)
- Healing over time — Single target — `low` — conditional (rare)

#### Crowd Control provided by Laios

- Pin — Area — `medium`

#### Laios's Special Effects

#### Laios Provides

- Summoning — Single target

#### Laios Requires

- Enemy monsters present (Mythic+) — Enemies
- Monster ingredients (Supreme+) — Enemies
- Stacked resource (Supreme+) — Enemies

## Lenya

### Lenya's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Wild Duel (ultimate) — dash + duel multi-hit
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Lenya benefits from

Look for units providing: `Haste` `Max HP` `Crit` `Crit DMG Boost` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units that can act as a replacement for Lenya

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Vala (100% `Stun`)
- Walker (100% `Stun`)
- Gunnar (90% `Stun`)

### Summary for Lenya

#### Stats Lenya benefits from

- Haste
- Max HP
- Crit
- Crit DMG Boost
- Energy

#### Damage types dealt by Lenya

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Stun — Single target — `medium`

## Lily May

### Lily May's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Tempest Shot (ultimate) — interrupt enemy ultimate
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Lily May benefits from

Look for units providing: `ATK` `DEF Penetration`  
Common buffers are **Lyca**, **Ravion**, or **Mikola**.

- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, medium)
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]

### Units benefitting from Lily May

- Bonnie
- Aliceth

### Units that can act as a replacement for Lily May

**Buffs on allies**

- Kulu (100% `DEF Penetration`)
- Silven (100% `DEF Penetration`)
- Pang (50% `DEF Penetration`)

**Damage**

- Alsa (93% `Magic`)
- Sylphira (89% `Magic` `Max HP-based damage`)
- Shemira (80% `Magic` `Max HP-based damage`)

**Crowd Control**

- Marcille (60% `Interrupt`)
- Smokey & Meerky (55% `Interrupt`)

### Summary for Lily May

#### Stats Lily May benefits from

- ATK
- DEF Penetration

#### Damage types dealt by Lily May

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs provided by Lily May

- DEF Penetration buff (Legendary+) — Single target — `low`

#### Debuffs provided by Lily May

- Energy drain — All units — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Start of battle
- Interrupt — All units — `low`

#### Lily May's Special Effects

#### Lily May Provides

- Invincibility — Single target

## Lorsan

### Lorsan's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Whispering Tempest (ultimate) — storm zone + haste debuff
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Lorsan benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Hugin**, or **Ravion**.

- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]

### Units benefitting from Lorsan

- Callan
- Contess
- Evie
- Igor
- Phraesto
- Smokey & Meerky
- Thador
- Tilaya

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Hewynn (71% `Healing`)
- Isabella (50% `Healing`)

**Damage**

- Cryonaia (90% `Magic` `DoT`)
- Tasi (90% `Magic` `DoT`)
- Berial (88% `DoT` `Magic`)

**Crowd Control**

- Faramor (88% `Stun`)
- Koko (88% `Stun`)
- Lucy (75% `Stun`)

### Summary for Lorsan

#### Stats Lorsan benefits from

- ATK

#### Damage types dealt by Lorsan

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — Area

#### Buffs provided by Lorsan

- Dodge chance buff — Single target — `medium`
- Healing over time — Single target — `medium`
- Healing (Mythic+) — All units — `high`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Self — On skill
- Stun (EX+10) — Multiple targets — `high`

## Lucca

### Lucca's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Quake Slam (ultimate) — area knockdown slam
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Lucca benefits from

Look for units providing: `Max HP` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Hugin**, or **Rowan**.

- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Fay**
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]

### Units that can act as a replacement for Lucca

**Buffs on allies**

- Atalanta (100% `Healing`)
- Igor (100% `Healing`)
- Talene (100% `Healing`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Perseus (80% `Stun`)
- Zandrok (80% `Stun`)
- Lorsan (60% `Stun`)

### Summary for Lucca

#### Stats Lucca benefits from

- Max HP
- Physical DEF
- Magic DEF

#### Damage types dealt by Lucca

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Lucca

- Healing (Supreme+) — Single target — `low`

#### Crowd Control provided by Lucca

- Immune — Self — On skill
- Interrupt — Single target — `medium`
- Stun — Area — `medium`

## Lucius

### Lucius's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Divine Light Aegis (ultimate) — area shield + light damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Lucius benefits from

Look for units providing: `Healing`  
Common buffers are **Rowan**, **Mikola**, or **Lyca**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Kafra**
  - Healing over time (area, high)

### Units benefitting from Lucius

**23** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Shadewing
- Valka
- Himmel
- Tilaya
- Alna
- Athalia
- Baelran
- Daimon
- Eironn
- Gerda

### Units that can act as a replacement for Lucius

**Buffs on allies**

- Saida (80% `Max HP` `Healing`)
- Callan (50% `Max HP` `Healing`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Twins (66% `Move`)
- Soren (57% `Move` `Stun`)
- Rhys (54% `Move`)

### Summary for Lucius

#### Stats Lucius benefits from

- Healing

#### Damage types dealt by Lucius

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lucius

- Healing — Single target — `medium`
- Shield — Area — `high`

#### Debuffs provided by Lucius

- ATK debuff (Mythic+) — Area — `high`

#### Crowd Control provided by Lucius

- Move — Single target — `high`
- Stun — Single target — `low`

#### Lucius's Special Effects

#### Lucius Provides

- Reposition enemies — Single target

## Lucy

### Lucy's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Star Dress: Aquarius Form — permanent AoE water form
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: slow

### Units Lucy benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Dunlingr**
  - ATK SPD buff (all units, low) [signature fuel]
  - Haste buff (single target, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Lucy

**Buffs on allies**

- Korin (66% `Max HP`)
- Scarlita (66% `Max HP`)
- Callan (60% `Max HP`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

**Crowd Control**

- Pang (88% `Stun`)
- Faramor (84% `Stun`)
- Koko (84% `Stun`)

### Summary for Lucy

#### Stats Lucy benefits from

- ATK SPD
- Haste

#### Damage types dealt by Lucy

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Lucy

- Shield (Mythic+) — Single target — `high`

#### Debuffs provided by Lucy

- Damage taken debuff — Single target — `high`

#### Crowd Control provided by Lucy

- Unaffected — Self — On skill
- Stun — Single target — `high`

## Ludovic

### Ludovic's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Eternal Serenity (ultimate) — area sustained healing
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Ludovic benefits from

Look for units providing: `Healing`  
Common buffers are **Rowan**, **Mikola**, or **Lyca**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Kafra**
  - Healing over time (area, high)

### Units that can act as a replacement for Ludovic

**Buffs on allies**

- Gerda (65% `Healing`)
- Granny Dahnie (60% `Healing`)
- Antandra (59% `Healing`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

**Crowd Control**

- Damian (100% `Stun`)
- Nazrik (100% `Stun`)
- Nerion (100% `Stun`)

### Summary for Ludovic

#### Stats Ludovic benefits from

- Healing

#### Damage types dealt by Ludovic

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Ludovic

- Healing — Area — `medium`
- Healing over time — Single target — `high`

#### Crowd Control provided by Ludovic

- Unaffected — Self — On skill
- Stun (Supreme+) — Single target — `medium`

#### Ludovic's Special Effects

#### Ludovic Provides

- Revive ally — Area

## Lumont

### Lumont's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Lumont's Charge (ultimate) — charge + stomp knockdown
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Lumont benefits from

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Isabella**
  - Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)
  - Healing (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Hewynn**
  - Healing (all units, high)

### Units benefitting from Lumont

- Carolina
- Lucca
- Niru

### Units that can act as a replacement for Lumont

**Damage**

- Granny Dahnie (100% `Physical` `Max HP-based damage`)
- Soren (92% `Physical`)
- Gwyneth (92% `Physical` `Max HP-based damage`)

**Crowd Control**

- Antandra (57% `Stun` `Taunt`)
- Hepler (53% `Taunt` `Stun`)
- Brutus (50% `Taunt`)

### Summary for Lumont

#### Stats Lumont benefits from

- Haste
- Max HP
- Healing

#### Damage types dealt by Lumont

- Primary damage type (unit): **Physical**
- Physical — Area, Single target
- Max HP-based damage — Single target — `low`

#### Buffs provided by Lumont

- DEF buff — Multiple targets — `medium`

#### Debuffs provided by Lumont

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Lumont

- Unaffected — Self — On skill
- Stun — Area — `high`
- Taunt — Area — `medium`

## Lyca

### Lyca's behavior

- Movement: stationary (avg attack range 11.0 tiles)
- Signature skill: Comet Archery (ultimate) — area ranged volley
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Lyca benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Lyca

**63** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Indris
- Aliceth
- Valka
- Zorya
- Cecia
- Cyran
- Dionel
- Fay
- Gwyneth
- Korin

### Units that can act as a replacement for Lyca

**Buffs on allies**

- Valka (50% `ATK SPD`)

**Energy provider**

- Ravion
- Rowan
- Thador

**Damage**

- Igor (100% `Physical`)
- Koko (100% `Physical`)
- Kulu (100% `Physical`)

**Crowd Control**

- Bonnie (100% `Stun`)
- Marilee (100% `Stun`)
- Zanie (100% `Stun`)

### Summary for Lyca

#### Stats Lyca benefits from

- ATK SPD

#### Damage types dealt by Lyca

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target

#### Buffs provided by Lyca

- ATK SPD buff — All units — `medium`
- Energy recovery — All units — `low`

#### Debuffs provided by Lyca

- ATK debuff — All units — `high`
- Phys DEF debuff — All units — `high`

#### Crowd Control provided by Lyca

- Stun (EX+10) — Single target — `low`

## Marcille

### Marcille's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Silver-White Wings that Streak Across the Skies (ultimate) — large AoE magic damage
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Marcille benefits from

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Dunlingr**
  - ATK SPD buff (all units, low) [signature fuel]
  - Haste buff (single target, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Marcille

**Buffs on allies**

- Antandra (100% `Healing`)
- Solise (66% `Healing`)
- Hewynn (60% `Healing`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

**Crowd Control**

- Lily May (60% `Interrupt`)
- Saida (59% `Interrupt`)

### Summary for Marcille

#### Stats Marcille benefits from

- ATK SPD
- Haste
- Energy

#### Damage types dealt by Marcille

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Marcille

- Healing — Multiple targets — `high`

#### Crowd Control provided by Marcille

- Unaffected (Supreme+) — Self — On skill
- Interrupt (Mythic+) — Single target — `high`

#### Marcille's Special Effects

#### Marcille Provides

- Revive ally (Mythic+) — Single target
- Stacking buff (Supreme+) — Single target

#### Marcille Requires

- Once per battle (Mythic+) — Allies

## Marilee

### Marilee's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Mid-Air Shot (ultimate) — high-damage precision shot
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Marilee benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Crit` `Crit DMG Boost`  
Common buffers are **Twins**, **Lyca**, or **Mikola**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Marilee

**Damage**

- Perseus (94% `Physical` `True damage`)
- Scarlita (90% `Physical` `True damage`)
- Athalia (79% `Physical` `True damage`)

**Crowd Control**

- Bonnie (100% `Stun`)
- Lyca (100% `Stun`)
- Zanie (100% `Stun`)

### Summary for Marilee

#### Stats Marilee benefits from

- ATK
- ATK SPD
- Crit
- Crit DMG Boost

#### Damage types dealt by Marilee

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target
- True damage — Multiple targets — `low`

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

#### Marilee's Special Effects

#### Marilee Provides

- Stacking buff (Mythic+) — Multiple targets

## Mehira

### Mehira's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Euphoric Rush (ultimate) — AoE damage + charm
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Mehira benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Life Drain`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
  - Lifedrain buff (summons only, high, conditional (frequent))
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Isabella**
  - Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Vala (100% `Haste`)
- Gala (50% `Haste`)

**Similar Skills**

- Cyran (100% `enemy-grouping`)
- Eironn (100% `enemy-grouping`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

**Crowd Control**

- Satrana (56% `Charm`)

### Summary for Mehira

#### Stats Mehira benefits from

- Haste
- Max HP
- Healing
- Life Drain

#### Damage types dealt by Mehira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Mehira

- Haste buff — Single target — `high`

#### Debuffs provided by Mehira

- Damage taken debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Mehira

- Charm — Area — `medium`

#### Mehira's Special Effects

#### Mehira Provides

- HP threshold strike (Mythic+) — Self
- Summoning (Mythic+) — Self
- Untargetable (Mythic+) — Self

## Mikola

### Mikola's behavior

- Movement: moving (avg attack range 2.0 tiles)
- Signature skill: Dauntless Hymn (ultimate) — haste + DEF aura zone
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Mikola benefits from

Look for units providing: `ATK` `Haste`  
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units benefitting from Mikola

**79** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Sylphira
- Vala
- Laios
- Temesia
- Lumont
- Mehira
- Zorya
- Aurora

### Units that can act as a replacement for Mikola

**Damage**

- Igor (100% `Physical`)
- Koko (100% `Physical`)
- Kulu (100% `Physical`)

### Summary for Mikola

#### Stats Mikola benefits from

- ATK
- Haste

#### Damage types dealt by Mikola

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets

#### Buffs provided by Mikola

- ATK buff — Multiple targets — `medium`
- Haste buff — Multiple targets — `high`
- Healing — Multiple targets — `high`
- Healing over time — All units — `medium`
- Vitality buff (EX+10) — Multiple targets — `low`

#### Crowd Control provided by Mikola

- Unaffected (Supreme+) — Self — Conditional

## Mirael

### Mirael's behavior

- Movement: stationary (avg attack range 10.1 tiles)
- Signature skill: Winged Flame (ultimate) — area fire barrage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Mirael benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Mirael

**Damage**

- Bonnie (100% `Magic` `DoT`)
- Arden (78% `Magic` `DoT`)
- Aurora (72% `Magic`)

### Summary for Mirael

#### Stats Mirael benefits from

- ATK SPD

#### Damage types dealt by Mirael

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target

#### Debuffs provided by Mirael

- DoT — Single target — `low`

## Nara

### Nara's behavior

- Movement: mostly stationary (pulls enemies)
- Signature skill: Phantom Chains — pull enemy to self
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Nara benefits from

Look for units providing: `ATK` `Energy`  
Common buffers are **Ravion** or **Lyca**.

- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Units that can act as a replacement for Nara

**Buffs on allies**

- Berial (88% `Healing`)
- Athalia (75% `Healing`)
- Velara (72% `Healing`)

**Damage**

- Korin (90% `Max HP-based damage` `True damage` `Physical`)
- Baelran (85% `Max HP-based damage` `True damage` `Physical`)
- Nazrik (84% `True damage` `Physical` `Max HP-based damage`)

### Summary for Nara

#### Stats Nara benefits from

- ATK
- Energy

#### Damage types dealt by Nara

- Primary damage type (unit): **Physical**
- Physical — Single target
- Max HP-based damage — Area — `medium`
- True damage — Single target — `high`

#### Buffs provided by Nara

- Healing (Mythic+) — Area — `low`

#### Debuffs provided by Nara

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Nara

- Unaffected (Supreme+) — Self — Permanent

## Natsu

### Natsu's behavior

- Movement: stationary (avg attack range 11.0 tiles)
- Signature skill: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate) — high-damage elemental beam
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: normal

### Units Natsu benefits from

Look for units providing: `ATK` `Haste` `Crit` `Crit DMG Boost`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, low) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, low) [signature fuel]

### Units benefitting from Natsu

- Indris
- Bonnie

### Units that can act as a replacement for Natsu

**Similar Skills**

- Talene (100% `fire-attack`)

**Damage**

- Daimon (88% `Max HP-based damage` `Magic` `DoT`)
- Satrana (88% `Max HP-based damage` `Magic` `DoT`)
- Shemira (87% `Max HP-based damage` `Magic`)

**Crowd Control**

- Valka (70% `Stun` `Knock down`)
- Callan (58% `Stun` `Knock down`)
- Frieren (52% `Knock down` `Stun`)

### Summary for Natsu

#### Stats Natsu benefits from

- ATK
- Haste
- Crit
- Crit DMG Boost

#### Damage types dealt by Natsu

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Single target
- Max HP-based damage — Area — `medium`

#### Debuffs provided by Natsu

- Haste debuff — Area — `high`
- Max HP debuff (Mythic+) — Single target — `medium`
- DoT (Supreme+) — Single target — `low`

#### Crowd Control provided by Natsu

- Knock down — Area — `low`
- Stun — Single target — `medium`

## Nazrik

### Nazrik's behavior

- Movement: stationary (avg attack range 10.0 tiles)
- Signature skill: Rend Rupture (ultimate) — HP-drain bleed DoT
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Nazrik benefits from

Look for units providing: `Crit`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Nazrik

**Damage**

- Nara (84% `True damage` `Physical` `Max HP-based damage`)
- Indris (81% `True damage` `Physical` `Max HP-based damage`)
- Pippa (79% `True damage` `Max HP-based damage`)

**Crowd Control**

- Damian (100% `Stun`)
- Ludovic (100% `Stun`)
- Nerion (100% `Stun`)

### Summary for Nazrik

#### Stats Nazrik benefits from

- Crit

#### Damage types dealt by Nazrik

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- Max HP-based damage — Single target — `low`
- True damage — Single target — `high`

#### Debuffs provided by Nazrik

- Max HP debuff — Single target — `medium`
- Crit Resist debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Nazrik

- Stun — Single target — `medium`

#### Nazrik's Special Effects

#### Nazrik Provides

- Stacking buff — Single target

## Nerion

### Nerion's behavior

- Movement: mostly stationary (avg attack range 4.0 tiles)
- Signature skill: Drowning Doom (ultimate) — pull + submerge enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Nerion benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Enables CC on enemies via Stun (area, high)
- **Tasi**
  - Enables CC on enemies via Sleep (all units, high)
- **Kordan**
  - DEF Penetration buff (multiple targets, low)
  - Enables CC on enemies via Pin (area, high)
- **Carolina**
  - Enables CC on enemies via Freeze (area, high)
- **Indris**
  - Enables CC on enemies via Pin (area, high)

### Units that can act as a replacement for Nerion

**Damage**

- Aurora (100% `Magic`)
- Carolina (100% `Magic`)
- Eironn (100% `Magic`)

**Crowd Control**

- Damian (100% `Stun`)
- Ludovic (100% `Stun`)
- Nazrik (100% `Stun`)

### Summary for Nerion

#### Stats Nerion benefits from

- ATK SPD
- Max HP
- Energy
- DEF Penetration

#### Damage types dealt by Nerion

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target

#### Debuffs provided by Nerion

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Stun — Single target — `medium`

#### Nerion's Special Effects

#### Nerion Provides

- Enhanced form (Supreme+) — Single target

#### Nerion Requires

- CC on enemies (EX+15) — Enemies

## Niru

### Niru's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Soul Shepherd (ultimate) — save ally from fatal blow
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Niru benefits from

Look for units providing: `Physical DEF` `Magic DEF`  
Common buffers are **Rowan**, **Lyca**, or **Twins**.

- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)
- **Fay**
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Enables Enemy defeat via HP threshold strike
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Enables Enemy defeat via Marked target (focus fire)

### Units that can act as a replacement for Niru

**Similar Skills**

- Bryon (100% `battle-start-ult`)

**Damage**

- Dunlingr (79% `Magic` `HP loss`)
- Walker (70% `HP loss` `Max HP-based damage`)
- Shadewing (60% `Magic` `Max HP-based damage` `HP loss`)

### Summary for Niru

#### Stats Niru benefits from

- Physical DEF
- Magic DEF

#### Damage types dealt by Niru

- Primary damage type (unit): **Magic**
- Magic — All units, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units, Single target — `low`

#### Buffs provided by Niru

- Healing — Single target — `low` — conditional (rare)

#### Niru's Special Effects

#### Niru Provides

- Spirit form protection — Single target
- Start-of-battle cast (Mythic+) — Self

#### Niru Requires

- Ally blessing active — Allies
- Enemy defeat — Allies

## Odie

### Odie's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Heart Crusher — instantly defeat below poison threshold
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Odie benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Odie

**Damage**

- Bonnie (54% `DoT` `Magic`)
- Mirael (54% `DoT` `Magic`)
- Hammie (50% `Magic`)

### Summary for Odie

#### Stats Odie benefits from

- ATK SPD

#### Damage types dealt by Odie

- Primary damage type (unit): **Magic**
- Magic — Single target
- DoT — Single target

#### Debuffs provided by Odie

- DoT — Single target — `medium`

## Pandora

### Pandora's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Boxed Blessing — pull ally into box at start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Pandora benefits from

Look for units providing: `Energy`  
Common buffers are **Ravion** or **Lyca**.

- **Smokey & Meerky**
  - Energy recovery (multiple targets, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Units benefitting from Pandora

- Indris
- Chippy
- Nara
- Scarlita

### Units that can act as a replacement for Pandora

**Buffs on allies**

- Gunnar (54% `Healing` `Invincible`)

**Energy provider**

- Rowan

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

### Summary for Pandora

#### Stats Pandora benefits from

- Energy

#### Damage types dealt by Pandora

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Pandora

- Energy recovery — Single target — `low`
- Healing — Single target — `high`
- Invincible — Single target — `high`
- Max HP buff (Legendary+) — Single target — `low`

#### Debuffs provided by Pandora

- ATK debuff — All units — `low`
- Damage taken debuff — Single target — `low`
- Energy drain — Single target — `low`
- Haste debuff — Single target — `medium`
- Vitality debuff — Single target — `high`

#### Pandora's Special Effects

#### Pandora Provides

- Invincibility — Single target

## Pang

### Pang's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Sky Splitter (ultimate) — area knockdown burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Pang benefits from

Look for units providing: `ATK` `Haste` `Energy` `DEF Penetration`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Aliceth**
  - ATK buff (multiple targets, low)
  - DEF Penetration buff (multiple targets, medium)

### Units that can act as a replacement for Pang

**Buffs on allies**

- Kulu (50% `DEF Penetration`)
- Lily May (50% `DEF Penetration`)
- Silven (50% `DEF Penetration`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Lucy (88% `Stun`)
- Gunnar (83% `Stun`)
- Faramor (75% `Stun`)

### Summary for Pang

#### Stats Pang benefits from

- ATK
- Haste
- Energy
- DEF Penetration

#### Damage types dealt by Pang

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Pang

- Shield (EX+10) — Single target — `low`
- DEF Penetration buff (Supreme+) — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected — Self — On skill
- Stun — Area — `low`

#### Pang's Special Effects

#### Pang Provides

- Transformation — Self

## Parisa

### Parisa's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Floral Splendor (ultimate) — mark + AoE burst damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Parisa benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Parisa

**Damage**

- Aurora (100% `Magic`)
- Carolina (100% `Magic`)
- Eironn (100% `Magic`)

### Summary for Parisa

#### Stats Parisa benefits from

- ATK
- ATK SPD
- Energy

#### Damage types dealt by Parisa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Self, Single target

#### Parisa's Special Effects

#### Parisa Provides

- Marked target (focus fire) — Area

## Perseus

### Perseus's behavior

- Movement: moving (avg attack range 2.9 tiles)
- Signature skill: Divine Rend (ultimate) — march + continuous knockback
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Perseus benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Koko**
  - Max HP via Shield (all units, low)
  - Enables Ally stat buffs via 6 ally stat buffs
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Alna**
  - ATK buff (single target, medium)
  - Max HP buff (single target, low)
  - Enables Ally stat buffs via 6 ally stat buffs (start of battle)

### Units that can act as a replacement for Perseus

**Buffs on allies**

- Ravion (50% `ATK`)
- Sonja (50% `ATK`)

**Damage**

- Scarlita (95% `Physical` `True damage`)
- Marilee (94% `Physical` `True damage`)
- Athalia (82% `Physical` `True damage`)

**Crowd Control**

- Zandrok (100% `Stun`)
- Lucca (80% `Stun`)
- Lorsan (75% `Stun`)

### Summary for Perseus

#### Stats Perseus benefits from

- ATK
- ATK SPD
- Max HP

#### Damage types dealt by Perseus

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Perseus

- ATK buff — Multiple targets — `medium`

#### Crowd Control provided by Perseus

- Unaffected — Multiple targets — On skill
- Stun — Area — `medium`

#### Perseus's Special Effects

#### Perseus Requires

- Ally stat buffs (EX+10) — —

## Phraesto

### Phraesto's behavior

- Movement: moving (avg attack range 1.8 tiles)
- Signature skill: Crimson Contract — buff two allies at battle start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Phraesto benefits from

Look for units providing: `Healing` `Energy`  
Common buffers are **Mikola**, **Rowan**, or **Ravion**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Isabella**
  - Healing (area, high)

### Units that can act as a replacement for Phraesto

**Buffs on allies**

- Korin (50% `Max HP`)
- Scarlita (50% `Max HP`)

**Energy provider**

- Smokey & Meerky
- Thador

**Damage**

- Aurora (100% `Magic`)
- Carolina (100% `Magic`)
- Eironn (100% `Magic`)

**Crowd Control**

- Bonnie (50% `Stun`)
- Lyca (50% `Stun`)
- Marilee (50% `Stun`)

### Summary for Phraesto

#### Stats Phraesto benefits from

- Healing
- Energy

#### Damage types dealt by Phraesto

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Phraesto

- Damage taken reduction — Single target — `low`
- Max HP buff — Single target — `low`
- Shield — Single target — `medium`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `low`
- Taunt (Mythic+) — Single target — `low`

#### Phraesto's Special Effects

#### Phraesto Provides

- Summoning — Area

## Pippa

### Pippa's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Chaos Manifest (ultimate) — reposition + random chaos
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: normal

### Units Pippa benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, low) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, low) [signature fuel]

### Units that can act as a replacement for Pippa

**Damage**

- Nazrik (79% `True damage` `Max HP-based damage`)
- Nara (74% `True damage` `Max HP-based damage`)
- Indris (73% `True damage` `Max HP-based damage`)

### Summary for Pippa

#### Stats Pippa benefits from

- Haste

#### Damage types dealt by Pippa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`
- True damage — Area — `low`

#### Debuffs provided by Pippa

- Energy drain — Area — `medium`

#### Crowd Control provided by Pippa

- Unaffected — Self — On skill
- Knock down — Single target — `low`
- Move — Single target — `low`
- Pin — Single target — `medium`

## Ravion

### Ravion's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Killer Flush (ultimate) — multi-hit lost-HP scaling
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Ravion benefits from

Look for units providing: `ATK` `Haste` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units benefitting from Ravion

**23** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Indris
- Aliceth
- Arden
- Pang
- Parisa
- Cryonaia
- Cyran
- Hammie
- Hewynn
- Hodgkin

### Units that can act as a replacement for Ravion

**Buffs on allies**

- Perseus (50% `ATK`)

**Energy provider**

- Lyca
- Thador

**Damage**

- Kordan (100% `Physical` `HP loss`)
- Aliceth (89% `Physical` `HP loss`)
- Harak (82% `Physical` `HP loss`)

### Summary for Ravion

#### Stats Ravion benefits from

- ATK
- Haste
- Energy

#### Damage types dealt by Ravion

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `low`

#### Buffs provided by Ravion

- ATK buff — Multiple targets — `medium`
- Energy recovery — Multiple targets — `medium`
- Lifedrain buff (EX+10) — Single target — `low` — conditional (rare)
- Shield (EX+10) — Multiple targets — `low` — conditional (rare)

#### Debuffs provided by Ravion

- ATK debuff — Multiple targets — `medium`
- Phys DEF debuff — Multiple targets — `medium`

#### Crowd Control provided by Ravion

- Unaffected — Self — Start of battle
- Knock down — Multiple targets — `high`
- Move — Multiple targets — `high`

#### Ravion's Special Effects

#### Ravion Provides

- Position swap (EX+10) — Multiple targets

#### Ravion Requires

- Boss encounter — Allies

## Reinier

### Reinier's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Dynamic Balance — swap ally+enemy positions at start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Reinier benefits from

_No synergy partners matched stat buffs or enablers._

### Units that can act as a replacement for Reinier

**Buffs on allies**

- Atalanta (50% `Healing`)
- Igor (50% `Healing`)
- Lucca (50% `Healing`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

### Summary for Reinier

#### Damage types dealt by Reinier

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Reinier

- Healing — Single target — `low` — conditional (frequent)
- ATK buff (Legendary+) — Single target — `low`

#### Debuffs provided by Reinier

- ATK debuff (Legendary+) — Single target — `low`
- Damage taken debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Reinier

- Steadfast — Single target — Conditional
- Unaffected — Single target — Conditional
- Interrupt — Single target — `high`
- Move — Multiple targets — `high`
- Knock down (Mythic+) — Single target — `low`

## Rhys

### Rhys's behavior

- Movement: high movement (moves while attacking)
- Signature skill: Flame Barrage (ultimate) — ranged fire barrage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Rhys benefits from

Look for units providing: `ATK SPD / Haste` `Crit` `Crit DMG Boost`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Rhys

**Buffs on allies**

- Athalia (66% `Healing`)
- Nara (54% `Healing`)
- Berial (50% `Healing`)

**Damage**

- Hugin (100% `Physical`)
- Sinbad (100% `Physical`)
- Antandra (75% `Physical`)

**Crowd Control**

- Twins (59% `Move`)
- Cassadee (56% `Move`)
- Lucius (54% `Move`)

### Summary for Rhys

#### Stats Rhys benefits from

- ATK SPD
- Crit
- Crit DMG Boost

#### Damage types dealt by Rhys

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs provided by Rhys

- Healing — Single target — `medium`
- Movement speed buff (Mythic+) — Single target — `low`

#### Crowd Control provided by Rhys

- Move — Single target — `high`

## Rowan

### Rowan's behavior

- Movement: moving (repositions on cast)
- Signature skill: Fatal Greed (ultimate) — AoE energy recovery burst
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Rowan benefits from

Look for units providing: `Haste` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, low) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, low) [signature fuel]

### Units benefitting from Rowan

**26** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Granny Dahnie
- Kordan
- Temesia
- Lumont
- Shemira
- Sylphira
- Vala
- Cecia
- Niru
- Lucius

### Units that can act as a replacement for Rowan

**Energy provider**

- Pandora
- Lyca

**Damage**

- Hammie (100% `Magic`)
- Odie (50% `Magic`)

### Summary for Rowan

#### Stats Rowan benefits from

- Haste
- Energy

#### Damage types dealt by Rowan

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Rowan

- Healing — Area — `medium`
- DEF buff (Mythic+) — Single target — `high`
- Max HP buff (Mythic+) — Single target — `high`
- ATK buff (EX+5) — Single target — `low`

#### Debuffs provided by Rowan

- Energy drain — Single target — `medium`

#### Rowan's Special Effects

#### Rowan Provides

- Energy steal — Single target

#### Rowan Requires

- Once per battle (Mythic+) — Allies

## Saida

### Saida's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Seed Siphon (ultimate) — pin + energy drain + seed
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Saida benefits from

Look for units providing: `Max HP`  
Common buffers are **Lucius** or **Hugin**.

- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Gala**
  - Max HP via Shield (single target, high)
- **Lucy**
  - Max HP via Shield (single target, high)

### Units benefitting from Saida

- Alna
- Athalia
- Daimon
- Eironn
- Gerda
- Kruger
- Silvina
- Thoran
- Ulmus

### Units that can act as a replacement for Saida

**Buffs on allies**

- Lucius (80% `Max HP` `Healing`)
- Callan (62% `Max HP` `Healing`)
- Hepler (54% `Max HP` `Healing`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

**Crowd Control**

- Marcille (59% `Interrupt`)

### Summary for Saida

#### Stats Saida benefits from

- Max HP

#### Damage types dealt by Saida

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Self, Single target

#### Buffs provided by Saida

- Healing — Single target — `medium`
- Shield — Multiple targets — `high`

#### Debuffs provided by Saida

- Energy drain — Single target — `high`

#### Crowd Control provided by Saida

- Unaffected — Self — Conditional
- Interrupt — Area — `low`
- Move — Single target — `low`

#### Saida's Special Effects

#### Saida Provides

- Revive ally — Single target

#### Saida Requires

- Boss encounter — Enemies

## Salazer

### Salazer's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Rain of Blades (ultimate) — area blade storm
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Salazer benefits from

Look for units providing: `Max HP`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]

### Units that can act as a replacement for Salazer

**Buffs on allies**

- Thoran (60% `Healing` `Life Drain`)
- Ulmus (60% `Healing` `Life Drain` `Max HP`)
- Viperian (60% `Healing` `Life Drain`)

**Damage**

- Chippy (100% `Physical`)
- Silvina (100% `Physical`)
- Thoran (100% `Physical`)

**Crowd Control**

- Gala (50% `Pin`)

### Summary for Salazer

#### Stats Salazer benefits from

- Max HP

#### Damage types dealt by Salazer

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Buffs provided by Salazer

- Lifedrain buff — Single target — `low`
- Healing (Supreme+) — Single target — `medium`
- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Salazer

- Pin — Single target — `low`

## Satrana

### Satrana's behavior

- Movement: moving (avg attack range 1.5 tiles)
- Signature skill: Fiery Dance (ultimate) — area fire burn damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Satrana benefits from

Look for units providing: `Max HP`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]

### Units that can act as a replacement for Satrana

**Buffs on allies**

- Sylphira (100% `Life Drain`)
- Brutus (50% `Life Drain`)
- Seth (50% `Life Drain`)

**Damage**

- Daimon (100% `Max HP-based damage` `DoT` `Magic`)
- Shemira (90% `Max HP-based damage` `Magic`)
- Natsu (88% `Max HP-based damage` `Magic` `DoT`)

**Crowd Control**

- Mehira (56% `Charm`)

### Summary for Satrana

#### Stats Satrana benefits from

- Max HP

#### Damage types dealt by Satrana

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Arc, Area, Single target — `high`

#### Buffs provided by Satrana

- Lifedrain buff — Single target — `low`

#### Debuffs provided by Satrana

- Vitality debuff — Area — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `high`

#### Satrana's Special Effects

#### Satrana Provides

- Ally DoT on enemies — Area
- Ally Vitality debuff on enemies — Area
- Ally grant (Sparks) — Area
- Invincibility — Area

## Scarlita

### Scarlita's behavior

- Movement: moving (brief reposition)
- Signature skill: Divine Wrath — instantly defeat low-HP enemies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Scarlita benefits from

Look for units providing: `Execution` `Energy`  
Common buffers are **Ravion** or **Lyca**.

- **Smokey & Meerky**
  - Energy recovery (multiple targets, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
- **Thador**
  - Energy recovery (single target, low) [signature fuel]

### Units that can act as a replacement for Scarlita

**Buffs on allies**

- Korin (100% `Max HP`)
- Lucy (66% `Max HP`)
- Daimon (50% `Max HP`)

**Damage**

- Perseus (95% `Physical` `True damage`)
- Marilee (90% `Physical` `True damage`)
- Athalia (85% `Physical` `True damage`)

**Crowd Control**

- Soren (65% `Stun` `Move`)
- Alsa (56% `Stun` `Move`)
- Cassadee (51% `Move` `Stun`)

### Summary for Scarlita

#### Stats Scarlita benefits from

- Execution
- Energy

#### Damage types dealt by Scarlita

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Scarlita

- Shield — Single target — `medium`

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock down — Arc — `low`
- Move — All units — `low`
- Stun — Area — `medium`

#### Scarlita's Special Effects

#### Scarlita Provides

- Invincibility — Area

## Seth

### Seth's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Shadow Strike (ultimate) — multi-hit shadow burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Seth benefits from

Look for units providing: `ATK` `Haste` `Crit` `Energy` `Life Drain`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, low) [signature fuel]
  - Lifedrain buff (all units, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, low) [signature fuel]
  - Lifedrain buff (single target, high)
  - ATK SPD via Haste buff (multiple targets, low) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Seth

**Buffs on allies**

- Atalanta (50% `Healing`)
- Igor (50% `Healing`)
- Lucca (50% `Healing`)

**Damage**

- Harak (85% `Physical`)
- Kordan (75% `Physical`)
- Ravion (75% `Physical`)

### Summary for Seth

#### Stats Seth benefits from

- ATK
- Haste
- Crit
- Energy
- Life Drain

#### Damage types dealt by Seth

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- HP loss — Self

#### Buffs provided by Seth

- Healing — Single target — `low`
- Lifedrain buff — Single target — `low`

#### Debuffs provided by Seth

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Freeze — Single target — `low`

#### Seth's Special Effects

#### Seth Provides

- Invincibility — Single target
- Stacking buff — Self

## Shadewing

### Shadewing's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Withering Curse — convert DoT to burst damage
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Shadewing benefits from

Look for units providing: `ATK` `Max HP` `Energy` `Life Drain`  
Common buffers are **Lucius**, **Lyca**, or **Ravion**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Enables Debuff on target via DoT (all units)
  - Enables Continuous damage on enemies via Burn
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via tick damage
- **Alna**
  - ATK buff (single target, medium)
  - Max HP buff (single target, low)
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via DoT
- **Koko**
  - Max HP via Shield (all units, low)
  - Lifedrain buff (multiple targets, low)
  - Enables Debuff on target via Damage taken debuff (area)
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Continuous damage on enemies via DoT + Burn

### Units that can act as a replacement for Shadewing

**Damage**

- Niru (60% `Magic` `Max HP-based damage` `HP loss`)
- Baelran (55% `Max HP-based damage` `True damage`)
- Nara (53% `Max HP-based damage` `True damage`)

### Summary for Shadewing

#### Stats Shadewing benefits from

- ATK
- Max HP
- Energy
- Life Drain

#### Damage types dealt by Shadewing

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units, Single target — `high`
- True damage — Single target — `low`

#### Debuffs provided by Shadewing

- Magic DEF debuff — All units — `low`

#### Shadewing's Special Effects

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — All units
- Invincibility — All units
- Damage leech from allies (Supreme+) — Self

#### Shadewing Requires

- Continuous damage on enemies — Enemies
- Debuff on target — Enemies

## Shakir

### Shakir's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Ravaging Claws (ultimate) — single-target charge damage
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Shakir benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]

### Units that can act as a replacement for Shakir

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

### Summary for Shakir

#### Stats Shakir benefits from

- Haste

#### Damage types dealt by Shakir

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Multiple targets, Single target

#### Buffs provided by Shakir

- Damage taken reduction — Multiple targets — `low`
- Haste buff — Multiple targets — `low`
- Lifedrain buff — Single target — `high`

#### Debuffs provided by Shakir

- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Shakir

- Unaffected — Self — Form

#### Shakir's Special Effects

#### Shakir Provides

- Transformation — Self

#### Shakir Requires

- Form or stance active — Enemies

## Shemira

### Shemira's behavior

- Movement: mostly stationary (avg attack range 4.0 tiles)
- Signature skill: Phantom Procession (ultimate) — sustained area ghost damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Shemira benefits from

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Rowan**, or **Mikola**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Isabella**
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units that can act as a replacement for Shemira

**Similar Skills**

- Frieren (100% `high-damage-ult`)

**Damage**

- Daimon (90% `Max HP-based damage` `Magic`)
- Satrana (90% `Max HP-based damage` `Magic`)
- Natsu (87% `Max HP-based damage` `Magic`)

### Summary for Shemira

#### Stats Shemira benefits from

- Max HP
- Healing
- Energy

#### Damage types dealt by Shemira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- Max HP-based damage — Area, Single target — `high`

## Silven

### Silven's behavior

- Movement: stationary (avg attack range 12.0 tiles)
- Signature skill: Gravity Collapse — stack marks + detonate stun
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Silven benefits from

Look for units providing: `ATK SPD / Haste` `Energy` `DEF Penetration` `Physical DEF`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Evie**
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Koko**
  - Enables Ally stat buffs via 6 ally stat buffs
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - DEF buff (multiple targets, low)
  - Enables Ally stat buffs via 5 ally stat buffs
- **Alna**
  - Enables Ally stat buffs via 6 ally stat buffs (start of battle)
- **Contess**
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)

### Units that can act as a replacement for Silven

**Buffs on allies**

- Kulu (100% `DEF Penetration`)
- Lily May (100% `DEF Penetration`)
- Pang (50% `DEF Penetration`)

**Damage**

- Lily May (80% `Magic` `Max HP-based damage`)
- Sylphira (79% `Magic` `Max HP-based damage`)
- Alsa (73% `Magic`)

### Summary for Silven

#### Stats Silven benefits from

- ATK SPD
- Energy
- DEF Penetration
- Physical DEF

#### Damage types dealt by Silven

- Primary damage type (unit): **Magic**
- Magic — Self, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs provided by Silven

- DEF Penetration buff (Mythic+) — Single target — `low`

#### Silven's Special Effects

#### Silven Requires

- Ally stat buffs (Mythic+) — Allies

## Silvina

### Silvina's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Shadow Slayer (ultimate) — stealth + execute burst
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Silvina benefits from

Look for units providing: `Max HP` `Crit`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Cecia**
  - Max HP buff (single target, high)
  - ATK SPD buff (single target, low) [signature fuel]

### Units that can act as a replacement for Silvina

**Damage**

- Chippy (100% `Physical`)
- Salazer (100% `Physical`)
- Thoran (100% `Physical`)

**Crowd Control**

- Daimon (72% `Frighten`)

### Summary for Silvina

#### Stats Silvina benefits from

- Max HP
- Crit

#### Damage types dealt by Silvina

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Debuffs provided by Silvina

- Energy drain — Single target — `high`
- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Silvina

- Stun — Single target — `low`
- Frighten (EX+10) — Area — `low`

#### Silvina's Special Effects

#### Silvina Provides

- Marked target (focus fire) — Single target

## Sinbad

### Sinbad's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Whizzing Edge (ultimate) — multi-hit physical slashes
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Sinbad benefits from

Look for units providing: `ATK SPD / Haste` `Energy`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Sinbad

- Indris

### Units that can act as a replacement for Sinbad

**Damage**

- Hugin (100% `Physical`)
- Rhys (100% `Physical`)
- Antandra (75% `Physical`)

### Summary for Sinbad

#### Stats Sinbad benefits from

- ATK SPD
- Energy

#### Damage types dealt by Sinbad

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Self, Single target

#### Debuffs provided by Sinbad

- Damage taken debuff — Single target — `medium`
- ATK debuff (Mythic+) — Multiple targets — `high`
- Energy drain (Mythic+) — Multiple targets — `medium`
- Magic DEF debuff (Mythic+) — Multiple targets — `medium`
- Phys DEF debuff (Mythic+) — Multiple targets — `medium`
- Vitality debuff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Sinbad

- Unaffected — Multiple targets — Conditional

#### Sinbad's Special Effects

#### Sinbad Provides

- Marked target (focus fire) — Multiple targets

## Smokey & Meerky

### Smokey & Meerky's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Special Aroma (ultimate) — heal aura + upgradeable zone
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Smokey & Meerky benefits from

Look for units providing: `ATK` `Healing` `Energy`  
Common buffers are **Mikola**, **Ravion**, or **Rowan**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Contess**
  - ATK buff (single target, high)
  - Healing (multiple targets, high)
- **Isabella**
  - Healing (area, high)

### Units benefitting from Smokey & Meerky

- Nara
- Pandora
- Scarlita

### Units that can act as a replacement for Smokey & Meerky

**Buffs on allies**

- Gerda (60% `Healing`)
- Ludovic (52% `Healing`)

**Energy provider**

- Phraesto
- Thador

**Damage**

- Aurora (100% `Magic`)
- Carolina (100% `Magic`)
- Eironn (100% `Magic`)

**Crowd Control**

- Lily May (55% `Interrupt`)

### Summary for Smokey & Meerky

#### Stats Smokey & Meerky benefits from

- ATK
- Healing
- Energy

#### Damage types dealt by Smokey & Meerky

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Smokey & Meerky

- Energy recovery — Multiple targets — `low`
- Healing — Multiple targets — `medium`
- Healing over time — Multiple targets — `medium`
- ATK buff (Legendary+) — Multiple targets — `low`

#### Crowd Control provided by Smokey & Meerky

- Interrupt — Area — `medium`
- Stun (EX+10) — Single target — `low`

## Solise

### Solise's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Life's Embrace (ultimate) — AoE healing waves
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: fast

### Units Solise benefits from

Look for units providing: `ATK`  
Common buffers are **Hugin**, **Mikola**, or **Twins**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Energy recovery (multiple targets, low) [signature fuel]

### Units that can act as a replacement for Solise

**Buffs on allies**

- Berial (75% `Healing`)
- Antandra (66% `Healing`)
- Marcille (66% `Healing`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

### Summary for Solise

#### Stats Solise benefits from

- ATK

#### Damage types dealt by Solise

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Solise

- Healing — Multiple targets — `medium`
- Shield — Summons only — `medium`

#### Crowd Control provided by Solise

- Unaffected — Self — Start of battle

#### Solise's Special Effects

#### Solise Provides

- Ally blessing (Mythic+) — Single target

## Sonja

### Sonja's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Crimson Covenant — ATK + DEF buff two flanking allies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Sonja benefits from

Look for units providing: `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Callan**
  - Max HP via Shield (multiple targets, medium)

### Units that can act as a replacement for Sonja

**Buffs on allies**

- Perseus (50% `ATK`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Lenya (88% `Stun`)
- Vala (88% `Stun`)
- Walker (88% `Stun`)

### Summary for Sonja

#### Stats Sonja benefits from

- Haste
- Max HP

#### Damage types dealt by Sonja

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Sonja

- ATK buff — Multiple targets — `low`

#### Crowd Control provided by Sonja

- Stun — Area — `low`

## Soren

### Soren's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Whirlwind Swing (ultimate) — knockback + collision stun
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Soren benefits from

Look for units providing: `Haste` `Max HP` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units that can act as a replacement for Soren

**Buffs on allies**

- Ulmus (50% `Healing` `Max HP`)
- Zorya (50% `Healing`)

**Damage**

- Granny Dahnie (92% `Physical`)
- Lumont (92% `Physical`)
- Gwyneth (86% `Physical`)

**Crowd Control**

- Alsa (73% `Stun` `Move`)
- Atalanta (66% `Move` `Stun`)
- Cassadee (66% `Move` `Stun`)

### Summary for Soren

#### Stats Soren benefits from

- Haste
- Max HP
- Energy

#### Damage types dealt by Soren

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- Max HP-based damage — Self

#### Buffs provided by Soren

- Healing over time (Mythic+) — Single target — `low`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Soren

- Move — Single target — `high`
- Stun — Area — `low`

## Sylphira

### Sylphira's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Grand Finale (ultimate) — beat stacking + song DoT
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Sylphira benefits from

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Isabella**
  - Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)

### Units that can act as a replacement for Sylphira

**Buffs on allies**

- Satrana (100% `Life Drain`)
- Brutus (50% `Life Drain`)
- Seth (50% `Life Drain`)

**Damage**

- Lily May (89% `Magic` `Max HP-based damage`)
- Alsa (84% `Magic`)
- Natsu (84% `Magic` `Max HP-based damage`)

**Crowd Control**

- Temesia (60% `Knock down` `Interrupt`)

### Summary for Sylphira

#### Stats Sylphira benefits from

- ATK
- Haste
- Healing

#### Damage types dealt by Sylphira

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Single target — `medium`

#### Buffs provided by Sylphira

- Lifedrain buff (Supreme+) — Single target — `low`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `medium`
- Max HP debuff — Area — `medium`

#### Crowd Control provided by Sylphira

- Immune — Self — On skill
- Unaffected — Area — Conditional
- Cleanse (Mythic+) — Self — On skill
- Interrupt — Area — `low`
- Knock down — Area — `medium`
- Silence — Area — `low`

#### Sylphira's Special Effects

#### Sylphira Provides

- Dispel debuffs (Mythic+) — Self
- Stacking buff (Mythic+) — Self

## Talene

### Talene's behavior

- Movement: moving (avg attack range 3.0 tiles)
- Signature skill: Divine Conflagration (ultimate) — sustained channelled flame beam
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Talene benefits from

Look for units providing: `ATK` `Max HP` `Healing` `Life Drain`  
Common buffers are **Mikola**, **Lucius**, or **Rowan**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)
  - Healing (multiple targets, high)
- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)

### Units that can act as a replacement for Talene

**Buffs on allies**

- Atalanta (100% `Healing`)
- Igor (100% `Healing`)
- Lucca (100% `Healing`)

**Similar Skills**

- Natsu (100% `fire-attack`)

**Damage**

- Zorya (93% `HP loss` `Magic`)
- Aliceth (70% `HP loss`)
- Harak (67% `HP loss`)

### Summary for Talene

#### Stats Talene benefits from

- ATK
- Max HP
- Healing
- Life Drain

#### Damage types dealt by Talene

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- HP loss — All units, Single target — `high`

#### Buffs provided by Talene

- Healing — Single target — `low`

#### Talene's Special Effects

#### Talene Provides

- Transformation — Self
- Stacking buff (Mythic+) — Area

## Tasi

### Tasi's behavior

- Movement: stationary (avg attack range 10.0 tiles)
- Signature skill: Eternal Dreamscape (ultimate) — sleep all enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Tasi benefits from

Look for units providing: `ATK` `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Tasi

- Nerion
- Carolina

### Units that can act as a replacement for Tasi

**Buffs on allies**

- Hodgkin (100% `Healing`)
- Bryon (66% `Healing`)
- Granny Dahnie (60% `Healing`)

**Damage**

- Cryonaia (100% `DoT` `Magic`)
- Lorsan (90% `Magic` `DoT`)
- Berial (80% `DoT` `Magic`)

### Summary for Tasi

#### Stats Tasi benefits from

- ATK
- Haste
- Max HP

#### Damage types dealt by Tasi

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Single target

#### Buffs provided by Tasi

- Healing over time — Single target — `high`

#### Crowd Control provided by Tasi

- Pin — All units — `low`
- Sleep — All units — `high`
- Stun — Area — `high`

#### Tasi's Special Effects

#### Tasi Provides

- Invincibility — Area
- Sleep (area) — Single target
- Transformation — Self

## Temesia

### Temesia's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Knight's Heart (ultimate) — constant charge + knockdown through enemies
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Temesia benefits from

Look for units providing: `ATK` `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)
- **Contess**
  - ATK buff (single target, high)
  - Max HP via Shield (single target, medium)
  - Healing (multiple targets, high)
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
  - Healing (single target, low)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))

### Units that can act as a replacement for Temesia

**Buffs on allies**

- Atalanta (100% `Healing`)
- Igor (100% `Healing`)
- Lucca (100% `Healing`)

**Damage**

- Korin (84% `Physical` `Max HP-based damage` `True damage`)
- Indris (83% `Physical` `Max HP-based damage` `True damage`)
- Baelran (77% `Physical` `Max HP-based damage` `True damage`)

**Crowd Control**

- Athalia (62% `Knock down`)
- Baelran (60% `Knock down`)
- Sylphira (60% `Knock down` `Interrupt`)

### Summary for Temesia

#### Stats Temesia benefits from

- ATK
- ATK SPD
- Max HP
- Healing
- Energy

#### Damage types dealt by Temesia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Single target — `low`

#### Buffs provided by Temesia

- Healing — Single target — `low`

#### Debuffs provided by Temesia

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `high`
- Knock down — All units — `low`

#### Temesia's Special Effects

#### Temesia Provides

- Stacking buff — Single target

## Thador

### Thador's behavior

- Movement: moving (avg attack range 0.2 tiles)
- Signature skill: Darkmoon Pact — crit + shield for ally behind
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Thador benefits from

Look for units providing: `Max HP` `Crit` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Isabella**
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - Healing (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]

### Units benefitting from Thador

- Nara
- Pandora
- Scarlita

### Units that can act as a replacement for Thador

**Energy provider**

- Phraesto
- Ravion
- Lyca

**Damage**

- Antandra (72% `Physical`)
- Atalanta (72% `Physical`)
- Gerda (72% `Physical`)

**Crowd Control**

- Athalia (60% `Knock down`)
- Baelran (56% `Knock down`)
- Frieren (50% `Knock down`)

### Summary for Thador

#### Stats Thador benefits from

- Max HP
- Crit
- Healing

#### Damage types dealt by Thador

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- DoT — Single target

#### Buffs provided by Thador

- Energy recovery (EX+10) — Single target — `low`

#### Debuffs provided by Thador

- Magic DEF debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Thador

- Knock down — Single target — `high`

## Thoran

### Thoran's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Resurrection — self-revive on defeat
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Thoran benefits from

Look for units providing: `Max HP` `Energy`  
Common buffers are **Lucius**, **Hugin**, or **Ravion**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Gala**
  - Max HP via Shield (single target, high)

### Units that can act as a replacement for Thoran

**Buffs on allies**

- Salazer (60% `Healing` `Life Drain`)
- Viperian (60% `Healing` `Life Drain`)
- Athalia (50% `Healing`)

**Damage**

- Chippy (100% `Physical`)
- Salazer (100% `Physical`)
- Silvina (100% `Physical`)

### Summary for Thoran

#### Stats Thoran benefits from

- Max HP
- Energy

#### Damage types dealt by Thoran

- Primary damage type (unit): **Physical**
- Physical — Self, Single target

#### Buffs provided by Thoran

- Healing — Single target — `medium`
- Lifedrain buff — Single target — `medium` — conditional (frequent)

#### Crowd Control provided by Thoran

- Unaffected — Self — On skill
- Interrupt — Single target — `low`

## Tilaya

### Tilaya's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Wrath of the Wilds (ultimate) — 8-hit greatsword arc slashes
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Tilaya benefits from

Look for units providing: `Max HP` `Healing`  
Common buffers are **Lucius**, **Rowan**, or **Twins**.

- **Hewynn**
  - Healing (all units, high)
- **Lorsan**
  - Healing (all units, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Contess**
  - Max HP via Shield (single target, medium)
  - Healing (multiple targets, high)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - Healing (multiple targets, medium)

### Units that can act as a replacement for Tilaya

**Buffs on allies**

- Granny Dahnie (52% `Healing`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

### Summary for Tilaya

#### Stats Tilaya benefits from

- Max HP
- Healing

#### Damage types dealt by Tilaya

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Buffs provided by Tilaya

- Healing over time — Single target — `medium`
- Healing (Mythic+) — Single target — `medium`
- Max HP buff (EX+10) — Area — `low`

#### Crowd Control provided by Tilaya

- Unaffected — Arc — Start of battle

#### Tilaya's Special Effects

#### Tilaya Provides

- Start-of-battle cast — Arc

## Ulmus

### Ulmus's behavior

- Movement: moving (stationary when rooted)
- Signature skill: Way of the Forest — HP regen + energy when rooted
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Ulmus benefits from

Look for units providing: `Max HP` `Energy`  
Common buffers are **Lucius**, **Hugin**, or **Ravion**.

- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)
- **Gala**
  - Max HP via Shield (single target, high)

### Units that can act as a replacement for Ulmus

**Buffs on allies**

- Salazer (60% `Healing` `Life Drain` `Max HP`)
- Baelran (50% `Healing`)
- Seth (50% `Healing` `Life Drain`)

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Twins (57% `Move`)

### Summary for Ulmus

#### Stats Ulmus benefits from

- Max HP
- Energy

#### Damage types dealt by Ulmus

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Ulmus

- Healing — Single target — `low` — conditional (frequent)
- Healing over time — Single target — `low`
- Shield — Single target — `low`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control provided by Ulmus

- Unaffected — Self — On skill
- Knock down (Mythic+) — Single target — `medium`
- Move (Supreme+) — Area — `low`

#### Ulmus's Special Effects

#### Ulmus Requires

- Vulnerable enemy (Mythic+) — Enemies

## Vala

### Vala's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Swift Shift (ultimate) — mode shift + stun/true damage
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Vala benefits from

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Isabella**
  - Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Evie**
  - ATK buff (multiple targets, high)
  - Healing (multiple targets, high)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Kafra**
  - Healing over time (area, high)
  - Enables Enemy defeat via Marked target (focus fire)
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Enables Enemy defeat via HP threshold strike

### Units that can act as a replacement for Vala

**Buffs on allies**

- Mehira (100% `Haste`)
- Gala (50% `Haste`)

**Damage**

- Faramor (79% `True damage` `Physical` `HP loss`)
- Marilee (53% `True damage` `Physical`)
- Harak (51% `Physical` `HP loss`)

**Crowd Control**

- Lenya (100% `Stun`)
- Walker (100% `Stun`)
- Gunnar (90% `Stun`)

### Summary for Vala

#### Stats Vala benefits from

- ATK
- Haste
- Healing
- Energy

#### Damage types dealt by Vala

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`
- True damage — Single target — `medium`

#### Buffs provided by Vala

- Haste buff (Mythic+) — Single target — `high`

#### Debuffs provided by Vala

- Haste debuff — Single target — `high`
- Marked target (focus fire) — Single target — `medium`

#### Crowd Control provided by Vala

- Stun — Single target — `medium`

#### Vala's Special Effects

#### Vala Provides

- Marked target (focus fire) — Self
- Untargetable (Mythic+) — Multiple targets

#### Vala Requires

- Enemy defeat (Legendary+) — Enemies

## Valen

### Valen's behavior

- Movement: moving (avg attack range 1.4 tiles)
- Signature skill: Thunder Swordwork (ultimate) — multi-hit area + ATK buff
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Valen benefits from

Look for units providing: `ATK`  
Common buffers are **Lyca**, **Ravion**, or **Mikola**.

- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]

### Units that can act as a replacement for Valen

**Damage**

- Antandra (100% `Physical`)
- Atalanta (100% `Physical`)
- Gerda (100% `Physical`)

**Crowd Control**

- Damian (100% `Stun`)
- Ludovic (100% `Stun`)
- Nazrik (100% `Stun`)

### Summary for Valen

#### Stats Valen benefits from

- ATK

#### Damage types dealt by Valen

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Valen

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `medium`

#### Valen's Special Effects

#### Valen Provides

- Invincibility — Area
- Stacking buff (Mythic+) — Single target

## Valka

### Valka's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Blooming Terror (ultimate) — stack fear + consume enemy
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Valka benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Enables Adjacent allies via Multiple ally buffs
- **Himmel**
  - Max HP buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Lorsan**
  - Enables Adjacent allies via Multiple ally buffs
- **Saida**
  - Max HP via Shield (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Isabella**
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Enables Adjacent allies via Multiple ally buffs

### Units benefitting from Valka

- Lyca

### Units that can act as a replacement for Valka

**Buffs on allies**

- Lyca (50% `ATK SPD`)

**Damage**

- Himmel (93% `Physical` `Max HP-based damage`)
- Granny Dahnie (90% `Physical` `Max HP-based damage`)
- Lumont (90% `Physical` `Max HP-based damage`)

**Crowd Control**

- Natsu (70% `Stun` `Knock down`)
- Zorya (66% `Knock down` `Stun`)
- Callan (60% `Knock down` `Stun`)

### Summary for Valka

#### Stats Valka benefits from

- ATK SPD
- Haste
- Max HP
- Energy

#### Damage types dealt by Valka

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area, Single target — `low`

#### Buffs provided by Valka

- ATK SPD buff — Multiple targets — `high`
- Healing — Single target — `low`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control provided by Valka

- Unaffected — Self — On skill
- Knock down — Area — `low`
- Stun — Area — `low`

#### Valka's Special Effects

#### Valka Requires

- Adjacent allies — Allies

## Velara

### Velara's behavior

- Movement: stationary (no finite attack range)
- Signature skill: Ruthless Rite (ultimate) — transfer enemy stats to allies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Velara benefits from

Look for units providing: `Haste` `Max HP` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Callan**
  - Max HP via Shield (multiple targets, medium)

### Units that can act as a replacement for Velara

**Buffs on allies**

- Nara (72% `Healing`)
- Berial (66% `Healing`)
- Athalia (54% `Healing`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

**Crowd Control**

- Cecia (100% `Pin`)
- Korin (100% `Pin`)
- Gala (66% `Pin`)

### Summary for Velara

#### Stats Velara benefits from

- Haste
- Max HP
- Energy

#### Damage types dealt by Velara

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Velara

- Haste buff — Single target — `low`
- Healing — Area — `low`

#### Debuffs provided by Velara

- Haste debuff — Single target — `medium`

#### Crowd Control provided by Velara

- Pin — Single target — `high`

#### Velara's Special Effects

#### Velara Provides

- Start-of-battle cast — All units

#### Velara Requires

- Boss encounter — Allies

## Viperian

### Viperian's behavior

- Movement: mostly stationary (avg attack range 5.0 tiles)
- Signature skill: Crimson Waltz — AoE burst damage to all enemies
- Signature skill speed: slow
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Viperian benefits from

Look for units providing: `Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Shakir**
  - Haste buff (multiple targets, low) [signature fuel]
  - ATK SPD via Haste buff (multiple targets, low) [signature fuel]

### Units that can act as a replacement for Viperian

**Buffs on allies**

- Berial (75% `Healing`)
- Nara (66% `Healing`)
- Salazer (60% `Healing` `Life Drain`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Damian (100% `Magic`)

### Summary for Viperian

#### Stats Viperian benefits from

- Haste

#### Damage types dealt by Viperian

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Viperian

- Healing — Single target — `high`
- Lifedrain buff (EX+5) — Single target — `low`

#### Debuffs provided by Viperian

- Energy drain — Single target — `low`

#### Crowd Control provided by Viperian

- Unaffected — Self — Start of battle

## Walker

### Walker's behavior

- Movement: moving (avg attack range 2.0 tiles)
- Signature skill: Six-Shot (ultimate) — multi-target burst shots
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Walker benefits from

Look for units providing: `Max HP` `Crit` `Crit DMG Boost` `Life Drain`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Zandrok**
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, low)
  - ATK SPD buff (single target, low) [signature fuel]
- **Kordan**
  - Lifedrain buff (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Walker

**Buffs on allies**

- Kruger (88% `Life Drain`)
- Brutus (66% `Life Drain`)

**Damage**

- Niru (70% `HP loss` `Max HP-based damage`)
- Dunlingr (67% `HP loss`)
- Granny Dahnie (61% `Physical` `Max HP-based damage`)

**Crowd Control**

- Lenya (100% `Stun`)
- Vala (100% `Stun`)
- Gunnar (90% `Stun`)

### Summary for Walker

#### Stats Walker benefits from

- Max HP
- Crit
- Crit DMG Boost
- Life Drain

#### Damage types dealt by Walker

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

#### Buffs provided by Walker

- Lifedrain buff (Supreme+) — Single target — `high`

#### Debuffs provided by Walker

- Crit Resist debuff (EX+5) — Single target — `low`

#### Crowd Control provided by Walker

- Stun — Single target — `medium`

## Zandrok

### Zandrok's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Rallying Roar — destroy obstacles + inspire allies
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Zandrok benefits from

Look for units providing: `Haste` `Max HP`  
Common buffers are **Twins**, **Hugin**, or **Lucius**.

- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Hepler**
  - Haste buff (single target, low) [signature fuel]
  - Max HP via Shield (multiple targets, medium)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Units benefitting from Zandrok

**17** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Nerion
- Carolina
- Mehira
- Seth
- Zorya
- Aurora
- Mikola
- Natsu
- Twins
- Viperian

### Units that can act as a replacement for Zandrok

**Damage**

- Shemira (85% `Max HP-based damage`)
- Florabelle (85% `Max HP-based damage` `Physical`)
- Hodgkin (85% `Max HP-based damage` `Physical`)

**Crowd Control**

- Perseus (100% `Stun`)
- Lucca (80% `Stun`)
- Lorsan (75% `Stun`)

### Summary for Zandrok

#### Stats Zandrok benefits from

- Haste
- Max HP

#### Damage types dealt by Zandrok

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- Max HP-based damage — Area, Multiple targets, Single target — `high`

#### Buffs provided by Zandrok

- Haste buff — Area — `medium` — conditional (frequent)
- Lifedrain buff — Area — `medium` — conditional (frequent)

#### Crowd Control provided by Zandrok

- Stun — Area — `high`

## Zanie

### Zanie's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Vein Pulse (ultimate) — deploy turrets at battle start
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Zanie benefits from

Look for units providing: `ATK SPD / Haste`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Zanie

**Damage**

- Alna (55% `DoT` `Physical`)

**Crowd Control**

- Bonnie (100% `Stun`)
- Lyca (100% `Stun`)
- Marilee (100% `Stun`)

### Summary for Zanie

#### Stats Zanie benefits from

- ATK SPD

#### Damage types dealt by Zanie

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- DoT — Area

#### Buffs provided by Zanie

- Healing — Single target — `high`
- Shield — Single target — `high`
- DEF Penetration buff (Legendary+) — Single target — `medium`
- Max HP buff (Mythic+) — Single target — `medium`

#### Debuffs provided by Zanie

- ATK debuff (Supreme+) — Single target — `low`
- DoT (Supreme+) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Zanie

- Stun — Single target — `low`

#### Zanie's Special Effects

#### Zanie Provides

- Summoning — Self

## Zorya

### Zorya's behavior

- Movement: moving (inactive while dormant)
- Signature skill: Circle of Vigil (ultimate) — dormant cycle + AoE jump
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Zorya benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Energy` `Life Drain`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, medium, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Contess**
  - Max HP via Shield (single target, medium)
  - Healing (multiple targets, high)
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Isabella**
  - Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
  - Healing (area, high)
  - ATK SPD via Haste buff (multiple targets, low, conditional (frequent)) [signature fuel]
- **Smokey & Meerky**
  - Healing over time (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)

### Units that can act as a replacement for Zorya

**Buffs on allies**

- Baelran (50% `Healing`)
- Bryon (50% `Healing`)
- Soren (50% `Healing`)

**Damage**

- Talene (93% `HP loss` `Magic`)
- Aliceth (71% `HP loss`)
- Harak (67% `HP loss`)

**Crowd Control**

- Perseus (66% `Stun`)
- Valka (66% `Knock down` `Stun`)
- Zandrok (66% `Stun`)

### Summary for Zorya

#### Stats Zorya benefits from

- Haste
- Max HP
- Healing
- Energy
- Life Drain

#### Damage types dealt by Zorya

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- HP loss — Area — `high`

#### Buffs provided by Zorya

- Healing over time — Single target — `low`

#### Crowd Control provided by Zorya

- Steadfast — Self — Start of battle
- Unaffected (EX+10) — Single target — On skill
- Knock down — Arc — `medium`
- Stun — Area — `medium`

#### Zorya's Special Effects

#### Zorya Provides

- Invincibility — Area

#### Zorya Requires

- Ally Ultimate casts (Mythic+) — Allies
