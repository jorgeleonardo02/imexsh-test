from pydantic import BaseModel


class UpdateDeviceGroupResponse(BaseModel): # clase que representa la respuesta del caso de uso de crear usuario
    result: bool # atributo que indica si la operación fue exitosa
    message: str # atributo que contiene un mensaje de éxito o error