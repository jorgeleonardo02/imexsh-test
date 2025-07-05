from app.dependencies_factory.repositories.postgres_device_group_repository import postgres_device_group_repository
from app.dependencies_factory.repositories.postgres_device_repository import postgres_device_repository
from app.src.cases.create_device_group_data import CreateDeviceGroupDataUseCase

# instancia el caso de uso
def create_device_group_use_case() -> CreateDeviceGroupDataUseCase: # función de fábrica que crea y devuelve una instancia de CreateUserUseCase
    device_repository = postgres_device_group_repository() # obtener el repositorio de usuarios
    device_group_repository = postgres_device_group_repository() # obtener el repositorio de usuarios
    return CreateDeviceGroupDataUseCase(
        device_group_repository=device_group_repository,
        device_repository=device_repository
    ) # devolver una instancia de CreateUserUseCase con el repositorio de usuarios

def delete_device_group_use_case() -> CreateDeviceGroupDataUseCase: # función de fábrica que crea y devuelve una instancia de CreateUserUseCase
    device_repository = postgres_device_group_repository() # obtener el repositorio de usuarios
    device_group_repository = postgres_device_group_repository() # obtener el repositorio de usuarios
    return CreateDeviceGroupDataUseCase(
        device_group_repository=device_group_repository,
        device_repository=device_repository
    ) # devolver una instancia de CreateUserUseCase con el repositorio de usuarios