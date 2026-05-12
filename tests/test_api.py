import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# ---------------------------------------------------------------------------
# Realistic text samples
# ---------------------------------------------------------------------------

CV_FINANCE = """
Finance graduate with 3 years of experience in financial analysis and reporting.
Proficient in Excel including Pivot Tables, Advanced Formulas, and VLOOKUP.
Strong skills in Financial Modeling, Budgeting, and Forecasting.
Used Power BI for dashboard creation and SQL for data extraction.
Knowledge of Financial Reporting and Variance Analysis.
"""

JD_FINANCE = """
We are hiring a Financial Analyst with strong Excel skills including Pivot Tables,
VLOOKUP, and Advanced Formulas. The role requires experience in Financial Modeling,
Forecasting, and Valuation. Power BI or Tableau experience preferred.
Knowledge of Financial Reporting and Business Acumen is essential.
"""

CV_MANAGEMENT = """
Experienced project manager with 5 years leading cross-functional teams.
Strong leadership and team management skills with a focus on delegation and mentoring.
Proficient in stakeholder management and written communication.
Experience with planning, organization, prioritization, and project management.
Used Microsoft Office and Asana for project tracking.
Skilled in problem solving and decision making under pressure.
"""

JD_MANAGEMENT = """
We are looking for a Project Manager with strong leadership and team management skills.
The role requires excellent stakeholder management and presentation abilities.
Experience with project management methodologies, planning, and organization is essential.
Proficiency in Microsoft Office required. Agile experience is a strong plus.
Strong problem solving and decision making abilities needed.
"""

CV_BA = """
Data analyst with 2 years of experience. Proficient in Python including Pandas and NumPy.
Strong SQL skills for database querying and data modeling.
Built interactive dashboards in Tableau and Power BI. Experience with statistical analysis,
hypothesis testing, A/B testing, and regression. Familiarity with Excel including
advanced formulas and statistical functions. Strong business acumen and KPI definition.
"""

JD_BA = """
We are seeking a Business Analyst with strong SQL and Python skills including Pandas.
Experience with data visualization using Tableau or Power BI is required.
Statistical Analysis, Hypothesis Testing, and A/B Testing experience preferred.
Excel proficiency including advanced formulas for reporting and analysis.
Knowledge of KPI Definition, metrics tracking, and business acumen expected.
"""


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------

def test_health_check():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


# ---------------------------------------------------------------------------
# Finance end-to-end
# ---------------------------------------------------------------------------

def test_finance_response_structure():
    r = client.post("/api/analyze", json={
        "cv_text": CV_FINANCE,
        "job_text": JD_FINANCE,
        "domain": "finance",
    })
    assert r.status_code == 200
    body = r.json()
    assert body["domain"] == "finance"
    assert "fit_analysis" in body
    assert "recommendations" in body
    fa = body["fit_analysis"]
    for key in ("matched_skills", "missing_skills", "extra_skills",
                "fit_percentage", "total_required", "total_matched"):
        assert key in fa


def test_finance_matched_skills():
    r = client.post("/api/analyze", json={
        "cv_text": CV_FINANCE,
        "job_text": JD_FINANCE,
        "domain": "finance",
    })
    fa = r.json()["fit_analysis"]
    assert "Excel" in fa["matched_skills"]
    assert "Financial Modeling" in fa["matched_skills"]
    assert "Power BI" in fa["matched_skills"]
    assert "Forecasting" in fa["matched_skills"]
    assert fa["fit_percentage"] > 0
    assert fa["total_matched"] <= fa["total_required"]


def test_finance_missing_skills():
    r = client.post("/api/analyze", json={
        "cv_text": CV_FINANCE,
        "job_text": JD_FINANCE,
        "domain": "finance",
    })
    fa = r.json()["fit_analysis"]
    # Valuation is in JD but not in CV
    assert "Valuation" in fa["missing_skills"]


# ---------------------------------------------------------------------------
# Management end-to-end
# ---------------------------------------------------------------------------

def test_management_response_ok():
    r = client.post("/api/analyze", json={
        "cv_text": CV_MANAGEMENT,
        "job_text": JD_MANAGEMENT,
        "domain": "management",
    })
    assert r.status_code == 200
    assert r.json()["domain"] == "management"


def test_management_matched_skills():
    r = client.post("/api/analyze", json={
        "cv_text": CV_MANAGEMENT,
        "job_text": JD_MANAGEMENT,
        "domain": "management",
    })
    fa = r.json()["fit_analysis"]
    assert "Leadership" in fa["matched_skills"]
    assert "Project Management" in fa["matched_skills"]
    assert "Stakeholder Management" in fa["matched_skills"]
    assert fa["fit_percentage"] > 0


# ---------------------------------------------------------------------------
# Business Analytics end-to-end
# ---------------------------------------------------------------------------

def test_ba_response_ok():
    r = client.post("/api/analyze", json={
        "cv_text": CV_BA,
        "job_text": JD_BA,
        "domain": "business_analytics",
    })
    assert r.status_code == 200
    assert r.json()["domain"] == "business_analytics"


def test_ba_matched_skills():
    r = client.post("/api/analyze", json={
        "cv_text": CV_BA,
        "job_text": JD_BA,
        "domain": "business_analytics",
    })
    fa = r.json()["fit_analysis"]
    assert "SQL" in fa["matched_skills"]
    assert "Python" in fa["matched_skills"]
    assert "Tableau" in fa["matched_skills"]
    assert "A/B Testing" in fa["matched_skills"]
    assert fa["fit_percentage"] > 0


# ---------------------------------------------------------------------------
# Recommendations structure
# ---------------------------------------------------------------------------

def test_recommendations_list_structure():
    r = client.post("/api/analyze", json={
        "cv_text": CV_BA,
        "job_text": JD_BA,
        "domain": "business_analytics",
    })
    assert r.status_code == 200
    for rec in r.json()["recommendations"]:
        assert "skill" in rec
        assert "resources" in rec
        for res in rec["resources"]:
            assert "title" in res
            assert "url" in res
            assert "type" in res
            assert "time" in res


# ---------------------------------------------------------------------------
# Validation errors
# ---------------------------------------------------------------------------

def test_invalid_domain_returns_400():
    r = client.post("/api/analyze", json={
        "cv_text": CV_FINANCE,
        "job_text": JD_FINANCE,
        "domain": "marketing",
    })
    assert r.status_code == 400
    assert "unsupported" in r.json()["detail"].lower()


def test_short_cv_returns_422():
    r = client.post("/api/analyze", json={
        "cv_text": "short",
        "job_text": JD_FINANCE,
        "domain": "finance",
    })
    assert r.status_code == 422
    assert "cv" in r.json()["detail"].lower()


def test_short_jd_returns_422():
    r = client.post("/api/analyze", json={
        "cv_text": CV_FINANCE,
        "job_text": "short",
        "domain": "finance",
    })
    assert r.status_code == 422
    assert "job" in r.json()["detail"].lower()


def test_missing_required_fields_returns_422():
    r = client.post("/api/analyze", json={"cv_text": CV_FINANCE})
    assert r.status_code == 422


def test_jd_with_no_domain_skills_returns_422():
    r = client.post("/api/analyze", json={
        "cv_text": CV_FINANCE,
        "job_text": "We are looking for a great person who loves hiking and cooking delicious food outdoors.",
        "domain": "finance",
    })
    assert r.status_code == 422
    assert "no recognizable skills" in r.json()["detail"].lower()
