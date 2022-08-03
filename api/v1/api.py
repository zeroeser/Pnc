from fastapi import APIRouter

from .endpoints import chars

api_router = APIRouter()

api_router.include_router(
    chars.router,
    prefix="/pnc_chars",
    tags=["Список персонажей"],
)
