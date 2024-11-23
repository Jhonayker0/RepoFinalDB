import psycopg2
from datetime import datetime

# Configuración de conexión a la base de datos
DATABASE_CONFIG = {
    "dbname": "DB",  
    "user": "postgres",         
    "password": "123456789",    
    "host": "127.0.0.1",          
    "port": "5432"                
}


def agregar_institucion(cursor):
    """Agregar una nueva institución."""
    codigo_insti = input("Ingrese el código de la institución: ")
    nombre_insti = input("Ingrese el nombre de la institución: ")
    nombre_rector = input("Ingrese el nombre del rector: ")
    localidad = input("Ingrese la localidad de la institución: ")
    barrio = input("Ingrese el barrio de la institución: ")
    numero = input("Ingrese el número de la institución: ")
    direccion = input("Ingrese la dirección de la institución: ")

    # Obtener el año actual
    anio_actual = datetime.now().year

    try:
        query = """
        INSERT INTO "TempSchema"."Institucion" ("CodigoInsti", "NombreInsti", "NombreRector", "Localidad", "Barrio", "Numero", "Direccion", "Año")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (codigo_insti, nombre_insti, nombre_rector, localidad, barrio, numero, direccion, anio_actual))
        print("Institución agregada exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al agregar la institución: {e}")

def eliminar_institucion(cursor):
    """Eliminar una institución por su CódigoInsti."""
    codigo_insti = input("Ingrese el código de la institución a eliminar: ")

    try:
        query = """
        DELETE FROM "TempSchema"."Institucion"
        WHERE "CodigoInsti" = %s;
        """
        cursor.execute(query, (codigo_insti,))
        print("Institución eliminada exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al eliminar la institución: {e}")

def editar_institucion(cursor):
    """Editar una institución existente."""
    codigo_insti = input("Ingrese el código de la institución a editar: ")

    nuevo_nombre_insti = input("Ingrese el nuevo nombre de la institución: ")
    nuevo_nombre_rector = input("Ingrese el nuevo nombre del rector: ")
    nueva_localidad = input("Ingrese la nueva localidad: ")
    nuevo_barrio = input("Ingrese el nuevo barrio: ")
    nuevo_numero = input("Ingrese el nuevo número: ")
    nueva_direccion = input("Ingrese la nueva dirección: ")

    # Obtener el año actual
    anio_actual = datetime.now().year

    try:
        query = """
        UPDATE "TempSchema"."Institucion"
        SET "NombreInsti" = %s, "NombreRector" = %s, "Localidad" = %s, "Barrio" = %s, 
            "Numero" = %s, "Direccion" = %s, "Año" = %s
        WHERE "CodigoInsti" = %s;
        """
        cursor.execute(query, (nuevo_nombre_insti, nuevo_nombre_rector, nueva_localidad, nuevo_barrio, nuevo_numero, nueva_direccion, anio_actual, codigo_insti))
        print("Institución actualizada exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al actualizar la institución: {e}")

def main():
    """Función principal con menú interactivo."""
    try:
        # Conexión a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                while True:
                    print("\n--- Gestión de Instituciones ---")
                    print("1. Agregar institución")
                    print("2. Eliminar institución")
                    print("3. Editar institución")
                    print("4. Salir")
                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":
                        agregar_institucion(cursor)
                    elif opcion == "2":
                        eliminar_institucion(cursor)
                    elif opcion == "3":
                        editar_institucion(cursor)
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
