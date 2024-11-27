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

def obtener_siguiente_grupo(cursor):
    """Obtiene el próximo valor para la columna 'Grupo'."""
    try:
        query = """
        SELECT COALESCE(MAX("Grupo"), 0) + 1 AS siguiente_grupo
        FROM "TempSchema"."Aula";
        """
        cursor.execute(query)
        resultado = cursor.fetchone()
        return resultado[0] if resultado else 1
    except psycopg2.Error as e:
        print(f"Error al obtener el siguiente grupo: {e}")
        return None

def agregar_aula(cursor):
    """Agregar un nuevo aula."""
    siguiente_grupo = obtener_siguiente_grupo(cursor)
    if siguiente_grupo is None:
        print("No se pudo obtener el siguiente valor para 'Grupo'.")
        return

    grado_t = input("Ingrese el tipo de grado (GradoT): ")
    grado_num = input("Ingrese el número de grado (GradoNum): ")
    grupo_equivalente = input("Ingrese el grupo equivalente: ")
    jornada = input("Ingrese la jornada: ")
    codigo_insti = input("Ingrese el código de la institución asociada: ")
    id_usuario = input("Ingrese el IDUsuario del tutor asignado: ")

    # Obtener el año actual
    anio_actual = datetime.now().year

    try:
        query = """
        INSERT INTO "TempSchema"."Aula" ("Grupo", "GradoT", "GradoNum", "GrupoEquivalente", "Jornada", "Año", "CodigoInsti", "IDUsuario")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(query, (siguiente_grupo, grado_t, grado_num, grupo_equivalente, jornada, anio_actual, codigo_insti, id_usuario))
        print(f"Aula agregada exitosamente con Grupo = {siguiente_grupo}.")
    except psycopg2.Error as e:
        print(f"Error al agregar el aula: {e}")

def eliminar_aula(cursor):
    """Eliminar un aula por su Grupo."""
    grupo = input("Ingrese el número del grupo (Grupo) a eliminar: ")

    try:
        query = """
        DELETE FROM "TempSchema"."Aula"
        WHERE "Grupo" = %s;
        """
        cursor.execute(query, (grupo,))
        print("Aula eliminada exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al eliminar el aula: {e}")

def editar_aula(cursor):
    """Editar un aula existente."""
    grupo = input("Ingrese el número del grupo (Grupo) a editar: ")

    nuevo_grado_t = input("Ingrese el nuevo tipo de grado (GradoT): ")
    nuevo_grado_num = input("Ingrese el nuevo número de grado (GradoNum): ")
    nuevo_grupo_equivalente = input("Ingrese el nuevo grupo equivalente: ")
    nueva_jornada = input("Ingrese la nueva jornada: ")
    nuevo_codigo_insti = input("Ingrese el nuevo código de la institución asociada: ")
    nuevo_id_usuario = input("Ingrese el nuevo IDUsuario del tutor asignado: ")

    # Obtener el año actual
    anio_actual = datetime.now().year

    try:
        query = """
        UPDATE "TempSchema"."Aula"
        SET "GradoT" = %s, "GradoNum" = %s, "GrupoEquivalente" = %s, "Jornada" = %s, "Año" = %s, "CodigoInsti" = %s, "IDUsuario" = %s
        WHERE "Grupo" = %s;
        """
        cursor.execute(query, (nuevo_grado_t, nuevo_grado_num, nuevo_grupo_equivalente, nueva_jornada, anio_actual, nuevo_codigo_insti, nuevo_id_usuario, grupo))
        print("Aula actualizada exitosamente.")
    except psycopg2.Error as e:
        print(f"Error al actualizar el aula: {e}")

def main():
    """Función principal con menú interactivo."""
    try:
        # Conexión a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                while True:
                    print("\n--- Gestión de Aulas ---")
                    print("1. Agregar aula")
                    print("2. Eliminar aula")
                    print("3. Editar aula")
                    print("4. Salir")
                    opcion = input("Seleccione una opción: ")

                    if opcion == "1":
                        agregar_aula(cursor)
                    elif opcion == "2":
                        eliminar_aula(cursor)
                    elif opcion == "3":
                        editar_aula(cursor)
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
