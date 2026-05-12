import json
from pathlib import Path

_resources: dict = {}


def _load() -> dict:
    global _resources
    if not _resources:
        path = Path(__file__).parent.parent / "data" / "resources.json"
        with open(path) as f:
            _resources = json.load(f)
    return _resources


def get_recommendations(missing_skills: list[str], domain: str) -> list[dict]:
    domain_resources = _load().get(domain, {})
    # Case-insensitive key lookup so "sql" finds "SQL" in resources.json
    lower_map = {k.lower(): k for k in domain_resources}
    result = []
    for skill in missing_skills:
        key = lower_map.get(skill.lower())
        if key:
            result.append({"skill": skill, "resources": domain_resources[key]})
    return result
