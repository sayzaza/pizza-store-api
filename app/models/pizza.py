"""
SQLAlchemy models for Pizza Store API
"""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class Pizza(Base):
    """Pizza model representing a pizza with its basic information"""
    __tablename__ = 'pizzas'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    ingredients = relationship("Ingredient", secondary="pizza_ingredients")


class PizzaIngredient(Base):
    """Association table for pizza-ingredient many-to-many relationship"""
    __tablename__ = 'pizza_ingredients'
    
    pizza_id = Column(Integer, ForeignKey('pizzas.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)


class Ingredient(Base):
    """Ingredient model representing individual ingredients"""
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_allergen = Column(Boolean, default=False)
    sub_ingredients = relationship("Ingredient", secondary="ingredient_ingredients")


class IngredientIngredient(Base):
    """Association table for ingredient-ingredient self-referential relationship"""
    __tablename__ = 'ingredient_ingredients'
    
    parent_ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    child_ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
