def analyze_fit(cv_skills: list[str], job_skills: list[str]) -> dict:
    cv_set = set(s.lower() for s in cv_skills)
    job_set = set(s.lower() for s in job_skills)

    matched = sorted(cv_set & job_set)
    missing = sorted(job_set - cv_set)
    extra = sorted(cv_set - job_set)
    fit_pct = round(len(matched) / len(job_set) * 100, 1) if job_set else 0.0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra,
        "fit_percentage": fit_pct,
        "total_required": len(job_set),
        "total_matched": len(matched),
    }
