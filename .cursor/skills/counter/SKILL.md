---
name: counter
description: >-
  Writes or refreshes PVP counter overviews in data/hero_counter_overviews.json
  for one hero, a named subset, or the full roster. Use when a new hero is added,
  when counter text needs updating, or when following docs/ai-generated-data.md
  section 5. Maintains the Explicit counters list in this skill.
---

# Counter proposal

Author short PVP counter advice per hero for the site viewer **Counter proposal**
section (after Play overview). Output: `data/hero_counter_overviews.json`.

**Scope:** one hero, a named subset, heroes missing an entry, or a full roster
refresh. For new heroes, run after play overview in [add-hero](../add-hero/SKILL.md)
Phase C.

## Source files (read in this order)

1. `docs/ai-generated-data.md` section 5 — authoring rules
2. This skill — **Validation gates** and **Explicit counters** below
3. `data/hero_counter_overviews.json` — current entries
4. `data/hero_play_overviews.json` — how the hero plays (threat context)
5. `data/hero_behavior_tags.json` — pick counter units by combat role
6. `data/heroes_data_processed.json` + `data/heroes_data_skill_summary.json`
7. `data/heroes_data.json` — `prydwen_tiers.pvp` + `damage_type` for assassin pick
8. `data/character_stat_ranks.json` — Phys DEF / Magic DEF ranks (`low` /
   `average` / `high`) for Gate 2 damage-type bias
9. `afkj-data/docs` (faq-pvp, combat-*-pvp) — private grounding only; never copy
   implementation jargon into public counter text

## Workflow

```
Task progress:
- [ ] 1. Scope — which heroes (single / subset / missing / all)
- [ ] 2. Read play overview, skills, tags, PVP tiers, DEF ranks for each hero
- [ ] 3. Run validation gates 1–6
- [ ] 4. Apply Explicit counters + high-PVP naming for [[pills]]
- [ ] 5. Write 3–5 sentences with [[Display Name]] markers
- [ ] 6. Update hero_counter_overviews.json
- [ ] 7. Extend Explicit counters if a reusable named combo was confirmed
- [ ] 8. Run just render-site; spot-check character pills on site
```

### 1. Scope

| Request | Action |
| --- | --- |
| Single hero | One key in `hero_counter_overviews.json` |
| Named subset | Only listed display names |
| New hero (add-hero) | One entry for the new hero |
| Missing | All roster heroes without a counter entry |
| Full refresh | Every hero (confirm with user if large) |

Keys use display names from `heroes-overview.md` (e.g. Twins, Lily May).

### 2. Content shape

Per hero, **3–5 sentences**, under ~900 characters:

1. PVP threat — what to watch for (PVP / Arena OK)
2. Fight flow — how the matchup tends to play out
3. Counter hints — short comp directions with `[[Hero]]` pills

Use **bold** sparingly for key threats and levers. Every `[[Name]]` must match
a roster display name exactly.

### 3. Validation gates (required every run)

Run these **before** inventing counter hints. Failures here caused past bad
advice (Contess, Cryonaia, Dunlingr, Alna, Tasi).

#### Gate 1 — Phase / hittability

Never suggest damage or targeting during windows where the unit is **hidden**,
**untargetable**, **invincible**, or otherwise unhittable. Counter the
**actionable** phase: emerge, rule trigger, exposed ally, or post-window.

Example: Contess — cannot burst while hidden; punish on emerge (see Gate 4b for
mid-fight damage curve, not opener dump).

Example: Zorya — invincible while dormant; late delete after awake + stone fade
(Gate 4b).
Example: Tasi — invincible in butterfly form; delete between forms, not during.
Example: Solise — unaffected while casting her ultimate; do not bank on a mid-channel interrupt.
Example: Cyran — unaffected through his battle-start Enlightening window; delete after it ends (Gate 4b).
Example: Harak — unaffected during Vicious Bite and the feast-end devour; do not interrupt those casts.
Example: Scarlita — invincible while airborne; punish on descend (Gate 4b), not during hover.
Example: Bonnie — invincible in mist form; lasting coverage, not mist-dump burst (Gate 5).
Example: Baelran / Pang — Unaffected during key channels/forms; do not bank on CC or interrupts there.
Example: Galahad — early delete before the energy circle matures (Gate 4b early).

