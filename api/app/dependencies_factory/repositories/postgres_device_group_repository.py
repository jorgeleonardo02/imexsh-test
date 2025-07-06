from app.dependencies_factory.clients.postgresdb_client import postgresdb_client
from app.implementations.repositories import (
    PostgresDeviceGroupDataRepository
)
from app.implementations.repositories.entity import DeviceGroup
from config import settings

def postgres_device_group_repository() -> PostgresDeviceGroupDataRepository: 
    return PostgresDeviceGroupDataRepository(
        postgres_db_client= postgresdb_client(
            database_url=settings.DATABASE_URL,
            model=DeviceGroup
        )
    )

