# Pizza Store API

A modern FastAPI backend for browsing pizzas with advanced search, filtering, and sorting capabilities.

## 📋 Project Summary

### Overview
The Pizza Store API is a comprehensive RESTful web service built with FastAPI that provides advanced pizza browsing capabilities. It features sophisticated search, filtering, and sorting functionality with professional-grade code architecture suitable for production environments.

### Key Features
- **Advanced Search**: Full-text search across pizza names and descriptions
- **Smart Filtering**: Filter by ingredients and allergens with sub-ingredient support
- **Professional Sorting**: Multiple sort fields (name, id, description) with asc/desc order
- **Allergen Detection**: Automatic detection from main ingredients and sub-ingredients
- **Auto Documentation**: Interactive Swagger UI and ReDoc documentation
- **Clean Architecture**: Modular design with separation of concerns

### Technical Stack
- **Backend**: FastAPI (Python 3.8+)
- **Database**: SQLAlchemy ORM with SQLite
- **Validation**: Pydantic for data validation
- **Documentation**: Auto-generated OpenAPI/Swagger
- **Server**: Uvicorn ASGI server

### Architecture Highlights
- **RESTful Design**: Resource-based URLs with proper HTTP methods
- **Type Safety**: Full type hints with Pydantic validation
- **Database Design**: Efficient relational schema with proper indexing
- **Error Handling**: Comprehensive HTTP exception handling
- **Scalability**: Modular structure for easy feature addition

### Use Cases
- **E-commerce**: Pizza ordering systems
- **Restaurant Management**: Menu browsing and management
- **Food Delivery**: API for delivery platforms
- **Allergen Management**: Food safety and dietary restrictions
- **Menu Analytics**: Search and filtering for business intelligence

### Production Ready
- **Security**: Input validation and SQL injection prevention
- **Performance**: Optimized database queries with proper indexing
- **Monitoring**: Health checks and error tracking ready
- **Documentation**: Complete API documentation with examples
- **Testing**: Comprehensive test coverage and validation

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Setup & Run

   ```bash
# Install dependencies
   pip install -r requirements.txt

# Seed database with sample data
   python seed_data.py

# Run the API server
   python main.py
   ```

The API will be available at `http://localhost:8000`

*Swagger Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📁 Project Structure

```
pizza-store-api/
├── app/
│   ├── database/         # Database configuration
│   ├── models/           # SQLAlchemy models
│   ├── routers/          # API route handlers
│   └── schemas/          # Pydantic schemas
├── main.py              # FastAPI application
├── requirements.txt     # Dependencies
├── seed_data.py         # Database seeding
└── test_api.py          # API testing
```

## 🔧 Key Features

- **Search**: Full-text search across pizza names and descriptions
- **Filtering**: By ingredients and allergens
- **Professional Sorting**: Multiple fields (name, id, description) with asc/desc order
- **Allergen Detection**: Automatic detection from ingredients and sub-ingredients

### Professional Sorting Capabilities

The API provides advanced sorting functionality with:

- **Multiple Sort Fields**: `name`, `id`, `description`
- **Sort Directions**: `asc` (ascending), `desc` (descending)
- **Type Safety**: Enum-based validation for sort parameters
- **Database Optimization**: Efficient SQL ORDER BY clauses
- **Extensible Design**: Easy to add new sort fields

**Example Usage**:
- `GET /pizzas?sort_by=name&sort_order=asc` - Sort by name A-Z
- `GET /pizzas?sort_by=id&sort_order=desc` - Sort by ID descending
- `GET /pizzas?sort_by=description&sort_order=asc` - Sort by description A-Z

---

## 1. API Architecture

### HTTP Methods & URL Structure

**Base URL**: `http://localhost:8000`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome endpoint |
| `GET` | `/pizzas` | Get all pizzas with filtering |
| `GET` | `/pizzas/{id}` | Get specific pizza |
| `GET` | `/ingredients` | Get all ingredients |

### Query Parameters
- `search` - Search pizzas by name/description
- `sort_by` - Sort results by field (name, id, description)
- `sort_order` - Sort order (asc, desc)
- `ingredient_filter` - Filter by ingredient
- `allergen_filter` - Filter by allergen

### Design Principles
1. **RESTful URLs**: Resource-based endpoints
2. **Hierarchical Structure**: `/pizzas/{id}` pattern
3. **Query Parameters**: Flexible filtering
4. **Consistent Naming**: Plural nouns for collections

---

## 2. Essential Services & Libraries

### Core Dependencies
- **FastAPI** - Modern web framework with automatic OpenAPI docs
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation and serialization
- **SQLite** - Lightweight database for development
- **Uvicorn** - ASGI server

### Production Considerations
- **PostgreSQL** - Production database
- **Redis** - Caching layer
- **JWT** - Authentication
- **Prometheus** - Monitoring

---

## 3. FastAPI Routes & Pydantic Schemas

### Application Setup

```python
from fastapi import FastAPI
from app.database.base import Base, engine
from app.routers import pizza_router, ingredients_router

app = FastAPI(
    title="Pizza Store API",
    description="API for browsing pizzas with search, sort, and filter capabilities",
    version="1.0.0"
)

app.include_router(pizza_router)
app.include_router(ingredients_router)
Base.metadata.create_all(bind=engine)
```

### Pydantic Schemas

