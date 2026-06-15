(function () {
  "use strict";

  const BASE = resolveBase();

  let heroes = [];
  let heroBySlug = {};
  let heroByName = {};
  let activeFaction = "";
  let activeClass = "";
  let activeRole = "";
  let viewMode = "grid";
  let csvHeaders = [];
  let csvRows = [];
  let sortColumn = 0;
  let sortDir = 1;
  let csvColumnFilters = {};
  let csvColumnFilterOptions = [];
  let openColumnFilter = -1;
  let csvColumnWidths = [];
  let columnWidthsLocked = false;
  let detailHero = null;
  let closeSkillCardPopover = function () {};

  const gridView = document.getElementById("grid-view");
  const listView = document.getElementById("list-view");
  const detailView = document.getElementById("detail-view");
  const heroGrid = document.getElementById("hero-grid");
  const heroDetail = document.getElementById("hero-detail");
  const emptyState = document.getElementById("empty-state");
  const listEmptyState = document.getElementById("list-empty-state");
  const heroesTableHead = document.getElementById("heroes-table-head");
  const heroesTableBody = document.getElementById("heroes-table-body");
  const heroesTable = document.getElementById("heroes-table");
  const searchInput = document.getElementById("search");
  const filtersPanel = document.getElementById("filters-panel");
  const filtersEl = document.getElementById("filters");
  const filtersToggle = document.getElementById("filters-toggle");
  const filtersToggleLabel = document.getElementById("filters-toggle-label");
  const FILTERS_COLLAPSE_MQ = window.matchMedia("(max-width: 600px)");
  const headerBack = document.getElementById("header-back");
  const viewToggle = document.querySelector(".view-toggle");
  const siteHeader = document.querySelector(".site-header");
  const WELCOME_WARNING_KEY = "afjk-welcome-dismissed";
  const VIEW_MODE_KEY = "afjk-view-mode";

  function readStoredViewMode() {
    try {
      const stored = localStorage.getItem(VIEW_MODE_KEY);
      if (stored === "grid" || stored === "list") {
        return stored;
      }
    } catch (e) {
      /* private mode / disabled storage */
    }
    return "grid";
  }

  function storeViewMode(mode) {
    try {
      localStorage.setItem(VIEW_MODE_KEY, mode);
    } catch (e) {
      /* private mode / disabled storage */
    }
  }

  function syncViewToggleButtons() {
    if (!viewToggle) {
      return;
    }
    viewToggle.querySelectorAll(".view-btn").forEach(function (b) {
      const active = b.dataset.view === viewMode;
      b.classList.toggle("active", active);
      b.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  function initWelcomeWarning() {
    const root = document.getElementById("welcome-warning");
    if (!root) {
      return;
    }
    if (localStorage.getItem(WELCOME_WARNING_KEY) === "1") {
      root.hidden = true;
      document.documentElement.classList.remove("welcome-warning-pending");
      return;
    }

    const dismissBtn = document.getElementById("welcome-warning-dismiss");
    const blocked = [
      siteHeader,
      document.getElementById("app"),
      document.querySelector(".site-footer"),
    ].filter(Boolean);

    function setBlocked(block) {
      root.classList.toggle("is-open", block);
      document.body.classList.toggle("welcome-warning-open", block);
      document.documentElement.classList.toggle("welcome-warning-pending", block);
      blocked.forEach(function (el) {
        if (block) {
          el.setAttribute("inert", "");
          el.setAttribute("aria-hidden", "true");
        } else {
          el.removeAttribute("inert");
          el.removeAttribute("aria-hidden");
        }
      });
    }

    function blockSitePointer(e) {
      if (root.hidden) {
        return;
      }
      if (root.contains(e.target)) {
        return;
      }
      e.preventDefault();
      e.stopPropagation();
      if (typeof e.stopImmediatePropagation === "function") {
        e.stopImmediatePropagation();
      }
    }

    function dismissWelcomeWarning() {
      root.hidden = true;
      setBlocked(false);
      try {
        localStorage.setItem(WELCOME_WARNING_KEY, "1");
      } catch (e) {
        /* ignore quota / private-mode errors */
      }
    }

    dismissBtn.addEventListener("click", dismissWelcomeWarning);

    ["click", "mousedown", "touchstart"].forEach(function (type) {
      document.addEventListener(type, blockSitePointer, true);
    });

    root.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        e.preventDefault();
      }
      if (e.key === "Tab") {
        e.preventDefault();
        dismissBtn.focus();
      }
    });

    setBlocked(true);
    dismissBtn.focus();
  }

  function updateHeaderNav(inDetail) {
    if (filtersPanel) {
      filtersPanel.classList.toggle("hidden", inDetail);
    }
    if (headerBack) {
      headerBack.classList.toggle("hidden", !inDetail);
    }
    updateListStickyOffset();
  }

  function updateFiltersToggleLabel() {
    if (!filtersToggle) {
      return;
    }
    const collapsed = filtersPanel
      ? filtersPanel.classList.contains("filters-collapsed")
      : false;
    const parts = [];
    if (activeFaction) {
      parts.push(activeFaction);
    }
    if (activeClass) {
      parts.push(activeClass);
    }
    if (activeRole) {
      const meta = ROLE_CATEGORY_META[activeRole];
      parts.push(meta ? meta.label : activeRole);
    }
    const action = collapsed ? "Show filters" : "Hide filters";
    const activeSuffix = parts.length ? " (" + parts.join(", ") + ")" : "";
    const label = action + activeSuffix;
    filtersToggle.title = action;
    filtersToggle.setAttribute("aria-label", label);
    if (filtersToggleLabel) {
      filtersToggleLabel.textContent = label;
    }
  }

  function setFiltersCollapsed(collapsed) {
    if (!filtersPanel || !filtersToggle) {
      return;
    }
    filtersPanel.classList.toggle("filters-collapsed", collapsed);
    filtersToggle.setAttribute("aria-expanded", collapsed ? "false" : "true");
    updateFiltersToggleLabel();
    updateListStickyOffset();
  }

  function initFiltersCollapse() {
    if (!filtersPanel || !filtersToggle) {
      return;
    }
    setFiltersCollapsed(FILTERS_COLLAPSE_MQ.matches);
    filtersToggle.addEventListener("click", function () {
      setFiltersCollapsed(
        !filtersPanel.classList.contains("filters-collapsed")
      );
    });
    FILTERS_COLLAPSE_MQ.addEventListener("change", function () {
      setFiltersCollapsed(FILTERS_COLLAPSE_MQ.matches);
    });
  }

  function updateListStickyOffset() {
    if (!siteHeader) {
      return;
    }
    document.documentElement.style.setProperty(
      "--list-sticky-top",
      siteHeader.offsetHeight + "px"
    );
    updateTableHeadStickyOffsets();
  }

  function updateTableHeadStickyOffsets() {
    if (!heroesTableHead) {
      return;
    }
    const labelRow = heroesTableHead.querySelector(".heroes-table-label-row");
    if (!labelRow) {
      return;
    }
    document.documentElement.style.setProperty(
      "--table-head-label-height",
      labelRow.getBoundingClientRect().height + "px"
    );
  }

  function getTableScrollEl() {
    return listView ? listView.querySelector(".table-scroll") : null;
  }

  function clearColumnFilterPanelPosition(details) {
    if (!details) {
      return;
    }
    const panel = details.querySelector(".col-filter-panel");
    if (!panel) {
      return;
    }
    panel.classList.remove("is-floating");
    panel.style.top = "";
    panel.style.left = "";
    panel.style.minWidth = "";
    panel.style.maxWidth = "";
  }

  function positionOpenColumnFilter() {
    if (openColumnFilter < 0 || !heroesTableHead) {
      return;
    }
    heroesTableHead.querySelectorAll("details.col-filter[open]").forEach(function (details) {
      if (parseInt(details.dataset.col, 10) !== openColumnFilter) {
        clearColumnFilterPanelPosition(details);
      }
    });
    const details = getOpenColumnFilterDetails();
    if (!details || !details.open) {
      return;
    }
    const panel = details.querySelector(".col-filter-panel");
    const trigger = details.querySelector(".col-filter-trigger");
    if (!panel || !trigger) {
      return;
    }
    const rect = trigger.getBoundingClientRect();
    panel.classList.add("is-floating");
    panel.style.top = Math.round(rect.bottom + 2) + "px";
    panel.style.left = Math.round(rect.left) + "px";
    panel.style.minWidth = Math.round(rect.width) + "px";
    panel.style.maxWidth = "16rem";
  }

  function getOpenColumnFilterDetails() {
    if (openColumnFilter < 0 || !heroesTableHead) {
      return null;
    }
    return heroesTableHead.querySelector(
      'details.col-filter[data-col="' + openColumnFilter + '"]'
    );
  }

  let columnFilterPointerHandler = null;

  function rectContainsPoint(rect, x, y, pad) {
    return (
      x >= rect.left - pad &&
      x <= rect.right + pad &&
      y >= rect.top - pad &&
      y <= rect.bottom + pad
    );
  }

  function isPointerInColumnFilterZone(clientX, clientY) {
    const details = getOpenColumnFilterDetails();
    if (!details || !details.open) {
      return false;
    }
    const trigger = details.querySelector(".col-filter-trigger");
    const panel = details.querySelector(".col-filter-panel");
    const pad = 6;
    if (trigger && rectContainsPoint(trigger.getBoundingClientRect(), clientX, clientY, pad)) {
      return true;
    }
    if (panel && rectContainsPoint(panel.getBoundingClientRect(), clientX, clientY, pad)) {
      return true;
    }
    return false;
  }

  function unbindColumnFilterPointerTracking() {
    if (!columnFilterPointerHandler) {
      return;
    }
    document.removeEventListener("mousemove", columnFilterPointerHandler);
    columnFilterPointerHandler = null;
  }

  function bindColumnFilterPointerTracking() {
    if (columnFilterPointerHandler) {
      return;
    }
    columnFilterPointerHandler = function (e) {
      if (openColumnFilter < 0) {
        unbindColumnFilterPointerTracking();
        return;
      }
      if (!isPointerInColumnFilterZone(e.clientX, e.clientY)) {
        closeColumnFilter();
      }
    };
    document.addEventListener("mousemove", columnFilterPointerHandler);
  }

  function closeColumnFilter() {
    const details = getOpenColumnFilterDetails();
    unbindColumnFilterPointerTracking();
    if (details && details.open) {
      details.open = false;
      return;
    }
    openColumnFilter = -1;
  }

  function closeColumnFilterOnScroll() {
    if (openColumnFilter >= 0) {
      closeColumnFilter();
    }
  }

  function measureEffectStackCellWidth(cell) {
    const entries = cell.querySelectorAll(".effect-cell-entry");
    if (!entries.length) {
      return cell.getBoundingClientRect().width;
    }
    let max = 0;
    entries.forEach(function (entry) {
      max = Math.max(max, entry.scrollWidth);
    });
    return max;
  }

  function measureColumnWidths() {
    if (!heroesTableHead || !heroesTableBody || !csvHeaders.length) {
      return;
    }
    if (!heroesTableBody.rows.length) {
      return;
    }
    const widths = new Array(csvHeaders.length).fill(0);
    const labelRow = heroesTableHead.querySelector(".heroes-table-label-row");
    if (labelRow) {
      let colIdx = 0;
      Array.from(labelRow.cells).forEach(function (cell) {
        widths[colIdx] = Math.max(
          widths[colIdx],
          cell.getBoundingClientRect().width
        );
        colIdx += cell.colSpan || 1;
      });
    }
    const filterRow = heroesTableHead.querySelector(".heroes-table-filter-row");
    if (filterRow) {
      let colIdx = 1;
      Array.from(filterRow.cells).forEach(function (cell) {
        widths[colIdx] = Math.max(
          widths[colIdx],
          cell.getBoundingClientRect().width
        );
        colIdx += 1;
      });
    }
    Array.from(heroesTableBody.rows).forEach(function (row) {
      Array.from(row.cells).forEach(function (cell, idx) {
        const col = csvHeaders[idx];
        const width =
          isEffectSortColumn(col) && cell.querySelector(".effect-cell-entry")
            ? measureEffectStackCellWidth(cell)
            : cell.getBoundingClientRect().width;
        widths[idx] = Math.max(widths[idx], width);
      });
    });
    csvColumnWidths = widths.map(function (width) {
      return Math.ceil(width);
    });
  }

  function updateTableColgroup() {
    if (!heroesTable) {
      return;
    }
    let colgroup = heroesTable.querySelector("colgroup");
    if (!csvColumnWidths.length) {
      if (colgroup) {
        colgroup.remove();
      }
      heroesTable.style.tableLayout = "";
      return;
    }
    if (!colgroup) {
      colgroup = document.createElement("colgroup");
      heroesTable.insertBefore(colgroup, heroesTableHead);
    }
    colgroup.innerHTML = csvColumnWidths
      .map(function (width) {
        return (
          '<col style="width:' +
          width +
          "px;min-width:" +
          width +
          'px">'
        );
      })
      .join("");
    heroesTable.style.tableLayout = "fixed";
  }

  function buildListBodyHtml(rows) {
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
          inner = renderTableCell(col, getListCellRawValue(row, idx, col));
        }
        let tdCls = "";
        if (col === "Name") {
          tdCls = " class=\"col-name\"";
        } else if (TIER_CSV_HEADERS[col]) {
          tdCls = " class=\"col-tier\"";
        } else if (col === "Role") {
          tdCls = " class=\"col-role\"";
        } else if (isEffectSortColumn(col)) {
          tdCls = " class=\"col-effect-stack\"";
        }
        bodyHtml += "<td" + tdCls + ">" + inner + "</td>";
      });
      bodyHtml += "</tr>";
    });
    return bodyHtml;
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

  function tryMergeTrailingLabel(before, indicator) {
    const match = before.match(/(^|[\s,])([\w][\w\s]*?)\s+$/);
    if (!match) {
      return null;
    }
    const prefix = before.slice(0, match.index) + match[1];
    const label = match[2].trim();
    const merged = mergeLabelWithIndicator(label, indicator.trim());
    if (!merged) {
      return null;
    }
    return escapeHtml(prefix) + merged;
  }

  function renderInline(text) {
    const parts = [];
    let last = 0;
    const re = /`([^`]+)`/g;
    let match;
    while ((match = re.exec(text))) {
      const merged = tryMergeTrailingLabel(
        text.slice(last, match.index),
        match[1]
      );
      if (merged) {
        parts.push(merged);
      } else {
        parts.push(escapeHtml(text.slice(last, match.index)));
        parts.push(formatTag(match[1]));
      }
      last = match.index + match[0].length;
    }
    parts.push(escapeHtml(text.slice(last)));
    let out = parts.join("");
    out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    return out;
  }

  const QUALITY_CLASS = {
    high: "chip-q-high",
    average: "chip-q-medium",
    low: "chip-q-low",
  };

  const SKILL_OVERVIEW_SPEED_LABELS = {
    speed: true,
    "first cast speed": true,
  };

  const SPEED_CLASS = {
    slow: "chip-s-slow",
    average: "chip-s-normal",
    fast: "chip-s-fast",
  };

  const SPEED_EMOJI = {
    slow: "🐢",
    average: "🚶",
    fast: "🚀",
  };

  const CC_DURATION_LABEL = {
    low: "short",
    average: "average",
    high: "long",
  };

  const QUALITY_TOOLTIPS = {
    high: "Top third vs same-role peers for this effect.",
    average:
      "Middle band vs same-role peers with the same effect label.",
    low: "Below average vs same-role peers for this effect type.",
  };

  const SPEED_TOOLTIPS = {
    slow:
      "Slow to cast: longer cooldown, initial delay, or ultimate " +
      "energy fill time.",
    average:
      "Typical cast timing for this skill group among same-role peers.",
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
    "Magic damage": { emoji: "🪄", cls: "chip-damage" },
    "Physical damage": { emoji: "⚔️", cls: "chip-damage" },
    "Magic damage from allies": { emoji: "🪄", cls: "chip-role" },
    "Debuff on target": { emoji: "🥀", cls: "chip-debuff" },
    "Multiple debuffs on target": { emoji: "🥀", cls: "chip-debuff" },
    "CC on enemies": { emoji: "💫", cls: "chip-cc" },
    "Ally stat buffs": { emoji: "💪", cls: "chip-role" },
    "Party composition": { emoji: "👥", cls: "chip-role" },
    "Continuous damage on enemies": { emoji: "🔥", cls: "chip-debuff" },
    "Enemy defeat": { emoji: "💀", cls: "chip-role" },
    "Ally Ultimate casts": { emoji: "⚡", cls: "chip-role" },
    "Ally blessing active": { emoji: "✨", cls: "chip-role" },
    ATK: { emoji: "💪", cls: "chip-stat" },
    "ATK SPD": { emoji: "⚡", cls: "chip-stat" },
    "ATK SPD / Haste": { emoji: "⚡", cls: "chip-stat" },
    Haste: { emoji: "💨", cls: "chip-stat" },
    Healing: { emoji: "💚", cls: "chip-heal" },
    "Direct healing": { emoji: "💚", cls: "chip-heal" },
    HoT: { emoji: "💚", cls: "chip-heal" },
    "Healing over time": { emoji: "💚", cls: "chip-heal" },
    Shield: { emoji: "🛡️", cls: "chip-stat" },
    "Max HP": { emoji: "❤️", cls: "chip-stat" },
    Energy: { emoji: "🔋", cls: "chip-stat" },
    "DEF Penetration": { emoji: "🎯", cls: "chip-stat" },
    Penetration: { emoji: "🎯", cls: "chip-stat" },
    Crit: { emoji: "💥", cls: "chip-stat" },
    "Crit DMG Boost": { emoji: "💥", cls: "chip-stat" },
    Execution: { emoji: "🗡️", cls: "chip-stat" },
    "Life Drain": { emoji: "🩸", cls: "chip-stat" },
    Lifedrain: { emoji: "🩸", cls: "chip-stat" },
    "Physical DEF": { emoji: "🛡️", cls: "chip-stat" },
    "Phys DEF": { emoji: "🛡️", cls: "chip-stat" },
    "Magic DEF": { emoji: "🔮", cls: "chip-stat" },
    "Energy recovery": { emoji: "🔋", cls: "chip-stat" },
    Vitality: { emoji: "🌿", cls: "chip-generic" },
    "Vitality buff": { emoji: "🌿", cls: "chip-generic" },
    "Vitality debuff": { emoji: "🥀", cls: "chip-debuff" },
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
    "ATK debuff": { emoji: "🥀", cls: "chip-debuff" },
    "Blind HP loss debuff": { emoji: "👁️", cls: "chip-debuff" },
    "DoT debuff": { emoji: "🔥", cls: "chip-debuff" },
    "Damage taken debuff": { emoji: "🥀", cls: "chip-debuff" },
    "Damage taken": { emoji: "🥀", cls: "chip-debuff" },
    "Magic damage amplification": { emoji: "🪄", cls: "chip-debuff" },
    "Magic damage reduction": { emoji: "🪄", cls: "chip-stat" },
    "Energy drain": { emoji: "🔋", cls: "chip-debuff" },
    "Energy recovery debuff": { emoji: "🔋", cls: "chip-debuff" },
    "Execution debuff": { emoji: "☠️", cls: "chip-debuff" },
    "Magic DEF debuff": { emoji: "🔮", cls: "chip-debuff" },
    "Max HP debuff": { emoji: "💔", cls: "chip-debuff" },
    "Movement speed debuff": { emoji: "🐌", cls: "chip-debuff" },
    "Phys DEF debuff": { emoji: "🛡️", cls: "chip-debuff" },
    "Healing debuff": { emoji: "🥀", cls: "chip-debuff" },
    "Crit Resist debuff": { emoji: "💥", cls: "chip-debuff" },
    "Vulnerable debuff": { emoji: "🎯", cls: "chip-debuff" },
    "Damage taken reduction": { emoji: "🛡️", cls: "chip-stat" },
    "DoT": { emoji: "🔥", cls: "chip-debuff" },
    "ally-buffer": { emoji: "📈", cls: "chip-role" },
    "ally-healer": { emoji: "💚", cls: "chip-role" },
    "ally-shielder": { emoji: "🛡️", cls: "chip-role" },
    "aoe-damage": { emoji: "💥", cls: "chip-role" },
    "aoe-healing": { emoji: "💚", cls: "chip-role" },
    "assassin": { emoji: "🎯", cls: "chip-role" },
    "battle-start-burst": { emoji: "🚀", cls: "chip-role" },
    "battle-start-ult": { emoji: "⚡", cls: "chip-role" },
    "battlefield-modification": { emoji: "🗺️", cls: "chip-role" },
    "cc-immunity": { emoji: "🔰", cls: "chip-anti-cc" },
    "cheat-death": { emoji: "♻️", cls: "chip-role" },
    "clone": { emoji: "👥", cls: "chip-role" },
    "counterattack": { emoji: "↩️", cls: "chip-role" },
    "disabler": { emoji: "🚫", cls: "chip-role" },
    "dot-specialist": { emoji: "🔥", cls: "chip-role" },
    "enemy-debuffer": { emoji: "🥀", cls: "chip-role" },
    "enemy-grouping": { emoji: "🧲", cls: "chip-role" },
    "energy-provider": { emoji: "🔋", cls: "chip-role" },
    "execute": { emoji: "☠️", cls: "chip-role" },
    "fire-attack": { emoji: "🔥", cls: "chip-role" },
    "high-damage-ult": { emoji: "💣", cls: "chip-role" },
    "hp-scaling": { emoji: "❤️", cls: "chip-role" },
    invincibility: { emoji: "✨", cls: "chip-role" },
    "life-drain": { emoji: "🩸", cls: "chip-role" },
    "mark-target": { emoji: "🎯", cls: "chip-role" },
    "mass-cc": { emoji: "💫", cls: "chip-role" },
    revive: { emoji: "✨", cls: "chip-role" },
    "self-repositioner": { emoji: "💨", cls: "chip-role" },
    "static-tile-buffer": { emoji: "📍", cls: "chip-role" },
    stealth: { emoji: "🥷", cls: "chip-role" },
    summoner: { emoji: "🐾", cls: "chip-role" },
    taunt: { emoji: "📣", cls: "chip-role" },
    transformation: { emoji: "🔄", cls: "chip-role" },
    "ultimate-cancel": { emoji: "🚫", cls: "chip-cc" },
    untargetable: { emoji: "👻", cls: "chip-role" },
    Invincible: { emoji: "✨", cls: "chip-role" },
    "Dmg and CC immunity": { emoji: "🔰", cls: "chip-anti-cc" },
    "Dmg and CC immunity (ally)": { emoji: "🔰", cls: "chip-anti-cc" },
    "Damage and control immunity": { emoji: "🔰", cls: "chip-anti-cc" },
    "Damage and control immunity (ally)": { emoji: "🔰", cls: "chip-anti-cc" },
    "Knock up": { emoji: "⬆️", cls: "chip-cc" },
    Interrupt: { emoji: "🚫", cls: "chip-cc" },
    Displace: { emoji: "↔️", cls: "chip-cc" },
    Unaffected: { emoji: "🛡️", cls: "chip-anti-cc" },
    Steadfast: { emoji: "🛡️", cls: "chip-anti-cc" },
    Immune: { emoji: "⛔", cls: "chip-anti-cc" },
    Untargetable: { emoji: "👻", cls: "chip-anti-cc" },
    Cleanse: { emoji: "💧", cls: "chip-anti-cc" },
    "Max HP damage": { emoji: "💔", cls: "chip-damage" },
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

  const HEAL_CHIP_KEYS = ["Direct healing", "Healing over time", "HoT", "Healing"]
    .sort(function (a, b) {
      return b.length - a.length;
    });

  function healingChipDisplay(text) {
    if (text === "Healing over time") {
      return "HoT";
    }
    return text;
  }

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
    "summons only": { emoji: "👻", cls: "chip-target" },
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
    { re: /\bSummons only\b/gi, key: "summons only" },
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

  function isInsideSpanClass(html, index, className) {
    const before = html.slice(0, index);
    const openTag = '<span class="' + className + '"';
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

  function isInsideSkillInlineStat(html, index) {
    return isInsideSpanClass(html, index, "skill-inline-stat");
  }

  function isInsideSkillInlineTime(html, index) {
    return isInsideSpanClass(html, index, "skill-inline-time");
  }

  function replaceOutsideChips(text, re, replacer) {
    return text.replace(re, function () {
      const args = Array.prototype.slice.call(arguments);
      const offset = args[args.length - 2];
      const match = args[0];
      if (
        isInsideHtmlTag(text, offset) ||
        isInsideChipSpan(text, offset) ||
        isInsideSkillInlineStat(text, offset) ||
        isInsideSkillInlineTime(text, offset)
      ) {
        return match;
      }
      return replacer.apply(null, args);
    });
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

  function chipDisplayLabel(text) {
    if (text === "Max HP-based damage") {
      return "Max HP damage";
    }
    return text;
  }

  function chipSpan(emoji, text, cls, tooltip) {
    const attrs =
      ' class="chip ' +
      cls +
      (tooltip ? " chip-has-tip" : "") +
      '"' +
      (tooltip ? chipTipAttrs(tooltip) : "");
    const prefix = emoji ? emoji + " " : "";
    return (
      "<span" +
      attrs +
      ">" +
      prefix +
      escapeHtml(chipDisplayLabel(text)) +
      "</span>"
    );
  }

  function behaviorTagDefinition(tag) {
    const text = (tag || "").trim();
    if (!text) {
      return null;
    }
    const lower = text.toLowerCase();
    if (TAG_DEFINITIONS[text]) {
      return TAG_DEFINITIONS[text];
    }
    for (const key of Object.keys(TAG_DEFINITIONS)) {
      if (key.toLowerCase() === lower) {
        return TAG_DEFINITIONS[key];
      }
    }
    return null;
  }

  function behaviorTagChip(tag) {
    const def = behaviorTagDefinition(tag);
    const emoji = def ? def.emoji : "🏷️";
    return chipSpan(emoji, tag.trim(), "chip-behavior-tag");
  }

  function isSpeedMetricLabel(label) {
    return SKILL_OVERVIEW_SPEED_LABELS[label.trim().toLowerCase()] === true;
  }

  function qualityIndicatorMeta(value, isCc) {
    const lower = value.toLowerCase();
    if (!QUALITY_CLASS[lower]) {
      return null;
    }
    return {
      cls: "chip-quality " + QUALITY_CLASS[lower],
      label: isCc ? CC_DURATION_LABEL[lower] : lower,
      tooltip: QUALITY_TOOLTIPS[lower],
      emoji: "",
    };
  }

  function targetingIndicatorMeta(targeting) {
    const lower = (targeting || "").trim().toLowerCase();
    if (lower !== "self") {
      return null;
    }
    const def = TARGETING_DEFINITIONS.self;
    return {
      cls: def.cls,
      label: "Self",
      tooltip: "",
      emoji: def.emoji,
    };
  }

  function resolveIndicatorMeta(label, indicator, isCc) {
    if (isSpeedMetricLabel(label)) {
      return (
        speedIndicatorMeta(indicator) ||
        qualityIndicatorMeta(indicator, isCc)
      );
    }
    return (
      qualityIndicatorMeta(indicator, isCc) ||
      speedIndicatorMeta(indicator)
    );
  }

  function speedIndicatorMeta(value) {
    const lower = value.toLowerCase();
    if (!SPEED_CLASS[lower]) {
      return null;
    }
    return {
      cls: "chip-speed " + SPEED_CLASS[lower],
      label: lower,
      tooltip: SPEED_TOOLTIPS[lower],
      emoji: SPEED_EMOJI[lower],
    };
  }

  function isCcChipClass(cls) {
    return cls === "chip-cc";
  }

  function isCcFamilyChipClass(cls) {
    return cls === "chip-cc" || cls === "chip-anti-cc";
  }

  function ccFamilyChipKeys() {
    return Object.keys(TAG_DEFINITIONS)
      .filter(function (key) {
        return isCcFamilyChipClass(TAG_DEFINITIONS[key].cls);
      })
      .sort(function (a, b) {
        return b.length - a.length;
      });
  }

  function exactTagDefinitionKey(label) {
    const trimmed = label.trim();
    if (!trimmed) {
      return null;
    }
    if (TAG_DEFINITIONS[trimmed]) {
      return trimmed;
    }
    const labelLower = trimmed.toLowerCase();
    if (
      labelLower === "max hp-based damage" ||
      labelLower === "max hp damage"
    ) {
      return "Max HP damage";
    }
    for (const key of Object.keys(TAG_DEFINITIONS)) {
      if (key.toLowerCase() === labelLower) {
        return key;
      }
    }
    return null;
  }

  const BUFF_DISPLAY_EFFECT_CHIPS = {
    "Damage taken": { emoji: "🛡️", cls: "chip-stat" },
    "Magic damage amplification": { emoji: "🪄", cls: "chip-stat" },
  };

  function resolveLeadingChip(label, polarity) {
    const trimmed = label.trim();
    if (!trimmed) {
      return { textOnly: "", remainder: "", isCc: false };
    }

    if (polarity === "buff" && BUFF_DISPLAY_EFFECT_CHIPS[trimmed]) {
      const buff = BUFF_DISPLAY_EFFECT_CHIPS[trimmed];
      return {
        emoji: buff.emoji,
        text: trimmed,
        cls: buff.cls,
        isCc: false,
        remainder: "",
      };
    }

    const exactKey = exactTagDefinitionKey(trimmed);
    if (exactKey) {
      const def = TAG_DEFINITIONS[exactKey];
      return {
        emoji: def.emoji,
        text: exactKey,
        cls: def.cls,
        isCc: isCcChipClass(def.cls),
        remainder: "",
      };
    }

    const ccKeys = ccFamilyChipKeys();

    const labelLower = trimmed.toLowerCase();
    for (let i = 0; i < ccKeys.length; i++) {
      const cc = ccKeys[i];
      const ccLower = cc.toLowerCase();
      if (
        labelLower === ccLower ||
        labelLower.startsWith(ccLower + " ") ||
        labelLower.startsWith(ccLower + " HP")
      ) {
        const def = TAG_DEFINITIONS[cc];
        return {
          emoji: def.emoji,
          text: cc,
          cls: def.cls,
          isCc: isCcChipClass(def.cls),
          remainder: trimmed.slice(cc.length),
        };
      }
    }

    for (let i = 0; i < HEAL_CHIP_KEYS.length; i++) {
      const heal = HEAL_CHIP_KEYS[i];
      const healLower = heal.toLowerCase();
      if (labelLower === healLower || labelLower.startsWith(healLower + " ")) {
        const def = TAG_DEFINITIONS[heal];
        return {
          emoji: def.emoji,
          text: healingChipDisplay(heal),
          cls: def.cls,
          isCc: false,
          remainder: trimmed.slice(heal.length),
        };
      }
    }

    for (let i = 0; i < STAT_KEYS.length; i++) {
      const stat = STAT_KEYS[i];
      const statLower = stat.toLowerCase();
      if (labelLower === statLower || labelLower.startsWith(statLower + " ")) {
        const def = TAG_DEFINITIONS[stat];
        return {
          emoji: def.emoji,
          text: stat,
          cls: def.cls,
          isCc: false,
          remainder: trimmed.slice(stat.length),
        };
      }
    }

    return { textOnly: trimmed, remainder: "", isCc: false };
  }

  function effectChipRemainder(remainder) {
    const trimmed = (remainder || "").trim().toLowerCase();
    if (trimmed === "buff" || trimmed === "debuff") {
      return "";
    }
    return remainder || "";
  }

  function formatMergedTierSuffix(tierSuffix) {
    if (!tierSuffix) {
      return "";
    }
    return (
      ' <span class="chip-merged-tier">' +
      escapeHtml(tierSuffix) +
      "</span>"
    );
  }

  function formatMergedIndicator(left, indicatorMeta, textOnlyLeft) {
    let leftHtml;
    if (left.hasIcon) {
      leftHtml =
        '<span class="chip-merged-left ' +
        left.cls +
        '">' +
        left.emoji +
        " " +
        escapeHtml(chipDisplayLabel(left.text)) +
        formatMergedTierSuffix(left.tierSuffix) +
        "</span>";
    } else {
      leftHtml =
        '<span class="chip-merged-left chip-merged-label">' +
        escapeHtml(chipDisplayLabel(left.textOnly)) +
        formatMergedTierSuffix(left.tierSuffix) +
        "</span>";
    }

    const emojiPart =
      textOnlyLeft && indicatorMeta.emoji ? indicatorMeta.emoji + " " : "";
    const rightAttrs =
      ' class="chip-merged-right ' +
      indicatorMeta.cls +
      (indicatorMeta.tooltip ? " chip-has-tip" : "") +
      '"' +
      (indicatorMeta.tooltip ? chipTipAttrs(indicatorMeta.tooltip) : "");
    const rightHtml =
      "<span" +
      rightAttrs +
      ">" +
      emojiPart +
      escapeHtml(indicatorMeta.label) +
      "</span>";

    return (
      '<span class="chip chip-merged">' +
      leftHtml +
      '<span class="chip-merged-sep" aria-hidden="true">|</span>' +
      rightHtml +
      "</span>"
    );
  }

  function mergeLabelWithIndicator(label, indicator, tierSuffix, polarity) {
    const leading = resolveLeadingChip(label, polarity);
    const meta = resolveIndicatorMeta(label, indicator, leading.isCc);
    if (!meta) {
      return null;
    }
    if (leading.emoji) {
      return (
        formatMergedIndicator(
          {
            hasIcon: true,
            emoji: leading.emoji,
            text: leading.text,
            cls: leading.cls,
            tierSuffix: tierSuffix || "",
          },
          meta,
          false
        ) + escapeHtml(effectChipRemainder(leading.remainder))
      );
    }
    return formatMergedIndicator(
      { textOnly: label, tierSuffix: tierSuffix || "" },
      meta,
      true
    );
  }

  function mergeEffectWithQuality(effectLabel, qualityValue, tierSuffix, polarity) {
    const qualityMeta = qualityIndicatorMeta(
      qualityValue,
      resolveLeadingChip(effectLabel, polarity).isCc
    );
    if (!qualityMeta) {
      return null;
    }
    const leading = resolveLeadingChip(effectLabel, polarity);
    if (leading.emoji) {
      return (
        formatMergedIndicator(
          {
            hasIcon: true,
            emoji: leading.emoji,
            text: leading.text,
            cls: leading.cls,
            tierSuffix: tierSuffix || "",
          },
          qualityMeta,
          false
        ) + escapeHtml(effectChipRemainder(leading.remainder))
      );
    }
    return formatMergedIndicator(
      { textOnly: effectLabel, tierSuffix: tierSuffix || "" },
      qualityMeta,
      true
    );
  }

  function mergeEffectWithTargeting(effectLabel, targeting, tierSuffix, polarity) {
    const targetingMeta = targetingIndicatorMeta(targeting);
    if (!targetingMeta) {
      return null;
    }
    const leading = resolveLeadingChip(effectLabel, polarity);
    if (leading.emoji) {
      return (
        formatMergedIndicator(
          {
            hasIcon: true,
            emoji: leading.emoji,
            text: leading.text,
            cls: leading.cls,
            tierSuffix: tierSuffix || "",
          },
          targetingMeta,
          false
        ) + escapeHtml(effectChipRemainder(leading.remainder))
      );
    }
    return formatMergedIndicator(
      { textOnly: effectLabel, tierSuffix: tierSuffix || "" },
      targetingMeta,
      true
    );
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
      return chipSpan(def.emoji, healingChipDisplay(text), def.cls);
    }
    for (const key of Object.keys(TAG_DEFINITIONS)) {
      if (key.toLowerCase() === lower) {
        const def = TAG_DEFINITIONS[key];
        return chipSpan(def.emoji, healingChipDisplay(key), def.cls);
      }
    }

    return null;
  }

  function tokenToHtml(token) {
    const chip = tryChipify(token);
    return chip !== null ? chip : escapeHtml(token.trim());
  }

  function chipifyEffectName(name, polarity) {
    const parsed = parseEffectLabelParts(name);
    const label = parsed.base;
    const tier = parsed.tier;

    if (label.indexOf(" via ") === -1) {
      return renderStandaloneEffectChip(label, tier, polarity);
    }

    const viaIdx = label.indexOf(" via ");
    const left = label.slice(0, viaIdx).trim();
    const right = label.slice(viaIdx + 5).trim();
    const leftChip = chipifyLeadingStat(left);
    const rightChip = chipifyLeadingStat(right);
    if (leftChip !== null || rightChip !== null) {
      let leftHtml = leftChip !== null ? leftChip : escapeHtml(left);
      let rightHtml = rightChip !== null ? rightChip : escapeHtml(right);
      if (tier) {
        const leftOnly = extractChipHtml(leftHtml);
        const rightOnly = extractChipHtml(rightHtml);
        if (leftOnly) {
          leftHtml = injectTierIntoChipHtml(leftOnly, tier) + leftHtml.slice(leftOnly.length);
        } else if (rightOnly) {
          rightHtml = injectTierIntoChipHtml(rightOnly, tier) + rightHtml.slice(rightOnly.length);
        } else {
          leftHtml += formatMergedTierSuffix(tier);
        }
      }
      return leftHtml + " via " + rightHtml;
    }

    return renderStandaloneEffectChip(label, tier, polarity);
  }

  function chipifyLeadingCcType(label) {
    const ccKeys = ccFamilyChipKeys();

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
    const exactKey = exactTagDefinitionKey(label);
    if (exactKey) {
      return tryChipify(exactKey);
    }
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

  const ASCENSION_TIER_SUFFIX_RE =
    /\s*(\((?:Legendary\+|Mythic\+|Supreme\+|EX\+\d+)\))\s*$/i;

  function parseEffectLabelParts(label) {
    let text = (label || "").trim();
    let tier = "";
    const tierMatch = text.match(ASCENSION_TIER_SUFFIX_RE);
    if (tierMatch) {
      tier = tierMatch[1];
      text = text.slice(0, tierMatch.index).trim();
    }
    return { base: text, tier: tier };
  }

  function injectTierIntoChipHtml(chipHtml, tier) {
    if (!tier || !chipHtml) {
      return chipHtml;
    }
    const closeIdx = chipHtml.lastIndexOf("</span>");
    if (closeIdx === -1) {
      return chipHtml + formatMergedTierSuffix(tier);
    }
    return (
      chipHtml.slice(0, closeIdx) +
      formatMergedTierSuffix(tier) +
      chipHtml.slice(closeIdx)
    );
  }

  function renderStandaloneEffectChip(base, tier, polarity) {
    const leading = resolveLeadingChip(base, polarity);
    if (leading.emoji) {
      return (
        '<span class="chip ' +
        leading.cls +
        '">' +
        leading.emoji +
        " " +
        escapeHtml(chipDisplayLabel(leading.text)) +
        formatMergedTierSuffix(tier) +
        escapeHtml(leading.remainder || "") +
        "</span>"
      );
    }
    const direct = tryChipify(base);
    if (direct) {
      return injectTierIntoChipHtml(direct, tier);
    }
    const ccChip = extractChipHtml(chipifyLeadingCcType(base));
    if (ccChip) {
      return injectTierIntoChipHtml(ccChip, tier);
    }
    const statChip = extractChipHtml(chipifyLeadingStat(base));
    if (statChip) {
      return injectTierIntoChipHtml(statChip, tier);
    }
    return escapeHtml(base) + formatMergedTierSuffix(tier);
  }

  function renderSummaryEffectChip(base, tier, quality) {
    if (quality) {
      const merged =
        mergeEffectWithQuality(base, quality, tier) ||
        mergeLabelWithIndicator(base, quality, tier);
      if (merged) {
        return merged;
      }
      const qMeta = qualityIndicatorMeta(
        quality,
        resolveLeadingChip(base).isCc
      );
      if (qMeta) {
        return formatMergedIndicator(
          { textOnly: base, tierSuffix: tier },
          qMeta,
          true
        );
      }
    }
    return renderStandaloneEffectChip(base, tier);
  }

  function renderEmDashLine(text) {
    const segments = splitSummarySegments(text);

    const trailingParts = [];
    let trailingQuality = null;

    function popTrailingQuality() {
      if (!segments.length) {
        return;
      }
      const raw = segments[segments.length - 1];
      const unwrapped = unwrapBackticks(raw);
      const lower = unwrapped.toLowerCase();
      if (QUALITY_CLASS[lower]) {
        trailingQuality = unwrapped;
        segments.pop();
      }
    }

    function popTrailingConditional() {
      if (!segments.length) {
        return;
      }
      const last = segments[segments.length - 1];
      if (/conditional/i.test(last)) {
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
    const parsed = parseEffectLabelParts(first);
    let firstHtml;
    if (/^Primary damage type/i.test(first)) {
      firstHtml = promoteStrongToDamageChips(renderInline(first));
    } else if (trailingQuality) {
      firstHtml = renderSummaryEffectChip(
        parsed.base,
        parsed.tier,
        trailingQuality
      );
    } else {
      firstHtml = renderSummaryEffectChip(parsed.base, parsed.tier, "");
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
        "",
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
            escapeHtml(chipDisplayLabel(key)) +
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
        escapeHtml(chipDisplayLabel(text)) +
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

  const TIER_RANK_ORDER = ["C", "B", "A", "A+", "S", "S+"];

  function isUnrankedPrydwenTier(tier) {
    const value = tier != null ? String(tier).trim() : "";
    return !value || value === "?";
  }

  function prydwenTierClass(tier) {
    if (isUnrankedPrydwenTier(tier)) {
      return "tier-unknown";
    }
    const normalized = String(tier).trim().replace(/\+/g, "-plus");
    return "tier-" + normalized.toLowerCase();
  }

  function prydwenTierDisplay(tier) {
    return isUnrankedPrydwenTier(tier) ? "?" : String(tier).trim();
  }

  function prydwenTierRank(tier) {
    if (!tier || tier === "?") {
      return -1;
    }
    const idx = TIER_RANK_ORDER.indexOf(tier);
    return idx >= 0 ? idx : -1;
  }

  function comparePrydwenTiers(repTier, mainTier) {
    const repRank = prydwenTierRank(repTier);
    const mainRank = prydwenTierRank(mainTier);
    if (mainRank < 0 && repRank < 0) {
      return "same";
    }
    if (mainRank < 0) {
      return "better";
    }
    if (repRank < 0) {
      return "worse";
    }
    if (repRank > mainRank) {
      return "better";
    }
    if (repRank < mainRank) {
      return "worse";
    }
    return "same";
  }

  function relativeTierTooltip(
    relation,
    mainHeroName,
    modeLabel,
    mainTier,
    repTier
  ) {
    const base = mainHeroName + "'s " + modeLabel + " tier";
    if (!mainTier) {
      return "No Prydwen tier listed for " + base + ".";
    }
    if (!repTier) {
      return "No Prydwen tier listed for this replacement hero.";
    }
    if (relation === "better") {
      return (
        "Better than " +
        base +
        " (" +
        mainTier +
        "). This replacement is " +
        repTier +
        "."
      );
    }
    if (relation === "worse") {
      return (
        "Worse than " +
        base +
        " (" +
        mainTier +
        "). This replacement is " +
        repTier +
        "."
      );
    }
    return "Same as " + base + " (" + mainTier + ").";
  }

  function formatTierColumnHeader(col) {
    if (col.endsWith(" tier")) {
      return (
        escapeHtml(col.slice(0, -5)) + "<br>" + escapeHtml("tier")
      );
    }
    return escapeHtml(col);
  }

  function getHeroPrydwenTiers(hero) {
    const tiers = (hero && hero.prydwenTiers) || {};
    const out = {};
    PRYDWEN_TIER_MODES.forEach(function (mode) {
      const raw = tiers[mode.key];
      out[mode.key] = isUnrankedPrydwenTier(raw) ? "?" : String(raw).trim();
    });
    return out;
  }

  function renderTierTableCell(tier) {
    const value = (tier || "").trim();
    const display = prydwenTierDisplay(value);
    return (
      '<span class="tier-chip tier-chip-table ' +
      prydwenTierClass(value) +
      '"><span class="tier-grade">' +
      escapeHtml(display) +
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

    let roleIdx = csvHeaders.indexOf("Role");
    if (roleIdx === -1) {
      roleIdx = classIdx + 1;
      csvHeaders.splice(roleIdx, 0, "Role");
      csvRows = csvRows.map(function (row) {
        const newRow = row.slice();
        newRow.splice(roleIdx, 0, "");
        return newRow;
      });
    }

    const missing = TIER_CSV_COLUMNS.filter(function (tierCol) {
      return csvHeaders.indexOf(tierCol.header) === -1;
    });
    if (missing.length) {
      const insertAt = roleIdx + 1;
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

    const roleColIdx = csvHeaders.indexOf("Role");
    csvRows.forEach(function (row) {
      const hero = heroByName[row[0] || ""];
      if (!hero) {
        return;
      }
      if (roleColIdx !== -1 && !String(row[roleColIdx] || "").trim()) {
        const roleMeta = roleCategoryMeta(hero.roleCategory);
        if (roleMeta) {
          row[roleColIdx] = roleMeta.label;
        }
      }
      const tiers = getHeroPrydwenTiers(hero);
      Object.keys(colByKey).forEach(function (key) {
        const idx = colByKey[key];
        if (!String(row[idx] || "").trim()) {
          row[idx] = tiers[key] || "?";
        }
      });
    });
  }

  function renderPrydwenTierBoxes(tiers, variant, compareTo, mainHeroName) {
    if (!tiers) {
      return "";
    }
    const compact = variant === "compact";
    const relative = compact && compareTo;
    const rowClass = compact ? "tier-box-row tier-box-row-compact" : "tier-box-row";
    const chipClass = compact ? "tier-chip tier-chip-compact" : "tier-chip";
    let html = '<div class="' + rowClass + '">';
    PRYDWEN_TIER_MODES.forEach(function (mode) {
      const rawTier = tiers[mode.key];
      const displayTier = prydwenTierDisplay(rawTier);
      let colorClass = prydwenTierClass(rawTier);
      let tipAttrs = "";
      if (relative) {
        const mainTier = compareTo[mode.key];
        const relation = comparePrydwenTiers(rawTier, mainTier);
        colorClass = "tier-rel-" + relation;
        tipAttrs = chipTipAttrs(
          relativeTierTooltip(
            relation,
            mainHeroName || "this hero",
            mode.label,
            mainTier,
            displayTier
          )
        );
      }
      html +=
        '<span class="' +
        chipClass +
        " " +
        colorClass +
        (tipAttrs ? " chip-has-tip" : "") +
        '"' +
        tipAttrs +
        ">" +
        '<span class="tier-grade">' +
        escapeHtml(displayTier) +
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

  function splitBehaviorHeading(md) {
    if (!md) {
      return { title: "", body: "" };
    }
    const lines = md.split("\n");
    if (lines[0].trim().startsWith("### ")) {
      return {
        title: lines[0].trim().slice(4).trim(),
        body: lines.slice(1).join("\n").trim(),
      };
    }
    return { title: "", body: md };
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
        const cardTitle = line.slice(5).trim();
        if (/ Requires$/i.test(cardTitle)) {
          current = null;
          return;
        }
        if (/^Buffs provided by /i.test(cardTitle)) {
          current = null;
          return;
        }
        current = { title: cardTitle, items: [] };
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

  function parseSkillCardTag(raw) {
    let tag = raw.trim();
    let targeting = "";
    const selfMatch = tag.match(/^(.+?)\s*(?:—|–)\s*Self\s*$/i);
    if (selfMatch) {
      tag = selfMatch[1].trim();
      targeting = "Self";
    }
    return { tag: tag, targeting: targeting };
  }

  function chipifySkillCardTag(raw) {
    const split = parseSkillCardTag(raw);
    let tag = split.tag;
    if (!tag) {
      return "";
    }
    const parsed = parseEffectLabelParts(tag);
    tag = parsed.base;
    const polarity = / debuff$/i.test(tag) ? "debuff" : "buff";

    if (split.targeting === "Self") {
      const merged = mergeEffectWithTargeting(
        tag,
        split.targeting,
        parsed.tier,
        polarity
      );
      if (merged) {
        return merged;
      }
    }

    const direct = tryChipify(tag);
    if (direct) {
      return injectTierIntoChipHtml(direct, parsed.tier);
    }

    const ccChip = extractChipHtml(chipifyLeadingCcType(tag));
    if (ccChip) {
      return injectTierIntoChipHtml(ccChip, parsed.tier);
    }

    const statChip = extractChipHtml(chipifyLeadingStat(tag));
    if (statChip) {
      return injectTierIntoChipHtml(statChip, parsed.tier);
    }

    const effectChip = extractChipHtml(renderStandaloneEffectChip(tag, parsed.tier));
    if (effectChip) {
      return effectChip;
    }

    const label = tag.replace(/\s*\([^)]*\)/g, "").trim();
    if (!label) {
      return "";
    }
    return injectTierIntoChipHtml(
      chipSpan("🏷️", label, "chip-generic"),
      parsed.tier
    );
  }

  const SKILL_CARD_DAMAGE_KEYS = [
    "HP loss",
    "Max HP damage",
    "Max HP-based damage",
    "True damage",
    "Physical",
    "Magic",
    "DoT",
  ];

  const SKILL_CARD_CC_KEYS = Object.keys(TAG_DEFINITIONS)
    .filter(function (key) {
      return isCcChipClass(TAG_DEFINITIONS[key].cls);
    })
    .sort(function (a, b) {
      return b.length - a.length;
    });

  function skillCardChipKey(raw) {
    let tag = raw.trim().toLowerCase();
    if (!tag) {
      return "";
    }
    tag = tag.replace(/\s*(?:—|–)\s*self\s*$/, "").trim();
    tag = tag
      .replace(
        /\s*\((?:legendary\+|mythic\+|supreme\+|ex\+\d+)\)/gi,
        ""
      )
      .trim();

    if (tag.endsWith(" debuff")) {
      return tag.replace(/\s*\([^)]*\)/g, "").trim();
    }

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
    if (tag === "hot" || tag === "healing over time" || tag.indexOf("healing over time") === 0) {
      return "hot";
    }
    if (tag === "direct healing" || tag.indexOf("direct healing") === 0) {
      return "direct healing";
    }
    if (tag.indexOf("healing") !== -1 && tag.indexOf("over time") === -1) {
      return "direct healing";
    }
    if (tag.indexOf("healing") !== -1 && tag.indexOf("over time") !== -1) {
      return "hot";
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

  function parseSkillOverviewMetricEntry(entry) {
    const match = entry.trim().match(/^(.+?)\s+`(high|average|low|slow|fast)`$/i);
    if (!match) {
      return null;
    }
    return {
      label: match[1].trim(),
      value: match[2].trim(),
    };
  }

  function formatSkillOverviewRow(labelHtml, pillsHtml) {
    if (pillsHtml) {
      return (
        '<span class="skill-overview-label">' +
        labelHtml +
        "</span>" +
        '<span class="skill-overview-pills">' +
        pillsHtml +
        "</span>"
      );
    }
    return '<span class="skill-overview-full">' + labelHtml + "</span>";
  }

  function renderDamageTypeEntry(typeName, quality) {
    const merged = mergeEffectWithQuality(typeName, quality);
    if (merged) {
      return merged;
    }
    const typeChip = tryChipify(typeName);
    const qualityChip = formatTag(quality);
    return (
      (typeChip !== null ? typeChip : escapeHtml(typeName)) +
      " " +
      qualityChip
    );
  }

  function stripSkillOverviewDamageTypesLine(md) {
    return md.replace(/\n- \*\*Damage types\*\*:[^\n]*/gi, "");
  }

  function renderSkillOverviewMetrics(md) {
    if (!md) {
      return "";
    }
    const metrics = stripSkillSummarySubsections(
      stripSkillOverviewDamageTypesLine(md)
    );
    const lines = metrics.split("\n").filter(function (line) {
      return !line.startsWith("#### ");
    });
    return renderMarkdown(lines.join("\n"), { skillOverview: true });
  }

  const SKILL_META_EMOJI = {
    Cooldown: "⏱️",
    "Initial Cooldown": "⏳",
    "Skill Range": "📏",
    "Initial Energy": "🔋",
  };

  const SKILL_META_ORDER = [
    "Cooldown",
    "Initial Cooldown",
    "Skill Range",
    "Initial Energy",
  ];

  const SKILL_CHIP_KEYS = Object.keys(TAG_DEFINITIONS).sort(function (a, b) {
    return b.length - a.length;
  });

  // Popup-only: verb/adjective inflections for single-word TAG_DEFINITIONS
  // keys (base forms are matched by SKILL_CHIP_KEYS above).
  const SKILL_DURATION_PATTERNS = [
    /\d+(?:\.\d+)?\s*\+\s*\d+(?:\.\d+)?\s*s\b/gi,
    /\d+(?:\.\d+)?\s*-\s*\d+(?:\.\d+)?\s*s\b/gi,
    /\d+(?:\.\d+)?\s*s\b/gi,
  ];

  const SKILL_INFLECTION_CHIPS = [
    { re: /\bstunn(?:ed|ing|s)\b/gi, tag: "Stun" },
    { re: /\bstun(?:s|ned|ning)\b/gi, tag: "Stun" },
    { re: /\bblind(?:ing|s|ed)\b/gi, tag: "Blind" },
    { re: /\bimmobiliz(?:e|es|ed|ing)\b/gi, tag: "Bind" },
    { re: /\bentangl(?:e|es|ed|ing)\b/gi, tag: "Bind" },
    { re: /\bimprison(?:s|ed|ing)\b/gi, tag: "Bind" },
    { re: /\bfreez(?:e|es|ing|ed)\b(?! time)(?!and defeats)/gi, tag: "Bind" },
    { re: /\bbind(?:ing|s)\b/gi, tag: "Bind" },
    { re: /(?<! of )silenc(?:e|es|ed|ing)\b/gi, tag: "Silence" },
    { re: /\bcharm(?:ed|s|ing)\b/gi, tag: "Charm" },
    { re: /\bhypnotiz(?:e|es|ed|ing)\b/gi, tag: "Sleep" },
    { re: /\basleep\b/gi, tag: "Sleep" },
    { re: /\btaunt(?:ing|s|ed)\b/gi, tag: "Taunt" },
    { re: /\bfrighten(?:ing|ed|s)\b/gi, tag: "Frighten" },
    { re: /\binterrupt(?:s|ed|ing)\b/gi, tag: "Interrupt" },
    { re: /\bshield(?:s|ed|ing)\b/gi, tag: "Shield" },
    { re: /\bheal(?:s|ed|ing)\b/gi, tag: "Healing" },
    { re: /\bcleanse(?:s|d|ing)\b/gi, tag: "Cleanse" },
    { re: /\bdispel(?:s|led|ling)\b/gi, tag: "Cleanse" },
  ];

  function enrichSkillInline(text) {
    if (!text) {
      return "";
    }
    let out = escapeHtml(text);
    out = out.replace(/\(ATK-based\)/g, "{{ATK_BASED}}");
    out = out.replace(/\(HP-based\)/g, "{{HP_BASED}}");
    SKILL_CHIP_KEYS.forEach(function (key) {
      const def = TAG_DEFINITIONS[key];
      const re = new RegExp(
        "\\b" + key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "\\b",
        "gi"
      );
      out = replaceOutsideChips(out, re, function (match) {
        return chipSpan(def.emoji, match, def.cls);
      });
    });
    SKILL_INFLECTION_CHIPS.forEach(function (entry) {
      const def = TAG_DEFINITIONS[entry.tag];
      out = replaceOutsideChips(out, entry.re, function () {
        return chipSpan(def.emoji, entry.tag, def.cls);
      });
    });
    out = out.replace(
      /\{\{ATK_BASED\}\}/g,
      '<span class="skill-inline-stat">💪 ATK</span>'
    );
    out = out.replace(
      /\{\{HP_BASED\}\}/g,
      '<span class="skill-inline-stat">❤️ HP</span>'
    );
    SKILL_DURATION_PATTERNS.forEach(function (re) {
      out = replaceOutsideChips(out, re, function (match) {
        return (
          '<span class="skill-inline-time">⏱️ ' +
          escapeHtml(match) +
          "</span>"
        );
      });
    });
    return out;
  }

  function skillDetailPhases(card) {
    const passive = (card.passive || "").trim();
    const active = (card.active || "").trim();
    if (passive || active) {
      const phases = [];
      if (passive) {
        phases.push({ label: "passive", body: passive });
      }
      if (active) {
        phases.push({ label: "active", body: active });
      }
      return phases;
    }
    const description = (card.description || card.summary || "").trim();
    if (!description) {
      return [];
    }
    return [{ label: null, body: description }];
  }

  function formatSkillDetail(card) {
    const title = card.name || card.label || "Skill";
    let headerHtml =
      '<div class="skill-popover-header">' +
      '<button type="button" class="skill-popover-close" aria-label="Close">' +
      "×</button>" +
      '<h4 id="skill-popover-title" class="skill-popover-title">' +
      escapeHtml(title) +
      "</h4>";
    if (card.unlock) {
      headerHtml +=
        '<p class="skill-popover-unlock">🔓 <em>' +
        escapeHtml(card.unlock) +
        "</em></p>";
    }

    const meta = card.meta || {};
    const metaItems = [];
    SKILL_META_ORDER.forEach(function (label) {
      if (meta[label]) {
        metaItems.push(
          '<span class="skill-popover-meta-item">' +
            SKILL_META_EMOJI[label] +
            " " +
            escapeHtml(label) +
            ": " +
            escapeHtml(meta[label]) +
            "</span>"
        );
      }
    });
    if (metaItems.length) {
      headerHtml +=
        '<div class="skill-popover-meta">' + metaItems.join("") + "</div>";
    }

    headerHtml += "</div>";

    let scrollHtml = '<div class="skill-popover-scroll">';

    const description = card.description || card.summary || "";
    const phases = skillDetailPhases(card);
    if (phases.length) {
      scrollHtml += '<div class="skill-popover-body">';
      phases.forEach(function (phase) {
        if (phase.label === "passive") {
          scrollHtml +=
            '<p class="skill-popover-phase">' +
            '<span class="skill-popover-phase-label">📖 <strong>Passive</strong></span> ' +
            enrichSkillInline(phase.body) +
            "</p>";
        } else if (phase.label === "active") {
          scrollHtml +=
            '<p class="skill-popover-phase">' +
            '<span class="skill-popover-phase-label">⚡ <strong>Active</strong></span> ' +
            enrichSkillInline(phase.body) +
            "</p>";
        } else {
          scrollHtml +=
            '<p class="skill-popover-phase">' +
            enrichSkillInline(phase.body) +
            "</p>";
        }
      });
      scrollHtml += "</div>";
    }

    const levels = card.levels || [];
    if (levels.length) {
      scrollHtml += '<ul class="skill-popover-levels">';
      levels.forEach(function (level) {
        const levelLabel = level.unlock
          ? "Level " + level.level + " — " + level.unlock
          : "Level " + level.level;
        scrollHtml +=
          "<li><span class=\"skill-popover-level-label\">🔼 " +
          escapeHtml(levelLabel) +
          ":</span> " +
          enrichSkillInline(level.text || "") +
          "</li>";
      });
      scrollHtml += "</ul>";
    }

    scrollHtml += "</div>";
    return headerHtml + scrollHtml;
  }

  function skillCardData(category) {
    if (!detailHero || !detailHero.sections || !detailHero.sections.skillCards) {
      return null;
    }
    const cards = detailHero.sections.skillCards;
    for (let i = 0; i < cards.length; i++) {
      if (cards[i].category === category) {
        return cards[i];
      }
    }
    return null;
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
        '" role="button" tabindex="0" aria-expanded="false" ' +
        'aria-haspopup="dialog">';
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

  const BENEFIT_MAX_STARS = 5;
  const BENEFIT_MIN_STARS = 1;
  const BENEFIT_STAR = "⭐";

  function formatBeneficiaryRatingDisplay(scoreRating) {
    const rating = Number(scoreRating);
    if (!isFinite(rating)) {
      return "";
    }
    const clamped = Math.max(
      BENEFIT_MIN_STARS,
      Math.min(BENEFIT_MAX_STARS, rating)
    );
    const fullStars = Math.max(
      BENEFIT_MIN_STARS,
      Math.min(BENEFIT_MAX_STARS, Math.floor(clamped))
    );
    return BENEFIT_STAR.repeat(fullStars) + " (" + clamped.toFixed(1) + ")";
  }

  function renderBeneficiaryScore(scoreRating, scoreDisplay) {
    const text = scoreDisplay || formatBeneficiaryRatingDisplay(scoreRating);
    if (!text) {
      return "";
    }
    return (
      '<div class="hero-compact-score" title="Benefit rating out of 5">' +
      escapeHtml(text) +
      "</div>"
    );
  }

  function renderHeroCompactCard(slug, name, bodyHtml, footerHtml) {
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
      (footerHtml || "") +
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

  function renderDamageTypesOverviewLine(text) {
    const match = text.match(/^\*\*Damage types\*\*:\s*(.+)$/i);
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
      const parsed = parseSkillOverviewMetricEntry(entry);
      if (!parsed) {
        return renderInline(entry);
      }
      return renderDamageTypeEntry(parsed.label, parsed.value);
    });
    return formatSkillOverviewRow(
      "<strong>Damage types</strong>",
      rendered.join("")
    );
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
    let pillsHtml;
    if (hero && hero.signatureSkill) {
      pillsHtml =
        '<a href="#" class="signature-skill-link" data-skill-category="' +
        escapeHtml(hero.signatureSkill.category) +
        '">' +
        escapeHtml(body) +
        "</a>";
    } else {
      pillsHtml = escapeHtml(body);
    }
    return formatSkillOverviewRow("<strong>Signature skill</strong>", pillsHtml);
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
    return formatSkillOverviewRow(
      "<strong>Movement</strong>",
      (chip !== null ? chip : escapeHtml(base)) + suffix
    );
  }

  function renderBehaviorTagsLine(text) {
    const match = text.match(/^\*\*Behavior tags\*\*:\s*(.+)$/i);
    if (!match) {
      return null;
    }
    const tags = match[1].match(/`([^`]+)`/g);
    if (!tags || !tags.length) {
      return null;
    }
    const chips = tags
      .map(function (raw) {
        return behaviorTagChip(raw.slice(1, -1));
      })
      .join(" ");
    return formatSkillOverviewRow(
      "<strong>Behavior tags</strong>",
      '<span class="behavior-tags-cell">' + chips + "</span>"
    );
  }

  function renderSkillOverviewMetric(text) {
    const trimmed = text.trim();
    const parsed = parseSkillOverviewMetricEntry(trimmed);
    if (!parsed) {
      return renderInline(trimmed);
    }
    const labelParts = parseEffectLabelParts(parsed.label);
    if (isSpeedMetricLabel(labelParts.base)) {
      return (
        mergeLabelWithIndicator(
          labelParts.base,
          parsed.value,
          labelParts.tier
        ) || renderSummaryEffectChip(labelParts.base, labelParts.tier, parsed.value)
      );
    }
    return (
      mergeEffectWithQuality(
        labelParts.base,
        parsed.value,
        labelParts.tier
      ) ||
      mergeLabelWithIndicator(
        labelParts.base,
        parsed.value,
        labelParts.tier
      ) ||
      renderSummaryEffectChip(labelParts.base, labelParts.tier, parsed.value)
    );
  }

  function renderSkillOverviewItem(text) {
    if (renderDamageTypesOverviewLine(text) !== null) {
      return "";
    }

    const colonMatch = text.match(/^(.+?:\s*)(.+)$/);
    if (colonMatch) {
      const segments = colonMatch[2]
        .trim()
        .split(/\s*,\s*/)
        .filter(Boolean);
      const allMetrics =
        segments.length > 0 &&
        segments.every(function (segment) {
          return parseSkillOverviewMetricEntry(segment.trim()) !== null;
        });
      if (allMetrics) {
        const pills = segments.map(function (segment) {
          return renderSkillOverviewMetric(segment);
        });
        return formatSkillOverviewRow(
          renderInline(colonMatch[1].trim().replace(/:\s*$/, "")),
          pills.join("")
        );
      }
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
    const behaviorTags = renderBehaviorTagsLine(text);
    if (behaviorTags !== null) {
      return behaviorTags;
    }
    const damageTypes = renderDamageTypesOverviewLine(text);
    if (damageTypes !== null) {
      return damageTypes;
    }
    const colonMatch = text.match(/^\*\*(.+?)\*\*:\s*(.+)$/);
    if (colonMatch) {
      const label = colonMatch[1].trim();
      return formatSkillOverviewRow(
        "<strong>" + escapeHtml(label) + "</strong>",
        renderInline(colonMatch[2].trim())
      );
    }
    return renderInline(text);
  }

  function renderMarkdown(md, options) {
    if (!md) return "";
    const skillOverview = options && options.skillOverview;
    const behaviorSection = options && options.behaviorSection;
    const overviewList = skillOverview || behaviorSection;
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
          parts.push(
            overviewList ? '<ul class="skill-overview-list">' : "<ul>"
          );
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

  const ROLE_CATEGORY_META = {
    damage_dealer: {
      label: "Damage dealer",
      emoji: "⚔️",
      className: "badge-role-damage-dealer",
    },
    specialist: {
      label: "Specialist",
      emoji: "🎭",
      className: "badge-role-specialist",
    },
    support: {
      label: "Support",
      emoji: "🤝",
      className: "badge-role-support",
    },
    tank: {
      label: "Tank",
      emoji: "🛡️",
      className: "badge-role-tank",
    },
  };

  const ROLE_FILTER_ORDER = [
    "damage_dealer",
    "specialist",
    "support",
    "tank",
  ];

  function roleCategoryMeta(roleCategory) {
    return ROLE_CATEGORY_META[roleCategory] || null;
  }

  function renderRoleCategoryBadge(heroOrCategory) {
    const key =
      typeof heroOrCategory === "string"
        ? heroOrCategory
        : heroOrCategory.roleCategory;
    const meta = roleCategoryMeta(key);
    if (!meta) {
      return "";
    }
    return (
      '<span class="badge ' +
      meta.className +
      '"><span class="badge-emoji" aria-hidden="true">' +
      meta.emoji +
      "</span>" +
      escapeHtml(meta.label) +
      "</span>"
    );
  }

  function renderBadges(hero, options) {
    const includeRoleCategory =
      options && options.includeRoleCategory === true;
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
    if (includeRoleCategory) {
      const roleBadge = renderRoleCategoryBadge(hero);
      if (roleBadge) {
        badges.push(roleBadge);
      }
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
        (h.class || "").toLowerCase().indexOf(token) !== -1 ||
        (roleCategoryMeta(h.roleCategory) || { label: "" }).label
          .toLowerCase()
          .indexOf(token) !== -1
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
      if (activeRole && h.roleCategory !== activeRole) {
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

  const DMG_COLUMN_BASE = {
    Magic: "Magic",
    Physical: "Physical",
    Ranged: "Ranged",
    True: "True damage",
    "HP Loss": "HP loss",
    "Max HP": "Max HP damage",
  };

  function parseDebuffEffectLabel(label) {
    let text = (label || "").trim();
    let tier = "";
    const tierMatch = text.match(ASCENSION_TIER_SUFFIX_RE);
    if (tierMatch) {
      tier = tierMatch[1];
      text = text.slice(0, tierMatch.index).trim();
    }
    text = text.replace(/\s+debuff\s*$/i, "").trim();
    if (!text) {
      text = (label || "").trim();
    }
    return { base: text, tier: tier };
  }

  function parseEffectColumnLabel(column) {
    if (column.endsWith(" DMG")) {
      const short = column.slice(0, -4);
      return {
        base: DMG_COLUMN_BASE[short] || short,
        polarity: "damage",
        tier: "",
      };
    }
    if (column.endsWith(" buff")) {
      const parsed = parseBuffEffectLabel(column);
      return {
        base: parsed.base,
        polarity: "buff",
        tier: parsed.tier,
      };
    }
    if (column.endsWith(" debuff")) {
      const parsed = parseDebuffEffectLabel(column);
      return {
        base: parsed.base,
        polarity: "debuff",
        tier: parsed.tier,
      };
    }
    const parsed = parseEffectLabelParts(column);
    return {
      base: parsed.base,
      polarity: null,
      tier: parsed.tier,
    };
  }

  function isTimingSegment(segment) {
    const lower = segment.trim().toLowerCase();
    if (Object.prototype.hasOwnProperty.call(TIMING_RANK, lower)) {
      return true;
    }
    if (lower.indexOf("start of battle") !== -1) {
      return true;
    }
    if (lower.indexOf("on ultimate") !== -1) {
      return true;
    }
    if (lower.indexOf("on skill") !== -1) {
      return true;
    }
    if (lower.indexOf("permanent") !== -1) {
      return true;
    }
    return false;
  }

  function parseEffectCellPart(text) {
    const segments = splitSummarySegments(text);
    let quality = "";
    let conditional = "";
    let timing = "";

    function popTrailingQuality() {
      if (!segments.length) {
        return;
      }
      const last = unwrapBackticks(segments[segments.length - 1]);
      const lower = last.toLowerCase();
      if (QUALITY_CLASS[lower]) {
        quality = last;
        segments.pop();
      }
    }

    function popTrailingConditional() {
      if (!segments.length) {
        return;
      }
      const last = segments[segments.length - 1];
      if (/conditional/i.test(last)) {
        conditional = last;
        segments.pop();
      }
    }

    function popTrailingTiming() {
      if (!segments.length) {
        return;
      }
      const last = segments[segments.length - 1];
      if (isTimingSegment(last)) {
        timing = last;
        segments.pop();
      }
    }

    popTrailingConditional();
    popTrailingQuality();
    popTrailingConditional();
    popTrailingTiming();

    const targeting = segments.join(" — ");
    return {
      targeting: targeting,
      quality: quality,
      conditional: conditional,
      timing: timing,
    };
  }

  function renderEffectConditionalChip(conditionalText) {
    if (!conditionalText) {
      return "";
    }
    const condMatch = conditionalText.match(/conditional\s*\(([^)]+)\)/i);
    if (condMatch) {
      return "";
    }
    return (
      ' <span class="chip chip-generic chip-has-tip"' +
      chipTipAttrs(conditionalTooltip(conditionalText)) +
      ">🎲 " +
      escapeHtml(conditionalText) +
      "</span>"
    );
  }

  function renderEffectCellPart(column, text) {
    if (!text || !text.trim()) {
      return "";
    }
    const colMeta = parseEffectColumnLabel(column);
    const parsed = parseEffectCellPart(text.trim());
    let conditionalParam = "";
    if (parsed.conditional) {
      const condMatch = parsed.conditional.match(/conditional\s*\(([^)]+)\)/i);
      if (condMatch) {
        conditionalParam = condMatch[1].trim();
      }
    }

    let html = renderMergedEffectPill(
      colMeta.base,
      parsed.quality,
      colMeta.tier || "",
      conditionalParam,
      colMeta.polarity
    );
    if (parsed.targeting) {
      html += " " + renderBuffTargetingChip(parsed.targeting);
    }
    if (parsed.timing) {
      const timingChip = tryChipify(parsed.timing);
      html += " " + (timingChip !== null ? timingChip : formatTag(parsed.timing));
    }
    html += renderEffectConditionalChip(parsed.conditional);
    return html;
  }

  function getListCellRawValue(row, colIdx, col) {
    let cellValue = row[colIdx] || "";
    const hero = heroByName[row[0] || ""];
    if (col === "Role" && !String(cellValue || "").trim() && hero) {
      const roleMeta = roleCategoryMeta(hero.roleCategory);
      if (roleMeta) {
        cellValue = roleMeta.label;
      }
    }
      if (hero && TIER_CSV_HEADERS[col] && !String(cellValue || "").trim()) {
        const tierCol = TIER_CSV_COLUMNS.find(function (t) {
          return t.header === col;
        });
        if (tierCol) {
          cellValue = getHeroPrydwenTiers(hero)[tierCol.key] || "?";
        }
      }
    return String(cellValue || "").trim();
  }

  function classifyFilterAtom(value) {
    const trimmed = (value || "").trim();
    if (!trimmed) {
      return "other";
    }
    const lower = trimmed.toLowerCase();
    if (QUALITY_CLASS[lower]) {
      return "quality";
    }
    if (/conditional/i.test(trimmed)) {
      return "conditional";
    }
    if (TARGETING_DEFINITIONS[lower]) {
      return "targeting";
    }
    if (isTimingSegment(trimmed)) {
      return "timing";
    }
    return "other";
  }

  const FILTER_GROUP_META = [
    { id: "targeting", label: "Targeting" },
    { id: "quality", label: "Magnitude" },
    { id: "timing", label: "Timing" },
    { id: "conditional", label: "Conditional" },
    { id: "other", label: "Other" },
  ];

  function splitSelectedByFilterGroup(selected) {
    const groups = {};
    selected.forEach(function (value) {
      const kind = classifyFilterAtom(value);
      if (!groups[kind]) {
        groups[kind] = new Set();
      }
      groups[kind].add(value);
    });
    return groups;
  }

  function atomSetMatchesGroupedSelection(atomSet, selectedByGroup) {
    const normalized = {};
    atomSet.forEach(function (atom) {
      normalized[atom.toLowerCase()] = atom;
    });
    return FILTER_GROUP_META.every(function (meta) {
      const groupSelected = selectedByGroup[meta.id];
      if (!groupSelected || !groupSelected.size) {
        return true;
      }
      let groupMatched = false;
      groupSelected.forEach(function (value) {
        if (normalized[value.toLowerCase()]) {
          groupMatched = true;
        }
      });
      return groupMatched;
    });
  }

  function sortFilterOptionValues(values) {
    return values.slice().sort(function (a, b) {
      return a.toLowerCase().localeCompare(b.toLowerCase());
    });
  }

  function buildEffectColumnFilterGroups(col, idx) {
    const byGroup = {};
    csvRows.forEach(function (row) {
      extractCellFilterAtoms(col, getListCellRawValue(row, idx, col)).forEach(
        function (v) {
          const kind = classifyFilterAtom(v);
          if (!byGroup[kind]) {
            byGroup[kind] = new Set();
          }
          byGroup[kind].add(v);
        }
      );
    });
    return FILTER_GROUP_META.map(function (meta) {
      const values = byGroup[meta.id];
      return {
        id: meta.id,
        label: meta.label,
        values: values ? sortFilterOptionValues(Array.from(values)) : [],
      };
    }).filter(function (group) {
      return group.values.length;
    });
  }

  function filterOptionGroupsHasChoices(groups) {
    return groups.some(function (group) {
      return group.values.length;
    });
  }

  function atomsFromEffectEntry(entry) {
    const atoms = new Set();
    const trimmed = entry.trim();
    if (!trimmed) {
      return atoms;
    }
    const parsed = parseEffectCellPart(trimmed);
    if (parsed.targeting) {
      parsed.targeting.split(/\s*,\s*/).forEach(function (token) {
        const t = token.trim();
        if (t) {
          atoms.add(t);
        }
      });
    }
    if (parsed.quality) {
      atoms.add(parsed.quality);
    }
    if (parsed.conditional) {
      atoms.add(parsed.conditional);
    }
    if (parsed.timing) {
      atoms.add(parsed.timing);
    }
    return atoms;
  }

  function renderBehaviorTagsCell(value) {
    const parts = String(value || "")
      .split(/\s*;\s*/)
      .filter(function (part) {
        return part.trim();
      });
    if (!parts.length) {
      return "";
    }
    return (
      '<span class="behavior-tags-cell">' +
      parts
        .map(function (tag) {
          return behaviorTagChip(tag);
        })
        .join(" ") +
      "</span>"
    );
  }

  function extractCellFilterAtoms(column, cellValue) {
    const values = new Set();
    const raw = String(cellValue || "").trim();
    if (!raw) {
      return values;
    }
    if (column === "Behavior tags") {
      raw.split(/\s*;\s*/).forEach(function (tag) {
        const trimmed = tag.trim();
        if (trimmed) {
          values.add(trimmed);
        }
      });
      return values;
    }
    if (isEffectSortColumn(column)) {
      raw.split(/\s*;\s*/).forEach(function (entry) {
        atomsFromEffectEntry(entry).forEach(function (atom) {
          values.add(atom);
        });
      });
      return values;
    }
    values.add(raw);
    return values;
  }

  function effectEntryAtomSets(cellValue) {
    const raw = String(cellValue || "").trim();
    if (!raw) {
      return [];
    }
    return raw.split(/\s*;\s*/).map(function (entry) {
      return atomsFromEffectEntry(entry);
    });
  }

  function buildColumnFilterOptions() {
    if (!csvHeaders.length) {
      csvColumnFilterOptions = [];
      return;
    }
    csvColumnFilterOptions = csvHeaders.map(function (col, idx) {
      if (col === "Name") {
        return [];
      }
      if (isEffectSortColumn(col)) {
        return buildEffectColumnFilterGroups(col, idx);
      }
      const values = new Set();
      csvRows.forEach(function (row) {
        extractCellFilterAtoms(col, getListCellRawValue(row, idx, col)).forEach(
          function (v) {
            values.add(v);
          }
        );
      });
      return [
        {
          id: "value",
          label: "",
          values: sortFilterOptionValues(Array.from(values)),
        },
      ];
    });
  }

  function cellMatchesColumnFilter(column, cellValue, selected) {
    if (!selected || !selected.size) {
      return true;
    }
    const raw = String(cellValue || "").trim();
    if (!raw) {
      return false;
    }
    if (isEffectSortColumn(column)) {
      const selectedByGroup = splitSelectedByFilterGroup(selected);
      const entrySets = effectEntryAtomSets(raw);
      return entrySets.some(function (atomSet) {
        return atomSetMatchesGroupedSelection(atomSet, selectedByGroup);
      });
    }
    const atoms = extractCellFilterAtoms(column, cellValue);
    let matched = false;
    selected.forEach(function (value) {
      if (atoms.has(value)) {
        matched = true;
      }
    });
    return matched;
  }

  function rowMatchesColumnFilters(row) {
    for (let colIdx = 0; colIdx < csvHeaders.length; colIdx++) {
      const selected = csvColumnFilters[colIdx];
      if (!selected || !selected.size) {
        continue;
      }
      const col = csvHeaders[colIdx];
      if (col === "Name") {
        continue;
      }
      const cellValue = getListCellRawValue(row, colIdx, col);
      if (!cellMatchesColumnFilter(col, cellValue, selected)) {
        return false;
      }
    }
    return true;
  }

  const FILTER_QUALITY_EMOJI = {
    high: "⬆️",
    average: "➡️",
    low: "⬇️",
  };

  function filterOptionIconHtml(column, value) {
    const trimmed = (value || "").trim();
    if (!trimmed) {
      return "";
    }
    const lower = trimmed.toLowerCase();

    if (column === "Faction") {
      const icon = iconPath("factions", trimmed);
      if (icon) {
        return (
          '<img class="col-filter-option-img" src="' +
          assetUrl(icon) +
          '" alt="" loading="lazy">'
        );
      }
    }
    if (column === "Class") {
      const icon = iconPath("class", trimmed);
      if (icon) {
        return (
          '<img class="col-filter-option-img" src="' +
          assetUrl(icon) +
          '" alt="" loading="lazy">'
        );
      }
    }
    if (column === "Role") {
      const roleKey = Object.keys(ROLE_CATEGORY_META).find(function (key) {
        return ROLE_CATEGORY_META[key].label.toLowerCase() === lower;
      });
      if (roleKey) {
        return (
          '<span class="col-filter-option-emoji" aria-hidden="true">' +
          ROLE_CATEGORY_META[roleKey].emoji +
          "</span>"
        );
      }
    }
    if (column === "Movement") {
      const moveDef = MOVEMENT_DEFINITIONS[lower];
      if (moveDef) {
        return (
          '<span class="col-filter-option-emoji" aria-hidden="true">' +
          moveDef.emoji +
          "</span>"
        );
      }
    }
    if (column === "Behavior tags") {
      const def = behaviorTagDefinition(trimmed);
      if (def) {
        return (
          '<span class="col-filter-option-emoji" aria-hidden="true">' +
          def.emoji +
          "</span>"
        );
      }
    }
    if (
      column === "Signature skill speed" ||
      column === "Non-ultimate speed"
    ) {
      if (SPEED_EMOJI[lower]) {
        return (
          '<span class="col-filter-option-emoji" aria-hidden="true">' +
          SPEED_EMOJI[lower] +
          "</span>"
        );
      }
    }
    if (
      column === "DoT" ||
      column === "HoT" ||
      column === "Summons" ||
      column === "Energy provider"
    ) {
      if (lower === "yes") {
        return (
          '<span class="col-filter-option-emoji" aria-hidden="true">✓</span>'
        );
      }
    }

    const targeting = TARGETING_DEFINITIONS[lower];
    if (targeting) {
      return (
        '<span class="col-filter-option-emoji" aria-hidden="true">' +
        targeting.emoji +
        "</span>"
      );
    }

    const exactKey = exactTagDefinitionKey(trimmed);
    if (exactKey && TAG_DEFINITIONS[exactKey]) {
      return (
        '<span class="col-filter-option-emoji" aria-hidden="true">' +
        TAG_DEFINITIONS[exactKey].emoji +
        "</span>"
      );
    }

    if (QUALITY_CLASS[lower]) {
      return (
        '<span class="col-filter-option-emoji" aria-hidden="true">' +
        (FILTER_QUALITY_EMOJI[lower] || "") +
        "</span>"
      );
    }

    if (/conditional/i.test(trimmed)) {
      return (
        '<span class="col-filter-option-emoji" aria-hidden="true">🎲</span>'
      );
    }

    if (isTimingSegment(trimmed)) {
      return (
        '<span class="col-filter-option-emoji" aria-hidden="true">⏱️</span>'
      );
    }

    return "";
  }

  function renderColumnFilterPanel(colIdx, column, optionGroups) {
    if (!filterOptionGroupsHasChoices(optionGroups)) {
      return "";
    }
    const selected = csvColumnFilters[colIdx] || new Set();
    const visibleGroups = optionGroups.filter(function (group) {
      return group.values.length;
    });
    const showGroupLabels = visibleGroups.length > 1;
    let html =
      '<div class="col-filter-panel" role="group" aria-label="Filter column">';
    visibleGroups.forEach(function (group, groupIdx) {
      if (showGroupLabels && group.label) {
        if (groupIdx > 0) {
          html += '<div class="col-filter-group-sep" role="separator"></div>';
        }
        html +=
          '<div class="col-filter-group-label">' +
          escapeHtml(group.label) +
          "</div>";
      } else if (groupIdx > 0) {
        html += '<div class="col-filter-group-sep" role="separator"></div>';
      }
      group.values.forEach(function (value) {
        const checked = selected.has(value) ? " checked" : "";
        const iconHtml = filterOptionIconHtml(column, value);
        html +=
          '<label class="col-filter-option">' +
          '<input type="checkbox" class="col-filter-cb" data-col="' +
          colIdx +
          '" data-group="' +
          escapeHtml(group.id) +
          '" value="' +
          escapeHtml(value) +
          '"' +
          checked +
          ">" +
          '<span class="col-filter-option-body">' +
          (iconHtml
            ? '<span class="col-filter-option-icon">' + iconHtml + "</span>"
            : "") +
          '<span class="col-filter-option-text">' +
          escapeHtml(value) +
          "</span>" +
          "</span></label>";
      });
    });
    if (selected.size) {
      html +=
        '<button type="button" class="col-filter-clear" data-col="' +
        colIdx +
        '">Clear</button>';
    }
    html += "</div>";
    return html;
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
    if (column === "Role") {
      const roleKey = Object.keys(ROLE_CATEGORY_META).find(function (key) {
        return (
          ROLE_CATEGORY_META[key].label.toLowerCase() ===
          String(value).trim().toLowerCase()
        );
      });
      if (roleKey) {
        return renderRoleCategoryBadge(roleKey);
      }
      return escapeHtml(value);
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
    if (column === "Behavior tags") {
      return renderBehaviorTagsCell(value);
    }
    if (TIER_CSV_HEADERS[column]) {
      return renderTierTableCell(value);
    }
    if (isEffectSortColumn(column)) {
      const parts = String(value || "")
        .split(/\s*;\s*/)
        .filter(function (part) {
          return part.trim();
        });
      if (!parts.length) {
        return "";
      }
      return (
        '<span class="effect-cell-stack">' +
        parts
          .map(function (part) {
            return (
              '<span class="effect-cell-entry">' +
              renderEffectCellPart(column, part) +
              "</span>"
            );
          })
          .join("") +
        "</span>"
      );
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

  const EFFECT_CC_COLUMNS = [
    "Stun",
    "Knock down",
    "Knock up",
    "Knock back",
    "Frighten",
    "Silence",
    "Charm",
    "Sleep",
    "Displace",
    "Bind",
    "Interrupt",
    "Taunt",
    "Blind",
  ];

  const EFFECT_ANTI_CC_COLUMNS = [
    "Unaffected",
    "Steadfast",
    "Immune",
    "Untargetable",
    "Cleanse",
  ];

  const TARGETING_RANK = {
    "all units": 70,
    global: 65,
    area: 60,
    arc: 50,
    "multiple targets": 40,
    allies: 35,
    enemies: 35,
    "single target": 30,
    self: 20,
  };

  const TIMING_RANK = {
    permanent: 50,
    "start of battle": 40,
    form: 35,
    "on ultimate": 30,
    "on skill": 25,
    once: 20,
    "conditional (frequent)": 15,
    conditional: 10,
    "conditional (rare)": 5,
  };

  const STRENGTH_RANK = {
    high: 3,
    average: 2,
    low: 1,
  };

  function isDmgColumn(column) {
    return !!column && column.endsWith(" DMG");
  }

  function isEffectSortColumn(column) {
    if (!column) {
      return false;
    }
    if (isDmgColumn(column)) {
      return true;
    }
    if (column === "Healing" || column === "Shields") {
      return true;
    }
    if (column.endsWith(" buff") || column.endsWith(" debuff")) {
      return true;
    }
    if (EFFECT_CC_COLUMNS.indexOf(column) !== -1) {
      return true;
    }
    if (EFFECT_ANTI_CC_COLUMNS.indexOf(column) !== -1) {
      return true;
    }
    return false;
  }

  function targetingRank(text) {
    const trimmed = text.trim();
    if (!trimmed) {
      return 0;
    }
    const lower = trimmed.toLowerCase();
    if (Object.prototype.hasOwnProperty.call(TARGETING_RANK, lower)) {
      return TARGETING_RANK[lower];
    }
    if (trimmed.indexOf(",") !== -1) {
      return trimmed.split(/\s*,\s*/).reduce(function (max, part) {
        return Math.max(max, targetingRank(part));
      }, 0);
    }
    return 0;
  }

  function timingRank(text) {
    const lower = text.trim().toLowerCase();
    if (Object.prototype.hasOwnProperty.call(TIMING_RANK, lower)) {
      return TIMING_RANK[lower];
    }
    if (lower.indexOf("conditional (frequent)") !== -1) {
      return TIMING_RANK["conditional (frequent)"];
    }
    if (lower.indexOf("conditional (rare)") !== -1) {
      return TIMING_RANK["conditional (rare)"];
    }
    if (lower.indexOf("start of battle") !== -1) {
      return TIMING_RANK["start of battle"];
    }
    if (lower.indexOf("on ultimate") !== -1) {
      return TIMING_RANK["on ultimate"];
    }
    if (lower.indexOf("on skill") !== -1) {
      return TIMING_RANK["on skill"];
    }
    if (lower.indexOf("permanent") !== -1) {
      return TIMING_RANK.permanent;
    }
    return 0;
  }

  function parseEffectEntry(entry) {
    const trimmed = entry.trim();
    if (!trimmed) {
      return null;
    }
    const parts = trimmed.split(/\s*—\s*/);
    if (parts.length === 1) {
      return {
        targeting: targetingRank(parts[0]),
        strength: 0,
        timing: 0,
      };
    }
    let strength = 0;
    let timing = 0;
    for (let i = 1; i < parts.length; i++) {
      const token = parts[i].trim().toLowerCase();
      if (Object.prototype.hasOwnProperty.call(STRENGTH_RANK, token)) {
        strength = Math.max(strength, STRENGTH_RANK[token]);
      } else {
        timing = Math.max(timing, timingRank(parts[i]));
      }
    }
    return {
      targeting: targetingRank(parts[0]),
      strength: strength,
      timing: timing,
    };
  }

  function effectSortKey(cellValue) {
    if (!cellValue || !cellValue.trim()) {
      return [-1, -1, -1];
    }
    const entries = cellValue.split(/\s*;\s*/);
    let best = [-1, -1, -1];
    entries.forEach(function (entry) {
      const parsed = parseEffectEntry(entry);
      if (!parsed) {
        return;
      }
      const key = [parsed.targeting, parsed.strength, parsed.timing];
      if (compareEffectSortKeys(key, best) > 0) {
        best = key;
      }
    });
    return best;
  }

  function compareEffectSortKeys(ka, kb) {
    for (let i = 0; i < 3; i++) {
      if (ka[i] !== kb[i]) {
        return ka[i] - kb[i];
      }
    }
    return 0;
  }

  function compareEffectCells(av, bv) {
    if (!av && !bv) {
      return 0;
    }
    if (!av) {
      return 1;
    }
    if (!bv) {
      return -1;
    }
    const cmp = compareEffectSortKeys(effectSortKey(av), effectSortKey(bv));
    if (cmp !== 0) {
      return cmp * sortDir;
    }
    return 0;
  }

  function compareCsvRows(a, b) {
    const col = csvHeaders[sortColumn];
    const av = (a[sortColumn] || "").trim();
    const bv = (b[sortColumn] || "").trim();
    if (isEffectSortColumn(col)) {
      return compareEffectCells(av, bv);
    }
    const avLower = av.toLowerCase();
    const bvLower = bv.toLowerCase();
    if (!avLower && !bvLower) {
      return 0;
    }
    if (!avLower) {
      return 1;
    }
    if (!bvLower) {
      return -1;
    }
    if (avLower < bvLower) {
      return -sortDir;
    }
    if (avLower > bvLower) {
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
      return allowed[row[0]] && rowMatchesColumnFilters(row);
    });
    rows = rows.slice().sort(compareCsvRows);

    let labelRowHtml = '<tr class="heroes-table-label-row">';
    let filterRowHtml = '<tr class="heroes-table-filter-row">';
    csvHeaders.forEach(function (col, idx) {
      let cls = "sortable";
      if (col === "Name") {
        cls += " col-name";
      }
      if (TIER_CSV_HEADERS[col]) {
        cls += " col-tier";
      }
      if (col === "Role") {
        cls += " col-role";
      }
      if (col === "Behavior tags") {
        cls += " col-behavior-tags";
      }
      if (isEffectSortColumn(col)) {
        cls += " col-effect-stack";
      }
      const optionGroups = csvColumnFilterOptions[idx] || [];
      const activeCount =
        csvColumnFilters[idx] && csvColumnFilters[idx].size
          ? csvColumnFilters[idx].size
          : 0;
      const hasFilter = activeCount > 0;
      const filterCls =
        "col-filter" +
        (hasFilter ? " is-active" : "") +
        (filterOptionGroupsHasChoices(optionGroups) ? "" : " is-empty");
      const label =
        TIER_CSV_HEADERS[col] ? formatTierColumnHeader(col) : escapeHtml(col);
      let sortCls = "th-sort-btn";
      if (idx === sortColumn) {
        sortCls += sortDir === 1 ? " sort-asc" : " sort-desc";
      }
      const showFilter = col !== "Name" && filterOptionGroupsHasChoices(optionGroups);
      const nameRowSpan = col === "Name" ? ' rowspan="2"' : "";
      labelRowHtml +=
        "<th" +
        nameRowSpan +
        ' class="' +
        cls +
        '" data-col="' +
        idx +
        '">' +
        '<button type="button" class="' +
        sortCls +
        '" data-col="' +
        idx +
        '">' +
        label +
        "</button></th>";
      if (col === "Name") {
        return;
      }
      let filterCellCls = "col-filter-cell";
      if (TIER_CSV_HEADERS[col]) {
        filterCellCls += " col-tier";
      }
      if (col === "Role") {
        filterCellCls += " col-role";
      }
      if (isEffectSortColumn(col)) {
        filterCellCls += " col-effect-stack";
      }
      filterRowHtml +=
        '<th class="' +
        filterCellCls +
        '" data-col="' +
        idx +
        '">';
      if (showFilter) {
        const countHtml = hasFilter
          ? '<span class="col-filter-count">(' + activeCount + ")</span>"
          : "";
        filterRowHtml +=
          '<details class="' +
          filterCls +
          '" data-col="' +
          idx +
          '"' +
          (openColumnFilter === idx ? " open" : "") +
          ">" +
          '<summary class="col-filter-trigger" title="Filter column">' +
          '<span class="col-filter-field-label">' +
          '<span class="col-filter-status-dot" aria-hidden="true"></span>' +
          '<span class="col-filter-label-text">filter</span>' +
          countHtml +
          "</span>" +
          '<span class="col-filter-sep" aria-hidden="true"></span>' +
          '<span class="col-filter-caret" aria-hidden="true"></span>' +
          "</summary>" +
          renderColumnFilterPanel(idx, col, optionGroups) +
          "</details>";
      }
      filterRowHtml += "</th>";
    });
    labelRowHtml += "</tr>";
    filterRowHtml += "</tr>";
    heroesTableHead.innerHTML = labelRowHtml + filterRowHtml;
    updateTableHeadStickyOffsets();
    requestAnimationFrame(positionOpenColumnFilter);

    const allRows = csvRows.filter(function (row) {
      return allowed[row[0]];
    });

    if (!columnWidthsLocked && allRows.length) {
      heroesTableBody.innerHTML = buildListBodyHtml(allRows);
      listEmptyState.classList.toggle("hidden", rows.length > 0);
      requestAnimationFrame(function () {
        measureColumnWidths();
        columnWidthsLocked = csvColumnWidths.length > 0;
        updateTableColgroup();
        heroesTableBody.innerHTML = buildListBodyHtml(rows);
        listEmptyState.classList.toggle("hidden", rows.length > 0);
      });
      return;
    }

    heroesTableBody.innerHTML = buildListBodyHtml(rows);
    updateTableColgroup();
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
    closeSkillCardPopover();
    detailHero = null;
    detailView.classList.add("hidden");
    gridView.classList.toggle("hidden", viewMode !== "grid");
    listView.classList.toggle("hidden", viewMode !== "list");
    updateHeaderNav(false);
    renderCurrentView();
  }

  const SYNERGY_TARGETING_TOKENS = {
    "single target": true,
    "multiple targets": true,
    "all units": true,
    area: true,
    arc: true,
    global: true,
    self: true,
    allies: true,
    enemies: true,
    "on skill": true,
    "summons only": true,
  };

  const SYNERGY_QUALITY_TOKENS = {
    low: true,
    average: true,
    high: true,
  };

  function splitSynergyReasonDetail(text) {
    const match = text.match(/^(.+?)\s*\((.+)\)\s*$/);
    if (!match) {
      return {
        label: text.trim(),
        quality: "",
        conditional: "",
        modifiers: [],
      };
    }
    let label = match[1].trim();
    let inner = match[2].trim();
    let conditional = "";
    const condMatch = inner.match(/(?:,\s*)?conditional\s*\(([^)]+)\)\s*$/i);
    if (condMatch) {
      conditional = condMatch[1].trim();
      inner = inner.slice(0, condMatch.index).replace(/,\s*$/, "").trim();
    }
    let quality = "";
    const modifiers = [];
    inner.split(/\s*,\s*/).forEach(function (part) {
      const trimmed = part.trim();
      if (!trimmed) {
        return;
      }
      const lower = trimmed.toLowerCase();
      if (SYNERGY_QUALITY_TOKENS[lower]) {
        quality = lower;
        return;
      }
      if (SYNERGY_TARGETING_TOKENS[lower]) {
        return;
      }
      modifiers.push(trimmed);
    });
    return { label: label, quality: quality, conditional: conditional, modifiers: modifiers };
  }

  function stripSynergyReasonTargeting(text) {
    const detail = splitSynergyReasonDetail(text);
    const kept = detail.modifiers.slice();
    if (detail.quality) {
      kept.push(detail.quality);
    }
    if (detail.conditional) {
      kept.push("conditional (" + detail.conditional + ")");
    }
    if (!kept.length) {
      return detail.label;
    }
    return detail.label + " (" + kept.join(", ") + ")";
  }

  function parseSynergyReason(reason) {
    let text = normalizeSummaryText(reason);
    let signatureFuel = false;
    if (/`signature fuel`\s*$/i.test(text)) {
      signatureFuel = true;
      text = text.replace(/`signature fuel`\s*$/i, "").trim();
    }

    if (/^Enables /i.test(text) || /^Grants /i.test(text)) {
      return {
        type: "enable",
        text: stripSynergyReasonTargeting(text),
      };
    }

    const viaIdx = text.toLowerCase().indexOf(" via ");
    if (viaIdx !== -1) {
      text = text.slice(viaIdx + 5).trim();
    }

    const detail = splitSynergyReasonDetail(text);
    const parsed = parseBuffEffectLabel(detail.label);
    return {
      type: "effect",
      base: parsed.base,
      tier: parsed.tier,
      quality: detail.quality,
      conditional: detail.conditional,
      signatureFuel: signatureFuel,
    };
  }

  function synergyReasonKey(parsed) {
    return [
      parsed.base,
      parsed.tier,
      parsed.quality,
      parsed.conditional,
      parsed.signatureFuel ? "1" : "0",
    ].join("|");
  }

  function chipifySynergyEnableLabel(text) {
    const direct = tryChipify(text);
    if (direct) {
      return direct;
    }
    return escapeHtml(text);
  }

  function chipifySynergyEnableDetail(text) {
    const detail = splitSynergyReasonDetail(text);
    const parsed = parseBuffEffectLabel(detail.label);
    const parts = parsed.base.split(/\s+\+\s+/);

    function renderPart(part, applyQuality) {
      const partParsed = parseBuffEffectLabel(part.trim());
      return renderMergedEffectPill(
        partParsed.base,
        applyQuality ? detail.quality : "",
        applyQuality ? parsed.tier || partParsed.tier : partParsed.tier,
        applyQuality ? detail.conditional : ""
      );
    }

    if (parts.length === 1) {
      return renderPart(parts[0], true);
    }

    return parts
      .map(function (part, idx) {
        const applyQuality =
          idx === parts.length - 1 && !!detail.quality;
        return renderPart(part, applyQuality);
      })
      .join(" + ");
  }

  function renderSynergyEnableLine(text) {
    if (/^Grants /i.test(text)) {
      return escapeHtml(text);
    }
    const viaIdx = text.toLowerCase().indexOf(" via ");
    if (viaIdx === -1) {
      return chipifySynergyEnableLabel(text);
    }
    const prefix = text.slice(0, viaIdx).trim();
    const effect = text.slice(viaIdx + 5).trim();
    const enableMatch = prefix.match(/^Enables\s+(.+)$/i);
    const enableLabel = enableMatch ? enableMatch[1].trim() : prefix;
    return (
      "Enables " +
      chipifySynergyEnableLabel(enableLabel) +
      " via " +
      chipifySynergyEnableDetail(effect)
    );
  }

  function renderSynergyPartnerExplanation(reasons) {
    if (!reasons || !reasons.length) {
      return "";
    }
    const effects = [];
    const enables = [];
    const seen = Object.create(null);

    reasons.forEach(function (reason) {
      const parsed = parseSynergyReason(reason);
      if (parsed.type === "enable") {
        enables.push(parsed.text);
        return;
      }
      const key = synergyReasonKey(parsed);
      if (seen[key]) {
        return;
      }
      seen[key] = true;
      effects.push(parsed);
    });

    let html = "";
    if (effects.length) {
      html += '<div class="synergy-partner-pills">';
      effects.forEach(function (effect) {
        let pill = renderMergedEffectPill(
          effect.base,
          effect.quality,
          effect.tier,
          effect.conditional
        );
        if (effect.signatureFuel) {
          pill += " " + formatTag("signature fuel");
        }
        html += '<span class="synergy-partner-pill">' + pill + "</span>";
      });
      html += "</div>";
    }
    if (enables.length) {
      html += '<div class="synergy-partner-specials">';
      enables.forEach(function (line) {
        html +=
          '<div class="synergy-partner-special">' +
          renderSynergyEnableLine(line) +
          "</div>";
      });
      html += "</div>";
    }
    return html;
  }

  function sortSynergyHeroes(heroes) {
    return heroes.slice().sort(function (a, b) {
      const aRating =
        a.scoreRating != null ? a.scoreRating : a.score_rating;
      const bRating =
        b.scoreRating != null ? b.scoreRating : b.score_rating;
      if (bRating !== aRating) {
        return bRating - aRating;
      }
      return String(a.name || "").localeCompare(String(b.name || ""));
    });
  }

  function renderSynergyHeroCard(ref, bodyHtml) {
    const scoreHtml = renderBeneficiaryScore(
      ref.scoreRating != null ? ref.scoreRating : ref.score_rating,
      ref.scoreDisplay || ref.score_display
    );
    return renderHeroCompactCard(
      ref.slug,
      ref.name,
      scoreHtml + (bodyHtml || "")
    );
  }

  function renderSynergyHeroGrid(heroes, bodyForHero) {
    if (!heroes || !heroes.length) {
      return "";
    }
    return renderHeroRowList(
      sortSynergyHeroes(heroes).map(function (hero) {
        return renderSynergyHeroCard(hero, bodyForHero(hero));
      }),
      "hero-compact-grid-2"
    );
  }

  function renderInlineHeroPortrait(slug, name) {
    const hero = heroBySlug[slug];
    const portrait = hero ? hero.portrait : "assets/portraits/" + name + ".png";
    return (
      '<img class="inline-hero-portrait" src="' +
      assetUrl(portrait) +
      '" alt="" loading="lazy" onerror="this.style.opacity=0.3">'
    );
  }

  function synergyIntroWithoutCommonBuffers(intro) {
    if (!intro) {
      return "";
    }
    return intro
      .split("\n")
      .filter(function (line) {
        return !/^Common buffers are /i.test(line.trim());
      })
      .join("\n")
      .trim();
  }

  function renderCommonBuffers(buffers) {
    if (!buffers || !buffers.length) {
      return "";
    }
    const items = buffers.map(function (ref) {
      return (
        '<span class="synergy-common-buffer">' +
        renderInlineHeroPortrait(ref.slug, ref.name) +
        linkifyHero(ref.name, ref.slug) +
        "</span>"
      );
    });
    return (
      '<div class="synergy-common-buffers">Common buffers are ' +
      joinIntroFragments(items) +
      ".</div>"
    );
  }

  function renderSynergies(sections, heroName) {
    const syn = sections.benefits_from;
    if (!syn) return "";

    let html = '<div class="detail-section">';
    html +=
      "<h2>Units improving " + escapeHtml(heroName) + "</h2>";

    if (syn.intro || (syn.common_buffers && syn.common_buffers.length)) {
      const introText = synergyIntroWithoutCommonBuffers(syn.intro);
      const buffersHtml = renderCommonBuffers(syn.common_buffers);
      if (introText || buffersHtml) {
        html += '<div class="synergy-intro-block">';
        if (introText) {
          html +=
            '<div class="synergy-intro">' +
            renderInline(introText.replace(/\n/g, " ")) +
            "</div>";
        }
        html += buffersHtml;
        html += "</div>";
      }
    }

    if (syn.requires && syn.requires.text) {
      html +=
        '<div class="synergy-requires"><p>' +
        renderInline(syn.requires.text) +
        "</p></div>";
    }

    if (syn.partners && syn.partners.length) {
      html += renderSynergyHeroGrid(syn.partners, function (partner) {
        return renderSynergyPartnerExplanation(partner.reasons);
      });
    } else {
      html +=
        "<p><em>No synergy partners matched stat buffs or enablers.</em></p>";
    }

    html += "</div>";

    if (syn.benefited_by) {
      html += renderBenefitedBySection(syn.benefited_by, heroName);
    }

    return html;
  }

  function joinIntroFragments(fragments) {
    if (!fragments.length) {
      return "";
    }
    if (fragments.length === 1) {
      return fragments[0];
    }
    if (fragments.length === 2) {
      return fragments[0] + " and " + fragments[1];
    }
    return (
      fragments.slice(0, -1).join(", ") +
      ", and " +
      fragments[fragments.length - 1]
    );
  }

  function parseBuffEffectLabel(label) {
    let text = (label || "").trim();
    let tier = "";
    const tierMatch = text.match(ASCENSION_TIER_SUFFIX_RE);
    if (tierMatch) {
      tier = tierMatch[1];
      text = text.slice(0, tierMatch.index).trim();
    }
    text = text.replace(/\s+(?:de)?buff\s*$/i, "").trim();
    if (!text) {
      text = (label || "").trim();
    }
    return { base: text, tier: tier };
  }

  function renderBuffTargetingChip(targetingType) {
    if (!targetingType) {
      return "";
    }
    return chipifyTargetingSegment(targetingType);
  }

  function renderMergedEffectPill(baseLabel, quality, tier, conditional, polarity) {
    const qMeta = qualityIndicatorMeta(
      quality,
      resolveLeadingChip(baseLabel, polarity).isCc
    );
    let merged =
      mergeEffectWithQuality(baseLabel, quality, tier, polarity) ||
      mergeLabelWithIndicator(baseLabel, quality, tier, polarity);
    if (!merged && qMeta) {
      merged = formatMergedIndicator(
        { textOnly: baseLabel, tierSuffix: tier || "" },
        qMeta,
        true
      );
    }
    if (!merged) {
      merged =
        chipifyEffectName(baseLabel, polarity) +
        formatMergedTierSuffix(tier) +
        (quality ? " " + formatTag(quality) : "");
    }
    if (conditional) {
      merged +=
        ' <span class="chip chip-generic chip-has-tip"' +
        chipTipAttrs(conditionalTooltip(conditional)) +
        ">🎲 " +
        escapeHtml("conditional (" + conditional + ")") +
        "</span>";
    }
    return merged;
  }

  function renderBuffProvidedEntry(buff) {
    const parsed = parseBuffEffectLabel(buff.label || "");
    const quality = buff.quality || "";
    let html = renderMergedEffectPill(
      parsed.base,
      quality,
      parsed.tier,
      buff.conditional,
      "buff"
    );
    const targetingHtml = renderBuffTargetingChip(
      buff.targetingType || buff.targeting
    );
    if (targetingHtml) {
      html += " " + targetingHtml;
    }
    return '<span class="synergy-buff-entry">' + html + "</span>";
  }

  function renderBuffsProvidedIntro(data) {
    if (!data || !data.buffs || !data.buffs.length) {
      return "";
    }
    const entries = data.buffs.map(renderBuffProvidedEntry);
    return (
      escapeHtml(data.hero + " provides ") +
      '<span class="synergy-buff-pills">' +
      joinIntroFragments(entries) +
      "</span>."
    );
  }

  function renderBenefitedBySection(bb, heroName) {
    const hasHeroes = bb.heroes && bb.heroes.length;
    const hasOverflow =
      bb.intro ||
      (bb.overflow_reasons && bb.overflow_reasons.length) ||
      bb.strongest_note;
    const buffsProvided = bb.buffs_provided || null;
    if (!buffsProvided && !bb.buffs_intro && !hasHeroes && !hasOverflow) {
      return "";
    }

    let html = '<div class="detail-section">';
    html +=
      "<h2>Units benefitting most from " + escapeHtml(heroName) + "</h2>";

    if (buffsProvided) {
      html +=
        '<div class="synergy-intro">' +
        renderBuffsProvidedIntro(buffsProvided) +
        "</div>";
    } else if (bb.buffs_intro) {
      html +=
        '<div class="synergy-intro">' +
        renderInline(bb.buffs_intro) +
        "</div>";
    }

    if (bb.intro) {
      html +=
        '<div class="synergy-intro">' +
        renderInline(bb.intro.replace(/\n/g, " ")) +
        "</div>";
    }
    if (bb.overflow_reasons && bb.overflow_reasons.length) {
      html += "<ul>";
      bb.overflow_reasons.forEach(function (r) {
        html += "<li>" + renderRichLine(r) + "</li>";
      });
      html += "</ul>";
    }
    if (bb.strongest_note) {
      html +=
        '<div class="synergy-intro">' +
        renderInline(bb.strongest_note) +
        "</div>";
    }
    if (hasHeroes) {
      html += renderSynergyHeroGrid(bb.heroes, function (hero) {
        return renderSynergyPartnerExplanation(hero.reasons);
      });
    }

    html += "</div>";
    return html;
  }

  function renderReplacements(sections, mainHero) {
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
          let footer = "";
          const repHero = heroBySlug[e.slug];
          if (repHero) {
            footer = renderPrydwenTierBoxes(
              getHeroPrydwenTiers(repHero),
              "compact",
              mainHero ? getHeroPrydwenTiers(mainHero) : null,
              mainHero && mainHero.name
            );
          }
          return renderHeroCompactCard(e.slug, e.name, body, footer);
        }),
        "hero-compact-grid-3"
      );
      html += "</div>";
    });
    html += "</div>";
    return html;
  }

  function showDetail(hero) {
    closeSkillCardPopover();
    detailHero = hero;
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
    html +=
      '<div class="badges badges-left">' +
      renderBadges(hero, { includeRoleCategory: true }) +
      "</div>";
    if (hero.description) {
      html +=
        '<p class="detail-desc">' + escapeHtml(hero.description) + "</p>";
    }
    html += "</div></div>";

    if (hero.sections.behavior) {
      const parts = splitBehavior(hero.sections.behavior);
      if (parts.behavior) {
        html +=
          '<div class="detail-section summary-section skill-overview-section">';
        html += renderPrydwenTierBoxes(getHeroPrydwenTiers(hero));
        const behaviorMd = stripPrydwenTierLine(parts.behavior);
        const behaviorParts = splitBehaviorHeading(behaviorMd);
        if (behaviorParts.title) {
          html += "<h2>" + escapeHtml(behaviorParts.title) + "</h2>";
        }
        if (behaviorParts.body) {
          html += '<div class="skill-overview-metrics">';
          html += renderMarkdown(behaviorParts.body, {
            behaviorHero: hero,
            behaviorSection: true,
          });
          html += "</div>";
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
          const metricsHtml = renderSkillOverviewMetrics(parts.skillOverview);
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
    html += renderReplacements(hero.sections, hero);

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
    const seenRoles = {};
    heroes.forEach(function (h) {
      if (h.faction && !seenF[h.faction]) {
        seenF[h.faction] = true;
        factions.push(h.faction);
      }
      if (h.class && !seenC[h.class]) {
        seenC[h.class] = true;
        classes.push(h.class);
      }
      if (h.roleCategory && !seenRoles[h.roleCategory]) {
        seenRoles[h.roleCategory] = true;
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
    html += '<span class="filter-label">Role</span>';
    ROLE_FILTER_ORDER.forEach(function (roleKey) {
      if (!seenRoles[roleKey]) {
        return;
      }
      const meta = ROLE_CATEGORY_META[roleKey];
      html +=
        '<button type="button" class="filter-btn" data-filter="role" data-value="' +
        escapeHtml(roleKey) +
        '">' +
        escapeHtml(meta.label) +
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
        b.classList.toggle(
          "active",
          !activeFaction && !activeClass && !activeRole
        );
      } else if (f === "faction") {
        b.classList.toggle("active", b.dataset.value === activeFaction);
      } else if (f === "class") {
        b.classList.toggle("active", b.dataset.value === activeClass);
      } else if (f === "role") {
        b.classList.toggle("active", b.dataset.value === activeRole);
      }
    });
    updateFiltersToggleLabel();
  }

  filtersEl.addEventListener("click", function (e) {
    const btn = e.target.closest(".filter-btn");
    if (!btn) {
      return;
    }
    if (btn.dataset.filter === "all") {
      activeFaction = "";
      activeClass = "";
      activeRole = "";
    } else if (btn.dataset.filter === "faction") {
      const v = btn.dataset.value;
      activeFaction = activeFaction === v ? "" : v;
    } else if (btn.dataset.filter === "class") {
      const v = btn.dataset.value;
      activeClass = activeClass === v ? "" : v;
    } else if (btn.dataset.filter === "role") {
      const v = btn.dataset.value;
      activeRole = activeRole === v ? "" : v;
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
      storeViewMode(viewMode);
      syncViewToggleButtons();
      if (!detailView.classList.contains("hidden")) {
        return;
      }
      showIndexView();
    });
  }

  if (heroesTableHead) {
    heroesTableHead.addEventListener("click", function (e) {
      const clearBtn = e.target.closest(".col-filter-clear");
      if (clearBtn) {
        e.preventDefault();
        e.stopPropagation();
        const col = parseInt(clearBtn.dataset.col, 10);
        openColumnFilter = col;
        delete csvColumnFilters[col];
        renderList();
        return;
      }
      if (e.target.closest(".col-filter-panel")) {
        return;
      }
      const filterTrigger = e.target.closest(".col-filter-trigger");
      if (filterTrigger) {
        const details = filterTrigger.closest("details.col-filter");
        if (details) {
          openColumnFilter = parseInt(details.dataset.col, 10);
        }
        return;
      }
      const sortBtn = e.target.closest(".th-sort-btn");
      if (!sortBtn) {
        return;
      }
      const col = parseInt(sortBtn.dataset.col, 10);
      if (col === sortColumn) {
        sortDir = -sortDir;
      } else {
        sortColumn = col;
        sortDir = 1;
      }
      renderList();
    });

    heroesTableHead.addEventListener("change", function (e) {
      const cb = e.target.closest(".col-filter-cb");
      if (!cb) {
        return;
      }
      const col = parseInt(cb.dataset.col, 10);
      const value = cb.value;
      if (!csvColumnFilters[col]) {
        csvColumnFilters[col] = new Set();
      }
      if (cb.checked) {
        csvColumnFilters[col].add(value);
      } else {
        csvColumnFilters[col].delete(value);
        if (!csvColumnFilters[col].size) {
          delete csvColumnFilters[col];
        }
      }
      openColumnFilter = col;
      renderList();
    });

    heroesTableHead.addEventListener("toggle", function (e) {
      const details = e.target;
      if (!details.matches || !details.matches("details.col-filter")) {
        return;
      }
      if (details.open) {
        openColumnFilter = parseInt(details.dataset.col, 10);
        requestAnimationFrame(positionOpenColumnFilter);
        bindColumnFilterPointerTracking();
      } else {
        clearColumnFilterPanelPosition(details);
        unbindColumnFilterPointerTracking();
        if (openColumnFilter === parseInt(details.dataset.col, 10)) {
          openColumnFilter = -1;
        }
      }
    }, true);

    const tableScrollEl = getTableScrollEl();
    if (tableScrollEl) {
      tableScrollEl.addEventListener("scroll", closeColumnFilterOnScroll, {
        passive: true,
      });
    }
    window.addEventListener("scroll", closeColumnFilterOnScroll, {
      passive: true,
    });
    window.addEventListener("resize", positionOpenColumnFilter);
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
    csvColumnWidths = [];
    columnWidthsLocked = false;
    augmentCsvWithTiers();
    buildColumnFilterOptions();
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
    buildColumnFilterOptions();
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
    const TIP_CHIP_SELECTOR =
      "[data-tip].chip-has-tip, .tier-chip[data-tip]";
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

    function tipChipFromEvent(e) {
      return e.target.closest(TIP_CHIP_SELECTOR);
    }

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
          const chip = tipChipFromEvent(e);
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
          const chip = tipChipFromEvent(e);
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
      const chip = tipChipFromEvent(e);
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
        const chip = tipChipFromEvent(e);
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
      const chip = tipChipFromEvent(e);
      if (chip) {
        showChipTooltip(chip);
      }
    });

    document.addEventListener("focusout", function (e) {
      const chip = tipChipFromEvent(e);
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

  (function initSkillCardPopover() {
    const backdrop = document.createElement("div");
    backdrop.className = "skill-card-popover-backdrop";
    backdrop.hidden = true;

    const popover = document.createElement("div");
    popover.id = "skill-card-popover";
    popover.className = "skill-card-popover";
    popover.hidden = true;
    popover.setAttribute("role", "dialog");
    popover.setAttribute("aria-modal", "true");
    popover.setAttribute("aria-labelledby", "skill-popover-title");

    document.body.appendChild(backdrop);
    document.body.appendChild(popover);

    let anchorCard = null;

    function setCardExpanded(card, expanded) {
      if (!card) {
        return;
      }
      card.setAttribute("aria-expanded", expanded ? "true" : "false");
      card.classList.toggle("skill-card-active", expanded);
    }

    function positionSkillPopover(card) {
      const rect = card.getBoundingClientRect();
      const margin = 12;
      const arrowSize = 10;
      const maxHeight = Math.min(window.innerHeight * 0.6, 420);

      popover.style.maxHeight = maxHeight + "px";
      popover.style.visibility = "hidden";
      popover.hidden = false;

      const popH = popover.offsetHeight;
      const popW = popover.offsetWidth;

      let placeBelow = false;
      let top = rect.top - popH - margin - arrowSize;
      if (top < margin) {
        placeBelow = true;
        top = rect.bottom + margin + arrowSize;
      }

      let left = rect.left + rect.width / 2 - popW / 2;
      const maxLeft = window.innerWidth - popW - margin;
      left = Math.max(margin, Math.min(left, maxLeft));

      const cardCenter = rect.left + rect.width / 2;
      const arrowLeft = Math.max(18, Math.min(cardCenter - left, popW - 18));

      popover.style.top = top + "px";
      popover.style.left = left + "px";
      popover.style.setProperty("--arrow-left", arrowLeft + "px");
      popover.classList.toggle("skill-card-popover--below", placeBelow);
      popover.style.visibility = "";
    }

    function hideSkillPopover() {
      if (anchorCard) {
        setCardExpanded(anchorCard, false);
      }
      popover.hidden = true;
      backdrop.hidden = true;
      anchorCard = null;
    }

    function showSkillPopover(card, cardData) {
      if (!card || !cardData) {
        return;
      }
      if (anchorCard === card) {
        hideSkillPopover();
        return;
      }
      if (anchorCard) {
        setCardExpanded(anchorCard, false);
      }
      anchorCard = card;
      popover.innerHTML = formatSkillDetail(cardData);
      backdrop.hidden = false;
      popover.hidden = false;
      setCardExpanded(card, true);
      positionSkillPopover(card);
    }

    closeSkillCardPopover = hideSkillPopover;

    popover.addEventListener("click", function (e) {
      if (e.target.closest(".skill-popover-close")) {
        e.stopPropagation();
        hideSkillPopover();
      }
    });

    function skillCardFromEvent(e) {
      const chip = e.target.closest(".skill-card-tags .chip");
      if (chip) {
        return null;
      }
      return e.target.closest(".skill-card[data-skill-category]");
    }

    function openFromCard(card) {
      const data = skillCardData(card.dataset.skillCategory);
      if (!data) {
        return;
      }
      showSkillPopover(card, data);
    }

    document.addEventListener("click", function (e) {
      const card = skillCardFromEvent(e);
      if (card) {
        e.preventDefault();
        e.stopPropagation();
        openFromCard(card);
        return;
      }
      if (
        anchorCard &&
        !popover.contains(e.target) &&
        !anchorCard.contains(e.target)
      ) {
        hideSkillPopover();
      }
    });

    backdrop.addEventListener("click", function () {
      hideSkillPopover();
    });

    document.addEventListener("keydown", function (e) {
      const card = e.target.closest(".skill-card[data-skill-category]");
      if (
        card &&
        (e.key === "Enter" || e.key === " ") &&
        !e.target.closest(".skill-card-tags .chip")
      ) {
        e.preventDefault();
        openFromCard(card);
        return;
      }
      if (e.key === "Escape" && anchorCard) {
        hideSkillPopover();
        anchorCard.focus();
      }
    });

    window.addEventListener(
      "scroll",
      function () {
        if (anchorCard && !popover.hidden) {
          positionSkillPopover(anchorCard);
        }
      },
      true
    );

    window.addEventListener("resize", function () {
      if (anchorCard && !popover.hidden) {
        positionSkillPopover(anchorCard);
      }
    });
  })();

  viewMode = readStoredViewMode();
  syncViewToggleButtons();
  initWelcomeWarning();
  initFiltersCollapse();
  redirectLegacyHeroPath();
  loadHeroData();
  loadCsvData();
})();
