import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def generar_reporte_usuarios(cursor):
    try:
        # Consulta para obtener los datos de los usuarios
        query_reporte_usuarios = """
        SELECT u."IDUsuario", p."PrimerNombre", p."SegundoNombre", 
               p."PrimerApellido", p."SegundoApellido", u."Rol", p."Correo", p."Telefono"
        FROM "TempSchema"."Usuario" u
        INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
        ORDER BY p."PrimerApellido", p."SegundoApellido", p."PrimerNombre";
        """
        cursor.execute(query_reporte_usuarios)
        usuarios = cursor.fetchall()

        if not usuarios:
            print("No se encontraron usuarios registrados.")
            return

        print(f"\n=== Reporte de Usuarios ===\n")
        print(f"{'ID':<8} {'Nombre Completo':<35} {'Rol':<15} {'Correo':<25} {'Teléfono':<12}")
        print("-" * 100)

        for usuario in usuarios:
            id_usuario = usuario[0]
            nombre_completo = f"{usuario[1]} {usuario[2] or ''} {usuario[3]} {usuario[4] or ''}".strip()
            rol = usuario[5]
            correo = usuario[6] or "N/A"
            telefono = usuario[7] or "N/A"

            print(f"{id_usuario:<8} {nombre_completo:<35} {rol:<15} {correo:<25} {telefono:<12}")

    except psycopg2.Error as e:
        print(f"Error al generar el reporte de usuarios: {e}")

def main():
    try:
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                generar_reporte_usuarios(cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
