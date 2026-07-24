window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;

  function columnIndex(columnName) {
    const headers = window.AFKJ.state.csvHeaders || [];
    return headers.indexOf(columnName);
  }

  function allOptionsForColumn(colIdx) {
    const groups = window.AFKJ.state.csvColumnFilterOptions[colIdx] || [];
    const values = [];
    groups.forEach(function (group) {
      (group.values || []).forEach(function (value) {
        if (value) {
          values.push(value);
        }
      });
    });
    return values;
  }

  function encodeFilterParam(column, values) {
    if (values.length === 1 && values[0] === "all") {
      return encodeURIComponent(column) + "=all";
    }
    return (
      encodeURIComponent(column) +
      "=" +
      values.map(encodeURIComponent).join(",")
    );
  }

  function comboDeepLink(combo) {
    const parts = [];
    Object.keys(combo.filters || {}).forEach(function (column) {
      const spec = combo.filters[column];
      parts.push(encodeFilterParam(column, spec.values || []));
    });
    return "#list?f=" + parts.join(";");
  }

  function comboDeepLinkById(comboId) {
    const combos = window.AFKJ.state.counterFilterCombos || {};
    const combo = combos[comboId];
    if (!combo) {
      return "#";
    }
    return comboDeepLink(combo);
  }

  function parseListFilterHash() {
    const hash = location.hash || "";
    const match = hash.match(/^#list\?(?:.*&)?f=([^&#]+)/);
    if (!match) {
      const direct = hash.match(/^#list\?f=([^#]+)/);
      if (!direct) {
        return null;
      }
      return parseFilterQuery(direct[1]);
    }
    return parseFilterQuery(match[1]);
  }

  function parseFilterQuery(raw) {
    const decoded = decodeURIComponent(raw);
    const result = {};
    decoded.split(";").forEach(function (pair) {
      if (!pair) {
        return;
      }
      const eq = pair.indexOf("=");
      if (eq === -1) {
        return;
      }
      const column = decodeURIComponent(pair.slice(0, eq));
      const valPart = pair.slice(eq + 1);
      const values = valPart.split(",").map(decodeURIComponent);
      result[column] = values;
    });
    return Object.keys(result).length ? result : null;
  }

  function resolveFilterValues(column, colIdx, values) {
    if (values.length === 1 && values[0] === "all") {
      return allOptionsForColumn(colIdx);
    }
    return values.slice();
  }

  function legacyEffectColumnAlias(column) {
    const meta = (window.AFKJ.state.listColumnsById || {})[column];
    if (!meta || !meta.label) {
      return null;
    }
    if (meta.group === "buff" || meta.polarity === "buff") {
      return { column: "Buffs", effect: meta.label };
    }
    if (meta.group === "debuff" || meta.polarity === "debuff") {
      return { column: "Debuffs", effect: meta.label };
    }
    return null;
  }

  function expandLegacyFilterMap(filterMap) {
    const expanded = {};
    Object.keys(filterMap || {}).forEach(function (column) {
      const values = filterMap[column] || [];
      const alias = legacyEffectColumnAlias(column);
      if (alias) {
        if (!expanded[alias.column]) {
          expanded[alias.column] = [];
        }
        expanded[alias.column].push(alias.effect);
        if (!(values.length === 1 && values[0] === "all")) {
          values.forEach(function (value) {
            if (value) {
              expanded[alias.column].push(value);
            }
          });
        }
        return;
      }
      if (!expanded[column]) {
        expanded[column] = [];
      }
      values.forEach(function (value) {
        expanded[column].push(value);
      });
    });
    Object.keys(expanded).forEach(function (column) {
      const seen = {};
      expanded[column] = expanded[column].filter(function (value) {
        if (!value || seen[value]) {
          return false;
        }
        seen[value] = true;
        return true;
      });
    });
    return expanded;
  }

  function applyListFilterMap(filterMap) {
    const state = window.AFKJ.state;
    state.csvColumnFilters = {};
    state.csvColumnFilterCombine = {};
    const expanded = expandLegacyFilterMap(filterMap);
    Object.keys(expanded).forEach(function (column) {
      const colIdx = columnIndex(column);
      if (colIdx === -1) {
        return;
      }
      const resolved = resolveFilterValues(column, colIdx, expanded[column]);
      if (!resolved.length) {
        return;
      }
      state.csvColumnFilters[colIdx] = resolved;
      if (column === "Behavior tags" && expanded[column].length > 1) {
        state.csvColumnFilterCombine[colIdx] = "and";
      }
    });
    state.viewMode = "list";
    try {
      localStorage.setItem(window.AFKJ.config.VIEW_MODE_KEY, "list");
    } catch (e) {
      /* ignore quota / private-mode errors */
    }
    if (window.AFKJ.main && window.AFKJ.main.syncViewToggleButtons) {
      window.AFKJ.main.syncViewToggleButtons();
    }
  }

  function applyComboFilters(combo) {
    const filterMap = {};
    Object.keys(combo.filters || {}).forEach(function (column) {
      const spec = combo.filters[column];
      filterMap[column] = (spec.values || []).slice();
      if (column === "Behavior tags" && spec.combine === "and") {
        /* combine mode set after apply via explicit flag */
      }
    });
    applyListFilterMap(filterMap);
    Object.keys(combo.filters || {}).forEach(function (column) {
      const spec = combo.filters[column];
      if (column === "Behavior tags" && spec.combine === "and") {
        const colIdx = columnIndex(column);
        if (colIdx !== -1) {
          window.AFKJ.state.csvColumnFilterCombine[colIdx] = "and";
        }
      }
    });
  }

  function tryApplyPendingListFilters() {
    const state = window.AFKJ.state;
    if (!state.pendingListFilterMap || !state.csvHeaders.length) {
      return false;
    }
    applyListFilterMap(state.pendingListFilterMap);
    state.pendingListFilterMap = null;
    return true;
  }

  function isListFilterHash() {
    return /^#list(?:\?|$)/.test(location.hash || "");
  }

  window.AFKJ.listFilters = {
    columnIndex: columnIndex,
    allOptionsForColumn: allOptionsForColumn,
    comboDeepLink: comboDeepLink,
    comboDeepLinkById: comboDeepLinkById,
    parseListFilterHash: parseListFilterHash,
    parseFilterQuery: parseFilterQuery,
    expandLegacyFilterMap: expandLegacyFilterMap,
    applyListFilterMap: applyListFilterMap,
    applyComboFilters: applyComboFilters,
    tryApplyPendingListFilters: tryApplyPendingListFilters,
    isListFilterHash: isListFilterHash,
  };
})();
