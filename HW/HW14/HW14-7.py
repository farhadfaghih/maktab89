from fastapi import FastAPI
from typing import List

app = FastAPI()


@app.post("/sum_even_numbers/")
async def sum_even_numbers(numbers: List[int]) -> int:
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sum(even_numbers)


# example list:
# [1,2,3,4,5,6,7,8,9,8,8]
# result:
# 36
