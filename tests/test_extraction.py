import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from models.skill_extractor import extract_skills


def test_extract_exact_match():
    text = "I have experience with Python, SQL, and Tableau."
    skills = extract_skills(text, "business_analytics")
    assert "Python" in skills
    assert "SQL" in skills
    assert "Tableau" in skills


def test_extract_case_insensitive():
    text = "proficient in excel and pivot tables"
    skills = extract_skills(text, "finance")
    assert "Excel" in skills
    assert "Pivot Tables" in skills


def test_extract_unknown_domain_returns_empty():
    text = "Python, SQL"
    skills = extract_skills(text, "unknown_domain")
    assert skills == []
