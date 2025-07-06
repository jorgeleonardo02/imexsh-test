from app.dependencies_factory.clients.postgresdb_client import postgresdb_client
from app.implementations.repositories import (
    PostgresDeviceRepository
)
from app.implementations.repositories.entity import Device
from config import settings

def postgres_device_repository() -> PostgresDeviceRepository: 
    return PostgresDeviceRepository(
        postgres_db_client= postgresdb_client(
            database_url=settings.DATABASE_URL,
            model=Device
        )
    )

