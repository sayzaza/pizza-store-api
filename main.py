"""
Pizza Store API - FastAPI Backend
A comprehensive API for browsing pizzas with search, sort, and filter capabilities.
"""

from fastapi import FastAPI
from app.database.base import Base, engine
from app.routers import pizza_router, ingredients_router

# Create FastAPI app
app = FastAPI(
    title="Pizza Store API",
    description="API for browsing pizzas with search, sort, and filter capabilities",
    version="1.0.0"
)

# Include routers
app.include_router(pizza_router)
app.include_router(ingredients_router)

# Create database tables
Base.metadata.create_all(bind=engine)


@app.get("/", response_model=dict)
async def root():
    """Welcome endpoint"""
    return {"message": "Welcome to Pizza Store API", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
