import abc
from typing import List

from app.src.domain.models import Device

class DeviceRepository(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id: int) -> Device:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[Device]:
        pass

    @abc.abstractmethod
    async def add(self, device_group: Device) -> bool:
        pass

    @abc.abstractmethod
    def update(self, device_group: Device) -> bool:
        pass

    @abc.abstractmethod
    def delete(self, id: int) -> bool:
        pass