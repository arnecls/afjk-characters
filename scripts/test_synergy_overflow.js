#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.resolve(__dirname, "..");
const SRC = path.join(ROOT, "site", "js", "src");

function loadModule(relativePath) {
  const code = fs.readFileSync(path.join(SRC, relativePath), "utf8");
  vm.runInContext(code, context, { filename: relativePath });
}

const context = {
  window: {},
  document: {
    querySelector() {
      return null;
    },
    createElement() {
      return { setAttribute() {}, appendChild() {} };
    },
  },
  location: { pathname: "/", protocol: "file:" },
  console,
};
context.window = context;
vm.createContext(context);

[
  "namespace.js",
  "utils.js",
  "config.js",
  "chips.js",
  "skills.js",
  "tiers.js",
  "views-grid.js",
  "views-detail.js",
].forEach(loadModule);

const renderOverflow =
  context.window.AFKJ.views.detail.renderSynergyPartnerOverflow;
if (typeof renderOverflow !== "function") {
  console.error("renderSynergyPartnerOverflow not found");
  process.exit(1);
}

function partner(name, scoreRating) {
  return { name, scoreRating };
}

function decodeTooltipHtml(html) {
  const match = html.match(/data-tip-html="([^"]*)"/);
  if (!match) {
    return "";
  }
  return match[1]
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&amp;/g, "&");
}

function assertIncludes(label, html, needle) {
  if (!html.includes(needle)) {
    throw new Error(
      `${label}: expected ${JSON.stringify(needle)} in ${html}`
    );
  }
}

function assertNotIncludes(label, html, needle) {
  if (html.includes(needle)) {
    throw new Error(
      `${label}: did not expect ${JSON.stringify(needle)} in ${html}`
    );
  }
}

let failed = 0;

function runCase(label, fn) {
  try {
    fn();
  } catch (err) {
    failed += 1;
    console.error(`${label}: ${err.message}`);
  }
}

runCase("singular small overflow", function () {
  const html = renderOverflow([partner("Rowan", 1.2)]);
  assertIncludes("singular", html, "There were ");
  assertIncludes("singular", html, "1 more unit");
  assertIncludes("singular", html, "detected.");
  assertNotIncludes("singular", html, "score higher");
  const tip = decodeTooltipHtml(html);
  assertIncludes("singular tip", tip, "Rowan");
});

runCase("plural small overflow", function () {
  const html = renderOverflow([
    partner("Rowan", 1.2),
    partner("Lyca", 1.1),
    partner("Thador", 1.0),
  ]);
  assertIncludes("plural", html, "3 more units");
  assertNotIncludes("plural", html, "score higher");
  const tip = decodeTooltipHtml(html);
  assertIncludes("plural tip", tip, "Rowan");
  assertIncludes("plural tip", tip, "Lyca");
  assertIncludes("plural tip", tip, "Thador");
});

runCase("five partner boundary uses simple wording", function () {
  const partners = [
    partner("A", 1.0),
    partner("B", 1.0),
    partner("C", 1.0),
    partner("D", 1.0),
    partner("E", 1.0),
  ];
  const html = renderOverflow(partners);
  assertIncludes("five", html, "5 more units");
  assertNotIncludes("five", html, "score higher");
});

runCase("six partner overflow keeps score summary", function () {
  const partners = [
    partner("A", 3.0),
    partner("B", 1.0),
    partner("C", 1.0),
    partner("D", 1.0),
    partner("E", 1.0),
    partner("F", 1.0),
  ];
  const html = renderOverflow(partners);
  assertIncludes("six", html, "6 more units detected of which ");
  assertIncludes("six", html, "1 score higher");
  assertIncludes("six", html, "than 2.");
  const tip = decodeTooltipHtml(html);
  assertIncludes("six tip", tip, "A");
  assertNotIncludes("six tip", tip, "B");
});

runCase("large overflow with no high-rated partners", function () {
  const partners = Array.from({ length: 7 }, function (_, i) {
    return partner(`Hero${i}`, 1.0);
  });
  const html = renderOverflow(partners);
  assertIncludes("large none", html, "0 score higher than 2.");
});

if (failed) {
  process.exit(1);
}

console.log("synergy overflow tests passed");
