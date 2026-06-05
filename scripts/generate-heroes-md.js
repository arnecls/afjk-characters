#!/usr/bin/env node
/**
 * Scrapes https://www.yaphalla.com/heroes and writes Heroes.md
 */

const fs = require("fs");
const path = require("path");

const BASE = "https://www.yaphalla.com";
const OUT = path.join(__dirname, "..", "Heroes.md");
const CONCURRENCY = 6;

const SLOT_ORDER = [
  { key: "ultimate", section: "Ultimate" },
  { key: "skill1", section: "Skill1" },
  { key: "skill2", section: "Skill2" },
  { key: "legendary", section: "Unlocks at Legendary+" },
  { key: "ex", section: "Ex. Skill" },
  { key: "supreme", section: "Unlocks at Supreme+" },
];

const CC_PATTERNS = [
  ["Stun", /\bstun(?:ned|s)?\b/i],
  ["Knock down", /\bknock(?:s|ing)?\s+down\b/i],
  ["Frighten", /\bfrighten(?:ed|s)?\b/i],
  ["Silence", /\bsilenc(?:e|ed|es)\b/i],
  ["Charm", /\bcharm(?:ed|s)?\b/i],
  ["Sleep", /\bsleep(?:s|ing)?\b/i],
  ["Pin", /\bpin(?:ned|s)?\b/i],
  ["Move (forced)", /\b(?:pull|push|drag|displace|teleport|reposition)\b/i],
  ["Interrupt", /\binterrupt(?:ion)?\b/i],
  ["Uncontrol immunity", /\bunaffected\b|\buncontrol\b/i],
];

const STAT_PATTERNS = [
  ["ATK", /\bATK\b|\bAttack\b/i],
  ["ATK SPD", /\bATK\s*SPD\b|\battack\s+speed\b/i],
  ["Haste", /\bHaste\b/i],
  ["Crit", /\bCrit(?:ical)?\b/i],
  [
    "DEF Penetration",
    /\bDEF\s*Penetration\b|\bDefense\s+Penetration\b/i,
  ],
  ["Resilience", /\bResilience\b/i],
  ["Vitality", /\bVitality\b/i],
  ["Max HP", /\bmax\s+HP\b/i],
  ["HP", /\blost\s+HP\b|\brestores?\b.*\bHP\b/i],
  ["Energy", /\bEnergy\b/i],
  ["Shield", /\bshield\b/i],
  ["Healing", /\bheal(?:s|ing)?\b/i],
  ["Physical DEF", /\bPhys(?:ical)?\s+DEF\b/i],
  ["Magic DEF", /\bMagic\s+DEF\b/i],
  ["Damage reduction", /\b(?:less|reduced?)\s+damage\b/i],
];

const DAMAGE_PATTERNS = [
  ["Physical", /\bphysical\b/i],
  ["Magic", /\bmagic\b/i],
  ["True damage", /\btrue\s+damage\b/i],
  ["DoT", /\bdamage\s+over\s+time\b|\bDoT\b/i],
  [
    "HP-based",
    /\b(?:max|lost)\s+HP\b.*\bdamage\b|\bdamage\b.*\b(?:max|lost)\s+HP\b/i,
  ],
];

const TARGET_PATTERNS = [
  ["Self", /\b(?:herself|himself|itself|(?:to|on)\s+self)\b/i],
  ["Single target", /\b(?:an?\s+enemy|the\s+enemy|target|foe)\b/i],
  ["Multiple targets", /\b(?:enemies|foes)\b/i],
  ["All units", /\ball\s+(?:units|allies|enemies)\b/i],
  ["Adjacent", /\badjacent\b/i],
  ["Area / path", /\b(?:area|path|in\s+her\s+path)\b/i],
  ["Farthest enemy", /\bfarthest\s+enemy\b/i],
];

function heroSlug(name) {
  return encodeURIComponent(name);
}

