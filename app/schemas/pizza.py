"""
Pydantic schemas for Pizza-related API responses
"""

from pydantic import BaseModel
from typing import List, Optional


class IngredientResponse(BaseModel):
    """Schema for ingredient response"""
    id: int
    name: str
    is_allergen: bool
    sub_ingredients: List['IngredientResponse'] = []

    class Config:
        from_attributes = True


class PizzaResponse(BaseModel):
    """Schema for pizza response"""
    id: int
    name: str
    description: str
    ingredients: List[IngredientResponse] = []
    allergens: List[str] = []

    class Config:
        from_attributes = True


class PizzaListResponse(BaseModel):
    """Schema for pizza list response"""
    pizzas: List[PizzaResponse]
    total: int
