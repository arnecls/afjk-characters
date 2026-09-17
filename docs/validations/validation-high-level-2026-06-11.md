# High-level validation — 2026-06-11

Scope: compare detected **damage types**, **CC types**, **buff labels**, and **debuff
labels** per skill in `data/heroes_data_processed.json` against each skill's
`description`. No values, timings, or targeting checked.

Roster: **116 heroes**, ~**680 skills**. Skills with discrepancies: **~120**
(~18%).

## Common failure patterns

1. **Spurious damage** — execute thresholds or ally-attack riders parsed as
   Physical (e.g. Aliceth Sealed Fate, Athalia Unbroken Retribution).
2. **True vs Physical/Magic** — true-damage phrases classified as normal damage
   (Dionel, Faramor, Koko, Shemira, Silven, Valka, Pippa).
3. **Missing CC** — bind/sleep/knock-down/silence/charm not emitted
   (Aurora, Bryon, Cyran, Mehira, Saida, Ulmus, Gerda, Indris).
4. **Wrong CC type** — bind vs sleep (Gerda), ATK debuff vs frighten (Pandora).
5. **Missing debuffs from tier upgrades** — Enhance Force / Ex lines often
   partial (Contess, Dunlingr, Granny Dahnie, Nara, Niru, Pang, Zanie).
6. **DoT vs Magic only** — sustained damage not tagged as DoT (Arden, Berial,
   Cryonaia, Harak, Marcille, Saida).
7. **Mis-assigned target** — enemy DEF reduction detected as ally DEF buff
   (Laios Intimidate, Cyran Mystic Recollection).
8. **Empty effects on combat skills** — passive_only or unprocessed CC
   (Mehira Alluring Mirage → Charm missing).
9. **Poison / DoT naming** — Odie skills detect DoT but not Poison debuff label.
10. **Conditional / mode-split text** — second-form or unlock branches skipped
    (Natsu Fiery Ties, Marilee Battlefield Learning).

## Findings

Format: `Character, Skill, found, expected`

### Batch A–Damian

Aliceth, Hero Focus, Marked target (focus fire), none
Aliceth, Sealed Fate, physical, none
Alna, Winter Anthem, physical, dot
Alsa, Don of Terra, Energy drain, none
Antandra, Spear Barrage, none, ATK debuff
Arden, Entangling Vines, magic, dot
Arden, Force of Nature, magic, dot
Atalanta, Sleight of Hand, none, ATK debuff
Athalia, Unbroken Retribution, physical, none
Athalia, Unbroken Retribution, ATK debuff, none
Aurora, Plushification, none, bind
Baelran, Celestial Rise, physical, none
Baelran, Sanctified Surge, none, true
Berial, Scared Swamp, magic, dot
Berial, Hero Focus, none, damage dealt debuff
Bonnie, Decay's Reach, none, dot
Bryon, Shadow Flash, none, Energy drain
Bryon, Tacit Strike, none, stun
Carolina, Freezing Nova, none, Haste debuff
Carolina, Enhance Force, none, Haste debuff
Cassadee, Tidal Strength, none, Tidal Strength buff
Cecia, Trial of Thorns, none, Phys DEF debuff
Cecia, Trial of Thorns, none, Magic DEF debuff
Cecia, Trial of Thorns, none, Vitality debuff
Chippy, Eureka!, none, physical
Contess, Detention Pass, none, Exemption buff
Contess, Detention Pass, none, hp_loss
Contess, Mandatory Civility, none, ATK debuff
Contess, Quiet Period, none, Energy recovery debuff
Contess, Hero Focus, none, Energy recovery debuff
Contess, Expulsion Notice, none, hp_loss
Cryonaia, Frostveil Domain, magic, none
Cryonaia, Icicle Tempest, magic, dot
Cyran, Cursed Grasp, none, knock_down
Cyran, Mystic Recollection, magic, none
Cyran, Mystic Recollection, ATK debuff, ATK SPD debuff
Cyran, Mystic Recollection, none, Haste buff
Cyran, Mystic Recollection, none, magic
Daimon, Dolly Defender, magic, physical
Daimon, Playtime Plunder, max_hp, true
Daimon, Guardian Howl, max_hp, dot
Damian, Inventor's Will, none, Haste buff

### Batch Dionel–Hewynn

