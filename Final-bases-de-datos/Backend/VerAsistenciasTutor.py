import psycopg2
from datetime import datetime

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def mostrar_asistencias_usuarios(grupo, cursor):
    try:
        # Consulta para obtener las asistencias de los usuarios en un aula
        query_asistencias = """
        SELECT a."Grupo", p."PrimerNombre", p."PrimerApellido", u."Rol",
               h."DiaTexto", h."HoraInicio", h."HoraFin", au."Fecha", au."Asiste"
        FROM "TempSchema"."AsistenciaUsuario" au
        INNER JOIN "TempSchema"."Usuario" u ON au."IDUsuario" = u."IDUsuario"
        INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
        INNER JOIN "TempSchema"."Horario" h ON au."CodigoH" = h."CodigoH"
        INNER JOIN "TempSchema"."HorarioTieneAula" ha ON h."CodigoH" = ha."CodigoH"
        INNER JOIN "TempSchema"."Aula" a ON ha."Grupo" = a."Grupo"
        WHERE a."Grupo" = %s
        ORDER BY au."Fecha", h."DiaTexto", h."HoraInicio", p."PrimerApellido", p."PrimerNombre";
        """
        cursor.execute(query_asistencias, (grupo,))
        asistencias = cursor.fetchall()

        if not asistencias:
            print(f"No se encontraron asistencias registradas para el aula del grupo {grupo}.")
            return

        print(f"\n=== Asistencias de Usuarios en el Aula (Grupo: {grupo}) ===\n")
        print(f"{'Fecha':<12} {'Día':<10} {'Hora Inicio':<10} {'Hora Fin':<10} {'Usuario':<25} {'Rol':<15} {'Asistió':<8}")
        print("-" * 90)

        for asistencia in asistencias:
            fecha = asistencia[7].strftime('%Y-%m-%d')
            dia = asistencia[4]
            hora_inicio = asistencia[5].strftime('%H:%M')  # Formatear HoraInicio
            hora_fin = asistencia[6].strftime('%H:%M')      # Formatear HoraFin
            usuario = f"{asistencia[1]} {asistencia[2]}"
            rol = asistencia[3]
            asiste = "Sí" if asistencia[8] else "No"

            print(f"{fecha:<12} {dia:<10} {hora_inicio:<10} {hora_fin:<10} {usuario:<25} {rol:<15} {asiste:<8}")

    except psycopg2.Error as e:
        print(f"Error al obtener las asistencias: {e}")

def main():
    grupo = input("Ingrese el grupo del aula: ")
    try:
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                mostrar_asistencias_usuarios(grupo, cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()