**Channel / chant maintenance (control CC)** — separate from Gate 4a ultimate
**Interrupt** ([[Lily May]] on discrete ult wind-ups). When a kit’s payoff
depends on **finishing or maintaining** a chant/channel, control CC that
**breaks the cast** is a primary counter — unless the threatening cast is
immune.

Read skill text for the **threatening cast** in this order:

1. **Unaffected** / **immune to control** while casting or channeling? → do
   **not** suggest control CC interrupt (examples above).
2. Effect **cannot be maintained** under control, or **recreate cooldown**
   after interrupt? → **S1** — name control CC ([[Lily May]] sleep,
   stun/sleep packages).
3. **Chanting** passive (all or key skills require chant) and the threatening
   cast has **no** immunity clause? → **S2** — control CC during chant.
4. Ongoing **`while channeling`** effect with **no** immunity on that cast? →
   infer breakable — same control CC lever.
5. Else → do not suggest generic control CC interrupt ([[Lily May]] may still
   apply via Gate 4a / Explicit for a discrete ultimate wind-up only).

Example: [[Smokey & Meerky]] (S1) — aroma drops under Control Effects with a
4s recreate lockout; break the channel with [[Lily May]] or stun/sleep CC (Gate
6b displacement is complementary, not a substitute).

Example: [[Marcille]] (S2) — every skill requires chanting and she is not
unaffected mid-channel; CC during chant before companions or revive land.

#### Gate 2 — Role match for “kill / burst”

If the advice is to **delete** a unit, pick from `backline-assassin` then
`assassin` (prefer faster damage). Do **not** invent “burst” from high Prydwen
PVP tier alone — S-tier AoE, CC, or shield heroes are not delete tools unless
they also fit the kill tags.

Then apply **kit-fit** (Naming rules §4) — name **1–2** best-fit units, never the
stock [[Athalia]] / [[Evie]] / [[Nerion]] trio as a default list.

**DEF skew + true damage (variance):** after the role pool is set, read the
target’s Phys DEF and Magic DEF ranks in `data/character_stat_ranks.json`. Any
asymmetry biases `damage_type` among tagged assassins:

- Phys DEF **lower** than Magic DEF → prefer **Physical** assassins
- Magic DEF **lower** than Phys DEF → prefer **Magic** assassins
- Equal ranks → no DEF bias; keep timing / kit-fit only

**Damage immunities override** DEF bias (e.g. Hodgkin ethereal / phys immune →
Magic pressure, not Physical dump into intangibility).

When **both** Phys DEF and Magic DEF are **high**, and/or the kit leans on
**heavy shields**, prefer assassins whose skill text includes **true damage**
first (rotate among fits such as [[Himmel]], [[Nara]], [[Vala]], [[Pippa]],
[[Athalia]] — do **not** re-center every high-DEF delete on Athalia). Allow
non-assassin true-damage pressure only when Gate 5 / timing already selected
that class (e.g. lasting [[Frieren]] / [[Sylphira]] coverage).

Goal: meaningful variance in delete pills — DEF and true damage break the
repeated stock trio, not replace it with a new single default.

Example: Cryonaia wind-up (**early** delete) — [[Athalia]] or [[Ravion]], not
slow investigators like Evie, and not generic S-tier names like Mehira/Saida.

**Exception:** Gate 5 overrides this when the delete target is a high-mobility /
late-ult leaper — do not default to assassins there.

#### Gate 3 — Protected / exempt allies

When a kit singles out an ally as **exempt** from a team-wide restriction (or
similarly protected), that **exempt/protected carry is the priority delete** —
usually with non-ult-capable `backline-assassin` pressure — not “whoever isn’t
protected.”

Example: Dunlingr — send [[Athalia]] or [[Gwyneth]] / [[Ravion]] at the
**exempt carry** he shields from the order; prefer non-ult kits while the ban
lasts (Athalia is Celestial — always pair with a non-C/H path).

#### Gate 4 — Timing (threat window + delete window)

Timing has **two directions**. Check both before naming pills.

##### 4a — Threat window (is my counter ready when *they* fire?)

For “before X” / opener / pull / interrupt advice, match the counter’s cast
timing to the threat’s window using `behavior.skill_overview` speeds
(`first_cast_speed`, `speed`), behavior tags (`battle-start-ult`,
`battle-start-burst`), and skill text (“when a battle starts”). A slow mid-fight
setup does **not** answer a battle-start opener.

