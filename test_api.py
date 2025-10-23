"""
Test script for Pizza Store API
Demonstrates all API functionality with example requests
"""

import requests
import json
import os

# Set environment to avoid proxy issues
os.environ['NO_PROXY'] = 'localhost,127.0.0.1'

BASE_URL = "http://127.0.0.1:8000"
PROXIES = {'http': None, 'https': None}

def test_api():
    """Test all API endpoints with example requests"""
    
    print("Pizza Store API Test Suite")
    print("=" * 50)
    
    # Test 1: Get all pizzas
    print("\n1. Getting all pizzas...")
    response = requests.get(f"{BASE_URL}/pizzas", proxies=PROXIES)
    if response.status_code == 200:
        data = response.json()
        print(f"Found {data['total']} pizzas")
        print(f"   First pizza: {data['pizzas'][0]['name']}")
    else:
        print(f"Error: {response.status_code}")
    
    # Test 2: Search functionality
    print("\n2. Searching for 'margherita'...")
    response = requests.get(f"{BASE_URL}/pizzas?search=margherita", proxies=PROXIES)
    if response.status_code == 200:
        data = response.json()
        print(f"Found {data['total']} margherita pizzas")
        for pizza in data['pizzas']:
            print(f" - {pizza['name']}: {pizza['description']}")
    else:
        print(f"Error: {response.status_code}")
    
    # Test 3: Filter by ingredient
    print("\n3. Filtering by ingredient 'cheese'...")
    response = requests.get(f"{BASE_URL}/pizzas?ingredient_filter=cheese", proxies=PROXIES)
    if response.status_code == 200:
        data = response.json()
        print(f"Found {data['total']} pizzas with cheese")
        for pizza in data['pizzas']:
            print(f" - {pizza['name']}")
    else:
        print(f"Error: {response.status_code}")
    
    # Test 4: Filter by allergen
    print("\n4. Filtering by allergen 'dairy'...")
    response = requests.get(f"{BASE_URL}/pizzas?allergen_filter=dairy", proxies=PROXIES)
    if response.status_code == 200:
        data = response.json()
        print(f"Found {data['total']} pizzas with dairy allergens")
        for pizza in data['pizzas']:
            print(f"   - {pizza['name']} (allergens: {', '.join(pizza['allergens'])})")
    else:
        print(f"Error: {response.status_code}")
    
    # Test 5: Get specific pizza
    print("\n5. Getting specific pizza (ID: 1)...")
    response = requests.get(f"{BASE_URL}/pizzas/1", proxies=PROXIES)
    if response.status_code == 200:
        pizza = response.json()
        print(f"Pizza: {pizza['name']}")
        print(f"Description: {pizza['description']}")
        print(f"Ingredients: {', '.join([ing['name'] for ing in pizza['ingredients']])}")
        print(f"Allergens: {', '.join(pizza['allergens'])}")
    else:
        print(f"Error: {response.status_code}")
    
    # Test 6: Get all ingredients
    print("\n6. Getting all ingredients...")
    response = requests.get(f"{BASE_URL}/ingredients", proxies=PROXIES)
    if response.status_code == 200:
        ingredients = response.json()
        print(f"Found {len(ingredients)} ingredients")
        allergen_count = sum(1 for ing in ingredients if ing['is_allergen'])
        print(f"Allergens: {allergen_count}")
        print(f"Non-allergens: {len(ingredients) - allergen_count}")
    else:
        print(f"Error: {response.status_code}")
    
    # Test 7: Combined filters
    print("\n7. Combined search and filter...")
    response = requests.get(f"{BASE_URL}/pizzas?search=chicken&ingredient_filter=cheese", proxies=PROXIES)
    if response.status_code == 200:
        data = response.json()
        print(f"Found {data['total']} chicken pizzas with cheese")
        for pizza in data['pizzas']:
            print(f"- {pizza['name']}")
    else:
        print(f"Error: {response.status_code}")
    
    print("\n" + "=" * 50)
    print("API testing completed!")
    print(f"Interactive docs: {BASE_URL}/docs")
    print(f"ReDoc: {BASE_URL}/redoc")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API server.")
        print("Make sure the server is running on http://localhost:8000")
        print("Run: python main.py")
    except Exception as e:
        print(f"Error: {e}")
