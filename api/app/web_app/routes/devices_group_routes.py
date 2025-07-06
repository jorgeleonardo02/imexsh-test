from typing import Optional
from fastapi import APIRouter

from app.dependencies_factory.use_cases import (
    create_device_group_use_case,
    delete_device_group_use_case,
    update_device_group_use_case,
    get_all_device_groups_use_case,
)

from app.src.cases.create_device_group_data import (
    CreateDeviceGroupDataResponse, CreateDeviceGroupDataRequest
)
from app.src.cases.get_all_device_groups_data import (
    GetAllDeviceGroupDataRequest, GetAllDeviceGroupDataResponse
)
from app.src.cases.delete_device_group_data import DeleteDeviceGroupDataRequest
from app.src.cases.update_device_group import (
    UpdateDeviceGroupRequest, UpdateDeviceGroupResponse
)
from app.src.domain.models.device_group import DeviceGroupRequestFilters

device_group_router = APIRouter(prefix="/device-groups")

@device_group_router.get("/", response_model=GetAllDeviceGroupDataResponse)
async def device_groups(id: int = None, filters: DeviceGroupRequestFilters = None):
    request = GetAllDeviceGroupDataRequest(id=id, filters=filters)
    use_case = get_all_device_groups_use_case() 
    result = await use_case.execute(request)
    return result

@device_group_router.post("/")
async def create_device_group(request: CreateDeviceGroupDataRequest)-> CreateDeviceGroupDataResponse:
    use_case = create_device_group_use_case()
    result = await use_case.execute(request)
    return result

@device_group_router.put("/{id}/")
async def update_device_group(
    id: int,
    device_name: Optional[str] = None,
    new_id: Optional[str] = None
) -> UpdateDeviceGroupResponse:
    request = UpdateDeviceGroupRequest(id=new_id, device_name=device_name)
    use_case = update_device_group_use_case()
    result = await use_case.execute(id, update_device_group_request=request)
    return result

@device_group_router.delete("/{id}")
async def delete_device_group(id: int):
    request = DeleteDeviceGroupDataRequest(id=id)
    user_case = delete_device_group_use_case()
    result = await user_case.execute(request)
    return result
