# Validation pitfalls

Reference from prior runs (`docs/validation-high-level-2026-06-11.md`,
`docs/validation-high-level-2026-06-15.md`,
`docs/validation-detailed-2026-06-15.md`). Definitions live in
`.cursor/AGENTS.md`.

## High-level label pitfalls

### Healing types missing or wrong

Pass 1 must check **Direct healing** and **Healing over time** (`healing_type:
direct` / `over_time`), not only damage and buffs.

**Missing heal label** — text restores HP but no `type: heal` effect:

- Himmel Hero Party — ally HP restore alongside shield
- Kafra Forest's Wrath — HoT within range
- Damian Inventor's Will — Haste buff present but HoT on EX tier missed

**Wrong heal type** — instant vs sustained swapped or spurious:

- Harak Vicious Bite — healing-lock cast drain tagged as Healing over time
- Lorsan Zephyr's Embrace — HoT present but Haste buff listed instead in
  findings when HoT was missing

**Heal vs buff** — restoration is not ATK buff, shield, or `stat_mod`:

- Himmel Blue-Moon Blessings — Penetration buff, not generic heal
- Koko Fulfilling Feast — Direct healing vs ATK buff

**Healing debuff** — cannot heal / healing reduction is a **debuff** label
(Gunnar Enhance Force, Niru Enhance Force), not a healing type.