Example: Alna frost — [[Eironn]] battle-start pull or [[Mehira]] fast pull; not
[[Cyran]]’s slow setup grouping.

Example: Eironn battle-start pull — [[Lily May]] on the opening beat; not
[[Pandora]]’s delay (too slow for the same window).

Do not describe `enemy-grouping` heroes as clustering **allies** — units like
[[Eironn]], [[Cyran]], or [[Mehira]] pull or displace **enemies**, not your
formation.

**Steadfast** and **Unaffected** counter enemy-grouping / displacement (pulls,
throws, knocks). Prefer them over “spread formation” when the pull is **global**
or otherwise ignores spacing (e.g. Cyran’s black hole pulls the whole field —
spread does nothing). Named steadfast tools: [[Gunnar]] Doomfield (self + the
ally parked on it stay Steadfast), self-Steadfast [[Igor]] (and awake [[Zorya]]).
Unaffected windows (self or granted) block the same displace class. Cyran’s
throw also **skips** unaffected/steadfast targets when choosing whom to hurl.

##### 4b — Delete window (does my damage peak when *they* are killable?)

Find when the unit is actually soft (Gate 1’s actionable phase), then match the
counter’s **damage curve** to that window — not merely “wait, then dump an
opener assassin.”

| Window type | Examples | Prefer | Avoid |
| --- | --- | --- | --- |
| **Early** | Frieren pre-amp, Cryonaia wind-up, Solise pre-bloom | Fast assassins / openers | Slow mid-fight setup that arrives after the window |
| **Late / delayed** | Zorya awake + fading stone skin, Contess emerge, post-invuln soft phases | Sustained / long ultimates / mid-fight peak ([[Shemira]], [[Gwyneth]], amp’d [[Frieren]]) | Battle-start burst that spends itself before the window |

Example: Zorya — [[Gwyneth]] / [[Shemira]] after stone skin fades; not opener
assassins into full 70% DR.

Example: Contess — mid-fight pressure on emerge ([[Gwyneth]], [[Shemira]],
[[Bonnie]]); not opener burst that fires while she is still hidden, and not a
stacked Hypogean pair for the same lever.

Example: Frieren — early [[Athalia]] / [[Himmel]] before amplify (Gate 2 + 4b
early); not Evie intel delay.

#### Gate 5 — High mobility vs pin-delete

If the threat **leaps, flies, teleports, or otherwise relocates often**
(`self-repositioner`, skill text like “flies to the farthest”, shadow hops,
dives), especially with a **late / slow-to-online ultimate**, do **not** answer
with single-target `backline-assassin` pin-deletes. Assassins miss or waste
burst as the target leaves their tile.

Prefer **long-lasting ultimates with wide or retargeting coverage** that keep
hitting wherever the unit moves:

- Strong fits: [[Shemira]] (multi-second random bombardment), [[Frieren]]
  (multi-second wide rectangle channel)
- Conditional: lasting **localized domains** (e.g. [[Sylphira]]’s Harmonic
  Domain on the densest clump) help only if the mover stays in that zone —
  leap-to-farthest kits like [[Tasi]] often leave densest clumps, so treat
  Sylphira as secondary at best, not a primary pin

Peeling a diver’s **victim** (Athalia’s carry target) or deleting a
**stationary partner** (Alna’s Winter Warrior, Aliceth’s bonded carry) is still
Gate 2 — Gate 5 applies to pinning the **mobile unit itself**.

Example: Tasi — [[Shemira]] / [[Frieren]] lasting coverage + [[Lily May]] for
sleep; not a backline-assassin pin.

#### Gate 6 — Mid-fight position dependence

Use displacement when a kit needs an ally to **stay** somewhere **during** the
fight — not merely at battle start.

**Out of scope:** battle-start-only placement / bonding / linking (e.g. Twins
Stellar Bond line, Thador / Thoran prep placement). Those are not Gate 6.

##### 6a — `static-tile-buffer`

