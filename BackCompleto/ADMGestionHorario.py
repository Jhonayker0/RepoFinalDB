import psycopg2
from psycopg2 import sql

# Configuración de conexión a la base de datos
DATABASE_CONFIG = {
    "dbname": "DB",  
    "user": "postgres",         
    "password": "123456789",    
    "host": "127.0.0.1",          
    "port": "5432"                
}
def insertar_horario(cursor):
    """Insertar un nuevo horario en la tabla Horario."""
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
    hora_fin = input("Ingrese la hora de fin (HH:MM): ")
    dia_inicial = input("Ingrese la inicial del día (M, T, W, R, F): ").upper()
    dia_texto = input("Ingrese el nombre completo del día (MONDAY, TUESDAY, etc.): ").upper()

    try:
        # Validar que no se repita el horario
        query_validar = """
        SELECT COUNT(*)
        FROM "TempSchema"."Horario"
        WHERE "HoraInicio" = %s AND "HoraFin" = %s AND "DiaTexto" = %s;
        """
        cursor.execute(query_validar, (hora_inicio, hora_fin, dia_texto))
        existe = cursor.fetchone()[0]

        if existe > 0:
            print("Error: Ya existe un horario con el mismo rango de horas en ese día.")
            return

        # Insertar el horario
        query_insertar = """
        INSERT INTO "TempSchema"."Horario" ("FechaInicio", "FechaFin", "HoraInicio", "HoraFin", "DiaInicial", "DiaTexto")
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query_insertar, (fecha_inicio, fecha_fin, hora_inicio, hora_fin, dia_inicial, dia_texto))
        print("Horario insertado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al insertar el horario: {e}")

def eliminar_horario(cursor):
    """Eliminar un horario específico por CodigoH."""
    codigo_h = input("Ingrese el código del horario (CodigoH) a eliminar: ")

    try:
        query_eliminar = """
        DELETE FROM "TempSchema"."Horario"
        WHERE "CodigoH" = %s;
        """
        cursor.execute(query_eliminar, (codigo_h,))
        print("Horario eliminado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al eliminar el horario: {e}")

def actualizar_horario(cursor):
    """Actualizar un horario específico."""
    codigo_h = input("Ingrese el código del horario (CodigoH) a actualizar: ")
    nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio (YYYY-MM-DD): ")
    nueva_fecha_fin = input("Ingrese la nueva fecha de fin (YYYY-MM-DD): ")
    nueva_hora_inicio = input("Ingrese la nueva hora de inicio (HH:MM): ")
    nueva_hora_fin = input("Ingrese la nueva hora de fin (HH:MM): ")
    nuevo_dia_inicial = input("Ingrese la nueva inicial del día (M, T, W, R, F): ").upper()
    nuevo_dia_texto = input("Ingrese el nuevo nombre completo del día (MONDAY, TUESDAY, etc.): ").upper()

    try:
        # Validar que no se repita el horario con los nuevos valores
        query_validar = """
        SELECT COUNT(*)
        FROM "TempSchema"."Horario"
        WHERE "HoraInicio" = %s AND "HoraFin" = %s AND "DiaTexto" = %s AND "CodigoH" != %s;
        """
        cursor.execute(query_validar, (nueva_hora_inicio, nueva_hora_fin, nuevo_dia_texto, codigo_h))
        existe = cursor.fetchone()[0]

        if existe > 0:
            print("Error: Ya existe un horario con el mismo rango de horas en ese día.")
            return

        # Actualizar el horario
        query_actualizar = """
        UPDATE "TempSchema"."Horario"
        SET "FechaInicio" = %s, "FechaFin" = %s, "HoraInicio" = %s, "HoraFin" = %s, 
            "DiaInicial" = %s, "DiaTexto" = %s
        WHERE "CodigoH" = %s;
        """
        cursor.execute(query_actualizar, (nueva_fecha_inicio, nueva_fecha_fin, nueva_hora_inicio, nueva_hora_fin, nuevo_dia_inicial, nuevo_dia_texto, codigo_h))
        print("Horario actualizado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al actualizar el horario: {e}")

def main():
    """Función principal con menú interactivo."""
    try:
        # Conexión a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                while True:
                    print("\n--- Gestión de Horarios ---")
                    print("1. Insertar horario")
                    print("2. Eliminar horario")
                    print("3. Actualizar horario")
                    print("4. Salir")
                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":
                        insertar_horario(cursor)
                    elif opcion == "2":
                        eliminar_horario(cursor)
                    elif opcion == "3":
                        actualizar_horario(cursor)
                    elif opcion == "4":
                        print("Saliendo del programa.")
                        break
                    else:
                        print("Opción no válida. Intente nuevamente.")
                    
                    # Confirmar cambios en la base de datos
                    conn.commit()

    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    main()
