# Heroes Overview

Per-hero synergy picks and summaries derived from skill text in
[Heroes.md](Heroes.md). [Heroes.md](Heroes.md) has skills only.
Synergy: stat buff tags under **Units X benefits from**, and
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
Common buffers are **Lyca**, **Ravion**, or **Evie**.

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
- **Koko**
  - Enables Debuff on target via Damage taken debuff (area)

### Units that can act as a replacement for Aliceth

**Similar Skills**

- Nazrik (50% `hp-scaling` `mark-target`)

**Damage**

- Faramor (100% `Physical` `HP loss`)
- Kordan (89% `Physical` `HP loss`)
- Ravion (89% `Physical` `HP loss`)

**Crowd Control**

- Alsa (100% `Move` `Stun`)
- Atalanta (100% `Move` `Stun`)
- Cassadee (100% `Move` `Stun`)

### Summary for Aliceth

#### Damage types dealt by Aliceth

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`

#### Buffs provided by Aliceth

- Ally empower buff — Single target — `low`
- Attack range buff — Single target — `low`
- DEF Penetration buff — Multiple targets — `medium`
- ATK buff (Legendary+) — Multiple targets — `medium`
- Fatal blow immunity (Mythic+) — Single target — `high` — conditional (rare)
- Healing (Mythic+) — Single target — `low`

#### Debuffs provided by Aliceth

- Execution debuff — Multiple targets — `medium`
- Marked target (focus fire) — Single target — `medium`
- Blind HP loss debuff (EX+15) — Area — `low`

#### Crowd Control provided by Aliceth

- Move — Single target — `low`
- Stun — Single target — `low`

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

Look for units providing: `Max HP` `Healing`  
Common buffers are **Lorsan**, **Evie**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units benefitting from Alna

- Shadewing
- Aliceth

### Units that can act as a replacement for Alna

**Similar Skills**

- Cryonaia (75% `battlefield-modification` `cc-immunity` `invincibility`)

**Damage**

- Gunnar (90% `Physical` `DoT`)
- Brutus (80% `DoT` `Physical`)
- Cecia (70% `Physical` `DoT`)

**Debuffs on enemies**

- Hepler (75% `Haste debuff`)
- Natsu (75% `Haste debuff`)

**Crowd Control**

- Carolina (100% `Freeze`)

### Summary for Alna

#### Damage types dealt by Alna

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Self, Single target
- DoT — All units

#### Buffs provided by Alna

- Ally empower buff — Single target — `low`
- Max HP buff — Single target — `low`
- Damage and control immunity (EX+15) — Single target — `high`
- ATK buff (Supreme+) — Single target — `medium`

#### Debuffs provided by Alna

- Haste debuff — Arc — `high`
- Vitality debuff (Supreme+) — Area — `low`

#### Crowd Control provided by Alna

- Freeze (Supreme+) — Area — `medium`

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
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Alsa

**Similar Skills**

- Athalia (50% `self-repositioner` `transformation`)
- Kulu (50% `battlefield-modification` `self-repositioner`)

**Damage**

- Cassadee (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Kulu (59% `Movement speed debuff`)

**Crowd Control**

- Perseus (100% `Stun` `Move`)
- Scarlita (100% `Stun` `Move`)
- Soren (91% `Stun` `Move`)

### Summary for Alsa

#### Damage types dealt by Alsa

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Debuffs provided by Alsa

- Movement speed debuff — Area — `medium`
- Energy drain (EX+5) — Single target — `low`
- Magic DEF debuff (EX+5) — Area — `low`

#### Crowd Control provided by Alsa

- Immune — Area — Once
- Move — Single target — `low`
- Stun — Single target — `high`

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

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)

### Units benefitting from Antandra

**11** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Alna
- Callan
- Contess
- Evie
- Gerda
- Igor
- Phraesto
- Reinier
- Saida
- Tilaya

### Units that can act as a replacement for Antandra

**Buffs on allies**

- Evie (100% `Healing`)
- Fay (100% `Healing`)
- Hewynn (100% `Healing`)

**Similar Skills**

- Lucca (50% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Atalanta (100% `Physical`)

**Crowd Control**

- Lumont (57% `Stun` `Taunt`)
- Hepler (52% `Taunt` `Stun`)

### Summary for Antandra

#### Damage types dealt by Antandra

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target

#### Buffs provided by Antandra

- Healing — Multiple targets — `high`

#### Crowd Control provided by Antandra

- Unaffected — Area — On Skill
- Knock down — Area — `medium`
- Stun — Area — `medium`
- Taunt — Area — `high`

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

- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
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

### Units that can act as a replacement for Arden

**Similar Skills**

- Lorsan (100% `aoe-damage` `dot-specialist`)
- Faramor (66% `aoe-damage` `dot-specialist`)
- Viperian (66% `aoe-damage` `dot-specialist`)

**Damage**

- Berial (100% `Magic` `DoT`)
- Bryon (100% `Magic` `DoT`)
- Cryonaia (100% `Magic` `DoT`)

**Crowd Control**

- Gwyneth (100% `Pin`)
- Indris (100% `Pin`)
- Kordan (100% `Pin`)

### Summary for Arden

#### Damage types dealt by Arden

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Multiple targets

#### Crowd Control provided by Arden

- Pin — Single target — `high`

## Atalanta

### Atalanta's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Wild Sniper (ultimate) — dash + line stun shot
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Atalanta benefits from

Look for units providing: `Haste` `Healing` `Physical DEF`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Rowan**
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Atalanta

**Similar Skills**

- Zandrok (66% `aoe-damage` `battle-start-burst`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Lyca (100% `Phys DEF debuff`)
- Ravion (100% `Phys DEF debuff`)
- Sinbad (100% `Phys DEF debuff`)

**Crowd Control**

- Cassadee (75% `Move` `Stun`)
- Lenya (75% `Move` `Stun`)
- Perseus (75% `Move` `Stun`)

### Summary for Atalanta

#### Damage types dealt by Atalanta

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Debuffs provided by Atalanta

- Phys DEF debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Atalanta

- Move — Single target — `high`
- Pin — Single target — `medium`
- Stun — Single target — `medium`

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

Look for units providing: `Max HP` `CRIT` `Execution` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Antandra**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Athalia

**Similar Skills**

- Baelran (66% `hp-scaling` `transformation`)
- Kordan (66% `hp-scaling` `self-repositioner`)
- Pippa (66% `hp-scaling` `self-repositioner`)

**Damage**

- Dionel (100% `True damage` `Physical`)
- Baelran (97% `True damage` `Physical`)
- Indris (95% `True damage` `Physical`)

**Debuffs on enemies**

- Lucius (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)
- Sinbad (90% `ATK debuff`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Baelran (100% `Knock down`)
- Ravion (100% `Knock down`)

### Summary for Athalia

#### Damage types dealt by Athalia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- True damage — All units, Single target — `medium`

#### Buffs provided by Athalia

- Crit buff (Legendary+) — Single target — `low`

#### Debuffs provided by Athalia

- ATK debuff — All units — `medium`

#### Crowd Control provided by Athalia

- Unaffected — Area — On Skill
- Knock down — All units — `low`

#### Athalia Provides

- Invincibility — Self
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
- Florabelle
- Gala
- Phraesto
- Zanie

### Units that can act as a replacement for Aurora

**Buffs on allies**

- Gunnar (100% `Invincible`)
- Pandora (100% `Invincible`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Berial (100% `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Bryon (100% `Haste debuff`)
- Carolina (100% `Haste debuff`)

**Crowd Control**

- Tasi (100% `Sleep`)

### Summary for Aurora

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

- Unaffected — Self — Conditional
- Sleep — Single target — `high`

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

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Evie**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Baelran

**Similar Skills**

- Athalia (66% `hp-scaling` `transformation`)
- Silven (50% `hp-scaling`)
- Tilaya (50% `hp-scaling`)

**Damage**

- Dionel (100% `True damage` `Physical`)
- Athalia (95% `True damage` `Physical`)
- Indris (93% `True damage` `Physical`)

**Debuffs on enemies**

- Contess (100% `Max HP debuff`)
- Natsu (100% `Max HP debuff`)
- Nazrik (100% `Max HP debuff`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Ravion (100% `Knock down`)
- Sylphira (100% `Knock down`)

### Summary for Baelran

#### Damage types dealt by Baelran

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- True damage — Arc, Area, Single target — `high`

#### Debuffs provided by Baelran

- Max HP debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Baelran

- Unaffected — Self — Start of Battle
- Knock down — Area — `medium`

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

Look for units providing: `Healing`  
Common buffers are **Lyca**, **Mikola**, or **Lorsan**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Berial

**Damage**

- Bryon (100% `DoT` `Magic`)
- Cryonaia (100% `DoT` `Magic`)
- Daimon (100% `DoT` `Magic`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `Damage taken debuff`)
- Contess (66% `Energy drain`)
- Dunlingr (66% `Energy drain`)

### Summary for Berial

#### Damage types dealt by Berial

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- DoT — Area

#### Debuffs provided by Berial

- Damage taken debuff (Legendary+) — Single target — `low`
- Energy drain (Mythic+) — Single target — `medium`

#### Crowd Control provided by Berial

- Frighten — Area — `medium`

#### Berial Provides

- Invincibility — Self
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
Common buffers are **Evie**, **Lyca**, or **Ravion**.

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
- **Pippa**
  - Enables Debuff on target via Energy drain (area)
  - Enables Magic damage from allies via Magic damage + wide area (area)

### Units that can act as a replacement for Bonnie

**Damage**

- Arden (100% `Magic` `DoT`)
- Berial (100% `Magic` `DoT`)
- Bryon (100% `Magic` `DoT`)

**Debuffs on enemies**

- Pandora (100% `ATK debuff` `Damage taken debuff` `Haste debuff`)
- Granny Dahnie (75% `ATK debuff` `Haste debuff`)
- Kafra (75% `ATK debuff` `Haste debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Alsa (100% `Stun`)
- Antandra (100% `Stun`)

### Summary for Bonnie

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

#### Bonnie Provides

- Invincibility — Self
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
Common buffers are **Lyca**, **Twins**, or **Ravion**.

- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Zandrok**
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Kordan**
  - Lifedrain buff (multiple targets, high)
- **Dunlingr**
  - Lifedrain buff (all units, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]

### Units that can act as a replacement for Brutus

**Buffs on allies**

- Cecia (100% `Life Drain`)
- Daimon (100% `Life Drain`)
- Dunlingr (100% `Life Drain`)

**Similar Skills**

- Granny Dahnie (66% `hp-scaling` `taunt`)
- Zorya (66% `hp-scaling` `life-drain`)
- Salazer (50% `hp-scaling` `life-drain`)

**Damage**

- Gunnar (100% `Max HP-based damage` `DoT` `Physical`)
- Daimon (90% `Max HP-based damage` `DoT`)
- Satrana (90% `Max HP-based damage` `DoT`)

**Debuffs on enemies**

- Evie (66% `DoT`)
- Frieren (66% `DoT`)

**Crowd Control**

- Antandra (100% `Taunt`)
- Hepler (100% `Taunt`)
- Lumont (100% `Taunt`)

### Summary for Brutus

#### Damage types dealt by Brutus

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Arc — `high`

#### Buffs provided by Brutus

- Lifedrain buff — Single target — `medium`

#### Debuffs provided by Brutus

- DoT — Area — `medium`
- Phys DEF debuff — Area — `low`

#### Crowd Control provided by Brutus

- Unaffected — Self — On Skill
- Taunt — Area — `high`

## Bryon

### Bryon's behavior

- Movement: stationary (summon moves)
- Signature skill: Falcon Raid (ultimate) — falcon area dive damage
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: slow

### Units Bryon benefits from

Look for units providing: `Haste` `Healing`  
Common buffers are **Mikola**, **Twins**, or **Lorsan**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Bryon

**Similar Skills**

- Dunlingr (50% `battle-start-burst` `summoner`)

**Damage**

- Berial (100% `DoT` `Magic`)
- Cryonaia (100% `DoT` `Magic`)
- Daimon (100% `DoT` `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Carolina (100% `Haste debuff`)
- Eironn (100% `Haste debuff`)

**Crowd Control**

- Gerda (100% `Stun` `Interrupt`)
- Lucca (100% `Stun` `Interrupt`)
- Alsa (66% `Stun`)

### Summary for Bryon

#### Damage types dealt by Bryon

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- DoT — Area

#### Debuffs provided by Bryon

- Haste debuff — Area — `low`

#### Crowd Control provided by Bryon

- Interrupt — Single target — `low`
- Stun (Mythic+) — Single target — `medium`

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
Common buffers are **Lorsan**, **Evie**, or **Mikola**.

- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)
- **Ludovic**
  - Healing (area, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))

### Units benefitting from Callan

- Daimon
- Eironn
- Thoran

### Units that can act as a replacement for Callan

**Buffs on allies**

- Hepler (100% `Max HP`)
- Hugin (100% `Max HP`)
- Lucius (100% `Max HP`)

**Damage**

- Alna (62% `Physical`)
- Athalia (62% `Physical`)
- Dionel (62% `Physical`)

