from fastapi import FastAPI

app = FastAPI()

# Items list
items = [
    {"id": 1, "name": "Notebook", "price": 50, "category": "Stationery", "in_stock": True},
    {"id": 2, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Monitor", "price": 7000, "category": "Electronics", "in_stock": False},

    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

# Show all items
@app.get("/products")
def show_items():
    return {
        "items": items,
        "total_items": len(items)
    }

# Filter items by category
@app.get("/products/category/{cat_name}")
def category_items(cat_name: str):
    filtered_items = [i for i in items if i["category"] == cat_name]

    if not filtered_items:
        return {"error": "No products found in this category"}

    return {
        "category": cat_name,
        "items": filtered_items,
        "count": len(filtered_items)
    }

# Only available items
@app.get("/products/instock")
def available_items():
    available_list = [i for i in items if i["in_stock"] == True]

    return {
        "available_items": available_list,
        "count": len(available_list)
    }

# Store information
@app.get("/store/summary")
def store_info():
    stock_count = len([i for i in items if i["in_stock"]])
    out_stock = len(items) - stock_count
    category_list = list(set([i["category"] for i in items]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(items),
        "in_stock": stock_count,
        "out_of_stock": out_stock,
        "categories": category_list
    }

# Search items
@app.get("/products/search/{word}")
def search_items(word: str):

    search_result = [
        i for i in items
        if word.lower() in i["title"].lower()
    ]

    if not search_result:
        return {"message": "No products matched your search"}

    return {
        "keyword": word,
        "results": search_result,
        "matches": len(search_result)
    }

# Cheapest and most expensive
@app.get("/products/deals")
def item_deals():
    cheapest_item = min(items, key=lambda i: i["price"])
    expensive_item = max(items, key=lambda i: i["price"])

    return {
        "best_deal": cheapest_item,
        "premium_pick": expensive_item
    }