function decodeEntities(s) {
  return s
    .replace(/&#x27;/g, "'")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"');
}

function htmlFragmentToText(html) {
  return decodeEntities(
    html
      .replace(/<script[\s\S]*?<\/script>/gi, "")
      .replace(/<style[\s\S]*?<\/style>/gi, "")
      .replace(/<br\s*\/?>/gi, " ")
      .replace(/<[^>]+>/g, " ")
      .replace(/\s+/g, " ")
      .trim()
  );
}

function cleanRenderedText(raw) {
  return raw
    .replace(/Lite\s*Full/gi, "")
    .replace(
      /A value determined by the caster's ATK\.?/gi,
      "(ATK-based)"
    )
    .replace(
      /A value determined by the caster's HP\.?/gi,
      "(HP-based)"
    )
    .replace(
      /Increase in this stat with each point of (?:Ultimate|Skill) Power gained\.?/gi,
      ""
    )
    .replace(/\s+/g, " ")
    .trim();
}

function unescapeRsc(s) {
  if (!s) return "";
  return s
    .replace(/\\n/g, "\n")
    .replace(/\\"/g, '"')
    .replace(/\\u003c/g, "<")
    .replace(/\\u003e/g, ">");
}

function parseRscLevels(levelsStr) {
  const levels = [];
  const parts = levelsStr.split(/\},\{/);
  for (let i = 0; i < parts.length; i++) {
    let p = parts[i];
    if (i > 0) p = "{" + p;
    if (i < parts.length - 1) p = p + "}";

    const displayLevel = p.match(/\\"DisplayLevel\\":(\d+)/)?.[1];
    const desc = p.match(
      /\\"Description\\":\\"((?:[^"\\]|\\.)*?)\\"/
    )?.[1];
    if (!displayLevel || !desc) continue;

    const unlockLevel = p.match(/\\"UnlockLevel\\":(\d+)/)?.[1];
    const unlockMastery = p.match(/\\"UnlockMastery\\":(\d+)/)?.[1];
    const unlockEx = p.match(/\\"UnlockEx\\":(\d+)/)?.[1];

    let unlock;
    if (unlockEx) unlock = `Unlocks at EX. +${unlockEx}`;
    else if (unlockMastery) unlock = `Level ${displayLevel}`;
    else if (unlockLevel && Number(unlockLevel) > 10) {
      unlock = `Unlocks at Level ${unlockLevel}`;
    } else if (Number(displayLevel) >= 2 && Number(unlockLevel) <= 1) {
      unlock = `Unlocks at EX. +${(Number(displayLevel) - 1) * 5}`;
    } else if (unlockLevel) {
      unlock = `Unlocks at Level ${unlockLevel}`;
    } else {
      unlock = `Level ${displayLevel}`;
    }

    levels.push({
      level: displayLevel,
      unlock,
      text: unescapeRsc(desc),
    });
  }
  return levels.sort((a, b) => Number(a.level) - Number(b.level));
}

function parseRscSkillMap(html, heroName) {
  const map = new Map();
  const heroEsc = heroName.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const re = new RegExp(
    `\\\\"hero\\\\":\\\\"${heroEsc}\\\\"[\\s\\S]*?\\\\"isNPC\\\\":\\\\"\\$undefined\\\\"`,
    "g"
  );
  for (const block of html.matchAll(re)) {
    const b = block[0];
    const slot = b.match(/\\"DisplaySlot\\":(\d+)/)?.[1];
    const name = b.match(/\\"DisplayName\\":\\"([^\\]+)/)?.[1];
    if (!slot || !name) continue;

    let description =
      b.match(
        /\\"CD\\":\d+,\\"Description\\":\\"((?:[^"\\]|\\.)*)\\",\\"DisplayName\\":/
      )?.[1] ||
      b.match(
        /\\"InitCD\\":\d+,\\"Description\\":\\"((?:[^"\\]|\\.)*)\\",\\"DisplayName\\":/
      )?.[1] ||
      "";

    const levelsMatch = b.match(
      /\\"Levels\\":\[([\s\S]*?)\],\\"(?:PlusArgs|CD|TargetShapeArgs|SimpleDescription)\\"/
    );
    const levels = levelsMatch ? parseRscLevels(levelsMatch[1]) : [];

    map.set(Number(slot), {
      name,
      description: unescapeRsc(description),
      levels,
    });
  }
  return map;
}