```python
from pydantic import BaseModel
from typing import List

class IngredientResponse(BaseModel):
    id: int
    name: str
    is_allergen: bool
    sub_ingredients: List['IngredientResponse'] = []

class PizzaResponse(BaseModel):
    id: int
    name: str
    description: str
    ingredients: List[IngredientResponse] = []
    allergens: List[str] = []

class PizzaListResponse(BaseModel):
    pizzas: List[PizzaResponse]
    total: int
```

### Route Declarations

```python
from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from typing import Optional
from enum import Enum

class SortField(str, Enum):
    """Available sorting fields for pizzas"""
    NAME = "name"
    ID = "id"
    DESCRIPTION = "description"

class SortOrder(str, Enum):
    """Available sorting orders"""
    ASC = "asc"
    DESC = "desc"

router = APIRouter(prefix="/pizzas", tags=["pizzas"])

@router.get("/", response_model=PizzaListResponse)
async def get_pizzas(
    search: Optional[str] = Query(None, description="Search pizzas by name or description"),
    sort_by: SortField = Query(SortField.NAME, description="Sort by field (name, id, description)"),
    sort_order: SortOrder = Query(SortOrder.ASC, description="Sort order (asc, desc)"),
    ingredient_filter: Optional[str] = Query(None, description="Filter by ingredient name"),
    allergen_filter: Optional[str] = Query(None, description="Filter by allergen"),
    db: Session = Depends(get_db)
):
    """Get all pizzas with professional sorting and filtering"""

@router.get("/{pizza_id}", response_model=PizzaResponse)
async def get_pizza(pizza_id: int, db: Session = Depends(get_db)):
    """Get specific pizza by ID"""
```

---

## 4. Endpoint Logic Examples

### GET /pizzas - Filtered Pizza Listing

```python
async def get_pizzas(
    search: Optional[str] = None,
    sort_by: SortField = SortField.NAME,
    sort_order: SortOrder = SortOrder.ASC,
    ingredient_filter: Optional[str] = None,
    allergen_filter: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Professional Sorting Business Logic:
    1. Start with base query for all pizzas
    2. Apply search filter (name or description contains search term)
    3. Apply ingredient filter (pizza must contain ingredient)
    4. Apply allergen filter (pizza must contain allergen)
    5. Apply professional sorting with multiple fields and directions
    6. Execute query and transform results
    7. Return formatted response
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
        query = query.join(PizzaIngredient).join(Ingredient).filter(
            Ingredient.name.contains(ingredient_filter)
        )
    
    # Allergen filter
    if allergen_filter:
        query = query.join(PizzaIngredient).join(Ingredient).filter(
            Ingredient.is_allergen == True,
            Ingredient.name.contains(allergen_filter)
        )
    
    # Professional sorting implementation
    sort_column = get_sort_column(sort_by)
    sort_direction = desc if sort_order == SortOrder.DESC else asc
    query = query.order_by(sort_direction(sort_column))
    
    pizzas = query.all()
    return transform_pizzas_to_response(pizzas)

def get_sort_column(sort_field: SortField):
    """Helper function to get the appropriate column for sorting"""
    sort_mapping = {
        SortField.NAME: Pizza.name,
        SortField.ID: Pizza.id,
        SortField.DESCRIPTION: Pizza.description
    }
    return sort_mapping[sort_field]
```

### GET /pizzas/{id} - Specific Pizza

```python
async def get_pizza(pizza_id: int, db: Session = Depends(get_db)):
    """
    Business Logic:
    1. Query database for pizza with specific ID
    2. Check if pizza exists
    3. If not found, raise 404 HTTP exception
    4. If found, transform and return response
    """
    pizza = db.query(Pizza).filter(Pizza.id == pizza_id).first()
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    
    return transform_pizza_to_response(pizza)
```

### GET /ingredients - All Ingredients

```python
async def get_ingredients(db: Session = Depends(get_db)):
    """
    Business Logic:
    1. Query database for all ingredients
    2. Include sub-ingredients for each ingredient
    3. Return formatted list
    """
    ingredients = db.query(Ingredient).all()
    return transform_ingredients_to_response(ingredients)
```

---

## 🗄️ Database Schema

```python
class Pizza(Base):
    __tablename__ = 'pizzas'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    ingredients = relationship("Ingredient", secondary="pizza_ingredients", back_populates="pizzas")

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_allergen = Column(Boolean, default=False)
    pizzas = relationship("Pizza", secondary="pizza_ingredients", back_populates="ingredients")
    sub_ingredients = relationship("Ingredient", secondary="ingredient_ingredients", ...)
```

---

## 📊 API Response Examples

### Successful Response
```json
{
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "description": "Classic Italian pizza with fresh tomatoes, mozzarella, and basil",
      "ingredients": [
        {
          "id": 1,
          "name": "Tomato Sauce",
          "is_allergen": false,
          "sub_ingredients": []
        },
        {
          "id": 2,
          "name": "Mozzarella Cheese",
          "is_allergen": true,
          "sub_ingredients": []
        }
      ],
      "allergens": ["Mozzarella Cheese"]
    }
  ],
  "total": 1
}
```

### Error Response
```json
{
  "detail": "Pizza not found"
}
```

---

## 🏗️ Architecture Benefits

- **Scalability**: Modular design for easy feature addition
- **Maintainability**: Type-safe code with Pydantic validation
- **Performance**: Efficient database queries with proper indexing
- **Documentation**: Auto-generated OpenAPI documentation

---

*This API provides a solid foundation for a pizza ordering system with room for future enhancements like user authentication, order management, and payment processing.*