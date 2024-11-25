import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def verificar_solapamiento_horario(id_usuario, codigo_horario, cursor):
    """
    Verifica si el horario ya está asignado al tutor.
    """
    try:
        query_verificar = """
        SELECT COUNT(*)
        FROM "TempSchema"."UsuarioTieneHorario"
        WHERE "IDUsuario" = %s AND "CodigoH" = %s;
        """
        cursor.execute(query_verificar, (id_usuario, codigo_horario))
        solapamiento = cursor.fetchone()[0]
        return solapamiento > 0
    except psycopg2.Error as e:
        print(f"Error al verificar solapamiento: {e}")
        return True

def asignar_horario_tutor(cursor):
    """
    Asigna un horario existente (predefinido) a un tutor si no está asignado previamente.
    """
    id_usuario = input("Ingrese el IDUsuario del tutor: ")
    codigo_horario = input("Ingrese el Código del horario (CodigoH): ")

    try:
        # Verificar si el horario ya está asignado al tutor
        if verificar_solapamiento_horario(id_usuario, codigo_horario, cursor):
            print("El horario seleccionado ya está asignado al tutor. No se puede asignar nuevamente.")
            return

        # Relacionar el horario con el usuario
        query_asociar_horario_usuario = """
        INSERT INTO "TempSchema"."UsuarioTieneHorario" ("CodigoH", "IDUsuario")
        VALUES (%s, %s);
        """
        cursor.execute(query_asociar_horario_usuario, (codigo_horario, id_usuario))

        print(f"Horario asignado exitosamente al tutor con IDUsuario {id_usuario}.")

    except psycopg2.Error as e:
        print(f"Error al asignar el horario: {e}")

def main():
    try:
        # Conexión a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                asignar_horario_tutor(cursor)
                conn.commit()
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