If the subject is tagged `static-tile-buffer` (today [[Hugin]], [[Gunnar]]),
counter by **displacing the buffed ally off the tile** so the mid-fight buff
drops. Lead with [[Lumont]] or [[Eironn]]; rotate other mid-fight displacers
([[Mehira]], [[Reinier]], [[Pippa]]) — still name at most two, with C/H
same-clause rules. **Not** [[Temesia]] — she charges enemies and knockdowns;
she does not shove allies off tiles or out of auras.

If the parked ally is **Steadfast** or **Unaffected**, displacement does not
move them — fall back to **delete / inhibit** that ally instead (see Explicit
counters [[Gunnar]] Doomfield).

##### 6b — Moving / provider-attached aura

If skill text or play overview shows a buff zone that **follows the caster**
(proximity aura / circle around the provider — e.g. [[Perseus]], [[Shakir]]
Lupine Aura), prefer **shoving receivers out of the aura** first with
**targeted foe displacement** — [[Lumont]], [[Pippa]], [[Reinier]], [[Mehira]]
(rotate 1–2).

**Not** enemy-grouping pulls ([[Cyran]] black hole, [[Eironn]] battle-start
pull): those are displacement, but they **group/pull enemies** — they do **not**
evict enemy **allies** packed in the provider’s aura. Clustering on [[Shakir]]
is the problem, not the fix.

**Peel the provider** away from his carries only when the provider is **not**
**Steadfast** or **Unaffected** on that cast (e.g. [[Shakir]] is **Unaffected
in Wolf Form** — peeling him fails; shove receivers instead).

Do **not** treat global / non-positional team buffs as Gate 6b.

### 4. Naming rules for [[pills]]

- Prefer Prydwen PVP **S+** then **S**, then **A+** for example and counter units
- **A** tier OK for matchup-specific picks (see Explicit counters)
- Avoid **B/C** unless listed in Explicit counters or the user requests them
- Single-ally buffers: assume a hypercarry partner (often high-ult damage).
  Alna: typical partners [[Sylphira]], [[Frieren]]
- Prefer high Prydwen PVP among tagged candidates; Explicit counters override
  the B/C ban when listed for that role
- **Kit-fit over stock trio:** never paste [[Athalia]] / [[Evie]] / [[Nerion]]
  as a default “backline assassins like X, Y, or Z” list. Name **at most two**
  delete/inhibit tools, chosen for how their kit meets *this* threat (timing,
  damage type, inhibit vs burst, non-ult, etc.). Rotate A+/S alternatives
  ([[Himmel]], [[Ravion]], [[Bonnie]]) when fit is equal so the roster file
  does not repeat the same pair on every entry.
- **DEF / true-damage bias (Gate 2):** use Phys DEF vs Magic DEF ranks and
  true-damage kit text to diversify delete picks — prefer the matching
  `damage_type`, then true-damage assassins when both DEFs are high or shields
  are thick. Immunities override. Still rotate among fit names; do not collapse
  every Physical-skew or high-DEF case onto [[Athalia]] alone.
- **Celestial / Hypogean alternatives:** if any suggested **counter** unit is
  Celestial or Hypogean, always also name a **non-Celestial, non-Hypogean**
  alternative for that same lever in the **same clause** (e.g. `[[Athalia]] or
  [[Ravion]]`). Prefer **leading with the non-C/H** name when both fit. Do **not**
  stack two C/H units for one lever (`[[Mehira]], [[Cryonaia]]`) even if other
  sentences have non-C/H elsewhere. Enemy lineup examples (e.g. Alna’s Winter
  Warrior) are not counters. Dimensional / Wilder / Lightbearer / Graveborn /
  Mauler all count as non-C/H.
- **Enemy-side buff/debuff amplification:** if a (de)buff grows from **enemy**
  allies’ actions (e.g. Bonnie Aging stacks when *her* magic allies hit the
  Aged target), do **not** tell the reader to “not feed” it or to bring
  “non-magic lines” on *their* team — those levers are not available. Counter
  by pressuring the **providers** (the debuff/buff source and the enemy units
  that amplify it), cleansing/dispelling when possible, or winning before max
  stacks. Only advise “don’t feed X” when *your* units’ actions actually
  power the enemy effect (e.g. overhealing into Galahad’s bind HP-loss, or
  standing healers in Faramor’s anti-heal circle).

#### Kit-fit cheat sheet (among tagged delete/inhibit pool)

