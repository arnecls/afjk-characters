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

Examples: Faramor Sanctified Circle, Himmel Heroic Slash, Silven, Valka.

**Convention:** prefer **true-only** (drop Physical/Magic) when the strike is
explicitly true without a separate ATK-based component.

### True vs Max HP-based double-tag

`true damage equal to X% (+ Y%) of max HP` is one strike — store **Max
HP-based damage only**, not generic **True damage** alongside it.

**June 2026 partial fix:** `_apply_true_damage_hierarchy` dedupes when the
trigger regex matches. Gaps that still produced double labels:

| Gap | Symptom | Example |
|-----|---------|---------|
| Intervening target phrase | Regex misses; both labels emitted | Shemira: `true damage to a single enemy equal to …` |
| Pronoun `their` | `_TRUE_DAMAGE_MAX_HP_RE` missed `their max HP` | Shemira ghost strike |
| Heal in same sentence | `_text_has_max_hp_damage` false; only True emitted | Valka slash + self-heal clause |
| Weak regression test | Test asserts True **present**, not Max HP **only** | `test_shemira_true_damage_without_atk_scalar` (fixed) |

**Audit checklist:**

1. Run true/max-HP pre-scan from `SKILL.md` (pass 1).
2. Read the **clause** that deals damage, not upgrade cap lines (`cannot exceed
   N% (ATK-based)` is a cap, not a second damage type).
3. After fix: skill should have one `damage_type: max_hp` row; skill-card tags
   should not list both `True damage` and `Max HP-based damage`.
4. Add regression test asserting `True damage` **not in** labels/types.

Resolved: Shemira Ghastly Tribute, Valka Phantom Slasher (slash clauses),
Daimon Playtime Plunder (passive Stitchy attack). Still open / different
pattern: Nara Crimson Vengeance (`damage equal to X% of max HP` without
`true damage` word), Vala Swift Shift (mixed strike types).

**Convention:** prefer **Max HP-based damage only** for max-HP-scaled true
hits (not generic True + Max HP).

### DoT false positives

Self or summon HP drain, periodic auto-attacks, on-entry bursts, channels,
and cooldown `each time` wording are not sustained enemy DoT.

- Harak Vicious Bite — healing-lock cast drain (also spurious HoT)
- Berial Shadow Reflection — Silhouette self HP cost (debatable)
- Berial Scared Swamp — channeled shadow damage every 0.25s (Magic, not DoT)
- Brutus Whirlwind Wrath — spin channel every second for 4s
- Dunlingr Bell of Order — damage each time it is summoned
- Mehira Total Devotion — voidling attacks every 1.5s
- Perseus Fertile Ground — `damage … each time it's triggered` (cooldown)
- Carolina Snowball Witchery — discrete auto-shot cooldown
- Cryonaia Frozen in Time — domain-entry burst, not sustained DoT
- Evie Intel Chase — channeled magic per second stays **Magic**, not DoT

### DoT false negatives

Sustained `every Ns` / `per second` enemy damage without `dot` label.

- Bonnie Decay's Reach — max-stack Aging `100% every 1s`
- Arden vine skills (resolved in later pass but pattern recurs)
- Daimon Guardian Howl EX+10 — max-HP shockwave ticks
- Ludovic Lifeweaver's Blooms active — HP loss over 4s
- Pippa Botanical Woe — persistent plant zone
- Satrana Ignite Passions / Talene Pyre of Renewal — ally-granted burn
- Mikola Passionate Opening — ally-adjacent damage aura
- Viperian Spiritual Viper — possessed-enemy HP drain

### HoT false positives

Healing-lock wording (`cannot be healed while…`) with `0%` self tick → not
Healing over time.

### Targeting false merges

Area/All units reach copied from a splash or summoner clause onto a different
subject in the same sentence.

- Kordan Dominance Ring — challenge Bind is **Single target**; circle damage
  and ally buffs stay **Area**
- Gwyneth Fulgur Arrow — Silence on the attack target is **Single target**;
  splash stun/damage stay **Area**
- Gwyneth Hailing Arrows — active rain Bind/damage are **Area** (2 tiles);
  charged normal-attack hit stays **Single target**
