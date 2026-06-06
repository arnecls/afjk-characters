#!/usr/bin/env node
/**
 * Downloads hero skill data from afk-journey.fandom.com via the
 * MediaWiki wikitext API and writes heroes2.md.
 *
 * The output structure mirrors Heroes.md (from generate-heroes-md.js)
 * and additionally includes Skill Range and Initial Energy per skill.
 *
 * Hero list sourced from:
 * https://afk-journey.fandom.com/wiki/Hero/List
 * (Category:Playable_Heroes, fetched 2026-06-06)
 */

const fs = require('fs');
const path = require('path');

const API = 'https://afk-journey.fandom.com/api.php';
const OUT = path.join(__dirname, '..', 'heroes2.md');
const CONCURRENCY = 4;

// All playable heroes from Category:Playable_Heroes (alphabetical).
const HERO_NAMES = [
  'Aliceth', 'Alna', 'Alsa', 'Antandra', 'Arden', 'Atalanta', 'Athalia',
  'Aurora', 'Baelran', 'Berial', 'Bonnie', 'Brutus', 'Bryon', 'Callan',
  'Carolina', 'Cassadee', 'Cecia', 'Chippy', 'Contess', 'Cryonaia', 'Cyran',
  'Daimon', 'Damian', 'Dionel', 'Dunlingr', 'Eironn', 'Elijah & Lailah',
  'Evie', 'Faramor', 'Fay', 'Florabelle', 'Frieren', 'Galahad', 'Gerda',
  'Granny Dahnie', 'Gunnar', 'Gwyneth', 'Hammie', 'Harak', 'Hepler',
  'Hewynn', 'Himmel', 'Hodgkin', 'Hugin', 'Igor', 'Indris', 'Isabella',
  'Kafra', 'Koko', 'Kordan', 'Korin', 'Kruger', 'Kulu', 'Laios', 'Lenya',
  'Lily May', 'Lorsan', 'Lucca', 'Lucius', 'Lucy', 'Ludovic', 'Lumont',
  'Lyca', 'Marcille', 'Marilee', 'Mehira', 'Mikola', 'Mirael', 'Nara',
  'Natsu', 'Nazrik', 'Nerion', 'Niru', 'Odie', 'Pandora', 'Pang', 'Parisa',
  'Perseus', 'Phraesto', 'Pippa', 'Ravion', 'Reinier', 'Rhys', 'Rowan',
  'Saida', 'Salazer', 'Satrana', 'Scarlita', 'Seth', 'Shadewing', 'Shakir',
  'Shemira', 'Silven', 'Silvina', 'Sinbad', 'Smokey & Meerky', 'Solise',
  'Sonja', 'Soren', 'Sylphira', 'Talene', 'Tasi', 'Temesia', 'Thador',
  'Thoran', 'Tilaya', 'Ulmus', 'Vala', 'Valen', 'Valka', 'Velara',
  'Viperian', 'Walker', 'Zandrok', 'Zanie', 'Zorya',
];

// Maps the fandom {{Skill |type = X}} field to the Heroes.md section
// heading and the unlock label shown in italics under the skill name.
const SKILL_TYPE_MAP = {
  'Ultimate':        {
    section: 'Ultimate',
    unlock: 'Unlocks at Level 1',
  },
  'Skill I':         {
    section: 'Skill1',
    unlock: 'Unlocks at Level 11',
  },
  'Skill II':        {
    section: 'Skill2',
    unlock: 'Unlocks at Level 31',
  },
  'Hero Focus':      {
    section: 'Unlocks at Legendary+',
    unlock: 'Unlocks at Legendary+',
  },
  'Exclusive Skill': {
    section: 'Ex. Skill',
    unlock: 'Unlocks at Mythic+',
  },
  'Enhance Force':   {
    section: 'Unlocks at Supreme+',
    unlock: 'Unlocks at Supreme+',
  },
};

// ---------------------------------------------------------------------------
// Wikitext processing
// ---------------------------------------------------------------------------

/**
 * Replace common fandom wiki template syntax and wikilinks with plain text.
 * Handles {{ATK|N%}}, {{HP|N%}}, {{PWR|N%|...}}, {{b|X}}, {{e|term}},
 * [[links]], and generic faction/status templates.
 */
