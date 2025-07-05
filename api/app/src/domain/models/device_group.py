from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class DeviceGroup(BaseModel):
    id: Optional[int]=None
    device_id: str
    average_before_normalization: float
    average_after_normalization: float
    data_size: int
    created_date: datetime
    updated_date: Optional[datetime]

class DeviceGroupRequestFilters(BaseModel):
    id: Optional[int] = None
    created_date_from: Optional[datetime]=None
    created_date_to: Optional[datetime]=None
    updated_date_from: Optional[datetime]=None
    updated_date_to: Optional[datetime]=None
    average_before_normalization_from: Optional[float]=None
    average_before_normalization_to: Optional[float]=None
    average_after_normalization_from: Optional[float]=None
    average_after_normalization_to: Optional[float]=None
    data_size_from: Optional[int]=None
    data_size_to: Optional[int]=None