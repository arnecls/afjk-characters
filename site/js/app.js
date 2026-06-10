(function () {
  "use strict";

  const BASE = resolveBase();

  let heroes = [];
  let heroBySlug = {};
  let heroByName = {};
  let activeFaction = "";
  let activeClass = "";
  let viewMode = "grid";
  let csvHeaders = [];
  let csvRows = [];
  let sortColumn = 0;
  let sortDir = 1;

  const gridView = document.getElementById("grid-view");
  const listView = document.getElementById("list-view");
  const detailView = document.getElementById("detail-view");
  const heroGrid = document.getElementById("hero-grid");
  const heroDetail = document.getElementById("hero-detail");
  const emptyState = document.getElementById("empty-state");
  const listEmptyState = document.getElementById("list-empty-state");
  const heroesTableHead = document.getElementById("heroes-table-head");
  const heroesTableBody = document.getElementById("heroes-table-body");
  const searchInput = document.getElementById("search");
  const filtersEl = document.getElementById("filters");
  const headerBack = document.getElementById("header-back");
  const viewToggle = document.querySelector(".view-toggle");
  const siteHeader = document.querySelector(".site-header");

  function updateHeaderNav(inDetail) {
    filtersEl.classList.toggle("hidden", inDetail);
    if (headerBack) {
      headerBack.classList.toggle("hidden", !inDetail);
    }
    updateListStickyOffset();
  }

  function updateListStickyOffset() {
    if (!siteHeader) {
      return;
    }
    document.documentElement.style.setProperty(
      "--list-sticky-top",
      siteHeader.offsetHeight + "px"
    );
  }

  function inferBase() {
    const path = location.pathname;
    const heroIdx = path.indexOf("/hero/");
    if (heroIdx !== -1) {
      return path.slice(0, heroIdx + 1);
    }
    if (!path.endsWith("/")) {
      const last = path.lastIndexOf("/");
      if (last >= 0) {
        return path.slice(0, last + 1);
      }
    }
    return path.endsWith("/") ? path : path + "/";
  }

  function resolveBase() {
    if (location.protocol === "file:") {
      return inferBase();
    }
    const meta = document.querySelector('meta[name="github-pages-base"]');
    const configured = meta && meta.content;
    if (configured && location.pathname.startsWith(configured)) {
      return configured;
    }
    return inferBase();
  }

  function isLocalFile() {
    return location.protocol === "file:";
  }

  function assetUrl(relative) {
    if (isLocalFile()) {
      return relative;
    }
    return BASE + relative;
  }

  function heroHash(slug) {
    return "#hero/" + encodeURIComponent(slug);
  }

  function heroUrl(slug) {
    if (isLocalFile()) {
      return heroHash(slug);
    }
    return BASE + heroHash(slug);
  }

  function homeUrl() {
    if (isLocalFile()) {
      return location.pathname;
    }
    return BASE;
  }

  function slugFromLocation() {
    const hashMatch = location.hash.match(/^#hero\/([^/?#]+)/);
    if (hashMatch) {
      return decodeURIComponent(hashMatch[1]);
    }
    const path = location.pathname;
    const prefix = BASE.replace(/\/$/, "");
    if (path.startsWith(prefix + "/hero/")) {
      return decodeURIComponent(
        path.slice((prefix + "/hero/").length).replace(/\/$/, "")
      );
    }
    if (path.indexOf("/hero/") !== -1) {
      return decodeURIComponent(
        path.split("/hero/")[1].replace(/\/$/, "")
      );
    }
    return null;
  }

  function redirectLegacyHeroPath() {
    if (location.hash.match(/^#hero\//)) {
      return;
    }
    const path = location.pathname;
    const idx = path.indexOf("/hero/");
    if (idx === -1) {
      return;
    }
    const slug = path.slice(idx + 6).replace(/\/$/, "");
    if (!slug) {
      return;
    }
    const base = path.slice(0, idx + 1);
    history.replaceState(null, "", base + heroHash(decodeURIComponent(slug)));
  }

  function iconPath(kind, value) {
    if (!value) return null;
    const fname = value.toLowerCase().replace(/\s+/g, "");
    return "assets/icons/" + kind + "/" + fname + ".png";
  }

  function factionClass(faction) {
    if (!faction) return "";
    return "badge-faction-" + faction.toLowerCase().replace(/\s+/g, "");
  }

  function escapeHtml(text) {
    return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function linkifyHero(name, slug) {
    if (slug && heroBySlug[slug]) {
      return (
        '<a href="' +
        escapeHtml(heroUrl(slug)) +
        '" class="hero-link" data-slug="' +
        escapeHtml(slug) +
        '">' +
        escapeHtml(name) +
        "</a>"
      );
    }
    return escapeHtml(name);
  }

  function renderInline(text) {
    const parts = [];
    let last = 0;
    const re = /`([^`]+)`/g;
    let match;
    while ((match = re.exec(text))) {
      parts.push(escapeHtml(text.slice(last, match.index)));
      parts.push(formatTag(match[1]));
      last = match.index + match[0].length;
    }
    parts.push(escapeHtml(text.slice(last)));
    let out = parts.join("");
    out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    return out;
  }

  const QUALITY_CLASS = {
    high: "chip-q-high",
    medium: "chip-q-medium",
    low: "chip-q-low",
  };

  const QUALITY_EMOJI = {
    high: "📈",
    medium: "⚖️",
    low: "📉",
  };

  const SPEED_CLASS = {
    slow: "chip-s-slow",
    normal: "chip-s-normal",
    fast: "chip-s-fast",
  };

  const SPEED_EMOJI = {
    slow: "🐢",
    normal: "⏱️",
    fast: "🚀",
  };

  const QUALITY_TOOLTIPS = {
    high:
      "Top third vs the roster for this effect (parsed %, reach, " +
      "frequency, or CC duration; fully ascended).",
    medium: "Middle band vs other heroes with the same effect label.",
    low: "Below average vs the roster for this effect type.",
  };

  const SPEED_TOOLTIPS = {
    slow:
      "Slow to cast: longer cooldown, initial delay, or ultimate " +
      "energy fill time.",
    normal: "Typical cast timing for this skill group across the roster.",
    fast:
      "Quick to cast: short delay, low cooldown, or battle-start " +
      "override.",
  };

  const SIGNATURE_FUEL_TOOLTIP =
    "Signature skill casts slowly; Haste and Energy recovery " +
    "buffs are especially valuable.";

  function conditionalTooltip(text) {
    const lower = text.toLowerCase();
    if (lower.indexOf("conditional (frequent)") !== -1) {
      return "Often applies in a fight; magnitude is not reduced.";
    }
    if (lower.indexOf("conditional (rare)") !== -1) {
      return (
        "Situational or once per battle; magnitude is lowered " +
        "by two steps."
      );
    }
    return "";
  }

  function chipTipAttrs(tooltip) {
    if (!tooltip) {
      return "";
    }
    return (
      ' data-tip="' +
      escapeHtml(tooltip) +
      '" tabindex="0" role="button" aria-describedby="chip-tooltip"'
    );
  }

  const TAG_DEFINITIONS = {
    Physical: { emoji: "⚔️", cls: "chip-damage" },
    Magic: { emoji: "🪄", cls: "chip-damage" },
    "HP loss": { emoji: "💔", cls: "chip-damage" },
    Melee: { emoji: "🗡️", cls: "chip-damage" },
    Ranged: { emoji: "🏹", cls: "chip-damage" },
    "True damage": { emoji: "✨", cls: "chip-damage" },
    Normal: { emoji: "👊", cls: "chip-damage" },
    ATK: { emoji: "💪", cls: "chip-stat" },
    "ATK SPD": { emoji: "⚡", cls: "chip-stat" },
    "ATK SPD / Haste": { emoji: "⚡", cls: "chip-stat" },
    Haste: { emoji: "💨", cls: "chip-stat" },
    Healing: { emoji: "💚", cls: "chip-stat" },
    "Max HP": { emoji: "❤️", cls: "chip-stat" },
    Energy: { emoji: "🔋", cls: "chip-stat" },
    "DEF Penetration": { emoji: "🎯", cls: "chip-stat" },
    Crit: { emoji: "💥", cls: "chip-stat" },
    "Crit DMG Boost": { emoji: "💥", cls: "chip-stat" },
    Execution: { emoji: "🗡️", cls: "chip-stat" },
    "Life Drain": { emoji: "🩸", cls: "chip-stat" },
    Lifedrain: { emoji: "🩸", cls: "chip-stat" },
    "Physical DEF": { emoji: "🛡️", cls: "chip-stat" },
    "Magic DEF": { emoji: "🔮", cls: "chip-stat" },
    "Energy recovery": { emoji: "🔋", cls: "chip-stat" },
    Blind: { emoji: "👁️", cls: "chip-cc" },
    Stun: { emoji: "💫", cls: "chip-cc" },
    "Knock back": { emoji: "↩️", cls: "chip-cc" },
    "Knock down": { emoji: "⬇️", cls: "chip-cc" },
    Bind: { emoji: "⛓️", cls: "chip-cc" },
    Silence: { emoji: "🤐", cls: "chip-cc" },
    Charm: { emoji: "💕", cls: "chip-cc" },
    Sleep: { emoji: "😴", cls: "chip-cc" },
    Taunt: { emoji: "📣", cls: "chip-cc" },
    Frighten: { emoji: "😱", cls: "chip-cc" },
    "Haste debuff": { emoji: "🐌", cls: "chip-debuff" },
    "DoT": { emoji: "🔥", cls: "chip-debuff" },
    "ally-healer": { emoji: "💚", cls: "chip-role" },
    "ally-shielder": { emoji: "🛡️", cls: "chip-role" },
    "energy-provider": { emoji: "🔋", cls: "chip-role" },
    "battlefield-modification": { emoji: "🗺️", cls: "chip-role" },
    "cc-immunity": { emoji: "🛡️", cls: "chip-role" },
    invincibility: { emoji: "✨", cls: "chip-role" },
    "Knock up": { emoji: "⬆️", cls: "chip-cc" },
    Interrupt: { emoji: "🚫", cls: "chip-cc" },
    Displace: { emoji: "↔️", cls: "chip-cc" },
    Unaffected: { emoji: "🛡️", cls: "chip-cc" },
    Steadfast: { emoji: "🛡️", cls: "chip-cc" },
    Immune: { emoji: "🛡️", cls: "chip-cc" },
    Untargetable: { emoji: "👻", cls: "chip-cc" },
    Cleanse: { emoji: "💧", cls: "chip-cc" },
    "Max HP-based damage": { emoji: "💔", cls: "chip-damage" },
  };

  const STAT_KEYS = Object.keys(TAG_DEFINITIONS)
    .filter(function (key) {
      const cls = TAG_DEFINITIONS[key].cls;
      return cls && cls.indexOf("chip-stat") !== -1;
    })
    .sort(function (a, b) {
      return b.length - a.length;
    });

  const TARGETING_DEFINITIONS = {
    "single target": { emoji: "🎯", cls: "chip-target" },
    "multiple targets": { emoji: "👥", cls: "chip-target" },
    "all units": { emoji: "🌐", cls: "chip-target" },
    area: { emoji: "⭕", cls: "chip-target" },
    arc: { emoji: "📐", cls: "chip-target" },
    self: { emoji: "🪞", cls: "chip-target" },
    allies: { emoji: "🤝", cls: "chip-target" },
    enemies: { emoji: "☠️", cls: "chip-target" },
    global: { emoji: "🌍", cls: "chip-target" },
    "on skill": { emoji: "⏱️", cls: "chip-target" },
  };

  const MOVEMENT_DEFINITIONS = {
    stationary: { emoji: "📍", cls: "chip-movement" },
    moving: { emoji: "🏃", cls: "chip-movement" },
    "mostly stationary": { emoji: "🚶", cls: "chip-movement" },
    "high movement": { emoji: "💨", cls: "chip-movement" },
    "moving / stationary": { emoji: "↔️", cls: "chip-movement" },
  };

  const MOVEMENT_KEYS = Object.keys(MOVEMENT_DEFINITIONS).sort(function (a, b) {
    return b.length - a.length;
  });

  const TARGETING_PHRASES = [
    { re: /\bMultiple targets\b/gi, key: "multiple targets" },
    { re: /\bSingle target\b/gi, key: "single target" },
    { re: /\bAll units\b/gi, key: "all units" },
    { re: /\bEnemies\b/gi, key: "enemies" },
    { re: /\bGlobal\b/gi, key: "global" },
    { re: /\bOn Skill\b/gi, key: "on skill" },
    { re: /\bArea\b/g, key: "area" },
    { re: /\bArc\b/g, key: "arc" },
    { re: /\bSelf\b/g, key: "self" },
  ];

  function normalizeToken(text) {
    return text.replace(/\u200b/g, "").trim();
  }

  function normalizeSummaryText(text) {
    return text.replace(/\s+/g, " ").trim();
  }

  function splitSummarySegments(text) {
    return normalizeSummaryText(text)
      .split(/\s*(?:—|–)\s*/)
      .map(function (s) {
        return s.trim();
      })
      .filter(Boolean);
  }

  function isInsideHtmlTag(html, index) {
    const before = html.slice(0, index);
    const lastOpen = before.lastIndexOf("<");
    const lastClose = before.lastIndexOf(">");
    return lastOpen > lastClose;
  }

  function isInsideChipSpan(html, index) {
    const before = html.slice(0, index);
    const openTag = "<span class=\"chip";
    let openPos = -1;
    let searchFrom = 0;
    for (;;) {
      const idx = before.indexOf(openTag, searchFrom);
      if (idx === -1) {
        break;
      }
      openPos = idx;
      searchFrom = idx + 1;
    }
    if (openPos === -1) {
      return false;
    }
    const closePos = before.indexOf("</span>", openPos);
    return closePos === -1 || closePos >= index;
  }

  function enhancePlainTargetingInHtml(html) {
    let out = html;
    TARGETING_PHRASES.forEach(function (entry) {
      out = out.replace(entry.re, function (match, offset) {
        if (
          isInsideHtmlTag(out, offset) ||
          isInsideChipSpan(out, offset)
        ) {
          return match;
        }
        const def = TARGETING_DEFINITIONS[entry.key];
        if (!def) {
          return match;
        }
        return chipSpan(def.emoji, match, def.cls);
      });
    });
    return out;
  }

  function chipifyTargetingSegment(segment) {
    const normalized = unwrapBackticks(segment.trim());
    if (!normalized) {
      return "";
    }
    return normalized
      .split(/\s*,\s*/)
      .map(function (part) {
        return tokenToHtml(normalizeToken(part));
      })
      .join(" ");
  }

  function chipSpan(emoji, text, cls, tooltip) {
    const attrs =
      ' class="chip ' +
      cls +
      (tooltip ? " chip-has-tip" : "") +
      '"' +
      (tooltip ? chipTipAttrs(tooltip) : "");
    return "<span" + attrs + ">" + emoji + " " + escapeHtml(text) + "</span>";
  }

  function tryChipify(token) {
    const text = normalizeToken(token);
    if (!text) {
      return null;
    }
    const lower = text.toLowerCase();

    if (QUALITY_CLASS[lower]) {
      return formatTag(text);
    }
    if (lower === "signature fuel") {
      return formatTag(text);
    }

    const targeting = TARGETING_DEFINITIONS[lower];
    if (targeting) {
      return chipSpan(targeting.emoji, text, targeting.cls);
    }

    if (TAG_DEFINITIONS[text]) {
      const def = TAG_DEFINITIONS[text];
      return chipSpan(def.emoji, text, def.cls);
    }
    for (const key of Object.keys(TAG_DEFINITIONS)) {
      if (key.toLowerCase() === lower) {
        const def = TAG_DEFINITIONS[key];
        return chipSpan(def.emoji, key, def.cls);
      }
    }

    return null;
  }

  function tokenToHtml(token) {
    const chip = tryChipify(token);
    return chip !== null ? chip : escapeHtml(token.trim());
  }

  function chipifyEffectName(name) {
    const tierMatch = name.match(/^(.+?)\s*(\([^)]+\))\s*$/);
    const label = tierMatch ? tierMatch[1].trim() : name.trim();
    const tierSuffix = tierMatch ? " " + escapeHtml(tierMatch[2]) : "";

    const direct = tryChipify(label);
    if (direct) {
      return direct + tierSuffix;
    }

    const viaIdx = label.indexOf(" via ");
    if (viaIdx !== -1) {
      const left = label.slice(0, viaIdx).trim();
      const right = label.slice(viaIdx + 5).trim();
      const leftChip = chipifyLeadingStat(left);
      const rightChip = chipifyLeadingStat(right);
      if (leftChip !== null || rightChip !== null) {
        const leftHtml =
          leftChip !== null ? leftChip : escapeHtml(left);
        const rightHtml =
          rightChip !== null ? rightChip : escapeHtml(right);
        return leftHtml + " via " + rightHtml + tierSuffix;
      }
    }

    const leadingStat = chipifyLeadingStat(label);
    if (leadingStat) {
      return leadingStat + tierSuffix;
    }

    const leadingCc = chipifyLeadingCcType(label);
    if (leadingCc) {
      return leadingCc + tierSuffix;
    }

    return escapeHtml(name);
  }

  function chipifyLeadingCcType(label) {
    const ccKeys = Object.keys(TAG_DEFINITIONS).filter(function (key) {
      const cls = TAG_DEFINITIONS[key].cls;
      return cls && cls.indexOf("chip-cc") !== -1;
    });
    ccKeys.sort(function (a, b) {
      return b.length - a.length;
    });

    const labelLower = label.toLowerCase();
    for (let i = 0; i < ccKeys.length; i++) {
      const cc = ccKeys[i];
      const ccLower = cc.toLowerCase();
      if (labelLower === ccLower) {
        return tryChipify(cc);
      }
      if (
        labelLower.startsWith(ccLower + " ") ||
        labelLower.startsWith(ccLower + " HP")
      ) {
        return tryChipify(cc) + escapeHtml(label.slice(cc.length));
      }
    }
    return null;
  }

  function chipifyLeadingStat(label) {
    const labelLower = label.toLowerCase();
    for (let i = 0; i < STAT_KEYS.length; i++) {
      const stat = STAT_KEYS[i];
      const statLower = stat.toLowerCase();
      if (labelLower === statLower) {
        return tryChipify(stat);
      }
      if (labelLower.startsWith(statLower + " ")) {
        return tryChipify(stat) + escapeHtml(label.slice(stat.length));
      }
    }
    return null;
  }

  function unwrapBackticks(text) {
    const trimmed = text.trim();
    const match = trimmed.match(/^`([^`]+)`$/);
    return match ? match[1].trim() : trimmed;
  }

  function promoteStrongToDamageChips(html) {
    return html.replace(/<strong>([^<]+)<\/strong>/g, function (_match, name) {
      const chip = tryChipify(name.trim());
      return chip !== null ? chip : "<strong>" + name + "</strong>";
    });
  }

  function renderEmDashLine(text) {
    const segments = splitSummarySegments(text);

    const trailingParts = [];

    function popTrailingQuality() {
      if (!segments.length) {
        return;
      }
      const raw = segments[segments.length - 1];
      const unwrapped = unwrapBackticks(raw);
      const lower = unwrapped.toLowerCase();
      if (QUALITY_CLASS[lower]) {
        trailingParts.unshift(formatTag(unwrapped));
        segments.pop();
      }
    }

    function popTrailingConditional() {
      if (!segments.length) {
        return;
      }
      const last = segments[segments.length - 1];
      if (last.indexOf("conditional") !== -1) {
        trailingParts.unshift(
          '<span class="chip chip-generic chip-has-tip"' +
            chipTipAttrs(conditionalTooltip(last)) +
            ">🎲 " +
            escapeHtml(last) +
            "</span>"
        );
        segments.pop();
      }
    }

    popTrailingConditional();
    popTrailingQuality();
    popTrailingConditional();

    const first = segments.shift();
    let firstHtml;
    if (/^Primary damage type/i.test(first)) {
      firstHtml = promoteStrongToDamageChips(renderInline(first));
    } else {
      firstHtml = chipifyEffectName(first);
    }

    const targetingHtml = segments
      .map(function (seg) {
        return chipifyTargetingSegment(seg);
      })
      .join(" ");

    return enhancePlainTargetingInHtml(
      [firstHtml, targetingHtml, trailingParts.join(" ")]
        .filter(Boolean)
        .join(" ")
    );
  }

  function renderRichLine(raw) {
    const text = normalizeSummaryText(raw);

    if (/\s*(?:—|–)\s*/.test(text)) {
      return renderEmDashLine(text);
    }

    const parenMatch = text.match(/^(.+?)\s*\(([^)]+)\)\s*(.*)$/);
    if (parenMatch && !/^Primary damage type/i.test(text)) {
      const prefixHtml = chipifyEffectName(parenMatch[1].trim());
      const innerParts = parenMatch[2]
        .split(/\s*,\s*/)
        .map(function (s) {
          return normalizeToken(s);
        })
        .filter(Boolean);
      const innerHtml = innerParts.map(tokenToHtml).join(" ");
      const suffixRaw = parenMatch[3].trim();
      const suffixHtml = suffixRaw ? renderInline(suffixRaw) : "";
      return enhancePlainTargetingInHtml(
        prefixHtml +
          " (" +
          innerHtml +
          ")" +
          (suffixHtml ? " " + suffixHtml : "")
      );
    }

    return enhancePlainTargetingInHtml(
      promoteStrongToDamageChips(renderInline(text))
    );
  }

  function formatTag(raw) {
    const text = raw.trim();
    const lower = text.toLowerCase();

    if (lower === "signature fuel") {
      return chipSpan(
        "⚡",
        "signature fuel",
        "chip-signature-fuel",
        SIGNATURE_FUEL_TOOLTIP
      );
    }
    if (QUALITY_CLASS[lower]) {
      return chipSpan(
        QUALITY_EMOJI[lower],
        text,
        "chip-quality " + QUALITY_CLASS[lower],
        QUALITY_TOOLTIPS[lower]
      );
    }
    if (SPEED_CLASS[lower]) {
      return chipSpan(
        SPEED_EMOJI[lower],
        text,
        "chip-speed " + SPEED_CLASS[lower],
        SPEED_TOOLTIPS[lower]
      );
    }

    const def = TAG_DEFINITIONS[text];
    if (!def) {
      for (const key of Object.keys(TAG_DEFINITIONS)) {
        if (key.toLowerCase() === lower) {
          const match = TAG_DEFINITIONS[key];
          return (
            '<span class="chip ' +
            match.cls +
            '">' +
            match.emoji +
            " " +
            escapeHtml(key) +
            "</span>"
          );
        }
      }
    }
    if (def) {
      return (
        '<span class="chip ' +
        def.cls +
        '">' +
        def.emoji +
        " " +
        escapeHtml(text) +
        "</span>"
      );
    }

    const label = text.replace(/-/g, " ");
    return (
      '<span class="chip chip-generic">🏷️ ' + escapeHtml(label) + "</span>"
    );
  }

  const PRYDWEN_TIER_MODES = [
    { key: "afk_stages", label: "AFK Stages" },
    { key: "dream_realm", label: "Dream Realm" },
    { key: "dream_realm_endless", label: "Dream Realm (Endless)" },
    { key: "pvp", label: "PVP" },
  ];

  const TIER_CSV_COLUMNS = [
    { header: "AFK Stages tier", key: "afk_stages" },
    { header: "Dream Realm tier", key: "dream_realm" },
    { header: "Dream Realm Endless tier", key: "dream_realm_endless" },
    { header: "PVP tier", key: "pvp" },
  ];

  const TIER_CSV_HEADERS = {};
  TIER_CSV_COLUMNS.forEach(function (tierCol) {
    TIER_CSV_HEADERS[tierCol.header] = true;
  });

  function prydwenTierClass(tier) {
    if (!tier) {
      return "tier-unknown";
    }
    const normalized = String(tier).replace(/\+/g, "-plus");
    return "tier-" + normalized.toLowerCase();
  }

  function formatTierColumnHeader(col) {
    if (col.endsWith(" tier")) {
      return (
        escapeHtml(col.slice(0, -5)) + "<br>" + escapeHtml("tier")
      );
    }
    return escapeHtml(col);
  }

  function renderTierTableCell(tier) {
    const value = (tier || "").trim();
    if (!value) {
      return "";
    }
    return (
      '<span class="tier-chip tier-chip-table ' +
      prydwenTierClass(value) +
      '"><span class="tier-grade">' +
      escapeHtml(value) +
      "</span></span>"
    );
  }

  function augmentCsvWithTiers() {
    if (!csvHeaders.length || !Object.keys(heroByName).length) {
      return;
    }
    const classIdx = csvHeaders.indexOf("Class");
    if (classIdx === -1) {
      return;
    }

    const missing = TIER_CSV_COLUMNS.filter(function (tierCol) {
      return csvHeaders.indexOf(tierCol.header) === -1;
    });
    if (missing.length) {
      const insertAt = classIdx + 1;
      missing.forEach(function (tierCol, offset) {
        csvHeaders.splice(insertAt + offset, 0, tierCol.header);
      });
      csvRows = csvRows.map(function (row) {
        const newRow = row.slice();
        missing.forEach(function (_, offset) {
          newRow.splice(insertAt + offset, 0, "");
        });
        return newRow;
      });
    }

    const colByKey = {};
    TIER_CSV_COLUMNS.forEach(function (tierCol) {
      const idx = csvHeaders.indexOf(tierCol.header);
      if (idx !== -1) {
        colByKey[tierCol.key] = idx;
      }
    });

    csvRows.forEach(function (row) {
      const hero = heroByName[row[0] || ""];
      if (!hero || !hero.prydwenTiers) {
        return;
      }
      Object.keys(colByKey).forEach(function (key) {
        const idx = colByKey[key];
        if (!String(row[idx] || "").trim()) {
          row[idx] = hero.prydwenTiers[key] || "";
        }
      });
    });
  }

  function renderPrydwenTierBoxes(tiers) {
    if (!tiers) {
      return "";
    }
    let html = '<div class="tier-box-row">';
    PRYDWEN_TIER_MODES.forEach(function (mode) {
      const tier = tiers[mode.key];
      if (!tier) {
        return;
      }
      html +=
        '<span class="tier-chip ' +
        prydwenTierClass(tier) +
        '">' +
        '<span class="tier-grade">' +
        escapeHtml(tier) +
        "</span>" +
        '<span class="tier-mode">' +
        escapeHtml(mode.label) +
        "</span></span>";
    });
    html += "</div>";
    return html;
  }

  function stripPrydwenTierLine(md) {
    if (!md) {
      return md;
    }
    const parts = md.split("\n\n");
    if (parts.length < 3) {
      return md;
    }
    if (!parts[0].endsWith("'s behavior")) {
      return md;
    }
    if (parts[1].startsWith("- ") || parts[1].startsWith("#")) {
      return md;
    }
    return [parts[0], parts.slice(2).join("\n\n")].join("\n\n");
  }

  function splitBehavior(md) {
    const marker = "#### Skill overview";
    const idx = md.indexOf(marker);
    if (idx === -1) {
      return { behavior: md, skillOverview: null };
    }
    return {
      behavior: md.slice(0, idx).trim(),
      skillOverview: md.slice(idx).trim(),
    };
  }

  function renderSummaryCards(md) {
    const cards = [];
    let current = null;

    md.split("\n").forEach(function (line) {
      if (line.startsWith("### Summary")) {
        return;
      }
      if (line.startsWith("#### ")) {
        if (current) {
          cards.push(current);
        }
        current = { title: line.slice(5).trim(), items: [] };
        return;
      }
      if (line.startsWith("- ") && current) {
        current.items.push(line.slice(2));
      }
    });
    if (current) {
      cards.push(current);
    }
    if (!cards.length) {
      return "";
    }

    let html = '<div class="detail-section summary-section">';
    html += "<h2>Summary</h2>";
    html += '<div class="summary-grid">';
    cards.forEach(function (card) {
      html += '<div class="summary-card">';
      html += "<h4>" + renderInline(card.title) + "</h4>";
      if (card.items.length) {
        html += "<ul>";
        card.items.forEach(function (item) {
          html += "<li>" + renderRichLine(item) + "</li>";
        });
        html += "</ul>";
      }
      html += "</div>";
    });
    html += "</div></div>";
    return html;
  }

  function extractChipHtml(html) {
    if (!html || html.indexOf('<span class="chip') !== 0) {
      return null;
    }
    const end = html.indexOf("</span>");
    if (end === -1) {
      return null;
    }
    return html.slice(0, end + 7);
  }

  function chipifySkillCardTag(raw) {
    let tag = raw.trim();
    if (!tag) {
      return "";
    }
    tag = tag
      .replace(
        /\s*\((?:Legendary\+|Mythic\+|Supreme\+|EX\+\d+)\)/gi,
        ""
      )
      .trim();

    const direct = tryChipify(tag);
    if (direct) {
      return direct;
    }

    const ccChip = extractChipHtml(chipifyLeadingCcType(tag));
    if (ccChip) {
      return ccChip;
    }

    const statChip = extractChipHtml(chipifyLeadingStat(tag));
    if (statChip) {
      return statChip;
    }

    const effectChip = extractChipHtml(chipifyEffectName(tag));
    if (effectChip) {
      return effectChip;
    }

    const label = tag.replace(/\s*\([^)]*\)/g, "").trim();
    if (!label) {
      return "";
    }
    return chipSpan("🏷️", label, "chip-generic");
  }

  const SKILL_CARD_DAMAGE_KEYS = [
    "HP loss",
    "Max HP-based damage",
    "True damage",
    "Physical",
    "Magic",
    "DoT",
  ];

  const SKILL_CARD_CC_KEYS = Object.keys(TAG_DEFINITIONS)
    .filter(function (key) {
      const cls = TAG_DEFINITIONS[key].cls;
      return cls && cls.indexOf("chip-cc") !== -1;
    })
    .sort(function (a, b) {
      return b.length - a.length;
    });

  function skillCardChipKey(raw) {
    let tag = raw.trim().toLowerCase();
    if (!tag) {
      return "";
    }
    tag = tag
      .replace(
        /\s*\((?:legendary\+|mythic\+|supreme\+|ex\+\d+)\)/gi,
        ""
      )
      .trim();

    let i;
    for (i = 0; i < SKILL_CARD_DAMAGE_KEYS.length; i++) {
      const dt = SKILL_CARD_DAMAGE_KEYS[i].toLowerCase();
      if (tag === dt || tag.indexOf(dt + " ") === 0) {
        return dt;
      }
    }
    for (i = 0; i < SKILL_CARD_CC_KEYS.length; i++) {
      const cc = SKILL_CARD_CC_KEYS[i].toLowerCase();
      if (tag === cc || tag.indexOf(cc + " ") === 0) {
        return cc;
      }
    }
    for (i = 0; i < STAT_KEYS.length; i++) {
      const stat = STAT_KEYS[i].toLowerCase();
      if (tag === stat || tag.indexOf(stat + " ") === 0) {
        return stat;
      }
    }
    if (tag.indexOf("healing") !== -1) {
      return "healing";
    }
    return tag.replace(/\s*\([^)]*\)/g, "").trim();
  }

  function renderSkillCardTags(tags) {
    if (!tags || !tags.length) {
      return "";
    }

    const seen = new Set();
    let html = "";
    tags.forEach(function (tag) {
      const key = skillCardChipKey(tag);
      if (!key || seen.has(key)) {
        return;
      }
      seen.add(key);
      const chip = chipifySkillCardTag(tag);
      if (chip) {
        html += chip;
      }
    });
    return html;
  }

  function stripSkillSummarySubsections(md) {
    const marker = "##### ";
    const idx = md.indexOf(marker);
    if (idx === -1) {
      return md;
    }
    return md.slice(0, idx).trim();
  }

  function renderSkillOverviewMetrics(md) {
    if (!md) {
      return "";
    }
    const metrics = stripSkillSummarySubsections(md);
    const lines = metrics.split("\n").filter(function (line) {
      return !line.startsWith("#### ");
    });
    return renderMarkdown(lines.join("\n"), { skillOverview: true });
  }

  function renderSkillCards(cards) {
    if (!cards || !cards.length) {
      return "";
    }

    let html = '<div class="skill-card-grid">';
    cards.forEach(function (card) {
      const tags = card.tags || card.effects || [];
      html +=
        '<div class="skill-card" data-skill-category="' +
        escapeHtml(card.category) +
        '">';
      html += "<h4>" + escapeHtml(card.label) + "</h4>";
      if (card.summary) {
        html +=
          '<p class="skill-card-summary">' +
          escapeHtml(card.summary) +
          "</p>";
      }
      if (tags.length) {
        html +=
          '<div class="skill-card-tags">' +
          renderSkillCardTags(tags) +
          "</div>";
      }
      html += "</div>";
    });
    html += "</div>";
    return html;
  }

  function renderHeroCompactCard(slug, name, bodyHtml) {
    const hero = heroBySlug[slug];
    const portrait = hero ? hero.portrait : "assets/portraits/" + name + ".png";
    return (
      '<article class="hero-compact-card" data-slug="' +
      escapeHtml(slug) +
      '" tabindex="0" role="link" aria-label="' +
      escapeHtml(name) +
      '">' +
      '<img src="' +
      assetUrl(portrait) +
      '" alt="" loading="lazy" onerror="this.style.opacity=0.3">' +
      '<div class="hero-compact-body">' +
      '<div class="hero-compact-name">' +
      linkifyHero(name, slug) +
      "</div>" +
      (bodyHtml || "") +
      "</div></article>"
    );
  }

  function renderHeroRowCard(slug, name, bodyHtml) {
    const hero = heroBySlug[slug];
    const portrait = hero ? hero.portrait : "assets/portraits/" + name + ".png";
    return (
      '<article class="hero-row-card" data-slug="' +
      escapeHtml(slug) +
      '" tabindex="0" role="link" aria-label="' +
      escapeHtml(name) +
      '">' +
      '<img src="' +
      assetUrl(portrait) +
      '" alt="" loading="lazy" onerror="this.style.opacity=0.3">' +
      '<div class="hero-row-body">' +
      '<div class="hero-row-name">' +
      linkifyHero(name, slug) +
      "</div>" +
      (bodyHtml || "") +
      "</div></article>"
    );
  }

  function renderHeroRowList(items, layoutClass) {
    if (!items.length) {
      return "";
    }
    return (
      '<div class="hero-row-list' +
      (layoutClass ? " " + layoutClass : "") +
      '">' +
      items.join("") +
      "</div>"
    );
  }

  function renderTrueDamageOverviewLine(text) {
    const match = text.match(/^\*\*True damage\*\*:\s*(.+)$/i);
    if (!match) {
      return null;
    }
    const entries = match[1]
      .split(/\s*,\s*/)
      .map(function (s) {
        return s.trim();
      })
      .filter(Boolean);
    const rendered = entries.map(function (entry) {
      const entryMatch = entry.match(/^(.+?)\s+`(high|medium|low)`$/i);
      if (!entryMatch) {
        return renderInline(entry);
      }
      const typeName = entryMatch[1].trim();
      const quality = entryMatch[2].trim();
      const typeChip = tryChipify(typeName);
      const qualityChip = formatTag(quality);
      return (
        (typeChip !== null ? typeChip : escapeHtml(typeName)) +
        " " +
        qualityChip
      );
    });
    return "<strong>True damage</strong>: " + rendered.join(", ");
  }

  function formatMovementChip(text) {
    const trimmed = text.trim();
    if (!trimmed) {
      return null;
    }
    const lower = trimmed.toLowerCase();
    for (let i = 0; i < MOVEMENT_KEYS.length; i++) {
      const key = MOVEMENT_KEYS[i];
      if (lower === key.toLowerCase()) {
        const def = MOVEMENT_DEFINITIONS[key];
        return chipSpan(def.emoji, trimmed, def.cls);
      }
    }
    return null;
  }

  function renderSignatureSkillLine(text, hero) {
    const match = text.match(/^\*\*Signature skill\*\*:\s*(.+)$/i);
    if (!match) {
      return null;
    }
    const body = match[1].trim();
    if (!hero || !hero.signatureSkill) {
      return (
        "<strong>Signature skill</strong>: " + escapeHtml(body)
      );
    }
    return (
      '<strong>Signature skill</strong>: <a href="#" class="signature-skill-link" data-skill-category="' +
      escapeHtml(hero.signatureSkill.category) +
      '">' +
      escapeHtml(body) +
      "</a>"
    );
  }

  function renderMovementLine(text) {
    const match = text.match(/^\*\*Movement\*\*:\s*(.+)$/i);
    if (!match) {
      return null;
    }
    const rest = match[1].trim();
    const paren = rest.match(/^(.+?)\s*(\([^)]+\))\s*$/);
    const base = paren ? paren[1].trim() : rest;
    const suffix = paren ? " " + escapeHtml(paren[2]) : "";
    const chip = formatMovementChip(base);
    return (
      "<strong>Movement</strong>: " +
      (chip !== null ? chip : escapeHtml(base)) +
      suffix
    );
  }

  function renderSkillOverviewItem(text) {
    const trueDamage = renderTrueDamageOverviewLine(text);
    if (trueDamage !== null) {
      return trueDamage;
    }
    return renderInline(text);
  }

  function renderBehaviorItem(text, options) {
    const hero = options && options.behaviorHero;
    const signature = renderSignatureSkillLine(text, hero);
    if (signature !== null) {
      return signature;
    }
    const movement = renderMovementLine(text);
    if (movement !== null) {
      return movement;
    }
    return renderInline(text);
  }

  function renderMarkdown(md, options) {
    if (!md) return "";
    const skillOverview = options && options.skillOverview;
    const renderItem = skillOverview
      ? renderSkillOverviewItem
      : function (text) {
          return renderBehaviorItem(text, options);
        };
    const lines = md.split("\n");
    const parts = [];
    let inList = false;

    function closeList() {
      if (inList) {
        parts.push("</ul>");
        inList = false;
      }
    }

    for (const raw of lines) {
      const line = raw.trimEnd();
      if (!line.trim()) {
        closeList();
        continue;
      }

      if (line.startsWith("##### ")) {
        closeList();
        parts.push("<h5>" + renderInline(line.slice(6)) + "</h5>");
      } else if (line.startsWith("#### ")) {
        closeList();
        parts.push("<h4>" + renderInline(line.slice(5)) + "</h4>");
      } else if (line.startsWith("### ")) {
        closeList();
        parts.push("<h3>" + renderInline(line.slice(4)) + "</h3>");
      } else if (line.startsWith("- ")) {
        if (!inList) {
          parts.push("<ul>");
          inList = true;
        }
        parts.push("<li>" + renderItem(line.slice(2)) + "</li>");
      } else {
        closeList();
        parts.push("<p>" + renderInline(line) + "</p>");
      }
    }
    closeList();
    return parts.join("\n");
  }

  function renderBadges(hero) {
    const badges = [];
    if (hero.faction) {
      const icon = iconPath("factions", hero.faction);
      badges.push(
        '<span class="badge ' +
          factionClass(hero.faction) +
          '">' +
          (icon
            ? '<img src="' + assetUrl(icon) + '" alt="" loading="lazy">'
            : "") +
          escapeHtml(hero.faction) +
          "</span>"
      );
    }
    if (hero.class) {
      const icon = iconPath("class", hero.class);
      badges.push(
        '<span class="badge">' +
          (icon
            ? '<img src="' + assetUrl(icon) + '" alt="" loading="lazy">'
            : "") +
          escapeHtml(hero.class) +
          "</span>"
      );
    }
    if (hero.damage_type) {
      badges.push(
        '<span class="badge">' + escapeHtml(hero.damage_type) + "</span>"
      );
    }
    return badges.join("");
  }

  function heroMatchesSearch(h, q) {
    if (!q) {
      return true;
    }
    const tokens = q.split(/\s+/).filter(Boolean);
    return tokens.every(function (token) {
      return (
        h.name.toLowerCase().indexOf(token) !== -1 ||
        (h.faction || "").toLowerCase().indexOf(token) !== -1 ||
        (h.class || "").toLowerCase().indexOf(token) !== -1
      );
    });
  }

  function filteredHeroes() {
    const q = (searchInput.value || "").trim().toLowerCase();
    return heroes.filter(function (h) {
      if (activeFaction && h.faction !== activeFaction) {
        return false;
      }
      if (activeClass && h.class !== activeClass) {
        return false;
      }
      if (!heroMatchesSearch(h, q)) {
        return false;
      }
      return true;
    });
  }

  function filteredHeroNames() {
    const names = {};
    filteredHeroes().forEach(function (h) {
      names[h.name] = true;
    });
    return names;
  }

  function parseCsv(text) {
    const rows = [];
    let row = [];
    let field = "";
    let inQuotes = false;
    for (let i = 0; i < text.length; i++) {
      const c = text[i];
      if (inQuotes) {
        if (c === '"') {
          if (text[i + 1] === '"') {
            field += '"';
            i++;
          } else {
            inQuotes = false;
          }
        } else {
          field += c;
        }
      } else if (c === '"') {
        inQuotes = true;
      } else if (c === ",") {
        row.push(field);
        field = "";
      } else if (c === "\n" || (c === "\r" && text[i + 1] === "\n")) {
        row.push(field);
        if (row.some(function (cell) {
          return cell.length > 0;
        })) {
          rows.push(row);
        }
        row = [];
        field = "";
        if (c === "\r") {
          i++;
        }
      } else if (c !== "\r") {
        field += c;
      }
    }
    if (field.length || row.length) {
      row.push(field);
      rows.push(row);
    }
    return rows;
  }

  function renderBadgeChip(label, kind) {
    if (!label) {
      return "";
    }
    if (kind === "faction") {
      const icon = iconPath("factions", label);
      return (
        '<span class="badge ' +
        factionClass(label) +
        '">' +
        (icon
          ? '<img src="' +
            assetUrl(icon) +
            '" alt="" loading="lazy">'
          : "") +
        escapeHtml(label) +
        "</span>"
      );
    }
    if (kind === "class") {
      const icon = iconPath("class", label);
      return (
        '<span class="badge">' +
        (icon
          ? '<img src="' +
            assetUrl(icon) +
            '" alt="" loading="lazy">'
          : "") +
        escapeHtml(label) +
        "</span>"
      );
    }
    return (
      '<span class="badge">' + escapeHtml(label) + "</span>"
    );
  }

  function renderTableCell(column, value) {
    if (!value || !value.trim()) {
      return "";
    }
    if (column === "Faction") {
      return renderBadgeChip(value, "faction");
    }
    if (column === "Class") {
      return renderBadgeChip(value, "class");
    }
    if (
      column === "Signature skill speed" ||
      column === "Non-ultimate speed"
    ) {
      return formatTag(value.trim());
    }
    if (
      column === "DoT" ||
      column === "HoT" ||
      column === "Summons" ||
      column === "Energy provider"
    ) {
      if (value.trim().toLowerCase() === "yes") {
        return '<span class="chip chip-generic">✓ yes</span>';
      }
      return escapeHtml(value);
    }
    if (column === "Movement") {
      const chip = formatMovementChip(value);
      if (chip !== null) {
        return chip;
      }
      return (
        '<span class="chip chip-movement">🚶 ' +
        escapeHtml(value.trim()) +
        "</span>"
      );
    }
    if (TIER_CSV_HEADERS[column]) {
      return renderTierTableCell(value);
    }
    return value
      .split(/\s*;\s*/)
      .map(function (part) {
        return renderTableEntry(part.trim());
      })
      .join(" ");
  }

  function renderTableEntry(text) {
    if (/\s*(?:—|–)\s*/.test(text)) {
      return renderRichLine(text);
    }
    return text
      .split(/\s*,\s*/)
      .map(function (part) {
        const chip = tryChipify(part.trim());
        return chip !== null ? chip : escapeHtml(part.trim());
      })
      .join(" ");
  }

  function compareCsvRows(a, b) {
    const av = (a[sortColumn] || "").trim().toLowerCase();
    const bv = (b[sortColumn] || "").trim().toLowerCase();
    if (!av && !bv) {
      return 0;
    }
    if (!av) {
      return 1;
    }
    if (!bv) {
      return -1;
    }
    if (av < bv) {
      return -sortDir;
    }
    if (av > bv) {
      return sortDir;
    }
    return 0;
  }

  function renderList() {
    if (!csvHeaders.length) {
      heroesTableHead.innerHTML = "";
      heroesTableBody.innerHTML =
        "<tr><td class=\"empty-state\">Table data missing. Run " +
        "<code>just render-site</code>.</td></tr>";
      listEmptyState.classList.add("hidden");
      return;
    }

    const allowed = filteredHeroNames();
    let rows = csvRows.filter(function (row) {
      return allowed[row[0]];
    });
    rows = rows.slice().sort(compareCsvRows);

    let headHtml = "<tr>";
    csvHeaders.forEach(function (col, idx) {
      let cls = "sortable";
      if (idx === sortColumn) {
        cls += sortDir === 1 ? " sort-asc" : " sort-desc";
      }
      if (col === "Name") {
        cls += " col-name";
      }
      if (TIER_CSV_HEADERS[col]) {
        cls += " col-tier";
      }
      headHtml +=
        '<th class="' +
        cls +
        '" data-col="' +
        idx +
        '">' +
        (TIER_CSV_HEADERS[col] ? formatTierColumnHeader(col) : escapeHtml(col)) +
        "</th>";
    });
    headHtml += "</tr>";
    heroesTableHead.innerHTML = headHtml;

    let bodyHtml = "";
    rows.forEach(function (row) {
      const name = row[0] || "";
      const hero = heroByName[name];
      bodyHtml += "<tr>";
      row.forEach(function (cell, idx) {
        const col = csvHeaders[idx];
        let inner;
        if (col === "Name") {
          if (hero) {
            inner =
              '<a href="' +
              escapeHtml(heroUrl(hero.slug)) +
              '" class="hero-link col-name-link" data-slug="' +
              escapeHtml(hero.slug) +
              '">' +
              '<span class="col-name-text">' +
              escapeHtml(name) +
              "</span>" +
              '<img class="col-name-portrait" src="' +
              assetUrl(hero.portrait) +
              '" alt="" loading="lazy" onerror="this.style.opacity=0.3">' +
              "</a>";
          } else {
            inner = escapeHtml(name);
          }
        } else {
          let cellValue = cell;
          if (hero && TIER_CSV_HEADERS[col] && !String(cellValue || "").trim()) {
            const tierCol = TIER_CSV_COLUMNS.find(function (t) {
              return t.header === col;
            });
            if (tierCol && hero.prydwenTiers) {
              cellValue = hero.prydwenTiers[tierCol.key] || "";
            }
          }
          inner = renderTableCell(col, cellValue);
        }
        let tdCls = "";
        if (col === "Name") {
          tdCls = " class=\"col-name\"";
        } else if (TIER_CSV_HEADERS[col]) {
          tdCls = " class=\"col-tier\"";
        }
        bodyHtml += "<td" + tdCls + ">" + inner + "</td>";
      });
      bodyHtml += "</tr>";
    });
    heroesTableBody.innerHTML = bodyHtml;
    listEmptyState.classList.toggle("hidden", rows.length > 0);
  }

  function renderGrid() {
    const list = filteredHeroes();
    heroGrid.innerHTML = list
      .map(function (h) {
        return (
          '<article class="hero-card" data-slug="' +
          escapeHtml(h.slug) +
          '" tabindex="0" role="link" aria-label="' +
          escapeHtml(h.name) +
          '">' +
          '<img src="' +
          assetUrl(h.portrait) +
          '" alt="" loading="lazy" onerror="this.style.opacity=0.3">' +
          '<div class="card-body">' +
          "<h2>" +
          escapeHtml(h.name) +
          "</h2>" +
          '<div class="badges">' +
          renderBadges(h) +
          "</div></div></article>"
        );
      })
      .join("");

    emptyState.classList.toggle("hidden", list.length > 0);
  }

  function renderCurrentView() {
    if (viewMode === "list") {
      renderList();
    } else {
      renderGrid();
    }
  }

  function showIndexView() {
    detailView.classList.add("hidden");
    gridView.classList.toggle("hidden", viewMode !== "grid");
    listView.classList.toggle("hidden", viewMode !== "list");
    updateHeaderNav(false);
    renderCurrentView();
  }

  function renderSynergies(sections, heroName) {
    const syn = sections.benefits_from;
    if (!syn) return "";

    let html = '<div class="detail-section">';
    html +=
      "<h2>Units " + escapeHtml(heroName) + " benefits from</h2>";

    if (syn.intro) {
      html +=
        '<div class="synergy-intro">' +
        renderInline(syn.intro.replace(/\n/g, " ")) +
        "</div>";
    }

    if (syn.partners && syn.partners.length) {
      html += renderHeroRowList(
        syn.partners.map(function (p) {
          let body = "";
          if (p.reasons && p.reasons.length) {
            body += '<ul class="hero-row-reasons">';
            p.reasons.forEach(function (r) {
              body += "<li>" + renderRichLine(r) + "</li>";
            });
            body += "</ul>";
          }
          return renderHeroRowCard(p.slug, p.name, body);
        })
      );
    } else {
      html +=
        "<p><em>No synergy partners matched stat buffs or enablers.</em></p>";
    }

    if (syn.benefited_by) {
      const bb = syn.benefited_by;
      html +=
        "<h3>Units benefitting most from " + escapeHtml(heroName) + "</h3>";
      if (bb.intro) {
        html += "<p>" + renderInline(bb.intro) + "</p>";
      }
      if (bb.overflow_reasons && bb.overflow_reasons.length) {
        html += "<ul>";
        bb.overflow_reasons.forEach(function (r) {
          html += "<li>" + renderRichLine(r) + "</li>";
        });
        html += "</ul>";
      }
      if (bb.strongest_note) {
        html += "<p>" + renderInline(bb.strongest_note) + "</p>";
      }
      if (bb.heroes && bb.heroes.length) {
        html += renderHeroRowList(
          bb.heroes.map(function (h) {
            return renderHeroCompactCard(h.slug, h.name, "");
          }),
          "hero-compact-grid-4"
        );
      }
    }

    html += "</div>";
    return html;
  }

  function renderReplacements(sections) {
    const reps = sections.replacements;
    if (!reps || !reps.length) return "";

    let html = '<div class="detail-section">';
    html += "<h2>Replacement options</h2>";
    reps.forEach(function (cat) {
      html += '<div class="replacement-category">';
      html += "<h4>" + escapeHtml(cat.category) + "</h4>";
      html += renderHeroRowList(
        cat.entries.map(function (e) {
          let body = "";
          if (e.detail) {
            body =
              '<div class="hero-compact-detail">' +
              renderInline(e.detail) +
              "</div>";
          }
          return renderHeroCompactCard(e.slug, e.name, body);
        }),
        "hero-compact-grid-3"
      );
      html += "</div>";
    });
    html += "</div>";
    return html;
  }

  function showDetail(hero) {
    gridView.classList.add("hidden");
    listView.classList.add("hidden");
    detailView.classList.remove("hidden");

    let html = '<div class="detail-header">';
    html +=
      '<img class="detail-portrait" src="' +
      assetUrl(hero.portrait) +
      '" alt="" onerror="this.style.opacity=0.3">';
    html += '<div class="detail-title">';
    html += "<h1>" + escapeHtml(hero.name) + "</h1>";
    if (hero.title && hero.title !== hero.name) {
      html +=
        '<p class="detail-subtitle">' + escapeHtml(hero.title) + "</p>";
    }
    html += '<div class="badges badges-left">' + renderBadges(hero) + "</div>";
    if (hero.description) {
      html +=
        '<p class="detail-desc">' + escapeHtml(hero.description) + "</p>";
    }
    html += "</div></div>";

    if (hero.sections.behavior) {
      const parts = splitBehavior(hero.sections.behavior);
      if (parts.behavior || hero.prydwenTiers) {
        html += '<div class="detail-section">';
        if (hero.prydwenTiers) {
          html += renderPrydwenTierBoxes(hero.prydwenTiers);
        }
        if (parts.behavior) {
          const behaviorMd = hero.prydwenTiers
            ? stripPrydwenTierLine(parts.behavior)
            : parts.behavior;
          html += renderMarkdown(behaviorMd, { behaviorHero: hero });
        }
        html += "</div>";
      }
      if (
        parts.skillOverview ||
        (hero.sections.skillCards && hero.sections.skillCards.length)
      ) {
        html +=
          '<div class="detail-section summary-section skill-overview-section">';
        html += "<h2>Skill overview</h2>";
        if (parts.skillOverview) {
          const hasSkillCards =
            hero.sections.skillCards && hero.sections.skillCards.length;
          const metricsHtml = hasSkillCards
            ? renderSkillOverviewMetrics(parts.skillOverview)
            : renderMarkdown(parts.skillOverview, { skillOverview: true });
          html +=
            '<div class="skill-overview-metrics">' + metricsHtml + "</div>";
        }
        if (hero.sections.skillCards && hero.sections.skillCards.length) {
          html += renderSkillCards(hero.sections.skillCards);
        }
        html += "</div>";
      }
    }

    if (hero.sections.summary) {
      html += renderSummaryCards(hero.sections.summary);
    }

    html += renderSynergies(hero.sections, hero.name);
    html += renderReplacements(hero.sections);

    heroDetail.innerHTML = html;
    document.title = hero.name + " — AFK Journey Heroes";
    updateHeaderNav(true);
    window.scrollTo(0, 0);
  }

  function highlightSkillCard(category) {
    if (!category || !heroDetail) {
      return;
    }
    const card = heroDetail.querySelector(
      '.skill-card[data-skill-category="' + category + '"]'
    );
    if (!card || card.classList.contains("skill-card-highlight")) {
      return;
    }

    function onHighlightEnd(event) {
      if (event.animationName !== "skill-card-glow") {
        return;
      }
      card.classList.remove("skill-card-highlight");
      card.removeEventListener("animationend", onHighlightEnd);
    }

    card.addEventListener("animationend", onHighlightEnd);
    card.classList.add("skill-card-highlight");
    card.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  function showGrid() {
    document.title = "AFK Journey Heroes";
    showIndexView();
  }

  function navigateHome(replace) {
    const home = homeUrl();
    if (replace) {
      history.replaceState(null, "", home);
    } else {
      history.pushState(null, "", home);
    }
    showGrid();
  }

  function navigateTo(url, replace) {
    if (replace) {
      history.replaceState(null, "", url);
    } else {
      history.pushState(null, "", url);
    }
    route();
  }

  function route() {
    const slug = slugFromLocation();
    if (slug) {
      const hero = heroBySlug[slug];
      if (hero) {
        showDetail(hero);
        return;
      }
    }
    showGrid();
  }

  function buildFilters() {
    const factions = [];
    const classes = [];
    const seenF = {};
    const seenC = {};
    heroes.forEach(function (h) {
      if (h.faction && !seenF[h.faction]) {
        seenF[h.faction] = true;
        factions.push(h.faction);
      }
      if (h.class && !seenC[h.class]) {
        seenC[h.class] = true;
        classes.push(h.class);
      }
    });
    factions.sort();
    classes.sort();

    let html =
      '<span class="filter-label">Faction</span>';
    html +=
      '<button type="button" class="filter-btn filter-btn-all" data-filter="all">All</button>';
    factions.forEach(function (f) {
      html +=
        '<button type="button" class="filter-btn" data-filter="faction" data-value="' +
        escapeHtml(f) +
        '">' +
        escapeHtml(f) +
        "</button>";
    });
    html += '<span class="filter-label">Class</span>';
    classes.forEach(function (c) {
      html +=
        '<button type="button" class="filter-btn" data-filter="class" data-value="' +
        escapeHtml(c) +
        '">' +
        escapeHtml(c) +
        "</button>";
    });
    filtersEl.innerHTML = html;
    updateFilterActiveStates();
    updateListStickyOffset();
  }

  function updateFilterActiveStates() {
    filtersEl.querySelectorAll(".filter-btn").forEach(function (b) {
      const f = b.dataset.filter;
      if (f === "all") {
        b.classList.toggle("active", !activeFaction && !activeClass);
      } else if (f === "faction") {
        b.classList.toggle("active", b.dataset.value === activeFaction);
      } else if (f === "class") {
        b.classList.toggle("active", b.dataset.value === activeClass);
      }
    });
  }

  filtersEl.addEventListener("click", function (e) {
    const btn = e.target.closest(".filter-btn");
    if (!btn) {
      return;
    }
    if (btn.dataset.filter === "all") {
      activeFaction = "";
      activeClass = "";
    } else if (btn.dataset.filter === "faction") {
      const v = btn.dataset.value;
      activeFaction = activeFaction === v ? "" : v;
    } else if (btn.dataset.filter === "class") {
      const v = btn.dataset.value;
      activeClass = activeClass === v ? "" : v;
    }
    updateFilterActiveStates();
    renderCurrentView();
  });

  searchInput.addEventListener("input", renderCurrentView);

  if (viewToggle) {
    viewToggle.addEventListener("click", function (e) {
      const btn = e.target.closest(".view-btn");
      if (!btn) {
        return;
      }
      viewMode = btn.dataset.view;
      viewToggle.querySelectorAll(".view-btn").forEach(function (b) {
        const active = b === btn;
        b.classList.toggle("active", active);
        b.setAttribute("aria-pressed", active ? "true" : "false");
      });
      if (!detailView.classList.contains("hidden")) {
        return;
      }
      showIndexView();
    });
  }

  if (heroesTableHead) {
    heroesTableHead.addEventListener("click", function (e) {
      const th = e.target.closest("th[data-col]");
      if (!th) {
        return;
      }
      const col = parseInt(th.dataset.col, 10);
      if (col === sortColumn) {
        sortDir = -sortDir;
      } else {
        sortColumn = col;
        sortDir = 1;
      }
      renderList();
    });
  }

  document.addEventListener("click", function (e) {
    const home = e.target.closest("[data-nav-home]");
    if (home) {
      e.preventDefault();
      navigateHome();
      return;
    }

    const card = e.target.closest(".hero-card, .hero-row-card, .hero-compact-card");
    if (card && card.dataset.slug) {
      e.preventDefault();
      navigateTo(heroUrl(card.dataset.slug));
      return;
    }

    const link = e.target.closest("a[data-slug], a.hero-link");
    if (link && link.dataset.slug) {
      e.preventDefault();
      navigateTo(heroUrl(link.dataset.slug));
      return;
    }

    const sigLink = e.target.closest("a.signature-skill-link");
    if (sigLink && sigLink.dataset.skillCategory) {
      e.preventDefault();
      highlightSkillCard(sigLink.dataset.skillCategory);
    }
  });

  document.addEventListener("keydown", function (e) {
    const card = e.target.closest(".hero-card, .hero-row-card, .hero-compact-card");
    if (card && (e.key === "Enter" || e.key === " ")) {
      e.preventDefault();
      navigateTo(heroUrl(card.dataset.slug));
    }
  });

  window.addEventListener("popstate", route);
  window.addEventListener("hashchange", route);

  function initCsv(text) {
    const parsed = parseCsv(text);
    if (!parsed.length) {
      csvHeaders = [];
      csvRows = [];
      return;
    }
    csvHeaders = parsed[0];
    csvRows = parsed.slice(1);
    augmentCsvWithTiers();
    if (!detailView.classList.contains("hidden")) {
      return;
    }
    renderCurrentView();
  }

  function initHeroes(data) {
    heroes = data.heroes || [];
    heroBySlug = {};
    heroByName = {};
    heroes.forEach(function (h) {
      heroBySlug[h.slug] = h;
      heroByName[h.name] = h;
    });
    augmentCsvWithTiers();
    buildFilters();
    route();
  }

  function localServerHint() {
    return (
      "<code>python3 -m http.server</code> from the " +
      "<code>site/</code> directory (after " +
      "<code>just render-site</code>)."
    );
  }

  function loadHeroData() {
    if (location.protocol === "file:") {
      heroGrid.innerHTML =
        '<p class="empty-state">Open this site via a local web server: ' +
        localServerHint() +
        "</p>";
      return;
    }
    fetch(assetUrl("data/heroes.json"))
      .then(function (r) {
        if (!r.ok) throw new Error("Failed to load hero data");
        return r.json();
      })
      .then(initHeroes)
      .catch(function (err) {
        heroGrid.innerHTML =
          '<p class="empty-state">Could not load hero data: ' +
          escapeHtml(String(err)) +
          ". Run <code>just render-site</code>.</p>";
      });
  }

  function loadCsvData() {
    if (location.protocol === "file:") {
      return;
    }
    fetch(assetUrl("data/heroes-overview.csv"))
      .then(function (r) {
        if (!r.ok) {
          throw new Error("Failed to load table data");
        }
        return r.text();
      })
      .then(initCsv)
      .catch(function () {
        /* list view shows missing-data message */
      });
  }

  updateListStickyOffset();
  window.addEventListener("resize", updateListStickyOffset);
  if (siteHeader && typeof ResizeObserver !== "undefined") {
    new ResizeObserver(updateListStickyOffset).observe(siteHeader);
  }

  (function initChipTooltips() {
    const chipTooltip = document.createElement("div");
    chipTooltip.id = "chip-tooltip";
    chipTooltip.className = "chip-tooltip";
    chipTooltip.hidden = true;
    chipTooltip.setAttribute("role", "tooltip");
    document.body.appendChild(chipTooltip);

    let tipAnchor = null;
    let tipHideTimer = null;
    const hoverCapable = window.matchMedia(
      "(hover: hover) and (pointer: fine)"
    ).matches;

    function positionChipTooltip(anchor) {
      const rect = anchor.getBoundingClientRect();
      chipTooltip.style.left = rect.left + rect.width / 2 + "px";
      chipTooltip.style.top = rect.top - 8 + "px";
    }

    function showChipTooltip(anchor) {
      const text = anchor.getAttribute("data-tip");
      if (!text) {
        return;
      }
      clearTimeout(tipHideTimer);
      if (tipAnchor && tipAnchor !== anchor) {
        tipAnchor.classList.remove("chip-tip-active");
      }
      tipAnchor = anchor;
      anchor.classList.add("chip-tip-active");
      chipTooltip.textContent = text;
      chipTooltip.hidden = false;
      positionChipTooltip(anchor);
    }

    function hideChipTooltip(delay) {
      clearTimeout(tipHideTimer);
      tipHideTimer = setTimeout(function () {
        if (tipAnchor) {
          tipAnchor.classList.remove("chip-tip-active");
        }
        chipTooltip.hidden = true;
        tipAnchor = null;
      }, delay || 0);
    }

    if (hoverCapable) {
      document.addEventListener(
        "pointerover",
        function (e) {
          if (e.pointerType !== "mouse") {
            return;
          }
          const chip = e.target.closest(".chip[data-tip]");
          if (chip) {
            showChipTooltip(chip);
          }
        },
        true
      );
      document.addEventListener(
        "pointerout",
        function (e) {
          if (e.pointerType !== "mouse") {
            return;
          }
          const chip = e.target.closest(".chip[data-tip]");
          if (
            chip &&
            tipAnchor === chip &&
            !chip.contains(e.relatedTarget)
          ) {
            hideChipTooltip(100);
          }
        },
        true
      );
    }

    document.addEventListener("keydown", function (e) {
      const chip = e.target.closest(".chip[data-tip]");
      if (!chip) {
        return;
      }
      if (e.key === "Escape" && tipAnchor === chip) {
        hideChipTooltip(0);
        chip.blur();
        return;
      }
      if ((e.key === " " || e.key === "Enter") && !hoverCapable) {
        e.preventDefault();
        if (tipAnchor === chip) {
          hideChipTooltip(0);
        } else {
          showChipTooltip(chip);
        }
      }
    });

    document.addEventListener(
      "click",
      function (e) {
        const chip = e.target.closest(".chip[data-tip]");
        if (!chip) {
          if (tipAnchor) {
            hideChipTooltip(0);
          }
          return;
        }
        const touchLike =
          e.pointerType === "touch" || !hoverCapable;
        if (!touchLike) {
          return;
        }
        e.stopPropagation();
        if (tipAnchor === chip) {
          hideChipTooltip(0);
        } else {
          showChipTooltip(chip);
        }
      },
      true
    );

    document.addEventListener("focusin", function (e) {
      const chip = e.target.closest(".chip[data-tip]");
      if (chip) {
        showChipTooltip(chip);
      }
    });

    document.addEventListener("focusout", function (e) {
      const chip = e.target.closest(".chip[data-tip]");
      if (chip && tipAnchor === chip) {
        hideChipTooltip(0);
      }
    });

    window.addEventListener(
      "scroll",
      function () {
        if (tipAnchor && !chipTooltip.hidden) {
          positionChipTooltip(tipAnchor);
        }
      },
      true
    );

    window.addEventListener("resize", function () {
      if (tipAnchor && !chipTooltip.hidden) {
        positionChipTooltip(tipAnchor);
      }
    });
  })();

  redirectLegacyHeroPath();
  loadHeroData();
  loadCsvData();
})();
