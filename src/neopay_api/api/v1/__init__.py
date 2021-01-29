from fastapi import APIRouter

from .endpoints import router as api_v1_router

router = APIRouter()
router.include_router(api_v1_router, prefix='/api/v1')
