import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def generar_reporte_estudiantes_aula(grupo, cursor):
    try:
        # Consulta para obtener los estudiantes de un aula específica
        query_reporte_estudiantes_aula = """
        SELECT e."IDEstudiante", e."PrimerNombre", e."PrimerApellido", 
               a."Grupo", i."NombreInsti"
        FROM "TempSchema"."Estudiante" e
        INNER JOIN "TempSchema"."Aula" a ON e."Grupo" = a."Grupo"
        INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
        WHERE a."Grupo" = %s
        ORDER BY e."PrimerApellido", e."PrimerNombre";
        """
        cursor.execute(query_reporte_estudiantes_aula, (grupo,))
        estudiantes = cursor.fetchall()

        if not estudiantes:
            print(f"No se encontraron estudiantes registrados en el aula con Grupo {grupo}.")
            return

        print(f"\n=== Reporte de Estudiantes por Aula (Grupo: {grupo}) ===\n")
        print(f"{'ID Estudiante':<15} {'Nombre Completo':<30} {'Grupo':<10} {'Institución':<25}")
        print("-" * 80)

        for estudiante in estudiantes:
            id_estudiante = estudiante[0]
            nombre_completo = f"{estudiante[1]} {estudiante[2]}"
            grupo = estudiante[3]
            institucion = estudiante[4]

            print(f"{id_estudiante:<15} {nombre_completo:<30} {grupo:<10} {institucion:<25}")

    except psycopg2.Error as e:
        print(f"Error al generar el reporte de estudiantes por aula: {e}")

def main():
    try:
        grupo = input("Ingrese el Grupo del aula: ")
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                generar_reporte_estudiantes_aula(grupo, cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
