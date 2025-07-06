from pydantic import BaseModel

class UpdateDeviceGroupResponse(BaseModel):
    result: bool
    message: str