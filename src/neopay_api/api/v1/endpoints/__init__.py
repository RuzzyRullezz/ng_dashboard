from fastapi import APIRouter

from .sample.methods import router as sample_router
from .user.methods import router as user_router


router = APIRouter()
router.include_router(sample_router, prefix='/sample')
router.include_router(user_router, prefix='/user')
