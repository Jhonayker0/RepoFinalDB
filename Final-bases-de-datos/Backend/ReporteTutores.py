import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def generar_reporte_tutores(cursor):
    try:
        # Consulta para obtener los datos de los tutores
        query_reporte_tutores = """
        SELECT p."IDUsuario", p."PrimerNombre", p."PrimerApellido", 
               p."Correo", p."Telefono"
        FROM "TempSchema"."Usuario" u
        INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
        WHERE u."Rol" = 'Tutor';
        """
        cursor.execute(query_reporte_tutores)
        tutores = cursor.fetchall()

        if not tutores:
            print("No se encontraron tutores registrados.")
            return

        print(f"\n=== Reporte de Tutores ===\n")
        print(f"{'ID Usuario':<12} {'Nombre':<20} {'Apellido':<20} {'Correo':<25} {'Teléfono':<12}")
        print("-" * 90)

        for tutor in tutores:
            id_usuario = tutor[0]
            nombre = tutor[1]
            apellido = tutor[2]
            correo = tutor[3] or "N/A"
            telefono = tutor[4] or "N/A"

            print(f"{id_usuario:<12} {nombre:<20} {apellido:<20} {correo:<25} {telefono:<12}")

    except psycopg2.Error as e:
        print(f"Error al generar el reporte de tutores: {e}")

def main():
    try:
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                generar_reporte_tutores(cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
