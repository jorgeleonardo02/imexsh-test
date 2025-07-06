from fastapi import HTTPException
from app.src.cases.update_device_group import UpdateDeviceGroupRequest, UpdateDeviceGroupResponse

from app.src.domain.repositories import DeviceGroupDataRepository, DeviceRepository

class UpdateDeviceGroupUseCase:
    def __init__(self,
                 device_group_repository: DeviceGroupDataRepository,
                 device_repository: DeviceRepository):
        self.device_group_repository = device_group_repository
        self.device_repository = device_repository
    async def execute(self, id: int, update_device_group_request: UpdateDeviceGroupRequest) -> UpdateDeviceGroupResponse:
        new_device_group_id = update_device_group_request.id
        new_device_name = update_device_group_request.device_name

        device_group = await self.device_group_repository.get_by_id(id)
        device_id = device_group.device_id
        device = await self.device_repository.get_by_device_id(device_id)

        if not device_group or not device:
            self.__raise_exception(404, "Datos no encontrados")
        
        if new_device_group_id is not None:
            device.device_id = new_device_group_id
            device_group.device_id = new_device_group_id

        if new_device_name is not None:
            device.device_name = new_device_name
            device_group.device_name = new_device_name

            # Guarda
            result_device = await self.device_repository.update(device=device)
            result_group = await self.device_group_repository.update(device_group=device_group)

            # Devuelve OK o error
            if result_device and result_group:
                message = "Device y Device group actualizados exitosamente"
                return UpdateDeviceGroupResponse(result=True, message=message)
            else:
                self.__raise_exception(500, "Error al actualizar los datos")

    def __raise_exception(self, status_code: int, message: str) -> None:
        raise HTTPException(
            status_code=status_code,
            detail=message
        )
