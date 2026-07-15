---
name: update-behavior-tags
description: >-
  Audits and updates curated combat-role tags in data/hero_behavior_tags.json
  against hero skill data. Use when asked to update, refresh, audit, review, or
  fix behavior tags, hero_behavior_tags.json, similar-skills tags, or when
  following docs/ai-generated-data.md section 2.
---

# Update behavior tags

Curate `data/hero_behavior_tags.json` so each hero has a small set of tags
that describe how they are played in combat. Tags drive **Similar Skills**
replacement scoring (Jaccard overlap in `scripts/generate-heroes-overview.py`).

## Source files (read in this order)

1. `.cursor/AGENTS.md` — **Behavior tags** section (definitions + 3–5 tag rule)
2. `data/schema/tags.schema.json` — allowed tag enum (do not invent tags)
3. `data/hero_behavior_tags.json` — current assignments
4. `data/heroes_data.json` — `description`, `description_lite`, skill text
5. `data/heroes_data_skill_summary.json` — mechanic summaries per skill slot
6. `data/hero_play_overviews.json` — curated playstyle blurbs (good first pass
   for identity; cross-check against skill text before changing tags)

Optional context: `docs/ai-generated-data.md` section 2, `docs/replacement-algorithm.md`.

## Audit prompt

Compare `data/hero_behavior_tags.json` against skill descriptions in
`data/heroes_data.json`, using `heroes_data_skill_summary.json` and
`hero_play_overviews.json` to spot identity mismatches quickly.
Are there any characters where the tags do not describe the character's skills
sufficiently?
Look for misleading tags, missing tags or tags that are wrongly attributed.
When creating new tags, try to build groups of tags over single-use tags.

**Schema constraint:** only use tags from `tags.schema.json`. If no existing
tag fits, note the gap; do not add enum values unless the user requests a
schema change.

## Workflow

```
Task progress:
- [ ] 1. Load definitions, schema enum, current tags, hero list
- [ ] 2. Flag coverage gaps (missing heroes, name aliases)
- [ ] 3. Review heroes (all, or user-named subset)
- [ ] 4. Apply fixes to hero_behavior_tags.json
- [ ] 5. Validate JSON against schema enum
- [ ] 6. Summarize findings and edits
```

### 1. Load and inventory

- Hero count in `heroes_data.json` must match tag keys (alias: **Twins** in
  tags = **Elijah & Lailah** in `heroes_data.json`; pipeline uses `Twins`).
- Note heroes with fewer than 2 or more than 6 tags after edits.
- Prefer **3–5 tags** per hero; only exceed for genuinely multi-role kits.

### 2. Per-hero review

For each hero, read play overview + summaries + `description_lite` and ask:

1. **Missing** — defining mechanic with no matching tag?
2. **Misleading** — tag present but mechanic is minor, wrong target, or wrong
   type?
3. **Wrong attribution** — tag describes a one-off skill, not how the hero is
   played?

Assign tags that describe **playstyle identity**, not every skill effect.

When a hero has **ally** tags, still scan enemy-facing skills for
`enemy-debuffer`, `mass-cc`, `execute`, etc. Support kits often debuff
enemies through punishments, rule violations, or stat penalties — not only
direct casts. Check `heroes_data_skill_summary.json` and the processed
`debuffs` line in skill overview; do not skip debuff identity because the
hero also heals or shields allies.

**`high-initial-energy` (≥ 500 effective IE):** read Ultimate `Initial Energy`
from skill `meta`, then add the largest ascension bonus matching
`Gains extra N initial Energy` / `extra N initial Energy` in upgrade text.
Re-audit when new heroes or ascension tiers change IE values:

```bash
python3 - <<'PY'
import json, re
from pathlib import Path

EXTRA = re.compile(r"(?:Gains extra|extra)\s+(\d+)\s+initial\s+Energy", re.I)
THRESH = 500

def parse_num(s):
    if s is None: return 0
    try: return int(float(str(s).strip().replace(",", "")))
    except: return 0

for h in json.loads(Path("data/heroes_data.json").read_text())["heroes"]:
    ult = extra = 0
    for sk in h.get("skills", []):
        if sk.get("section") == "Ultimate":
            ult = parse_num((sk.get("meta") or {}).get("Initial Energy"))
        desc = sk.get("description") or {}
        parts = [desc.get("raw", "")]
        for u in desc.get("upgrades") or []:
            parts.extend(u.get("text") or [])
        for p in parts:
            m = EXTRA.search(p)
            if m:
                extra = max(extra, int(m.group(1)))
    eff = ult + extra
    if eff >= THRESH:
        print(f"{h['name']}: {eff} ({ult}+{extra})")
PY
```

