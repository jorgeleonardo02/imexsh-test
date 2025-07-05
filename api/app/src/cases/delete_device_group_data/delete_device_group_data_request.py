from pydantic import BaseModel

class DeleteDeviceGroupDataRequest(BaseModel):
    id: int