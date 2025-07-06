from fastapi import HTTPException
from app.src.cases.get_all_device_groups_data import GetAllDeviceGroupDataRequest, GetAllDeviceGroupDataResponse
from app.src.domain.repositories import (
    DeviceGroupDataRepository
)
from app.src.domain.models.device_group import DeviceGroupRequestFilters
from app.src.shemas.device_group_schema import DeviceGroupSchema


class GetAllDeviceGroupsDataUseCase:
    def __init__(self,
                 device_group_repository: DeviceGroupDataRepository):
        self.device_group_repository = device_group_repository

    async def execute(self, request: GetAllDeviceGroupDataRequest) -> GetAllDeviceGroupDataResponse:
        id = request.id
        filters = request.filters

        if filters:
            self.__validate_filters(filters)

        result = await self.device_group_repository.get_all(id, filters)
        return GetAllDeviceGroupDataResponse(
            device_groups=[
                DeviceGroupSchema.from_orm(item)
                for item in result
            ]
        )
    
    def __validate_filters(self, filters: DeviceGroupRequestFilters):
        def validate_range(field_from, field_to, field_name):
            if field_from and field_to and field_from > field_to:
                raise HTTPException(
                    status_code=400,
                    detail=f"{field_name}_from cannot be greater than {field_name}_to"
                )

        validate_range(filters.created_date_from, filters.created_date_to, "created_date")
        validate_range(filters.updated_date_from, filters.updated_date_to, "updated_date")
        validate_range(filters.average_before_normalization_from, filters.average_before_normalization_to, "average_before_normalization")
        validate_range(filters.average_after_normalization_from, filters.average_after_normalization_to, "average_after_normalization")
        validate_range(filters.data_size_from, filters.data_size_to, "data_size")