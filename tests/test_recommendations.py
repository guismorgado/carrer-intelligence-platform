import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from models.recommendation_engine import get_recommendations


def test_no_resources_returns_empty():
    # resources.json is empty at project init; missing skills yield no results
    result = get_recommendations(["SQL", "Python"], "business_analytics")
    assert result == []


def test_unknown_domain_returns_empty():
    result = get_recommendations(["SQL"], "unknown_domain")
    assert result == []
