from fastapi import HTTPException

MIN_TEXT_LENGTH = 50


def validate_domain(domain: str, supported: set[str]) -> None:
    if domain not in supported:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported domain '{domain}'. Choose from: {sorted(supported)}",
        )


def validate_input_text(cv_text: str, job_text: str) -> None:
    if len(cv_text.strip()) < MIN_TEXT_LENGTH:
        raise HTTPException(
            status_code=422,
            detail=f"CV text is too short (minimum {MIN_TEXT_LENGTH} characters). Please paste more of your CV.",
        )
    if len(job_text.strip()) < MIN_TEXT_LENGTH:
        raise HTTPException(
            status_code=422,
            detail=f"Job description is too short (minimum {MIN_TEXT_LENGTH} characters). Please paste more of the job description.",
        )
