#!/usr/bin/env python3
"""Generate data/hero_play_overviews.json from Prydwen character reviews."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import heroes_io as io
import sources_web as sw

OUTPUT = ROOT / "data" / "hero_play_overviews.json"
REVIEWS_CACHE = ROOT / "data" / "prydwen_reviews_cache.json"

MAX_CHARS = 900
MAX_SENTENCES = 7
MIN_SENTENCES = 4

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
_MODE_PREFIX_RE = re.compile(
    r"^(?:Story and AFK Stages|AFK Stages|Dream Realm|PVP)\s*[-–—]?\s*",
    re.I,
)
_MODE_BREAK_RE = re.compile(
    r"(?<=[.!?])\s*(?=(?:Story and AFK Stages|AFK Stages|Dream Realm|PVP)\s*[-–—])",
    re.I,
)
_VAGUE_MODE_RE = re.compile(
    r"\b(?:"
    r"in this (?:game )?mode|in this gamemode|for this mode|"
    r"(?:as )?this (?:game ?)?mode represents|"
    r"(?:pretty much )?useless in this mode|"
    r"does nothing in this mode|see(?:s)? (?:much |limited )?use in this (?:game )?mode|"
    r"not (?:much )?use in this (?:game )?mode|"
    r"isn't very viable in this game mode|"
    r"is a bad choice in this mode|"
    r"performs poorly in this mode|"
    r"excels in this mode|"
    r"decent in this gamemode|"
    r"not viable in this gamemode|"
    r"rarely used here|used here|not used here"
    r")\b",
    re.I,
)
_SUBJECT_PRONOUN_RE = re.compile(r"^(He|She|They)\b")
_FRAGMENT_PREFIX_RE = re.compile(
    r"^(?:"
    r"Is|Has|Can|Excels|Specializ(?:e|ing)|Offers|Stalling|Controls|Featured|"
    r"Sacrifices|And one of|A dazzling|From the|Team damage|Provides|Acts|"
    r"Serves|Primarily|With|Of the|On initial|Centered|Focuses|Uses|Was|"
    r"Strongly|Despite|Character|Their|Her|His|Bombards|Curses|Unlike|While|"
    r"Starting|Who|On initial|Most certainly|After \d|With a|Focusing"
    r")\b",
    re.I,
)
_ROLE_FRAGMENT_RE = re.compile(
    r"^(?:"
    r"From the [\w ]+ (?:class|faction)(?: who belongs to the [\w ]+ faction)?"
    r"(?: whose)?|"
    r"Of the [\w ]+ (?:class|faction)(?: who| whose|,)"
    r")[.,\s]*",
    re.I,
)
_INVESTMENT_RE = re.compile(
    r"\b(investment|breakpoint|ascend|ideal build|worth investing)\b",
    re.I,
)
_SYNERGY_RE = re.compile(
    r"\b(synergiz|pairs? (?:well|best)|works? (?:well|best)|team(?:s)? with)\b",
    re.I,
)
_SKIP_OPENERS_RE = re.compile(
    r"^(?:To understand|Let's |Before the |Now, for |In many ways|Starting with|"
    r"For a quick overview|When it comes to|All her offensive|This is a passive)",
    re.I,
)

_TIER = r"(?:S|A|B|C)[+-]?(?:level|Level|rank|Rank)"
_FACTION = (
    r"(?:Celestial|Hypogean|Graveborn|Wilder|Mauler|Lightbearer|Dimensional|"
    r"Lightborn|Lightbearer)"
)
_CLASS = (
    r"(?:Marksman|Mage|Warrior|Tank|Support|Rogue|Assassin|Specialist|Rouge|"
    r"character)"
)

_HERO_INTRO_ALIASES: dict[str, list[str]] = {
    "Twins": ["Elijah and Lailah", "Twins"],
    "Smokey & Meerky": ["Smokey"],
}


def _hero_intro_names(hero_name: str) -> list[str]:
    names = [hero_name]
    names.extend(_HERO_INTRO_ALIASES.get(hero_name, ()))
    return names


def _role_intro_patterns(hero_name: str) -> list[re.Pattern[str]]:
    patterns: list[str] = []
    for name in _hero_intro_names(hero_name):
        n = re.escape(name)
        patterns.extend(
            [
                rf"{n} is an? {_TIER}(?: character)? of the {_CLASS} class "
                rf"who belongs to the {_FACTION} faction,?\s*",
                rf"{n} is an? {_TIER} {_CLASS} who belongs to the {_FACTION} "
                rf"faction,?\s*",
                rf"{n} is an? {_TIER} {_FACTION} {_CLASS} who ",
                rf"{n} is an? {_TIER} {_CLASS} of the {_FACTION} faction\.\s*",
                rf"{n} is an? {_TIER} from the {_FACTION} faction\.\s*",
                rf"{n} is an? {_TIER} {_CLASS},?\s*",
                rf"{n} is an? {_TIER} {_CLASS} who ",
                rf"{n} is an? {_TIER} {_CLASS} specializing in ",
                rf"{n} is an? {_TIER} {_FACTION} {_CLASS},?\s*",
                rf"{n} is an? {_TIER} {_CLASS} with ",
                rf"{n} is an? {_TIER} {_CLASS} and one of the ",
                rf"{n} is an? {_FACTION} {_CLASS} who ",
                rf"{n} is an? {_FACTION} {_CLASS} whose ",
                rf"{n} is a? {_FACTION} {_CLASS} focused on ",
                rf"{n} is a? {_FACTION} {_CLASS} that ",
                rf"{n} is a? {_FACTION} {_CLASS},?\s*",
                rf"{n} is a? {_FACTION} support that ",
                rf"{n} is a? stall tank with ",
                rf"{n} is a? {_CLASS} from the {_FACTION} faction\.\s*",
                rf"{n} is a? {_CLASS} from the {_FACTION} faction who ",
                rf"{n} is a? {_FACTION} {_CLASS} who ",
                rf"{n} is a? {_TIER} {_FACTION} {_CLASS},?\s*",
                rf"{n} is a? {_TIER} {_FACTION} {_CLASS} who ",
                rf"{n} is an? {_TIER} {_FACTION} who,?\s*",
                rf"{n} is a? {_TIER} {_CLASS},?\s*",
                rf"{n} is good in every game mode",
            ]
        )
    patterns.append(
        r"Elijah and Lailah \(or Twins in short\) are a? S-Rank Celestial "
        r"Support that are "
    )
    return [re.compile(p, re.I) for p in patterns]


def _fix_sentence_start(text: str) -> str:
    cleaned = text.strip().lstrip(": ")
    cleaned = re.sub(r"^(?:who|that)\s+", "", cleaned, flags=re.I)
    cleaned = re.sub(r"^whose\s+", "Their ", cleaned, flags=re.I)
    cleaned = re.sub(r"^,?\s*which\s+", "", cleaned, flags=re.I)
    cleaned = re.sub(r"^featuring\s+", "", cleaned, flags=re.I)
    if re.match(r"^are\b", cleaned, re.I):
        cleaned = "They " + cleaned
    if re.match(r"^a unique\b", cleaned, re.I):
        cleaned = "Has " + cleaned
    if cleaned and cleaned[0].islower():
        cleaned = cleaned[0].upper() + cleaned[1:]
    return cleaned


def strip_role_intro_sentence(sentence: str, hero_name: str) -> str:
    """Remove redundant tier/faction/class opener from a sentence."""
    text = sentence.strip()
    if not text:
        return ""
    for pattern in _role_intro_patterns(hero_name):
        match = pattern.match(text)
        if not match:
            continue
        remainder = _fix_sentence_start(text[match.end() :])
        if remainder.endswith(".") or remainder.endswith("!") or remainder.endswith("?"):
            return remainder
        return remainder
    return text


def strip_role_intro_text(text: str, hero_name: str) -> str:
    sentences = _split_sentences(text)
    cleaned = [
        stripped
        for sentence in sentences
        if (stripped := strip_role_intro_sentence(sentence, hero_name))
    ]
    return " ".join(cleaned)


def _mode_label_from_para(para: str) -> str | None:
    match = _MODE_PREFIX_RE.match(para)
    if not match:
        return None
    prefix = match.group(0).lower()
    if "afk" in prefix or "story" in prefix:
        return "AFK Stages"
    if "dream" in prefix:
        return "Dream Realm"
    if "pvp" in prefix:
        return "PvP"
    return None


def _mode_named_in_text(text: str) -> str | None:
    lowered = text.lower()
    if "dream realm" in lowered or "bossing" in lowered or re.search(
        r"\bboss(?:es)?\b", lowered
    ):
        return "Dream Realm"
    if "pvp" in lowered or "arena" in lowered:
        return "PvP"
    if "afk stage" in lowered or "afk stages" in lowered:
        return "AFK Stages"
    return None


def _infer_mode_from_context(sentence: str, preceding: str = "") -> str:
    named = _mode_named_in_text(f"{preceding} {sentence}")
    if named:
        return named
    combined = f"{preceding} {sentence}".lower()
    if any(
        token in combined
        for token in ("pvp", "arena", "defense team", "offense", "stall comp")
    ):
        return "PvP"
    if any(
        token in combined
        for token in (
            "dream realm",
            "boss",
            "bosses",
            "bossing",
            "endless dr",
            "pre-endless",
        )
    ):
        return "Dream Realm"
    if any(
        token in combined
        for token in ("afk stage", "afk stages", "deficit", "mob stage", "story and")
    ):
        return "AFK Stages"
    return "Dream Realm"


def _mode_for_sentence_in_review(sentence: str, review: str) -> str | None:
    needle = sentence.strip()[:60]
    if len(needle) < 20:
        return None
    idx = review.find(needle)
    if idx == -1:
        return None
    active: str | None = None
    for para in _paragraphs(review[: idx + len(needle)]):
        if label := _mode_label_from_para(para):
            active = label
    return active


def _replace_vague_mode_phrase(
    match: re.Match[str], mode: str, sentence: str
) -> str:
    phrase = match.group(0).lower()
    if "this gamemode represents" in phrase or "this mode represents" in phrase:
        if mode.lower() in sentence.lower():
            return "which represent"
        return f"in {mode}, which represent"
    if "for this mode" in phrase:
        return f"for {mode}"
    if phrase.endswith("here"):
        return phrase.replace("here", f"in {mode}")
    if "in this" in phrase or "viable in this" in phrase:
        return f"in {mode}"
    if "useless in this mode" in phrase:
        return f"useless in {mode}"
    if "does nothing in this mode" in phrase:
        return f"does nothing in {mode}"
    if "see much use in this" in phrase or "see limited use in this" in phrase:
        return phrase.replace("this game mode", mode).replace("this mode", mode)
    if "not much use in this" in phrase or "no use in this" in phrase:
        return phrase.replace("this game mode", mode).replace("this mode", mode)
    if "bad choice in this mode" in phrase:
        return f"a bad choice in {mode}"
    if "performs poorly in this mode" in phrase:
        return f"performs poorly in {mode}"
    if "excels in this mode" in phrase:
        return f"excels in {mode}"
    if "decent in this gamemode" in phrase:
        return f"decent in {mode}"
    if "not viable in this gamemode" in phrase:
        return f"not viable in {mode}"
    return f"in {mode}"


def resolve_vague_mode_references(
    text: str, hero_name: str, review: str | None = None
) -> str:
    sentences = _split_sentences(text)
    polished: list[str] = []
    preceding = ""
    for sentence in sentences:
        if not _VAGUE_MODE_RE.search(sentence):
            polished.append(sentence)
            preceding = f"{preceding} {sentence}".strip()
            continue
        mode = _mode_named_in_text(sentence)
        if mode is None and review:
            mode = _mode_for_sentence_in_review(sentence, review)
        if mode is None:
            mode = _infer_mode_from_context(sentence, preceding)
        resolved = _VAGUE_MODE_RE.sub(
            lambda match: _replace_vague_mode_phrase(match, mode, sentence),
            sentence,
        )
        resolved = re.sub(
            r"\befficacy in this mode\b",
            f"efficacy in {mode}",
            resolved,
            flags=re.I,
        )
        resolved = re.sub(
            r"\bvalue for this mode\b",
            f"value for {mode}",
            resolved,
            flags=re.I,
        )
        resolved = re.sub(
            r"\bmain value for this mode\b",
            f"main value for {mode}",
            resolved,
            flags=re.I,
        )
        polished.append(resolved)
        preceding = f"{preceding} {resolved}".strip()
    return " ".join(polished)


def _hero_name_in_sentence(sentence: str, hero_name: str) -> bool:
    if hero_name in sentence:
        return True
    return any(alias in sentence for alias in _HERO_INTRO_ALIASES.get(hero_name, ()))


def _attach_subject_to_fragment(sentence: str, hero_name: str) -> str:
    text = sentence.strip()
    possessive = f"{hero_name}'s" if not hero_name.endswith("s") else f"{hero_name}'"

    if match := re.match(r"^(Her|His|Their) kit\b", text, re.I):
        return re.sub(r"^(Her|His|Their) kit\b", f"{possessive} kit", text, count=1)
    if match := re.match(r"^(She|He|They)\b", text, re.I):
        return re.sub(r"^(She|He|They)\b", hero_name, text, count=1)
    if re.match(r"^Despite\b", text, re.I):
        return f"{hero_name}, despite{text[8:]}"
    if re.match(r"^While\b", text, re.I):
        return f"{hero_name}, while{text[5:]}"
    if re.match(r"^Unlike\b", text, re.I):
        return f"Unlike other heroes, {hero_name.lower()}{text[7:]}"
    if re.match(r"^With a\b", text, re.I):
        return f"{hero_name} has a{text[6:]}"
    if re.match(r"^With\b", text, re.I):
        return f"{hero_name} brings{text[4:]}"
    if re.match(r"^Of the\b", text, re.I):
        rest = text[7:].strip()
        if rest.lower().startswith("faction"):
            return f"{hero_name} {rest[0].lower()}{rest[1:]}"
        return f"{hero_name}, from the {rest[0].lower()}{rest[1:]}"
    if re.match(r"^Who\b", text, re.I):
        return f"{hero_name} is someone who{text[3:]}"
    if re.match(r"^Is\b", text, re.I):
        rest = text[3:].strip()
        return f"{hero_name} is {rest[0].lower()}{rest[1:]}" if rest else hero_name
    if re.match(r"^Has\b", text, re.I):
        return f"{hero_name} has {text[4:].lstrip()}"
    if re.match(r"^Can\b", text, re.I):
        return f"{hero_name} can {text[4:].lstrip()}"
    if re.match(r"^Excels\b", text, re.I):
        return f"{hero_name} excels {text[6:].lstrip()}"
    if re.match(r"^Specializ", text, re.I):
        return f"{hero_name} specializes {text.split(maxsplit=1)[1]}"
    if re.match(r"^Offers\b", text, re.I):
        return f"{hero_name} offers {text[7:].lstrip()}"
    if re.match(r"^Stalling\b", text, re.I):
        return f"{hero_name} focuses on stalling {text[9:].lstrip()}"
    if re.match(r"^Controls\b", text, re.I):
        return f"{hero_name} controls {text[9:].lstrip()}"
    if re.match(r"^Sacrifices\b", text, re.I):
        return f"{hero_name} sacrifices {text[10:].lstrip()}"
    if re.match(r"^Featured\b", text, re.I):
        return f"{hero_name} was featured {text[9:].lstrip()}"
    if re.match(r"^Was\b", text, re.I):
        return f"{hero_name} was {text[4:].lstrip()}"
    if re.match(r"^And one of\b", text, re.I):
        return f"{hero_name} is one of {text[10:].lstrip()}"
    if re.match(r"^A dazzling\b", text, re.I):
        return f"{hero_name} is a dazzling {text[11:].lstrip()}"
    if re.match(r"^Provides\b", text, re.I):
        return f"{hero_name} provides {text[9:].lstrip()}"
    if re.match(r"^Acts\b", text, re.I):
        return f"{hero_name} acts {text[5:].lstrip()}"
    if re.match(r"^Serves\b", text, re.I):
        return f"{hero_name} serves {text[7:].lstrip()}"
    if re.match(r"^Primarily\b", text, re.I):
        return f"{hero_name} primarily {text[10:].lstrip()}"
    if re.match(r"^Strongly\b", text, re.I):
        return f"{hero_name} strongly {text[9:].lstrip()}"
    if re.match(r"^Character\b", text, re.I):
        return f"{hero_name} is a {text[10:].lstrip()}"
    if re.match(r"^Centered\b", text, re.I):
        return f"{hero_name} is centered {text[8:].lstrip()}"
    if re.match(r"^Focuses\b", text, re.I):
        return f"{hero_name} focuses {text[7:].lstrip()}"
    if re.match(r"^Uses\b", text, re.I):
        return f"{hero_name} uses {text[5:].lstrip()}"
    if re.match(r"^Focusing\b", text, re.I):
        return f"{hero_name} focuses on {text[10:].lstrip()}"
    if re.match(r"^Bombards\b", text, re.I):
        return f"{hero_name} bombards {text[9:].lstrip()}"
    if re.match(r"^Curses\b", text, re.I):
        return f"{hero_name} curses {text[7:].lstrip()}"
    if re.match(r"^Starting\b", text, re.I):
        return f"{hero_name}, starting{text[8:]}"
    if re.match(r"^After\b", text, re.I):
        return f"{hero_name}, after{text[5:]}"
    if re.match(r"^Most certainly\b", text, re.I):
        return f"{hero_name} is most certainly {text[14:].lstrip()}"
    if re.match(r"^On initial\b", text, re.I):
        return f"{hero_name}, on initial{text[10:]}"
    if match := re.match(r"^From the (.+?) who ", text, re.I):
        return f"{hero_name}, from the {match.group(1)}, {text[match.end():]}"
    if match := re.match(r"^From the (.+?)[.,]\s*", text, re.I):
        detail = match.group(1).strip()
        rest = text[match.end():].strip()
        if rest:
            return f"{hero_name}, from the {detail}, {rest[0].lower()}{rest[1:]}"
        return f"{hero_name} is from the {detail}."
    if re.match(r"^Team damage\b", text, re.I):
        return f"{possessive} kit provides team damage {text[12:].lstrip()}"
    if match := re.match(r"^Their (.+)$", text, re.I):
        return f"{possessive} {match.group(1)[0].lower()}{match.group(1)[1:]}"
    return f"{hero_name} {text[0].lower()}{text[1:]}"


def ensure_first_sentence_subject(text: str, hero_name: str) -> str:
    sentences = _split_sentences(text)
    if not sentences:
        return text

    while sentences and _ROLE_FRAGMENT_RE.match(sentences[0]):
        if len(sentences) == 1:
            break
        sentences = sentences[1:]

    first = sentences[0].strip()
    if _hero_name_in_sentence(first, hero_name) and first.startswith(hero_name):
        first = re.sub(
            r"^(Her|His|Their) kit\b",
            f"{hero_name}'s kit" if not hero_name.endswith("s") else f"{hero_name}' kit",
            first,
            count=1,
        )
        sentences[0] = first
        return " ".join(sentences)

    if re.match(r"^(She|He|They)\b", first):
        sentences[0] = re.sub(r"^(She|He|They)\b", hero_name, first, count=1)
        return " ".join(sentences)

    if _hero_name_in_sentence(first, hero_name) and _FRAGMENT_PREFIX_RE.match(first):
        sentences[0] = _attach_subject_to_fragment(first, hero_name)
        return " ".join(sentences)

    if _FRAGMENT_PREFIX_RE.match(first) or not first.startswith(hero_name):
        sentences[0] = _attach_subject_to_fragment(first, hero_name)

    return " ".join(sentences)


def polish_play_overview(
    text: str, hero_name: str, review: str | None = None
) -> str:
    polished = strip_role_intro_text(text, hero_name)
    polished = resolve_vague_mode_references(polished, hero_name, review)
    polished = ensure_first_sentence_subject(polished, hero_name)
    return polished


def _split_sentences(text: str) -> list[str]:
    text = re.sub(r"\.([A-Z])", r". \1", text)
    text = text.strip()
    if not text:
        return []
    parts = _SENTENCE_SPLIT_RE.split(text)
    return [part.strip() for part in parts if part.strip()]


def _paragraphs(review: str) -> list[str]:
    normalized = _MODE_BREAK_RE.sub("\n\n", review)
    return [part.strip() for part in normalized.split("\n\n") if part.strip()]


def _normalize_mode_sentence(paragraph: str) -> str:
    sentence = _split_sentences(_MODE_PREFIX_RE.sub("", paragraph))[0]
    return sentence.strip()


def _is_weak_sentence(sentence: str) -> bool:
    return bool(_SKIP_OPENERS_RE.match(sentence)) or len(sentence) < 45


def _pick_within_budget(candidates: list[str], hero_name: str) -> str:
    picked: list[str] = []
    seen: set[str] = set()
    total = 0

    for sentence in candidates:
        if len(picked) >= MAX_SENTENCES:
            break
        normalized = sentence.strip()
        if not normalized or normalized in seen or _is_weak_sentence(normalized):
            continue
        normalized = strip_role_intro_sentence(normalized, hero_name)
        if not normalized or _is_weak_sentence(normalized):
            continue
        add_len = len(normalized) + (1 if picked else 0)
        if total + add_len > MAX_CHARS:
            continue
        seen.add(normalized)
        picked.append(normalized)
        total += add_len

    if len(picked) < MIN_SENTENCES:
        for sentence in candidates:
            if len(picked) >= MIN_SENTENCES or len(picked) >= MAX_SENTENCES:
                break
            normalized = sentence.strip()
            if not normalized or normalized in seen:
                continue
            normalized = strip_role_intro_sentence(normalized, hero_name)
            if not normalized:
                continue
            add_len = len(normalized) + (1 if picked else 0)
            if total + add_len > MAX_CHARS:
                continue
            seen.add(normalized)
            picked.append(normalized)
            total += add_len

    return " ".join(picked)


def summarize_prydwen_review(review: str, hero_name: str = "") -> str:
    """Condense Prydwen review prose to a short 3–5 sentence overview."""
    paras = _paragraphs(review)
    if not paras:
        return ""

    mode_sentences: list[str] = []
    body_sentences: list[str] = []
    synergy_sentences: list[str] = []

    for para in paras:
        if _MODE_PREFIX_RE.match(para):
            mode = _normalize_mode_sentence(para)
            if mode:
                mode_sentences.append(mode)
            continue
        for sentence in _split_sentences(para):
            if _INVESTMENT_RE.search(sentence):
                continue
            if _SYNERGY_RE.search(sentence):
                synergy_sentences.append(sentence)
            else:
                body_sentences.append(sentence)

    candidates: list[str] = []
    if body_sentences:
        candidates.append(body_sentences[0])
    for sentence in body_sentences[1:3]:
        candidates.append(sentence)
    if mode_sentences:
        candidates.append(mode_sentences[0])
    if len(mode_sentences) > 1:
        candidates.append(mode_sentences[1])
    if synergy_sentences:
        candidates.append(synergy_sentences[0])
    for sentence in body_sentences[3:6]:
        candidates.append(sentence)

    return _pick_within_budget(candidates, hero_name)


def hero_names_from_processed() -> list[str]:
    processed = io.load_processed()
    return sorted(processed["heroes"])


def build_play_overviews(
    hero_names: list[str] | None = None,
    *,
    fetch: bool = True,
    reviews: dict[str, str] | None = None,
    use_cache: bool = False,
    save_cache: bool = False,
) -> tuple[dict[str, str], list[str]]:
    names = hero_names or hero_names_from_processed()
    if reviews is not None:
        raw_reviews = reviews
    elif use_cache and REVIEWS_CACHE.exists():
        raw_reviews = json.loads(REVIEWS_CACHE.read_text(encoding="utf-8"))
    else:
        raw_reviews = sw.fetch_prydwen_reviews(names)
        if save_cache or not REVIEWS_CACHE.exists():
            REVIEWS_CACHE.write_text(
                json.dumps(raw_reviews, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
    out: dict[str, str] = {}
    missing: list[str] = []
    for name in names:
        review = raw_reviews.get(name)
        if not review:
            missing.append(name)
            continue
        summary = summarize_prydwen_review(review, name)
        if not summary:
            missing.append(name)
            continue
        out[name] = polish_play_overview(summary, name, review)
    return out, missing


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print missing heroes without writing JSON",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print JSON to stdout instead of writing the data file",
    )
    parser.add_argument(
        "--use-cache",
        action="store_true",
        help="Resummarize from data/prydwen_reviews_cache.json when present",
    )
    args = parser.parse_args()

    overviews, missing = build_play_overviews(
        use_cache=args.use_cache,
        save_cache=not args.use_cache,
    )
    if args.stdout:
        print(json.dumps(overviews, indent=2, ensure_ascii=False))
    elif not args.dry_run:
        OUTPUT.write_text(
            json.dumps(overviews, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {len(overviews)} play overviews to {OUTPUT}")

    if missing:
        print(f"Missing review/overview for {len(missing)} hero(es):")
        for name in missing:
            print(f"  - {name}")


if __name__ == "__main__":
    main()
