from pydantic import RootModel
from typing import Dict, List
from pydantic import BaseModel, Field

class DeviceRequest(BaseModel):
    id: str
    data: List[str]
    device_name: str = Field(... , alias="deviceName")

class CreateDeviceGroupDataRequest(RootModel[Dict[str, DeviceRequest]]):
    pass