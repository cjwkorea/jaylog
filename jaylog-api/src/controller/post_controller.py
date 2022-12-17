
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from dependencies import get_db
from dto import sign_dto
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/api/v1/posts",
    tags=["post"]
)
