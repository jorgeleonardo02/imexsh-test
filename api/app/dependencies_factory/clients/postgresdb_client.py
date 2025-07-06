from typing import Any
from app.implementations.clients.postgres_db_client import PostgresDbClient

def postgresdb_client(database_url, model: Any)-> PostgresDbClient: 
    return PostgresDbClient(database_url=database_url, model=model) 