function processWikitext(text) {
  if (!text) return '';
  return text
    // MediaWiki bold: '''text''' → text
    .replace(/'''([^']+)'''/g, '$1')
    // MediaWiki italic: ''text'' → text
    .replace(/''([^']+)''/g, '$1')
    // Bold-only template: {{b|value}} → value
    .replace(/\{\{b\|([^}]+)\}\}/g, '$1')
    // ATK-based damage: {{ATK|N%}} → N% (ATK-based)
    .replace(/\{\{ATK\|([^}]+)\}\}/g, '$1 (ATK-based)')
    // HP-based value: {{HP|N%}} → N% (HP-based)
    .replace(/\{\{HP\|([^}]+)\}\}/g, '$1 (HP-based)')
    // Power scaling (ult / skill / both / etc.): keep first param only
    .replace(/\{\{PWR\|([^|}]+)(?:\|[^}]*)?\}\}/g, '$1')
    // Glossary tooltip: {{e|term}} → term
    .replace(/\{\{e\|([^}]+)\}\}/g, '$1')
    // Status / faction / rarity templates like {{Celestial}}, {{S-Level}}
    .replace(/\{\{([A-Z][A-Za-z0-9-]+)\}\}/g, '$1')
    // Wiki link with display text: [[Page|Text]] → Text
    .replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, '$2')
    // Wiki link without display text: [[Page]] → Page
    .replace(/\[\[([^\]]+)\]\]/g, '$1')
    // File / image links: strip entirely
    .replace(/\[\[(?:File|Image):[^\]]+\]\]/g, '')
    // Remaining unknown templates: strip
    .replace(/\{\{[^}]+\}\}/g, '')
    // HTML line-break tags → space
    .replace(/<br\s*\/?>/gi, ' ')
    // Strip any remaining HTML tags
    .replace(/<[^>]+>/g, '')
    // Collapse extra whitespace (but preserve intentional line breaks)
    .replace(/[ \t]+/g, ' ')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

/**
 * Normalise a cooldown value: "7" → "7s", "7s" → "7s".
 * Returns null when the input is absent.
 */
function normaliseCD(cd) {
  if (!cd) return null;
  const s = cd.trim();
  return /^\d+(\.\d+)?$/.test(s) ? `${s}s` : s;
}

/**
 * Format the range field: "8" → "8 tiles", "1" → "1 tile",
 * "Global" → "Global".
 */
function formatRange(range) {
  if (!range) return null;
  const s = range.trim();
  if (/^\d+$/.test(s)) return s === '1' ? '1 tile' : `${s} tiles`;
  return s;
}

// ---------------------------------------------------------------------------
// Template extraction
// ---------------------------------------------------------------------------

/**
 * Find all occurrences of {{templateName\n...\n}} in wikitext and return
 * the inner content of each (between the opening newline and closing }}).
 * Handles nested {{ }} correctly.
 * Uses a trailing newline in the search key to avoid matching
 * sub-templates like {{Skill/Header}}.
 */
function extractTemplates(wikitext, templateName) {
  const results = [];
  const openStr = `{{${templateName}\n`;

  let pos = 0;
  while (pos < wikitext.length) {
    const start = wikitext.indexOf(openStr, pos);
    if (start === -1) break;

    let depth = 0;
    let i = start;
    while (i < wikitext.length - 1) {
      if (wikitext[i] === '{' && wikitext[i + 1] === '{') {
        depth++;
        i += 2;
      } else if (wikitext[i] === '}' && wikitext[i + 1] === '}') {
        depth--;
        i += 2;
        if (depth === 0) break;
      } else {
        i++;
      }
    }

    // Slice from right after the opening tag name to before the closing }}
    const innerStart = start + openStr.length;
    results.push(wikitext.slice(innerStart, i - 2));
    pos = i;
  }

  return results;
}

/**
 * Parse key = value fields from a template's inner content.
 * Lines beginning with | start a new field; subsequent lines that do not
 * begin with | are continuation lines (used for multi-line values such
 * as |buffs = \n* item1\n* item2).
 */
function parseFields(inner) {
  const fields = {};
  let currentKey = null;
  let currentLines = [];

  for (const line of inner.split('\n')) {
    if (line.startsWith('|')) {
      if (currentKey !== null) {
        fields[currentKey] = currentLines.join('\n').trim();
      }
      const eqIdx = line.indexOf('=');
      if (eqIdx !== -1) {
        currentKey = line.slice(1, eqIdx).trim();
        currentLines = [line.slice(eqIdx + 1).trim()];
      } else {
        currentKey = line.slice(1).trim();
        currentLines = [];
      }
    } else if (currentKey !== null) {
      currentLines.push(line);
    }
  }
  if (currentKey !== null) {
    fields[currentKey] = currentLines.join('\n').trim();
  }

  return fields;
}

