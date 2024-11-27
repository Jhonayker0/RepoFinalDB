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

def registrar_asistencia_por_estudiante(grupo, codigo_horario, fecha, id_tutor, cursor):
    try:
        # Validar formato de la fecha
        try:
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            print("Error: La fecha ingresada no es válida. Use el formato YYYY-MM-DD.")
            return

        # Registrar asistencia del tutor si su rol es "Tutor"
        query_verificar_rol_tutor = """
        SELECT "Rol"
        FROM "TempSchema"."Usuario"
        WHERE "IDUsuario" = %s;
        """
        cursor.execute(query_verificar_rol_tutor, (id_tutor,))
        rol_tutor = cursor.fetchone()

        if rol_tutor and rol_tutor[0] == "Tutor":
            # Verificar si ya existe un registro para el tutor
            query_verificar_asistencia_tutor = """
            SELECT COUNT(*)
            FROM "TempSchema"."AsistenciaUsuario"
            WHERE "CodigoH" = %s AND "IDUsuario" = %s AND "Fecha" = %s;
            """
            cursor.execute(query_verificar_asistencia_tutor, (codigo_horario, id_tutor, fecha_obj))
            existe_asistencia_tutor = cursor.fetchone()[0]

            if existe_asistencia_tutor == 0:
                # Registrar la asistencia del tutor
                query_insertar_asistencia_tutor = """
                INSERT INTO "TempSchema"."AsistenciaUsuario" ("CodigoH", "IDUsuario", "Fecha", "Asiste")
                VALUES (%s, %s, %s, %s);
                """
                cursor.execute(query_insertar_asistencia_tutor, (codigo_horario, id_tutor, fecha_obj, True))
                print("Asistencia del tutor registrada exitosamente.")
            else:
                print("El tutor ya tiene registrada su asistencia para este horario y fecha.")

        # Paso 1: Obtener estudiantes con horarios asignados al grupo
        query_estudiantes = """
        SELECT DISTINCT eth."IDEstudiante", e."PrimerNombre", e."PrimerApellido"
        FROM "TempSchema"."EstudianteTieneHorario" eth
        INNER JOIN "TempSchema"."Estudiante" e ON eth."IDEstudiante" = e."IDEstudiante"
        INNER JOIN "TempSchema"."Aula" a ON e."Grupo" = a."Grupo"
        WHERE a."Grupo" = %s;
        """
        cursor.execute(query_estudiantes, (grupo,))
        estudiantes = cursor.fetchall()

        if not estudiantes:
            print(f"No se encontraron estudiantes con horarios asignados para el grupo {grupo}.")
            return

        # Paso 2: Obtener el horario específico si se especificó un código de horario
        query_horarios = """
        SELECT h."CodigoH", h."DiaTexto", h."HoraInicio", h."HoraFin"
        FROM "TempSchema"."Horario" h
        INNER JOIN "TempSchema"."HorarioTieneAula" ha ON h."CodigoH" = ha."CodigoH"
        WHERE ha."Grupo" = %s AND h."CodigoH" = %s;
        """
        cursor.execute(query_horarios, (grupo, codigo_horario))
        horarios = cursor.fetchall()

        if not horarios:
            print(f"No se encontraron horarios asociados al grupo {grupo} y al código de horario {codigo_horario}.")
            return

        # Paso 3: Registrar asistencia estudiante por estudiante
        for horario in horarios:
            codigo_h = horario[0]
            dia = horario[1]
            print(f"\n=== Horario: {dia} {horario[2]} - {horario[3]} ===")

            for estudiante in estudiantes:
                id_estudiante = estudiante[0]
                nombre = estudiante[1]
                apellido = estudiante[2]

                # Verificar si el estudiante tiene asignado ese horario
                query_verificar_horario = """
                SELECT COUNT(*)
                FROM "TempSchema"."EstudianteTieneHorario"
                WHERE "IDEstudiante" = %s AND "CodigoH" = %s;
                """
                cursor.execute(query_verificar_horario, (id_estudiante, codigo_h))
                tiene_horario = cursor.fetchone()[0]

                if tiene_horario == 0:
                    print(f"{nombre} {apellido} no tiene asignado el horario {codigo_h}.")
                    continue

                # Preguntar si asistió o no
                while True:
                    asiste = input(f"¿Asistió {nombre} {apellido} en la fecha {fecha}? (S/N): ").strip().upper()
                    if asiste in ['S', 'N']:
                        break
                    print("Entrada inválida. Por favor ingrese 'S' para Sí o 'N' para No.")

                # Verificar si ya existe el registro
                query_verificar = """
                SELECT COUNT(*)
                FROM "TempSchema"."AsistenciaEstudiante"
                WHERE "CodigoH" = %s AND "IDEstudiante" = %s AND "Fecha" = %s;
                """
                cursor.execute(query_verificar, (codigo_h, id_estudiante, fecha_obj))
                existe = cursor.fetchone()[0]

                if existe > 0:
                    print(f"Ya existe un registro de asistencia para {nombre} {apellido} en este horario y fecha.")
                else:
                    # Insertar el registro en la tabla AsistenciaEstudiante
                    query_asistencia = """
                    INSERT INTO "TempSchema"."AsistenciaEstudiante" ("CodigoH", "IDEstudiante", "Fecha", "Asiste")
                    VALUES (%s, %s, %s, %s);
                    """
                    cursor.execute(query_asistencia, (codigo_h, id_estudiante, fecha_obj, asiste == 'S'))
        
        print("Asistencia registrada exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al registrar la asistencia: {e}")

def main():
    grupo = input("Ingrese el grupo del aula: ")
    codigo_horario = input("Ingrese el código de horario: ")
    fecha = input("Ingrese la fecha para registrar la asistencia (YYYY-MM-DD): ")
    id_tutor = input("Ingrese la identificación del tutor: ")  # ID del tutor que inicia sesión
    try:
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                registrar_asistencia_por_estudiante(grupo, codigo_horario, fecha, id_tutor, cursor)
                conn.commit()
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
