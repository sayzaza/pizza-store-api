"""
Ingredients-related API routes
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.models.pizza import Ingredient
from app.schemas.pizza import IngredientResponse

router = APIRouter(prefix="/ingredients", tags=["ingredients"])


@router.get("/", response_model=List[IngredientResponse])
async def get_ingredients(db: Session = Depends(get_db)):
    """Get all available ingredients"""
    ingredients = db.query(Ingredient).all()
    return ingredients
