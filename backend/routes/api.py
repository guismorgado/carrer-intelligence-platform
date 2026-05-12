from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.skill_extractor import extract_skills
from models.fit_analyzer import analyze_fit
from models.recommendation_engine import get_recommendations
from utils.validators import validate_domain, validate_input_text

router = APIRouter()

SUPPORTED_DOMAINS = {"management", "finance", "business_analytics"}


class AnalyzeRequest(BaseModel):
    cv_text: str
    job_text: str
    domain: str


@router.post("/analyze")
def analyze(request: AnalyzeRequest):
    validate_domain(request.domain, SUPPORTED_DOMAINS)
    validate_input_text(request.cv_text, request.job_text)

    cv_skills = extract_skills(request.cv_text, request.domain)
    job_skills = extract_skills(request.job_text, request.domain)

    if not job_skills:
        raise HTTPException(
            status_code=422,
            detail="No recognizable skills found in the job description for this domain.",
        )

    fit = analyze_fit(cv_skills, job_skills)
    recommendations = get_recommendations(fit["missing_skills"], request.domain)

    return {
        "domain": request.domain,
        "fit_analysis": fit,
        "recommendations": recommendations,
    }