function simplifyRscText(text) {
  return text
    .replace(/<\/?ATK>/g, "")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/\{[^}]+\}/g, "(scaled)");
}

function normalizeUnlockLabel(unlock) {
  return unlock.replace(/Level:\s*/g, "Level ");
}

function mergeLevels(htmlLevels, rscLevels) {
  if (!rscLevels.length) return htmlLevels;
  const htmlByLevel = Object.fromEntries(
    htmlLevels.map((l) => [l.level, l])
  );
  return rscLevels.map((rl) => ({
    level: rl.level,
    unlock: normalizeUnlockLabel(
      htmlByLevel[rl.level]?.unlock || rl.unlock
    ),
    text: htmlByLevel[rl.level]?.text || simplifyRscText(rl.text),
  }));
}

function parseSkillBlocksFromHtml(html) {
  const re =
    /<div class="container-primary flex flex-col size-full">([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>/g;
  const blocks = [];
  let m;
  while ((m = re.exec(html)) !== null) {
    if (!m[1].includes("<h3>")) continue;
    blocks.push(m[1]);
  }
  return blocks;
}

function parseSkillFragment(fragment, slot, rscSkill) {
  const nameMatch = fragment.match(/<h3>([^<]+)<\/h3>/);
  const name = nameMatch ? decodeEntities(nameMatch[1].trim()) : "";
  let slotLabel = "";
  const slotHtml = fragment.match(
    /<span class="text-neutral-400[^"]*">([\s\S]*?)<\/span>\s*<\/span>\s*<div[^>]*>\s*<h3>/
  );
  if (slotHtml) {
    slotLabel = cleanRenderedText(htmlFragmentToText(slotHtml[1]));
  }

  let full = cleanRenderedText(htmlFragmentToText(fragment));

  full = full
    .replace(
      /^(?:Ultimate|Skill\s*[12]|EX\.\s*Skill)\s*-\s*Unlocks at\s+Level\s+\d+\s*/i,
      ""
    )
    .replace(
      /^(?:Ultimate|Skill\s*[12]|EX\.\s*Skill)\s*-\s*Unlocks at\s+Mythic\+\s*/i,
      ""
    )
    .replace(/^Unlocks at\s+(?:Legendary\+|Mythic\+|Supreme\+)\s*/i, "")
    .replace(new RegExp(`^${escapeRe(name)}\\s*`, "i"), "")
    .trim();

  const cooldown = full.match(/Cooldown:\s*(\d+)\s*s/i);
  const initCd = full.match(/Initial Cooldown:\s*(\d+)\s*s/i);
  if (cooldown) full = full.replace(/Cooldown:\s*\d+\s*s/i, "").trim();
  if (initCd) full = full.replace(/Initial Cooldown:\s*\d+\s*s/i, "").trim();

  const levels = [];
  const upgradeStarts = [];
  const startRe =
    /\sLevel\s+(\d+)(?:\s*\|\s*Unlocks at|\s*—\s*Unlocks at|\s+(?=[A-Z]))/g;
  let sm;
  while ((sm = startRe.exec(full)) !== null) {
    const before = full.slice(Math.max(0, sm.index - 14), sm.index);
    if (/Unlocks at\s*$/i.test(before)) continue;
    const displayLevel = parseInt(sm[1], 10);
    if (displayLevel < 2 || displayLevel > 6) continue;
    upgradeStarts.push(sm.index);
  }

  let description = full;
  if (upgradeStarts.length > 0) {
    description = full.slice(0, upgradeStarts[0]).trim();
    for (let i = 0; i < upgradeStarts.length; i++) {
      const chunk = full
        .slice(
          upgradeStarts[i],
          upgradeStarts[i + 1] ?? full.length
        )
        .trim();
      const heroLevel = chunk.match(
        /^Level\s+(\d+)\s*\|\s*Unlocks at\s+Level\s+(\d+)\s+(.+)$/s
      );
      if (heroLevel) {
        levels.push({
          level: heroLevel[1],
          unlock: `Unlocks at Level ${heroLevel[2]}`,
          text: heroLevel[3].trim(),
        });
        continue;
      }
      const withUnlock = chunk.match(
        /^Level\s+(\d+)\s*\|\s*Unlocks at\s+(.+?)\s+(.+)$/s
      );
      if (withUnlock) {
        levels.push({
          level: withUnlock[1],
          unlock: normalizeUnlockLabel(`Unlocks at ${withUnlock[2].trim()}`),
          text: withUnlock[3].trim(),
        });
        continue;
      }
      const withEx = chunk.match(
        /^Level\s+(\d+)\s*—\s*Unlocks at\s+(.+?)\s+(.+)$/s
      );
      if (withEx) {
        levels.push({
          level: withEx[1],
          unlock: `Unlocks at ${withEx[2].trim()}`,
          text: withEx[3].trim(),
        });
        continue;
      }
      const plain = chunk.match(/^Level\s+(\d+)\s+(.+)$/s);
      if (plain) {
        levels.push({
          level: plain[1],
          unlock: `Level ${plain[1]}`,
          text: plain[2].trim(),
        });
      }
    }
  }

  const mergedLevels = mergeLevels(levels, rscSkill?.levels || []);

  return {
    section: slot.section,
    name: name || rscSkill?.name || "",
    slotLabel,
    cooldown: cooldown?.[1],
    initCd: initCd?.[1],
    description: simplifyRscText(
      description.trim() || rscSkill?.description || ""
    ),
    levels: mergedLevels,
  };
}

function escapeRe(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function parseHeroPage(html, heroName, meta) {
  const titleMatch = html.match(
    /<h2[^>]*>([^<]+ - [^<]+)<\/h2>/
  );
  const title = titleMatch
    ? decodeEntities(titleMatch[1].trim())
    : `${heroName}${meta.title ? ` - ${meta.title}` : ""}`;
  const descMatch = html.match(
    /<meta name="description" content="([^"]*)"/
  );
  const description = descMatch
    ? decodeEntities(descMatch[1])
    : meta.description || "";

  const rscMap = parseRscSkillMap(html, heroName);
  const blocks = parseSkillBlocksFromHtml(html);
  const skills = [];
  for (let i = 0; i < SLOT_ORDER.length && i < blocks.length; i++) {
    const slotNum = i + 1;
    skills.push(
      parseSkillFragment(blocks[i], SLOT_ORDER[i], rscMap.get(slotNum))
    );
  }

  return {
    title,
    description,
    skills,
    faction: meta.faction,
    class: meta.class,
    damageType: meta.damageType,
  };
}

