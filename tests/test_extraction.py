from models.skill_extractor import extract_skills

# --- exact matches ---

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


# --- realistic CV sample ---

SAMPLE_CV_FINANCE = """
Finance Graduate with 2 years of internship experience.
Skills: Excel, Pivot Tables, Financial Modeling, Budgeting, Forecasting,
Financial Analysis, Financial Reporting. Familiar with Power BI and SQL.
"""

SAMPLE_JD_FINANCE = """
We are looking for a Financial Analyst with strong Excel skills including
Pivot Tables, VLOOKUP, and Advanced Formulas. Experience in Financial Modeling,
Valuation, and Forecasting required. Power BI or Tableau experience a plus.
"""

def test_cv_finance_extraction():
    skills = extract_skills(SAMPLE_CV_FINANCE, "finance")
    assert "Excel" in skills
    assert "Financial Modeling" in skills
    assert "Budgeting" in skills


def test_jd_finance_extraction():
    skills = extract_skills(SAMPLE_JD_FINANCE, "finance")
    assert "Excel" in skills
    assert "Pivot Tables" in skills
    assert "Financial Modeling" in skills
    assert "Valuation" in skills


# --- realistic BA sample ---

SAMPLE_CV_BA = """
Data Analyst with experience in Python (Pandas, NumPy), SQL, Tableau,
and statistical analysis. Built dashboards in Power BI. Experience with
A/B Testing, Hypothesis Testing, and Regression analysis.
"""

def test_cv_ba_extraction():
    skills = extract_skills(SAMPLE_CV_BA, "business_analytics")
    assert "Python" in skills
    assert "Pandas" in skills
    assert "SQL" in skills
    assert "Tableau" in skills
    assert "Power BI" in skills


# --- edge cases ---

def test_unknown_domain_returns_empty():
    skills = extract_skills("Python, SQL, Excel", "unknown_domain")
    assert skills == []


def test_empty_text_returns_empty():
    skills = extract_skills("", "finance")
    assert skills == []


def test_no_matching_skills_returns_empty():
    skills = extract_skills("I enjoy hiking and cooking.", "business_analytics")
    assert skills == []


# --- realistic management sample ---

SAMPLE_CV_MANAGEMENT = """
Senior Project Manager with 6 years of experience in leadership and team management.
Skilled in stakeholder management, written communication, and presentation.
Strong background in project management, planning, organization, and prioritization.
Tools used: Microsoft Office, Asana, Slack. Problem solving and decision making focus.
"""

SAMPLE_JD_MANAGEMENT = """
We are looking for a Project Manager with proven leadership and team management skills.
The role requires stakeholder management, presentation skills, and strong written communication.
Experience with project management, planning, and organization is essential.
Microsoft Office proficiency required. Agile and decision making skills are a plus.
"""


def test_cv_management_extraction():
    skills = extract_skills(SAMPLE_CV_MANAGEMENT, "management")
    assert "Leadership" in skills
    assert "Project Management" in skills
    assert "Stakeholder Management" in skills
    assert "Microsoft Office" in skills


def test_jd_management_extraction():
    skills = extract_skills(SAMPLE_JD_MANAGEMENT, "management")
    assert "Leadership" in skills
    assert "Project Management" in skills
    assert "Stakeholder Management" in skills
    assert "Presentation Skills" in skills
