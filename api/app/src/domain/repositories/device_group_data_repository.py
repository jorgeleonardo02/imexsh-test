import abc
from typing import List, Optional

from app.src.domain.models import DeviceGroup
from app.src.domain.models.device_group import DeviceGroupRequestFilters

# Interfaz que define los métodos que debe implementar un repositorio de DeviceGroup
class DeviceGroupDataRepository(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id: int) -> DeviceGroup:
        pass
    
    @abc.abstractmethod
    def get_by_device_id(self, id: int) -> DeviceGroup:
        pass

    @abc.abstractmethod
    def get_all(self,
                id: Optional[int],
                filters: Optional[DeviceGroupRequestFilters]) -> List[DeviceGroup]:
        pass

    @abc.abstractmethod
    async def add(self, device_group: DeviceGroup) -> bool:
        pass

    @abc.abstractmethod
    def update(self, device_group: DeviceGroup) -> bool:
        pass

    @abc.abstractmethod
    def delete(self, device_group_id: int) -> bool:
        pass