**Crowd Control**

- Antandra (68% `Knock down` `Stun`)
- Lucca (68% `Knock down` `Stun`)
- Zorya (68% `Knock down` `Stun`)

### Summary for Callan

#### Damage types dealt by Callan

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- Magic — Multiple targets

#### Buffs provided by Callan

- Shield — Multiple targets — `medium`

#### Crowd Control provided by Callan

- Unaffected — Self — Once
- Knock down — All units — `low`
- Pin — Multiple targets — `low`
- Stun (Mythic+) — Single target — `low`

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

Look for units providing: `CRIT`  
Common buffers are **Ravion**, **Lyca**, or **Lorsan**.

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

**Similar Skills**

- Kruger (50% `enemy-debuffer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Eironn (100% `Haste debuff` `Magic DEF debuff`)
- Alna (50% `Haste debuff`)
- Alsa (50% `Magic DEF debuff`)

### Summary for Carolina

#### Damage types dealt by Carolina

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- DoT — Self

#### Debuffs provided by Carolina

- Haste debuff — Area — `low`
- Magic DEF debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Carolina

- Freeze — Single target — `high`

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
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Units that can act as a replacement for Cassadee

**Similar Skills**

- Parisa (50% `ally-buffer` `aoe-damage`)
- Temesia (50% `aoe-damage` `enemy-debuffer`)

**Damage**

- Alsa (100% `Magic`)
- Contess (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Alsa (100% `Magic DEF debuff`)
- Carolina (100% `Magic DEF debuff`)
- Eironn (100% `Magic DEF debuff`)

**Crowd Control**

- Scarlita (84% `Move` `Knock up` `Stun`)
- Lenya (63% `Move` `Stun`)
- Perseus (63% `Move` `Stun`)

### Summary for Cassadee

#### Damage types dealt by Cassadee

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Debuffs provided by Cassadee

- Magic DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Cassadee

- Knock up — Single target — `high`
- Move — All units — `low`
- Stun — Single target — `high`

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
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Rowan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
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

### Units that can act as a replacement for Cecia

**Buffs on allies**

- Kordan (53% `Life Drain` `DEF Penetration`)

**Similar Skills**

- Viperian (50% `dot-specialist` `life-drain`)

**Damage**

- Alna (100% `Physical` `DoT`)
- Brutus (100% `Physical` `DoT`)
- Gunnar (100% `Physical` `DoT`)

**Debuffs on enemies**

- Cryonaia (100% `Damage taken debuff`)
- Indris (100% `Damage taken debuff`)
- Koko (100% `Damage taken debuff`)

**Crowd Control**

- Arden (100% `Pin`)
- Callan (100% `Pin`)
- Eironn (100% `Pin`)

### Summary for Cecia

#### Damage types dealt by Cecia

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target
- DoT — Arc, Single target

#### Buffs provided by Cecia

- ATK SPD buff — Single target — `medium`
- DEF Penetration buff — Single target — `medium`
- Lifedrain buff — Area — `low`
- Max HP buff — Single target — `high`

#### Debuffs provided by Cecia

- Damage taken debuff (EX+10) — Single target — `medium`

#### Crowd Control provided by Cecia

- Pin — Single target — `high`

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

- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Thador**
  - Energy recovery (lieutenant, start of battle) [signature fuel]

### Units that can act as a replacement for Chippy

**Similar Skills**

- Florabelle (100% `summoner`)
- Zanie (100% `summoner`)
- Damian (50% `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

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
Common buffers are **Lorsan**, **Evie**, or **Mikola**.

- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)
- **Smokey & Meerky**
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Ludovic**
  - Healing (area, medium)

### Units that can act as a replacement for Contess

**Buffs on allies**

- Hugin (100% `ATK` `Max HP`)
- Evie (60% `ATK`)
- Himmel (60% `ATK` `Max HP`)

**Similar Skills**

