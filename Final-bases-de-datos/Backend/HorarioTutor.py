import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def generar_reporte_horario_tutor(id_usuario, cursor):
    try:
        # Consulta para obtener el horario del tutor validando sus aulas asignadas
        query_reporte_horario_tutor = """
        SELECT h."DiaTexto", h."HoraInicio", h."HoraFin", a."Grupo", i."NombreInsti"
        FROM "TempSchema"."Horario" h
        INNER JOIN "TempSchema"."HorarioTieneAula" hta ON h."CodigoH" = hta."CodigoH"
        INNER JOIN "TempSchema"."Aula" a ON hta."Grupo" = a."Grupo"
        INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
        WHERE a."IDUsuario" = %s
        ORDER BY h."DiaTexto", h."HoraInicio";
        """
        cursor.execute(query_reporte_horario_tutor, (id_usuario,))
        horarios = cursor.fetchall()

        if not horarios:
            print(f"No se encontraron horarios asociados al tutor con IDUsuario {id_usuario}.")
            return

        print(f"\n=== Reporte de Horario por Tutor (IDUsuario: {id_usuario}) ===\n")
        print(f"{'Día':<10} {'Hora Inicio':<12} {'Hora Fin':<12} {'Grupo':<10} {'Institución':<25}")
        print("-" * 80)

        for horario in horarios:
            dia = horario[0]
            hora_inicio = horario[1].strftime('%H:%M')  # Formatear hora
            hora_fin = horario[2].strftime('%H:%M')     # Formatear hora
            grupo = horario[3]
            institucion = horario[4]

            print(f"{dia:<10} {hora_inicio:<12} {hora_fin:<12} {grupo:<10} {institucion:<25}")

    except psycopg2.Error as e:
        print(f"Error al generar el reporte del horario del tutor: {e}")

def main():
    try:
        id_usuario = input("Ingrese el IDUsuario del tutor: ")
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                generar_reporte_horario_tutor(id_usuario, cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
