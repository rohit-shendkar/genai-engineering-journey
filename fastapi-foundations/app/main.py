from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="FastAPI Foundations",
    description="A foundational FastAPI application with health check endpoint.",
    version="1.0.0",
)

app.include_router(health.router)