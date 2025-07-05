from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class DeviceGroupRequestFilters(BaseModel):
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

class GetAllDeviceGroupDataRequest(BaseModel):
    id: Optional[int]
    filters: Optional[DeviceGroupRequestFilters]
