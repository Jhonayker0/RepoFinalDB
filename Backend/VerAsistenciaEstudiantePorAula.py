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

def mostrar_asistencias_aula(grupo, cursor):
    try:
        # Consulta para obtener las asistencias de los estudiantes de un aula
        query_asistencias = """
        SELECT a."Grupo", e."IDEstudiante", e."PrimerNombre", e."PrimerApellido",
               h."DiaTexto", h."HoraInicio", h."HoraFin", ae."Fecha", ae."Asiste"
        FROM "TempSchema"."AsistenciaEstudiante" ae
        INNER JOIN "TempSchema"."Estudiante" e ON ae."IDEstudiante" = e."IDEstudiante"
        INNER JOIN "TempSchema"."EstudianteTieneHorario" eth ON e."IDEstudiante" = eth."IDEstudiante"
        INNER JOIN "TempSchema"."Horario" h ON ae."CodigoH" = h."CodigoH"
        INNER JOIN "TempSchema"."HorarioTieneAula" ha ON h."CodigoH" = ha."CodigoH"
        INNER JOIN "TempSchema"."Aula" a ON ha."Grupo" = a."Grupo"
        WHERE a."Grupo" = %s
        ORDER BY ae."Fecha", h."DiaTexto", h."HoraInicio", e."PrimerApellido", e."PrimerNombre";
        """
        cursor.execute(query_asistencias, (grupo,))
        asistencias = cursor.fetchall()

        if not asistencias:
            print(f"No se encontraron asistencias registradas para el aula del grupo {grupo}.")
            return

        print(f"\n=== Asistencias del Aula (Grupo: {grupo}) ===\n")
        print(f"{'Fecha':<12} {'Día':<10} {'Hora Inicio':<10} {'Hora Fin':<10} {'Estudiante':<25} {'Asistió':<8}")
        print("-" * 75)

        for asistencia in asistencias:
            fecha = asistencia[7].strftime('%Y-%m-%d')
            dia = asistencia[4]
            hora_inicio = asistencia[5].strftime('%H:%M')  # Formatear HoraInicio
            hora_fin = asistencia[6].strftime('%H:%M')      # Formatear HoraFin
            estudiante = f"{asistencia[2]} {asistencia[3]}"
            asiste = "Sí" if asistencia[8] else "No"

            print(f"{fecha:<12} {dia:<10} {hora_inicio:<10} {hora_fin:<10} {estudiante:<25} {asiste:<8}")

    except psycopg2.Error as e:
        print(f"Error al obtener las asistencias: {e}")

def main():
    grupo = input("Ingrese el grupo del aula: ")
    try:
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                mostrar_asistencias_aula(grupo, cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
