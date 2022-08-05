from typing import Any

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.templating import Jinja2Templates

from app.api.deps.db import get_db
from app.models import Character

router = APIRouter()

templates = Jinja2Templates(directory="static")


@router.get(
    "/",
    summary="Get list of chars",
)
async def list_of_chars(
        request: Request,
        db: Session = Depends(get_db),
) -> Any:
    """
    List of chars
    """
    a = db.query(Character).all()
    return templates.TemplateResponse("index.html", {"request": request})
