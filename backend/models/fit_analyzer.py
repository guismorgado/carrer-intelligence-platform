def analyze_fit(cv_skills: list[str], job_skills: list[str]) -> dict:
    # Build lowercase → original-case maps so comparison is case-insensitive
    # but output preserves the taxonomy's casing (e.g. "SQL" not "sql").
    cv_map: dict[str, str] = {}
    for s in cv_skills:
        cv_map.setdefault(s.lower(), s)

    job_map: dict[str, str] = {}
    for s in job_skills:
        job_map.setdefault(s.lower(), s)

    cv_keys = set(cv_map)
    job_keys = set(job_map)

    matched = sorted(job_map[k] for k in cv_keys & job_keys)
    missing = sorted(job_map[k] for k in job_keys - cv_keys)
    extra = sorted(cv_map[k] for k in cv_keys - job_keys)
    fit_pct = round(len(matched) / len(job_keys) * 100, 1) if job_keys else 0.0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra,
        "fit_percentage": fit_pct,
        "total_required": len(job_keys),
        "total_matched": len(matched),
    }
