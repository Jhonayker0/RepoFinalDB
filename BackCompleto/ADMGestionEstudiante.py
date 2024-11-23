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

def insertar_estudiante(cursor):
    """Insertar un nuevo estudiante en la tabla Estudiantes."""
    tipo_id = input("Ingrese el tipo de identificación (CC, TI, etc.): ").upper()
    id_estudiante = input("Ingrese el ID del estudiante: ")
    primer_nombre = input("Ingrese el primer nombre: ")
    segundo_nombre = input("Ingrese el segundo nombre (opcional): ")
    primer_apellido = input("Ingrese el primer apellido: ")
    segundo_apellido = input("Ingrese el segundo apellido (opcional): ")
    genero = input("Ingrese el género (M/F): ").upper()
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    estrato = input("Ingrese el estrato: ")
    anio = input("Ingrese el año: ")
    grupo = input("Ingrese el grupo: ")

    try:
        # Validar que no se repita el estudiante por TipoID e IDEstudiante
        query_validar = """
        SELECT COUNT(*)
        FROM "TempSchema"."Estudiantes"
        WHERE "TipoID" = %s AND "IDEstudiante" = %s;
        """
        cursor.execute(query_validar, (tipo_id, id_estudiante))
        existe = cursor.fetchone()[0]

        if existe > 0:
            print("Error: Ya existe un estudiante con el mismo TipoID y IDEstudiante.")
            return

        # Insertar el estudiante
        query_insertar = """
        INSERT INTO "TempSchema"."Estudiantes" ("TipoID", "IDEstudiante", "PrimerNombre", "SegundoNombre",
                                                "PrimerApellido", "SegundoApellido", "Genero", "FechaNacimiento",
                                                "Estrato", "Año", "Grupo")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query_insertar, (tipo_id, id_estudiante, primer_nombre, segundo_nombre,
                                        primer_apellido, segundo_apellido, genero, fecha_nacimiento,
                                        estrato, anio, grupo))
        print("Estudiante insertado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al insertar el estudiante: {e}")

def eliminar_estudiante(cursor):
    """Eliminar un estudiante específico por su ID."""
    id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")

    try:
        query_eliminar = """
        DELETE FROM "TempSchema"."Estudiantes"
        WHERE "IDEstudiante" = %s;
        """
        cursor.execute(query_eliminar, (id_estudiante,))
        print("Estudiante eliminado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al eliminar el estudiante: {e}")

def actualizar_estudiante(cursor):
    """Actualizar un estudiante específico."""
    id_estudiante = input("Ingrese el ID del estudiante a actualizar: ")
    nuevo_tipo_id = input("Ingrese el nuevo tipo de identificación (CC, TI, etc.): ").upper()
    nuevo_primer_nombre = input("Ingrese el nuevo primer nombre: ")
    nuevo_segundo_nombre = input("Ingrese el nuevo segundo nombre (opcional): ")
    nuevo_primer_apellido = input("Ingrese el nuevo primer apellido: ")
    nuevo_segundo_apellido = input("Ingrese el nuevo segundo apellido (opcional): ")
    nuevo_genero = input("Ingrese el nuevo género (M/F): ").upper()
    nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ")
    nuevo_estrato = input("Ingrese el nuevo estrato: ")
    nuevo_anio = input("Ingrese el nuevo año: ")
    nuevo_grupo = input("Ingrese el nuevo grupo: ")

    try:
        # Actualizar el estudiante
        query_actualizar = """
        UPDATE "TempSchema"."Estudiantes"
        SET "TipoID" = %s, "PrimerNombre" = %s, "SegundoNombre" = %s, "PrimerApellido" = %s,
            "SegundoApellido" = %s, "Genero" = %s, "FechaNacimiento" = %s, "Estrato" = %s, "Año" = %s, "Grupo" = %s
        WHERE "IDEstudiante" = %s;
        """
        cursor.execute(query_actualizar, (nuevo_tipo_id, nuevo_primer_nombre, nuevo_segundo_nombre,
                                          nuevo_primer_apellido, nuevo_segundo_apellido, nuevo_genero,
                                          nueva_fecha_nacimiento, nuevo_estrato, nuevo_anio, nuevo_grupo,
                                          id_estudiante))
        print("Estudiante actualizado exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al actualizar el estudiante: {e}")

def main():
    """Función principal con menú interactivo."""
    try:
        # Conexión a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                while True:
                    print("\n--- Gestión de Estudiantes ---")
                    print("1. Insertar estudiante")
                    print("2. Eliminar estudiante")
                    print("3. Actualizar estudiante")
                    print("4. Salir")
                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":
                        insertar_estudiante(cursor)
                    elif opcion == "2":
                        eliminar_estudiante(cursor)
                    elif opcion == "3":
                        actualizar_estudiante(cursor)
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
