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
      return { setAttribute() { }, appendChild() { } };
    },
  },
  location: { pathname: "/", protocol: "file:" },
  console,
};
context.window = context;
vm.createContext(context);

loadModule("namespace.js");
loadModule("utils.js");
loadModule("config.js");
loadModule("chips.js");
loadModule("skills.js");

const chipify = context.window.AFKJ.chips.chipifySkillCardTag;
const renderSkillCardTags =
  context.window.AFKJ.skills.renderSkillCardTags;
if (typeof chipify !== "function") {
  console.error("chipifySkillCardTag not found");
  process.exit(1);
}

function assertTargetingRendered(label, polarity, needles) {
  const html = chipify(label, polarity);
  if (!html) {
    throw new Error(`empty chip html for ${label}`);
  }
  const expected = Array.isArray(needles) ? needles : [needles];
  for (const needle of expected) {
    if (!html.includes(needle)) {
      throw new Error(
        `expected ${JSON.stringify(needle)} in chip html for ${label}: ${html}`
      );
    }
  }
}

const singleTargetCases = [
  ["Phys DEF — Area", "debuff", ["⭕", "Area"]],
  ["ATK — Self (EX+10)", "buff", ["🪞", "Self"]],
  ["Lifedrain — Multiple targets", "buff", ["👥", "multiple"]],
  ["Blind — Area (EX+15)", "", ["⭕", "Area"]],
  ["Direct healing — Self (Supreme+)", "buff", ["🪞", "Self"]],
  ["Knock back — path", "cc", ["〰️", "path"]],
  ["Lifedrain — Owned", "buff", ["🐾", "owned"]],
];

let failed = 0;
for (const [label, polarity, needles] of singleTargetCases) {
  try {
    assertTargetingRendered(label, polarity, needles);
  } catch (err) {
    failed += 1;
    console.error(err.message);
  }
}

const multiTargetHtml = renderSkillCardTags([
  { label: "ATK SPD — Self", polarity: "buff" },
  { label: "ATK SPD — Owned", polarity: "buff" },
]);
if (!multiTargetHtml.includes("🪞") || !multiTargetHtml.includes("🐾")) {
  failed += 1;
  console.error(
    "expected grouped multi-target pill to include Self and owned icons"
  );
}
if (multiTargetHtml.includes(">Self<") || />\s*owned\s*</i.test(multiTargetHtml)) {
  failed += 1;
  console.error(
    "expected grouped multi-target pill to omit targeting text labels"
  );
}

const stunHtml = renderSkillCardTags([
  { label: "Stun — All units", polarity: "cc" },
  { label: "Stun — Multiple targets", polarity: "cc" },
  { label: "Stun — Single target", polarity: "cc" },
]);
if (!stunHtml.includes("🌐") || !stunHtml.includes("👥") || !stunHtml.includes("🎯")) {
  failed += 1;
  console.error("expected grouped stun pill to include all targeting icons");
}
if (
  stunHtml.includes(">all<") ||
  stunHtml.includes(">multiple<") ||
  stunHtml.includes(">single<")
) {
  failed += 1;
  console.error(
    "expected grouped stun pill to omit short targeting text labels"
  );
}

if (failed) {
  process.exit(1);
}

const walkCases = [
  ["stationary", "slow", ["chip-merged", "chip-movement", "chip-s-slow", "slow"]],
  ["moving", "normal", ["chip-merged", "chip-s-normal", "normal"]],
  ["mostly stationary", "fast", ["chip-merged", "chip-s-fast", "fast"]],
  ["high movement", "zero", ["chip-merged", "chip-s-slow", "zero"]],
  ["moving / stationary", "veryfast", ["chip-merged", "chip-s-fast", "veryfast"]],
];
for (const [movement, walk, needles] of walkCases) {
  try {
    const html = context.window.AFKJ.chips.mergeMovementWithWalkSpeed(
      movement,
      walk
    );
    if (!html) {
      throw new Error(`empty merge for ${movement} | ${walk}`);
    }
    for (const needle of needles) {
      if (!html.includes(needle)) {
        throw new Error(
          `expected ${JSON.stringify(needle)} in ${movement} | ${walk}: ${html}`
        );
      }
    }
  } catch (err) {
    failed += 1;
    console.error(err.message);
  }
}

if (failed) {
  process.exit(1);
}
console.log(
  `OK: ${singleTargetCases.length} single-target, 2 multi-target, and ${walkCases.length} walk-speed checks`
);
