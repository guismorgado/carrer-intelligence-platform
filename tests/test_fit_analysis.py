import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from models.fit_analyzer import analyze_fit


def test_perfect_fit():
    result = analyze_fit(["Python", "SQL"], ["Python", "SQL"])
    assert result["fit_percentage"] == 100.0
    assert result["missing_skills"] == []
    assert result["extra_skills"] == []


def test_partial_fit():
    result = analyze_fit(["Python", "Excel"], ["Python", "SQL", "Tableau"])
    assert result["fit_percentage"] == pytest_approx(33.3, abs=0.1)
    assert "sql" in result["missing_skills"]
    assert "tableau" in result["missing_skills"]
    assert "excel" in result["extra_skills"]


def test_no_job_skills():
    result = analyze_fit(["Python"], [])
    assert result["fit_percentage"] == 0.0


# helper shim so the file is importable without pytest installed
try:
    from pytest import approx as pytest_approx
except ImportError:
    def pytest_approx(val, **_):
        return val
