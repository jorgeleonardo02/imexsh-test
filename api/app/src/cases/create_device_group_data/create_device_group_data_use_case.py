from fastapi import HTTPException
from typing import List, Dict, Union

from datetime import datetime
from ..create_device_group_data import CreateDeviceGroupDataRequest, CreateDeviceGroupDataResponse
from app.src.domain.repositories import (
    DeviceGroupDataRepository,
    DeviceRepository
)
from app.src.domain.models import DeviceGroup, Device

class CreateDeviceGroupDataUseCase:
    def __init__(self,
                 device_group_repository: DeviceGroupDataRepository,
                 device_repository: DeviceRepository
        ):
        self.device_group_repository = device_group_repository
        self.device_repository=device_repository

    async def execute(self, request: CreateDeviceGroupDataRequest) -> CreateDeviceGroupDataResponse:
        self.__validate_data(request)
        
        devices_groups: List[DeviceGroup] = []
        devices: List[Device] = []

        for group in request.root.values():
            data = group.data
            device_id = group.id
            created_date = datetime.now()

            numbers = self.__get_numbers_from_data(data)
            average_before_normalization = self.__calculate_average(numbers)
            normalized_numbers = self.__calculate_normalized_data(numbers)
            average_after_normalization = self.__calculate_average(normalized_numbers)
            
            device_group = DeviceGroup(
                device_id=device_id,
                average_before_normalization=average_before_normalization,
                average_after_normalization=average_after_normalization,
                data_size=len(data),
                created_date=created_date,
                updated_date=None
            )
            
            device = Device(
                device_id=device_id,
                device_name=group.device_name
            )

            devices_groups.append(device_group)
            devices.append(device)
        
            try :
                await self.device_group_repository.add(device_group)
                await self.device_repository.add(device)
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Error creating device group: {e}"
                )

        message = "Image result created successfully"

        return CreateDeviceGroupDataResponse(result=True, message=message)
    
    def __validate_data(self, request: Dict[str, Device]):
            device_group_request = request.root.values()
            device_group_mapping = device_group_request.mapping
            device_groups_requests = device_group_mapping.values()
            for device_group in device_groups_requests:
                numbers_str = device_group.data
                validation_result = self.__validate_all_numbers(numbers_str)

                if not validation_result:
                    raise HTTPException(
                        status_code=404,
                        detail="Invalid data"
                    )
    
    def __validate_all_numbers(self, numbers_str_list: str) -> bool:
        validations = []
        for numbers in numbers_str_list:
            numbers_list = numbers.split(" ")
            validation_result = all(number.isnumeric() for number in numbers_list)
            validations.append(validation_result)
        return all(validations)
    
    def __get_numbers_from_data(self, data: List[str]) -> List[int]:
        numbers = []
        for numbers_str in data:
            numbers_list = numbers_str.split(" ")
            numbers.extend(numbers_list)
        return self.__to_int_list(numbers)
    
    def __to_int_list(self, numbers: List[str]) -> List[int]:
        try:
            return [int(number) for number in numbers]
        except ValueError as e:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid number in data: {e}"
            )
    
    def __calculate_normalized_data(self, numbers: List[int]) -> List[float]:
        max_value = max(numbers)
        normalized_numbers = [number / max_value if max_value != 0 else 0 for number in numbers]
        return normalized_numbers
    
    def __calculate_average(self, numbers: List[Union[int, float]]) -> float:
        if not numbers:
            raise ValueError("Cannot calculate average of empty list.")
        return sum(numbers) / len(numbers)