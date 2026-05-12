# API Specification

Base URL: `http://localhost:8000/api`

Interactive docs: `http://localhost:8000/docs`

---

## POST /analyze

Analyzes CV vs job description fit for a given domain.

### Request Body

```json
{
  "cv_text": "string",
  "job_text": "string",
  "domain": "management | finance | business_analytics"
}
```

### Response

```json
{
  "domain": "finance",
  "fit_analysis": {
    "matched_skills": ["Excel", "Financial Analysis"],
    "missing_skills": ["SQL", "Power BI"],
    "extra_skills": ["Leadership"],
    "fit_percentage": 65.2,
    "total_required": 13,
    "total_matched": 9
  },
  "recommendations": [
    {
      "skill": "SQL",
      "resources": [
        {
          "title": "DataCamp: SQL for Data Analysis",
          "time": "25 hours",
          "type": "course",
          "url": "https://..."
        }
      ]
    }
  ]
}
```

### Error Responses

| Code | Reason |
|------|--------|
| 400 | Unsupported domain |
| 422 | No skills found in job description |

---

## GET /health

Returns `{"status": "ok"}` — used to verify the server is running.
