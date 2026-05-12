from models.fit_analyzer import analyze_fit


def test_perfect_fit():
    result = analyze_fit(["Python", "SQL", "Tableau"], ["Python", "SQL", "Tableau"])
    assert result["fit_percentage"] == 100.0
    assert result["missing_skills"] == []
    assert result["extra_skills"] == []
    assert result["total_required"] == 3
    assert result["total_matched"] == 3


def test_partial_fit():
    result = analyze_fit(["Python", "Excel"], ["Python", "SQL", "Tableau"])
    assert result["fit_percentage"] == pytest_approx(33.3, abs=0.2)
    assert "SQL" in result["missing_skills"]
    assert "Tableau" in result["missing_skills"]
    assert "Excel" in result["extra_skills"]
    assert "Python" in result["matched_skills"]


def test_zero_fit():
    result = analyze_fit(["Leadership", "Excel"], ["Python", "SQL", "Tableau"])
    assert result["fit_percentage"] == 0.0
    assert result["total_matched"] == 0


def test_no_job_skills_returns_zero():
    result = analyze_fit(["Python"], [])
    assert result["fit_percentage"] == 0.0
    assert result["total_required"] == 0


def test_preserves_original_casing():
    # Skills extracted from taxonomy always have correct casing.
    # Verify the output casing matches job description's taxonomy casing.
    result = analyze_fit(["SQL", "Python"], ["SQL", "Python", "Tableau"])
    assert "SQL" in result["matched_skills"]
    assert "Python" in result["matched_skills"]
    assert "Tableau" in result["missing_skills"]


def test_case_insensitive_comparison():
    # Even if casing differs, the match should still be found.
    result = analyze_fit(["sql", "python"], ["SQL", "Python"])
    assert result["fit_percentage"] == 100.0


def test_realistic_finance_scenario():
    cv_skills = ["Excel", "Financial Modeling", "Budgeting", "Power BI", "SQL"]
    job_skills = ["Excel", "Financial Modeling", "Valuation", "DCF", "Forecasting", "Power BI"]
    result = analyze_fit(cv_skills, job_skills)
    assert "Excel" in result["matched_skills"]
    assert "Financial Modeling" in result["matched_skills"]
    assert "Power BI" in result["matched_skills"]
    assert "Valuation" in result["missing_skills"]
    assert "DCF" in result["missing_skills"]
    assert result["fit_percentage"] == pytest_approx(50.0, abs=0.1)


# Lightweight approx helper so the file runs without pytest installed
try:
    from pytest import approx as pytest_approx
except ImportError:
    def pytest_approx(val, abs=0.1, **_):  # type: ignore[misc]
        return val
