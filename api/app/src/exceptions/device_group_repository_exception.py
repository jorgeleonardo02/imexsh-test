class DeviceGroupRepositoryGetAllError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class DeviceGroupRepositoryError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class DeviceGroupRepositoryNotFoundError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

