from app.dependencies_factory.clients.postgresdb_client import postgresdb_client
from app.implementations.repositories import (
    PostgresDeviceRepository
)
from app.implementations.repositories.entity import Device

# función de fábrica que crea y devuelve una instancia de PostgresUsuarioRepository
def postgres_device_repository() -> PostgresDeviceRepository: 
    return PostgresDeviceRepository( # devuelve una instancia de PostgresUsuarioRepository
        postgres_db_client= postgresdb_client( # obtiene un cliente de base de datos PostgresDbClient
            database_url='postgresql+asyncpg://postgres:jleo_BP963963@localhost:5432/IMEXHS',  #URL de la base de datos
            model=Device # modelo de la base de datos
        )
    )

