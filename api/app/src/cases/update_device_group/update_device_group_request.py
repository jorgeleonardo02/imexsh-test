from typing import List
from pydantic import BaseModel
from typing import Optional

class UpdateDeviceGroupRequest(BaseModel):
    id: Optional[str]=None
    device_name: Optional[str] = None