Dionel, Celestial Spear, Physical, True damage
Dunlingr, Grand Resonance, ATK debuff, Haste debuff
Dunlingr, Harmonic Soundwall, Magic, none
Dunlingr, Enhance Force, none, Magic
Dunlingr, Enhance Force, Energy drain, Energy drain + Haste debuff + Vitality debuff
Eironn, Tempest Guard, Shield, Shield + Dodge chance buff
Evie, Intel Chase, DoT (debuff), none
Evie, Intel Chase, none, Magic
Evie, Pointed Proof, none, Magic DEF debuff
Faramor, Sanctified Circle, Physical, True damage
Florabelle, Overgrowth, Lifedrain buff, Haste buff + Lifedrain buff
Frieren, Enhance Force, Knock down, Knock up + Knock down + Magic
Galahad, Temporal Field, none, Haste debuff + Movement speed debuff
Gerda, Splashing Fun, Bind, Sleep
Granny Dahnie, Threshold of Jade, none, Physical
Granny Dahnie, Threshold of Jade, none, Energy drain
Granny Dahnie, Enhance Force, ATK debuff, ATK debuff + Haste buff
Gunnar, Annihilation Directive, ATK buff, ATK buff + Attack range buff
Gunnar, Annihilation Directive, none, Vitality debuff
Gunnar, Enhance Force, Shield, cannot heal/gain shields debuff
Gwyneth, Flare Arrow, DoT, DoT + Vitality debuff
Harak, Vicious Bite, none, DoT
Harak, Vicious Bite, none, Healing debuff
Hepler, Remedial Class, Haste buff, none
Hewynn, Tranquility, none, Damage taken reduction

### Batch Himmel–Lyca

Himmel, Heroic Slash, Max HP-based damage, True damage
Himmel, Heroic Dash, Physical, Knock down
Himmel, Hero Party, Shield + Physical, ATK buff + Direct healing
Himmel, Blue-Moon Blessings, ATK buff + Max HP buff + Direct healing, Penetration buff
Himmel, Enhance Force, none, HP loss
Hodgkin, Rending Cleave, Physical, Energy drain
Hodgkin, Ardent Believers, Physical + Energy drain, Max HP-based damage
Hugin, Titan's Aegis, none, Shield
Hugin, Enhance Force Hugin, none, Damage taken reduction
Indris, Spellbane Shot, Physical + Phys DEF debuff + Magic DEF debuff, Silence + Max HP-based damage
Kafra, Forest's Wrath, Phys DEF debuff + Marked target (focus fire), Healing over time
Koko, Full Energy, Lifedrain buff + Damage taken reduction, True damage + ATK buff
Koko, Fulfilling Feast, Direct healing, ATK buff
Korin, Vine Arms, ATK SPD buff, Max HP-based damage
Kruger, Smashing Assault, Physical, Phys DEF debuff
Kruger, Ruthless Vanguard, Shield, Lifedrain buff
Kruger, Enhance Force, none, ATK buff
Laios, Living Armor - Kensuke, none, Physical
Laios, Intimidate, Bind + DEF buff (ally), Phys DEF debuff + Magic DEF debuff (enemy)
Lorsan, Whispering Tempest, Magic, DoT + Haste debuff
Lorsan, Zephyr's Embrace, Healing over time, Haste buff
Ludovic, Lifeweaver's Blooms, Magic, Max HP-based damage + HP loss
Ludovic, Ethereal Blooms, Magic, Max HP-based damage
Lumont, Lumont's Charge, Physical + Taunt, Knock back
Lyca, Nova Fall, Physical + Phys DEF debuff + ATK debuff, Phys DEF debuff only

### Batch Marcille–Rhys

