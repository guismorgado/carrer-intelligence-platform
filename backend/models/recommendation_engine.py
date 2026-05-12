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
    resources = _load().get(domain, {})
    result = []
    for skill in missing_skills:
        skill_resources = resources.get(skill, [])
        if skill_resources:
            result.append({"skill": skill, "resources": skill_resources})
    return result
