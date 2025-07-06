from typing import Any, Dict, List, Optional
from sqlalchemy import select, update, and_
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.src.exceptions.postgres_client_error import ModelNotFoundError

class PostgresDbClient:
    def __init__(self, database_url: str, model: Any):
        self.engine = create_async_engine(database_url, echo=True)
        
        self.session_local = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
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
                            min_val, max_val = value
                            if min_val is not None:
                                conditions.append(column >= min_val)
                            if max_val is not None:
                                conditions.append(column <= max_val)
                        else:
                            conditions.append(column == value)

                    if conditions:
                        query = query.where(and_(*conditions))

                result = await session.execute(query)
                return result.scalars().all()

        except Exception as e:
            print(f"Error al obtener registros con filtros: {e}")
            return []

    async def get_by_id(self, model: Any, id: Any) -> Any:
        async with self.session_local() as session:
            result = await session.get(model, id)
        return result
    
    async def get_by_device_id(self, model: Any, device_id: str) -> Any:
        async with self.session_local() as session:
            result = await session.execute(
                select(model).where(model.device_id == device_id)
            )
            return result.scalar_one_or_none()

    async def create(self, model: Any, data: Any) -> Any:
        async with self.session_local() as session:
            async with session.begin():
                new_user = model(**data)
                session.add(new_user)
                await session.flush()
                await session.refresh(new_user)
                return new_user

    async def update(self, model: Any, data: Any) -> Any:
        try:
            async with self.session_local() as session:
                id = data["id"]
                db_data = await session.get(model, data["id"])
                if not db_data:
                    raise ModelNotFoundError(model.__name__, id)
                
                column_names = {col.name for col in model.__table__.columns}
                new_clean_data = {k: v for k, v in data.items() if k in column_names}

                query = update(model).where(model.id == id).values(**new_clean_data)
                await session.execute(query)
                await session.commit()
                await session.refresh(db_data)

                return db_data

        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            return None

    async def delete(self, model: Any, data: Any) -> bool:
        try:
            async with self.session_local() as session:
                assert isinstance(session, AsyncSession), "La sesión no es asíncrona"
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
