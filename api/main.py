from typing import Union

from fastapi import FastAPI
from app.web_app.routes import device_group_router

app = FastAPI()
app.include_router(device_group_router)
