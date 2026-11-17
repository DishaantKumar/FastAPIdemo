from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 25.50}
]

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def create_item(item: Item):
    new_item = {"id": len(items) + 1, "name": item.name, "price": item.price}
    items.append(new_item)
    return {"message": "Item added!", "item": new_item}
