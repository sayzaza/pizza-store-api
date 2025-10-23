"""
Pizza-related API routes
"""

from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database.connection import get_db
from app.models.pizza import Pizza
from app.schemas.pizza import PizzaResponse, PizzaListResponse

router = APIRouter(prefix="/pizzas", tags=["pizzas"])


@router.get("/", response_model=PizzaListResponse)
async def get_pizzas(
    search: Optional[str] = Query(None, description="Search pizzas by name or description"),
    sort_by: Optional[str] = Query("name", description="Sort by field (name)"),
    ingredient_filter: Optional[str] = Query(None, description="Filter by ingredient name"),
    allergen_filter: Optional[str] = Query(None, description="Filter by allergen"),
    db: Session = Depends(get_db)
):
    """
    Get all pizzas with optional search, sort, and filter capabilities.
    
    - **search**: Search pizzas by name or description
    - **sort_by**: Sort pizzas by name (default: name)
    - **ingredient_filter**: Filter pizzas that contain specific ingredient
    - **allergen_filter**: Filter pizzas that contain specific allergen
    """
    query = db.query(Pizza)
    
    # Search functionality
    if search:
        query = query.filter(
            (Pizza.name.contains(search)) | 
            (Pizza.description.contains(search))
        )
    
    # Ingredient filter
    if ingredient_filter:
        from app.models.pizza import PizzaIngredient, Ingredient
        query = query.join(PizzaIngredient).join(Ingredient).filter(
            Ingredient.name.contains(ingredient_filter)
        )
    
    # Allergen filter
    if allergen_filter:
        from app.models.pizza import PizzaIngredient, Ingredient
        query = query.join(PizzaIngredient).join(Ingredient).filter(
            Ingredient.is_allergen == True,
            Ingredient.name.contains(allergen_filter)
        )
    
    # Sorting
    if sort_by == "name":
        query = query.order_by(Pizza.name)
    
    pizzas = query.all()
    
    # Convert to response format
    pizza_responses = []
    for pizza in pizzas:
        # Get all ingredients with their sub-ingredients
        ingredients = []
        allergens = []
        
        for ingredient in pizza.ingredients:
            ingredient_data = {
                "id": ingredient.id,
                "name": ingredient.name,
                "is_allergen": ingredient.is_allergen,
                "sub_ingredients": []
            }
            
            # Add sub-ingredients
            for sub_ingredient in ingredient.sub_ingredients:
                ingredient_data["sub_ingredients"].append({
                    "id": sub_ingredient.id,
                    "name": sub_ingredient.name,
                    "is_allergen": sub_ingredient.is_allergen,
                    "sub_ingredients": []
                })
                
                # Collect allergens
                if sub_ingredient.is_allergen:
                    allergens.append(sub_ingredient.name)
            
            ingredients.append(ingredient_data)
            
            # Collect allergens from main ingredients
            if ingredient.is_allergen:
                allergens.append(ingredient.name)
        
        pizza_responses.append(PizzaResponse(
            id=pizza.id,
            name=pizza.name,
            description=pizza.description,
            ingredients=ingredients,
            allergens=list(set(allergens))  # Remove duplicates
        ))
    
    return PizzaListResponse(pizzas=pizza_responses, total=len(pizza_responses))


@router.get("/{pizza_id}", response_model=PizzaResponse)
async def get_pizza(pizza_id: int, db: Session = Depends(get_db)):
    """Get a specific pizza by ID"""
    pizza = db.query(Pizza).filter(Pizza.id == pizza_id).first()
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    
    # Convert to response format (same logic as above)
    ingredients = []
    allergens = []
    
    for ingredient in pizza.ingredients:
        ingredient_data = {
            "id": ingredient.id,
            "name": ingredient.name,
            "is_allergen": ingredient.is_allergen,
            "sub_ingredients": []
        }
        
        for sub_ingredient in ingredient.sub_ingredients:
            ingredient_data["sub_ingredients"].append({
                "id": sub_ingredient.id,
                "name": sub_ingredient.name,
                "is_allergen": sub_ingredient.is_allergen,
                "sub_ingredients": []
            })
            
            if sub_ingredient.is_allergen:
                allergens.append(sub_ingredient.name)
        
        ingredients.append(ingredient_data)
        
        if ingredient.is_allergen:
            allergens.append(ingredient.name)
    
    return PizzaResponse(
        id=pizza.id,
        name=pizza.name,
        description=pizza.description,
        ingredients=ingredients,
        allergens=list(set(allergens))
    )
