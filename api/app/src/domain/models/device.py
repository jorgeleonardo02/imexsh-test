from typing import Optional
from pydantic import BaseModel

class Device(BaseModel):
    id: Optional[str]=None
    device_id: str
    device_name: str