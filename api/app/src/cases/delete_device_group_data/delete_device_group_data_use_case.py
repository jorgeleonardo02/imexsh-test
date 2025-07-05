from fastapi import HTTPException
from app.src.cases.delete_device_group_data import (
    DeleteDeviceGroupDataResponse,
    DeleteDeviceGroupDataRequest
)
from app.src.domain.repositories import (
    DeviceGroupDataRepository,
    DeviceRepository
)

class DeleteDeviceGroupDataUseCase:
    def __init__(self,
                 device_group_repository: DeviceGroupDataRepository,
                 device_repository: DeviceRepository
        ):
        self.device_group_repository = device_group_repository
        self.device_repository = device_repository

    async def execute(self, request: DeleteDeviceGroupDataRequest) -> DeleteDeviceGroupDataResponse:
        
        device_group = await self.device_group_repository.get_by_device_id(id)
        if not device_group:
            self.__raise_exception(status_code=404, message="device group not found")

        device = await self.device_repository.get_by_id(device_group.device_id)
        if not device:
            self.__raise_exception(status_code=404, message="device not found")
      
        self.device_group_repository.delete(device_group_id=request.id)
        self.device_repository.delete(id=device_group.device_id)

        message = "Device group data deleted successfully."
        return DeleteDeviceGroupDataResponse(result=True, message=message)
    
    def __raise_exception(self, status_code:int, message:str) -> None:
        raise HTTPException(
                status_code=status_code,
                detail=message
            )