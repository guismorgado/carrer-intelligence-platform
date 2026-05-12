from fuzzywuzzy import fuzz

MATCH_THRESHOLD = 85


def find_matches(text: str, skills: list[str]) -> list[str]:
    text_lower = text.lower()
    matched = []
    for skill in skills:
        if skill.lower() in text_lower:
            matched.append(skill)
        elif fuzz.partial_ratio(skill.lower(), text_lower) >= MATCH_THRESHOLD:
            matched.append(skill)
    return matched