- Lamentis Malevolent Gaze — apostle Stun and Max HP debuff are **Multiple
  targets (6)**; Lamentis' own damage stays **All units**

### Buff vs debuff swaps

- Aliceth Hero Focus — focus-fire mark is **Marked target**, not ATK buff
- Berial Hero Focus — **damage dealt** debuff, not damage taken
- Laios Intimidate — ally DEF buff spurious; enemy Phys/Magic DEF debuffs
  missing
- Cyran Mystic Recollection — enemy ATK SPD debuff, not ally ATK buff
- Kafra Sylvan Banishment — **Haste debuff** on enemy; not Haste buff; not
  spurious ATK debuff from `(ATK-based) damage and reducing … haste`

### Damage dealt vs damage taken

**Direction matters.** Enemy output reduction is **Damage dealt debuff** on
`target: enemy` (`reduces the enemy's damage dealt`, Berial Hero Focus,
Temesia Iron Heel). Caster mitigation is **Damage taken reduction** buff
(`reduces damage taken`, `takes N% less damage`).

**Display pitfall (June 2026):** detection stored `Damage dealt debuff`
correctly while the site showed a buff-styled chip because
`TAG_DEFINITIONS` lacked `Damage dealt debuff` / `Damage dealt`. Fix
`site/js/app.js` and ensure `DEBUFF_TYPES` + CSV map
`Damage dealt` → `Damage dealt debuff` in `overview-to-csv.py`.

### False partner requires (synergy)

**Own-skill temporary state ≠ ally buff require:** Zandrok Legendary+ extra
max HP while **Rallying Roar** temp buffs are active is self-setup. Do not
emit `Temporary ally stat buffs` in `special_requires`; `just validate`
rejects requires without ally-source wording (`from an ally`, `from allies`).

**Self-applied debuff/DoT state ≠ debuff partner require:** Shadewing Crimson
Venom tick text (`While affected by Crimson Venom…`) is not `Debuff on target`.
Keep `Continuous damage on enemies` for Withering Curse; omit generic debuff
requires when the hero inflicts the named state. `_filter_self_satisfied_debuff_requires`
drops these after analyze when skill text applies and references the same state.

**Common buffers with empty partner list:** receivers whose only matches are
roster-wide stat buffers (Contess, Pandora, Thoran, etc.) get common-buffer
names promoted into the partner grid when display filtering would leave none.

### DEF buff phrasing gaps

Rules often match `increases … def by` but miss combined gains:

- `gains N% Phys and Magic DEF` → **DEF buff Self** (Seth Hunter Instinct)
- `increasing her Phys DEF by 50% and Magic DEF by 50%` → **DEF buff Self**,
  not Phys/Magic DEF debuff (Granny Dahnie Glimmerbloom Blessings)

Guard: `reduces … Phys DEF` must not match DEF buff rules (Seth Enhance
Force → **Phys DEF debuff** on enemy).

**Scalar bleed:** HoT or heal upgrade lines in the same skill must not bump
DEF buff `value` (Granny: DEF stays 50%, HoT tier separate).

### Impersonal self-buff upgrades

Tier-upgrade chunks that start with the verb, not the hero name:

- `Gains 25 Crit when he first triggers Bloodlust` → **Crit buff Self** (Seth)
- Default targeting may yield `ally` / Single target if only `he gains N` is
  matched, not `Gains N … when he`

Audit upgrade `text[]` lines separately when base active text has no crit/def
clause.

### True damage conversion (no hit in chunk)

`turning the charge damage into true damage` (Temesia Invincible Fury) should
emit **True damage** on the Mythic+ skill card even when the chunk does not
`deal` damage directly. `detect_damage_types` alone is insufficient —
`_chunk_deals_enemy_damage` (or similar) must admit conversion phrasing.

Do not confuse with max-HP-scaled true hits (those collapse to Max HP-based).

### Detection correct, display wrong

When JSON `skill_card_tags` already list `Haste debuff`, `Phys DEF debuff`,
or `Damage dealt debuff` but the user reports a buff chip:

1. Read `site/data/heroes.json` skillCards for the hero.
2. Grep `TAG_DEFINITIONS` in `site/js/app.js` for the full debuff label.
3. Fix chip resolution before adding new detection rules.

The usual cause is a **missing polarity**, not a missing key: renderers fall
back to `effectLabelPolarity(base) || "buff"`, and `resolveLeadingChip` strips
a trailing ` debuff` when matching stat prefixes. `effectLabelPolarity` reads
polarity off a `… buff` / `… debuff` suffix, so a label carrying the suffix
styles correctly without its own `TAG_DEFINITIONS` entry; a bare label
(`Magic DEF`) needs the caller to pass `polarity` explicitly.

### Synergy reason prefixes

Synergy reasons render through `parseSynergyReason` in `views-detail.js`. A
`<stat> via <buff>` reason drops everything before ` via ` because the stat
and the buff say the same thing. Reasons whose lead-in carries extra meaning
(`Enemy defense via Magic DEF debuff (…)`) must be listed in
`SYNERGY_KEPT_REASON_PREFIXES`, or the prefix vanishes and the reason reads as
an ally buff.

### Self-debuff false positives (always verify)

Self-targeted debuffs (`target: self`, `… debuff — Self` tags) are **extremely
rare**. Run the self-debuff pre-scan in SKILL.md; **validate every hit** — do
not batch-close as low priority.

Common pattern: text **increases** caster Phys/Magic DEF or ATK (`increasing
her Phys DEF by 50%`) stored as **Phys DEF debuff Self** → expect **DEF buff
Self** (Granny Dahnie Glimmerbloom Blessings).

Other causes: HoT upgrade scalar bleed onto DEF buff magnitude; reduction
regex matching inside an `increasing … def` clause.

When auditing pass 1, if any self-debuff remains after a detection fix pass,
re-run the pre-scan until the candidate list is empty or each row is confirmed
legitimate.

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

### Flat `+ X%` on ATK-based hits

`X% (ATK-based) + Y% damage` without explicit max-HP wording is **not**
Max HP-based damage — score as Physical/Magic only. Do not infer max-HP
scaling from the flat rider alone.

Examples: Kazim Gale Barrage, marksmen ult lines, Aliceth Radiant Rain.

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

Dodge, Crit, heals, DEF buffs, **Invincible**, **Energy recovery**, and
immunity on wrong `target`. Ally mis-tags on **damage dealers** are high
impact: they pollute `heroes_data_synergies.json` replacement `"buff"` lists
even when the label is otherwise correct.

**Self energy recovery tagged ally (June 2026):** `{name} recovers N + M
Energy` on the caster was stored as `ally` / `Single target` because (1) the
self-detection regex only matched `recovers N energy` without `+ M`, and (2)
`enemy` in the trigger clause (`whenever … enemy is controlled`) pushed
single-target enemy heuristics. Resolved: Arden Nature's Resilience → **Self**.

**Ally haste tagged Self (reverse mis-tag):** `inspiring … allies …
increasing their Haste` was stored as **Self** because possessive `their
Haste` matched before explicit ally-buff checks, and `inspiring non-summoned
allies` missed `\binspir\w+ allies\b` (words between verb and `allies`).
Resolved: Damian Inventor's Will → **Multiple targets** / `ally`.

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

### Targeting priority vs immunity (spurious Unaffected / Steadfast)

`unaffected` and `steadfast` name **CC-immune enemy types** in target-priority
lines, not buffs on the caster or allies.

| Skill | Text cue | Wrong | Correct |
|-------|----------|-------|---------|
| Cyran Cursed Grasp | `prioritizes … neither unaffected nor steadfast` | immunity rows + skill-card tags | no immunity; CC/damage only |

**Audit:** if the only `unaffected` / `steadfast` mention is who to **target**
(`who are`, `neither … nor`, `prioritizes targeting`), expect **no**
`type: immunity` effect and no Steadfast/Unaffected skill-card chips.

### Artifact silence vs Silence CC

Silencing **enemy Merlin** (artifact) at battle start is **Artifact block** on
`synergy_profile.provides`, not hero-applied **Silence** CC.

