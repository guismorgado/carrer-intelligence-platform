import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.api import router

load_dotenv()

# Comma-separated list of allowed origins; defaults to localhost for development.
_origins = os.getenv("FRONTEND_URL", "http://localhost:3000")
origins = [o.strip() for o in _origins.split(",")]

app = FastAPI(
    title="Career Intelligence Platform API",
    description="Analyzes CV vs job description fit and recommends learning paths",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/health")
def health_check():
    return {"status": "ok"}
