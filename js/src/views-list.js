window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const config = window.AFKJ.config;
  const chips = window.AFKJ.chips;
  const gridView = window.AFKJ.views.grid;
  const escapeHtml = utils.escapeHtml.bind(utils);

  const CC_EFFECT_TYPES = [
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
    "Disarm",
  ];

  const ANTI_CC_EFFECT_TYPES = [
    "Unaffected",
    "Steadfast",
    "Immune",
    "Untargetable",
    "Cleanse",
  ];

  // Keep in sync with scripts/effect_labels.py BUFF_EFFECT_TYPES.
  const BUFF_EFFECT_TYPES = [
    "ATK",
    "Basic stats",
    "ATK SPD",
    "Haste",
    "Crit",
    "DEF Penetration",
    "DEF",
    "Damage taken",
    "Damage dealt",
    "Ranged damage",
    "Magic damage",
    "Energy",
    "Execution",
    "Fatal blow immunity",
    "Invincible",
    "Lifedrain",
    "Max HP",
    "Attack range",
    "Ranged DEF",
    "Crit DMG boost",
    "Vitality",
    "Dodge chance",
    "Movement speed",
  ];

  // Keep in sync with scripts/effect_labels.py DEBUFF_EFFECT_TYPES.
  const DEBUFF_EFFECT_TYPES = [
    "ATK",
    "Basic stats",
    "DoT",
    "Damage taken",
    "Damage dealt",
    "Debuff duration",
    "Magic damage",
    "Energy",
    "Execution",
    "Haste",
    "Magic DEF",
    "Max HP",
    "Movement speed",
    "Phys DEF",
    "Vitality",
    "Healing",
    "Crit Resist",
    "Vulnerable",
    "ATK SPD",
  ];

  const EFFECT_CC_COLUMN = "Crowd Control";
  const EFFECT_ANTI_CC_COLUMN = "Crowd Control Counter";
  const EFFECT_BUFF_COLUMN = "Buffs";
  const EFFECT_DEBUFF_COLUMN = "Debuffs";
  const EFFECT_CC_COLUMNS = [EFFECT_CC_COLUMN];
  const EFFECT_ANTI_CC_COLUMNS = [EFFECT_ANTI_CC_COLUMN];
  const EFFECT_BUFF_COLUMNS = [EFFECT_BUFF_COLUMN];
  const EFFECT_DEBUFF_COLUMNS = [EFFECT_DEBUFF_COLUMN];

  const CC_EFFECT_TYPE_SET = {};
  CC_EFFECT_TYPES.forEach(function (label) {
    CC_EFFECT_TYPE_SET[label.toLowerCase()] = label;
  });
  const ANTI_CC_EFFECT_TYPE_SET = {};
  ANTI_CC_EFFECT_TYPES.forEach(function (label) {
    ANTI_CC_EFFECT_TYPE_SET[label.toLowerCase()] = label;
  });
  const BUFF_EFFECT_TYPE_SET = {};
  BUFF_EFFECT_TYPES.forEach(function (label) {
    BUFF_EFFECT_TYPE_SET[label.toLowerCase()] = label;
  });
  const DEBUFF_EFFECT_TYPE_SET = {};
  DEBUFF_EFFECT_TYPES.forEach(function (label) {
    DEBUFF_EFFECT_TYPE_SET[label.toLowerCase()] = label;
  });

  function canonicalCcEffectType(label) {
    const trimmed = (label || "").trim();
    if (!trimmed) {
      return "";
    }
    const lower = trimmed.toLowerCase();
    return CC_EFFECT_TYPE_SET[lower] || ANTI_CC_EFFECT_TYPE_SET[lower] || "";
  }

  function canonicalBuffDebuffEffectType(label) {
    const trimmed = (label || "").trim();
    if (!trimmed) {
      return "";
    }
    const lower = trimmed.toLowerCase();
    return BUFF_EFFECT_TYPE_SET[lower] || DEBUFF_EFFECT_TYPE_SET[lower] || "";
  }

  function canonicalMergedEffectType(label) {
    return canonicalCcEffectType(label) || canonicalBuffDebuffEffectType(label);
  }

  function isMergedCcColumn(column) {
    return column === EFFECT_CC_COLUMN || column === EFFECT_ANTI_CC_COLUMN;
  }

  function isMergedBuffDebuffColumn(column) {
    return column === EFFECT_BUFF_COLUMN || column === EFFECT_DEBUFF_COLUMN;
  }

  function isMergedEffectColumn(column) {
    return isMergedCcColumn(column) || isMergedBuffDebuffColumn(column);
  }

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

  const DMG_COLUMN_BASE = {
    Magic: "Magic",
    Physical: "Physical",
    Ranged: "Ranged",
    True: "True damage",
    "HP Loss": "HP loss",
    "Max HP": "Max HP damage",
  };

  let columnFilterPointerHandler = null;

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

  function listColumnMeta(columnId) {
    const state = window.AFKJ.state;
    return state.listColumnsById[columnId] || null;
  }

  function listColumnDisplayLabel(columnId) {
    const meta = listColumnMeta(columnId);
    return meta ? meta.label : columnId;
  }

  function parseEffectColumnLabel(column) {
    if (column === EFFECT_BUFF_COLUMN) {
      return { base: column, polarity: "buff", tier: "" };
    }
    if (column === EFFECT_DEBUFF_COLUMN) {
      return { base: column, polarity: "debuff", tier: "" };
    }
    const meta = listColumnMeta(column);
    if (meta) {
      return {
        base: meta.label,
        polarity: meta.polarity,
        tier: "",
      };
    }
    if (column.endsWith(" DMG")) {
      const short = column.slice(0, -4);
      return {
        base: DMG_COLUMN_BASE[short] || short,
        polarity: "damage",
        tier: "",
      };
    }
    const parsed = chips.parseEffectLabelParts(column);
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
    const segments = chips.splitSummarySegments(text);
    let effect = "";
    let quality = "";
    let conditional = "";
    let timing = "";

    if (segments.length) {
      const leading = canonicalMergedEffectType(segments[0]);
      if (leading) {
        effect = leading;
        segments.shift();
      }
    }

    function popTrailingQuality() {
      if (!segments.length) {
        return;
      }
      const last = chips.unwrapBackticks(segments[segments.length - 1]);
      const lower = last.toLowerCase();
      if (chips.QUALITY_CLASS[lower]) {
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
      effect: effect,
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
      chips.chipTipAttrs(chips.conditionalTooltip(conditionalText)) +
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
    const pillBase = parsed.effect || colMeta.base;
    let conditionalParam = "";
    if (parsed.conditional) {
      const condMatch = parsed.conditional.match(/conditional\s*\(([^)]+)\)/i);
      if (condMatch) {
        conditionalParam = condMatch[1].trim();
      }
    }

    let html = chips.renderMergedEffectPill(
      pillBase,
      parsed.quality,
      colMeta.tier || "",
      conditionalParam,
      colMeta.polarity
    );
    if (parsed.targeting) {
      html += " " + chips.renderBuffTargetingChip(parsed.targeting);
    }
    if (parsed.timing) {
      const timingChip = chips.tryChipify(parsed.timing);
      html +=
        " " +
        (timingChip !== null ? timingChip : chips.formatTag(parsed.timing));
    }
    html += renderEffectConditionalChip(parsed.conditional);
    return html;
  }

  function getListCellRawValue(row, colIdx, col) {
    const state = window.AFKJ.state;
    const tiers = window.AFKJ.tiers;
    let cellValue = row[colIdx] || "";
    const hero = state.heroByName[row[0] || ""];
    if (col === "Role" && !String(cellValue || "").trim() && hero) {
      const roleMeta = tiers.roleCategoryMeta(hero.roleCategory);
      if (roleMeta) {
        cellValue = roleMeta.label;
      }
    }
    if (hero && tiers.TIER_CSV_HEADERS[col] && !String(cellValue || "").trim()) {
      const tierCol = tiers.TIER_CSV_COLUMNS.find(function (t) {
        return t.header === col;
      });
      if (tierCol) {
        cellValue = tiers.getHeroPrydwenTiers(hero)[tierCol.key] || "?";
      }
    }
    return String(cellValue || "").trim();
  }

  const FILTER_GROUP_META = [
    { id: "targeting", label: "Targeting" },
    { id: "quality", label: "Magnitude" },
    { id: "timing", label: "Timing" },
    { id: "conditional", label: "Conditional" },
    { id: "other", label: "Other" },
  ];

  function filterGroupMetaForColumn(column) {
    if (column === EFFECT_CC_COLUMN) {
      return [
        { id: "effect", label: "Effect" },
        { id: "targeting", label: "Targeting" },
        { id: "quality", label: "Magnitude" },
      ];
    }
    if (column === EFFECT_ANTI_CC_COLUMN) {
      return [
        { id: "effect", label: "Effect" },
        { id: "targeting", label: "Targeting" },
        { id: "timing", label: "Timing" },
      ];
    }
    if (isMergedBuffDebuffColumn(column)) {
      return [
        { id: "effect", label: "Effect" },
        { id: "targeting", label: "Targeting" },
        { id: "quality", label: "Magnitude" },
        { id: "conditional", label: "Conditional" },
      ];
    }
    return FILTER_GROUP_META;
  }

  function classifyFilterAtom(value) {
    const trimmed = (value || "").trim();
    if (!trimmed) {
      return "other";
    }
    const lower = trimmed.toLowerCase();
    if (canonicalMergedEffectType(trimmed)) {
      return "effect";
    }
    if (chips.QUALITY_CLASS[lower]) {
      return "quality";
    }
    if (chips.SPEED_CLASS[lower]) {
      return "quality";
    }
    if (/conditional/i.test(trimmed)) {
      return "conditional";
    }
    // Timing before targeting: labels like "On skill" also exist in
    // TARGETING_DEFINITIONS for chip styling, but are anti-CC timings.
    if (isTimingSegment(trimmed)) {
      return "timing";
    }
    if (config.TARGETING_DEFINITIONS[lower]) {
      return "targeting";
    }
    return "other";
  }

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

  function atomSetMatchesGroupedSelection(atomSet, selectedByGroup, groupMeta) {
    const metas = groupMeta || FILTER_GROUP_META;
    const normalized = {};
    atomSet.forEach(function (atom) {
      normalized[atom.toLowerCase()] = atom;
    });
    return metas.every(function (meta) {
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

  function sortFilterOptionValues(values, column) {
    const isTier = window.AFKJ.tiers.TIER_CSV_HEADERS[column];
    const isRole = column === "Role";
    if (isTier) {
      return values.slice().sort(function (a, b) {
        return tierFilterSortRank(a) - tierFilterSortRank(b);
      });
    }
    if (isRole) {
      return values.slice().sort(function (a, b) {
        const metaA = window.AFKJ.tiers.roleCategoryMeta(a) || config.ROLE_CATEGORY_META[a];
        const metaB = window.AFKJ.tiers.roleCategoryMeta(b) || config.ROLE_CATEGORY_META[b];
        const rankA = metaA ? config.ROLE_FILTER_ORDER.indexOf(a) : 99;
        const rankB = metaB ? config.ROLE_FILTER_ORDER.indexOf(b) : 99;
        return rankA - rankB;
      });
    }
    if (
      values.length &&
      values.every(function (value) {
        return !!canonicalMergedEffectType(value);
      })
    ) {
      return values.slice().sort(function (a, b) {
        return mergedEffectFilterSortRank(a, column) -
          mergedEffectFilterSortRank(b, column);
      });
    }
    return values.slice().sort();
  }

  function tierFilterSortRank(value) {
    const idx = window.AFKJ.tiers.TIER_FILTER_ORDER.indexOf(value);
    return idx >= 0 ? idx : 99;
  }

  function mergedEffectFilterSortRank(value, column) {
    if (column === EFFECT_BUFF_COLUMN) {
      const buffIdx = BUFF_EFFECT_TYPES.indexOf(value);
      return buffIdx >= 0 ? buffIdx : 99;
    }
    if (column === EFFECT_DEBUFF_COLUMN) {
      const debuffIdx = DEBUFF_EFFECT_TYPES.indexOf(value);
      return debuffIdx >= 0 ? debuffIdx : 99;
    }
    const ccIdx = CC_EFFECT_TYPES.indexOf(value);
    if (ccIdx >= 0) {
      return ccIdx;
    }
    const antiIdx = ANTI_CC_EFFECT_TYPES.indexOf(value);
    if (antiIdx >= 0) {
      return antiIdx;
    }
    return 99;
  }

  function buildEffectColumnFilterGroups(col, idx) {
    const state = window.AFKJ.state;
    const groupMeta = filterGroupMetaForColumn(col);
    const byGroup = {};
    state.csvRows.forEach(function (row) {
      const raw = getListCellRawValue(row, idx, col);
      if (!raw) {
        return;
      }
      extractCellFilterAtoms(col, raw).forEach(function (v) {
        const kind = classifyFilterAtom(v);
        if (!byGroup[kind]) {
          byGroup[kind] = new Set();
        }
        byGroup[kind].add(v);
      });
    });
    return groupMeta
      .map(function (meta) {
        const values = byGroup[meta.id];
        return {
          id: meta.id,
          label: meta.label,
          values: values ? sortFilterOptionValues(Array.from(values), col) : [],
        };
      })
      .filter(function (group) {
        return group.values.length;
      });
  }

  function filterOptionGroupsHasChoices(groups) {
    return groups.some(function (group) {
      return group.values && group.values.length;
    });
  }

  function columnFilterCombineMode(colIdx) {
    return window.AFKJ.state.csvColumnFilterCombine[colIdx] || "or";
  }

  function toggleColumnFilterCombine(colIdx) {
    const state = window.AFKJ.state;
    if (columnFilterCombineMode(colIdx) === "and") {
      delete state.csvColumnFilterCombine[colIdx];
    } else {
      state.csvColumnFilterCombine[colIdx] = "and";
    }
    renderList();
  }

  function atomsFromEffectEntry(entry) {
    const atoms = new Set();
    const trimmed = entry.trim();
    if (!trimmed) {
      return atoms;
    }
    const parsed = parseEffectCellPart(trimmed);
    if (parsed.effect) {
      atoms.add(parsed.effect);
    }
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
          return chips.behaviorTagChip(tag);
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
    const state = window.AFKJ.state;
    const filterOptions = [];
    state.csvHeaders.forEach(function (col, idx) {
      if (idx === 0) {
        filterOptions.push([]);
        return;
      }
      if (isEffectSortColumn(col)) {
        filterOptions.push(buildEffectColumnFilterGroups(col, idx));
        return;
      }
      const vals = new Set();
      state.csvRows.forEach(function (row) {
        const raw = getListCellRawValue(row, idx, col);
        if (!raw) return;
        const atoms = extractCellFilterAtoms(col, raw);
        atoms.forEach(vals.add, vals);
      });
      const uniqueVals = Array.from(vals);
      filterOptions.push([
        {
          id: "value",
          label: "",
          values: sortFilterOptionValues(uniqueVals, col),
        },
      ]);
    });
    state.csvColumnFilterOptions = filterOptions;
  }

  function cellMatchesColumnFilter(column, cellValue, selected, combineMode) {
    if (selected.length === 0) {
      return true;
    }
    const rawVal = (cellValue || "").trim();
    if (!rawVal) {
      return false;
    }

    if (isEffectSortColumn(column)) {
      const selectedByGroup = splitSelectedByFilterGroup(selected);
      const groupMeta = filterGroupMetaForColumn(column);
      const entrySets = effectEntryAtomSets(rawVal);
      return entrySets.some(function (atomSet) {
        return atomSetMatchesGroupedSelection(
          atomSet,
          selectedByGroup,
          groupMeta
        );
      });
    }

    const atoms = extractCellFilterAtoms(column, rawVal);
    const mode = combineMode === "and" ? "and" : "or";
    if (mode === "and") {
      return selected.every(function (value) {
        return atoms.has(value);
      });
    }
    return selected.some(function (value) {
      return atoms.has(value);
    });
  }

  function rowMatchesColumnFilters(row) {
    const state = window.AFKJ.state;
    for (let i = 1; i < state.csvHeaders.length; i++) {
      const col = state.csvHeaders[i];
      const selected = state.csvColumnFilters[i] || [];
      if (selected.length > 0) {
        const combine = columnFilterCombineMode(i);
        const cellValue = row[i];
        if (!cellMatchesColumnFilter(col, cellValue, selected, combine)) {
          return false;
        }
      }
    }
    return true;
  }

  function filterOptionIconHtml(column, value) {
    const trimmed = (value || "").trim();
    if (!trimmed) {
      return "";
    }
    const lower = trimmed.toLowerCase();

    if (column === "Faction") {
      const icon = utils.iconPath("factions", value);
      if (icon) {
        return (
          '<img class="col-filter-opt-icon" src="' +
          utils.assetUrl(icon) +
          '" alt="">'
        );
      }
    }
    if (column === "Class") {
      const icon = utils.iconPath("class", value);
      if (icon) {
        return (
          '<img class="col-filter-opt-icon" src="' +
          utils.assetUrl(icon) +
          '" alt="">'
        );
      }
    }
    if (column === "Role") {
      const roleKey = Object.keys(config.ROLE_CATEGORY_META).find(function (key) {
        return config.ROLE_CATEGORY_META[key].label.toLowerCase() === lower;
      });
      if (roleKey) {
        return (
          '<span class="col-filter-opt-emoji" aria-hidden="true">' +
          config.ROLE_CATEGORY_META[roleKey].emoji +
          "</span>"
        );
      }
    }

    for (let i = 0; i < chips.MOVEMENT_KEYS.length; i++) {
      const key = chips.MOVEMENT_KEYS[i];
      if (lower === key.toLowerCase()) {
        return (
          '<span class="col-filter-opt-emoji" aria-hidden="true">' +
          chips.MOVEMENT_DEFINITIONS[key].emoji +
          "</span>"
        );
      }
    }

    if (chips.SPEED_CLASS[lower]) {
      const emoji = chips.SPEED_EMOJI[lower] || "⏱️";
      return (
        '<span class="col-filter-opt-emoji" aria-hidden="true">' +
        emoji +
        "</span>"
      );
    }

    if (chips.QUALITY_CLASS[lower]) {
      const emoji = chips.QUALITY_EMOJI[lower] || "";
      return (
        '<span class="col-filter-opt-emoji" aria-hidden="true">' +
        emoji +
        "</span>"
      );
    }

    const targeting = config.TARGETING_DEFINITIONS[lower];
    if (targeting) {
      return (
        '<span class="col-filter-opt-emoji" aria-hidden="true">' +
        targeting.emoji +
        "</span>"
      );
    }

    if (isTimingSegment(trimmed)) {
      return '<span class="col-filter-opt-emoji" aria-hidden="true">⏱️</span>';
    }

    const tagKey = chips.exactTagDefinitionKey(trimmed);
    if (tagKey) {
      const def = config.TAG_DEFINITIONS[tagKey];
      return (
        '<span class="col-filter-opt-emoji" aria-hidden="true">' +
        def.emoji +
        "</span>"
      );
    }
    return "";
  }

  function renderColumnFilterPanel(colIdx, column, optionGroups) {
    if (!filterOptionGroupsHasChoices(optionGroups)) {
      return "";
    }
    const state = window.AFKJ.state;
    const selected = state.csvColumnFilters[colIdx] || [];
    const selectedSet = new Set(selected);
    const visibleGroups = optionGroups.filter(function (group) {
      return group.values && group.values.length;
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
        const checked = selectedSet.has(value) ? " checked" : "";
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
    if (selected.length) {
      html +=
        '<button type="button" class="col-filter-clear" data-col="' +
        colIdx +
        '">Clear</button>';
    }
    html += "</div>";
    return html;
  }

  function renderColumnFilterCombineToggle(colIdx, column) {
    if (column !== "Behavior tags") {
      return "";
    }
    const mode = columnFilterCombineMode(colIdx);
    const combineTitle =
      mode === "and"
        ? "Match all selected tags (and). Click to match any (or)."
        : "Match any selected tag (or). Click to match all (and).";
    return (
      '<button type="button" class="col-filter-combine-toggle" data-col="' +
      colIdx +
      '" aria-label="Combine filter selections" title="' +
      escapeHtml(combineTitle) +
      '">' +
      '<span class="col-filter-combine-seg' +
      (mode === "or" ? " active" : "") +
      '">or</span>' +
      '<span class="col-filter-combine-seg' +
      (mode === "and" ? " active" : "") +
      '">and</span>' +
      "</button>"
    );
  }

  function renderBadgeChip(label, kind) {
    if (!label) {
      return "";
    }
    if (kind === "faction") {
      const icon = utils.iconPath("factions", label);
      return (
        '<span class="badge ' +
        utils.factionClass(label) +
        '">' +
        (icon
          ? '<img src="' +
          utils.assetUrl(icon) +
          '" alt="" loading="lazy">'
          : "") +
        escapeHtml(label) +
        "</span>"
      );
    }
    if (kind === "class") {
      const icon = utils.iconPath("class", label);
      return (
        '<span class="badge">' +
        (icon
          ? '<img src="' +
          utils.assetUrl(icon) +
          '" alt="" loading="lazy">'
          : "") +
        escapeHtml(label) +
        "</span>"
      );
    }
    return '<span class="badge">' + escapeHtml(label) + "</span>";
  }

  function formatMovementChip(text) {
    const trimmed = text.trim();
    if (!trimmed) {
      return null;
    }
    const lower = trimmed.toLowerCase();
    for (let i = 0; i < chips.MOVEMENT_KEYS.length; i++) {
      const key = chips.MOVEMENT_KEYS[i];
      if (lower === key.toLowerCase()) {
        const def = chips.MOVEMENT_DEFINITIONS[key];
        return chips.chipSpan(def.emoji, trimmed, def.cls);
      }
    }
    return null;
  }

  function renderTableCell(column, value) {
    const rawVal = (value || "").trim();
    if (!rawVal) {
      return "";
    }
    if (column === "Hero") {
      const state = window.AFKJ.state;
      const hero = state.heroByName[rawVal];
      return utils.linkifyHero(rawVal, hero ? hero.slug : null);
    }
    if (column === "Faction") {
      return renderBadgeChip(rawVal, "faction");
    }
    if (column === "Class") {
      return renderBadgeChip(rawVal, "class");
    }
    if (column === "Role") {
      const roleKey = Object.keys(config.ROLE_CATEGORY_META).find(function (key) {
        return config.ROLE_CATEGORY_META[key].label.toLowerCase() === rawVal.toLowerCase();
      });
      if (roleKey) {
        return window.AFKJ.views.detail.renderRoleCategoryBadge(roleKey);
      }
      return escapeHtml(rawVal);
    }
    if (
      column === "Signature skill speed" ||
      column === "Non-ultimate speed"
    ) {
      return chips.formatTag(rawVal);
    }
    if (
      column === "DoT" ||
      column === "HoT" ||
      column === "Summons" ||
      column === "Energy provider"
    ) {
      if (rawVal.toLowerCase() === "yes") {
        return '<span class="chip chip-generic">✓ yes</span>';
      }
      return escapeHtml(rawVal);
    }
    if (column === "Movement") {
      const chip = formatMovementChip(rawVal);
      if (chip !== null) {
        return chip;
      }
      return (
        '<span class="chip chip-movement">🚶 ' +
        escapeHtml(rawVal) +
        "</span>"
      );
    }
    if (window.AFKJ.tiers.TIER_CSV_HEADERS[column]) {
      return window.AFKJ.tiers.renderTierTableCell(rawVal);
    }
    if (column === "Behavior tags") {
      return renderBehaviorTagsCell(rawVal);
    }
    if (isEffectSortColumn(column)) {
      const parts = rawVal
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
    return rawVal
      .split(/\s*;\s*/)
      .map(function (part) {
        return renderTableEntry(part.trim());
      })
      .join(" ");
  }

  function renderTableEntry(text) {
    if (/\s*(?:—|–)\s*/.test(text)) {
      return chips.renderRichLine(text);
    }
    return text
      .split(/\s*,\s*/)
      .map(function (part) {
        const chip = chips.tryChipify(part.trim());
        return chip !== null ? chip : escapeHtml(part.trim());
      })
      .join(" ");
  }

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
    if (listColumnMeta(column)) {
      return true;
    }
    if (isMergedEffectColumn(column)) {
      return true;
    }
    return false;
  }

  function listColumnClass(col) {
    const tiers = window.AFKJ.tiers;
    if (col === "Name") {
      return "col-name";
    }
    if (col === "Faction") {
      return "col-faction";
    }
    if (col === "Class") {
      return "col-class";
    }
    if (col === "Role") {
      return "col-role";
    }
    if (tiers.TIER_CSV_HEADERS[col]) {
      return "col-tier";
    }
    if (col === "Movement") {
      return "col-movement";
    }
    if (col === "Behavior tags") {
      return "col-behavior-tags";
    }
    if (isEffectSortColumn(col)) {
      return "col-effect-stack";
    }
    return "col-general";
  }

  function targetingRank(text) {
    const trimmed = (text || "").trim();
    if (!trimmed) {
      return 0;
    }
    const meta = chips.targetingTokenMeta(trimmed);
    if (meta) {
      return meta.rank || 0;
    }
    if (trimmed.indexOf(",") !== -1) {
      return trimmed.split(/\s*,\s*/).reduce(function (max, part) {
        return Math.max(max, targetingRank(part));
      }, 0);
    }
    if (/\s*(?:—|–)\s*/.test(trimmed)) {
      return chips.splitSummarySegments(trimmed).reduce(function (max, part) {
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
    const cellMeta = parseEffectCellPart(entry);
    if (!cellMeta) {
      return { label: entry, targetRank: 0, timeRank: 0, strengthRank: 0 };
    }
    const quality = (cellMeta.quality || "").toLowerCase();
    return {
      label: cellMeta.effect || cellMeta.targeting || entry,
      targetRank: targetingRank(cellMeta.targeting),
      timeRank: timingRank(cellMeta.timing),
      strengthRank: STRENGTH_RANK[quality] || 0,
    };
  }

  function effectSortKey(cellValue) {
    const trimmed = (cellValue || "").trim();
    if (!trimmed) {
      return null;
    }
    const parts = trimmed
      .split(/\s*;\s*/)
      .map(function (s) {
        return s.trim();
      })
      .filter(Boolean);
    const parsed = parts.map(parseEffectEntry);
    parsed.sort(compareEffectSortKeys);
    return parsed[0] || null;
  }

  function compareEffectSortKeys(ka, kb) {
    if (ka.strengthRank !== kb.strengthRank) {
      return kb.strengthRank - ka.strengthRank;
    }
    if (ka.targetRank !== kb.targetRank) {
      return kb.targetRank - ka.targetRank;
    }
    if (ka.timeRank !== kb.timeRank) {
      return kb.timeRank - ka.timeRank;
    }
    return ka.label.localeCompare(kb.label);
  }

  function compareEffectCells(av, bv) {
    const ka = effectSortKey(av);
    const kb = effectSortKey(bv);
    if (ka === null && kb === null) {
      return 0;
    }
    if (ka === null) {
      return 1;
    }
    if (kb === null) {
      return -1;
    }
    return compareEffectSortKeys(ka, kb);
  }

  function compareCsvRows(a, b) {
    const state = window.AFKJ.state;
    const idx = state.sortColumn;
    const col = state.csvHeaders[idx];
    const av = a[idx];
    const bv = b[idx];
    if (isEffectSortColumn(col)) {
      return compareEffectCells(av, bv) * state.sortDir;
    }
    if (window.AFKJ.tiers.TIER_CSV_HEADERS[col]) {
      const rankA = window.AFKJ.tiers.prydwenTierRank(av);
      const rankB = window.AFKJ.tiers.prydwenTierRank(bv);
      if (rankA !== rankB) {
        return (rankB - rankA) * state.sortDir;
      }
    }
    const sA = String(av || "").trim();
    const sB = String(bv || "").trim();
    const numA = Number(sA);
    const numB = Number(sB);
    if (!isNaN(numA) && !isNaN(numB)) {
      return (numA - numB) * state.sortDir;
    }
    return sA.localeCompare(sB) * state.sortDir;
  }

  function getTableScrollEl() {
    const state = window.AFKJ.state;
    return state.dom.listView ? state.dom.listView.querySelector(".table-scroll") : null;
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
    const state = window.AFKJ.state;
    if (state.openColumnFilter < 0 || !state.dom.heroesTableHead) {
      return;
    }
    state.dom.heroesTableHead.querySelectorAll("details.col-filter[open]").forEach(function (details) {
      if (parseInt(details.dataset.col, 10) !== state.openColumnFilter) {
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
    const state = window.AFKJ.state;
    if (state.openColumnFilter < 0 || !state.dom.heroesTableHead) {
      return null;
    }
    return state.dom.heroesTableHead.querySelector(
      'details.col-filter[data-col="' + state.openColumnFilter + '"]'
    );
  }

  function isPointerInColumnFilterZone(clientX, clientY) {
    const details = getOpenColumnFilterDetails();
    if (!details) {
      return false;
    }
    const trigger = details.querySelector(".col-filter-trigger");
    const panel = details.querySelector(".col-filter-panel");
    const pad = 6;
    if (trigger && utils.rectContainsPoint(trigger.getBoundingClientRect(), clientX, clientY, pad)) {
      return true;
    }
    if (panel && utils.rectContainsPoint(panel.getBoundingClientRect(), clientX, clientY, pad)) {
      return true;
    }
    return false;
  }

  function unbindColumnFilterPointerTracking() {
    if (columnFilterPointerHandler) {
      document.removeEventListener("pointerdown", columnFilterPointerHandler, true);
      columnFilterPointerHandler = null;
    }
  }

  function bindColumnFilterPointerTracking() {
    unbindColumnFilterPointerTracking();
    columnFilterPointerHandler = function (e) {
      if (!isPointerInColumnFilterZone(e.clientX, e.clientY)) {
        closeColumnFilter();
      }
    };
    document.addEventListener("pointerdown", columnFilterPointerHandler, true);
  }

  function closeColumnFilter() {
    const details = getOpenColumnFilterDetails();
    if (details) {
      details.open = false;
      clearColumnFilterPanelPosition(details);
    }
    window.AFKJ.state.openColumnFilter = -1;
    unbindColumnFilterPointerTracking();
  }

  function closeColumnFilterOnScroll() {
    if (window.AFKJ.state.openColumnFilter >= 0) {
      closeColumnFilter();
    }
  }

  function measureEffectStackCellWidth(cell) {
    const entries = cell.querySelectorAll(".effect-cell-entry");
    if (!entries.length) {
      return 0;
    }
    let maxWidth = 0;
    entries.forEach(function (ent) {
      let width = 0;
      Array.from(ent.childNodes).forEach(function (node) {
        if (node.nodeType === Node.ELEMENT_NODE) {
          width += node.getBoundingClientRect().width;
        } else if (node.nodeType === Node.TEXT_NODE) {
          const range = document.createRange();
          range.selectNodeContents(node);
          width += range.getBoundingClientRect().width;
        }
      });
      maxWidth = Math.max(maxWidth, width);
    });
    return maxWidth + 32;
  }

  function measureColumnWidths() {
    const state = window.AFKJ.state;
    if (!state.dom.heroesTableHead || !state.dom.heroesTableBody || !state.csvHeaders.length) {
      return;
    }
    if (!state.dom.heroesTableBody.rows.length) {
      return;
    }
    const widths = new Array(state.csvHeaders.length).fill(0);
    const labelRow = state.dom.heroesTableHead.querySelector(".heroes-table-label-row");
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
    const filterRow = state.dom.heroesTableHead.querySelector(".heroes-table-filter-row");
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
    Array.from(state.dom.heroesTableBody.rows).forEach(function (row) {
      Array.from(row.cells).forEach(function (cell, idx) {
        const col = state.csvHeaders[idx];
        const width =
          isEffectSortColumn(col) && cell.querySelector(".effect-cell-entry")
            ? measureEffectStackCellWidth(cell)
            : cell.getBoundingClientRect().width;
        widths[idx] = Math.max(widths[idx], width);
      });
    });
    state.csvColumnWidths = widths.map(function (width) {
      return Math.ceil(width);
    });
  }

  function updateTableColgroup() {
    const state = window.AFKJ.state;
    if (!state.dom.heroesTable) {
      return;
    }
    let colgroup = state.dom.heroesTable.querySelector("colgroup");
    if (!state.csvColumnWidths.length) {
      if (colgroup) {
        colgroup.remove();
      }
      state.dom.heroesTable.style.tableLayout = "";
      return;
    }
    if (!colgroup) {
      colgroup = document.createElement("colgroup");
      state.dom.heroesTable.insertBefore(colgroup, state.dom.heroesTableHead);
    }
    colgroup.innerHTML = state.csvColumnWidths
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
    state.dom.heroesTable.style.tableLayout = "fixed";
  }

  function buildListBodyHtml(rows) {
    const state = window.AFKJ.state;
    const tiers = window.AFKJ.tiers;
    let bodyHtml = "";
    rows.forEach(function (row) {
      const name = row[0] || "";
      const hero = state.heroByName[name];
      bodyHtml += "<tr>";
      row.forEach(function (cell, idx) {
        const col = state.csvHeaders[idx];
        let inner;
        if (col === "Name") {
          if (hero) {
            inner =
              '<a href="' +
              escapeHtml(utils.heroUrl(hero.slug)) +
              '" class="hero-link col-name-link" data-slug="' +
              escapeHtml(hero.slug) +
              '">' +
              '<span class="col-name-text">' +
              escapeHtml(name) +
              "</span>" +
              gridView.renderListHeroPortrait(hero) +
              "</a>";
          } else {
            inner = escapeHtml(name);
          }
        } else {
          inner = renderTableCell(col, getListCellRawValue(row, idx, col));
        }
        let tdCls = "";
        const colCls = listColumnClass(col);
        if (colCls) {
          tdCls = ' class="' + colCls + '"';
        }
        bodyHtml += "<td" + tdCls + ">" + inner + "</td>";
      });
      bodyHtml += "</tr>";
    });
    return bodyHtml;
  }

  function renderList() {
    const state = window.AFKJ.state;
    const dom = state.dom;
    const tiers = window.AFKJ.tiers;
    if (!state.csvHeaders.length) {
      if (dom.heroesTableHead) {
        dom.heroesTableHead.innerHTML = "";
      }
      if (dom.heroesTableBody) {
        dom.heroesTableBody.innerHTML =
          '<tr><td class="empty-state">Table data missing. Run ' +
          "<code>just render-site</code>.</td></tr>";
      }
      if (dom.listEmptyState) {
        dom.listEmptyState.classList.add("hidden");
      }
      return;
    }
    if (!dom.heroesTableHead || !dom.heroesTableBody) {
      return;
    }

    const allowed = window.AFKJ.router.filteredHeroNames();
    let rows = state.csvRows.filter(function (row) {
      return allowed[row[0]] && rowMatchesColumnFilters(row);
    });
    rows = rows.slice().sort(compareCsvRows);

    let labelRowHtml = '<tr class="heroes-table-label-row">';
    let filterRowHtml = '<tr class="heroes-table-filter-row">';
    state.csvHeaders.forEach(function (col, idx) {
      let cls = "sortable " + listColumnClass(col);
      const optionGroups = state.csvColumnFilterOptions[idx] || [];
      const selected = state.csvColumnFilters[idx] || [];
      const activeCount = selected.length;
      const hasFilter = activeCount > 0;
      const filterCls =
        "col-filter" +
        (hasFilter ? " is-active" : "") +
        (filterOptionGroupsHasChoices(optionGroups) ? "" : " is-empty");
      const label = tiers.TIER_CSV_HEADERS[col]
        ? tiers.formatTierColumnHeader(col)
        : escapeHtml(listColumnDisplayLabel(col));
      let sortCls = "th-sort-btn";
      if (idx === state.sortColumn) {
        sortCls += state.sortDir === 1 ? " sort-asc" : " sort-desc";
      }
      const showFilter =
        col !== "Name" && filterOptionGroupsHasChoices(optionGroups);
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
      let filterCellCls = "col-filter-cell " + listColumnClass(col);
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
        const combineToggleHtml = renderColumnFilterCombineToggle(idx, col);
        filterRowHtml += '<div class="col-filter-row">';
        filterRowHtml += combineToggleHtml;
        filterRowHtml +=
          '<details class="' +
          filterCls +
          '" data-col="' +
          idx +
          '"' +
          (state.openColumnFilter === idx ? " open" : "") +
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
        filterRowHtml += "</div>";
      }
      filterRowHtml += "</th>";
    });
    labelRowHtml += "</tr>";
    filterRowHtml += "</tr>";
    dom.heroesTableHead.innerHTML = labelRowHtml + filterRowHtml;
    requestAnimationFrame(positionOpenColumnFilter);

    const allRows = state.csvRows.filter(function (row) {
      return allowed[row[0]];
    });
    const tableScroll = getTableScrollEl();

    if (!state.columnWidthsLocked && allRows.length) {
      if (tableScroll) {
        tableScroll.style.visibility = "hidden";
      }
      dom.heroesTableBody.innerHTML = buildListBodyHtml(allRows);
      dom.listEmptyState.classList.toggle("hidden", rows.length > 0);
      requestAnimationFrame(function () {
        measureColumnWidths();
        state.columnWidthsLocked = state.csvColumnWidths.length > 0;
        updateTableColgroup();
        dom.heroesTableBody.innerHTML = buildListBodyHtml(rows);
        dom.listEmptyState.classList.toggle("hidden", rows.length > 0);
        if (tableScroll) {
          tableScroll.style.visibility = "";
        }
      });
      return;
    }

    dom.heroesTableBody.innerHTML = buildListBodyHtml(rows);
    updateTableColgroup();
    dom.listEmptyState.classList.toggle("hidden", rows.length > 0);
  }

  // Export module API to window.AFKJ.views.list
  window.AFKJ.views.list = {
    EFFECT_CC_COLUMNS: EFFECT_CC_COLUMNS,
    EFFECT_ANTI_CC_COLUMNS: EFFECT_ANTI_CC_COLUMNS,
    EFFECT_BUFF_COLUMNS: EFFECT_BUFF_COLUMNS,
    EFFECT_DEBUFF_COLUMNS: EFFECT_DEBUFF_COLUMNS,
    TIMING_RANK: TIMING_RANK,
    parseCsv: parseCsv,
    parseEffectColumnLabel: parseEffectColumnLabel,
    parseEffectCellPart: parseEffectCellPart,
    renderEffectCellPart: renderEffectCellPart,
    cellMatchesColumnFilter: cellMatchesColumnFilter,
    rowMatchesColumnFilters: rowMatchesColumnFilters,
    buildColumnFilterOptions: buildColumnFilterOptions,
    renderColumnFilterPanel: renderColumnFilterPanel,
    renderTableCell: renderTableCell,
    compareCsvRows: compareCsvRows,
    getTableScrollEl: getTableScrollEl,
    clearColumnFilterPanelPosition: clearColumnFilterPanelPosition,
    positionOpenColumnFilter: positionOpenColumnFilter,
    getOpenColumnFilterDetails: getOpenColumnFilterDetails,
    isPointerInColumnFilterZone: isPointerInColumnFilterZone,
    unbindColumnFilterPointerTracking: unbindColumnFilterPointerTracking,
    bindColumnFilterPointerTracking: bindColumnFilterPointerTracking,
    closeColumnFilter: closeColumnFilter,
    closeColumnFilterOnScroll: closeColumnFilterOnScroll,
    measureColumnWidths: measureColumnWidths,
    updateTableColgroup: updateTableColgroup,
    buildListBodyHtml: buildListBodyHtml,
    renderList: renderList,
    toggleColumnFilterCombine: toggleColumnFilterCombine,
  };
})();
