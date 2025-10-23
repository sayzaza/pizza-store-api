# Pizza Store API

A comprehensive FastAPI backend for browsing pizzas with advanced search, sort, and filter capabilities.

## Features

- **Browse Pizzas**: View all available pizzas with detailed information
- **Search**: Search pizzas by name or description
- **Sort**: Sort pizzas by name
- **Filter by Ingredients**: Filter pizzas that contain specific ingredients
- **Filter by Allergens**: Filter pizzas that contain specific allergens (including sub-ingredients)
- **Detailed Pizza Information**: Each pizza includes name, description, ingredients, and potential allergens

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Seed the database with sample data:
   ```bash
   python seed_data.py
   ```

4. Run the API server:
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:8000`

## API Documentation

### Base URL
```
http://localhost:8000
```

### Interactive API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔗 API Endpoints

### 1. Get All Pizzas
**GET** `/pizzas`

Retrieve all pizzas with optional search, sort, and filter capabilities.

**Query Parameters:**
- `search` (optional): Search pizzas by name or description
- `sort_by` (optional): Sort by field (default: "name")
- `ingredient_filter` (optional): Filter pizzas that contain specific ingredient
- `allergen_filter` (optional): Filter pizzas that contain specific allergen

**Example Requests:**
```bash
# Get all pizzas
GET /pizzas

# Search for pizzas containing "margherita"
GET /pizzas?search=margherita

# Filter pizzas containing "cheese"
GET /pizzas?ingredient_filter=cheese

# Filter pizzas containing dairy allergens
GET /pizzas?allergen_filter=dairy

# Combined filters
GET /pizzas?search=chicken&ingredient_filter=cheese&sort_by=name
```

**Response:**
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

### 2. Get Specific Pizza
**GET** `/pizzas/{pizza_id}`

Retrieve a specific pizza by ID.

**Example:**
```bash
GET /pizzas/1
```

**Response:**
```json
{
  "id": 1,
  "name": "Margherita",
  "description": "Classic Italian pizza with fresh tomatoes, mozzarella, and basil",
  "ingredients": [...],
  "allergens": ["Mozzarella Cheese"]
}
```

### 3. Get All Ingredients
**GET** `/ingredients`

Retrieve all available ingredients.

**Response:**
```json
[
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
]
```

## Architecture

### Database Schema

The API uses SQLAlchemy with the following models:

- **Pizza**: Main pizza entity with name, description, and ingredients
- **Ingredient**: Individual ingredients with allergen information
- **PizzaIngredient**: Many-to-many relationship between pizzas and ingredients
- **IngredientIngredient**: Self-referential relationship for sub-ingredients

### Key Features

1. **Search Functionality**: Full-text search across pizza names and descriptions
2. **Ingredient Filtering**: Filter pizzas by specific ingredients
3. **Allergen Filtering**: Filter pizzas by allergens (including sub-ingredients)
4. **Sorting**: Sort pizzas by various fields
5. **Comprehensive Allergen Detection**: Automatically detects allergens from main ingredients and sub-ingredients

### Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **SQLite**: Lightweight database for development

## Testing the API

### Using curl

```bash
# Get all pizzas
curl -X GET "http://localhost:8000/pizzas"

# Search for margherita
curl -X GET "http://localhost:8000/pizzas?search=margherita"

# Filter by ingredient
curl -X GET "http://localhost:8000/pizzas?ingredient_filter=cheese"

# Filter by allergen
curl -X GET "http://localhost:8000/pizzas?allergen_filter=dairy"
```

### Using the Interactive Documentation

Visit `http://localhost:8000/docs` to use the interactive Swagger UI for testing all endpoints.

## Sample Data

The database is seeded with 12 different pizzas including:

- **Classic Pizzas**: Margherita, Pepperoni, Hawaiian
- **Specialty Pizzas**: Supreme, Meat Lovers, Veggie Deluxe
- **Gourmet Pizzas**: Mediterranean, Pesto Chicken, Quattro Stagioni
- **Dietary Options**: Gluten-Free Margherita
- **Seafood**: Seafood Special

Each pizza includes detailed ingredient information and allergen data.

## 🔧 Development

### Project Structure
```
pizza-store-api/
├── main.py              # FastAPI application and routes
├── seed_data.py         # Database seeding script
├── requirements.txt     # Python dependencies
├── README.md           # This documentation
└── pizza_store.db      # SQLite database (created on first run)
```

### Adding New Pizzas

To add new pizzas, modify the `pizzas_data` list in `seed_data.py` and run the seeding script again.

### Extending the API

The API is designed to be easily extensible. You can add new endpoints, filters, or search capabilities by modifying the FastAPI routes in `main.py`.

## Interview Submission

This implementation demonstrates:

1. **Clean API Design**: RESTful endpoints with clear HTTP methods and URL structures
2. **Comprehensive Functionality**: All required features implemented (search, sort, filter)
3. **Professional Code Quality**: Well-structured code with proper error handling
4. **Database Design**: Efficient relational database schema with proper relationships
5. **Documentation**: Complete API documentation with examples
6. **Scalability**: Architecture that can easily be extended for future requirements

The API successfully addresses all requirements from the take-home test and provides a solid foundation for a production pizza ordering system.
