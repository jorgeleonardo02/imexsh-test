from app.dependencies_factory.repositories.postgres_device_group_repository import postgres_device_group_repository
from app.dependencies_factory.repositories.postgres_device_repository import postgres_device_repository
from app.src.cases.create_device_group_data import CreateDeviceGroupDataUseCase
from app.src.cases.delete_device_group_data import DeleteDeviceGroupDataUseCase
from app.src.cases.update_device_group import UpdateDeviceGroupUseCase
from app.src.cases.get_all_device_groups_data import GetAllDeviceGroupsDataUseCase

def create_device_group_use_case() -> CreateDeviceGroupDataUseCase:
    device_repository = postgres_device_repository()
    device_group_repository = postgres_device_group_repository()
    return CreateDeviceGroupDataUseCase(
        device_group_repository=device_group_repository,
        device_repository=device_repository
    )

def delete_device_group_use_case() -> DeleteDeviceGroupDataUseCase:
    device_repository = postgres_device_repository()
    device_group_repository = postgres_device_group_repository()
    return DeleteDeviceGroupDataUseCase(
        device_group_repository=device_group_repository,
        device_repository=device_repository
    )

def update_device_group_use_case() -> UpdateDeviceGroupUseCase:
    device_repository = postgres_device_repository()
    device_group_repository = postgres_device_group_repository()
    return UpdateDeviceGroupUseCase(
        device_group_repository=device_group_repository,
        device_repository=device_repository
    )
    
def get_all_device_groups_use_case() -> GetAllDeviceGroupsDataUseCase:
    device_repository = postgres_device_repository()
    device_group_repository = postgres_device_group_repository()
    return GetAllDeviceGroupsDataUseCase(
        device_group_repository=device_group_repository
    )
