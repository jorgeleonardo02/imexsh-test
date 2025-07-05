from typing import Any
from app.implementations.clients.postgres_db_client import PostgresDbClient

#función de fábrica que crea y devuelve una instancia de PostgresDbClient
#Facilita la creación de clientes PostgresDbClient para diferentes modelos.
def postgresdb_client(database_url, model: Any)-> PostgresDbClient: 
    return PostgresDbClient(database_url=database_url, model=model) 