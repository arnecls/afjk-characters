window.AFKJ = window.AFKJ || {};

(function () {
  const config = window.AFKJ.config;
  const utils = window.AFKJ.utils;
  const escapeHtml = utils.escapeHtml.bind(utils);

  const FILTERS_COLLAPSE_MQ = window.matchMedia("(max-width: 600px)");

  function updateListStickyOffset() {
    const dom = window.AFKJ.state.dom;
    if (!dom.siteHeader) {
      return;
    }
    const offset = dom.siteHeader.offsetHeight;
    document.documentElement.style.setProperty(
      "--list-sticky-top",
      offset + "px"
    );
    if (dom.listView) {
      dom.listView.style.setProperty("--list-sticky-offset", offset + "px");
    }
  }

  function updateHeaderNav(inDetail) {
    const state = window.AFKJ.state;
    const dom = state.dom;
    if (dom.filtersPanel) {
      dom.filtersPanel.classList.toggle(
        "hidden",
        inDetail || state.viewMode === "list"
      );
    }
    if (dom.headerBack) {
      dom.headerBack.classList.toggle("hidden", !inDetail);
    }
    updateListStickyOffset();
  }

  function updateFiltersToggleLabel() {
    const state = window.AFKJ.state;
    const dom = state.dom;
    if (!dom.filtersToggle) {
      return;
    }
    const collapsed = dom.filtersPanel
      ? dom.filtersPanel.classList.contains("filters-collapsed")
      : false;
    const parts = [];
    if (state.activeFaction) {
      parts.push(state.activeFaction);
    }
    if (state.activeClass) {
      parts.push(state.activeClass);
    }
    if (state.activeRole) {
      const roleMeta = window.AFKJ.config.ROLE_CATEGORY_META[state.activeRole];
      parts.push(roleMeta ? roleMeta.label : state.activeRole);
    }
    const action = collapsed ? "Show filters" : "Hide filters";
    const activeSuffix = parts.length ? " (" + parts.join(", ") + ")" : "";
    const label = action + activeSuffix;
    dom.filtersToggle.title = action;
    dom.filtersToggle.setAttribute("aria-label", label);
    if (dom.filtersToggleLabel) {
      dom.filtersToggleLabel.textContent = label;
    }
  }

  function setFiltersCollapsed(collapsed) {
    const dom = window.AFKJ.state.dom;
    if (!dom.filtersPanel || !dom.filtersToggle) {
      return;
    }
    dom.filtersPanel.classList.toggle("filters-collapsed", collapsed);
    dom.filtersToggle.setAttribute("aria-expanded", collapsed ? "false" : "true");
    updateFiltersToggleLabel();
    updateListStickyOffset();
  }

  function initFiltersCollapse() {
    const dom = window.AFKJ.state.dom;
    if (!dom.filtersPanel || !dom.filtersToggle) {
      return;
    }
    setFiltersCollapsed(FILTERS_COLLAPSE_MQ.matches);
    dom.filtersToggle.addEventListener("click", function () {
      setFiltersCollapsed(
        !dom.filtersPanel.classList.contains("filters-collapsed")
      );
    });
    FILTERS_COLLAPSE_MQ.addEventListener("change", function () {
      setFiltersCollapsed(FILTERS_COLLAPSE_MQ.matches);
    });
  }

  function initWelcomeWarning() {
    const state = window.AFKJ.state;
    const dom = state.dom;
    const root = document.getElementById("welcome-warning");
    if (!root) {
      return;
    }
    if (localStorage.getItem(config.WELCOME_WARNING_KEY) === "1") {
      root.hidden = true;
      document.documentElement.classList.remove("welcome-warning-pending");
      return;
    }

    const dismissBtn = document.getElementById("welcome-warning-dismiss");
    const blocked = [
      dom.siteHeader,
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
        localStorage.setItem(config.WELCOME_WARNING_KEY, "1");
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

  function initChipTooltips() {
    const TIP_CHIP_SELECTOR = "[data-tip].chip-has-tip, [data-tip-html].chip-has-tip, .tier-chip[data-tip]";
    const chipTooltip = document.createElement("div");
    chipTooltip.id = "chip-tooltip";
    chipTooltip.className = "chip-tooltip";
    chipTooltip.hidden = true;
    chipTooltip.setAttribute("role", "tooltip");
    document.body.appendChild(chipTooltip);

    let tipAnchor = null;
    let tipHideTimer = null;
    const hoverCapable = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

    function tipChipFromEvent(e) {
      return e.target.closest(TIP_CHIP_SELECTOR);
    }

    function positionChipTooltip(anchor) {
      const rect = anchor.getBoundingClientRect();
      chipTooltip.style.left = rect.left + rect.width / 2 + "px";
      chipTooltip.style.top = rect.top - 8 + "px";
    }

    function showChipTooltip(anchor) {
      const html = anchor.getAttribute("data-tip-html");
      const text = anchor.getAttribute("data-tip");
      if (!html && !text) {
        return;
      }
      clearTimeout(tipHideTimer);
      if (tipAnchor && tipAnchor !== anchor) {
        tipAnchor.classList.remove("chip-tip-active");
      }
      tipAnchor = anchor;
      anchor.classList.add("chip-tip-active");
      if (html) {
        chipTooltip.innerHTML = html;
        chipTooltip.classList.add("chip-tooltip--html");
      } else {
        chipTooltip.textContent = text;
        chipTooltip.classList.remove("chip-tooltip--html");
      }
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
        const touchLike = e.pointerType === "touch" || !hoverCapable;
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
  }

  function initSkillCardPopover() {
    const state = window.AFKJ.state;
    const popoverModule = window.AFKJ.skills;

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

    function viewportMetrics() {
      const viewport = window.visualViewport;
      if (!viewport) {
        return {
          top: 0,
          left: 0,
          width: window.innerWidth,
          height: window.innerHeight,
        };
      }
      return {
        top: viewport.offsetTop,
        left: viewport.offsetLeft,
        width: viewport.width,
        height: viewport.height,
      };
    }

    function clearPopoverLayout() {
      popover.style.top = "";
      popover.style.left = "";
      popover.style.width = "";
      popover.style.height = "";
      popover.style.maxHeight = "";
      popover.style.visibility = "";
    }

    function positionSkillPopover(card) {
      const cardRect = card.getBoundingClientRect();
      const offset = 20;
      const viewMargin = 8;
      const view = viewportMetrics();
      const isNarrow = view.width <= 600;
      const heightCap = Math.min(view.height * (isNarrow ? 0.82 : 0.6), 420);

      popover.style.maxHeight = heightCap + "px";
      popover.style.visibility = "hidden";
      popover.hidden = false;

      const popW = popover.offsetWidth;
      const popH = popover.offsetHeight;
      const viewCenter = view.left + view.width / 2;
      const cardCenter = cardRect.left + cardRect.width / 2;
      const alignRight = cardCenter >= viewCenter;

      let left;
      let top = cardRect.bottom - offset - popH;
      if (alignRight) {
        left = cardRect.right - offset - popW;
      } else {
        left = cardRect.left + offset;
      }

      const maxLeft = view.left + view.width - popW - viewMargin;
      left = Math.max(view.left + viewMargin, Math.min(left, maxLeft));
      top = Math.max(
        view.top + viewMargin,
        Math.min(top, view.top + view.height - popH - viewMargin)
      );

      popover.style.top = top + "px";
      popover.style.left = left + "px";
      popover.style.visibility = "";
    }

    function hideSkillPopover() {
      if (anchorCard) {
        setCardExpanded(anchorCard, false);
      }
      popover.hidden = true;
      backdrop.hidden = true;
      anchorCard = null;
      clearPopoverLayout();
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
      popover.innerHTML = popoverModule.formatSkillDetail(cardData);
      backdrop.hidden = false;
      popover.hidden = false;
      setCardExpanded(card, true);
      positionSkillPopover(card);
    }

    state.closeSkillCardPopover = hideSkillPopover;

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
      const data = popoverModule.skillCardData(card.dataset.skillCategory);
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

    if (window.visualViewport) {
      window.visualViewport.addEventListener("resize", function () {
        if (anchorCard && !popover.hidden) {
          positionSkillPopover(anchorCard);
        }
      });
      window.visualViewport.addEventListener("scroll", function () {
        if (anchorCard && !popover.hidden) {
          positionSkillPopover(anchorCard);
        }
      });
    }
  }

  function initThemeToggle() {
    const theme = window.AFKJ.theme;
    const dom = window.AFKJ.state.dom;
    const input = dom.themeToggle;
    if (!input) {
      return;
    }

    theme.syncToggleControl(input);

    input.addEventListener("change", function () {
      const next = input.checked ? "dark" : "light";
      theme.applyThemeOverride(next);
      theme.syncToggleControl(input);
    });

    const colorMq = window.matchMedia("(prefers-color-scheme: dark)");
    colorMq.addEventListener("change", function () {
      if (!theme.readStoredThemeOverride()) {
        theme.syncToggleControl(input);
      }
    });
  }

  // Export module API to window.AFKJ.ui
  window.AFKJ.ui = {
    updateListStickyOffset: updateListStickyOffset,
    updateHeaderNav: updateHeaderNav,
    updateFiltersToggleLabel: updateFiltersToggleLabel,
    setFiltersCollapsed: setFiltersCollapsed,
    initFiltersCollapse: initFiltersCollapse,
    initWelcomeWarning: initWelcomeWarning,
    initChipTooltips: initChipTooltips,
    initSkillCardPopover: initSkillCardPopover,
    initThemeToggle: initThemeToggle,
  };
})();
