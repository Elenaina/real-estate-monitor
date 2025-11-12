from fastapi import FastAPI
from api.routes_health import router as health_router
from src.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="API for monitoring real estate prices and alerts",
    version="0.1.0",
)

app.include_router(health_router, prefix="/health", tags=["health"])


@app.get("/")
async def root():
    return {"message": "Welcome to Real Estate Monitor"}
