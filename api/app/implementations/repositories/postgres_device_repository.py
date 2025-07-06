from fastapi import HTTPException
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
                self.__raise_exception(
                    status_code=404,
                    message=f'Device con id {id} no encontrado'
                )
            return Device(id=data.id, device_name=data.device_name)
        except DeviceRepositoryError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al obtener el Device: {error}'
            )
        
    async def get_by_device_id(self, device_id: str) -> Device:
        try:
            data = await self.postgres_db_client.get_by_device_id(model=Device, device_id=device_id)
            if not data:
                raise DeviceRepositoryNotFoundError(f'Device con device_id {device_id} no encontrado')
            return Device(id=data.id, device_id=data.device_id, device_name=data.device_name)
        except DeviceRepositoryError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al obtener el Device por device_id: {error}'
            )

    async def get_all(self) -> List[Device]:
        try:
            data_list = await self.postgres_db_client.get_all(model=Device)
            return [Device(id=item.id, device_name=item.device_name) for item in data_list]
        except DeviceRepositoryGetAllError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al obtener los Devices: {error}'
            )

    async def add(self, device: Device) -> bool:
        try:
            model_dict = device.model_dump(exclude={"id"})
            new_device = await self.postgres_db_client.create(model=Device, data=model_dict)
            return True if new_device else False
        except DeviceRepositoryError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al agregar el Device: {error}'
            )

    async def update(self, device: Device) -> bool:
        try:
            updated_device = await self.postgres_db_client.update(model=Device, data=device.__dict__)
            return True if updated_device else False
        except DeviceRepositoryError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al actualizar el Device: {error}'
            )

    async def delete(self, id: int) -> bool:
        try:
            deleted_device = await self.postgres_db_client.delete(model=Device, data={'id': id})
            return deleted_device
        except DeviceRepositoryError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al eliminar el Device: {error}'
            )
        
    def __raise_exception(self, status_code:int, message:str) -> None:
        raise HTTPException(
                status_code=status_code,
                detail=message
            )