Marcille, Silver-White Wings that Streak Across the Skies, Haste buff, Haste buff + Energy recovery
Marcille, Ancient Magic, Magic, Magic + DoT
Marilee, Hyperfocus, ATK buff, ATK buff + ATK SPD buff
Marilee, Hero Focus, Crit buff + Crit DMG boost, Crit DMG boost
Marilee, Battlefield Learning, ATK buff, ATK buff + True damage
Mehira, Blissful Whip, Haste buff, Haste buff + HP loss
Mehira, Hero Focus, Max HP buff, Lifedrain buff
Mehira, Alluring Mirage, none, Charm
Mikola, Dauntless Hymn, Haste buff, Haste buff + Ranged DEF buff
Mikola, Passionate Opening, Vitality buff, Vitality buff + Physical
Nara, Eerie Execution, none, Max HP-based damage
Nara, Enhance Force, Energy recovery + Unaffected + Vitality debuff, + Max HP debuff
Natsu, Fiery Ties, ATK buff + Crit buff + Crit DMG boost, + DEF buff
Nazrik, Rend Rupture, True damage + Physical, + Marked target (focus fire)
Nazrik, Savage Wound, True damage + Physical + Max HP debuff, + Max HP-based damage
Nerion, Drowning Doom, Magic, Magic + ATK buff + ATK SPD buff
Nerion, Tidal Rebuke, Magic + Stun, + Knock back
Nerion, Riptide Wrath, Magic, Magic + Knock up
Nerion, Abyssal Embrace, Magic + Shield + ATK debuff, + Haste debuff
Niru, Spirit Devour, Magic, Magic + Max HP-based damage
Niru, Enhance Force, DEF buff, DEF buff + Healing debuff
Odie, Corrosive Dart, Magic + DoT, + Poison debuff
Odie, Venom Surge, DoT, Poison debuff
Odie, Heart Crusher, DoT, Poison debuff
Pandora, Panic Projection, ATK debuff, Frighten + HP loss + ATK debuff
Pandora, Boxed Blessing, Invincible + Energy recovery, + ATK buff + Displace
Pandora, Tainted Tribute, Magic + Vitality debuff + Damage taken debuff + Haste debuff, debuffs only (no Magic)
Pandora, Eternal Legacy, Energy recovery + ATK debuff, + Unaffected
Pang, Sky Splitter, Physical + Stun + ATK buff + Haste buff + Unaffected, + Energy recovery debuff
Pang, Zen Ward, Physical + Unaffected, Physical + Shield + Unaffected
Pang, Spirit Sync, Shield, Shield + ATK buff
Parisa, Floral Splendor, Magic, Magic + Marked target (focus fire)
Perseus, Spear-Shield Combo, Physical, Physical + Shield + ATK SPD buff
Perseus, Fertile Ground, ATK buff + Max HP buff, + DEF buff
Phraesto, Futile Echo, Magic, Magic + Damage taken reduction
Phraesto, Crimson Contract, Magic + Shield + Damage taken reduction, + Energy recovery
Phraesto, Vicious Sting, Magic + Max HP buff, Magic + Haste debuff + Vitality debuff + Max HP-based damage
Pippa, Mage's Bloom, Bind, Bind + True damage
Pippa, Enhance Force, Bind + Displace, + Max HP-based damage
Reinier, Mutual Reflection, Magic + Displace + Unaffected + Steadfast, Magic + Displace
Reinier, Golden Ratio, Magic + Interrupt + Knock up, + HP loss

### Batch Rowan–Zorya

Saida, Deepening Roots, cc: none + damage: Magic, cc: Bind + damage: DoT
Saida, Seed Siphon, cc: Displace, cc: Bind
Satrana, Ignite Passions, none, Max HP-based damage
Shadewing, Withering Curse, none, Max HP-based damage
Shemira, Ghastly Tribute, Magic + Max HP-based damage, True damage + Max HP-based damage
Shemira, Spectral Barrier, Magic + Max HP-based damage, True damage
Silven, Tempered Field, Magic + Max HP-based damage, True damage + Max HP-based damage
Sinbad, Tracker's Instincts, Damage taken debuff, ATK debuff + Damage taken debuff
Solise, Resonant Bloom, DEF buff, ATK buff + DEF buff + Max HP buff
Sylphira, Harmonic Refrain, none, True damage
Talene, Divine Conflagration, Magic, Magic + HP loss
Ulmus, Prowling Roots, none, Bind
Valka, Phantom Slasher, Max HP-based damage + Physical, True damage
Valka, Phantom Slasher, none, Haste debuff
Walker, Bounty Pursuit, Physical, Physical + HP loss
Zandrok, Shock Stomp, none, Max HP-based damage
Zanie, Enhance Force, none, DoT

## Spot-checked confirmations

- **Laios Intimidate** — bind present; ally DEF buff spurious; enemy Phys/Magic
  DEF debuffs missing (description: "reduction in both Phys DEF and Magic DEF").
- **Mehira Alluring Mirage** — `effects: []`, `passive_only: true`; description
  says "bewitching" → Charm expected.
- **Aurora Plushification** — only Unaffected immunity; "unable to move or
  attack" → Bind expected.
- **Saida Deepening Roots** — Ex burst has Magic; trap + per-second HP loss →
  Bind + DoT expected.
- **Aliceth Sealed Fate** — spurious Physical from execute threshold parsing.

## Next step

Detailed validation (targeting, area, timings, magnitudes) per AGENTS.md — not
included here.
