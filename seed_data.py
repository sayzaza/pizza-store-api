"""
Data seeding script for Pizza Store API
Populates the database with sample pizza and ingredient data
"""

from sqlalchemy.orm import sessionmaker
from app.database.base import engine, Base
from app.models.pizza import Pizza, Ingredient, PizzaIngredient, IngredientIngredient

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_database():
    """Seed the database with sample data"""
    db = SessionLocal()
    
    try:
        # Create ingredients
        ingredients_data = [
            # Base ingredients
            {"name": "Tomato Sauce", "is_allergen": False},
            {"name": "Mozzarella Cheese", "is_allergen": True},  # Dairy allergen
            {"name": "Pepperoni", "is_allergen": False},
            {"name": "Mushrooms", "is_allergen": False},
            {"name": "Bell Peppers", "is_allergen": False},
            {"name": "Onions", "is_allergen": False},
            {"name": "Olives", "is_allergen": False},
            {"name": "Pineapple", "is_allergen": False},
            {"name": "Ham", "is_allergen": False},
            {"name": "Bacon", "is_allergen": False},
            {"name": "Sausage", "is_allergen": False},
            {"name": "Chicken", "is_allergen": False},
            {"name": "Basil", "is_allergen": False},
            {"name": "Garlic", "is_allergen": False},
            {"name": "Parmesan Cheese", "is_allergen": True},  # Dairy allergen
            {"name": "Feta Cheese", "is_allergen": True},  # Dairy allergen
            {"name": "Goat Cheese", "is_allergen": True},  # Dairy allergen
            {"name": "Pesto Sauce", "is_allergen": False},
            {"name": "Alfredo Sauce", "is_allergen": True},  # Dairy allergen
            {"name": "BBQ Sauce", "is_allergen": False},
            {"name": "Jalapeños", "is_allergen": False},
            {"name": "Spinach", "is_allergen": False},
            {"name": "Artichokes", "is_allergen": False},
            {"name": "Sun-dried Tomatoes", "is_allergen": False},
            {"name": "Arugula", "is_allergen": False},
            {"name": "Prosciutto", "is_allergen": False},
            {"name": "Anchovies", "is_allergen": True},  # Fish allergen
            {"name": "Shrimp", "is_allergen": True},  # Shellfish allergen
            {"name": "Gluten-Free Dough", "is_allergen": False},
            {"name": "Regular Dough", "is_allergen": True},  # Gluten allergen
        ]
        
        ingredients = []
        for ing_data in ingredients_data:
            ingredient = Ingredient(**ing_data)
            db.add(ingredient)
            ingredients.append(ingredient)
        
        db.commit()
        
        # Create ingredient relationships (sub-ingredients)
        # For example, some ingredients might have sub-ingredients
        # This is a simplified example - in reality, you'd have more complex relationships
        
        # Create pizzas
        pizzas_data = [
            {
                "name": "Margherita",
                "description": "Classic Italian pizza with fresh tomatoes, mozzarella, and basil",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Basil"]
            },
            {
                "name": "Pepperoni",
                "description": "Traditional pepperoni pizza with mozzarella cheese",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni"]
            },
            {
                "name": "Supreme",
                "description": "Loaded with pepperoni, sausage, mushrooms, bell peppers, and onions",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni", "Sausage", "Mushrooms", "Bell Peppers", "Onions"]
            },
            {
                "name": "Hawaiian",
                "description": "Sweet and savory combination of ham and pineapple",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Ham", "Pineapple"]
            },
            {
                "name": "Meat Lovers",
                "description": "For the carnivore in you - pepperoni, sausage, bacon, and ham",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni", "Sausage", "Bacon", "Ham"]
            },
            {
                "name": "Veggie Deluxe",
                "description": "Fresh vegetables including mushrooms, bell peppers, onions, olives, and spinach",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Mushrooms", "Bell Peppers", "Onions", "Olives", "Spinach"]
            },
            {
                "name": "BBQ Chicken",
                "description": "Grilled chicken with BBQ sauce, red onions, and cilantro",
                "ingredient_names": ["BBQ Sauce", "Mozzarella Cheese", "Chicken", "Onions"]
            },
            {
                "name": "Mediterranean",
                "description": "Mediterranean flavors with feta cheese, olives, artichokes, and sun-dried tomatoes",
                "ingredient_names": ["Tomato Sauce", "Feta Cheese", "Olives", "Artichokes", "Sun-dried Tomatoes"]
            },
            {
                "name": "Pesto Chicken",
                "description": "Grilled chicken with pesto sauce, mozzarella, and fresh arugula",
                "ingredient_names": ["Pesto Sauce", "Mozzarella Cheese", "Chicken", "Arugula"]
            },
            {
                "name": "Quattro Stagioni",
                "description": "Four seasons pizza with artichokes, mushrooms, prosciutto, and olives",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Artichokes", "Mushrooms", "Prosciutto", "Olives"]
            },
            {
                "name": "Seafood Special",
                "description": "Fresh seafood with shrimp and anchovies",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Shrimp", "Anchovies"]
            },
            {
                "name": "Gluten-Free Margherita",
                "description": "Classic margherita made with gluten-free dough",
                "ingredient_names": ["Tomato Sauce", "Mozzarella Cheese", "Basil", "Gluten-Free Dough"]
            }
        ]
        
        for pizza_data in pizzas_data:
            pizza = Pizza(
                name=pizza_data["name"],
                description=pizza_data["description"]
            )
            db.add(pizza)
            db.flush()  # Get the pizza ID
            
            # Add ingredients to pizza
            for ingredient_name in pizza_data["ingredient_names"]:
                ingredient = db.query(Ingredient).filter(Ingredient.name == ingredient_name).first()
                if ingredient:
                    pizza_ingredient = PizzaIngredient(
                        pizza_id=pizza.id,
                        ingredient_id=ingredient.id
                    )
                    db.add(pizza_ingredient)
        
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
