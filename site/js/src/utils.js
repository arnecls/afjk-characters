window.AFKJ = window.AFKJ || {};

window.AFKJ.utils = {
  inferBase: function () {
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
  },

  resolveBase: function () {
    if (location.protocol === "file:") {
      return this.inferBase();
    }
    const meta = document.querySelector('meta[name="github-pages-base"]');
    const configured = meta && meta.content;
    if (configured && location.pathname.startsWith(configured)) {
      return configured;
    }
    return this.inferBase();
  },

  isLocalFile: function () {
    return location.protocol === "file:";
  },

  assetUrl: function (relative) {
    if (this.isLocalFile()) {
      return relative;
    }
    return window.AFKJ.state.BASE + relative;
  },

  heroHash: function (slug) {
    return "#hero/" + encodeURIComponent(slug);
  },

  heroUrl: function (slug) {
    if (this.isLocalFile()) {
      return this.heroHash(slug);
    }
    return window.AFKJ.state.BASE + this.heroHash(slug);
  },

  homeUrl: function () {
    if (this.isLocalFile()) {
      return location.pathname;
    }
    return window.AFKJ.state.BASE;
  },

  slugFromLocation: function () {
    const hashMatch = location.hash.match(/^#hero\/([^/?#]+)/);
    if (hashMatch) {
      return decodeURIComponent(hashMatch[1]);
    }
    const path = location.pathname;
    const prefix = window.AFKJ.state.BASE.replace(/\/$/, "");
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
  },

  redirectLegacyHeroPath: function () {
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
    history.replaceState(null, "", base + this.heroHash(decodeURIComponent(slug)));
  },

  iconPath: function (kind, value) {
    if (!value) return null;
    const fname = value.toLowerCase().replace(/\s+/g, "");
    return "assets/icons/" + kind + "/" + fname + ".png";
  },

  characterPortraitPath: function (hero) {
    if (!hero || !hero.name) {
      return null;
    }
    return "assets/portraits/" + hero.name + ".png";
  },

  factionDataKey: function (faction) {
    if (!faction) {
      return "";
    }
    return faction.toLowerCase().replace(/\s+/g, "");
  },

  CELESTIAL_HYPOGEAN_BONUS_KEY: "celestialhypogean",

  factionBonusGroupKey: function (faction) {
    const key = this.factionDataKey(faction);
    if (key === "celestial" || key === "hypogean") {
      return this.CELESTIAL_HYPOGEAN_BONUS_KEY;
    }
    return key;
  },

  factionClass: function (faction) {
    if (!faction) return "";
    return "badge-faction-" + faction.toLowerCase().replace(/\s+/g, "");
  },

  escapeHtml: function (text) {
    if (typeof text !== "string") return "";
    return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  },

  linkifyHero: function (name, slug) {
    const state = window.AFKJ.state;
    if (slug && state.heroBySlug[slug]) {
      return (
        '<a href="' +
        this.escapeHtml(this.heroUrl(slug)) +
        '" class="hero-link" data-slug="' +
        this.escapeHtml(slug) +
        '">' +
        this.escapeHtml(name) +
        "</a>"
      );
    }
    return this.escapeHtml(name);
  },

  rectContainsPoint: function (rect, x, y, pad) {
    return (
      x >= rect.left - pad &&
      x <= rect.right + pad &&
      y >= rect.top - pad &&
      y <= rect.bottom + pad
    );
  }
};
