import abc
from typing import List

from app.src.domain.models import Usuario

# Interfaz que define los métodos que debe implementar un repositorio de usuarios
class UsuarioRepository(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id: int) -> Usuario:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[Usuario]:
        pass

    @abc.abstractmethod
    async def add(self, usuario: Usuario) -> bool:
        pass

    @abc.abstractmethod
    def update(self, usuario: Usuario) -> bool:
        pass

    @abc.abstractmethod
    def delete(self, user_id: int) -> bool:
        pass