from fastapi import HTTPException
from app.src.cases.update_device_group import UpdateDeviceGroupRequest, UpdateDeviceGroupResponse

from app.src.domain.repositories import DeviceGroupDataRepository, DeviceRepository

# acá va la logica de negocio (reglas de negocio)
class UpdateDeviceGroupUseCase:
    def __init__(self,
                 device_group_repository: DeviceGroupDataRepository,
                 device_repository: DeviceRepository):
        self.device_group_repository = device_group_repository
        self.device_repository = device_repository

    async def execute(self, update_device_group_request: UpdateDeviceGroupRequest) -> UpdateDeviceGroupResponse:
        id = update_device_group_request.id
        device_name = update_device_group_request.device_name

        device_group = await self.device_group_repository.get_by_device_id(id)
        device = await self.device_group_repository.get_by_id(id)

        if not device_group or not device:
            self.__raise_exception(404, "Datos no encontrados")
        
        if id is not None:
            device.id = id
            device_group.device_id = id

        if device_name is not None:
            device.device_name = device_name
            device_group.device_name=device_name

        result_group = await self.device_group_repository.update(device_group=device_group)
        result_device = await self.device_repository.update(device=device)

        if result_device and result_group:
            message="Device and Device group actualizados exitosamente"
            return UpdateDeviceGroupResponse(result=True, message=message)
        else:
            self.__raise_exception(500, "Error al actualizar los datos")

    def __raise_exception(self, status_code:int, message:str) -> None:
        raise HTTPException(
                status_code=status_code,
                detail=message
            )