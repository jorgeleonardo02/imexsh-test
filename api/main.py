from typing import Union

from fastapi import FastAPI
from app.web_app.routes import device_group_router

app = FastAPI()
app.include_router(device_group_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}