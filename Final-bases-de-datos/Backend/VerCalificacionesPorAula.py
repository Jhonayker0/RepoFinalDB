import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def mostrar_calificaciones_por_aula_y_anio(grupo, anio, cursor):
    try:
        # Consulta para obtener las calificaciones de los estudiantes de un aula en un año específico
        query_calificaciones = """
        SELECT a."Grupo", e."IDEstudiante", e."PrimerNombre", e."PrimerApellido",
               ex."Nota", ex."BloqueLectivo", ex."Año"
        FROM "TempSchema"."Examen" ex
        INNER JOIN "TempSchema"."Estudiante" e ON ex."IDEstudiante" = e."IDEstudiante"
        INNER JOIN "TempSchema"."Aula" a ON e."Grupo" = a."Grupo"
        WHERE a."Grupo" = %s AND ex."Año" = %s
        ORDER BY ex."BloqueLectivo", e."PrimerApellido", e."PrimerNombre";
        """
        cursor.execute(query_calificaciones, (grupo, anio))
        calificaciones = cursor.fetchall()

        if not calificaciones:
            print(f"No se encontraron calificaciones registradas para el aula del grupo {grupo} en el año {anio}.")
            return

        print(f"\n=== Calificaciones por Aula (Grupo: {grupo}, Año: {anio}) ===\n")
        print(f"{'ID':<8} {'Nombre':<25} {'Nota':<6} {'Bloque':<15}")
        print("-" * 60)

        for calificacion in calificaciones:
            id_estudiante = calificacion[1]
            nombre = f"{calificacion[2]} {calificacion[3]}"
            nota = calificacion[4]
            bloque = calificacion[5]

            print(f"{id_estudiante:<8} {nombre:<25} {nota:<6} {bloque:<15}")

    except psycopg2.Error as e:
        print(f"Error al obtener las calificaciones: {e}")

def main():
    grupo = input("Ingrese el grupo del aula: ")
    try:
        anio = int(input("Ingrese el año para filtrar las calificaciones: "))
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                mostrar_calificaciones_por_aula_y_anio(grupo, anio, cursor)
    except ValueError:
        print("Error: El año debe ser un número válido.")
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
