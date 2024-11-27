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

def agregar_usuario(cursor):
    """Agregar un nuevo usuario y su información asociada en Persona."""
    rol = input("Ingrese el rol del usuario: ")
    pwd = input("Ingrese la contraseña del usuario: ")

    tipo_id = input("Ingrese el tipo de ID de la persona: ")
    identificacion = input("Ingrese la identificación de la persona: ")
    primer_nombre = input("Ingrese el primer nombre: ")
    segundo_nombre = input("Ingrese el segundo nombre (opcional): ")
    primer_apellido = input("Ingrese el primer apellido: ")
    segundo_apellido = input("Ingrese el segundo apellido (opcional): ")
    correo = input("Ingrese el correo electrónico: ")
    telefono = input("Ingrese el teléfono: ")

    # Obtener el año actual
    anio_actual = datetime.now().year

    try:
        # Agregar el usuario
        usuario_query = """
        INSERT INTO "TempSchema"."Usuario" ("Rol", "Pwd", "Año")
        VALUES (%s, %s, %s)
        RETURNING "IDUsuario";
        """
        cursor.execute(usuario_query, (rol, pwd, anio_actual))
        id_usuario = cursor.fetchone()[0]

        # Agregar la persona asociada
        persona_query = """
        INSERT INTO "TempSchema"."Persona" ("TipoID", "Identificacion", "PrimerNombre", "SegundoNombre",
                                            "PrimerApellido", "SegundoApellido", "Correo", "Telefono", "Año", "IDUsuario")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(persona_query, (
            tipo_id, identificacion, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
            correo, telefono, anio_actual, id_usuario
        ))
        print("Usuario y Persona agregados exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al agregar usuario y persona: {e}")

def eliminar_usuario(cursor):
    """Eliminar un usuario y su información asociada en Persona basado en la Identificacion."""
    identificacion = input("Ingrese la identificación de la persona a eliminar: ")

    try:
        # Obtener el IDUsuario asociado a la identificación
        obtener_usuario_query = """
        SELECT "IDUsuario"
        FROM "TempSchema"."Persona"
        WHERE "Identificacion" = %s;
        """
        cursor.execute(obtener_usuario_query, (identificacion,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("No se encontró una persona con esa identificación.")
            return

        id_usuario = resultado[0]

        # Eliminar la persona asociada
        persona_query = """
        DELETE FROM "TempSchema"."Persona"
        WHERE "Identificacion" = %s;
        """
        cursor.execute(persona_query, (identificacion,))

        # Eliminar el usuario
        usuario_query = """
        DELETE FROM "TempSchema"."Usuario"
        WHERE "IDUsuario" = %s;
        """
        cursor.execute(usuario_query, (id_usuario,))
        print("Usuario y Persona eliminados exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al eliminar usuario y persona: {e}")

def actualizar_usuario(cursor):
    """Actualizar un usuario y su información asociada en Persona basado en la Identificacion."""
    identificacion = input("Ingrese la identificación de la persona a actualizar: ")

    nuevo_rol = input("Ingrese el nuevo rol del usuario: ")
    nueva_pwd = input("Ingrese la nueva contraseña: ")
    nuevo_tipo_id = input("Ingrese el nuevo tipo de ID de la persona: ")
    nueva_identificacion = input("Ingrese la nueva identificación: ")
    nuevo_primer_nombre = input("Ingrese el nuevo primer nombre: ")
    nuevo_segundo_nombre = input("Ingrese el nuevo segundo nombre (opcional): ")
    nuevo_primer_apellido = input("Ingrese el nuevo primer apellido: ")
    nuevo_segundo_apellido = input("Ingrese el nuevo segundo apellido (opcional): ")
    nuevo_correo = input("Ingrese el nuevo correo electrónico: ")
    nuevo_telefono = input("Ingrese el nuevo teléfono: ")

    # Obtener el año actual
    anio_actual = datetime.now().year

    try:
        # Obtener el IDUsuario asociado a la identificación
        obtener_usuario_query = """
        SELECT "IDUsuario"
        FROM "TempSchema"."Persona"
        WHERE "Identificacion" = %s;
        """
        cursor.execute(obtener_usuario_query, (identificacion,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("No se encontró una persona con esa identificación.")
            return

        id_usuario = resultado[0]

        # Actualizar el usuario
        usuario_query = """
        UPDATE "TempSchema"."Usuario"
        SET "Rol" = %s, "Pwd" = %s, "Año" = %s
        WHERE "IDUsuario" = %s;
        """
        cursor.execute(usuario_query, (nuevo_rol, nueva_pwd, anio_actual, id_usuario))

        # Actualizar la persona asociada
        persona_query = """
        UPDATE "TempSchema"."Persona"
        SET "TipoID" = %s, "Identificacion" = %s, "PrimerNombre" = %s, "SegundoNombre" = %s,
            "PrimerApellido" = %s, "SegundoApellido" = %s, "Correo" = %s, "Telefono" = %s, "Año" = %s
        WHERE "Identificacion" = %s;
        """
        cursor.execute(persona_query, (
            nuevo_tipo_id, nueva_identificacion, nuevo_primer_nombre, nuevo_segundo_nombre,
            nuevo_primer_apellido, nuevo_segundo_apellido, nuevo_correo, nuevo_telefono,
            anio_actual, identificacion
        ))
        print("Usuario y Persona actualizados exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al actualizar usuario y persona: {e}")

def main():
    """Función principal con menú interactivo."""
    try:
        # Conexión a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                while True:
                    print("\n--- Gestión de Usuarios y Personas ---")
                    print("1. Agregar usuario y persona")
                    print("2. Eliminar usuario y persona")
                    print("3. Actualizar usuario y persona")
                    print("4. Salir")
                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":
                        agregar_usuario(cursor)
                    elif opcion == "2":
                        eliminar_usuario(cursor)
                    elif opcion == "3":
                        actualizar_usuario(cursor)
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
