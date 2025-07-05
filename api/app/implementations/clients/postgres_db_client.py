from typing import Any, Dict, List, Optional
from sqlalchemy import create_engine, insert, select, update, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
#from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from app.src.exceptions.postgres_client_error import ModelNotFoundError


#clase genérica
class PostgresDbClient:
    def __init__(self, database_url: str, model: Any):
        # Motor asíncrono
        self.engine = create_async_engine(database_url, echo=True)
        
        # Sessionmaker asíncrono
        self.session_local = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,  # 👈 Ahora usa AsyncSession
            expire_on_commit=False
        )
        
        self.model = model
    
    async def get_all(self, model: Any, filters: Optional[Dict[str, Any]] = None) -> List[Any]:
        try:
            async with self.session_local() as session:
                query = select(model)

                if filters:
                    conditions = []
                    for field, value in filters.items():
                        if value is None:
                            continue
                        column = getattr(model, field, None)
                        if column is None:
                            continue
                        if isinstance(value, tuple) and len(value) == 2:
                            # Rangos: (min, max)
                            min_val, max_val = value
                            if min_val is not None:
                                conditions.append(column >= min_val)
                            if max_val is not None:
                                conditions.append(column <= max_val)
                        else:
                            # Valor exacto
                            conditions.append(column == value)

                    if conditions:
                        query = query.where(and_(*conditions))

                result = await session.execute(query)
                return result.scalars().all()

        except Exception as e:
            print(f"Error al obtener registros con filtros: {e}")
            return []


    #def get_by_id(self, model: Any, id:Any) -> Any:
     #   with self.session_local() as session:
      #      result = session.query(model).filter(model.id == id).first()
       #     return result
        
    async def get_by_id(self, model: Any, id: Any) -> Any:
        async with self.session_local() as session:  # Sesión asíncrona
            result = await session.get(model, id)  # get() para búsqueda directa por clave primaria
        return result
    
    async def get_by_device_id(self, model: Any, device_id: Any) -> Any:
        async with self.session_local() as session:  # Sesión asíncrona
            result = await session.get(model, device_id)  # get() para búsqueda directa por clave primaria
        return result


    async def create(self, model: Any, data: Any) -> Any: # método que crea un nuevo registro en la base de datos
        async with self.session_local() as session: # abrir una sesión con la base de datos
            async with session.begin():  # Asegura la transacción asíncrona
                new_user = model(**data)  # Crear instancia del modelo
                session.add(new_user)  # Agregar a la sesión
                await session.flush()  # Sincronizar para obtener valores generados (como ID)
                await session.refresh(new_user)  # Refrescar la instancia desde la BD
                return new_user


    async def update(self, model: Any, data: Any) -> Any:
        try:
            async with self.session_local() as session:  # 👈 Asíncrono
                # Buscar el registro en la base de datos
                usuario_db = await session.get(model, data["id"])
                if not usuario_db:
                    raise ModelNotFoundError(model.__name__, data["id"])

                # Crear una consulta de actualización
                query = update(model).where(model.id == data["id"]).values(**data)
                await session.execute(query)  # 👈 Asíncrono
                await session.commit()        # 👈 Asíncrono
                await session.refresh(usuario_db)  # 👈 Asíncrono

                return usuario_db

        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            return None

        
    async def delete(self, model: Any, data: Any) -> bool:
        print("Eliminando usuario...")  # ✅ Mensaje de depuración
        try:
            async with self.session_local() as session:  # Abre una sesión de base de datos
                assert isinstance(session, AsyncSession), "La sesión no es asíncrona"  # ✅ Verifica que es asíncrona
                result = await session.execute(select(model).filter(model.id == data["id"]))
                usuario_db = result.scalars().first()
                if not usuario_db:
                    print("Usuario no encontrado")
                    return False
                print("Usuario encontrado:", usuario_db)
                await session.delete(usuario_db)
                await session.commit()
                print("Usuario eliminado correctamente")
                return True
        except Exception as error:
            print("Hola")
            print(f"Error al eliminar el usuario: {error}")
            return False

    def close(self):
        self.session_local.close()
