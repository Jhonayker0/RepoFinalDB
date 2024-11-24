# instituciones.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Conexion import obtener_conexion, liberar_conexion
import psycopg2
from datetime import datetime

instituciones_bp = Blueprint('instituciones', __name__)

@instituciones_bp.route('/instituciones', methods=['POST'])
@jwt_required()

# Configuración de conexión a la base de datos
DATABASE_CONFIG = {
    "dbname": "DB",  
    "user": "postgres",         
    "password": "123456789",    
    "host": "127.0.0.1",          
    "port": "5432"                
}

def agregar_institucion_api():
    data = request.get_json()
    required_fields = ["codigo_insti", "nombre_insti", "nombre_rector", "localidad", 
                       "barrio", "numero", "direccion"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        codigo_insti = data["codigo_insti"]
        nombre_insti = data["nombre_insti"]
        nombre_rector = data["nombre_rector"]
        localidad = data["localidad"]
        barrio = data["barrio"]
        numero = data["numero"]
        direccion = data["direccion"]
        anio_actual = datetime.now().year

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar si la institución ya existe
        cursor.execute("""
            SELECT COUNT(*)
            FROM "TempSchema"."Institucion"
            WHERE "CodigoInsti" = %s;
        """, (codigo_insti,))
        existe = cursor.fetchone()[0]

        if existe > 0:
            return jsonify({"error": "La institución ya existe"}), 400

        # Insertar institución
        cursor.execute("""
            INSERT INTO "TempSchema"."Institucion" 
            ("CodigoInsti", "NombreInsti", "NombreRector", "Localidad", 
             "Barrio", "Numero", "Direccion", "Año")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            codigo_insti, nombre_insti, nombre_rector, localidad, 
            barrio, numero, direccion, anio_actual
        ))
        conexion.commit()

        return jsonify({"message": "Institución agregada exitosamente"}), 201

    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@instituciones_bp.route('/instituciones/<codigo_insti>', methods=['DELETE'])
@jwt_required()
def eliminar_institucion_api(codigo_insti):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM "TempSchema"."Institucion"
            WHERE "CodigoInsti" = %s;
        """, (codigo_insti,))
        conexion.commit()

        return jsonify({"message": "Institución eliminada exitosamente"}), 200
    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if conexion:
            liberar_conexion(conexion)

@instituciones_bp.route('/instituciones/<codigo_insti>', methods=['PUT'])
@jwt_required()
def editar_institucion_api(codigo_insti):
    data = request.get_json()
    required_fields = ["nombre_insti", "nombre_rector", "localidad", "barrio", 
                       "numero", "direccion"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        nombre_insti = data["nombre_insti"]
        nombre_rector = data["nombre_rector"]
        localidad = data["localidad"]
        barrio = data["barrio"]
        numero = data["numero"]
        direccion = data["direccion"]
        anio_actual = datetime.now().year

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Actualizar institución
        cursor.execute("""
            UPDATE "TempSchema"."Institucion"
            SET "NombreInsti" = %s, "NombreRector" = %s, "Localidad" = %s, "Barrio" = %s, 
                "Numero" = %s, "Direccion" = %s, "Año" = %s
            WHERE "CodigoInsti" = %s;
        """, (
            nombre_insti, nombre_rector, localidad, barrio,
            numero, direccion, anio_actual, codigo_insti
        ))
        conexion.commit()

        return jsonify({"message": "Institución actualizada exitosamente"}), 200

    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)
