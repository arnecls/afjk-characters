window.AFKJ = window.AFKJ || {};

window.AFKJ.theme = {
  readStoredThemeOverride: function () {
    const key = window.AFKJ.config.THEME_OVERRIDE_KEY;
    try {
      const stored = sessionStorage.getItem(key);
      if (stored === "light" || stored === "dark") {
        return stored;
      }
    } catch (e) {
      /* ignore quota / private-mode errors */
    }
    return null;
  },

  storeThemeOverride: function (theme) {
    const key = window.AFKJ.config.THEME_OVERRIDE_KEY;
    try {
      sessionStorage.setItem(key, theme);
    } catch (e) {
      /* ignore quota / private-mode errors */
    }
  },

  systemPrefersDark: function () {
    return window.matchMedia("(prefers-color-scheme: dark)").matches;
  },

  getEffectiveTheme: function () {
    const override = this.readStoredThemeOverride();
    if (override) {
      return override;
    }
    return this.systemPrefersDark() ? "dark" : "light";
  },

  applyThemeOverride: function (theme) {
    const root = document.documentElement;
    if (theme === "light" || theme === "dark") {
      root.dataset.theme = theme;
      this.storeThemeOverride(theme);
      return;
    }
    delete root.dataset.theme;
  },

  syncToggleControl: function (input) {
    if (!input) {
      return;
    }
    const dark = this.getEffectiveTheme() === "dark";
    input.checked = dark;
    input.setAttribute("aria-checked", dark ? "true" : "false");
    input.title = dark ? "Switch to light mode" : "Switch to dark mode";
    input.setAttribute(
      "aria-label",
      dark ? "Dark mode on" : "Dark mode off"
    );
  },
};
