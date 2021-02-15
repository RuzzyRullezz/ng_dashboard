from fastapi import APIRouter

from neopay_api.api.v1.sample.methods import router as sample_router
from neopay_api.api.v1.user.methods import router as user_router

methods_router = APIRouter()
methods_router.include_router(sample_router, prefix='/sample')
methods_router.include_router(user_router, prefix='/user')

router = APIRouter()
router.include_router(methods_router, prefix='/v1')