- Lucius (50% `ally-healer` `ally-shielder`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Cryonaia (100% `Magic`)

**Debuffs on enemies**

- Sylphira (80% `Energy drain` `Max HP debuff`)
- Dunlingr (60% `Energy drain` `ATK debuff`)
- Sinbad (60% `Energy drain` `ATK debuff`)

**Crowd Control**

- Gwyneth (100% `Silence` `Stun`)
- Alsa (50% `Stun`)
- Antandra (50% `Stun`)

### Summary for Contess

#### Damage types dealt by Contess

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets

#### Buffs provided by Contess

- ATK buff — Single target — `high`
- Shield — Single target — `medium`

#### Debuffs provided by Contess

- Energy drain — Single target — `low`
- Max HP debuff — Multiple targets — `low`
- ATK debuff (Legendary+) — Single target — `low`

#### Crowd Control provided by Contess

- Silence (Mythic+) — Single target — `medium`
- Stun (Supreme+) — Single target — `medium`

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

- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Cryonaia

**Similar Skills**

- Alna (75% `battlefield-modification` `cc-immunity` `invincibility`)

**Damage**

- Frieren (100% `DoT` `Magic`)
- Tasi (100% `DoT` `Magic`)
- Lorsan (90% `Magic` `DoT`)

**Debuffs on enemies**

- Koko (100% `Damage taken debuff`)
- Kruger (100% `Damage taken debuff`)
- Kulu (100% `Damage taken debuff`)

### Summary for Cryonaia

#### Damage types dealt by Cryonaia

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units

#### Debuffs provided by Cryonaia

- Damage taken debuff (EX+5) — Single target — `high`

#### Crowd Control provided by Cryonaia

- Immune — Self — Conditional
- Freeze (EX+15) — Self — `low`

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

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Cyran

**Damage**

- Frieren (100% `True damage` `Magic`)
- Pippa (93% `True damage` `Magic`)
- Athalia (86% `True damage`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Lucius (100% `ATK debuff`)
- Lyca (100% `ATK debuff`)

**Crowd Control**

- Contess (100% `Silence`)
- Dunlingr (100% `Silence`)
- Evie (100% `Silence`)

### Summary for Cyran

#### Damage types dealt by Cyran

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- True damage — All units — `medium`

#### Debuffs provided by Cyran

- ATK debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Cyran

- Steadfast — Area — Conditional
- Unaffected — Self — Conditional
- Pin — Area — `high`
- Silence (EX+10) — Single target — `low`

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
Common buffers are **Hugin**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Units that can act as a replacement for Daimon

**Buffs on allies**

- Koko (100% `Life Drain` `Max HP`)
- Brutus (50% `Life Drain`)
- Callan (50% `Max HP`)

**Similar Skills**

- Shemira (60% `hp-scaling` `life-drain` `summoner`)
- Koko (50% `ally-shielder` `life-drain`)
- Korin (50% `ally-shielder` `hp-scaling`)

**Damage**

- Satrana (100% `Max HP-based damage` `DoT` `Magic`)
- Shadewing (94% `Max HP-based damage` `Magic` `DoT`)
- Gunnar (91% `Max HP-based damage` `DoT`)

**Crowd Control**

- Berial (100% `Frighten`)
- Silvina (100% `Frighten`)

### Summary for Daimon

#### Damage types dealt by Daimon

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target
- DoT — Area
- Max HP-based damage — Area — `high`

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

Look for units providing: `ATK` `Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Evie**, or **Hugin**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)

### Units benefitting from Damian

**40** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Alsa
- Atalanta
- Aurora
- Cassadee
- Frieren
- Hepler
- Koko
- Lenya
- Lumont
- Mehira

### Units that can act as a replacement for Damian

**Buffs on allies**

- Hugin (100% `Haste`)
- Mikola (100% `Haste`)
- Twins (100% `Haste`)

**Similar Skills**

- Laios (66% `ally-healer` `summoner`)
- Chippy (50% `summoner`)
- Florabelle (50% `summoner`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Atalanta (100% `Stun`)

### Summary for Damian

#### Damage types dealt by Damian

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Damian

- Haste buff (Mythic+) — Multiple targets — `high` — conditional (frequent)

#### Crowd Control provided by Damian

- Stun — Single target — `medium`

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

- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Lucius**
  - Max HP via Shield (area, high)

### Units that can act as a replacement for Dionel

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Cecia (66% `DEF Penetration`)
- Kordan (66% `DEF Penetration`)

**Damage**

- Baelran (93% `True damage` `Physical`)
- Athalia (91% `True damage` `Physical`)
- Frieren (89% `True damage`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Faramor (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)

**Crowd Control**

- Florabelle (100% `Knock up`)
- Lucca (100% `Knock up`)
- Scarlita (100% `Knock up`)

### Summary for Dionel

#### Damage types dealt by Dionel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- True damage — All units, Single target — `high`

#### Buffs provided by Dionel

- DEF Penetration buff — Single target — `high`

#### Debuffs provided by Dionel

- Vitality debuff (EX+10) — Single target — `low`

#### Crowd Control provided by Dionel

- Knock up — Area — `low`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))

### Units that can act as a replacement for Dunlingr

**Buffs on allies**

- Valka (50% `ATK SPD` `Life Drain`)

**Similar Skills**

- Bryon (50% `battle-start-burst` `summoner`)
- Chippy (50% `summoner`)
- Florabelle (50% `summoner`)

**Damage**

- Talene (100% `HP loss` `Magic`)
- Zorya (96% `HP loss` `Magic`)
- Niru (84% `Magic` `HP loss`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `ATK debuff`)
- Pandora (61% `ATK debuff` `Energy drain`)
- Lily May (55% `Energy drain`)

**Crowd Control**

- Evie (100% `Silence`)
- Sylphira (80% `Silence`)
- Gwyneth (53% `Silence`)

### Summary for Dunlingr

#### Damage types dealt by Dunlingr

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target
- HP loss — Area — `medium`

#### Buffs provided by Dunlingr

- ATK buff (EX+5) — Single target — `low`
- Haste buff (EX+15) — Single target — `low`
- ATK SPD buff (Supreme+) — All units — `low`
- Lifedrain buff (Supreme+) — All units — `low`

#### Debuffs provided by Dunlingr

- ATK debuff — Area — `low`
- Energy drain (Supreme+) — All units — `low`

#### Crowd Control provided by Dunlingr

- Silence — All units — `low`

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
Common buffers are **Hugin**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Rowan**
  - Max HP buff (single target, high)
  - DEF buff (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)

### Units that can act as a replacement for Eironn

**Buffs on allies**

- Lorsan (66% `Dodge chance buff`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Carolina (53% `Haste debuff` `Magic DEF debuff`)

**Crowd Control**

- Indris (100% `Move` `Pin`)
- Evie (96% `Move` `Pin`)
- Kordan (86% `Pin` `Move`)

### Summary for Eironn

#### Damage types dealt by Eironn

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target

#### Buffs provided by Eironn

- Dodge chance buff — Single target — `high`

#### Debuffs provided by Eironn

- Haste debuff — Arc — `medium`
- Magic DEF debuff — Single target — `high`

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

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Mikola**, **Hugin**, or **Damian**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Twins

**84** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Valka
- Alsa
- Hepler
- Lenya
- Lumont
- Mehira
- Soren
- Tasi

### Units that can act as a replacement for Twins

**Similar Skills**

- Hugin (66% `ally-shielder` `energy-provider`)
- Lucius (66% `ally-healer` `ally-shielder`)
- Rowan (66% `ally-healer` `energy-provider`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Crowd Control**

- Atalanta (100% `Move`)
- Cassadee (100% `Move`)
- Eironn (100% `Move`)

### Summary for Twins

#### Damage types dealt by Twins

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Twins

- Haste buff — All units — `high`
- Max HP buff — Multiple targets — `high`
- Shield — Single target — `medium`
- Vitality buff (Mythic+) — Multiple targets — `low`

#### Crowd Control provided by Twins

- Unaffected — Area — On Skill
- Move — Area — `low`

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
Common buffers are **Lorsan**, **Mikola**, or **Ravion**.

- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)
- **Smokey & Meerky**
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Ludovic**
  - Healing (area, medium)

### Units benefitting from Evie

**23** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Bonnie
- Shadewing
- Aliceth
- Baelran
- Damian
- Hammie
- Hepler
- Hodgkin
- Isabella
- Kafra

### Units that can act as a replacement for Evie

**Buffs on allies**

- Mikola (83% `Healing` `ATK`)
- Fay (66% `Healing` `ATK`)
- Antandra (50% `Healing`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Frieren (100% `DoT`)
- Brutus (80% `DoT`)

**Crowd Control**

- Indris (76% `Move` `Pin` `Silence`)
- Eironn (63% `Move` `Pin`)
- Kordan (60% `Pin` `Move`)

### Summary for Evie

#### Damage types dealt by Evie

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Evie

- ATK buff — Multiple targets — `high`
- Healing — Multiple targets — `high`

#### Debuffs provided by Evie

- DoT — All units — `medium`

#### Crowd Control provided by Evie

- Move — All units — `low`
- Pin — All units — `low`
- Silence — All units — `low`

#### Evie Provides

- Invincibility — Self
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
- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Faramor

**Similar Skills**

- Arden (66% `aoe-damage` `dot-specialist`)
- Lorsan (66% `aoe-damage` `dot-specialist`)
- Satrana (50% `dot-specialist` `hp-scaling`)

**Damage**

- Vala (79% `True damage` `Physical` `HP loss`)
- Shadewing (71% `HP loss` `True damage`)
- Athalia (57% `True damage` `Physical`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Dionel (100% `Vitality debuff`)
- Frieren (100% `Vitality debuff`)

**Crowd Control**

- Antandra (100% `Stun`)
- Koko (100% `Stun`)
- Lorsan (100% `Stun`)

### Summary for Faramor

#### Damage types dealt by Faramor

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target
- HP loss — Single target — `high`
- True damage — Multiple targets — `medium`

#### Debuffs provided by Faramor

- Vitality debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Faramor

- Stun — Area — `medium`

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
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Fay

- Granny Dahnie
- Niru
- Lucca
- Solise
- Smokey & Meerky

### Units that can act as a replacement for Fay

**Buffs on allies**

- Mikola (69% `Healing` `ATK` `Vitality buff`)
- Evie (61% `Healing` `ATK`)
- Koko (53% `Healing` `Vitality buff`)

**Similar Skills**

- Hewynn (100% `ally-healer` `aoe-healing`)
- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Sinbad (100% `Magic DEF debuff` `Phys DEF debuff`)
- Alsa (50% `Magic DEF debuff`)
- Atalanta (50% `Phys DEF debuff`)

### Summary for Fay

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

- Dunlingr
- Laios
- Mehira
- Bryon
- Gala
- Phraesto
- Zanie

### Units that can act as a replacement for Florabelle

**Similar Skills**

- Chippy (100% `summoner`)
- Zanie (100% `summoner`)
- Damian (50% `summoner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Dionel (100% `Knock up`)
- Lucca (100% `Knock up`)
- Scarlita (100% `Knock up`)

### Summary for Florabelle

#### Damage types dealt by Florabelle

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Florabelle

- Lifedrain buff — Summons only — `high` — conditional (frequent)
- Shield (Mythic+) — Summons only — `medium`
- Haste buff (EX+10) — Summons only — `medium` — conditional (frequent)
- Summon damage buff (Supreme+) — Summons only — `medium`

#### Crowd Control provided by Florabelle

- Immune (Supreme+) — Self — Form
- Knock up — Area — `low`

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
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Frieren

- Bonnie

### Units that can act as a replacement for Frieren

**Similar Skills**

- Arden (50% `aoe-damage` `dot-specialist`)
- Lorsan (50% `aoe-damage` `dot-specialist`)

**Damage**

- Cyran (85% `True damage` `Magic`)
- Dionel (83% `True damage`)
- Pippa (81% `True damage` `Magic`)

**Debuffs on enemies**

- Evie (74% `DoT`)
- Brutus (59% `DoT`)

**Crowd Control**

- Antandra (100% `Knock down` `Stun`)
- Callan (100% `Knock down` `Stun`)
- Lucca (100% `Knock down` `Stun`)

### Summary for Frieren

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
- Sonja
- Velara
- Zandrok
- Silvina

### Units that can act as a replacement for Gala

**Buffs on allies**

- Hugin (100% `Haste` `Max HP`)
- Twins (83% `Haste` `Max HP`)
- Hepler (66% `Max HP` `Haste`)

**Similar Skills**

- Lucca (50% `ally-shielder`)
- Phraesto (50% `ally-shielder` `clone`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Crowd Control**

- Arden (100% `Pin`)
- Atalanta (100% `Pin`)
- Callan (100% `Pin`)

### Summary for Gala

#### Damage types dealt by Gala

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Gala

- Haste buff — Single target — `high`
- Shield — Single target — `high`

#### Crowd Control provided by Gala

- Steadfast (Supreme+) — Self — On Skill
- Pin — Single target — `medium`

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

Look for units providing: `Max HP` `Healing`  
Common buffers are **Lorsan**, **Evie**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Gerda

**Similar Skills**

- Solise (50% `ally-healer` `ally-shielder` `aoe-healing`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Atalanta (62% `Stun` `Pin`)
- Callan (62% `Stun` `Pin`)
- Lucca (62% `Stun` `Interrupt`)

### Summary for Gerda

#### Damage types dealt by Gerda

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Gerda

- Healing — Single target — `medium`

#### Crowd Control provided by Gerda

- Unaffected — Self — Conditional
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
Common buffers are **Lyca**, **Mikola**, or **Lorsan**.

- **Rowan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Granny Dahnie

**Similar Skills**

- Brutus (66% `hp-scaling` `taunt`)
- Silven (50% `hp-scaling`)
- Tilaya (50% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Pandora (100% `ATK debuff` `Haste debuff`)
- Athalia (75% `ATK debuff`)
- Bonnie (75% `ATK debuff` `Haste debuff`)

**Crowd Control**

- Arden (57% `Pin`)
- Eironn (57% `Pin`)
- Evie (57% `Pin`)

### Summary for Granny Dahnie

#### Damage types dealt by Granny Dahnie

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Debuffs provided by Granny Dahnie

- Haste debuff — Single target — `low`
- ATK debuff (Supreme+) — Single target — `high`

#### Crowd Control provided by Granny Dahnie

- Unaffected — Self — Conditional
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

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Gunnar

**Buffs on allies**

- Aurora (50% `Invincible`)
- Pandora (50% `Invincible`)

**Similar Skills**

- Rhys (50% `aoe-damage` `fire-attack`)

**Damage**

- Brutus (90% `Max HP-based damage` `DoT` `Physical`)
- Daimon (87% `Max HP-based damage` `DoT`)
- Satrana (87% `Max HP-based damage` `DoT`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Callan (100% `Stun`)

### Summary for Gunnar

#### Damage types dealt by Gunnar

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target
- DoT — Area
- Max HP-based damage — All units — `high`

#### Buffs provided by Gunnar

- ATK SPD buff — Single target — `low`
- Shield — Single target — `high`
- Ranged DEF buff (Legendary+) — Single target — `low`
- Vitality buff (Legendary+) — Single target — `low`
- Invincible (EX+15) — Single target — `high`

#### Crowd Control provided by Gunnar

- Stun — All units — `low`

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
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Gwyneth

**Similar Skills**

- Mirael (66% `dot-specialist` `fire-attack`)
- Natsu (50% `dot-specialist` `fire-attack` `mass-cc`)
- Satrana (50% `dot-specialist` `fire-attack`)

**Damage**

- Brutus (100% `Physical` `DoT` `Max HP-based damage`)
- Gunnar (100% `Physical` `DoT` `Max HP-based damage`)
- Himmel (92% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Brutus (100% `DoT`)
- Evie (100% `DoT`)
- Frieren (100% `DoT`)

**Crowd Control**

- Indris (71% `Pin` `Silence`)
- Kordan (60% `Pin`)
- Evie (57% `Pin` `Silence`)

### Summary for Gwyneth

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

Look for units providing: `ATK` `Healing`  
Common buffers are **Mikola**, **Evie**, or **Lyca**.

- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Hammie

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Similar Skills**

- Isabella (66% `ally-buffer` `ally-healer`)
- Laios (66% `ally-buffer` `ally-healer`)
- Perseus (50% `ally-buffer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

### Summary for Hammie

#### Damage types dealt by Hammie

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Hammie

- ATK buff — Multiple targets — `low`

## Harak

### Harak's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Flesh Feast — instantly defeat weakest unit
- Signature skill speed: fast
- Ultimate speed: slow
- Non-ultimate speed: slow

### Units Harak benefits from

Look for units providing: `Haste` `Max HP` `CRIT` `Healing` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)

### Units that can act as a replacement for Harak

**Buffs on allies**

- Brutus (100% `Life Drain`)
- Cecia (100% `Life Drain`)
- Daimon (100% `Life Drain`)

**Similar Skills**

- Seth (66% `assassin` `life-drain`)
- Nara (50% `assassin` `execute`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Kordan (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Aliceth (100% `Execution debuff`)

**Crowd Control**

- Kordan (100% `Move` `Knock down`)
- Ravion (100% `Move` `Knock down`)
- Reinier (100% `Move` `Knock down`)

### Summary for Harak

#### Damage types dealt by Harak

- Primary damage type (unit): **Physical**
- Physical — Single target
- HP loss — Single target — `low`

#### Buffs provided by Harak

- Crit buff — Single target — `high`
- Lifedrain buff (Legendary+) — Single target — `low`

#### Debuffs provided by Harak

- Execution debuff — Single target — `low`

#### Crowd Control provided by Harak

- Unaffected — Self — On Skill
- Knock down — Single target — `low`
- Move — Single target — `high`

#### Harak Provides

- Instant defeat — Single target
- Invincibility — Self

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

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units benefitting from Hepler

- Shadewing
- Daimon
- Thoran

### Units that can act as a replacement for Hepler

**Buffs on allies**

- Hugin (100% `Max HP` `Haste`)
- Callan (80% `Max HP`)
- Gala (80% `Max HP` `Haste`)

**Similar Skills**

- Lucius (66% `ally-healer` `ally-shielder`)
- Pang (66% `ally-shielder` `transformation`)
- Ulmus (66% `ally-shielder` `transformation`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Natsu (100% `Haste debuff`)
- Eironn (50% `Haste debuff`)

**Crowd Control**

- Antandra (100% `Taunt` `Stun`)
- Lumont (72% `Taunt` `Stun`)
- Brutus (54% `Taunt`)

### Summary for Hepler

#### Damage types dealt by Hepler

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Single target

#### Buffs provided by Hepler

- Haste buff — Single target — `low`
- Shield — Multiple targets — `medium`

#### Debuffs provided by Hepler

- Haste debuff — Area — `high`

#### Crowd Control provided by Hepler

- Stun — Area — `low`
- Taunt — Area — `high`

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

- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
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

### Units benefitting from Hewynn

**11** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Alna
- Callan
- Contess
- Evie
- Gerda
- Igor
- Phraesto
- Reinier
- Saida
- Tilaya

### Units that can act as a replacement for Hewynn

**Buffs on allies**

- Lorsan (100% `Healing`)
- Antandra (90% `Healing`)
- Evie (90% `Healing`)

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing`)
- Ludovic (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

### Summary for Hewynn

#### Damage types dealt by Hewynn

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Hewynn

- Healing — All units — `high`

#### Crowd Control provided by Hewynn

- Unaffected (Mythic+) — Self — On Skill

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

- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Party composition via Tank (party slot)
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

- Talene

### Units that can act as a replacement for Himmel

**Buffs on allies**

- Twins (77% `Max HP`)

**Similar Skills**

- Ravion (50% `ally-shielder` `self-repositioner`)
- Valka (50% `ally-buffer` `ally-shielder`)

**Damage**

- Gunnar (100% `Physical` `Max HP-based damage`)
- Brutus (96% `Physical` `Max HP-based damage`)
- Korin (96% `Physical` `Max HP-based damage`)

### Summary for Himmel

#### Damage types dealt by Himmel

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets, Single target
- Max HP-based damage — All units — `low`

#### Buffs provided by Himmel

- Shield — Single target — `low`
- ATK buff (Mythic+) — Multiple targets — `low`
- Max HP buff (Mythic+) — Multiple targets — `high`

#### Crowd Control provided by Himmel

- Unaffected — Multiple targets — On Skill

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

Look for units providing: `ATK` `Healing`  
Common buffers are **Mikola**, **Evie**, or **Lyca**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Units that can act as a replacement for Hodgkin

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `Phys DEF debuff` `Vitality debuff`)
- Silvina (78% `Energy drain` `Vitality debuff`)
- Dunlingr (57% `Energy drain`)

### Summary for Hodgkin

#### Damage types dealt by Hodgkin

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Debuffs provided by Hodgkin

- Energy drain (Mythic+) — Area — `low`
- Vitality debuff (EX+5) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `low`

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

**82** units include this provider among their top 5 synergy partners. Why the match is common:

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

**Buffs on allies**

- Mikola (55% `Haste` `ATK`)

**Similar Skills**

- Ravion (66% `ally-shielder` `energy-provider`)
- Twins (66% `ally-shielder` `energy-provider`)
- Lucca (50% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

### Summary for Hugin

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
Common buffers are **Lorsan**, **Evie**, or **Mikola**.

- **Koko**
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Kordan**
  - Lifedrain buff (multiple targets, high)
- **Ludovic**
  - Healing (area, medium)

### Units that can act as a replacement for Igor

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Callan (100% `Physical`)

### Summary for Igor

#### Damage types dealt by Igor

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

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

- Carolina

### Units that can act as a replacement for Indris

**Similar Skills**

- Kruger (50% `enemy-debuffer`)

**Damage**

- Korin (87% `Physical` `Max HP-based damage` `True damage`)
- Temesia (84% `Physical` `Max HP-based damage` `True damage`)
- Nara (84% `True damage` `Max HP-based damage` `Physical`)

**Debuffs on enemies**

- Sinbad (100% `Damage taken debuff` `Magic DEF debuff` `Phys DEF debuff`)
- Kruger (75% `Damage taken debuff` `Phys DEF debuff`)
- Cecia (50% `Damage taken debuff`)

**Crowd Control**

- Kordan (68% `Pin` `Move`)
- Evie (65% `Move` `Pin` `Silence`)
- Eironn (56% `Move` `Pin`)

### Summary for Indris

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
Common buffers are **Mikola**, **Hugin**, or **Twins**.

- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Isabella

**Buffs on allies**

- Damian (100% `Haste`)
- Gala (100% `Haste`)
- Hugin (100% `Haste`)

**Similar Skills**

- Hammie (66% `ally-buffer` `ally-healer`)
- Laios (50% `ally-buffer` `ally-healer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Contess (100% `ATK debuff`)

### Summary for Isabella

#### Damage types dealt by Isabella

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Isabella

- Haste buff — Multiple targets — `low` — conditional (frequent)

#### Debuffs provided by Isabella

- ATK debuff — Single target — `low`

#### Crowd Control provided by Isabella

- Unaffected — Single target — Once

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

Look for units providing: `ATK` `Max HP` `Healing`  
Common buffers are **Mikola**, **Twins**, or **Evie**.

- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)

### Units that can act as a replacement for Kafra

**Similar Skills**

- Sinbad (66% `enemy-debuffer` `mark-target`)
- Silvina (50% `assassin` `mark-target`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Lyca (60% `Phys DEF debuff` `ATK debuff`)
- Ravion (60% `Phys DEF debuff` `ATK debuff`)
- Sinbad (60% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Alsa (100% `Stun` `Move`)
- Atalanta (100% `Stun` `Move`)
- Cassadee (100% `Stun` `Move`)

### Summary for Kafra

#### Damage types dealt by Kafra

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Kafra

- Marked target (focus fire) — Single target — `medium`
- Phys DEF debuff — Single target — `low`
- ATK debuff (Mythic+) — Single target — `medium`
- Haste debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Kafra

- Unaffected (Mythic+) — Self — Conditional
- Move — Single target — `low`
- Stun — Single target — `high`

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

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Koko

**18** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Perseus
- Silven
- Valka
- Talene
- Alna
- Athalia
- Gerda
- Gunnar
- Harak
- Saida

### Units that can act as a replacement for Koko

**Similar Skills**

- Saida (66% `ally-shielder` `life-drain`)
- Daimon (50% `ally-shielder` `life-drain`)
- Lucca (50% `ally-shielder`)

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Callan (100% `Physical`)

**Debuffs on enemies**

- Kruger (66% `Damage taken debuff`)

**Crowd Control**

- Antandra (100% `Stun`)
- Faramor (100% `Stun`)
- Lorsan (100% `Stun`)

### Summary for Koko

#### Damage types dealt by Koko

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Koko

- Damage taken reduction — All units — `high`
- Healing — Multiple targets — `high`
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
Common buffers are **Mikola**, **Twins**, or **Evie**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Cecia**
  - Max HP buff (single target, high)
  - DEF Penetration buff (single target, medium)
  - Lifedrain buff (area, low)
  - ATK SPD buff (single target, low) [signature fuel]

### Units benefitting from Kordan

- Nerion
- Carolina

### Units that can act as a replacement for Kordan

**Buffs on allies**

- Cecia (58% `Life Drain` `DEF Penetration`)

**Similar Skills**

- Pippa (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)
- Marilee (66% `hp-scaling` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Ravion (100% `Physical` `HP loss`)

**Crowd Control**

- Indris (63% `Pin` `Move`)

### Summary for Kordan

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

- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
- **Lucius**
  - Max HP via Shield (area, high)

### Units that can act as a replacement for Korin

**Buffs on allies**

- Callan (100% `Max HP`)
- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)

**Similar Skills**

- Scarlita (66% `ally-shielder` `hp-scaling`)
- Daimon (50% `ally-shielder` `hp-scaling`)
- Lucca (50% `ally-shielder`)

**Damage**

- Nara (92% `Max HP-based damage` `True damage` `Physical`)
- Indris (89% `Physical` `Max HP-based damage` `True damage`)
- Temesia (86% `Physical` `Max HP-based damage` `True damage`)

**Crowd Control**

- Eironn (100% `Move` `Pin`)
- Evie (100% `Move` `Pin`)
- Indris (100% `Move` `Pin`)

### Summary for Korin

#### Damage types dealt by Korin

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area — `medium`
- True damage — Single target — `medium`

#### Buffs provided by Korin

- Shield — Single target — `medium`

#### Crowd Control provided by Korin

- Move — Area — `low`
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
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Rowan**
  - Max HP buff (single target, high)
  - DEF buff (single target, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - ATK SPD via Haste buff (single target, low) [signature fuel]

### Units that can act as a replacement for Kruger

**Similar Skills**

- Carolina (50% `enemy-debuffer`)
- Indris (50% `enemy-debuffer`)
- Lumont (50% `enemy-debuffer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)

### Summary for Kruger

#### Damage types dealt by Kruger

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Kruger

- Damage taken debuff — Area — `medium`
- Phys DEF debuff — Single target — `low`
- Vulnerable debuff — Area — `medium`

#### Crowd Control provided by Kruger

- Knock down — Single target — `low`

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

- Aliceth (100% `DEF Penetration`)
- Cecia (100% `DEF Penetration`)
- Dionel (100% `DEF Penetration`)

**Similar Skills**

- Alsa (50% `battlefield-modification` `self-repositioner`)

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Callan (100% `Physical`)

**Debuffs on enemies**

- Alsa (61% `Movement speed debuff`)

**Crowd Control**

- Cassadee (100% `Knock up` `Move`)
- Scarlita (100% `Knock up` `Move`)
- Reinier (83% `Move` `Knock up`)

### Summary for Kulu

#### Damage types dealt by Kulu

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target

#### Buffs provided by Kulu

- ATK buff (Legendary+) — Single target — `low`
- DEF Penetration buff (EX+15) — Single target — `low`

#### Debuffs provided by Kulu

- Movement speed debuff — Area — `medium`
- Damage taken debuff (Mythic+) — All units — `low`

#### Crowd Control provided by Kulu

- Unaffected — Area — On Ultimate
- Knock up — Single target — `low`
- Move — Single target — `low`

#### Kulu Provides

- Invincibility — Self
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
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units that can act as a replacement for Laios

**Similar Skills**

- Damian (66% `ally-healer` `summoner`)
- Hammie (66% `ally-buffer` `ally-healer`)
- Isabella (50% `ally-buffer` `ally-healer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Arden (100% `Pin`)
- Gwyneth (100% `Pin`)
- Indris (100% `Pin`)

### Summary for Laios

#### Damage types dealt by Laios

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Laios

- ATK buff — Multiple targets — `low` — conditional (rare)
- DEF buff — Single target — `low` — conditional (rare)

#### Crowd Control provided by Laios

- Pin — Area — `medium`

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

Look for units providing: `Haste` `Max HP` `CRIT` `CRIT DMG Boost` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Lenya

**Similar Skills**

- Soren (66% `counterattack` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Cassadee (100% `Move` `Stun`)
- Perseus (100% `Move` `Stun`)
- Scarlita (90% `Move` `Stun`)

### Summary for Lenya

#### Damage types dealt by Lenya

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Buffs provided by Lenya

- Crit buff — Single target — `low`
- Crit DMG boost (Mythic+) — Single target — `low`

#### Crowd Control provided by Lenya

- Unaffected — Self — Once
- Move — Area — `low`
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

- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
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

### Units benefitting from Lily May

- Bonnie
- Aliceth

### Units that can act as a replacement for Lily May

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Cecia (100% `DEF Penetration`)
- Dionel (100% `DEF Penetration`)

**Similar Skills**

- Athalia (60% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Shadewing (100% `Magic` `Max HP-based damage`)
- Shemira (100% `Magic` `Max HP-based damage`)
- Daimon (94% `Magic` `Max HP-based damage`)

**Debuffs on enemies**

- Pippa (53% `Energy drain`)

**Crowd Control**

- Smokey & Meerky (100% `Interrupt`)
- Sylphira (80% `Interrupt`)
- Gerda (60% `Interrupt`)

### Summary for Lily May

#### Damage types dealt by Lily May

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- Max HP-based damage — Self, Single target — `low`

#### Buffs provided by Lily May

- DEF Penetration buff (Legendary+) — Single target — `low`

#### Debuffs provided by Lily May

- Energy drain — Single target — `high`

#### Crowd Control provided by Lily May

- Unaffected — Self — Start of Battle
- Interrupt — Single target — `low`

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

Look for units providing: `ATK` `Healing`  
Common buffers are **Mikola**, **Evie**, or **Lyca**.

- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)

### Units benefitting from Lorsan

**33** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Valka
- Alna
- Athalia
- Baelran
- Berial
- Bryon
- Callan
- Contess
- Damian
- Dunlingr

### Units that can act as a replacement for Lorsan

**Buffs on allies**

- Hewynn (55% `Healing`)
- Antandra (50% `Healing`)
- Evie (50% `Healing`)

**Similar Skills**

- Arden (100% `aoe-damage` `dot-specialist`)
- Faramor (66% `aoe-damage` `dot-specialist`)
- Viperian (66% `aoe-damage` `dot-specialist`)

**Damage**

- Cryonaia (100% `Magic` `DoT`)
- Frieren (100% `Magic` `DoT`)
- Tasi (100% `Magic` `DoT`)

**Crowd Control**

- Antandra (100% `Stun`)
- Lucca (100% `Stun`)
- Lumont (100% `Stun`)

### Summary for Lorsan

#### Damage types dealt by Lorsan

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — Area

#### Buffs provided by Lorsan

- Dodge chance buff — Single target — `medium`
- Healing (Mythic+) — All units — `high`

#### Crowd Control provided by Lorsan

- Unaffected (Supreme+) — Self — On Skill
- Stun (EX+10) — Multiple targets — `high`

## Lucca

### Lucca's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Quake Slam (ultimate) — area knockdown slam
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: slow

### Units Lucca benefits from

Look for units providing: `Max HP` `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Rowan**
  - Max HP buff (single target, high)
  - DEF buff (single target, high)
  - DEF buff (single target, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)

### Units that can act as a replacement for Lucca

**Similar Skills**

- Antandra (50% `ally-shielder`)
- Gala (50% `ally-shielder`)
- Hugin (50% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Antandra (66% `Stun` `Knock down`)
- Zorya (66% `Stun` `Knock down`)
- Scarlita (62% `Stun` `Knock up` `Knock down`)

### Summary for Lucca

#### Damage types dealt by Lucca

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target

#### Crowd Control provided by Lucca

- Immune — Self — On Skill
- Interrupt — Single target — `medium`
- Knock down — Area — `low`
- Knock up — Area — `low`
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
Common buffers are **Lyca**, **Mikola**, or **Lorsan**.

- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Lucius

**17** units include this provider among their top 5 synergy partners. Why the match is common:

- ally buffs or enablers that match many receivers' benefit stats or Requires labels

These are the **10** strongest pairings: 

- Shadewing
- Himmel
- Alna
- Daimon
- Eironn
- Gerda
- Kruger
- Saida
- Satrana
- Silvina

### Units that can act as a replacement for Lucius

**Buffs on allies**

- Hugin (75% `Max HP`)
- Saida (75% `Max HP`)
- Callan (50% `Max HP`)

**Similar Skills**

- Hepler (66% `ally-healer` `ally-shielder`)
- Solise (66% `ally-healer` `ally-shielder`)
- Twins (66% `ally-healer` `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Lyca (100% `ATK debuff`)
- Athalia (83% `ATK debuff`)
- Sinbad (75% `ATK debuff`)

**Crowd Control**

- Atalanta (100% `Move` `Stun`)
- Cassadee (100% `Move` `Stun`)
- Lenya (100% `Move` `Stun`)

### Summary for Lucius

#### Damage types dealt by Lucius

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lucius

- Shield — Area — `high`

#### Debuffs provided by Lucius

- ATK debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Lucius

- Move — Single target — `high`
- Stun — Single target — `low`

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

- Callan (100% `Max HP`)
- Gala (100% `Max HP`)
- Hepler (100% `Max HP`)

**Similar Skills**

- Lucca (50% `ally-shielder`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Cryonaia (100% `Damage taken debuff`)
- Koko (100% `Damage taken debuff`)
- Kruger (100% `Damage taken debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Lucy

#### Damage types dealt by Lucy

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Lucy

- Shield (Mythic+) — Single target — `high`

#### Debuffs provided by Lucy

- Damage taken debuff — Single target — `high`

#### Crowd Control provided by Lucy

- Unaffected — Self — On Skill
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
Common buffers are **Lyca**, **Mikola**, or **Lorsan**.

- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Antandra**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Ludovic

**Buffs on allies**

- Antandra (64% `Healing`)
- Evie (64% `Healing`)
- Fay (64% `Healing`)

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)
- Smokey & Meerky (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Atalanta (100% `Stun`)

### Summary for Ludovic

#### Damage types dealt by Ludovic

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Ludovic

- Healing — Area — `medium`
- Healing over time — Single target — `high`

#### Crowd Control provided by Ludovic

- Unaffected — Self — On Skill
- Stun (Supreme+) — Single target — `medium`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units that can act as a replacement for Lumont

**Buffs on allies**

- Rowan (75% `Magic DEF` `Physical DEF`)
- Fay (50% `Magic DEF` `Physical DEF`)

**Similar Skills**

- Kruger (50% `enemy-debuffer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Cyran (100% `ATK debuff`)

**Crowd Control**

- Antandra (100% `Stun` `Taunt`)
- Hepler (66% `Taunt` `Stun`)
- Brutus (50% `Taunt`)

### Summary for Lumont

#### Damage types dealt by Lumont

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Lumont

- DEF buff — Multiple targets — `medium`

#### Debuffs provided by Lumont

- ATK debuff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Lumont

- Unaffected — Self — On Skill
- Stun — Single target — `high`
- Taunt — Single target — `medium`

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
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Lyca

**62** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on all allies fuel slow signature skills via the signature-fuel weight
- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Indris
- Perseus
- Silven
- Aliceth
- Zorya
- Cecia
- Cyran
- Dionel
- Fay
- Gwyneth

### Units that can act as a replacement for Lyca

**Buffs on allies**

- Valka (60% `ATK SPD`)

**Energy provider**

- Pandora
- Rowan
- Ravion

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Callan (100% `Physical`)

**Debuffs on enemies**

- Sinbad (50% `ATK debuff` `Phys DEF debuff`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Alsa (100% `Stun`)
- Antandra (100% `Stun`)

### Summary for Lyca

#### Damage types dealt by Lyca

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Self, Single target

#### Buffs provided by Lyca

- ATK SPD buff — All units — `medium`
- Energy recovery — All units — `low`

#### Debuffs provided by Lyca

- ATK debuff — All units — `high`

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

Look for units providing: `ATK SPD / Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Lyca**.

- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Marcille

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Crowd Control**

- Gerda (100% `Interrupt`)
- Lily May (100% `Interrupt`)
- Reinier (100% `Interrupt`)

### Summary for Marcille

#### Damage types dealt by Marcille

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target

#### Buffs provided by Marcille

- Haste buff — Single target — `low`

#### Crowd Control provided by Marcille

- Unaffected (Supreme+) — Self — On Skill
- Interrupt (Mythic+) — Single target — `high`

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

Look for units providing: `ATK` `ATK SPD / Haste` `CRIT` `CRIT DMG Boost`  
Common buffers are **Twins**, **Lyca**, or **Mikola**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Marilee

**Similar Skills**

- Kordan (66% `hp-scaling` `self-repositioner`)
- Pippa (66% `hp-scaling` `self-repositioner`)
- Tasi (66% `mass-cc` `self-repositioner`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `Physical` `True damage`)
- Dionel (100% `Physical` `True damage`)

**Crowd Control**

- Aliceth (100% `Stun`)
- Alsa (100% `Stun`)
- Antandra (100% `Stun`)

### Summary for Marilee

#### Damage types dealt by Marilee

- Primary damage type (unit): **Physical**
- Physical — Multiple targets, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Marilee

- ATK buff — Single target — `high` — conditional (frequent)

#### Crowd Control provided by Marilee

- Stun — Single target — `low`

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

Look for units providing: `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
  - Max HP via Shield (summons only, medium)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)

### Units that can act as a replacement for Mehira

**Buffs on allies**

- Damian (100% `Haste`)
- Gala (100% `Haste`)
- Hugin (100% `Haste`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Cecia (100% `Damage taken debuff`)
- Cryonaia (100% `Damage taken debuff`)
- Indris (100% `Damage taken debuff`)

**Crowd Control**

- Satrana (56% `Charm`)

### Summary for Mehira

#### Damage types dealt by Mehira

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Self, Single target

#### Buffs provided by Mehira

- Haste buff — Single target — `high`

#### Debuffs provided by Mehira

- Damage taken debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Mehira

- Charm — Single target — `medium`

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

Look for units providing: `ATK` `Haste` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Damian**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Mikola

**86** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Perseus
- Silven
- Hepler
- Seth
- Sylphira
- Tasi
- Vala
- Valka
- Laios
- Temesia

### Units that can act as a replacement for Mikola

**Buffs on allies**

- Evie (55% `Healing` `ATK`)
- Hugin (55% `Haste` `ATK`)
- Fay (50% `Healing` `ATK` `Vitality buff`)

**Damage**

- Alna (100% `Physical`)
- Athalia (100% `Physical`)
- Callan (100% `Physical`)

### Summary for Mikola

#### Damage types dealt by Mikola

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Multiple targets

#### Buffs provided by Mikola

- ATK buff — Multiple targets — `medium`
- Haste buff — Multiple targets — `high`
- Healing — Multiple targets — `high`
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
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Mirael

**Similar Skills**

- Gwyneth (66% `dot-specialist` `fire-attack`)
- Satrana (66% `dot-specialist` `fire-attack`)

**Damage**

- Arden (100% `Magic` `DoT`)
- Berial (100% `Magic` `DoT`)
- Bonnie (100% `Magic` `DoT`)

**Debuffs on enemies**

- Brutus (100% `DoT`)
- Evie (100% `DoT`)
- Frieren (100% `DoT`)

### Summary for Mirael

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

- Antandra (100% `Healing`)
- Evie (100% `Healing`)
- Fay (100% `Healing`)

**Similar Skills**

- Harak (50% `assassin` `execute`)

**Damage**

- Korin (96% `Max HP-based damage` `True damage` `Physical`)
- Indris (87% `True damage` `Max HP-based damage` `Physical`)
- Shadewing (87% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Pandora (100% `Vitality debuff`)
- Satrana (100% `Vitality debuff`)

**Crowd Control**

- Lucca (100% `Knock down` `Knock up`)
- Scarlita (80% `Knock down` `Knock up`)
- Antandra (60% `Knock down`)

### Summary for Nara

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
- Knock down — Single target — `high`
- Knock up — Single target — `medium`

## Natsu

### Natsu's behavior

- Movement: stationary (avg attack range 11.0 tiles)
- Signature skill: Lightning Fire Dragon's Roar/Fire Dragon King's Roar (ultimate) — high-damage elemental beam
- Signature skill speed: normal
- Ultimate speed: normal
- Non-ultimate speed: normal

### Units Natsu benefits from

Look for units providing: `ATK` `Haste` `CRIT` `CRIT DMG Boost`  
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

- Gwyneth (50% `dot-specialist` `fire-attack` `mass-cc`)

**Damage**

- Daimon (100% `Max HP-based damage` `Magic` `DoT`)
- Satrana (100% `Max HP-based damage` `Magic` `DoT`)
- Shadewing (100% `Max HP-based damage` `Magic` `DoT`)

**Debuffs on enemies**

- Alna (72% `Haste debuff`)
- Hepler (72% `Haste debuff`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Callan (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)

### Summary for Natsu

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

Look for units providing: `CRIT`  
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

**Similar Skills**

- Aliceth (50% `hp-scaling` `mark-target`)
- Silven (50% `hp-scaling`)
- Tilaya (50% `hp-scaling`)

**Damage**

- Athalia (100% `True damage` `Physical`)
- Baelran (100% `True damage` `Physical`)
- Dionel (100% `True damage` `Physical`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Atalanta (100% `Stun`)

### Summary for Nazrik

#### Damage types dealt by Nazrik

- Primary damage type (unit): **Physical**
- Physical — Single target
- True damage — Single target — `high`

#### Debuffs provided by Nazrik

- Healing debuff — Single target — `medium`
- Max HP debuff — Single target — `medium`
- Crit Resist debuff (Mythic+) — Single target — `low`
- Damage taken debuff (EX+10) — Single target — `low`
- Vitality debuff (EX+10) — Single target — `low`

#### Crowd Control provided by Nazrik

- Stun — Single target — `medium`

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
Common buffers are **Ravion**, **Twins**, or **Lyca**.

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

**Similar Skills**

- Shadewing (100% `dot-specialist` `enemy-debuffer`)
- Kruger (50% `enemy-debuffer`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Athalia (100% `ATK debuff`)
- Bonnie (100% `ATK debuff`)
- Contess (100% `ATK debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Atalanta (100% `Stun`)

### Summary for Nerion

#### Damage types dealt by Nerion

- Primary damage type (unit): **Magic**
- Magic — Area, Self, Single target

#### Debuffs provided by Nerion

- ATK debuff (Mythic+) — Single target — `low`

#### Crowd Control provided by Nerion

- Stun — Single target — `medium`

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

Look for units providing: `Healing` `Physical DEF` `Magic DEF`  
Common buffers are **Lyca**, **Mikola**, or **Lorsan**.

- **Rowan**
  - DEF buff (single target, high)
  - DEF buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - DEF buff (multiple targets, low)
  - DEF buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Lumont**
  - DEF buff (multiple targets, medium)
  - DEF buff (multiple targets, medium)
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Niru

**Damage**

- Dunlingr (100% `Magic` `HP loss`)
- Shadewing (100% `Magic` `HP loss`)
- Talene (100% `Magic` `HP loss`)

### Summary for Niru

#### Damage types dealt by Niru

- Primary damage type (unit): **Magic**
- Magic — All units, Self, Single target
- HP loss — Single target — `low`

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

- Arden (100% `DoT` `Magic`)
- Berial (100% `DoT` `Magic`)
- Bonnie (100% `DoT` `Magic`)

**Debuffs on enemies**

- Brutus (100% `DoT`)
- Evie (100% `DoT`)
- Frieren (100% `DoT`)

### Summary for Odie

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
- Lucius
- Ludovic
- Chippy
- Nara
- Scarlita

### Units that can act as a replacement for Pandora

**Buffs on allies**

- Smokey & Meerky (50% `Healing` `Energy`)
- Zanie (50% `Healing` `Max HP`)

**Energy provider**

- Rowan

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Sinbad (80% `ATK debuff` `Vitality debuff` `Damage taken debuff` `Energy drain`)

### Summary for Pandora

#### Damage types dealt by Pandora

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Pandora

- Energy recovery — Single target — `low`
- Healing — Single target — `high`
- Invincible — Single target — `high`
- Max HP buff (Legendary+) — Single target — `low`

#### Debuffs provided by Pandora

- ATK debuff — Single target — `low`
- Damage taken debuff — Single target — `low`
- Energy drain — Single target — `low`
- Haste debuff — Single target — `medium`
- Vitality debuff — Single target — `high`

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
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Pang

**Buffs on allies**

- Zanie (100% `DEF Penetration` `Max HP`)
- Aliceth (50% `DEF Penetration`)
- Callan (50% `Max HP`)

**Similar Skills**

- Ulmus (100% `ally-shielder` `transformation`)
- Hepler (66% `ally-shielder` `transformation`)
- Lucca (50% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Faramor (100% `Stun`)

### Summary for Pang

#### Damage types dealt by Pang

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Pang

- Shield (EX+10) — Single target — `low`
- DEF Penetration buff (Supreme+) — Single target — `low`

#### Crowd Control provided by Pang

- Unaffected — Self — On Skill
- Stun — Area — `low`

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
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Gala**
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Parisa

**Similar Skills**

- Cassadee (50% `ally-buffer` `aoe-damage`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

### Summary for Parisa

#### Damage types dealt by Parisa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Self, Single target

#### Buffs provided by Parisa

- ATK SPD buff — Single target — `medium`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Enables Ally stat buffs via 5 ally stat buffs
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Enables Ally stat buffs via 5 ally stat buffs
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs (start of battle)
- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
  - Enables Ally stat buffs via 3 ally stat buffs

### Units that can act as a replacement for Perseus

**Buffs on allies**

- Evie (100% `ATK`)
- Hugin (100% `ATK`)
- Mikola (100% `ATK`)

**Similar Skills**

- Hammie (50% `ally-buffer`)
- Sonja (50% `ally-buffer`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Baelran (100% `Physical` `True damage`)
- Dionel (100% `Physical` `True damage`)

**Crowd Control**

- Scarlita (72% `Stun` `Move`)
- Antandra (66% `Stun`)
- Lucca (66% `Stun`)

### Summary for Perseus

#### Damage types dealt by Perseus

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Perseus

- ATK buff — Multiple targets — `medium`

#### Crowd Control provided by Perseus

- Unaffected — Multiple targets — Conditional
- Move — Area — `low`
- Stun — Area — `medium`

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
Common buffers are **Lorsan**, **Evie**, or **Mikola**.

- **Aurora**
  - Summon damage buff (summons only, low)
  - ATK SPD via Haste buff (summons only, high)
- **Florabelle**
  - Summon damage buff (summons only, medium)
  - ATK SPD via Haste buff (summons only, medium, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Phraesto

**Buffs on allies**

- Koko (75% `Max HP` `Damage taken reduction`)
- Twins (75% `Max HP`)
- Zanie (75% `Max HP`)

**Energy provider**

- Lyca
- Pandora
- Ravion

**Similar Skills**

- Gala (50% `ally-shielder` `clone`)
- Hugin (50% `ally-shielder` `energy-provider`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Crowd Control**

- Antandra (100% `Stun` `Taunt`)
- Hepler (100% `Stun` `Taunt`)
- Lumont (100% `Stun` `Taunt`)

### Summary for Phraesto

#### Damage types dealt by Phraesto

- Primary damage type (unit): **Magic**
- Magic — Area, Single target

#### Buffs provided by Phraesto

- Damage taken reduction — Single target — `low`
- Max HP buff — Single target — `low`
- Shield — Single target — `high`

#### Crowd Control provided by Phraesto

- Stun (Mythic+) — Single target — `low`
- Taunt (Mythic+) — Single target — `low`

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

**Similar Skills**

- Kordan (100% `hp-scaling` `self-repositioner`)
- Athalia (66% `hp-scaling` `self-repositioner`)
- Marilee (66% `hp-scaling` `self-repositioner`)

**Damage**

- Indris (87% `True damage` `Max HP-based damage`)
- Shadewing (84% `Magic` `Max HP-based damage` `True damage`)
- Sylphira (84% `Magic` `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Lily May (100% `Energy drain`)
- Sinbad (75% `Energy drain`)
- Dunlingr (62% `Energy drain`)

**Crowd Control**

- Kordan (100% `Pin` `Knock down` `Move`)
- Atalanta (70% `Pin` `Move`)
- Callan (70% `Pin` `Knock down`)

### Summary for Pippa

#### Damage types dealt by Pippa

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target
- Max HP-based damage — Single target — `low`
- True damage — Area — `medium`

#### Buffs provided by Pippa

- Haste buff (Legendary+) — Single target — `low`

#### Debuffs provided by Pippa

- Energy drain — Area — `medium`

#### Crowd Control provided by Pippa

- Unaffected — Self — On Skill
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
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Vala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units benefitting from Ravion

**24** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy recovery** helps slow-ultimate units reach their first Ultimate sooner
- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Nerion
- Indris
- Carolina
- Aliceth
- Arden
- Pang
- Parisa
- Temesia
- Vala
- Cryonaia

### Units that can act as a replacement for Ravion

**Buffs on allies**

- Evie (50% `ATK`)
- Hugin (50% `ATK`)
- Mikola (50% `ATK`)

**Energy provider**

- Lyca
- Pandora
- Rowan

**Similar Skills**

- Hugin (66% `ally-shielder` `energy-provider`)
- Himmel (50% `ally-shielder` `self-repositioner`)
- Twins (50% `ally-shielder` `energy-provider`)

**Damage**

- Aliceth (100% `Physical` `HP loss`)
- Faramor (100% `Physical` `HP loss`)
- Kordan (100% `Physical` `HP loss`)

**Debuffs on enemies**

- Lyca (100% `ATK debuff` `Phys DEF debuff`)
- Sinbad (100% `ATK debuff` `Phys DEF debuff`)
- Kafra (58% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Kordan (58% `Move` `Knock down`)
- Reinier (58% `Move` `Knock down`)
- Antandra (50% `Knock down`)

### Summary for Ravion

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

- Unaffected — Self — Conditional
- Knock down — Multiple targets — `high`
- Move — Multiple targets — `high`

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

Look for units providing: `Healing`  
Common buffers are **Lorsan**, **Evie**, or **Mikola**.

- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)
- **Ludovic**
  - Healing (area, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))

### Units that can act as a replacement for Reinier

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Cryonaia (75% `Damage taken debuff`)
- Koko (75% `Damage taken debuff`)
- Kruger (75% `Damage taken debuff`)

**Crowd Control**

- Ravion (63% `Move` `Knock down`)
- Cassadee (54% `Move` `Knock up`)
- Indris (54% `Move`)

### Summary for Reinier

#### Damage types dealt by Reinier

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Multiple targets, Single target

#### Buffs provided by Reinier

- ATK buff (Legendary+) — Single target — `low`

#### Debuffs provided by Reinier

- ATK debuff (Legendary+) — Single target — `low`
- Damage taken debuff (Mythic+) — Single target — `high`

#### Crowd Control provided by Reinier

- Steadfast — Single target — Conditional
- Unaffected — Single target — Conditional
- Interrupt — Single target — `high`
- Knock up — Single target — `low`
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

Look for units providing: `ATK SPD / Haste` `CRIT` `CRIT DMG Boost` `Healing`  
Common buffers are **Twins**, **Mikola**, or **Lyca**.

- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Rowan**
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Units that can act as a replacement for Rhys

**Similar Skills**

- Gunnar (50% `aoe-damage` `fire-attack`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Cassadee (100% `Move`)
- Eironn (100% `Move`)
- Evie (100% `Move`)

### Summary for Rhys

#### Damage types dealt by Rhys

- Primary damage type (unit): **Physical**
- Physical — Arc, Single target

#### Buffs provided by Rhys

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

Look for units providing: `Haste` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)

### Units benefitting from Rowan

**15** units include this provider among their top 5 synergy partners. Why the match is common:

- **Energy at battle start** (or right after) accelerates early Ultimate access for slow-ultimate units

These are the **10** strongest pairings: 

- Cecia
- Granny Dahnie
- Niru
- Cryonaia
- Antandra
- Salazer
- Satrana
- Shemira
- Walker
- Lily May

### Units that can act as a replacement for Rowan

**Buffs on allies**

- Himmel (57% `Max HP` `ATK`)

**Energy provider**

- Pandora
- Lyca

**Similar Skills**

- Twins (66% `ally-healer` `energy-provider`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Debuffs on enemies**

- Berial (100% `Energy drain`)
- Contess (100% `Energy drain`)
- Dunlingr (100% `Energy drain`)

### Summary for Rowan

#### Damage types dealt by Rowan

- Primary damage type (unit): **Magic**
- Magic — Single target

#### Buffs provided by Rowan

- DEF buff (Mythic+) — Single target — `high`
- Max HP buff (Mythic+) — Single target — `high`
- ATK buff (EX+5) — Single target — `low`

#### Debuffs provided by Rowan

- Energy drain — Single target — `medium`

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

Look for units providing: `Max HP` `Healing`  
Common buffers are **Lorsan**, **Evie**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Zanie**
  - Max HP via Shield (single target, high)
  - Healing (single target, high)

### Units benefitting from Saida

- Daimon
- Eironn
- Kruger
- Silvina
- Thoran

### Units that can act as a replacement for Saida

**Buffs on allies**

- Hugin (100% `Max HP`)
- Lucius (100% `Max HP`)
- Callan (66% `Max HP`)

**Similar Skills**

- Koko (66% `ally-shielder` `life-drain`)
- Thoran (50% `life-drain` `revive`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Dunlingr (100% `Energy drain`)
- Lily May (100% `Energy drain`)
- Pippa (100% `Energy drain`)

**Crowd Control**

- Reinier (100% `Interrupt` `Move`)
- Gerda (64% `Interrupt`)
- Lily May (64% `Interrupt`)

### Summary for Saida

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

Look for units providing: `Max HP` `Healing`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Salazer

**Buffs on allies**

- Callan (100% `Max HP`)
- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)

**Similar Skills**

- Zorya (66% `hp-scaling` `life-drain`)
- Brutus (50% `hp-scaling` `life-drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Arden (100% `Pin`)
- Atalanta (100% `Pin`)
- Callan (100% `Pin`)

### Summary for Salazer

#### Damage types dealt by Salazer

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Buffs provided by Salazer

- Shield (Supreme+) — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Salazer

- Pin — Self — `low`

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

- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Gala**
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Satrana

**Similar Skills**

- Mirael (66% `dot-specialist` `fire-attack`)
- Faramor (50% `dot-specialist` `hp-scaling`)
- Gwyneth (50% `dot-specialist` `fire-attack`)

**Damage**

- Daimon (100% `Max HP-based damage` `DoT` `Magic`)
- Shadewing (94% `Max HP-based damage` `Magic` `DoT`)
- Gunnar (91% `Max HP-based damage` `DoT`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Pandora (100% `Vitality debuff`)
- Sinbad (100% `Vitality debuff`)

**Crowd Control**

- Mehira (100% `Charm`)

### Summary for Satrana

#### Damage types dealt by Satrana

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- DoT — Area
- Max HP-based damage — Arc, Area — `high`

#### Buffs provided by Satrana

- Damage taken reduction (Legendary+) — Single target — `medium`

#### Debuffs provided by Satrana

- Vitality debuff — Area — `low`

#### Crowd Control provided by Satrana

- Charm — Single target — `high`

#### Satrana Provides

- Ally DoT on enemies — Area
- Ally Vitality debuff on enemies — Area
- Ally grant (Sparks) — Area
- Invincibility — Self

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

- Callan (100% `Max HP`)
- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)

**Similar Skills**

- Korin (66% `ally-shielder` `hp-scaling`)
- Faramor (50% `aoe-damage` `hp-scaling`)
- Zandrok (50% `aoe-damage` `hp-scaling`)

**Damage**

- Athalia (100% `Physical` `True damage`)
- Dionel (100% `Physical` `True damage`)
- Baelran (95% `Physical` `True damage`)

**Crowd Control**

- Lucca (70% `Stun` `Knock up` `Knock down`)
- Cassadee (58% `Move` `Knock up` `Stun`)
- Perseus (54% `Stun` `Move`)

### Summary for Scarlita

#### Damage types dealt by Scarlita

- Primary damage type (unit): **Physical**
- Physical — All units, Arc, Area, Single target
- True damage — Multiple targets — `low`

#### Buffs provided by Scarlita

- Shield — Single target — `medium`

#### Crowd Control provided by Scarlita

- Unaffected — Self — Conditional
- Knock down — Arc — `low`
- Knock up — Area — `medium`
- Move — All units — `low`
- Stun — Single target — `medium`

#### Scarlita Provides

- Invincibility — Self

## Seth

### Seth's behavior

- Movement: high movement (repositioning skills)
- Signature skill: Shadow Strike (ultimate) — multi-hit shadow burst
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Seth benefits from

Look for units providing: `ATK` `Haste` `CRIT` `Healing` `Energy`  
Common buffers are **Twins**, **Mikola**, or **Hugin**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Dunlingr**
  - ATK buff (single target, low)
  - Haste buff (single target, low) [signature fuel]
  - Lifedrain buff (all units, low)
  - ATK SPD buff (all units, low) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Units that can act as a replacement for Seth

**Buffs on allies**

- Brutus (100% `Life Drain`)
- Cecia (100% `Life Drain`)
- Daimon (100% `Life Drain`)

**Similar Skills**

- Harak (66% `assassin` `life-drain`)

**Damage**

- Aliceth (100% `Physical`)
- Faramor (100% `Physical`)
- Harak (100% `Physical`)

**Debuffs on enemies**

- Atalanta (100% `Phys DEF debuff`)
- Brutus (100% `Phys DEF debuff`)
- Fay (100% `Phys DEF debuff`)

**Crowd Control**

- Alna (100% `Freeze`)
- Carolina (100% `Freeze`)

### Summary for Seth

#### Damage types dealt by Seth

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- HP loss — Self

#### Buffs provided by Seth

- Haste buff — Single target — `low`
- Lifedrain buff — Single target — `low`

#### Debuffs provided by Seth

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Seth

- Freeze — Single target — `low`

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
Common buffers are **Evie**, **Lyca**, or **Ravion**.

- **Hepler**
  - Max HP via Shield (multiple targets, medium)
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via tick damage
- **Alna**
  - ATK buff (single target, medium)
  - Max HP buff (single target, low)
  - Enables Debuff on target via Haste debuff (area)
  - Enables Continuous damage on enemies via DoT
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Debuff on target via ATK debuff (area)
- **Koko**
  - Max HP via Shield (all units, low)
  - Lifedrain buff (multiple targets, low)
  - Enables Debuff on target via Damage taken debuff (area)
- **Frieren**
  - Enables Debuff on target via DoT (area)
  - Enables Continuous damage on enemies via DoT + Burn

### Units that can act as a replacement for Shadewing

**Similar Skills**

- Nerion (100% `dot-specialist` `enemy-debuffer`)
- Kruger (50% `enemy-debuffer`)

**Damage**

- Sylphira (56% `Magic` `Max HP-based damage` `True damage`)
- Korin (55% `Max HP-based damage` `True damage`)
- Nara (55% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Eironn (100% `Magic DEF debuff`)
- Sinbad (100% `Magic DEF debuff`)
- Thador (90% `Magic DEF debuff`)

### Summary for Shadewing

#### Damage types dealt by Shadewing

- Primary damage type (unit): **Magic**
- Magic — All units, Single target
- DoT — Single target
- HP loss — Single target — `low`
- Max HP-based damage — All units — `high`
- True damage — Single target — `low`

#### Debuffs provided by Shadewing

- Magic DEF debuff — All units — `low`

#### Shadewing Provides

- Debuff application — Single target
- DoT conversion — All units
- Invincibility — Self
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

**Buffs on allies**

- Zandrok (66% `Life Drain` `Haste`)
- Dunlingr (57% `Life Drain` `Haste`)
- Koko (57% `Damage taken reduction` `Life Drain`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Vitality debuff`)
- Nara (100% `Vitality debuff`)
- Pandora (100% `Vitality debuff`)

### Summary for Shakir

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
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Shemira

**Similar Skills**

- Daimon (60% `hp-scaling` `life-drain` `summoner`)
- Zorya (50% `hp-scaling` `life-drain`)

**Damage**

- Shadewing (100% `Max HP-based damage` `Magic`)
- Daimon (97% `Max HP-based damage` `Magic`)
- Satrana (97% `Max HP-based damage` `Magic`)

### Summary for Shemira

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Koko**
  - Enables Ally stat buffs via 5 ally stat buffs
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - DEF buff (multiple targets, low)
  - Enables Ally stat buffs via 5 ally stat buffs
- **Himmel**
  - Enables Ally stat buffs via 3 ally stat buffs (start of battle)
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Enables Ally stat buffs via 2 ally stat buffs
- **Pandora**
  - Energy recovery (single target, low) [signature fuel]
  - Enables Ally stat buffs via 4 ally stat buffs (start of battle)

### Units that can act as a replacement for Silven

**Buffs on allies**

- Aliceth (100% `DEF Penetration`)
- Cecia (100% `DEF Penetration`)
- Dionel (100% `DEF Penetration`)

**Similar Skills**

- Tilaya (100% `hp-scaling`)
- Baelran (50% `hp-scaling`)
- Granny Dahnie (50% `hp-scaling`)

**Damage**

- Pippa (100% `Magic` `True damage`)
- Shadewing (100% `Magic` `True damage`)
- Sylphira (100% `Magic` `True damage`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)

### Summary for Silven

#### Damage types dealt by Silven

- Primary damage type (unit): **Magic**
- Magic — Self, Single target
- Max HP-based damage — Self
- True damage — Single target — `low`

#### Buffs provided by Silven

- DEF Penetration buff (Mythic+) — Single target — `low`

#### Crowd Control provided by Silven

- Knock down — Single target — `medium`

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

Look for units providing: `Max HP` `CRIT`  
Common buffers are **Twins**, **Hugin**, or **Lyca**.

- **Lucius**
  - Max HP via Shield (area, high)
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

### Units that can act as a replacement for Silvina

**Similar Skills**

- Kafra (50% `assassin` `mark-target`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Sinbad (100% `Energy drain` `Vitality debuff`)
- Hodgkin (73% `Energy drain` `Vitality debuff`)
- Dunlingr (60% `Energy drain`)

**Crowd Control**

- Berial (72% `Frighten`)
- Daimon (72% `Frighten`)

### Summary for Silvina

#### Damage types dealt by Silvina

- Primary damage type (unit): **Physical**
- Physical — Single target

#### Debuffs provided by Silvina

- Energy drain — Single target — `high`
- Vitality debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Silvina

- Stun — Single target — `low`
- Frighten (EX+10) — Area — `low`

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

**Similar Skills**

- Kafra (66% `enemy-debuffer` `mark-target`)
- Kruger (50% `enemy-debuffer`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

### Summary for Sinbad

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
Common buffers are **Evie**, **Lorsan**, or **Mikola**.

- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)
- **Ludovic**
  - Healing (area, medium)

### Units benefitting from Smokey & Meerky

- Nara
- Pandora
- Scarlita

### Units that can act as a replacement for Smokey & Meerky

**Buffs on allies**

- Evie (75% `Healing` `ATK`)
- Fay (75% `Healing` `ATK`)
- Mikola (75% `Healing` `ATK`)

**Energy provider**

- Lyca
- Pandora
- Phraesto

**Similar Skills**

- Fay (100% `ally-healer` `aoe-healing`)
- Hewynn (100% `ally-healer` `aoe-healing`)
- Ludovic (100% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Arden (100% `Magic`)
- Aurora (100% `Magic`)

**Crowd Control**

- Lily May (55% `Interrupt`)

### Summary for Smokey & Meerky

#### Damage types dealt by Smokey & Meerky

- Primary damage type (unit): **Magic**
- Magic — Area, Multiple targets, Single target

#### Buffs provided by Smokey & Meerky

- Energy recovery — Multiple targets — `low`
- Healing — Multiple targets — `medium`
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

Look for units providing: `ATK` `Healing`  
Common buffers are **Mikola**, **Evie**, or **Hugin**.

- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Smokey & Meerky**
  - ATK buff (multiple targets, low)
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Koko**
  - Healing (multiple targets, high)

### Units that can act as a replacement for Solise

**Similar Skills**

- Velara (75% `ally-healer` `ally-shielder` `aoe-healing`)
- Fay (66% `ally-healer` `aoe-healing`)
- Hewynn (66% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

### Summary for Solise

#### Damage types dealt by Solise

- Primary damage type (unit): **Magic**
- Magic — All units, Multiple targets, Single target

#### Buffs provided by Solise

- Shield — Summons only — `medium`

#### Crowd Control provided by Solise

- Unaffected — Self — On Skill

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Lucius**
  - Max HP via Shield (area, high)
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

### Units that can act as a replacement for Sonja

**Buffs on allies**

- Aliceth (100% `ATK`)
- Alna (100% `ATK`)
- Contess (100% `ATK`)

**Similar Skills**

- Perseus (50% `ally-buffer`)
- Silven (50% `hp-scaling`)
- Tilaya (50% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Atalanta (100% `Stun`)

### Summary for Sonja

#### Damage types dealt by Sonja

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Sonja

- ATK buff — Multiple targets — `low`

#### Crowd Control provided by Sonja

- Stun — Single target — `low`

## Soren

### Soren's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Whirlwind Swing (ultimate) — knockback + collision stun
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: normal

### Units Soren benefits from

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units that can act as a replacement for Soren

**Buffs on allies**

- Callan (100% `Max HP`)
- Contess (100% `Max HP`)
- Daimon (100% `Max HP`)

**Similar Skills**

- Lenya (66% `counterattack` `self-repositioner`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Perseus (100% `Stun` `Move`)
- Scarlita (100% `Stun` `Move`)
- Atalanta (85% `Move` `Stun`)

### Summary for Soren

#### Damage types dealt by Soren

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target

#### Buffs provided by Soren

- Damage taken reduction — Single target — `low`
- Haste buff (Legendary+) — Single target — `medium`
- Shield (Supreme+) — Single target — `low`

#### Crowd Control provided by Soren

- Move — Multiple targets — `high`
- Stun — Single target — `low`

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

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]

### Units that can act as a replacement for Sylphira

**Damage**

- Shadewing (100% `Magic` `Max HP-based damage` `True damage`)
- Pippa (94% `Magic` `Max HP-based damage` `True damage`)
- Indris (81% `Max HP-based damage` `True damage`)

**Debuffs on enemies**

- Contess (54% `Energy drain` `Max HP debuff`)

**Crowd Control**

- Temesia (60% `Knock down` `Interrupt`)

### Summary for Sylphira

#### Damage types dealt by Sylphira

- Primary damage type (unit): **Magic**
- Magic — Area, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Single target — `low`

#### Debuffs provided by Sylphira

- Energy drain — Single target — `medium`
- Max HP debuff — Area — `medium`

#### Crowd Control provided by Sylphira

- Immune — Self — On Skill
- Unaffected — Area — Conditional
- Cleanse (Mythic+) — Self — On Skill
- Interrupt — Area — `low`
- Knock down — Area — `medium`
- Silence — Area — `low`

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
Common buffers are **Evie**, **Lorsan**, or **Mikola**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Lifedrain buff (multiple targets, low)
- **Himmel**
  - ATK buff (multiple targets, low)
  - Max HP buff (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Talene

**Damage**

- Zorya (93% `HP loss` `Magic`)
- Dunlingr (88% `HP loss` `Magic`)
- Niru (78% `Magic` `HP loss`)

**Crowd Control**

- Atalanta (100% `Move`)
- Cassadee (100% `Move`)
- Eironn (100% `Move`)

### Summary for Talene

#### Damage types dealt by Talene

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- HP loss — All units, Single target — `high`

#### Crowd Control provided by Talene

- Move — Area — `low`

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

Look for units providing: `ATK` `Haste` `Max HP` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units benefitting from Tasi

- Nerion
- Carolina

### Units that can act as a replacement for Tasi

**Similar Skills**

- Marilee (66% `mass-cc` `self-repositioner`)

**Damage**

- Cryonaia (100% `DoT` `Magic`)
- Frieren (100% `DoT` `Magic`)
- Lorsan (90% `Magic` `DoT`)

### Summary for Tasi

#### Damage types dealt by Tasi

- Primary damage type (unit): **Magic**
- Magic — All units, Area, Single target
- DoT — All units, Single target

#### Buffs provided by Tasi

- Haste buff (Mythic+) — Single target — `high`

#### Crowd Control provided by Tasi

- Pin — All units — `low`
- Sleep — Single target — `high`
- Stun — Area — `high`

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

- **Rowan**
  - ATK buff (single target, low)
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
- **Pandora**
  - Max HP buff (single target, low)
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Valka**
  - ATK SPD buff (multiple targets, high) [signature fuel]
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units that can act as a replacement for Temesia

**Similar Skills**

- Cassadee (50% `aoe-damage` `enemy-debuffer`)

**Damage**

- Indris (95% `Physical` `Max HP-based damage` `True damage`)
- Korin (95% `Physical` `Max HP-based damage` `True damage`)
- Nara (85% `Max HP-based damage` `Physical` `True damage`)

**Debuffs on enemies**

- Atalanta (100% `Phys DEF debuff`)
- Brutus (100% `Phys DEF debuff`)
- Fay (100% `Phys DEF debuff`)

**Crowd Control**

- Sylphira (100% `Knock down` `Interrupt`)
- Lucca (75% `Knock down` `Interrupt`)
- Antandra (62% `Knock down`)

### Summary for Temesia

#### Damage types dealt by Temesia

- Primary damage type (unit): **Physical**
- Physical — All units, Area, Single target
- Max HP-based damage — Single target — `medium`
- True damage — Single target — `low`

#### Debuffs provided by Temesia

- Phys DEF debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Temesia

- Unaffected (Mythic+) — Self — Permanent
- Interrupt — Single target — `high`
- Knock down — All units — `low`

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

Look for units providing: `Max HP` `CRIT` `Healing`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Fay**
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Antandra**
  - Healing (multiple targets, high)

### Units benefitting from Thador

- Nara
- Pandora
- Scarlita

### Units that can act as a replacement for Thador

**Buffs on allies**

- Lyca (100% `Energy`)
- Pandora (100% `Energy`)
- Ravion (100% `Energy`)

**Energy provider**

- Lyca
- Pandora
- Ravion

**Similar Skills**

- Hugin (50% `ally-shielder` `energy-provider`)

**Damage**

- Alna (100% `Physical` `DoT`)
- Brutus (100% `Physical` `DoT`)
- Cecia (100% `Physical` `DoT`)

**Debuffs on enemies**

- Eironn (100% `Magic DEF debuff`)
- Shadewing (100% `Magic DEF debuff`)
- Sinbad (100% `Magic DEF debuff`)

**Crowd Control**

- Antandra (100% `Knock down`)
- Athalia (100% `Knock down`)
- Baelran (100% `Knock down`)

### Summary for Thador

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
Common buffers are **Hugin**, **Ravion**, or **Lyca**.

- **Lucius**
  - Max HP via Shield (area, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)
- **Callan**
  - Max HP via Shield (multiple targets, medium)
- **Hepler**
  - Max HP via Shield (multiple targets, medium)
- **Koko**
  - Max HP via Shield (all units, low)

### Units that can act as a replacement for Thoran

**Buffs on allies**

- Koko (100% `Healing` `Life Drain`)
- Antandra (66% `Healing`)
- Evie (66% `Healing`)

**Similar Skills**

- Saida (50% `life-drain` `revive`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Bryon (100% `Interrupt`)
- Gerda (100% `Interrupt`)
- Lily May (100% `Interrupt`)

### Summary for Thoran

#### Damage types dealt by Thoran

- Primary damage type (unit): **Physical**
- Physical — Self, Single target

#### Buffs provided by Thoran

- Healing — Single target — `medium`
- Lifedrain buff — Single target — `low` — conditional (frequent)

#### Crowd Control provided by Thoran

- Unaffected — Self — On Skill
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
Common buffers are **Lorsan**, **Evie**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Tilaya

**Buffs on allies**

- Cecia (100% `Max HP`)
- Himmel (100% `Max HP`)
- Rowan (100% `Max HP`)

**Similar Skills**

- Silven (100% `hp-scaling`)
- Baelran (50% `hp-scaling`)
- Granny Dahnie (50% `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

### Summary for Tilaya

#### Damage types dealt by Tilaya

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Single target

#### Buffs provided by Tilaya

- Max HP buff (EX+10) — Area — `low`

#### Crowd Control provided by Tilaya

- Unaffected — Arc — Start of Battle

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

Look for units providing: `Max HP` `Healing` `Energy`  
Common buffers are **Lorsan**, **Evie**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
- **Lucius**
  - Max HP via Shield (area, high)
- **Hewynn**
  - Healing (all units, medium)
- **Antandra**
  - Healing (multiple targets, high)
- **Saida**
  - Max HP via Shield (multiple targets, high)

### Units that can act as a replacement for Ulmus

**Buffs on allies**

- Daimon (100% `Life Drain` `Max HP`)
- Koko (100% `Life Drain` `Max HP`)
- Brutus (50% `Life Drain`)

**Similar Skills**

- Pang (100% `ally-shielder` `transformation`)
- Hepler (66% `ally-shielder` `transformation`)
- Lucca (50% `ally-shielder`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Kordan (100% `Move` `Knock down`)
- Ravion (100% `Move` `Knock down`)
- Scarlita (100% `Move` `Knock down`)

### Summary for Ulmus

#### Damage types dealt by Ulmus

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Buffs provided by Ulmus

- Shield — Single target — `low`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control provided by Ulmus

- Unaffected — Self — On Skill
- Knock down (Mythic+) — Single target — `medium`
- Move (Supreme+) — Area — `low`

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

- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Mehira**
  - Haste buff (single target, high) [signature fuel]
  - ATK SPD via Haste buff (single target, high) [signature fuel]
  - Enables Enemy defeat via HP threshold strike
- **Pandora**
  - Healing (single target, high)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Fay**
  - ATK buff (multiple targets, low)
  - Healing (arc, high, conditional (frequent))
  - ATK SPD buff (multiple targets, low) [signature fuel]
- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]

### Units that can act as a replacement for Vala

**Buffs on allies**

- Damian (100% `Haste`)
- Gala (100% `Haste`)
- Hugin (100% `Haste`)

**Similar Skills**

- Athalia (50% `hp-scaling` `self-repositioner` `transformation`)

**Damage**

- Faramor (100% `True damage` `Physical` `HP loss`)
- Shadewing (81% `HP loss` `True damage`)
- Athalia (59% `True damage` `Physical`)

**Debuffs on enemies**

- Alna (60% `Haste debuff`)
- Eironn (60% `Haste debuff`)
- Hepler (60% `Haste debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Atalanta (100% `Stun`)

### Summary for Vala

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

- **Rowan**
  - ATK buff (single target, low)
  - Energy recovery (energy potion, start of battle) [signature fuel]
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

### Units that can act as a replacement for Valen

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Aurora (100% `Haste debuff`)
- Bonnie (100% `Haste debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Atalanta (100% `Stun`)

### Summary for Valen

#### Damage types dealt by Valen

- Primary damage type (unit): **Physical**
- Physical — Area, Single target

#### Debuffs provided by Valen

- Haste debuff (Supreme+) — Single target — `low`

#### Crowd Control provided by Valen

- Stun (Supreme+) — Single target — `medium`

#### Valen Provides

- Invincibility — Self
- Stacking buff (Mythic+) — Single target

## Valka

### Valka's behavior

- Movement: moving (avg attack range 1.0 tiles)
- Signature skill: Blooming Terror (ultimate) — stack fear + consume enemy
- Signature skill speed: fast
- Ultimate speed: fast
- Non-ultimate speed: fast

### Units Valka benefits from

Look for units providing: `ATK SPD / Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Lorsan**, or **Hugin**.

- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Fay**
  - ATK SPD buff (multiple targets, low) [signature fuel]
  - Healing (arc, high, conditional (frequent))
  - Enables Adjacent allies via Multiple ally buffs
- **Lucius**
  - Max HP via Shield (area, high)
  - Enables Adjacent allies via Shield (area)
- **Himmel**
  - Max HP buff (multiple targets, high)
  - Enables Adjacent allies via Multiple ally buffs
- **Zandrok**
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - Enables Adjacent allies via Multiple ally buffs

### Units benefitting from Valka

- Lyca

### Units that can act as a replacement for Valka

**Buffs on allies**

- Lyca (85% `ATK SPD`)
- Dunlingr (61% `ATK SPD` `Life Drain`)

**Similar Skills**

- Himmel (50% `ally-buffer` `ally-shielder`)

**Damage**

- Brutus (100% `Physical` `Max HP-based damage`)
- Gunnar (100% `Physical` `Max HP-based damage`)
- Himmel (100% `Physical` `Max HP-based damage`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Scarlita (100% `Stun` `Knock down`)

### Summary for Valka

#### Damage types dealt by Valka

- Primary damage type (unit): **Physical**
- Physical — Area, Self, Single target
- Max HP-based damage — Area — `low`

#### Buffs provided by Valka

- ATK SPD buff — Multiple targets — `high`
- Lifedrain buff (EX+10) — Single target — `low`

#### Crowd Control provided by Valka

- Unaffected — Self — On Skill
- Knock down — Area — `low`
- Stun — Area — `low`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Lucius**
  - Max HP via Shield (area, high)
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

### Units that can act as a replacement for Velara

**Buffs on allies**

- Mikola (100% `Healing` `Haste`)
- Antandra (72% `Healing`)
- Evie (72% `Healing`)

**Similar Skills**

- Solise (75% `ally-healer` `ally-shielder` `aoe-healing`)
- Fay (50% `ally-healer` `aoe-healing`)
- Hewynn (50% `ally-healer` `aoe-healing`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Alna (100% `Haste debuff`)
- Aurora (100% `Haste debuff`)
- Bryon (100% `Haste debuff`)

**Crowd Control**

- Arden (100% `Pin`)
- Callan (100% `Pin`)
- Cecia (100% `Pin`)

### Summary for Velara

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

Look for units providing: `Haste` `Healing`  
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
- **Hewynn**
  - Healing (all units, medium)

### Units that can act as a replacement for Viperian

**Buffs on allies**

- Brutus (100% `Life Drain`)
- Cecia (100% `Life Drain`)
- Daimon (100% `Life Drain`)

**Similar Skills**

- Arden (66% `aoe-damage` `dot-specialist`)
- Lorsan (66% `aoe-damage` `dot-specialist`)
- Cecia (50% `dot-specialist` `life-drain`)

**Damage**

- Alsa (100% `Magic`)
- Cassadee (100% `Magic`)
- Contess (100% `Magic`)

**Debuffs on enemies**

- Alsa (100% `Energy drain`)
- Berial (100% `Energy drain`)
- Contess (100% `Energy drain`)

### Summary for Viperian

#### Damage types dealt by Viperian

- Primary damage type (unit): **Magic**
- Magic — All units, Single target

#### Buffs provided by Viperian

- Lifedrain buff (EX+5) — Single target — `low`

#### Debuffs provided by Viperian

- Energy drain — Single target — `low`

#### Crowd Control provided by Viperian

- Unaffected — Self — Once

## Walker

### Walker's behavior

- Movement: moving (avg attack range 2.0 tiles)
- Signature skill: Six-Shot (ultimate) — multi-target burst shots
- Signature skill speed: slow
- Ultimate speed: slow
- Non-ultimate speed: fast

### Units Walker benefits from

Look for units providing: `Max HP` `CRIT` `CRIT DMG Boost` `Life Drain`  
Common buffers are **Twins**, **Lyca**, or **Hugin**.

- **Rowan**
  - Max HP buff (single target, high)
  - Energy recovery (energy potion, start of battle) [signature fuel]
- **Lucius**
  - Max HP via Shield (area, high)
- **Pandora**
  - Max HP buff (single target, low)
  - Energy recovery (single target, low) [signature fuel]
  - Energy recovery (1000 at battle start, single target) [signature fuel]
- **Cecia**
  - Max HP buff (single target, high)
  - Lifedrain buff (area, low)
  - ATK SPD buff (single target, low) [signature fuel]
- **Zandrok**
  - Lifedrain buff (area, low, conditional (frequent))
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]

### Units that can act as a replacement for Walker

**Damage**

- Shadewing (77% `HP loss` `Max HP-based damage`)
- Aliceth (61% `Physical` `HP loss`)
- Brutus (61% `Physical` `Max HP-based damage`)

**Debuffs on enemies**

- Nazrik (100% `Crit Resist debuff`)

**Crowd Control**

- Alsa (100% `Stun`)
- Antandra (100% `Stun`)
- Atalanta (100% `Stun`)

### Summary for Walker

#### Damage types dealt by Walker

- Primary damage type (unit): **Physical**
- Physical — Arc, Area, Self, Single target
- HP loss — Single target — `low`
- Max HP-based damage — Single target — `low`

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
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Lucius**
  - Max HP via Shield (area, high)
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

### Units benefitting from Zandrok

**11** units include this provider among their top 5 synergy partners. Why the match is common:

- **Haste** / **ATK SPD** buffs on multiple allies fuel slow signature skills via the signature-fuel weight

These are the **10** strongest pairings: 

- Nerion
- Carolina
- Seth
- Aurora
- Natsu
- Twins
- Viperian
- Hugin
- Pippa
- Shakir

### Units that can act as a replacement for Zandrok

**Buffs on allies**

- Damian (66% `Haste`)
- Hugin (66% `Haste`)
- Mikola (66% `Haste`)

**Similar Skills**

- Atalanta (66% `aoe-damage` `battle-start-burst`)
- Faramor (50% `aoe-damage` `hp-scaling`)
- Scarlita (50% `aoe-damage` `hp-scaling`)

**Damage**

- Aliceth (100% `Physical`)
- Alna (100% `Physical`)
- Antandra (100% `Physical`)

**Crowd Control**

- Antandra (100% `Stun`)
- Lucca (100% `Stun`)
- Lumont (100% `Stun`)

### Summary for Zandrok

#### Damage types dealt by Zandrok

- Primary damage type (unit): **Physical**
- Physical — Area, Multiple targets, Self, Single target

#### Buffs provided by Zandrok

- Haste buff — Area — `medium` — conditional (frequent)
- Lifedrain buff — Area — `low` — conditional (frequent)

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

**Buffs on allies**

- Koko (60% `Healing` `Max HP`)

**Similar Skills**

- Chippy (100% `summoner`)
- Florabelle (100% `summoner`)
- Damian (50% `summoner`)

**Damage**

- Alna (100% `DoT` `Physical`)
- Brutus (100% `DoT` `Physical`)
- Gunnar (100% `DoT` `Physical`)

**Debuffs on enemies**

- Brutus (75% `Phys DEF debuff` `DoT`)
- Kafra (75% `Phys DEF debuff` `ATK debuff`)
- Lyca (75% `Phys DEF debuff` `ATK debuff`)

**Crowd Control**

- Atalanta (100% `Move` `Stun`)
- Cassadee (100% `Move` `Stun`)
- Lenya (100% `Move` `Stun`)

### Summary for Zanie

#### Damage types dealt by Zanie

- Primary damage type (unit): **Physical**
- Physical — Self, Single target
- DoT — Area

#### Buffs provided by Zanie

- ATK SPD buff — Single target — `low` — conditional (rare)
- Healing — Single target — `high`
- Shield — Single target — `high`
- DEF Penetration buff (Legendary+) — Single target — `medium`
- Max HP buff (Mythic+) — Single target — `medium`

#### Debuffs provided by Zanie

- ATK debuff (Supreme+) — Single target — `low`
- DoT (Supreme+) — Single target — `low`
- Phys DEF debuff (Supreme+) — Single target — `medium`

#### Crowd Control provided by Zanie

- Move — Single target — `high`
- Stun — Single target — `low`

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

Look for units providing: `Haste` `Max HP` `Healing` `Energy`  
Common buffers are **Twins**, **Hugin**, or **Mikola**.

- **Smokey & Meerky**
  - Healing (multiple targets, medium)
  - Energy recovery (multiple targets, low) [signature fuel]
  - Enables Ally Ultimate casts via Energy recovery (Ultimate pace)
- **Zandrok**
  - Haste buff (area, medium, conditional (frequent)) [signature fuel]
  - ATK SPD via Haste buff (area, medium, conditional (frequent)) [signature fuel]
- **Gala**
  - Haste buff (single target, high) [signature fuel]
  - Max HP via Shield (single target, high)
  - ATK SPD via Haste buff (single target, high) [signature fuel]
- **Velara**
  - Haste buff (single target, low) [signature fuel]
  - Healing (area, low)
  - ATK SPD via Haste buff (single target, low) [signature fuel]
  - Enables Ally Ultimate casts via Start-of-battle Ultimate
- **Koko**
  - Max HP via Shield (all units, low)
  - Healing (multiple targets, high)

### Units that can act as a replacement for Zorya

**Similar Skills**

- Brutus (66% `hp-scaling` `life-drain`)
- Salazer (66% `hp-scaling` `life-drain`)
- Daimon (50% `hp-scaling` `life-drain`)

**Damage**

- Talene (100% `HP loss` `Magic`)
- Dunlingr (91% `HP loss` `Magic`)
- Niru (78% `Magic` `HP loss`)

**Crowd Control**

- Antandra (100% `Stun` `Knock down`)
- Lucca (100% `Stun` `Knock down`)
- Lumont (66% `Stun`)

### Summary for Zorya

#### Damage types dealt by Zorya

- Primary damage type (unit): **Magic**
- Magic — Arc, Area, Single target
- HP loss — Area — `high`

#### Buffs provided by Zorya

- Haste buff (Mythic+) — Single target — `medium`

#### Crowd Control provided by Zorya

- Steadfast — Self — Start of Battle
- Unaffected (EX+10) — Single target — On Skill
- Knock down — Arc — `medium`
- Stun — Area — `medium`

#### Zorya Provides

- Invincibility — Area

#### Zorya Requires

- Ally Ultimate casts (Mythic+) — Allies
