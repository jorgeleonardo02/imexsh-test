from typing import List, Optional
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse

from app.dependencies_factory.use_cases import (
    create_device_group_use_case,
    delete_device_group_use_case,
    update_device_group_use_case,
    get_all_device_groups_use_case,
)

from app.src.cases.create_device_group_data import CreateDeviceGroupDataUseCase, CreateDeviceGroupDataResponse, CreateDeviceGroupDataRequest
from app.src.cases.get_all_device_groups_data import GetAllDeviceGroupDataRequest, GetAllDeviceGroupDataResponse, GetAllDeviceGroupsDataUseCase
from app.src.cases.delete_device_group_data import DeleteDeviceGroupDataUseCase, DeleteDeviceGroupDataResponse, DeleteDeviceGroupDataRequest
from app.src.cases.update_device_group import UpdateDeviceGroupRequest, UpdateDeviceGroupResponse, UpdateDeviceGroupUseCase
from app.src.domain.models.device_group import DeviceGroup, DeviceGroupRequestFilters

device_group_router = APIRouter(prefix="/device_groups")

@device_group_router.get("/")
async def device_groups(
        id: int = None,
        filters: DeviceGroupRequestFilters = None
    ) -> List[DeviceGroup]:
    request = GetAllDeviceGroupDataRequest(id=id, filters=filters)
    use_case = get_all_device_groups_use_case() 
    result = await use_case.execute(request)
    return result

@device_group_router.post("/")
async def create_device_group(request: CreateDeviceGroupDataRequest)-> CreateDeviceGroupDataResponse:  #recibe un usuario y devuelve un CreateUserResponse
    # request = CreateDeviceGroupDataRequest(device_group)  #encapsular el usuario en CreateUserRequest
    use_case = create_device_group_use_case()
    result = await use_case.execute(request) #ejecutar el caso de uso
    return result #devolver el resultado

@device_group_router.put("/")  #ruta para actualizar un usuario
async def update_device_group(id: Optional[int] = None, device_name: Optional[str]=None) -> UpdateDeviceGroupResponse:  #recibe un usuario y devuelve un CreateUserResponse
    request = UpdateDeviceGroupRequest(id=id, device_name=device_name)  #encapsular el usuario en CreateUserRequest    
    use_case = update_device_group_use_case() #instanciar el caso de uso
    result = await use_case.execute(update_device_group_request=request) #ejecutar el caso de uso
    return result


@device_group_router.delete("/{id}")
async def delete_device_group(id: int):
    request = DeleteDeviceGroupDataRequest(id)  # Encapsular el ID en un request
    user_case = delete_device_group_use_case()
    result = await user_case.execute(request)
    return result