| Threat need | Prefer | Usually avoid |
| --- | --- | --- |
| **Early** hard delete (pre-amp, wind-up, pre-bloom) | [[Athalia]] (C — pair with non-C/H) + [[Ravion]] / [[Himmel]]; or non-C/H alone | [[Evie]] (intel delay), slow DoT ramps |
| **Mid / late** continuous pressure | [[Nerion]], [[Evie]], [[Bonnie]] (all non-C/H) | Opener-only Athalia dump |
| Inhibit / delay a hypercarry | [[Evie]], [[Himmel]], [[Nerion]], [[Bonnie]] | Burst-only names with no stall |
| Non-ult damage (e.g. Dunlingr ban) | [[Athalia]] (C — pair with [[Gwyneth]] / [[Ravion]]) | Ult-dependent carries; Aliceth-only (also C) |
| Peel a diver / mark partner | Match the *victim* slot: inhibit ([[Bonnie]], [[Evie]]) or race buffers | Listing three assassins |
| Steadfast vs pulls | [[Gunnar]] (H — pair with [[Igor]]) | Spread vs global pulls |
| Heal denial | [[Dunlingr]] (C — pair with a non-C/H early-delete path) | Heal denial with no non-C/H fallback |
| Low Phys DEF / higher Magic DEF | Physical assassins ([[Ravion]], [[Himmel]], [[Vala]], …) | Magic dump into the strong DEF |
| Low Magic DEF / higher Phys DEF | Magic assassins ([[Evie]], [[Nerion]], [[Pippa]], …) | Physical dump into the strong DEF |
| Both DEF high and/or heavy shields | True-damage assassins ([[Himmel]], [[Nara]], [[Vala]], [[Pippa]], [[Athalia]]) — rotate | Ignoring DEF and defaulting stock trio |
| Damage immunity (e.g. phys ethereal) | Opposite damage type / lasting Magic coverage | Matching the immune type |
| Channel / chant maintenance (no cast immunity) | Control CC ([[Lily May]], stun/sleep packages) | Control CC vs unaffected casts; Lily May ult-Interrupt only (Gate 4a) |
| Mid-fight tile buff (`static-tile-buffer`) | Displace **buffed ally** ([[Lumont]], [[Eironn]], [[Pippa]], …) | Battle-start-only placement advice; shove Steadfast allies; [[Temesia]] |
| Moving proximity aura | Shove **receivers** ([[Lumont]], [[Pippa]], [[Reinier]], [[Mehira]]); peel provider only if not Steadfast/Unaffected | [[Cyran]] / [[Eironn]] enemy pulls; global buffs as positional |

Do not put tag names (`backline-assassin`, etc.) in public counter prose —
use them only to select which heroes to name as `[[pills]]`.

### 5. Tag heuristics (quick reference)

| Threat | Prefer counters tagged… | Gate |
| --- | --- | --- |
| Ranged / far hypercarry | `backline-assassin`, then `backline-inhibit` | 2 |
| Kill before wind-up / domain / invuln (**early** delete window) | `backline-assassin`, then `assassin` | 2 + 4b |
| Delayed vulnerability (**late** delete window) | Sustained / long ultimates ([[Shemira]], [[Gwyneth]], amp’d [[Frieren]]) | 4b |
| Any-row priority kill | `assassin` | 2 |
| High-mobility / leap / teleport (esp. late ult) | Long lasting wide/retargeting ultimates ([[Shemira]], [[Frieren]]); not assassin pin | 5 |
| Enemy-grouping / displacement (pull, throw, knock) | **Steadfast** / **Unaffected** — not spread vs global pulls | 4a note |
| Channel / chant breaks under control | Control CC during chant/channel ([[Lily May]], stun/sleep) | Control CC vs immune/unaffected casts (Gate 1) |
| Mid-fight tile buff (`static-tile-buffer`) | Displace buffed ally ([[Lumont]], [[Eironn]], [[Pippa]], …); Steadfast → delete/inhibit | 6a |
| Moving / provider-attached aura | Shove receivers ([[Lumont]], [[Pippa]], …); peel provider if not Steadfast/Unaffected | Enemy-grouping pulls ([[Cyran]], [[Eironn]]) for aura break | 6b |
| DEF skew / high both DEF + shields | Match assassin `damage_type`; true damage when both high | 2 |
| Early / high-damage ultimate | See Explicit counters | 4a |

