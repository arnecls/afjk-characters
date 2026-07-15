# High-level validation — 2026-07-15

Scope: manual comparison of detected damage types, healing types, CC types,
buffs, debuffs, and immunities in `data/heroes_data_processed.json` against
every skill's full source description in `data/heroes_data.json`. Targeting,
geometry, duration, tick interval, and magnitude are reserved for the detailed
pass.

Roster: **119 heroes**, **708 skills**. All skills were read in four
alphabetical batches. **129 skills (18.2%)** have at least one label
discrepancy, comprising **161 effect-level finding rows**.

Baseline: [validation-high-level-2026-06-30.md](validation-high-level-2026-06-30.md).
That report covered 117 heroes / 696 skills and excluded damage and healing
types.

## Pre-scan results

| Pre-scan | Start count |
| --- | ---: |
| Ally-target self-effect candidates | 3 |
| Self-target ally-buff candidates | 0 |
| Self-debuff (`target: self`) | 0 |
| Spurious immunity (target-priority wording) | 0 |
| Artifact Silence CC | 0 |
| True + Max HP double-label | 1 |
| Heal `value: 0` | 0 |
| DoT tick 1s with 0.25s/0.5s source text | 10 |
| Knock down `duration: 0` | 0 |

The three ally-target candidates are Contess Detention Pass (heal and shield)
and Smokey & Meerky Special Aroma (heal). They require clause-level targeting
review in the detailed pass. The True + Max HP candidate is Nara Crimson
Vengeance; manual review confirms cross-skill tier bleed from Eerie Execution.

## Resolved since 2026-06-30

- No self-targeted debuff rows remain.
- No targeting-priority immunity or artifact-Silence false positives remain.
- No heal effects remain at `value: 0`.
- No knock-down rows remain at `duration: 0`.
- Prior tricky fixes still hold for Seth Hunter Instinct, Granny Dahnie
  Glimmerbloom Blessings, Kafra Sylvan Banishment, Cyran Cursed Grasp,
  Shemira Ghastly Tribute, Valka Phantom Slasher, and Harak Tidal Assault.

## Common failure patterns

1. **Upgrade-only effects skipped** — EX, Supreme+, and Hero Focus lines often
   contain the only heal, stat effect, CC, immunity, or damage conversion.
2. **Cross-skill tier bleed** — an upgrade is attached to the named base skill
   instead of Enhance Force, or to a skill referenced by the upgrade text.
3. **Healing gaps** — direct heals and HoTs are absent, confused with the
   Healing stat, or swapped with healing-prevention debuffs.
4. **HP-scaling hierarchy gaps** — current/max/lost-HP riders are omitted or
   represented as generic Magic, Physical, DoT, or True damage.
5. **Immunity vocabulary loss** — explicit Invincible, Immune, Steadfast,
   Untargetable, and Cleanse clauses are omitted or reduced to Unaffected.
6. **Sustained damage loses its base type** — several DoT rows omit the
   underlying Magic or Physical type.
7. **Empty active/passive combat sections** — several multi-phase,
   normal-attack replacement, and state skills have no structured effects.

## Findings

Format: `Character (Skill): found -> expected`.

### Batch 1 — Aliceth–Florabelle

31 heroes, 183 skills; **24 skills**, **29 finding rows**.

- Aliceth (Radiant Rain): Unaffected -> Invincible.
- Aliceth (Aegis Wings): none -> Invincible.
- Alna (Winter Anthem): Direct healing -> Healing over time.
- Alna (Chilling Presence): Bind + Vitality debuff -> remove from this skill.
- Alna (Enhance Force): none -> Bind + Vitality debuff.
- Athalia (Unbroken Retribution): Unaffected -> Invincible.
- Athalia (Vengeance Charge): Unaffected -> Invincible.
- Baelran (Celestial Rise): Physical + True -> True only for the active arc.
- Berial (Scared Swamp): none -> Invincible.
- Berial (Shadow Trick): none -> Invincible.
- Brutus (Indomitable): Unaffected only -> add Immune.
- Bryon (Shadow Flash): Energy only -> add Magic.
- Bryon (Tacit Strike): none -> Direct healing + Healing over time +
  Untargetable on the EX fatal-blow clause.
