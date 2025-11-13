"""
API v1 router aggregation.
"""

from fastapi import APIRouter

from src.app.api.v1.endpoints import health, properties

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])

api_router.include_router(properties.router, prefix="/properties", tags=["properties"])
