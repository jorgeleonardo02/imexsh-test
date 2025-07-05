class DeviceRepositoryGetAllError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class DeviceRepositoryError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class DeviceRepositoryNotFoundError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

