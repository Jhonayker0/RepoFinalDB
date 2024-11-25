import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def generar_reporte_aulas_tutor(id_usuario, cursor):
    try:
        # Consulta actualizada para obtener las aulas asociadas a un tutor específico
        query_reporte_aulas_tutor = """
        SELECT a."Grupo", a."GradoT", a."GradoNum", a."Jornada", i."NombreInsti"
        FROM "TempSchema"."Aula" a
        INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
        WHERE a."IDUsuario" = %s
        ORDER BY a."Grupo";
        """
        cursor.execute(query_reporte_aulas_tutor, (id_usuario,))
        aulas_tutor = cursor.fetchall()

        if not aulas_tutor:
            print(f"No se encontraron aulas asociadas al tutor con IDUsuario {id_usuario}.")
            return

        print(f"\n=== Reporte de Aulas por Tutor (IDUsuario: {id_usuario}) ===\n")
        print(f"{'Grupo':<10} {'GradoT':<10} {'GradoNum':<10} {'Jornada':<15} {'Institución':<25}")
        print("-" * 80)

        for aula in aulas_tutor:
            grupo = aula[0]
            grado_t = aula[1]
            grado_num = aula[2]
            jornada = aula[3]
            institucion = aula[4]

            print(f"{grupo:<10} {grado_t:<10} {grado_num:<10} {jornada:<15} {institucion:<25}")

    except psycopg2.Error as e:
        print(f"Error al generar el reporte de aulas por tutor: {e}")

def main():
    try:
        id_usuario = input("Ingrese el IDUsuario del tutor: ")
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                generar_reporte_aulas_tutor(id_usuario, cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
