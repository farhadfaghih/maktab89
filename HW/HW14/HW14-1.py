from fastapi import FastAPI
from typing import Optional

app = FastAPI()

items = [
    {'id': 1, 'name': 'Apple', 'description': 'A round fruit with a red or green skin'},
    {'id': 2, 'name': 'Banana', 'description': 'A long curved fruit with a yellow skin'},
    {'id': 3, 'name': 'Orange', 'description': 'A round fruit with an orange skin'},
    {'id': 4, 'name': 'Grapes', 'description': 'A small fruit that grows in clusters'},
    {'id': 5, 'name': 'Mango', 'description': 'A tropical fruit with a sweet juicy flesh'}
]


# Define the search endpoint
@app.get("/search")
def search(q: Optional[str] = None):
    if not q:
        return {'error': 'There is no search term!'}
    result = [item for item in items if q.lower() in item['name'].lower() or q.lower() in item['description'].lower()]
    # # Next 4 lines are equal to line 21
    # result = []
    # for item in items:
    #     if q.lower() in item['name'].lower() or q.lower() in item['description'].lower():
    #         result.append(item)
    return result