### 6. Explicit counters

Consult this table **after** gates 1–6. Keep **named combos** here. When a run
confirms a new reusable **named** combo (not already covered by a gate),
**append a row in the same change set**.

| Pattern | Preferred counter / combo |
| --- | --- |
| Early-battle / battle-start ultimate (e.g. Eironn) | [[Lily May]] on the opening beat — **not** [[Pandora]] (Gate 4a) |
| High-damage ultimate (wind-up / mid-fight) | [[Lily May]]; if they run a Lily May catcher, pair [[Pandora]] with [[Lily May]] |
| Race another hypercarry | Speed your carry with [[Thador]], [[Hugin]], or [[Rowan]] |
| Enemy Lily May canceling your early ult | Frontline [[Niru]] or [[Bryon]] (battle-start ult) as “Lily May catcher” so her cancel hits them instead |
| Enemy Niru/Bryon catching your Lily May (slow ult only) | [[Pandora]] with [[Lily May]] — not vs battle-start openers (Gate 4a) |
| [[Dunlingr]] (ult/heal denial) | Non-ult kits on the **exempt carry** — [[Athalia]] (C) **or** [[Gwyneth]] / [[Ravion]] (non-C/H); see Gate 3 |
| [[Frieren]] (pre-amp / **early** delete window) | [[Athalia]] or [[Himmel]] / [[Ravion]] before ~15s amplify; if [[Himmel]] is *their* adjacent partner, amp skips the wait — shorter window. Not Evie intel delay (Gate 4b) |
| Delayed vulnerability (**late** delete window) | Sustained / long ultimates ([[Shemira]], [[Gwyneth]], amp’d [[Frieren]]); not opener assassins (Gate 4b) — e.g. [[Zorya]] awake+stone fade, [[Contess]] emerge, [[Cyran]] post-unaffected opener |
| [[Solise]] (heal snowball) | [[Dunlingr]] no-heal (C — also give non-C/H early delete [[Ravion]] / [[Himmel]]); she is unaffected mid-ult (Gate 1) |
| High-mobility / late-ult leaper (e.g. [[Tasi]]) | [[Shemira]] / [[Frieren]] lasting coverage; [[Lily May]] for sleep — not assassin pin (Gate 5). [[Sylphira]] domain only if mover stays in densest clump |
| [[Berial]] / [[Lily May]] / [[Harak]] (mobile finish) | Lasting coverage ([[Shemira]], [[Frieren]]) or area packages; do not chase shadow hops / relocates / dashes with assassin pin |
| [[Harak]] (feast / devour) | Deny assists that extend feast; keep weakest above devour HP threshold; Gate 5 lasting coverage |
| Enemy-grouping / displacement (pull, throw, knock) | **Steadfast** / **Unaffected** — [[Gunnar]] Doomfield (self+ally), self-Steadfast [[Igor]]; spread does **not** beat global pulls ([[Cyran]] black hole) |
| `static-tile-buffer` (mid-fight tile buff) | Displace the **buffed ally** off the tile — [[Lumont]] / [[Eironn]] / [[Pippa]] (rotate [[Mehira]], [[Reinier]]); not [[Temesia]]; Steadfast/Unaffected parked → delete/inhibit (Gate 6a) |
| Moving proximity aura (e.g. [[Perseus]], [[Shakir]]) | Shove **receivers** with [[Lumont]] / [[Pippa]] / [[Reinier]] — **not** [[Cyran]] / [[Eironn]] enemy pulls; peel provider only if not Steadfast/Unaffected (Gate 6b) |
| [[Shakir]] (Lupine Aura, wolf Unaffected) | [[Lumont]] / [[Pippa]] to shove receivers out — not [[Cyran]] / [[Eironn]] pulls; **Unaffected in Wolf Form** — cannot peel him off the pack |
| [[Smokey & Meerky]] (channeling aroma) | Break channel with control CC ([[Lily May]], stun/sleep) — aroma drops under Control Effects; 4s recreate lockout; also Gate 6b shove + early delete |
| [[Marcille]] (chanting kit) | Control CC during chant before companions/revive; [[Lily May]] on ultimate wind-up only (Gate 4a) — not unaffected mid-channel |
| [[Bonnie]] (Aging cleanse) | Ally cleanse: [[Hewynn]] (C OK here); soft team shorten: [[Evie]] full-intel. Self-only cleanses ([[Lucca]], [[Sylphira]]) only help if *they* are the Aged rearmost |
| [[Damian]] (off-field / unhittable) | Collapse chariot/toys with area packages ([[Shemira]], [[Frieren]], [[Pandora]]); never pin Damian |
| [[Evie]] (conceal invincible intel) | No opener dump into concealment; punish after reveal with lasting [[Shemira]] / [[Frieren]] or mid-fight [[Gwyneth]] |
| [[Dionel]] (untargetable soar + relocating late ult) | Lasting [[Shemira]] / [[Frieren]] + [[Lily May]] on soar; pressure buffer partners — not assassin pin mid-air |
| [[Gunnar]] Doomfield | Priority-delete the **parked rear ally** ([[Ravion]] / [[Evie]]); not Gunnar through shields first — Steadfast parked ally means displace fails (Gate 6a) |
| [[Hodgkin]] ethereal (phys immune) | **Magic** lasting coverage ([[Shemira]] / [[Frieren]]); no physical dump into intangibility — immunity overrides DEF skew (Gate 2) |
| [[Phraesto]] (Illusion) | Prefer deleting **Phraesto** over the Illusion — Illusion-first triggers his stun punish |
| [[Pandora]] (boxed ally) | Pressure the **boxed partner** (acts through her global CC); early delete before Corruption + [[Lily May]] on the freeze |
| [[Saida]] (seed/revive + teleports) | Lasting [[Shemira]] / [[Frieren]]; inhibit before seeds multiply — not assassin pin (Gate 5) |
| [[Satrana]] (invuln ult + Sparks) | No burst into Fiery Dance (Gate 1); pressure **Satrana + Sparks partners** |
| [[Kulu]] (teleport invuln + Unaffected ult) | Lasting [[Shemira]] / [[Frieren]]; [[Lily May]] for ult — not assassin pin (Gate 5) |
| [[Valka]] ult-parry (Soulshock Riposte) | Don’t ult into her range; [[Lily May]] + early [[Ravion]] / [[Himmel]]; lasting coverage from outside range |
| [[Aurora]] (battle-start invincible sleep) | Lasting [[Shemira]] / [[Gwyneth]] on Sonny & summon providers; never sleep-dump (Gate 1) |
| Enemy Rend / poison / burn DoT providers | Ally cleanse: [[Hewynn]] (C OK); pressure the provider — early [[Ravion]] / [[Himmel]] |