### 3. Apply edits

- Edit only `data/hero_behavior_tags.json`.
- Keep tag arrays **sorted alphabetically**, **unique**, non-empty.
- Minimize diff: fix clear issues; do not retag the whole roster without cause.
- When adding tags, prefer **reusable group tags** already in the enum over
  hero-specific nuance.

### 4. Validate

After editing, verify programmatically:

- Every tag is in `tags.schema.json` `behaviorTag` enum
- No duplicate tags per hero
- Every hero in `heroes_data.json` has an entry (via `Twins` alias)

```bash
python3 - <<'PY'
import json
from pathlib import Path

root = Path("data")
tags = json.loads((root / "hero_behavior_tags.json").read_text())
heroes = json.loads((root / "heroes_data.json").read_text())
allowed = set(json.loads((root / "schema/tags.schema.json").read_text())
              ["$defs"]["behaviorTag"]["enum"])

names = {h["name"] for h in heroes["heroes"]} - {"Elijah & Lailah"} | {"Twins"}
assert names == set(tags), (names - set(tags), set(tags) - names)
for hero, tlist in tags.items():
    assert tlist, hero
    assert len(tlist) == len(set(tlist)), hero
    bad = set(tlist) - allowed
    assert not bad, (hero, bad)
print("OK:", len(tags), "heroes")
PY
```

## Definition guardrails

Apply `.cursor/AGENTS.md` definitions strictly. Common mistakes:

