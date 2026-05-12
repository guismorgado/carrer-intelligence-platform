# Career Intelligence Platform

A web app that analyzes how well your CV matches a job description and recommends targeted learning paths.

## What it does

Paste your CV and a job description, select a domain, and get:
- A transparent fit breakdown (matched / missing / extra skills)
- A fit percentage based on skill alignment
- Prioritized learning recommendations for missing skills

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + FastAPI |
| NLP | spaCy + fuzzywuzzy |
| Frontend | React + TypeScript |
| Storage | JSON files (v1) |

## Target Domains (v1)

- Management
- Finance
- Business Analytics

## Project Status

- [ ] Backend skill extraction
- [ ] Fit analysis engine
- [ ] Learning recommendations
- [ ] Frontend input page
- [ ] Frontend results page
- [ ] End-to-end integration

## Quick Start

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Runs on `http://localhost:8000`. Docs at `http://localhost:8000/docs`.

### Frontend

```bash
cd frontend
npm install
npm start
```

Runs on `http://localhost:3000`.

## Architecture

See [CLAUDE.md](CLAUDE.md) for full project specification and technical decisions.

## License

MIT
