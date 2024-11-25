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

def calificar_estudiante(id_estudiante, nota, bloque_lectivo, cursor):
    try:
        # Validar que el estudiante exista
        query_verificar_estudiante = """
        SELECT COUNT(*)
        FROM "TempSchema"."Estudiante"
        WHERE "IDEstudiante" = %s;
        """
        cursor.execute(query_verificar_estudiante, (id_estudiante,))
        estudiante_existe = cursor.fetchone()[0]

        if estudiante_existe == 0:
            print(f"El estudiante con ID {id_estudiante} no existe.")
            return

        # Obtener el año actual
        anio_actual = datetime.now().year

        # Insertar la calificación en la tabla Examen
        query_insertar_calificacion = """
        INSERT INTO "TempSchema"."Examen" ("Nota", "BloqueLectivo", "Año", "IDEstudiante")
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query_insertar_calificacion, (nota, bloque_lectivo, anio_actual, id_estudiante))
        print(f"Calificación registrada exitosamente para el estudiante con ID {id_estudiante}.")

    except psycopg2.Error as e:
        print(f"Error al registrar la calificación: {e}")

def main():
    try:
        # Solicitar datos al usuario
        id_estudiante = input("Ingrese el ID del estudiante a calificar: ")
        nota = float(input("Ingrese la nota del estudiante: "))
        bloque_lectivo = input("Ingrese el bloque lectivo: ")

        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                calificar_estudiante(id_estudiante, nota, bloque_lectivo, cursor)
                conn.commit()
    except ValueError:
        print("Error: La nota debe ser un número válido.")
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")


if __name__ == "__main__":
    main()
