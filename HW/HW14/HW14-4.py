from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")

items = [
    {"name": "Apple", "price": 30},
    {"name": "Orange", "price": 10},
    {"name": "Potato", "price": 20},
    {"name": "Tomato", "price": 50},
    {"name": "Onion", "price": 40},
]


@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request, sort: Optional[str] = None):
    if sort == "asc":
        sorted_items = sorted(items, key=lambda x: x["price"])
    elif sort == "desc":
        sorted_items = sorted(items, key=lambda x: x["price"])[::-1]
    else:
        sorted_items = items

    return templates.TemplateResponse("items.html", {"request": request, "items": sorted_items})

