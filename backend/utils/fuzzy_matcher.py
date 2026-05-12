import re
from rapidfuzz import fuzz

FUZZY_THRESHOLD = 88
# Single-word skills (e.g. "R", "Go", "SQL") rely on exact word-boundary match
# only. Fuzzy is reserved for multi-word skills to avoid false positives.
MIN_FUZZY_SKILL_WORDS = 2


def find_matches(text: str, skills: list[str]) -> list[str]:
    text_lower = text.lower()
    matched = []
    for skill in skills:
        skill_lower = skill.lower()
        pattern = r"\b" + re.escape(skill_lower) + r"\b"
        if re.search(pattern, text_lower):
            matched.append(skill)
        elif (
            len(skill_lower.split()) >= MIN_FUZZY_SKILL_WORDS
            and fuzz.partial_ratio(skill_lower, text_lower) >= FUZZY_THRESHOLD
        ):
            matched.append(skill)
    return matched
