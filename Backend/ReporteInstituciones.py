import psycopg2

# Configuración de conexión
DATABASE_CONFIG = {
    "dbname": "DB",
    "user": "postgres",
    "password": "123456789",
    "host": "127.0.0.1",
    "port": "5432"
}

def generar_reporte_instituciones(cursor):
    try:
        # Consulta para obtener los datos de las instituciones
        query_reporte_instituciones = """
        SELECT i."CodigoInsti", i."NombreInsti", i."NombreRector", i."Localidad", 
               i."Barrio", i."Numero", i."Direccion", i."Año"
        FROM "TempSchema"."Institucion" i
        ORDER BY i."NombreInsti";
        """
        cursor.execute(query_reporte_instituciones)
        instituciones = cursor.fetchall()

        if not instituciones:
            print("No se encontraron instituciones registradas.")
            return

        print(f"\n=== Reporte de Instituciones ===\n")
        print(f"{'Código':<12} {'Nombre':<30} {'Rector':<25} {'Localidad':<20} {'Barrio':<20} {'Número':<10} {'Dirección':<25} {'Año':<6}")
        print("-" * 150)

        for institucion in instituciones:
            codigo = institucion[0]
            nombre = institucion[1]
            rector = institucion[2]
            localidad = institucion[3] or "N/A"
            barrio = institucion[4] or "N/A"
            numero = institucion[5] or "N/A"
            direccion = institucion[6] or "N/A"
            anio = institucion[7]

            print(f"{codigo:<12} {nombre:<30} {rector:<25} {localidad:<20} {barrio:<20} {numero:<10} {direccion:<25} {anio:<6}")

    except psycopg2.Error as e:
        print(f"Error al generar el reporte de instituciones: {e}")

def main():
    try:
        # Conectar a la base de datos
        with psycopg2.connect(**DATABASE_CONFIG) as conn:
            with conn.cursor() as cursor:
                generar_reporte_instituciones(cursor)
    except psycopg2.Error as e:
        print(f"Error de conexión a la base de datos: {e}")

if __name__ == "__main__":
    main()
