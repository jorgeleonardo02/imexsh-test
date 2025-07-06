from app.dependencies_factory.repositories.postgres_device_group_repository import postgres_device_group_repository
from app.dependencies_factory.repositories.postgres_device_repository import postgres_device_repository
from app.src.cases.create_device_group_data import CreateDeviceGroupDataUseCase

def create_device_group_use_case() -> CreateDeviceGroupDataUseCase:
    device_repository = postgres_device_group_repository()
    device_group_repository = postgres_device_group_repository()
    return CreateDeviceGroupDataUseCase(
        device_group_repository=device_group_repository,
        device_repository=device_repository
    )

def delete_device_group_use_case() -> CreateDeviceGroupDataUseCase:
    device_repository = postgres_device_group_repository()
    device_group_repository = postgres_device_group_repository()
    return CreateDeviceGroupDataUseCase(
        device_group_repository=device_group_repository,
        device_repository=device_repository
    )
