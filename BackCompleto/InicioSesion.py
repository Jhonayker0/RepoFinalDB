import psycopg2
from psycopg2 import sql

# Configuración de conexión a la base de datos
DATABASE_CONFIG = {
    "dbname": "DB",  
    "user": "postgres",         
    "password": "123456789",    
    "host": "127.0.0.1",          
    "port": "5432"                
}

def verificar_usuario(identificacion, password):
    QUERY = """
    SELECT u."Rol"
    FROM "TempSchema"."Usuario" u
    INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
    WHERE p."Identificacion" = %s AND u."Pwd" = %s;
    """
    try:
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute(QUERY, (identificacion, password))
                result = cursor.fetchone()
                return result[0] if result else None
    except psycopg2.Error as e:
        raise Exception(f"Error en la base de datos: {e}")
