import psycopg2

DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def obtener_conexion():
    """Retorna una conexión a la base de datos."""
    return psycopg2.connect(**DATABASE_CONFIG)
