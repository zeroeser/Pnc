from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    summary="Get list of chars",
)
async def list_of_chars() -> Any:
    """
    List of chars
    """
