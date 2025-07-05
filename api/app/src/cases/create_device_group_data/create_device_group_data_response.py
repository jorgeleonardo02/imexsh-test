from pydantic import BaseModel

class CreateDeviceGroupDataResponse(BaseModel):
    result: bool
    message: str