- Callan (Eternal Watch): none -> damage type for the golem-might strike.
- Callan (Hollowed Wrath): Stun + Unaffected only -> add damage type.
- Damian (Inventor's Will): Haste only -> add Healing over time.
- Dunlingr (Echo of Silence): DoT -> Magic burst, no DoT.
- Dunlingr (Grand Resonance): Haste debuff -> ATK SPD debuff.
- Evie (Foretold Favor): Direct healing only -> add Healing over time for the
  per-second quill.
- Evie (Tactical Briefing): none -> Magic damage debuff.
- Evie (Pointed Proof): debuffs only -> add Magic.
- Fay (Blinding Light): none -> Phys/Magic DEF buffs and debuffs.
- Fay (Enhance Force): none -> Direct healing.
- Cyran (Gravitic Requiem): Execution debuff + Crit buff -> remove both
  cross-clause/cross-skill labels.

### Batch 2 — Frieren–Lucius

30 heroes, 177 skills; **41 skills**, **48 finding rows**.

- Frieren (Zoltraak): DoT + True only -> add Magic.
- Frieren (Lightning: Judradjim): none -> Damage dealt buff + ATK buff.
- Frieren (Defensive Spell): Haste only -> add Damage taken reduction.
- Galahad (Binding Loop): Magic + Bind -> add HP loss.
- Galahad (Chrono Ward): Magic only -> add Shield.
- Gerda (Splashing Fun): Sleep + Bind -> Sleep only.
- Granny Dahnie (Threshold of Jade): none -> Direct healing.
- Granny Dahnie (Seed Cannon): Direct healing -> remove from this skill.
- Granny Dahnie (Enhance Force): none -> Direct healing.
- Gunnar (Annihilation Directive): none -> Steadfast.
- Gunnar (Absolute Defense): ATK SPD only -> add Shield.
- Gwyneth (Flare Arrow): DoT + Vitality debuff -> add Physical.
- Gwyneth (Fulgur Flare): Phys DEF debuff -> remove; ignoring reduction is not
  applying a debuff.
- Hammie (You'll Be Fine): ATK buff only -> add Direct healing.
- Hewynn (Rain Prayer): Unaffected -> remove from this skill.
- Hewynn (Tranquility): none -> Unaffected.
- Hewynn (Revitalize): none -> Direct healing + Cleanse.
- Himmel (Hero Party): Basic stats + Physical -> add Shield + Direct healing.
- Himmel (Hero Focus): none -> Haste buff.
- Himmel (Blue-Moon Blessings): ATK + Max HP -> add Penetration + Direct
  healing + Cleanse.
- Himmel (Enhance Force): Damage taken debuff -> remove; clause amplifies boss
  HP loss.
- Hodgkin (Phantom Respite): HoT only -> add physical-damage immunity.
- Hugin (Titan's Aegis): Energy buff -> remove from this skill.
- Hugin (Steelbound Kinship): none -> control Immune.
- Igor (Funereal Ring): Physical only -> add Steadfast.
- Igor (Ghastly Explosion): healing debuff -> remove; add Invincible.
- Indris (Spellbane Shot): none -> Silence.
- Kafra (Forest's Wrath): none -> Healing over time.
- Koko (Full Energy): none -> True damage.
- Koko (Fluffy Shield): none -> Cleanse.
- Kordan (Dominance Ring): none -> Damage taken reduction.
- Kordan (Fury Slash): Physical only -> add Shield.
- Kordan (Rage Unleashed): none -> HP loss.
- Kruger (Ruthless Vanguard): Lifedrain only -> add Shield + Immune.
- Kruger (Enhance Force): none -> ATK buff.
- Kulu (Bombs Away!): Physical only -> add Max HP-based damage.
- Lorsan (Whispering Tempest): DoT only -> add Magic.
- Lorsan (Zephyr's Embrace): Unaffected -> remove; add Dodge buff.
- Lorsan (Turbulent Resurgence): Stun only -> add Direct healing.
- Lucca (Courageous Call): Direct healing -> remove from this skill.
- Lucius (Hero Focus): Direct healing -> Healing stat buff only, no heal.

### Batch 3 — Lucy–Scarlita

30 heroes, 180 skills; **36 skills**, **44 finding rows**.

- Lucy (Hero Focus): none -> Haste buff.
- Lucy (Water Barrier): none -> Ranged DEF buff.
- Ludovic (Lifeweaver's Blooms): Magic + Max HP-based -> HP loss on active;
  remove passive nutrient-absorb damage labels.
- Ludovic (Ethereal Blooms): Magic -> HP loss.
- Lyca (Enhance Force): none -> Phys DEF debuff.
- Marcille (Magical Flash): none -> Direct healing.
- Mehira (Total Devotion): none -> Direct healing.
- Mehira (Alluring Mirage): Damage taken debuff -> remove from this skill.
- Mehira (Enhance Force): none -> Damage taken debuff.
- Mikola (Heroic Duel): none -> Healing over time.
- Mikola (Passionate Opening): none -> Magic.
- Nara (Crimson Vengeance): Max HP-based -> remove from this skill.
- Nara (Eerie Execution): none -> Max HP-based damage.
- Nara (Enhance Force): none -> Vitality debuff + Unaffected.
- Natsu (Lightning Fire Dragon's Iron Fist): Haste buff -> Haste debuff.
- Nazrik (Staggering Strike): Direct healing -> Healing debuff.
- Nazrik (Savage Wound): none -> Max HP-based damage.
- Niru (Spirit Devour): Magic only -> add Max HP-based damage + Direct healing.
- Niru (Enhance Force): Direct healing -> Healing debuff.
- Odie (Venom Surge): DoT -> remove; skill amplifies existing poison.
- Pandora (Panic Projection): DoT -> HP loss.
- Pang (Radiant Fist): Physical only -> add HP loss.
- Perseus (Fertile Ground): buffs only -> add Direct healing.
- Perseus (Spear-Shield Combo): Physical only -> add Shield + ATK SPD buff.
- Phraesto (Futile Echo): Magic only -> add Direct healing.
- Phraesto (Vicious Sting): Magic + DoT + Vitality -> add Haste debuff +
  Healing over time.
- Pippa (Botanical Woe): Magic + Energy debuff -> add DoT.
- Reinier (Mutual Reflection): Steadfast + Unaffected -> remove both.
- Reinier (Golden Ratio): Magic + CC only -> add HP loss + Direct healing.
- Reinier (Hero Focus): ATK debuff only -> add ATK buff.
- Rhys (Defensive Stance): buffs + Immune -> add Direct healing.
- Rowan (Great Bargain): stat buffs only -> add Direct healing.
- Salazer (Rain of Blades): Physical + Lifedrain -> add HP loss.
- Satrana (Ignite Passions): Vitality debuff only -> add DoT.
- Scarlita (Divine Wrath): none -> True damage.
- Scarlita (Enhance Force): none -> Phys/Magic DEF buff.

### Batch 4 — Seth–Zorya

28 heroes, 168 skills; **28 skills**, **40 finding rows**.

- Shadewing (Withering Curse): none -> Max HP-based damage.
- Shadewing (Curse Feast): none -> True damage conversion.
- Shadewing (Enhance Force): Lifedrain only -> add ATK + Shield.
- Shadewing (Crimson Venom): Energy -> remove from this skill.
- Seth (Predator's Lunge): Energy -> remove from this skill.
- Shemira (Phantom Procession): Magic only -> add Direct healing.
- Shakir (Wolf's Will): Lifedrain + Unaffected -> add Ranged DEF + ATK buff.
- Silvina (Blade Vortex): none -> Physical.
- Sinbad (Tracker's Instincts): none -> ATK debuff.
- Sonja (Crimson Covenant): ATK + Magic DEF -> add Phys DEF + Immune.
- Sonja (Enhance Force): none -> Direct healing.
- Sonja (Tempest Thrusts): Physical + Haste -> add Immune.
- Soren (Dusk Rejuvenation): Haste only -> add Healing over time + Energy +
  Cleanse.
- Sylphira (Harmonic Refrain): True -> Max HP-based; add Direct healing.
- Talene (Divine Conflagration): none -> Magic + DoT + HP loss.
- Talene (Radiant Resurgence): Magic + Lifedrain -> add Direct healing +
  passive Magic.
- Talene (Blazing Ascension): Magic + Knock back -> add Healing over time.
- Tasi (Eternal Dreamscape): DoT + Sleep -> add Magic.
- Tasi (Fluttering Dream): DoT + HoT -> add Magic + Invincible.
- Temesia (Invincible Fury): Unaffected + HoT -> add True damage conversion.
- Temesia (Iron Heel): damage + debuff only -> add Direct healing.
- Thador (Moonveil Manifest): Physical only -> add Crit DMG DEF debuff +
  Direct healing.
- Viperian (Soul Ravager): Magic only -> add Direct healing.
- Walker (Aerial Thunder): Crit Resist debuff only -> add Phys DEF debuff.
- Walker (Bounty Pursuit): Physical + Crit + Damage taken -> add HP loss.
- Zandrok (Hunter's Fury): none -> Max HP-based damage.
- Zorya (Devouring Strike): damage + Lifedrain -> add Direct healing.
- Zorya (Guardian's Ring): Magic + HoT + Energy + Steadfast -> add Invincible +
  ATK buff.

## Spot-checked confirmations

- Chippy's three skills remain clean Physical hits without spurious special
  damage or utility.
- Daimon Playtime Plunder and Shemira Ghastly Tribute retain Max HP-based
  damage without generic True double-labels.
- Faramor Sanctified Circle retains True + HP loss + DoT labels without
  spurious Physical; its tick and area remain detailed-pass concerns.
- Bonnie Decay's Reach retains Magic + DoT + ATK/Haste debuffs at full stacks.
- Harak Vicious Bite retains HP loss and healing prevention without spurious
  DoT/HoT; Tidal Assault Invincible remains Self.
- Cyran Cursed Grasp has CC but no immunity rows from target-priority wording.
- Seth Hunter Instinct retains DEF and Crit buffs on Self without a self-debuff.
- Valka Phantom Slasher retains Max HP-based damage without generic True.

## Fix priorities

1. Heal and healing-debuff label gaps.
2. HP-loss / Max HP / True hierarchy and cross-skill tier bleed.
3. Missing or wrong immunities and Cleanse.
4. Upgrade-only and empty combat sections.
5. Missing base damage type on sustained damage.

The detailed pass follows this baseline and separates target/value errors from
these label findings.

## Fixes applied in this run

- Resolved Nara's sole True + Max HP pre-scan hit by moving the max-HP
  shockwave to Eerie Execution; Crimson Vengeance retains its legitimate
  Physical/conditional True branches.
- Corrected Self/ally targets for existing valid effects. This does not close
  missing-label findings, but prevents those valid rows from corrupting
  ally-buff and ally-heal profiles.
- Kept the full findings tables as the start-of-pass baseline. Findings not
  covered by the completed pattern groups remain open.
