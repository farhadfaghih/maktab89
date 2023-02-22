from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/total_price/")
async def calculate_total_price(items: List[Item]):
    total_price = sum(item.price for item in items)
    return {"total_price": total_price}


# example json:
# [
#     {"name": "item1", "price": 10.99},
#     {"name": "item2", "price": 5.99},
#     {"name": "item3", "price": 7.99}
# ]
# Response body:
# {
#   "total_price": 24.97
# }