**Shield ≠ heal** — absorb shields are **Shield** buffs (Hugin Titan's Aegis);
do not count as Direct healing unless text explicitly restores HP.

### Spurious damage riders

Execute thresholds, upgrade stat lines, and ally-attack riders parsed as
damage effects.

- Aliceth Sealed Fate — `stat_mod` / DEF Penetration as buff, not damage
- Athalia Unbroken Retribution — `max_hp` on true-damage execute line
- Dunlingr Harmonic Soundwall — `(ATK-based)` in shield text → Physical

**Audit:** ask whether the phrase describes damage **dealt to enemies** or
a stat/shield/execute rider.

### True vs Physical/Magic double-tag

`(ATK-based) … true damage` should not also emit normal Physical/Magic when
true damage is the scored hit.

Examples: Faramor Sanctified Circle, Himmel Heroic Slash, Shemira, Silven,
Valka.

**Convention:** prefer **true-only** when the strike is explicitly true.

### DoT false positives

Self or summon HP drain, periodic auto-attacks, and on-entry bursts are not
sustained enemy DoT.

- Harak Vicious Bite — healing-lock cast drain (also spurious HoT)
- Berial Shadow Reflection — Silhouette self HP cost (debatable)
- Carolina Snowball Witchery — discrete auto-shot cooldown
- Cryonaia Frozen in Time — domain-entry burst, not sustained DoT
- Evie Intel Chase — channeled magic per second stays **Magic**, not DoT

### DoT false negatives

Sustained `every Ns` / `per second` enemy damage without `dot` label.

- Bonnie Decay's Reach — max-stack Aging `100% every 1s`
- Arden vine skills (resolved in later pass but pattern recurs)

### HoT false positives

Healing-lock wording (`cannot be healed while…`) with `0%` self tick → not
Healing over time.

### Buff vs debuff swaps

- Aliceth Hero Focus — focus-fire mark is **Marked target**, not ATK buff
- Berial Hero Focus — **damage dealt** debuff, not damage taken
- Laios Intimidate — ally DEF buff spurious; enemy Phys/Magic DEF debuffs
  missing
- Cyran Mystic Recollection — enemy ATK SPD debuff, not ally ATK buff

### Upgrade-only lines skipped

Enhance Force, EX, Supreme+ often hold the only mention of CC, debuffs, or
damage types.

Watch: Contess, Dunlingr, Granny Dahnie, Nara, Niru, Pang, Zanie, Hewynn
Tranquility, Hugin Enhance Force.

### Mode / conditional branches

Second form, unlock branches, or mode-dependent ult text partially parsed.

- Natsu Lightning Fire Dragon's Roar — Fire Dragon King vs base mode
- Vala Checkmate — Skyblaster vs Sword branches
- Marilee Battlefield Learning — conditional true + ATK buff

### Empty effects on combat skills

Summon recast, artifact mimic, or shadow cast may belong on `synergy_profile`
only (Galahad Time Recast, Cyran artifact block). Do not always expect
`effects` rows.

### Scalar upgrade chunks

Tier lines that only bump numbers must not add **new** effect types.

Resolved pattern: Faramor/Lorsan/Cecia upgrade bumps should merge into
existing effects, not duplicate DoT/Magic rows.

## Detailed value pitfalls

### Heal magnitude `0%`

Restoration text present but `value: 0` — very common (~many skills).

Examples: Alna Shared Resolve, Berial Shadow Trick, Marcille Magical Flash,
Niru Spirit Devour, Sylphira Harmonic Refrain, Talene Radiant Resurgence.

**Always check** `Direct healing` and ally-targeted heals first.

### DoT tick defaults to `1`

`every 0.25s` / `every 0.5s` stored as `tick: 1`.

Examples: Alna Winter Anthem, Berial shadow phase, Cryonaia storms, Cyran
black hole, Faramor circle, Gwyneth burn, Lorsan storm.

### Flat `+ X%` as max-HP magnitude

Additive rider duplicated or mis-split from main ATK-based hit (marksmen,
Aliceth Radiant Rain, Athalia).

**Correct split:** main hit in physical/magic; **only** the `+Y%` max-HP
clause in `max_hp`.

### Targeting collapsed to `single`

Path AOEs, adjacent tiles, penetrating lines, `all enemies` → wrong `single`.

Examples: Atalanta Wild Sniper (line), Dionel Starry Void (penetrating line),
Bonnie Deathmark Arrow (all enemies), Mehira Blissful Whip (arc),
Granny Dahnie Threshold (area zone).

### `target_count` placeholder `3`

`Multiple targets` default when text says **2** enemies/allies, or support
skills with vague "multiple".

Examples: Contess, Arden Entangling Vines, Marilee Mid-Air Shot, Himmel
Heroic Dash.

### Missing durations on timed effects

Haste/DEF/movement debuffs, shields, damage reduction, frighten, taunt often
lack `duration` when text gives seconds.

### Knock down `duration: 0`

Knock-down CC should get a brief lock duration when text implies it (Antandra
Shield Assault, Callan Flail Slam, Harak, Himmel Heroic Dash).

### Default `area_count: 2`

Explicit 1-tile or 3-tile wording keeps parser default of 2.

Examples: Faramor Sanctified Circle (should be **1**), Dunlingr frontal wave,
Himmel Heroic Slash (should be **3**).

### Self vs ally mis-targeting

Dodge, Crit, heals, DEF buffs, **Invincible**, and immunity on wrong `target`.
Ally mis-tags on **damage dealers** are high impact: they pollute
`heroes_data_synergies.json` replacement `"buff"` lists even when the label
is otherwise correct.

**Invincible / immunity — read the clause, not the skill title:**

| Skill | Text cue | Wrong | Correct |
|-------|----------|-------|---------|
| Harak Tidal Assault | `reaching the invincible` (self dive) | `target: ally` | `Self` |
| Aurora Starlit Slumber | `Aurora stays invincible` while asleep | `target: ally` | `Self` |
| Harak Flesh Feast | `enters feast mode, increasing Crit` | `target: ally` | `Self` |
| Evie (ult) | `{name} is invincible` (caster) | `target: ally` | `Self` |

Phrasing that often means **Self** but is easy to miss (no `{name} is
invincible` pattern):

- `stays invincible`
- `reaching the invincible`
- `while casting, … remains unaffected`
- `enters feast mode, increasing Crit/Haste`

**Synergy false positive:** two heroes with the same mis-tag (e.g. Harak +
Aurora both storing self Invincible as `ally`) score as **Buffs on allies**
replacements for each other. After fixing targeting, re-grep
`data/heroes_data_synergies.json` for the hero under `"replacements"."buff"`.

**Summon vs ally:** Aurora Haste and Summon damage buff use `target: summon`.
They are valid ally *support* in synergy scoring but must not be validated as
`target: ally` rows, and they do not fill the replacement **Buffs on allies**
profile (which uses standard ally targetings only).

Other examples: Eironn Tempest Guard (Dodge → Self), Hewynn Healing Wave
(weakest ally), Marcille Hero Focus (Haste → Self).

### Upgrade-tier magnitudes not merged

Max-tier EX/Supreme shield/heal/damage values missing; base tier kept.

Examples: Cryonaia Frostveil Domain, Carolina Ice Vortex, Lucius shields,
Koko Fluffy Shield.

### Multi-phase skills collapsed

Shadow phase vs exit burst (Berial), dash path vs target (Athalia), arc +
sweep (Alna Wild Whirl), mode branches (Natsu, Vala).

**Audit:** read passive + active + upgrade as one timeline, not one effect row.

### HoT vs direct heal

Sustained recovery stored as instant or wrong target.

Examples: Alna Winter Anthem (HoT + Winter Warrior), Damian Inventor's Will,
Fay Healing Gemstones, Hewynn Rain Prayer.

### Flat stat points as percentages

Life Drain, Haste, ATK SPD, Crit DMG Boost, Vitality — flat `+N` stored as
`N%` or omitted.

Examples: Kordan Life Drain, Indris ATK SPD, Lenya Crit DMG Boost, Lorsan
Haste reduction (-33 flat).

### Passive / upgrade-only effects empty

EX/Supreme lines with numbers but no `effects` row.

Examples: Evie Tactical Briefing, Hewynn Revitalize, Galahad Time Recast,
Talene Divine Conflagration, Valen Unseen Blade.

## Spot-check anchors

Use these to calibrate both passes:

| Skill | High-level expectation | Detailed nuance |
|-------|------------------------|-----------------|
| Kazim Gale Barrage | Max HP-based damage | **+40%** max tier, not +140% base |
| Harak Vicious Bite | No DoT/HoT | Healing debuff from lock |
| Harak Tidal Assault | Invincible Self | Not ally buff; no replacement buff match |
| Aurora Starlit Slumber | Invincible Self; Haste on summons | Self sleep immunity ≠ ally buffer |
| Faramor Sanctified Circle | True + DoT; no Physical | area_count 1; 0.5s tick |
| Lorsan Whispering Tempest | DoT + Haste debuff | -33 flat; 5s / 0.5s tick |
| Chippy (all skills) | Clean label pass | No targeting/magnitude issues |
| Bonnie Decay's Reach | DoT at max Aging | DoT value/duration tiering |
| Athalia Unbroken Retribution | True + HP loss | No spurious max_hp; path dash |
| Berial Shadow Reflection | Energy drain only | Not enemy DoT |

## High-level vs detailed gap

Labels can be correct while values/targeting remain wrong. Document both;

do not close a detailed finding because high-level passed.

Example table pattern:

| Skill | High-level | Detailed still open |
|-------|------------|---------------------|
| Lorsan Whispering Tempest | DoT + Haste debuff OK | Haste -33; 5s / 0.5s tick |
| Faramor Sanctified Circle | True damage OK | area_count, tick, magnitude |
| Florabelle Overgrowth | Haste + Lifedrain OK | flat Life Drain 100; 10s |

## Debatable cases

Note ambiguity instead of forcing a single expected value:

- **Berial Shadow Reflection** — self HP drain on Silhouette: self-cost vs
  enemy DoT
- **Aurora Plushification** — bind duration when source tiers conflict
- **Shemira Ghastly Tribute** — context-dependent true/max-HP cap

## Regression tests after fixes

Prior passes added tests in:

- `scripts/test_detect_damage_types.py`
- `scripts/test_skill_descriptions.py`
- `scripts/test_detailed_validation.py`
- `scripts/test_summary_parsing.py` — self Invincible (Evie, Harak, Aurora)

Add a **minimal** case per new pattern; run `just validate` before closing
the validation task. When detection rules change, bump
`scripts/roster_analysis.py` `CACHE_VERSION` before `just analyze`.
