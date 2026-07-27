window.AFKJ = window.AFKJ || {};

(function () {
  const utils = window.AFKJ.utils;
  const config = window.AFKJ.config;
  const chips = window.AFKJ.chips;
  const tiers = window.AFKJ.tiers;
  const skills = window.AFKJ.skills;
  const markdown = window.AFKJ.markdown;
  const gridView = window.AFKJ.views.grid;
  const escapeHtml = utils.escapeHtml.bind(utils);

  const BENEFIT_MAX_STARS = 5;
  const BENEFIT_MIN_STARS = 1;
  const BENEFIT_STAR = "⭐";

  function clampBenefitRating(scoreRating) {
    const rating = Number(scoreRating);
    if (!isFinite(rating)) {
      return 0;
    }
    return Math.max(
      BENEFIT_MIN_STARS,
      Math.min(BENEFIT_MAX_STARS, rating)
    );
  }

  function boxedRatingIconCount(rating) {
    const clamped = clampBenefitRating(rating);
    if (!clamped) {
      return 0;
    }
    return Math.max(
      BENEFIT_MIN_STARS,
      Math.min(BENEFIT_MAX_STARS, Math.round(clamped))
    );
  }

  function renderCompactRatingIcons(filledCount, glyph) {
    const emptyCount = BENEFIT_MAX_STARS - filledCount;
    let html = "";
    for (let i = 0; i < BENEFIT_MAX_STARS; i++) {
      if (i < emptyCount) {
        html +=
          '<span class="compact-rating-icon compact-rating-icon--empty" aria-hidden="true"></span>';
      } else {
        html +=
          '<span class="compact-rating-icon" aria-hidden="true">' +
          glyph +
          "</span>";
      }
    }
    return html;
  }

  function renderBoxedCompactScore(filledCount, glyph, tooltip, modifierClass) {
    if (!filledCount || !glyph) {
      return "";
    }
    const classes = "hero-compact-score hero-compact-score--boxed";
    return (
      '<div class="' +
      classes +
      (modifierClass ? " " + modifierClass : "") +
      '" title="' +
      escapeHtml(tooltip) +
      '" aria-label="' +
      escapeHtml(tooltip) +
      '">' +
      renderCompactRatingIcons(filledCount, glyph) +
      "</div>"
    );
  }

  function formatBeneficiaryRatingDisplay(scoreRating) {
    const count = boxedRatingIconCount(scoreRating);
    if (!count) {
      return "";
    }
    return BENEFIT_STAR.repeat(count);
  }

  function beneficiaryScoreTooltip(scoreRating) {
    const clamped = clampBenefitRating(scoreRating);
    if (!clamped) {
      return "Benefit rating out of 5";
    }
    return "Benefit rating: " + clamped.toFixed(1) + " out of 5";
  }

  function renderBeneficiaryScore(scoreRating) {
    const count = boxedRatingIconCount(scoreRating);
    return renderBoxedCompactScore(
      count,
      BENEFIT_STAR,
      beneficiaryScoreTooltip(scoreRating)
    );
  }

  function replacementScoreRating(score) {
    const value = Number(score);
    if (!isFinite(value) || value <= 0) {
      return BENEFIT_MIN_STARS;
    }
    return Math.max(
      BENEFIT_MIN_STARS,
      Math.min(BENEFIT_MAX_STARS, BENEFIT_MIN_STARS + (BENEFIT_MAX_STARS - BENEFIT_MIN_STARS) * value)
    );
  }

  function replacementRatingIconCount(score) {
    return boxedRatingIconCount(replacementScoreRating(score));
  }

  function replacementScoreTooltip(score) {
    const value = Number(score);
    if (!isFinite(value)) {
      return "Replacement fit";
    }
    return "Replacement fit: " + Math.round(value * 100) + "%";
  }

  function renderReplacementScore(score, categoryLabel) {
    const icon = replacementCategoryIcon(categoryLabel);
    const count = replacementRatingIconCount(score);
    const glyph = icon || "•";
    return renderBoxedCompactScore(
      count,
      glyph,
      replacementScoreTooltip(score),
      "hero-compact-score--replacement"
    );
  }

  function renderHeroCompactCard(slug, name, bodyHtml, footerHtml, headerHtml) {
    const hero = window.AFKJ.state.heroBySlug[slug];
    const factionKey = hero ? utils.factionDataKey(hero.faction) : "";
    const portraitHero = hero || { name: name, faction: "" };
    const portraitHtml = gridView.renderHeroPortrait(
      portraitHero,
      "compact-portrait"
    );
    return (
      '<article class="hero-compact-card afkj-box afkj-box-sm" data-slug="' +
      escapeHtml(slug) +
      '" data-faction="' +
      escapeHtml(factionKey) +
      '" tabindex="0" role="link" aria-label="' +
      escapeHtml(name) +
      '">' +
      '<div class="hero-compact-portrait-wrap">' +
      portraitHtml +
      "</div>" +
      '<div class="hero-compact-body">' +
      '<div class="hero-compact-header">' +
      '<div class="hero-compact-name">' +
      utils.linkifyHero(name, slug) +
      "</div>" +
      (headerHtml || "") +
      "</div>" +
      (bodyHtml || "") +
      (footerHtml || "") +
      "</div></article>"
    );
  }

  function renderHeroRowCard(slug, name, bodyHtml) {
    const hero = window.AFKJ.state.heroBySlug[slug];
    const portraitSrc = utils.assetUrl(
      utils.characterPortraitPath(hero || { name: name })
    );
    return (
      '<article class="hero-row-card" data-slug="' +
      escapeHtml(slug) +
      '" tabindex="0" role="link" aria-label="' +
      escapeHtml(name) +
      '">' +
      '<img src="' +
      escapeHtml(portraitSrc) +
      '" alt="" loading="lazy" onerror="this.style.opacity=0.3">' +
      '<div class="hero-row-body">' +
      '<div class="hero-row-name">' +
      utils.linkifyHero(name, slug) +
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
    const merged = chips.mergeEffectWithQuality(typeName, quality);
    if (merged) {
      return merged;
    }
    const typeChip = chips.tryChipify(typeName);
    const qualityChip = chips.formatTag(quality);
    return (
      (typeChip !== null ? typeChip : escapeHtml(typeName)) +
      " " +
      qualityChip
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
        return chips.renderInline(entry);
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
    for (let i = 0; i < chips.MOVEMENT_KEYS.length; i++) {
      const key = chips.MOVEMENT_KEYS[i];
      if (lower === key.toLowerCase()) {
        const def = chips.MOVEMENT_DEFINITIONS[key];
        return chips.chipSpan(def.emoji, trimmed, def.cls);
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
    let rest = match[1].trim();
    let walkSpeed = "";
    const walkMatch = rest.match(/;\s*walk speed\s+(\S+)\s*$/i);
    if (walkMatch) {
      walkSpeed = walkMatch[1].trim();
      rest = rest.slice(0, walkMatch.index).trim();
    }
    const paren = rest.match(/^(.+?)\s*(\([^)]+\))\s*$/);
    const base = paren ? paren[1].trim() : rest;
    const suffix = paren ? " " + escapeHtml(paren[2]) : "";
    let chip = null;
    if (walkSpeed) {
      chip = chips.mergeMovementWithWalkSpeed(base, walkSpeed);
    }
    if (!chip) {
      chip = formatMovementChip(base);
    }
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
    const tagChips = tags
      .map(function (raw) {
        return chips.behaviorTagChip(raw.slice(1, -1), true);
      })
      .join(" ");
    return formatSkillOverviewRow(
      "<strong>Behavior tags</strong>",
      '<span class="behavior-tags-cell">' + tagChips + "</span>"
    );
  }

  function renderSkillOverviewMetric(text) {
    const trimmed = text.trim();
    const parsed = parseSkillOverviewMetricEntry(trimmed);
    if (!parsed) {
      return chips.renderInline(trimmed);
    }
    const labelParts = chips.parseEffectLabelParts(parsed.label);
    if (chips.isSpeedMetricLabel(labelParts.base)) {
      return (
        chips.mergeLabelWithIndicator(
          labelParts.base,
          parsed.value,
          labelParts.tier
        ) ||
        chips.renderSummaryEffectChip(
          labelParts.base,
          labelParts.tier,
          parsed.value
        )
      );
    }
    return (
      chips.mergeEffectWithQuality(
        labelParts.base,
        parsed.value,
        labelParts.tier
      ) ||
      chips.mergeLabelWithIndicator(
        labelParts.base,
        parsed.value,
        labelParts.tier
      ) ||
      chips.renderSummaryEffectChip(
        labelParts.base,
        labelParts.tier,
        parsed.value
      )
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
        const parsedSegments = segments.map(function (segment) {
          return parseSkillOverviewMetricEntry(segment.trim());
        });
        const speedEntry = parsedSegments.find(function (entry) {
          return entry && entry.label.trim().toLowerCase() === "speed";
        });
        const filteredSegments = segments.filter(function (segment) {
          const entry = parseSkillOverviewMetricEntry(segment.trim());
          if (
            entry &&
            entry.label.trim().toLowerCase() === "first cast speed" &&
            speedEntry &&
            entry.value.toLowerCase() === speedEntry.value.toLowerCase()
          ) {
            return false;
          }
          return true;
        });
        const pills = filteredSegments.map(function (segment) {
          return renderSkillOverviewMetric(segment);
        });
        return formatSkillOverviewRow(
          chips.renderInline(colonMatch[1].trim().replace(/:\s*$/, "")),
          pills.join("")
        );
      }
    }

    return chips.renderInline(text);
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
        chips.renderInline(colonMatch[2].trim())
      );
    }
    return chips.renderInline(text);
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
    "all summons": true,
    "owned summons": true,
    "summons only": true,
  };

  const SYNERGY_QUALITY_TOKENS = {
    low: true,
    average: true,
    high: true,
  };

  // "<stat> via <buff>" reasons collapse to the effect pill alone, because the
  // stat and the buff say the same thing. These lead-ins carry extra meaning
  // the pill cannot express, so they survive rendering.
  const SYNERGY_KEPT_REASON_PREFIXES = {
    "enemy defense": true,
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
    return {
      label: label,
      quality: quality,
      conditional: conditional,
      modifiers: modifiers,
    };
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
    let text = chips.normalizeSummaryText(reason);
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
      const prefix = text.slice(0, viaIdx).trim().toLowerCase();
      if (SYNERGY_KEPT_REASON_PREFIXES[prefix]) {
        return {
          type: "enable",
          text: stripSynergyReasonTargeting(text),
        };
      }
      text = text.slice(viaIdx + 5).trim();
    }

    const detail = splitSynergyReasonDetail(text);
    const parsed = chips.parseEffectLabelParts(detail.label);
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
    const direct = chips.tryChipify(text);
    if (direct) {
      return direct;
    }
    return escapeHtml(text);
  }

  function chipifySynergyEnableDetail(text) {
    const detail = splitSynergyReasonDetail(text);
    const parsed = chips.parseEffectLabelParts(detail.label);
    const parts = parsed.base.split(/\s+\+\s+/);

    function renderPart(part, applyQuality) {
      const partParsed = chips.parseEffectLabelParts(part.trim());
      const polarity = chips.effectLabelPolarity(partParsed.base) || "buff";
      return chips.renderMergedEffectPill(
        partParsed.base,
        applyQuality ? detail.quality : "",
        applyQuality ? parsed.tier || partParsed.tier : partParsed.tier,
        applyQuality ? detail.conditional : "",
        polarity
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
      (enableMatch ? "Enables " : "") +
      chipifySynergyEnableLabel(enableLabel) +
      " via " +
      chipifySynergyEnableDetail(effect)
    );
  }

  function renderSynergyPartnerExplanation(reasons, options) {
    if (!reasons || !reasons.length) {
      return "";
    }
    options = options || {};
    const prioritizeSignatureFuel = !!options.prioritizeSignatureFuel;
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
      const hasSignatureFuel =
        prioritizeSignatureFuel &&
        effects.some(function (effect) {
          return effect.signatureFuel;
        });
      const pillsClass =
        "synergy-partner-pills" +
        (hasSignatureFuel ? " synergy-partner-pills-has-signature-fuel" : "");

      function renderEffectPill(effect, inlineSignatureFuel) {
        let pill = chips.renderMergedEffectPill(
          effect.base,
          effect.quality,
          effect.tier,
          ""
        );
        if (inlineSignatureFuel && effect.signatureFuel) {
          pill += " " + chips.formatTag("signature fuel");
        }
        return '<span class="synergy-partner-pill">' + pill + "</span>";
      }

      if (hasSignatureFuel) {
        const fuelEffects = effects.filter(function (effect) {
          return effect.signatureFuel;
        });
        const otherEffects = effects.filter(function (effect) {
          return !effect.signatureFuel;
        });
        html += '<div class="' + pillsClass + '">';
        html += '<div class="synergy-partner-fuel-row">';
        html +=
          '<span class="synergy-partner-signature-fuel">' +
          chips.formatTag("signature fuel") +
          "</span>";
        fuelEffects.forEach(function (effect) {
          html += renderEffectPill(effect, false);
        });
        html += "</div>";
        if (otherEffects.length) {
          html += '<div class="synergy-partner-other-pills">';
          otherEffects.forEach(function (effect) {
            html += renderEffectPill(effect, false);
          });
          html += "</div>";
        }
        html += "</div>";
      } else {
        html += '<div class="' + pillsClass + '">';
        effects.forEach(function (effect) {
          html += renderEffectPill(effect, true);
        });
        html += "</div>";
      }
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

  function synergyPartnerScoreRating(ref) {
    const rating =
      ref.scoreRating != null ? ref.scoreRating : ref.score_rating;
    const value = Number(rating);
    return Number.isFinite(value) ? value : 0;
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
      ref.scoreRating != null ? ref.scoreRating : ref.score_rating
    );
    return renderHeroCompactCard(
      ref.slug,
      ref.name,
      bodyHtml || "",
      "",
      scoreHtml
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
    const hero = window.AFKJ.state.heroBySlug[slug];
    const factionKey = hero ? utils.factionDataKey(hero.faction) : "";
    const portraitSrc = utils.assetUrl(
      utils.characterPortraitPath(hero || { name: name })
    );
    return (
      '<span class="inline-hero-hex" data-faction="' +
      escapeHtml(factionKey) +
      '" aria-hidden="true">' +
      '<span class="inline-hero-hex-wrap">' +
      '<span class="inline-hero-hex-inner">' +
      '<img class="inline-hero-hex-icon" src="' +
      escapeHtml(portraitSrc) +
      '" alt="" loading="lazy" onerror="this.style.opacity=0.3">' +
      "</span></span></span>"
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
    const chips = window.AFKJ.chips;
    const items = buffers.map(function (ref) {
      return chips.renderCharacterPill(ref.name);
    });
    return (
      '<div class="synergy-common-buffers">Common buffers are ' +
      joinIntroFragments(items) +
      ".</div>"
    );
  }

  function renderSynergyOverflowTooltipGrid(partners) {
    const names = partners
      .slice()
      .sort(function (a, b) {
        const ratingDiff =
          synergyPartnerScoreRating(b) - synergyPartnerScoreRating(a);
        if (ratingDiff !== 0) {
          return ratingDiff;
        }
        return a.name.localeCompare(b.name);
      })
      .map(function (ref) {
        return ref.name;
      });
    return (
      '<div class="synergy-overflow-tip-grid">' +
      names
        .map(function (name) {
          return "<span>" + escapeHtml(name) + "</span>";
        })
        .join("") +
      "</div>"
    );
  }

  function renderSynergyPartnerOverflow(morePartners) {
    if (!morePartners || !morePartners.length) {
      return "";
    }
    const overflowCount = morePartners.length;
    const unitLabel = overflowCount === 1 ? "unit" : "units";
    const moreUnitsPhrase = overflowCount + " more " + unitLabel;
    if (overflowCount <= 5) {
      return (
        '<p class="synergy-partner-overflow">There were ' +
        '<span class="synergy-overflow-trigger chip-has-tip" data-tip-html="' +
        escapeHtml(renderSynergyOverflowTooltipGrid(morePartners)) +
        '" tabindex="0" role="button" aria-describedby="chip-tooltip">' +
        moreUnitsPhrase +
        "</span> detected.</p>"
      );
    }
    const highRated = morePartners.filter(function (ref) {
      return synergyPartnerScoreRating(ref) > 2;
    });
    const highCount = highRated.length;
    let html =
      '<p class="synergy-partner-overflow">There were ' +
      overflowCount +
      " more " +
      unitLabel +
      " detected of which ";
    if (highCount > 0) {
      html +=
        '<span class="synergy-overflow-trigger chip-has-tip" data-tip-html="' +
        escapeHtml(renderSynergyOverflowTooltipGrid(highRated)) +
        '" tabindex="0" role="button" aria-describedby="chip-tooltip">' +
        highCount +
        " score higher</span>";
    } else {
      html += highCount + " score higher";
    }
    html += " than 2.</p>";
    return html;
  }

  function renderSynergies(sections, heroName) {
    const syn = sections.benefits_from;
    if (!syn) return "";

    let html = '<div class="detail-section synergy-section">';
    html += "<h2>Units improving " + escapeHtml(heroName) + "</h2>";

    if (syn.intro || (syn.common_buffers && syn.common_buffers.length)) {
      const introText = synergyIntroWithoutCommonBuffers(syn.intro);
      const buffersHtml = renderCommonBuffers(syn.common_buffers);
      if (introText || buffersHtml) {
        html += '<div class="synergy-intro-block">';
        if (introText) {
          html +=
            '<div class="synergy-intro">' +
            chips.renderInline(introText.replace(/\n/g, " ")) +
            "</div>";
        }
        html += buffersHtml;
        html += "</div>";
      }
    }

    if (syn.requires && syn.requires.text) {
      html +=
        '<div class="synergy-requires"><p>' +
        chips.renderInline(syn.requires.text) +
        "</p></div>";
    }

    if (syn.partners && syn.partners.length) {
      html += renderSynergyHeroGrid(syn.partners, function (partner) {
        return renderSynergyPartnerExplanation(partner.reasons, {
          prioritizeSignatureFuel: true,
        });
      });
      html += renderSynergyPartnerOverflow(syn.more_partners);
    } else {
      html += "<p><em>No synergy partners matched stat buffs or enablers.</em></p>";
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

  function renderBuffsProvidedIntro(data) {
    if (!data || !data.buffs || !data.buffs.length) {
      return "";
    }
    const entries = data.buffs.map(chips.renderBuffProvidedEntry);
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

    let html = '<div class="detail-section synergy-section synergy-benefited-by-section">';
    html += "<h2>Units benefitting most from " + escapeHtml(heroName) + "</h2>";

    if (buffsProvided) {
      html +=
        '<div class="synergy-intro">' +
        renderBuffsProvidedIntro(buffsProvided) +
        "</div>";
    } else if (bb.buffs_intro) {
      html +=
        '<div class="synergy-intro">' +
        chips.renderInline(bb.buffs_intro) +
        "</div>";
    }

    if (bb.intro) {
      html +=
        '<div class="synergy-intro">' +
        chips.renderInline(bb.intro.replace(/\n/g, " ")) +
        "</div>";
    }
    if (bb.overflow_reasons && bb.overflow_reasons.length) {
      html += "<ul>";
      bb.overflow_reasons.forEach(function (r) {
        html += "<li>" + chips.renderInline(r) + "</li>";
      });
      html += "</ul>";
    }
    if (bb.strongest_note) {
      html +=
        '<div class="synergy-intro">' +
        chips.renderInline(bb.strongest_note) +
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

  function replacementCategoryIcon(label) {
    return config.REPLACEMENT_CATEGORY_ICONS[label] || "";
  }

  function replacementCategoryClass(label) {
    const classes = {
      "Best overall replacement": "replacement-category--overall",
      "Buffs on allies": "replacement-category--buff",
      "Energy provider": "replacement-category--energy",
      Healing: "replacement-category--healing",
      "Similar Skills": "replacement-category--similar",
      Damage: "replacement-category--damage",
      "Debuffs on enemies": "replacement-category--debuff",
      "Crowd Control": "replacement-category--cc",
    };
    return classes[label] || "replacement-category--generic";
  }

  function renderReplacementCategoryHeading(label) {
    const icon = replacementCategoryIcon(label);
    if (!icon) {
      return "<h4>" + escapeHtml(label) + "</h4>";
    }
    return (
      "<h4>" +
      '<span class="replacement-category-icon" aria-hidden="true">' +
      icon +
      "</span> " +
      escapeHtml(label) +
      "</h4>"
    );
  }

  function renderReplacements(sections, mainHero) {
    const reps = sections.replacements;
    if (!reps || !reps.length) return "";

    let html = '<div class="detail-section">';
    html += "<h2>Replacement options</h2>";
    reps.forEach(function (cat) {
      html +=
        '<div class="replacement-category ' +
        replacementCategoryClass(cat.category) +
        '">';
      html += renderReplacementCategoryHeading(cat.category);
      html += renderHeroRowList(
        cat.entries.map(function (e) {
          let body = "";
          if (e.detail) {
            body =
              '<div class="hero-compact-detail">' +
              chips.renderInline(e.detail) +
              "</div>";
          }
          let footer = "";
          const repHero = window.AFKJ.state.heroBySlug[e.slug];
          if (repHero) {
            footer = tiers.renderPrydwenTierBoxes(
              tiers.getHeroPrydwenTiers(repHero),
              "compact",
              mainHero ? tiers.getHeroPrydwenTiers(mainHero) : null,
              mainHero && mainHero.name
            );
          }
          let header = "";
          if (e.score != null) {
            header = renderReplacementScore(e.score, cat.category);
          }
          return renderHeroCompactCard(e.slug, e.name, body, footer, header);
        }),
        "hero-compact-grid-3"
      );
      html += "</div>";
    });
    html += "</div>";
    return html;
  }

  function renderRoleCategoryIcon(roleCategory) {
    const icon = config.ROLE_CATEGORY_ICONS[roleCategory];
    if (!icon) {
      return "";
    }
    const parts = icon.viewBox.split(/\s+/).map(Number);
    const iconCx = parts[0] + parts[2] / 2;
    const iconCy = parts[1] + parts[3] / 2;
    const iconScale = 13.5 / Math.max(parts[2], parts[3]);
    return (
      '<span class="role-category-icon" aria-hidden="true">' +
      '<svg class="role-category-icon-svg" viewBox="0 0 24 24" focusable="false">' +
      '<circle class="role-category-icon-bg" cx="12" cy="12" r="10.5"/>' +
      '<g transform="translate(12 12) scale(' +
      iconScale +
      ") translate(" +
      -iconCx +
      " " +
      -iconCy +
      ')">' +
      '<path class="role-category-icon-shape" d="' +
      icon.path +
      '"/>' +
      "</g></svg></span>"
    );
  }

  function renderRoleCategoryBadge(heroOrCategory, options) {
    const key =
      typeof heroOrCategory === "string"
        ? heroOrCategory
        : heroOrCategory.roleCategory;
    const meta = window.AFKJ.tiers.roleCategoryMeta(key) || config.ROLE_CATEGORY_META[key];
    if (!meta) {
      return "";
    }
    const useSheetIcon = options && options.sheetIcon === true;
    const iconHtml = useSheetIcon
      ? renderRoleCategoryIcon(key)
      : '<span class="badge-emoji" aria-hidden="true">' +
      meta.emoji +
      "</span>";
    const badgeClass =
      meta.className + (useSheetIcon ? " badge-role-with-icon" : "");
    return (
      '<span class="badge ' +
      badgeClass +
      '">' +
      iconHtml +
      escapeHtml(meta.label) +
      "</span>"
    );
  }

  function renderBadges(hero, options) {
    const includeRoleCategory =
      options && options.includeRoleCategory === true;
    const badges = [];
    if (hero.faction) {
      const icon = utils.iconPath("factions", hero.faction);
      badges.push(
        '<span class="badge ' +
        utils.factionClass(hero.faction) +
        '">' +
        (icon
          ? '<img src="' + utils.assetUrl(icon) + '" alt="" loading="lazy">'
          : "") +
        escapeHtml(hero.faction) +
        "</span>"
      );
    }
    if (hero.class) {
      const icon = utils.iconPath("class", hero.class);
      badges.push(
        '<span class="badge">' +
        (icon
          ? '<img src="' + utils.assetUrl(icon) + '" alt="" loading="lazy">'
          : "") +
        escapeHtml(hero.class) +
        "</span>"
      );
    }
    if (includeRoleCategory) {
      const roleBadge = renderRoleCategoryBadge(hero, { sheetIcon: true });
      if (roleBadge) {
        badges.push(roleBadge);
      }
    }
    if (hero.damage_type) {
      const dmgDef = config.TAG_DEFINITIONS[hero.damage_type];
      badges.push(
        '<span class="badge">' +
        (dmgDef
          ? '<span class="badge-emoji" aria-hidden="true">' +
          dmgDef.emoji +
          "</span>"
          : "") +
        escapeHtml(hero.damage_type) +
        "</span>"
      );
    }
    return badges.join("");
  }

  const REPLACEMENT_ALGORITHM_URL =
    "https://github.com/arnecls/afjk-characters/blob/main/docs/replacement-algorithm.md";

  function renderAlgorithmDisclaimer() {
    return (
      '<div class="replacement-warning" role="note">' +
      '<p class="replacement-warning-text"><span class="replacement-warning-icon" aria-hidden="true">⚠️ </span>' +
      "The sections below are not curated lists but have been <a href=\"" +
      REPLACEMENT_ALGORITHM_URL +
      '" target="_blank" rel="noopener noreferrer">detected by an algorithm</a>.</p>' +
      "</div>"
    );
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
      html += "<h4>" + chips.renderInline(card.title) + "</h4>";
      if (card.items.length) {
        html += "<ul>";
        const polarity = chips.summaryCardPolarity(card.title);
        chips.groupSummaryItems(card.items, polarity).forEach(function (item) {
          if (item.type === "group") {
            html +=
              "<li>" + chips.renderGroupedVariantPill(item.variants) + "</li>";
            return;
          }
          html += "<li>" + chips.renderRichLine(item.item, polarity) + "</li>";
        });
        html += "</ul>";
      }
      html += "</div>";
    });
    html += "</div>";
    html += "</div>";
    return html;
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
    const firstLine = lines[0].trim();
    if (firstLine.startsWith("### ")) {
      return {
        title: firstLine.slice(4).trim(),
        body: lines.slice(1).join("\n").trim(),
      };
    }
    return { title: "", body: md.trim() };
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
    return markdown.renderMarkdown(lines.join("\n"), { skillOverview: true });
  }

  function stripSkillSummarySubsections(md) {
    if (!md) return "";
    return md.replace(/^\s*####\s+[^\n]*\n?/gm, "");
  }

  function stripSkillOverviewDamageTypesLine(md) {
    return md.replace(/\n- \*\*Damage types\*\*:[^\n]*/gi, "");
  }

  function renderStatsOverviewRow(entries, rowKind) {
    if (!entries || !entries.length) {
      return "";
    }
    return entries
      .map(function (entry) {
        if (rowKind === "category") {
          return chips.renderClassRankCategoryPill(entry);
        }
        return chips.renderClassRankMergedPill(
          entry.label,
          entry.rank,
          "buff",
          true
        );
      })
      .join("");
  }

  function renderStatsOverview(statsOverview) {
    if (!statsOverview) {
      return "";
    }
    const categories = renderStatsOverviewRow(
      statsOverview.categories,
      "category"
    );
    const stats = renderStatsOverviewRow(statsOverview.stats, "stat");
    if (!categories && !stats) {
      return "";
    }
    let html =
      '<div class="detail-section summary-section skill-overview-section stats-overview-section">';
    html += "<h2>Stats overview</h2>";
    html += '<div class="skill-overview-metrics stats-overview-pills">';
    if (categories) {
      html += '<div class="stats-overview-row">' + categories + "</div>";
    }
    if (stats) {
      html += '<div class="stats-overview-row">' + stats + "</div>";
    }
    html += "</div></div>";
    return html;
  }

  function highlightSkillCard(category) {
    const state = window.AFKJ.state;
    if (!category || !state.dom.heroDetail) {
      return;
    }
    const card = state.dom.heroDetail.querySelector(
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
  }

  function showDetail(hero) {
    const state = window.AFKJ.state;
    state.closeSkillCardPopover();
    state.detailHero = hero;
    state.dom.gridView.classList.add("hidden");
    state.dom.listView.classList.add("hidden");
    if (state.dom.mixView) {
      state.dom.mixView.classList.add("hidden");
    }
    state.dom.detailView.classList.remove("hidden");

    let html = '<div class="detail-panel afkj-box afkj-box-lg">';
    html += '<div class="detail-header">';
    html +=
      '<div class="detail-portrait-wrap afkj-box afkj-box-sm">' +
      gridView.renderHeroPortrait(hero, "detail-portrait") +
      "</div>";
    html += '<div class="detail-title">';
    html += "<h1>" + escapeHtml(hero.name) + "</h1>";
    if (hero.season != null && hero.seasonNumber != null) {
      html +=
        '<p class="detail-subtitle"><b>Season:</b> ' +
        escapeHtml(hero.season) +
        " (S" +
        hero.seasonNumber +
        ")</p>";
    } else if (hero.season) {
      html +=
        '<p class="detail-subtitle"><b>Season:</b> ' +
        escapeHtml(hero.season) +
        "</p>";
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
        html += tiers.renderPrydwenTierBoxes(tiers.getHeroPrydwenTiers(hero));
        const behaviorMd = tiers.stripPrydwenTierLine(parts.behavior);
        const behaviorParts = splitBehaviorHeading(behaviorMd);
        if (behaviorParts.title) {
          html += "<h2>" + escapeHtml(behaviorParts.title) + "</h2>";
        }
        if (behaviorParts.body) {
          html += '<div class="skill-overview-metrics">';
          html += markdown.renderMarkdown(behaviorParts.body, {
            behaviorHero: hero,
            behaviorSection: true,
          });
          html += "</div>";
        }
        html += "</div>";
      }
      if (hero.sections.statsOverview) {
        html += renderStatsOverview(hero.sections.statsOverview);
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
          html += skills.renderSkillCards(hero.sections.skillCards, hero);
        }
        html += "</div>";
      }
    }

    if (hero.sections.summary) {
      html += renderSummaryCards(hero.sections.summary);
    }

    html += "</div>";
    html += renderAlgorithmDisclaimer();
    const synergyHtml = renderSynergies(hero.sections, hero.name);
    if (synergyHtml) {
      html += '<div class="detail-panel afkj-box afkj-box-lg">';
      html += synergyHtml;
      html += "</div>";
    }
    const replacementHtml = renderReplacements(hero.sections, hero);
    if (replacementHtml) {
      html += '<div class="detail-panel afkj-box afkj-box-lg">';
      html += replacementHtml;
      html += "</div>";
    }

    state.dom.heroDetail.innerHTML = html;
    state.dom.heroDetail.setAttribute(
      "data-faction",
      utils.factionDataKey(hero.faction) || ""
    );
    document.title = hero.name + " — AFK Journey Heroes";
    window.AFKJ.ui.updateHeaderNav(true);
    window.scrollTo(0, 0);
  }

  // Export module API to window.AFKJ.views.detail
  window.AFKJ.views.detail = {
    formatBeneficiaryRatingDisplay: formatBeneficiaryRatingDisplay,
    renderBeneficiaryScore: renderBeneficiaryScore,
    renderHeroCompactCard: renderHeroCompactCard,
    renderHeroRowCard: renderHeroRowCard,
    renderHeroRowList: renderHeroRowList,
    renderDamageTypesOverviewLine: renderDamageTypesOverviewLine,
    formatMovementChip: formatMovementChip,
    renderSignatureSkillLine: renderSignatureSkillLine,
    renderMovementLine: renderMovementLine,
    renderBehaviorTagsLine: renderBehaviorTagsLine,
    renderSkillOverviewMetric: renderSkillOverviewMetric,
    renderSkillOverviewItem: renderSkillOverviewItem,
    renderBehaviorItem: renderBehaviorItem,
    splitSynergyReasonDetail: splitSynergyReasonDetail,
    stripSynergyReasonTargeting: stripSynergyReasonTargeting,
    parseSynergyReason: parseSynergyReason,
    synergyReasonKey: synergyReasonKey,
    chipifySynergyEnableLabel: chipifySynergyEnableLabel,
    chipifySynergyEnableDetail: chipifySynergyEnableDetail,
    renderSynergyEnableLine: renderSynergyEnableLine,
    renderSynergyPartnerExplanation: renderSynergyPartnerExplanation,
    sortSynergyHeroes: sortSynergyHeroes,
    renderSynergyHeroCard: renderSynergyHeroCard,
    renderSynergyHeroGrid: renderSynergyHeroGrid,
    renderInlineHeroPortrait: renderInlineHeroPortrait,
    synergyIntroWithoutCommonBuffers: synergyIntroWithoutCommonBuffers,
    renderCommonBuffers: renderCommonBuffers,
    renderSynergyOverflowTooltipGrid: renderSynergyOverflowTooltipGrid,
    renderSynergyPartnerOverflow: renderSynergyPartnerOverflow,
    renderSynergies: renderSynergies,
    joinIntroFragments: joinIntroFragments,
    renderBuffsProvidedIntro: renderBuffsProvidedIntro,
    renderBenefitedBySection: renderBenefitedBySection,
    renderReplacements: renderReplacements,
    renderRoleCategoryIcon: renderRoleCategoryIcon,
    renderRoleCategoryBadge: renderRoleCategoryBadge,
    renderBadges: renderBadges,
    renderAlgorithmDisclaimer: renderAlgorithmDisclaimer,
    renderSummaryCards: renderSummaryCards,
    splitBehavior: splitBehavior,
    splitBehaviorHeading: splitBehaviorHeading,
    renderSkillOverviewMetrics: renderSkillOverviewMetrics,
    renderStatsOverview: renderStatsOverview,
    highlightSkillCard: highlightSkillCard,
    showDetail: showDetail,
  };
})();
