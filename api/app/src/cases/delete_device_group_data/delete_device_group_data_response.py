from pydantic import BaseModel

class DeleteDeviceGroupDataResponse(BaseModel):
    result: bool
    message: str