| Tag | Requires | Reject when |
|-----|----------|-------------|
| `mass-cc` | Reliable CC on **multiple** enemies or wide areas | Single-target stun/bind/knock |
| `ally-buffer` / `ally-healer` / `ally-shielder` | Meaningful effect on **allies** | Self-only, or buffs/shields on summons/turrets |
| `energy-provider` | Grants Energy to **allies** or accelerates ally ulimates | Self energy recovery only |
| `enemy-debuffer` | Meaningful **enemy** stat or combat debuffs as a core pattern | Self debuffs; ally-only kits with no enemy penalties; one minor stat shave |
| `battlefield-modification` | Physical obstacles or map layout changes | Buff/debuff/terrain **zones** alone |
| `summoner` | **Battlefield summons** — independently acting combat units placed on or remaining on the battlefield beyond the cast animation (registry in `hero_summon_profiles.json`) | Transient attacks/effects (Sky Fish, magic leaves, Smashy strike); passive objects (Pandora's box); **spell-form** damage (Mehira voidlings, Shemira ghosts) |
| `dot-specialist` | Recurring tick damage as a **primary** pattern | Stat debuffs without DoT; bind damage alone |
| `life-drain` | HP sustain tied to **dealing damage** | Stat steal, shield regen, heal-on-shield |
| `revive` | Brings **defeated allies** back | Self-survival (`cheat-death` instead) |
| `cheat-death` | Self-survival at fatal blow or **critical HP threshold** via recovery/form | Ally revive (`revive` instead); form swap alone without a survival trigger |
| `aoe-damage` | Substantial multi-target damage **regularly** | Occasional summon detonation |
| `aoe-healing` | Heals **wide ally groups** | Single-target or post-channel one-off heal |
| `assassin` | Picks isolated/backline with burst | General focus-fire marksmen |
| `self-repositioner` | **Regularly** jumps/dashes/teleports self | One incidental leap |
| `hp-scaling` | Scales on **HP values** | Shield-value scaling |
| `invincibility` | Meaningful immunity windows | Do not drop when a skill grants a **post-trigger damage + control immunity window** (e.g. Brutus Indomitable after fatal blow) |
| `battle-start-burst` | Deals damage in the **first ~2–3s** of battle | Buff/shield/debuff/energy/summon setup at battle start without immediate damage; delayed openers (Frieren 15s); terrain bombs without a damage clause (Kulu debris); sequential battle-start cycles where damage is not the first effect (Cyran Mythic+) |
| `high-initial-energy` | **Effective IE ≥ 500** on the ultimate when fully built (meta + max ascension bonus) | IE below 500; free/guaranteed early ult without IE fill (`battle-start-ult` instead, e.g. Eironn, Niru) |
| `non-ult-utility` | Meaningful combat value from non-ultimate skills via **Path A** (≥ 2 `high` fields across qualifying Skill1/Skill2/Ex sections) or **Path B** (strong non-ult attacks, opening burst mages, or hp-scaling shield damage — see audit script) | `high-damage-ult` or `battle-start-ult` present; Ultimate text triggers at battle start; non-ult value is mostly ultimate-support; aggregated non-ultimate overview alone (use per-section audit) |

**`non-ult-utility` audit** — per-section skill overview, skipping ultimate-support
sections (skills that primarily buff/enhance the ultimate). Re-audit when skill
summaries or magnitude thresholds change:

```bash
python3 scripts/audit_non_ult_utility.py
```

Ultimate-support heuristic: section summary or skill text mentions
`ultimate` / `ult` / `signature skill` together with buff/enhance/stack/volley
or "on ultimate cast". Omit that section's metrics from scoring.

**Exclusions:** skip heroes with `high-damage-ult` or `battle-start-ult`, or
whose Ultimate text matches `text_has_start_of_battle_ultimate()` (e.g. Alna).

**Utility points** per section: `high`=2, `average`=1, `low`/`none`=0. For
damage, use the higher of overview tier and peak damage-effect magnitude from
skill slices (fixes under-scored multi-hit kits like Lily May).

**Path A:** ≥ 2 `high` fields across qualifying sections.

**Path B_attack** (e.g. Lily May): utility total ≥ 4, ≥ 2 sections with ≥ 2
utility pts and ≥ 1 damage pt, ≥ 2 sections with strong-attack summary text;
not `summoner`.

**Path B_burst** (e.g. Bonnie): utility total ≥ 5, ≥ 2 sections with ≥ 2
utility pts, ≥ 2 sections with damage utility, ≥ 2 sections with average/high
slice damage; has `battle-start-burst` and (`aoe-damage` or `enemy-debuffer`).

**Path B_hp_shield** (e.g. Daimon): same utility/damage thresholds as B_burst;
has `hp-scaling`, buff utility pts ≥ 3, total damage pts ≥ 2.

## Reporting

Summarize for the user:

1. **Findings** — misleading / missing / wrongly attributed (grouped by theme)
2. **Changes** — heroes edited with before → after tags
3. **Left unchanged** — heroes reviewed and already accurate
4. **Gaps** — kits that lack a good enum tag (e.g. self-shield tanks); propose
   schema additions only if asked

Do not regenerate `heroes-overview.md` or the site unless the user asks.

## Examples

**Bonnie** — debuff-spread mage with opening hit: `enemy-debuffer`,
`aoe-damage`, `battle-start-burst` (Aging deals damage at battle start). Not
`mass-cc` (ult stun only on debuffed targets) or `dot-specialist` (debuff
stacking ≠ DoT).

**Perseus** — terrain tile buffs: `ally-buffer`, `aoe-damage`. Not
`battlefield-modification` (buff zones do not count).

**Cecia** — `summoner`, `mass-cc` (area entangle on summon), `enemy-debuffer`
(stat steal). Not `life-drain` (stat absorb ≠ lifesteal).

**Contess** — `ally-healer`, `ally-shielder`, `enemy-debuffer`, `stealth`,
`untargetable`. Enemy debuffs are the kit's other half: ATK and energy
recovery penalties, permanent silence, and violation stacking — not just
ally protection. Do not tag support-only and skip `enemy-debuffer` when
debuffs appear across multiple skills or the skill overview lists
`debuffs`.

**Florabelle** — buffs/shields **summons**, not allies: `summoner`,
`aoe-damage`. Not `battle-start-burst` (battle-start Spiny summon is setup,
not burst), `ally-buffer` / `ally-shielder`.

**Mehira / Shemira** — voidlings and ghosts are **spell-form** damage, not
battlefield companions: keep `aoe-damage`, `life-drain`, etc. Not `summoner`
(cannot be targeted or destroyed; exist only briefly).

**Tasi** — `aoe-damage`, `cheat-death`, `mass-cc`, `self-repositioner`.
`cheat-death` from Fluttering Dream: butterfly form at 50% HP loss with
invincibility and self-heal (up to twice per battle). Not `revive` (self-only).

**Cyran** — `high-initial-energy` (400 base IE + 200 Supreme bonus = 600).
Not `battle-start-burst` (Mythic+ battle-start cycle leads with self-buff before
damage). **Bryon** — both `high-initial-energy` (1000 IE) and `battle-start-ult`
(falcon setup + early ult pattern); not every high-IE hero has `battle-start-ult`.

For more edge cases, see [pitfalls.md](pitfalls.md).
