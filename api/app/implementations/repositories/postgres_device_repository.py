from typing import List
from app.implementations.clients.postgres_db_client import PostgresDbClient
from app.src.domain.repositories.device_repository import DeviceRepository
from app.implementations.repositories.entity.device import Device
from app.src.exceptions.device_repository_exception import (
    DeviceRepositoryError,
    DeviceRepositoryGetAllError,
    DeviceRepositoryNotFoundError
)

class PostgresDeviceRepository(DeviceRepository):
    def __init__(self, postgres_db_client: PostgresDbClient):
        self.postgres_db_client = postgres_db_client

    async def get_by_id(self, id: int) -> Device:
        try:
            data = await self.postgres_db_client.get_by_id(model=Device, id=id)
            if not data:
                raise DeviceRepositoryNotFoundError(f'Device con id {id} no encontrado')
            return Device(id=data.id, device_name=data.device_name)
        except DeviceRepositoryError as error:
            raise DeviceRepositoryError(f'Error al obtener el Device: {error}')

    async def get_all(self) -> List[Device]:
        try:
            data_list = await self.postgres_db_client.get_all(model=Device)
            return [Device(id=item.id, device_name=item.device_name) for item in data_list]
        except DeviceRepositoryGetAllError as error:
            raise DeviceRepositoryGetAllError(f'Error al obtener los Devices: {error}')

    async def add(self, device: Device) -> bool:
        try:
            new_device = await self.postgres_db_client.create(model=Device, data=device.__dict__)
            return True if new_device else False
        except DeviceRepositoryError as error:
            raise DeviceRepositoryError(f'Error al crear el Device: {error}')

    async def update(self, device: Device) -> bool:
        try:
            updated_device = await self.postgres_db_client.update(model=Device, data=device.__dict__)
            return True if updated_device else False
        except DeviceRepositoryError as error:
            raise DeviceRepositoryError(f'Error al actualizar el Device: {error}')

    async def delete(self, id: int) -> bool:
        try:
            deleted_device = await self.postgres_db_client.delete(model=Device, data={'id': id})
            return deleted_device
        except DeviceRepositoryError as error:
            raise DeviceRepositoryError(f'Error al eliminar el Device: {error}')
