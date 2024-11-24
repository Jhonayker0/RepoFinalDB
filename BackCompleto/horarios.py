# horarios.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Conexion import obtener_conexion, liberar_conexion
import psycopg2
from datetime import datetime

horarios_bp = Blueprint('horarios', __name__)

@horarios_bp.route('/horarios', methods=['POST'])
@jwt_required()

# Configuración de conexión a la base de datos
DATABASE_CONFIG = {
    "dbname": "DB",  
    "user": "postgres",         
    "password": "123456789",    
    "host": "127.0.0.1",          
    "port": "5432"                
}

def insertar_horario_api():
    data = request.get_json()
    required_fields = ["fecha_inicio", "fecha_fin", "hora_inicio", "hora_fin", "dia_inicial", "dia_texto"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        fecha_inicio = data["fecha_inicio"]
        fecha_fin = data["fecha_fin"]
        hora_inicio = data["hora_inicio"]
        hora_fin = data["hora_fin"]
        dia_inicial = data["dia_inicial"].upper()
        dia_texto = data["dia_texto"].upper()

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar si el horario ya existe
        cursor.execute("""
            SELECT COUNT(*)
            FROM "TempSchema"."Horario"
            WHERE "HoraInicio" = %s AND "HoraFin" = %s AND "DiaTexto" = %s;
        """, (hora_inicio, hora_fin, dia_texto))
        existe = cursor.fetchone()[0]

        if existe > 0:
            return jsonify({"error": "El horario ya existe para el mismo rango de horas en ese día"}), 400

        # Insertar horario
        cursor.execute("""
            INSERT INTO "TempSchema"."Horario" 
            ("FechaInicio", "FechaFin", "HoraInicio", "HoraFin", "DiaInicial", "DiaTexto")
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (
            fecha_inicio, fecha_fin, hora_inicio, hora_fin, dia_inicial, dia_texto
        ))
        conexion.commit()

        return jsonify({"message": "Horario insertado exitosamente"}), 201

    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@horarios_bp.route('/horarios/<int:codigo_h>', methods=['DELETE'])
@jwt_required()
def eliminar_horario_api(codigo_h):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM "TempSchema"."Horario"
            WHERE "CodigoH" = %s;
        """, (codigo_h,))
        conexion.commit()

        return jsonify({"message": f"Horario con CodigoH = {codigo_h} eliminado exitosamente"}), 200
    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if conexion:
            liberar_conexion(conexion)

@horarios_bp.route('/horarios/<int:codigo_h>', methods=['PUT'])
@jwt_required()
def actualizar_horario_api(codigo_h):
    data = request.get_json()
    required_fields = ["fecha_inicio", "fecha_fin", "hora_inicio", "hora_fin", "dia_inicial", "dia_texto"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        fecha_inicio = data["fecha_inicio"]
        fecha_fin = data["fecha_fin"]
        hora_inicio = data["hora_inicio"]
        hora_fin = data["hora_fin"]
        dia_inicial = data["dia_inicial"].upper()
        dia_texto = data["dia_texto"].upper()

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Verificar si el nuevo horario ya existe
        cursor.execute("""
            SELECT COUNT(*)
            FROM "TempSchema"."Horario"
            WHERE "HoraInicio" = %s AND "HoraFin" = %s AND "DiaTexto" = %s AND "CodigoH" != %s;
        """, (hora_inicio, hora_fin, dia_texto, codigo_h))
        existe = cursor.fetchone()[0]

        if existe > 0:
            return jsonify({"error": "El horario ya existe para el mismo rango de horas en ese día"}), 400

        # Actualizar horario
        cursor.execute("""
            UPDATE "TempSchema"."Horario"
            SET "FechaInicio" = %s, "FechaFin" = %s, "HoraInicio" = %s, "HoraFin" = %s, 
                "DiaInicial" = %s, "DiaTexto" = %s
            WHERE "CodigoH" = %s;
        """, (
            fecha_inicio, fecha_fin, hora_inicio, hora_fin, dia_inicial, dia_texto, codigo_h
        ))
        conexion.commit()

        return jsonify({"message": f"Horario con CodigoH = {codigo_h} actualizado exitosamente"}), 200

    except Exception as e:
        if conexion:
            conexion.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)
