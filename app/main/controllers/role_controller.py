from app.main.core.dependencies import get_db, TokenRequired
from app.main import schemas, crud, models
from app.main.core.i18n import __
from app.main.core.config import Config
from fastapi import APIRouter, Depends, Body, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter(prefix="/roles", tags=["roles"])




@router.get("", response_model=list[schemas.RoleInDB],status_code=200)
async def get_roles(
    *,
    code: str = None,
    db: Session = Depends(get_db),
    # current_user=Depends(TokenRequired())
) -> list:
    """
    Roles
    """
    return crud.role.get_all(db, code)