from pydantic import BaseModel, ConfigDict


class Usuario(BaseModel): 
    id: int
    nombre: str
    edad: int
    email: str