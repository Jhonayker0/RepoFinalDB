from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Conexion import obtener_conexion, liberar_conexion
import psycopg2
from datetime import datetime

estudiantes_bp = Blueprint('estudiantes', __name__)

@estudiantes_bp.route('/estudiantes', methods=['POST'])
@jwt_required()

# Configuración de conexión a la base de datos
DATABASE_CONFIG = {
    "dbname": "DB",  
    "user": "postgres",         
    "password": "123456789",    
    "host": "127.0.0.1",          
    "port": "5432"                
}

def insertar_estudiante_api():
    data = request.get_json()
    required_fields = ["tipo_id", "id_estudiante", "primer_nombre", "primer_apellido",
                       "genero", "fecha_nacimiento", "estrato", "anio", "grupo"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        tipo_id = data["tipo_id"].upper()
        id_estudiante = data["id_estudiante"]
        primer_nombre = data["primer_nombre"]
        segundo_nombre = data.get("segundo_nombre", None)
        primer_apellido = data["primer_apellido"]
        segundo_apellido = data.get("segundo_apellido", None)
        genero = data["genero"].upper()
        fecha_nacimiento = data["fecha_nacimiento"]
        estrato = data["estrato"]
        anio = data["anio"]
        grupo = data["grupo"]

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar si el estudiante ya existe
        cursor.execute("""
            SELECT COUNT(*)
            FROM "TempSchema"."Estudiantes"
            WHERE "TipoID" = %s AND "IDEstudiante" = %s;
        """, (tipo_id, id_estudiante))
        existe = cursor.fetchone()[0]

        if existe > 0:
            return jsonify({"error": "El estudiante ya existe"}), 400

        # Insertar estudiante
        cursor.execute("""
            INSERT INTO "TempSchema"."Estudiantes" 
            ("TipoID", "IDEstudiante", "PrimerNombre", "SegundoNombre",
             "PrimerApellido", "SegundoApellido", "Genero", "FechaNacimiento",
             "Estrato", "Año", "Grupo")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            tipo_id, id_estudiante, primer_nombre, segundo_nombre,
            primer_apellido, segundo_apellido, genero, fecha_nacimiento,
            estrato, anio, grupo
        ))
        conexion.commit()

        return jsonify({"message": "Estudiante insertado exitosamente"}), 201

    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@estudiantes_bp.route('/estudiantes/<id_estudiante>', methods=['DELETE'])
@jwt_required()
def eliminar_estudiante_api(id_estudiante):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM "TempSchema"."Estudiantes"
            WHERE "IDEstudiante" = %s;
        """, (id_estudiante,))
        conexion.commit()

        return jsonify({"message": "Estudiante eliminado exitosamente"}), 200
    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if conexion:
            liberar_conexion(conexion)

@estudiantes_bp.route('/estudiantes/<id_estudiante>', methods=['PUT'])
@jwt_required()
def actualizar_estudiante_api(id_estudiante):
    data = request.get_json()
    required_fields = ["tipo_id", "primer_nombre", "primer_apellido",
                       "genero", "fecha_nacimiento", "estrato", "anio", "grupo"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        tipo_id = data["tipo_id"].upper()
        nuevo_primer_nombre = data["primer_nombre"]
        nuevo_segundo_nombre = data.get("segundo_nombre", None)
        nuevo_primer_apellido = data["primer_apellido"]
        nuevo_segundo_apellido = data.get("segundo_apellido", None)
        genero = data["genero"].upper()
        fecha_nacimiento = data["fecha_nacimiento"]
        estrato = data["estrato"]
        anio = data["anio"]
        grupo = data["grupo"]

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Actualizar estudiante
        cursor.execute("""
            UPDATE "TempSchema"."Estudiantes"
            SET "TipoID" = %s, "PrimerNombre" = %s, "SegundoNombre" = %s, "PrimerApellido" = %s,
                "SegundoApellido" = %s, "Genero" = %s, "FechaNacimiento" = %s, "Estrato" = %s, 
                "Año" = %s, "Grupo" = %s
            WHERE "IDEstudiante" = %s;
        """, (
            tipo_id, nuevo_primer_nombre, nuevo_segundo_nombre,
            nuevo_primer_apellido, nuevo_segundo_apellido, genero,
            fecha_nacimiento, estrato, anio, grupo, id_estudiante
        ))
        conexion.commit()

        return jsonify({"message": "Estudiante actualizado exitosamente"}), 200

    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)
