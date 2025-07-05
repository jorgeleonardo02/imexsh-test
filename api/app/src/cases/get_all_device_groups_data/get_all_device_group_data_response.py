from pydantic import BaseModel
from typing import List
from app.src.domain.models.device_group import DeviceGroup

class GetAllDeviceGroupDataResponse(BaseModel):
    device_groups: List[DeviceGroup]