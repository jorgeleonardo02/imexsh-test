from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DeviceGroupSchema(BaseModel):
    id: int
    device_id: str
    average_before_normalization: float
    average_after_normalization: float
    data_size: int
    created_date: Optional[datetime]
    updated_date: Optional[datetime]

    class Config:
        from_attributes = True