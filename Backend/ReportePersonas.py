import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def generar_reporte_personas(cursor):
    try:
        # Consulta para obtener los datos de las personas
        query_reporte_personas = """
        SELECT p."TipoID", p."Identificacion", p."IDUsuario", 
               p."PrimerNombre", p."SegundoNombre", 
               p."PrimerApellido", p."SegundoApellido", 
               p."Correo", p."Telefono"
        FROM "TempSchema"."Persona" p
        ORDER BY p."PrimerApellido", p."SegundoApellido", p."PrimerNombre";
        """
        cursor.execute(query_reporte_personas)
        personas = cursor.fetchall()

        if not personas:
            print("No se encontraron personas registradas.")
            return

        print(f"\n=== Reporte de Personas ===\n")
        print(f"{'TipoID':<8} {'Identificación':<15} {'ID Usuario':<12} {'Nombre Completo':<35} {'Correo':<25} {'Teléfono':<12}")
        print("-" * 110)

        for persona in personas:
            tipo_id = persona[0]
            identificacion = persona[1]
            id_usuario = persona[2] or "N/A"
            nombre_completo = f"{persona[3]} {persona[4] or ''} {persona[5]} {persona[6] or ''}".strip()
            correo = persona[7] or "N/A"
            telefono = persona[8] or "N/A"

            print(f"{tipo_id:<8} {identificacion:<15} {id_usuario:<12} {nombre_completo:<35} {correo:<25} {telefono:<12}")

    except psycopg2.Error as e:
        print(f"Error al generar el reporte de personas: {e}")

def main():
    try:
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                generar_reporte_personas(cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
