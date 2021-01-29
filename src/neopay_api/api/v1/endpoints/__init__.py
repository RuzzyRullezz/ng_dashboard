from fastapi import APIRouter

from .sample.methods import router as sample_router

router = APIRouter()
router.include_router(sample_router, prefix='/sample')
