# aulas.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Conexion import obtener_conexion, liberar_conexion
import psycopg2
from datetime import datetime

aulas_bp = Blueprint('aulas', __name__)

@aulas_bp.route('/aulas', methods=['POST'])
@jwt_required()

# Configuración de conexión a la base de datos
DATABASE_CONFIG = {
    "dbname": "DB",  
    "user": "postgres",         
    "password": "123456789",    
    "host": "127.0.0.1",          
    "port": "5432"                
}

def agregar_aula_api():
    data = request.get_json()
    required_fields = ["grado_t", "grado_num", "grupo_equivalente", "jornada", "codigo_insti", "id_usuario"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        grado_t = data["grado_t"]
        grado_num = data["grado_num"]
        grupo_equivalente = data["grupo_equivalente"]
        jornada = data["jornada"]
        codigo_insti = data["codigo_insti"]
        id_usuario = data["id_usuario"]
        anio_actual = datetime.now().year

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Obtener el siguiente grupo
        cursor.execute("""
            SELECT COALESCE(MAX("Grupo"), 0) + 1 AS siguiente_grupo FROM "TempSchema"."Aula";
        """)
        siguiente_grupo = cursor.fetchone()[0]

        # Insertar el aula
        cursor.execute("""
            INSERT INTO "TempSchema"."Aula" 
            ("Grupo", "GradoT", "GradoNum", "GrupoEquivalente", "Jornada", "Año", "CodigoInsti", "IDUsuario")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            siguiente_grupo, grado_t, grado_num, grupo_equivalente, jornada, anio_actual, codigo_insti, id_usuario
        ))
        conexion.commit()

        return jsonify({"message": f"Aula agregada exitosamente con Grupo = {siguiente_grupo}"}), 201

    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@aulas_bp.route('/aulas/<int:grupo>', methods=['DELETE'])
@jwt_required()
def eliminar_aula_api(grupo):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM "TempSchema"."Aula"
            WHERE "Grupo" = %s;
        """, (grupo,))
        conexion.commit()

        return jsonify({"message": f"Aula con Grupo = {grupo} eliminada exitosamente"}), 200
    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if conexion:
            liberar_conexion(conexion)

@aulas_bp.route('/aulas/<int:grupo>', methods=['PUT'])
@jwt_required()
def editar_aula_api(grupo):
    data = request.get_json()
    required_fields = ["grado_t", "grado_num", "grupo_equivalente", "jornada", "codigo_insti", "id_usuario"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        grado_t = data["grado_t"]
        grado_num = data["grado_num"]
        grupo_equivalente = data["grupo_equivalente"]
        jornada = data["jornada"]
        codigo_insti = data["codigo_insti"]
        id_usuario = data["id_usuario"]
        anio_actual = datetime.now().year

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE "TempSchema"."Aula"
            SET "GradoT" = %s, "GradoNum" = %s, "GrupoEquivalente" = %s, 
                "Jornada" = %s, "Año" = %s, "CodigoInsti" = %s, "IDUsuario" = %s
            WHERE "Grupo" = %s;
        """, (
            grado_t, grado_num, grupo_equivalente, jornada, anio_actual, codigo_insti, id_usuario, grupo
        ))
        conexion.commit()

        return jsonify({"message": f"Aula con Grupo = {grupo} actualizada exitosamente"}), 200

    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)