| Skill | Text cue | Wrong | Correct |
|-------|----------|-------|---------|
| Cyran Mystic Recollection (EX+10) | `Merlin is silenced … preventing Merlin from casting` | `cc-type: silence` | Artifact block only |

**Chunk-split pitfall:** upgrade text split across sentences can false-match
`after silence ends` as Silence CC even when the primary clause is artifact
block. Grep skill-card tags for `Silence` when description mentions Merlin.

### Cheat death vs self-heal only

Fatal-blow survival (`takes a fatal blow … block the fatal damage`) should
emit **Cheat death** on `synergy_profile.provides` and behavior tag
`cheat-death`, not only Direct healing on the same skill.

Resolved: Bryon Tacit Strike (EX+5).

### Haste word-order and Supreme+ upgrades

`{name}'s Haste permanently increases by N` does not match `increases …
haste` buff rules. Supreme+ / EX upgrade chunks often hold the only mention.

Resolved: Bryon Enhance Force (Supreme+) → Haste buff Self.

Watch: any `haste permanently increases` or `{possessive}'s haste` on caster.

### Scaled `N + M` stat amounts

Parser gaps recur when skill text uses `12 + 3 Energy` or similar split
values instead of a single number. Affects self-detection regexes and
magnitude merge — audit energy recovery and flat stat buffs when text uses
`+` between two numbers.

Resolved: Arden Nature's Resilience (energy recovery Self).

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
| Kazim Gale Barrage | Physical only | No Max HP chip without explicit max-HP text |
| Harak Vicious Bite | No DoT/HoT | Healing debuff from lock |
| Harak Tidal Assault | Invincible Self | Not ally buff; no replacement buff match |
| Aurora Starlit Slumber | Invincible Self; Haste on summons | Self sleep immunity ≠ ally buffer |
| Arden Nature's Resilience | Energy recovery Self | `12 + 3 Energy`; enemy in trigger ≠ ally buff |
| Damian Inventor's Will | Haste buff ally (Multiple targets) | `their Haste` in ally-inspire clause |
| Bryon Tacit Strike (EX+5) | Cheat death provide | Not heal-only |
| Bryon Enhance Force (Supreme+) | Haste buff Self | `haste permanently increases` |
| Cyran Cursed Grasp | No immunity rows | Targeting priority only |
| Cyran Mystic Recollection (EX+10) | Artifact block; no Silence CC | Merlin ≠ enemy hero Silence |
| Shemira Ghastly Tribute | Max HP-based damage only | Not True + Max HP double label |
| Seth Hunter Instinct | DEF buff Self; Crit buff Self on upgrade | Not ally Crit; not missing combined Phys+Magic DEF |
| Seth Enhance Force | Phys DEF debuff enemy | Not DEF buff from reduction text |
| Granny Dahnie Glimmerbloom Blessings | DEF buff Self | Not self DEF debuff; DEF % not from HoT scalar |
| Kafra Sylvan Banishment | Haste debuff | Not Haste buff; not ATK debuff |
| Temesia Iron Heel | Damage dealt debuff | Debuff chip on site; not Damage taken buff |
| Temesia Invincible Fury | True damage + Unaffected Self | Conversion line on Mythic+ card |
| Valka Phantom Slasher | Max HP-based damage on slashes | Heal in same clause must not block dedup |
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
- **Shemira Ghastly Tribute** — context-dependent true/max-HP cap on ghost
  strikes (resolved: label is Max HP-only; magnitude cap is pass 2)
- **Nara Crimson Vengeance** — shockwave `damage equal to X% of max HP` without
  `true damage` word: may legitimately differ from true-scaled hits

## Regression tests after fixes

Prior passes added tests in:

- `scripts/test_skill_descriptions.py` — sidecar-backed effect regressions
- `scripts/test_hero_schema.py` — skill-card chip keys (debuff distinct from
  buff stat, e.g. `damage dealt debuff` vs `damage taken reduction`)
- `scripts/test_detailed_validation.py`

Add a **minimal** case per new pattern; run `just validate` before closing
the task. When post-process rules change, bump
`scripts/roster_analysis.py` `CACHE_VERSION` before `just analyze` or
`just views` (stale disk cache otherwise reuses pre-fix targeting).
