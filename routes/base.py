from fastapi import FastAPI,APIRouter
import os 

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api"]
)

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME", "Mini Agent")
    app_version = os.getenv("APP_VERSION", "0.1.0")

    return {
        "app_name": app_name,
        "app_version": app_version
    }
