from sqlite3 import IntegrityError

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.app.db import get_db
from src.models.property import Property
from src.schemas.property import PropertyCreate

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new property",
    description="Add a new property to monitor",
)
async def create_property(
    property_in: PropertyCreate, db: AsyncSession = Depends(get_db)
):
    try:
        new_property = Property(**property_in.model_dump())
        db.add(new_property)
        await db.commit()
        await db.refresh(new_property)
        return new_property
    except IntegrityError as e:
        await db.rollback()
        raise HTTPException(status_code=409, detail="Property already exists") from e
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail=str(e)) from e
