# reportes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Conexion import obtener_conexion, liberar_conexion
import psycopg2
from datetime import datetime

reportes_bp = Blueprint('reportes', __name__)

@reportes_bp.route('/reportes/aulas', methods=['GET'])
@jwt_required()

# Configuración de conexión a la base de datos
DATABASE_CONFIG = {
    "dbname": "DB",  
    "user": "postgres",         
    "password": "123456789",    
    "host": "127.0.0.1",          
    "port": "5432"                
}
def reporte_aulas_api():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT a."Grupo", a."GradoT", a."GradoNum", a."GrupoEquivalente", 
                   a."Jornada", a."Año", i."NombreInsti",
                   p."PrimerNombre", p."PrimerApellido"
            FROM "TempSchema"."Aula" a
            INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
            INNER JOIN "TempSchema"."Usuario" u ON a."IDUsuario" = u."IDUsuario"
            INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
            ORDER BY a."Año" DESC, a."Grupo";
        """)
        aulas = cursor.fetchall()

        if not aulas:
            return jsonify({"message": "No se encontraron aulas registradas."}), 404

        # Formatear los datos en JSON
        reporte = []
        for aula in aulas:
            reporte.append({
                "grupo": aula[0],
                "grado_t": aula[1] or "N/A",
                "grado_num": aula[2] or "N/A",
                "grupo_equivalente": aula[3] or "N/A",
                "jornada": aula[4] or "N/A",
                "anio": aula[5],
                "institucion": aula[6] or "N/A",
                "tutor": f"{aula[7]} {aula[8]}"  # Nombre completo del tutor
            })

        return jsonify({"reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@reportes_bp.route('/reportes/aulas_tutor', methods=['GET'])
@jwt_required()
def reporte_aulas_tutor_api():
    id_usuario = request.args.get('id_usuario')

    if not id_usuario:
        return jsonify({"error": "El parámetro 'id_usuario' es requerido"}), 400

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT a."Grupo", a."GradoT", a."GradoNum", a."Jornada", i."NombreInsti"
            FROM "TempSchema"."Aula" a
            INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
            WHERE a."IDUsuario" = %s
            ORDER BY a."Grupo";
        """, (id_usuario,))
        aulas_tutor = cursor.fetchall()

        if not aulas_tutor:
            return jsonify({"message": f"No se encontraron aulas asociadas al tutor con IDUsuario {id_usuario}"}), 404

        reporte = []
        for aula in aulas_tutor:
            reporte.append({
                "grupo": aula[0],
                "grado_t": aula[1],
                "grado_num": aula[2],
                "jornada": aula[3],
                "institucion": aula[4]
            })

        return jsonify({"id_usuario": id_usuario, "reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@reportes_bp.route('/reportes/estudiantes_aula', methods=['GET'])
@jwt_required()
def reporte_estudiantes_aula_api():
    grupo = request.args.get('grupo')

    if not grupo:
        return jsonify({"error": "El parámetro 'grupo' es requerido"}), 400

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT e."IDEstudiante", e."PrimerNombre", e."PrimerApellido", 
                   a."Grupo", i."NombreInsti"
            FROM "TempSchema"."Estudiantes" e
            INNER JOIN "TempSchema"."Aula" a ON e."Grupo" = a."Grupo"
            INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
            WHERE a."Grupo" = %s
            ORDER BY e."PrimerApellido", e."PrimerNombre";
        """, (grupo,))
        estudiantes = cursor.fetchall()

        if not estudiantes:
            return jsonify({"message": f"No se encontraron estudiantes registrados en el aula con Grupo {grupo}"}), 404

        reporte = []
        for estudiante in estudiantes:
            reporte.append({
                "id_estudiante": estudiante[0],
                "nombre_completo": f"{estudiante[1]} {estudiante[2]}",
                "grupo": estudiante[3],
                "institucion": estudiante[4]
            })

        return jsonify({"grupo": grupo, "reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@reportes_bp.route('/reportes/instituciones', methods=['GET'])
@jwt_required()
def reporte_instituciones_api():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT i."CodigoInsti", i."NombreInsti", i."NombreRector", i."Localidad", 
                   i."Barrio", i."Numero", i."Direccion", i."Año"
            FROM "TempSchema"."Institucion" i
            ORDER BY i."NombreInsti";
        """)
        instituciones = cursor.fetchall()

        if not instituciones:
            return jsonify({"message": "No se encontraron instituciones registradas"}), 404

        reporte = []
        for institucion in instituciones:
            reporte.append({
                "codigo": institucion[0],
                "nombre": institucion[1],
                "rector": institucion[2],
                "localidad": institucion[3] or "N/A",
                "barrio": institucion[4] or "N/A",
                "numero": institucion[5] or "N/A",
                "direccion": institucion[6] or "N/A",
                "anio": institucion[7]
            })

        return jsonify({"reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@reportes_bp.route('/reportes/personas', methods=['GET'])
@jwt_required()
def reporte_personas_api():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT p."TipoID", p."Identificacion", p."IDUsuario", 
                   p."PrimerNombre", p."SegundoNombre", 
                   p."PrimerApellido", p."SegundoApellido", 
                   p."Correo", p."Telefono"
            FROM "TempSchema"."Persona" p
            ORDER BY p."PrimerApellido", p."SegundoApellido", p."PrimerNombre";
        """)
        personas = cursor.fetchall()

        if not personas:
            return jsonify({"message": "No se encontraron personas registradas"}), 404

        reporte = []
        for persona in personas:
            nombre_completo = f"{persona[3]}"
            if persona[4]:
                nombre_completo += f" {persona[4]}"
            nombre_completo += f" {persona[5]}"
            if persona[6]:
                nombre_completo += f" {persona[6]}"
            reporte.append({
                "tipo_id": persona[0],
                "identificacion": persona[1],
                "id_usuario": persona[2] or "N/A",
                "nombre_completo": nombre_completo.strip(),
                "correo": persona[7] or "N/A",
                "telefono": persona[8] or "N/A"
            })

        return jsonify({"reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@reportes_bp.route('/reportes/tutores', methods=['GET'])
@jwt_required()
def reporte_tutores_api():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT p."IDUsuario", p."PrimerNombre", p."PrimerApellido", 
                   p."Correo", p."Telefono"
            FROM "TempSchema"."Usuario" u
            INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
            WHERE u."Rol" = 'Tutor';
        """)
        tutores = cursor.fetchall()

        if not tutores:
            return jsonify({"message": "No se encontraron tutores registrados"}), 404

        reporte = []
        for tutor in tutores:
            reporte.append({
                "id_usuario": tutor[0],
                "nombre": tutor[1],
                "apellido": tutor[2],
                "correo": tutor[3] or "N/A",
                "telefono": tutor[4] or "N/A"
            })

        return jsonify({"reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)

@reportes_bp.route('/reportes/calificaciones_aula', methods=['GET'])
@jwt_required()
def calificaciones_aula_api():
    grupo = request.args.get('grupo')
    anio = request.args.get('anio')

    if not grupo or not anio:
        return jsonify({"error": "Los parámetros 'grupo' y 'anio' son requeridos"}), 400

    try:
        anio = int(anio)
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT a."Grupo", e."IDEstudiante", e."PrimerNombre", e."PrimerApellido",
                   ex."Nota", ex."BloqueLectivo", ex."Año"
            FROM "TempSchema"."Examen" ex
            INNER JOIN "TempSchema"."Estudiantes" e ON ex."IDEstudiante" = e."IDEstudiante"
            INNER JOIN "TempSchema"."Aula" a ON e."Grupo" = a."Grupo"
            WHERE a."Grupo" = %s AND ex."Año" = %s
            ORDER BY ex."BloqueLectivo", e."PrimerApellido", e."PrimerNombre";
        """, (grupo, anio))
        calificaciones = cursor.fetchall()

        if not calificaciones:
            return jsonify({"message": f"No se encontraron calificaciones registradas para el grupo {grupo} en el año {anio}"}), 404

        reporte = []
        for calificacion in calificaciones:
            reporte.append({
                "id_estudiante": calificacion[1],
                "nombre": f"{calificacion[2]} {calificacion[3]}",
                "nota": calificacion[4],
                "bloque_lectivo": calificacion[5]
            })

        return jsonify({"grupo": grupo, "anio": anio, "reporte": reporte}), 200

    except ValueError:
        return jsonify({"error": "El parámetro 'anio' debe ser un número válido"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if conexion:
            liberar_conexion(conexion)
