# Pizza Store API - Project Structure

## Clean Architecture Overview

This project follows a professional, scalable folder structure that separates concerns and makes the codebase maintainable and interview-ready.

```
pizza-store-api/
├── app/                          # Main application package
│   ├── __init__.py              # Package initialization
│   ├── models/                  # Database models
│   │   ├── __init__.py         # Models package
│   │   └── pizza.py            # Pizza, Ingredient, and relationship models
│   ├── schemas/                 # Pydantic schemas
│   │   ├── __init__.py         # Schemas package
│   │   └── pizza.py            # API response schemas
│   ├── routers/                 # API route handlers
│   │   ├── __init__.py         # Routers package
│   │   ├── pizza.py            # Pizza-related endpoints
│   │   └── ingredients.py      # Ingredient-related endpoints
│   └── database/                # Database configuration
│       ├── __init__.py         # Database package
│       ├── base.py             # Database base and engine
│       └── connection.py       # Session management
├── main.py                      # FastAPI application entry point
├── seed_data.py                 # Database seeding script
├── test_api.py                  # API testing script
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── PROJECT_STRUCTURE.md        # This file
```

## Architecture Benefits

### **1. Separation of Concerns**
- **Models**: Database entities and relationships
- **Schemas**: API request/response validation
- **Routers**: HTTP endpoint logic
- **Database**: Connection and session management

### **2. Scalability**
- Easy to add new features without affecting existing code
- Clear boundaries between different layers
- Modular design allows for easy testing and maintenance

### **3. Professional Standards**
- Follows FastAPI best practices
- Clean import structure
- Proper package organization
- Interview-ready code quality

## File Descriptions

### **Core Application Files**

#### `main.py`
- FastAPI application entry point
- Router registration
- Database table creation
- Clean and minimal (only 34 lines!)

#### `app/models/pizza.py`
- SQLAlchemy models for Pizza, Ingredient, and relationships
- Database table definitions
- Relationship configurations

#### `app/schemas/pizza.py`
- Pydantic models for API responses
- Data validation and serialization
- Type safety for API endpoints

#### `app/routers/pizza.py`
- Pizza-related API endpoints
- Business logic for pizza operations
- Search, filter, and sort functionality

#### `app/routers/ingredients.py`
- Ingredient-related API endpoints
- Simple CRUD operations for ingredients

#### `app/database/base.py`
- Database engine configuration
- Session factory setup
- Base class for models

#### `app/database/connection.py`
- Database session dependency
- Connection management
- Proper resource cleanup

### **Utility Files**

#### `seed_data.py`
- Database population script
- Sample pizza and ingredient data
- Easy to run and modify

#### `test_api.py`
- Comprehensive API testing
- Demonstrates all functionality
- Ready for interview demonstration

## Key Improvements

### **Before (Single File)**
- 235 lines in `main.py`
- Mixed concerns (models, schemas, routes)
- Hard to maintain and extend
- Not interview-ready

### **After (Clean Structure)**
- Clean separation of concerns
- Professional folder structure
- Easy to maintain and extend
- Interview-ready code quality
- Scalable architecture

## Interview Benefits

This structure demonstrates:

1. **Professional Code Organization**: Clear separation of concerns
2. **Scalable Architecture**: Easy to extend with new features
3. **FastAPI Best Practices**: Proper use of routers, dependencies, and schemas
4. **Database Design**: Clean model definitions and relationships
5. **Maintainability**: Easy to understand and modify
6. **Testing Ready**: Clear structure for unit and integration tests

## Development Workflow

1. **Add New Models**: Create in `app/models/`
2. **Add New Schemas**: Create in `app/schemas/`
3. **Add New Routes**: Create in `app/routers/`
4. **Database Changes**: Update `app/database/`
5. **Testing**: Use `test_api.py` for validation

This structure makes the codebase professional, maintainable, and perfect for demonstrating your skills in a technical interview! 🚀
