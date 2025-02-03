from fastapi import APIRouter

from .llm_router import router as llm_router

router = APIRouter()

router.include_router(llm_router)
