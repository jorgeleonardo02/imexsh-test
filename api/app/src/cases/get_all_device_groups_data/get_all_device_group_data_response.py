from pydantic import BaseModel
from typing import List
from app.src.domain.models.device_group import DeviceGroup
from app.src.shemas.device_group_schema import DeviceGroupSchema

class GetAllDeviceGroupDataResponse(BaseModel):
    device_groups: List[DeviceGroupSchema]