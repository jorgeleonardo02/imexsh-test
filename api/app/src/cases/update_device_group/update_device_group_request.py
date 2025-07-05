from typing import List
from pydantic import BaseModel

class UpdateDeviceGroupRequest(BaseModel):
    id: str
    device_name: str