function matchAny(text, patterns) {
  const found = [];
  for (const [label, re] of patterns) {
    if (re.test(text)) found.push(label);
  }
  return [...new Set(found)];
}

function analyzeTexts(texts) {
  const combined = texts.join("\n");
  return {
    stats: matchAny(combined, STAT_PATTERNS),
    cc: matchAny(combined, CC_PATTERNS),
    damage: matchAny(combined, DAMAGE_PATTERNS),
    targeting: matchAny(combined, TARGET_PATTERNS),
  };
}

function formatAnalysis(a) {
  const parts = [];
  parts.push(
    a.stats.length
      ? `Stats/effects: ${a.stats.join(", ")}`
      : "Stats/effects: None noted"
  );
  parts.push(
    a.cc.length
      ? `Debuffs/CC: ${a.cc.join(", ")}`
      : "Debuffs/CC: None noted"
  );
  const dmg = [...a.damage];
  parts.push(dmg.length ? `Damage: ${dmg.join(", ")}` : "Damage: None noted");
  parts.push(
    a.targeting.length
      ? `Targeting: ${a.targeting.join(", ")}`
      : "Targeting: None noted"
  );
  return parts.join("; ");
}

function scalingStats(texts) {
  const combined = texts.join(" ");
  const scales = [];
  if (/each point of ATK SPD|ATK SPD or Haste/i.test(combined))
    scales.push("ATK SPD and Haste");
  if (/each point of (?:Ultimate|Skill) Power/i.test(combined))
    scales.push("Ultimate Power / Skill Power");
  if (/caster's ATK|ATK-based|\(\d+%\).*ATK/i.test(combined))
    scales.push("ATK");
  if (/target'?s ATK/i.test(combined)) scales.push("Target ATK");
  if (/max HP/i.test(combined)) scales.push("Max HP");
  if (/lost HP/i.test(combined)) scales.push("Lost HP");
  if (/Energy/i.test(combined)) scales.push("Energy");
  if (/cannot exceed|up to \d+ stacks/i.test(combined))
    scales.push("Caps or stack limits mentioned in skills");
  return [...new Set(scales)];
}

function collectTexts(bySection, sections) {
  const texts = [];
  for (const sec of sections) {
    const sk = bySection[sec];
    if (!sk) continue;
    texts.push(sk.description);
    for (const lv of sk.levels) texts.push(lv.text);
  }
  return texts;
}

function buildSummary(hero) {
  const lines = [];
  const bySection = Object.fromEntries(hero.skills.map((s) => [s.section, s]));

  lines.push("### Summary");
  lines.push("");
  lines.push("#### Per Ascension");
  lines.push("");

  const ascensionNotes = [
    ["Epic / Epic+", ["Ultimate", "Skill1", "Skill2"]],
    [
      "Legendary / Legendary+",
      ["Ultimate", "Skill1", "Skill2", "Unlocks at Legendary+"],
    ],
    [
      "Mythic / Mythic+",
      [
        "Ultimate",
        "Skill1",
        "Skill2",
        "Unlocks at Legendary+",
        "Ex. Skill",
      ],
    ],
    [
      "Supreme / Supreme+",
      [
        "Ultimate",
        "Skill1",
        "Skill2",
        "Unlocks at Legendary+",
        "Ex. Skill",
        "Unlocks at Supreme+",
      ],
    ],
    [
      "Paragon 1–4",
      [
        "Ultimate",
        "Skill1",
        "Skill2",
        "Unlocks at Legendary+",
        "Ex. Skill",
        "Unlocks at Supreme+",
      ],
    ],
  ];

  for (const [tier, sections] of ascensionNotes) {
    const texts = collectTexts(bySection, sections);
    let unlock = "";
    if (tier.includes("Legendary+") && bySection["Unlocks at Legendary+"]) {
      unlock = ` Unlocks **${bySection["Unlocks at Legendary+"].name}**.`;
    } else if (tier.includes("Mythic+") && bySection["Ex. Skill"]) {
      unlock = ` Unlocks **${bySection["Ex. Skill"].name}** (Ex-weapon).`;
    } else if (tier.includes("Supreme+") && bySection["Unlocks at Supreme+"]) {
      unlock = ` Unlocks **${bySection["Unlocks at Supreme+"].name}**.`;
    }
    lines.push(
      `- **${tier}**:${unlock} ${formatAnalysis(analyzeTexts(texts))}`
    );
  }

  lines.push("");
  lines.push(
    "*Standard ascension stat bonuses (e.g. flat % ATK/HP per tier) are not listed on Yaphalla hero pages.*"
  );
  lines.push("");
  lines.push("#### Per ex-level");
  lines.push("");

  const exSkill = bySection["Ex. Skill"];
  if (exSkill) {
    lines.push(
      `- **Base (Mythic+) — ${exSkill.name}**: ${formatAnalysis(analyzeTexts([exSkill.description]))}`
    );
    for (const lv of exSkill.levels) {
      const exLabel = lv.unlock.match(/EX\.?\s*\+?\s*(\d+)/i)
        ? `EX. +${lv.unlock.match(/EX\.?\s*\+?\s*(\d+)/i)[1]}`
        : `EX. +${(Number(lv.level) - 1) * 5 || 5}`;
      lines.push(
        `- **${exLabel}**: ${formatAnalysis(analyzeTexts([lv.text]))}`
      );
    }
  } else {
    lines.push("- No Ex-weapon skill on this unit.");
  }

  lines.push("");
  lines.push("#### Stats the unit benefits from");
  lines.push("");

  const allTexts = hero.skills.flatMap((s) => [
    s.description,
    ...s.levels.map((l) => l.text),
  ]);
  const scales = scalingStats(allTexts);
  if (scales.length) {
    for (const s of scales) lines.push(`- ${s}`);
  } else {
    lines.push("- No explicit stat scaling called out in skill text.");
  }
  if (hero.damageType) {
    lines.push(`- Primary damage type (unit): **${hero.damageType}**`);
  }

  return lines.join("\n");
}

function skillToMarkdown(skill) {
  const lines = [];
  lines.push(`### ${skill.section}`);
  lines.push("");
  if (skill.name) lines.push(`**${skill.name}**`);
  if (skill.slotLabel) lines.push(`*${skill.slotLabel}*`);
  lines.push("");
  if (skill.cooldown) lines.push(`- Cooldown: ${skill.cooldown}s`);
  if (skill.initCd) lines.push(`- Initial Cooldown: ${skill.initCd}s`);
  if (skill.cooldown || skill.initCd) lines.push("");
  lines.push(skill.description || "_No description._");
  lines.push("");
  for (const lv of skill.levels) {
    const unlock = normalizeUnlockLabel(lv.unlock);
    const label = unlock.match(/Unlocks|EX/i)
      ? `Level ${lv.level} — ${unlock}`
      : `Level ${lv.level}`;
    lines.push(`- ${label}: ${lv.text}`);
  }
  if (skill.levels.length) lines.push("");
  return lines.join("\n");
}

function heroToMarkdown(hero) {
  const lines = [];
  lines.push(`## ${hero.title}`);
  lines.push("");
  if (hero.faction || hero.class) {
    const tags = [hero.faction, hero.class, hero.damageType]
      .filter(Boolean)
      .join(" · ");
    lines.push(`*${tags}*`);
    lines.push("");
  }
  if (hero.description) {
    lines.push(hero.description);
    lines.push("");
  }
  for (const skill of hero.skills) {
    lines.push(skillToMarkdown(skill));
  }
  lines.push(buildSummary(hero));
  lines.push("");
  return lines.join("\n");
}

async function fetchText(url) {
  const res = await fetch(url, {
    headers: { "User-Agent": "afkj-heroes-md-generator/1.0" },
  });
  if (!res.ok) throw new Error(`${url} → ${res.status}`);
  return res.text();
}

async function mapPool(items, limit, fn) {
  const results = new Array(items.length);
  let i = 0;
  async function worker() {
    while (i < items.length) {
      const idx = i++;
      results[idx] = await fn(items[idx], idx);
    }
  }
  await Promise.all(Array.from({ length: limit }, worker));
  return results;
}

async function main() {
  console.error("Fetching hero list…");
  const heroesJson = await fetchText(`${BASE}/api/heroes`);
  const heroes = JSON.parse(heroesJson);
  const skip = new Set([
    "Elijah",
    "Lailah",
    "Phraesto Clone",
    "Zanie Turret",
  ]);
  const names = Object.keys(heroes)
    .filter((n) => !skip.has(n))
    .sort();

  console.error(`Scraping ${names.length} heroes…`);
  const scraped = await mapPool(names, CONCURRENCY, async (name) => {
    const meta = heroes[name];
    const url = `${BASE}/heroes/${heroSlug(name)}`;
    try {
      const html = await fetchText(url);
      const hero = parseHeroPage(html, name, meta);
      console.error(`  ✓ ${name} (${hero.skills.length} skills)`);
      return hero;
    } catch (err) {
      console.error(`  ✗ ${name}: ${err.message}`);
      return {
        title: name,
        description: meta.description,
        skills: [],
        faction: meta.faction,
        class: meta.class,
        damageType: meta.damageType,
      };
    }
  });

  const parts = [
    "# AFK Journey Heroes",
    "",
    "Skill data sourced from [Yaphalla Heroes](https://www.yaphalla.com/heroes).",
    "Summaries are derived from skill text.",
    "",
  ];

  for (const hero of scraped) {
    parts.push(heroToMarkdown(hero));
  }

  fs.writeFileSync(OUT, parts.join("\n"), "utf8");
  console.error(`Wrote ${OUT} (${parts.join("\n").length} bytes)`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
