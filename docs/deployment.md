# Deployment Guide

## Local Development

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
uvicorn app:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## Production (v1 targets)

| Service | Platform | Notes |
|---------|----------|-------|
| Frontend | Vercel | Connect GitHub repo; auto-deploys on push to main |
| Backend | Render | Free tier; deploy from GitHub; set env vars in dashboard |

### Environment Variables (Render)

Set these in the Render dashboard under "Environment":
- `FRONTEND_URL` — your Vercel URL (for CORS)

### Environment Variables (Vercel)

Set these in the Vercel dashboard:
- `VITE_API_URL` — your Render backend URL
