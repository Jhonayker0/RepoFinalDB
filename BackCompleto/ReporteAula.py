import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def generar_reporte_aulas(cursor):
    try:
        # Consulta para obtener los datos de las aulas con información del tutor
        query_reporte_aulas = """
        SELECT a."Grupo", a."GradoT", a."GradoNum", a."GrupoEquivalente", 
               a."Jornada", a."Año", i."NombreInsti",
               p."PrimerNombre", p."PrimerApellido"
        FROM "TempSchema"."Aula" a
        INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
        INNER JOIN "TempSchema"."Usuario" u ON a."IDUsuario" = u."IDUsuario"
        INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
        ORDER BY a."Año" DESC, a."Grupo";
        """
        cursor.execute(query_reporte_aulas)
        aulas = cursor.fetchall()

        if not aulas:
            print("No se encontraron aulas registradas.")
            return

        print(f"\n=== Reporte de Aulas ===\n")
        print(f"{'Grupo':<10} {'Grado T':<10} {'Grado Num':<12} {'Equivalente':<15} {'Jornada':<12} {'Año':<6} {'Institución':<25} {'Tutor':<25}")
        print("-" * 125)

        for aula in aulas:
            grupo = aula[0]
            grado_t = aula[1] or "N/A"
            grado_num = aula[2] or "N/A"
            equivalente = aula[3] or "N/A"
            jornada = aula[4] or "N/A"
            anio = aula[5]
            institucion = aula[6] or "N/A"
            tutor = f"{aula[7]} {aula[8]}"  # Nombre completo del tutor

            print(f"{grupo:<10} {grado_t:<10} {grado_num:<12} {equivalente:<15} {jornada:<12} {anio:<6} {institucion:<25} {tutor:<25}")

    except psycopg2.Error as e:
        print(f"Error al generar el reporte de aulas: {e}")

def main():
    try:
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                generar_reporte_aulas(cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
