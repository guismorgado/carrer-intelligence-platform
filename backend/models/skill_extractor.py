from utils.fuzzy_matcher import find_matches
from data.taxonomies import SKILL_TAXONOMIES


def extract_skills(text: str, domain: str) -> list[str]:
    taxonomy = SKILL_TAXONOMIES.get(domain, {})
    all_skills = [skill for skills in taxonomy.values() for skill in skills]
    return find_matches(text, all_skills)
