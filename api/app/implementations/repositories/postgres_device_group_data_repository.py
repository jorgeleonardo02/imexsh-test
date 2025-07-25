from fastapi import HTTPException
from typing import Any, Dict, List, Optional
from app.implementations.clients.postgres_db_client import PostgresDbClient
from app.src.domain.repositories.device_group_data_repository import DeviceGroupDataRepository
from app.implementations.repositories.entity.device_group import DeviceGroup
from app.src.domain.models.device_group import DeviceGroupRequestFilters
from sqlalchemy.future import select

from app.src.exceptions.device_group_repository_exception import (DeviceGroupRepositoryError,
                                                                  DeviceGroupRepositoryGetAllError)

def to_device_group_model(model):
    return DeviceGroup.model_validate(model)

class PostgresDeviceGroupDataRepository(DeviceGroupDataRepository):
    def __init__(self, postgres_db_client: PostgresDbClient):
        self.postgres_db_client = postgres_db_client

    async def get_by_id(self, id: int) -> DeviceGroup:
        try:
            data = await self.postgres_db_client.get_by_id(model=DeviceGroup, id=id)
            if not data:
                self.__raise_exception(
                    status_code=404,
                    message="Device group not found for id: {}".format(id)
                )
            return DeviceGroup(id=data.id,
                               device_id=data.device_id,
                               average_before_normalization=data.average_before_normalization,
                               average_after_normalization=data.average_after_normalization,
                               data_size=data.data_size,
                               created_date=data.created_date,
                               updated_date=data.updated_date)
        except DeviceGroupRepositoryError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al obtener el Device group: {error}'
            )

    async def get_by_device_id(self, device_id: int) -> DeviceGroup:
        try:
            # 👇 Aquí sí hacemos SELECT por device_id con SQLAlchemy
            async with self.postgres_db_client.session_local() as session:
                stmt = select(DeviceGroup).where(DeviceGroup.device_id == device_id)
                result = await session.execute(stmt)
                data = result.scalars().first()

            if not data:
                self.__raise_exception(
                    status_code=404,
                    message="Device group not found for device_id: {}".format(device_id)
                )
            return data

        except DeviceGroupRepositoryError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al obtener el Device group por device_id: {error}'
            )
    
    async def get_all(self,
                  id: Optional[int],
                  filters: Optional[DeviceGroupRequestFilters]) -> List[DeviceGroup]:
        try:
            all_filters = DeviceGroupRequestFilters(id=id, **(filters.dict() if filters else {}))
            filter_dict = self.__build_filter_dict(all_filters)

            data_list = await self.postgres_db_client.get_all(model=DeviceGroup, filters=filter_dict)

            return [
                DeviceGroup(
                    id=item.id,
                    device_id=item.device_id,
                    average_before_normalization=item.average_before_normalization,
                    average_after_normalization=item.average_after_normalization,
                    data_size=item.data_size,
                    created_date=item.created_date,
                    updated_date=item.updated_date
                )
                for item in data_list
            if data_list]

        except DeviceGroupRepositoryGetAllError as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al obtener los Device groups: {error}'
            )


    async def add(self, device_group: DeviceGroup) -> bool:
        try:
            model_dict = device_group.model_dump(exclude={"id"})
            new_device_group = await self.postgres_db_client.create(model=DeviceGroup, data=model_dict)
            return True if new_device_group else False
        except DeviceGroupRepositoryError  as error:
            self.__raise_exception(
                status_code=500,
                message=f'Error al agregar el Device group: {error}'
            )

    async def update(self,device_group: DeviceGroup) -> bool:
        try:
            updated_device_group = await self.postgres_db_client.update(model=DeviceGroup, data=device_group.__dict__)
            return True if updated_device_group else False
        except DeviceGroupRepositoryError as error:
            raise DeviceGroupRepositoryError(f'Error al actualizar el Device group: {error}')

   
    async def delete(self, id: int) -> bool:
        try:
            deleted_device_group = await self.postgres_db_client.delete(model=DeviceGroup, data={'id': id})
            return deleted_device_group
        except DeviceGroupRepositoryError as error:
            raise DeviceGroupRepositoryError(f'Error al eliminar el Device group: {error}')


    def __build_filter_dict(self, filters: Optional[DeviceGroupRequestFilters]) -> Dict[str, Any]:
        if not filters:
            return {}

        return {
            "id": filters.id,
            "created_date": (filters.created_date_from, filters.created_date_to),
            "updated_date": (filters.updated_date_from, filters.updated_date_to),
            "average_before_normalization": (filters.average_before_normalization_from, filters.average_before_normalization_to),
            "average_after_normalization": (filters.average_after_normalization_from, filters.average_after_normalization_to),
            "data_size": (filters.data_size_from, filters.data_size_to)
        }
    
    def __raise_exception(self, status_code:int, message:str) -> None:
        raise HTTPException(
                status_code=status_code,
                detail=message
            )