// ---------------------------------------------------------------------------
// Level-upgrade parsing
// ---------------------------------------------------------------------------

/**
 * Parse the |buffs field of a skill template into structured level-upgrade
 * objects.  Each wiki bullet (* ...) becomes one entry numbered starting
 * at level 2.  Recognised patterns:
 *   - "Unlocks at Level N: text"
 *   - "Unlocks at Exclusive Weapon Level N: text"  → EX. +N
 *   - "Unlocks at Exclusive Equipment Refine N: text" → RN
 *   - "Level N: text"  (used in Hero Focus / Legendary+ skills)
 */
function parseLevelUpgrades(buffsText) {
  if (!buffsText) return [];

  const lines = buffsText
    .split('\n')
    .map((l) => l.trim())
    .filter((l) => l.startsWith('*') || l.startsWith('#'));

  return lines.map((line, i) => {
    const raw = line.replace(/^[*#]+\s*/, '');
    const seq = i + 2; // level numbers start at 2

    const atLevel = raw.match(/^Unlocks at Level (\d+):\s*([\s\S]+)$/);
    if (atLevel) {
      return {
        level: String(seq),
        unlock: `Unlocks at Level ${atLevel[1]}`,
        text: processWikitext(atLevel[2]),
      };
    }

    const exWeapon = raw.match(
      /^Unlocks at Exclusive Weapon Level (\d+):\s*([\s\S]+)$/
    );
    if (exWeapon) {
      return {
        level: String(seq),
        unlock: `Unlocks at EX. +${exWeapon[1]}`,
        text: processWikitext(exWeapon[2]),
      };
    }

    const exRefine = raw.match(
      /^Unlocks at Exclusive Equipment Refine (\d+):\s*([\s\S]+)$/
    );
    if (exRefine) {
      return {
        level: String(seq),
        unlock: `Unlocks at R${exRefine[1]}`,
        text: processWikitext(exRefine[2]),
      };
    }

    const lvOnly = raw.match(/^Level (\d+):\s*([\s\S]+)$/);
    if (lvOnly) {
      return {
        level: lvOnly[1],
        unlock: null,
        text: processWikitext(lvOnly[2]),
      };
    }

    // Fallback: keep the whole line as text
    return { level: String(seq), unlock: null, text: processWikitext(raw) };
  });
}

// ---------------------------------------------------------------------------
// Markdown rendering
// ---------------------------------------------------------------------------

function skillToMarkdown(skill) {
  const lines = [];
  lines.push(`### ${skill.section}`);
  lines.push('');
  lines.push(`**${skill.name}**`);
  lines.push(`*${skill.unlock}*`);
  lines.push('');

  // Metadata bullet points
  const meta = [];
  if (skill.cooldown && parseFloat(skill.cooldown) > 0) {
    meta.push(`- Cooldown: ${skill.cooldown}`);
  }
  if (skill.initCd && parseFloat(skill.initCd) > 0) {
    meta.push(`- Initial Cooldown: ${skill.initCd}`);
  }
  if (skill.range) {
    meta.push(`- Skill Range: ${skill.range}`);
  }
  if (skill.energy !== null && skill.energy !== undefined) {
    meta.push(`- Initial Energy: ${skill.energy}`);
  }

  if (meta.length > 0) {
    lines.push(...meta);
    lines.push('');
  }

  lines.push(skill.description || '_No description._');
  lines.push('');

  for (const lv of skill.upgrades) {
    const label = lv.unlock
      ? `Level ${lv.level} — ${lv.unlock}`
      : `Level ${lv.level}`;
    lines.push(`- ${label}: ${lv.text}`);
  }
  if (skill.upgrades.length > 0) lines.push('');

  return lines.join('\n');
}

function heroToMarkdown(hero) {
  const lines = [];
  const heading = hero.subtitle
    ? `${hero.name} - ${hero.subtitle}`
    : hero.name;
  lines.push(`## ${heading}`);
  lines.push('');

  const tags = [hero.faction, hero.heroClass, hero.damage]
    .filter(Boolean)
    .join(' · ');
  if (tags) {
    lines.push(`*${tags}*`);
    lines.push('');
  }

  if (hero.description) {
    lines.push(hero.description);
    lines.push('');
  }

  for (const skill of hero.skills) {
    lines.push(skillToMarkdown(skill));
  }

  lines.push('');
  return lines.join('\n');
}

// ---------------------------------------------------------------------------
// Fetching & parsing
// ---------------------------------------------------------------------------

async function fetchText(url) {
  const res = await fetch(url, {
    headers: { 'User-Agent': 'afkj-heroes2-md-generator/1.0' },
  });
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${url}`);
  return res.text();
}

async function fetchWikitext(heroName) {
  const pageTitle = heroName.replace(/ /g, '_');
  const url =
    `${API}?action=parse&page=${encodeURIComponent(pageTitle)}` +
    `&prop=wikitext&format=json`;
  const body = await fetchText(url);
  const data = JSON.parse(body);
  if (data.error) {
    throw new Error(data.error.info || data.error.code);
  }
  return data?.parse?.wikitext?.['*'] ?? '';
}

/**
 * Parse one hero's wikitext into a structured object ready for rendering.
 */
function parseHero(wikitext, heroName) {
  // --- Infobox ---
  const infoboxes = extractTemplates(wikitext, 'Character Infobox');
  const infobox = infoboxes.length > 0 ? parseFields(infoboxes[0]) : {};

  const name = (infobox.name ?? heroName).trim();
  const subtitle = (infobox.title ?? '').trim();
  const faction = (infobox.faction ?? '').trim();
  const heroClass = (infobox.class ?? '').trim();
  const damage = (infobox.damage ?? '').trim();
  const description = infobox.description
    ? processWikitext(infobox.description)
    : '';

  // --- Skills ---
  const skillInners = extractTemplates(wikitext, 'Skill');
  const skills = [];

  for (const inner of skillInners) {
    const fields = parseFields(inner);
    const skillType = (fields.type ?? '').trim();
    const typeInfo = SKILL_TYPE_MAP[skillType];
    // Skip {{Skill/Header}}, {{Skill/Footer}} and any unrecognised types.
    if (!typeInfo) continue;

    const cooldown = normaliseCD(fields.cd);
    const initCd = normaliseCD(fields.icd);
    const range = formatRange(fields.range);
    // Include energy only when the field is explicitly present and non-empty.
    const rawEnergy = Object.prototype.hasOwnProperty.call(fields, 'energy')
      ? (fields.energy ?? '').trim()
      : null;
    const energy = rawEnergy !== null && rawEnergy !== '' ? rawEnergy : null;

    const rawDesc = fields.full || fields.lite || '';
    // Collapse any internal newlines so the description is a single block.
    const desc = processWikitext(rawDesc)
      .replace(/\n+/g, ' ')
      .replace(/ {2,}/g, ' ')
      .trim();

    skills.push({
      section: typeInfo.section,
      unlock: typeInfo.unlock,
      name: (fields.name ?? skillType).trim(),
      cooldown,
      initCd,
      range,
      energy,
      description: desc,
      upgrades: parseLevelUpgrades(fields.buffs),
    });
  }

  return { name, subtitle, faction, heroClass, damage, description, skills };
}

// ---------------------------------------------------------------------------
// Concurrency helper
// ---------------------------------------------------------------------------

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

// ---------------------------------------------------------------------------
// Entry point
// ---------------------------------------------------------------------------

async function main() {
  console.error('Fetching heroes from afk-journey.fandom.com…');

  const heroData = await mapPool(HERO_NAMES, CONCURRENCY, async (name) => {
    try {
      const wikitext = await fetchWikitext(name);
      const hero = parseHero(wikitext, name);
      console.error(`  ✓ ${name} (${hero.skills.length} skills)`);
      return hero;
    } catch (err) {
      console.error(`  ✗ ${name}: ${err.message}`);
      return {
        name,
        subtitle: '',
        faction: '',
        heroClass: '',
        damage: '',
        description: '',
        skills: [],
      };
    }
  });

  const parts = [
    '# AFK Journey Heroes',
    '',
    'Skill data sourced from ' +
      '[AFK Journey Wiki]' +
      '(https://afk-journey.fandom.com/wiki/Hero/List).',
    'Summaries live in [heroes-overview.md](heroes-overview.md)' +
      ' (see `scripts/generate-heroes-overview.py`).',
    '',
  ];

  for (const hero of heroData) {
    if (hero) parts.push(heroToMarkdown(hero));
  }

  fs.writeFileSync(OUT, parts.join('\n'), 'utf8');
  console.error(`\nWrote ${OUT}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
