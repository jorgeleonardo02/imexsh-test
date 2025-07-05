from typing import Optional
from pydantic import BaseModel

class Device(BaseModel):
    id: str
    device_name: str