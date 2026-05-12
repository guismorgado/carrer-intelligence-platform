from models.recommendation_engine import get_recommendations


def test_returns_resources_for_known_skill():
    result = get_recommendations(["SQL"], "business_analytics")
    assert len(result) == 1
    assert result[0]["skill"] == "SQL"
    assert len(result[0]["resources"]) >= 1
    assert "title" in result[0]["resources"][0]
    assert "url" in result[0]["resources"][0]


def test_case_insensitive_skill_lookup():
    # Skill names from fit_analyzer may have mixed casing
    result_upper = get_recommendations(["SQL"], "business_analytics")
    result_lower = get_recommendations(["sql"], "business_analytics")
    assert len(result_upper) == len(result_lower)


def test_skips_skills_with_no_resources():
    # "Joins" is in the taxonomy but has no entry in resources.json
    result = get_recommendations(["Joins", "SQL"], "business_analytics")
    skills_returned = [r["skill"] for r in result]
    assert "SQL" in skills_returned
    assert "Joins" not in skills_returned


def test_unknown_domain_returns_empty():
    result = get_recommendations(["SQL"], "unknown_domain")
    assert result == []


def test_empty_missing_skills_returns_empty():
    result = get_recommendations([], "business_analytics")
    assert result == []


def test_finance_resources_present():
    result = get_recommendations(["Excel", "Financial Modeling", "Power BI"], "finance")
    skills_returned = [r["skill"] for r in result]
    assert "Excel" in skills_returned
    assert "Financial Modeling" in skills_returned
    assert "Power BI" in skills_returned


def test_management_resources_present():
    result = get_recommendations(["Leadership", "Project Management", "Agile"], "management")
    skills_returned = [r["skill"] for r in result]
    assert "Leadership" in skills_returned
    assert "Project Management" in skills_returned
    assert "Agile" in skills_returned
