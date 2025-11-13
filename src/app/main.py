from fastapi import FastAPI

from src.app.api import api_router
from src.app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="API for monitoring real estate prices and alerts",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "Welcome to Real Estate Monitor",
        "docs": "/api/docs",
        "version": "0.1.0",
    }
