from fastapi import APIRouter

from neopay_api.api.v1 import router as api_v1_router

root_router = APIRouter()
root_router.include_router(api_v1_router)