Gate-covered examples (Contess hittability + late emerge, Cryonaia early
hunters, Alna/Eironn threat timing, Zorya late delete) live in **Validation
gates** above; do not duplicate them here unless a new **named** unit combo is
confirmed.

### 7. Write and render

Edit `data/hero_counter_overviews.json`. Pipeline injects `#### Counter proposal`
after Play overview via `format_behavior_section()` in `rewrite-summaries.py`.

```bash
just render-site
```

Display: `[[Hero]]` → character pills in `site/js/src/chips.js` `renderInline()`.

### 8. Verify

- Entry length 80–1000 chars; 3–6 sentences
- All `[[markers]]` resolve to roster names (`just validate` counter overview)
- Pilot / partial roster: missing keys are OK (warning only)
- Site: `#hero/<slug>` — Counter proposal under Play overview; pills link correctly
- Spot-check: gates 1–6 applied (no unhittable burst, no tier-only “burst”,
  exempt carry if relevant, channel/chant maintenance — control CC only when
  S1/S2/inferred channeling and cast is not immune; Lily May ult-Interrupt stays
  Gate 4a, 4a threat timing + 4b delete-window curve, no assassin pin on
  high-movers, Gate 6 positional displace vs Steadfast fallback, DEF skew /
  true-damage variance on delete picks, immunity overrides DEF, no stock
  Athalia/Evie/Nerion trio — kit-fit 1–2, every Celestial/Hypogean counter has
  a non-C/H alternative)

## Related skills

- [add-hero](../add-hero/SKILL.md) — run counter overview after C4 play overview
- [behavior-tags](../behavior-tags/SKILL.md) — tag definitions for counter picks
- [web-ui](../web-ui/SKILL.md) — character pill display issues only
