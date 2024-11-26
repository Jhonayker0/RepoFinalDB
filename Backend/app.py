from flask import Flask, request, jsonify
from flask_cors import CORS
from InicioSesion import verificar_usuario
from Conexion import obtener_conexion
from datetime import datetime
app = Flask(__name__)
CORS(app)

@app.route('/obtener-rol', methods=['POST'])
def obtener_rol_api():
    # Obtener los datos del body
    data = request.get_json()
    identificacion = data.get('identificacion')
    password = data.get('password')

    # Validar los datos
    if not identificacion or not password:
        return jsonify({"error": "Identificación y contraseña son obligatorias"}), 400

    try:
        # Llamar a la función de la base de datos
        roles = verificar_usuario(identificacion, password)

        if not roles:
            return jsonify({"message": "No se encontró un rol para las credenciales proporcionadas"}), 404

        return jsonify({"roles": roles}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/agregar-usuario', methods=['POST'])
def agregar_usuario_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Datos requeridos
            rol = data['rol']
            pwd = data['pwd']
            tipo_id = data['tipo_id']
            identificacion = data['identificacion']
            primer_nombre = data['primer_nombre']
            segundo_nombre = data.get('segundo_nombre', None)
            primer_apellido = data['primer_apellido']
            segundo_apellido = data.get('segundo_apellido', None)
            correo = data['correo']
            telefono = data['telefono']
            anio_actual = datetime.now().year

            # Insertar usuario
            usuario_query = """
            INSERT INTO "TempSchema"."Usuario" ("Rol", "Pwd", "Año")
            VALUES (%s, %s, %s)
            RETURNING "IDUsuario";
            """
            cursor.execute(usuario_query, (rol, pwd, anio_actual))
            id_usuario = cursor.fetchone()[0]

            # Insertar persona
            persona_query = """
            INSERT INTO "TempSchema"."Persona" ("TipoID", "Identificacion", "PrimerNombre", "SegundoNombre",
                                                "PrimerApellido", "SegundoApellido", "Correo", "Telefono", "Año", "IDUsuario")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(persona_query, (
                tipo_id, identificacion, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
                correo, telefono, anio_actual, id_usuario
            ))
            conn.commit()

        return jsonify({"message": "Usuario y persona agregados exitosamente"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()


@app.route('/eliminar-usuario', methods=['DELETE'])
def eliminar_usuario_api():
    data = request.get_json()
    identificacion = data['identificacion']

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Obtener el IDUsuario
            obtener_usuario_query = """
            SELECT "IDUsuario"
            FROM "TempSchema"."Persona"
            WHERE "Identificacion" = %s;
            """
            cursor.execute(obtener_usuario_query, (identificacion,))
            resultado = cursor.fetchone()

            if resultado is None:
                return jsonify({"message": "No se encontró una persona con esa identificación"}), 404

            id_usuario = resultado[0]

            # Eliminar registros
            persona_query = """
            DELETE FROM "TempSchema"."Persona"
            WHERE "Identificacion" = %s;
            """
            cursor.execute(persona_query, (identificacion,))

            usuario_query = """
            DELETE FROM "TempSchema"."Usuario"
            WHERE "IDUsuario" = %s;
            """
            cursor.execute(usuario_query, (id_usuario,))
            conn.commit()

        return jsonify({"message": "Usuario y persona eliminados exitosamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()


@app.route('/actualizar-usuario', methods=['PUT'])
def actualizar_usuario_api():
    data = request.get_json()
    identificacion = data['identificacion']

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Obtener el IDUsuario
            obtener_usuario_query = """
            SELECT "IDUsuario"
            FROM "TempSchema"."Persona"
            WHERE "Identificacion" = %s;
            """
            cursor.execute(obtener_usuario_query, (identificacion,))
            resultado = cursor.fetchone()

            if resultado is None:
                return jsonify({"message": "No se encontró una persona con esa identificación"}), 404

            id_usuario = resultado[0]

            # Actualizar usuario
            usuario_query = """
            UPDATE "TempSchema"."Usuario"
            SET "Rol" = %s, "Pwd" = %s, "Año" = %s
            WHERE "IDUsuario" = %s;
            """
            cursor.execute(usuario_query, (
                data['nuevo_rol'], data['nueva_pwd'], datetime.now().year, id_usuario
            ))

            # Actualizar persona
            persona_query = """
            UPDATE "TempSchema"."Persona"
            SET "TipoID" = %s, "Identificacion" = %s, "PrimerNombre" = %s, "SegundoNombre" = %s,
                "PrimerApellido" = %s, "SegundoApellido" = %s, "Correo" = %s, "Telefono" = %s, "Año" = %s
            WHERE "Identificacion" = %s;
            """
            cursor.execute(persona_query, (
                data['nuevo_tipo_id'], data['nueva_identificacion'], data['nuevo_primer_nombre'],
                data.get('nuevo_segundo_nombre', None), data['nuevo_primer_apellido'],
                data.get('nuevo_segundo_apellido', None), data['nuevo_correo'], data['nuevo_telefono'],
                datetime.now().year, identificacion
            ))
            conn.commit()

        return jsonify({"message": "Usuario y persona actualizados exitosamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()

@app.route('/agregar-institucion', methods=['POST'])
def agregar_institucion_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            query = """
            INSERT INTO "TempSchema"."Institucion" ("CodigoInsti", "NombreInsti", "NombreRector", "Localidad", 
                                                    "Barrio", "Numero", "Direccion", "Año")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, (
                data['codigo_insti'], data['nombre_insti'], data['nombre_rector'], data['localidad'],
                data['barrio'], data['numero'], data['direccion'], datetime.now().year
            ))
            conn.commit()
        return jsonify({"message": "Institución agregada exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()


@app.route('/eliminar-institucion', methods=['DELETE'])
def eliminar_institucion_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            query = """
            DELETE FROM "TempSchema"."Institucion"
            WHERE "CodigoInsti" = %s;
            """
            cursor.execute(query, (data['codigo_insti'],))
            conn.commit()
        return jsonify({"message": "Institución eliminada exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()


@app.route('/editar-institucion', methods=['PUT'])
def editar_institucion_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            query = """
            UPDATE "TempSchema"."Institucion"
            SET "NombreInsti" = %s, "NombreRector" = %s, "Localidad" = %s, "Barrio" = %s, 
                "Numero" = %s, "Direccion" = %s, "Año" = %s
            WHERE "CodigoInsti" = %s;
            """
            cursor.execute(query, (
                data['nombre_insti'], data['nombre_rector'], data['localidad'], data['barrio'],
                data['numero'], data['direccion'], datetime.now().year, data['codigo_insti']
            ))
            conn.commit()
        return jsonify({"message": "Institución actualizada exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/insertar-estudiante', methods=['POST'])
def insertar_estudiante_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Validar si el estudiante ya existe
            query_validar = """
            SELECT COUNT(*)
            FROM "TempSchema"."Estudiantes"
            WHERE "TipoID" = %s AND "IDEstudiante" = %s;
            """
            cursor.execute(query_validar, (data['tipo_id'], data['id_estudiante']))
            existe = cursor.fetchone()[0]

            if existe > 0:
                return jsonify({"error": "El estudiante ya existe"}), 400

            # Insertar estudiante
            query_insertar = """
            INSERT INTO "TempSchema"."Estudiantes" ("TipoID", "IDEstudiante", "PrimerNombre", "SegundoNombre",
                                                    "PrimerApellido", "SegundoApellido", "Genero", "FechaNacimiento",
                                                    "Estrato", "Año", "Grupo")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query_insertar, (
                data['tipo_id'], data['id_estudiante'], data['primer_nombre'], data.get('segundo_nombre', None),
                data['primer_apellido'], data.get('segundo_apellido', None), data['genero'],
                data['fecha_nacimiento'], data['estrato'], data['anio'], data['grupo']
            ))
            conn.commit()
        return jsonify({"message": "Estudiante insertado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()


@app.route('/eliminar-estudiante', methods=['DELETE'])
def eliminar_estudiante_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            query_eliminar = """
            DELETE FROM "TempSchema"."Estudiantes"
            WHERE "IDEstudiante" = %s;
            """
            cursor.execute(query_eliminar, (data['id_estudiante'],))
            conn.commit()
        return jsonify({"message": "Estudiante eliminado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()


@app.route('/actualizar-estudiante', methods=['PUT'])
def actualizar_estudiante_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Actualizar estudiante
            query_actualizar = """
            UPDATE "TempSchema"."Estudiantes"
            SET "TipoID" = %s, "PrimerNombre" = %s, "SegundoNombre" = %s, "PrimerApellido" = %s,
                "SegundoApellido" = %s, "Genero" = %s, "FechaNacimiento" = %s, "Estrato" = %s, "Año" = %s, "Grupo" = %s
            WHERE "IDEstudiante" = %s;
            """
            cursor.execute(query_actualizar, (
                data['tipo_id'], data['primer_nombre'], data.get('segundo_nombre', None),
                data['primer_apellido'], data.get('segundo_apellido', None), data['genero'],
                data['fecha_nacimiento'], data['estrato'], data['anio'], data['grupo'], data['id_estudiante']
            ))
            conn.commit()
        return jsonify({"message": "Estudiante actualizado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/aulas/agregar', methods=['POST'])
def agregar_aula():
    data = request.get_json()

    required_fields = ["grado_t", "grado_num", "grupo_equivalente", "jornada", "codigo_insti", "id_usuario"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Obtener el siguiente valor para 'Grupo'
            query_siguiente_grupo = """
            SELECT COALESCE(MAX("Grupo"), 0) + 1 AS siguiente_grupo FROM "TempSchema"."Aula";
            """
            cursor.execute(query_siguiente_grupo)
            siguiente_grupo = cursor.fetchone()[0]

            # Insertar el aula
            query_insertar_aula = """
            INSERT INTO "TempSchema"."Aula" 
            ("Grupo", "GradoT", "GradoNum", "GrupoEquivalente", "Jornada", "Año", "CodigoInsti", "IDUsuario")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            anio_actual = datetime.now().year
            cursor.execute(query_insertar_aula, (
                siguiente_grupo, data["grado_t"], data["grado_num"], data["grupo_equivalente"],
                data["jornada"], anio_actual, data["codigo_insti"], data["id_usuario"]
            ))
            conn.commit()
            return jsonify({"message": f"Aula agregada exitosamente con Grupo = {siguiente_grupo}"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/aulas/eliminar/<int:grupo>', methods=['DELETE'])
def eliminar_aula(grupo):
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Eliminar el aula
            query_eliminar_aula = """
            DELETE FROM "TempSchema"."Aula" WHERE "Grupo" = %s;
            """
            cursor.execute(query_eliminar_aula, (grupo,))
            conn.commit()
            return jsonify({"message": f"Aula con Grupo = {grupo} eliminada exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/aulas/editar/<int:grupo>', methods=['PUT'])
def editar_aula(grupo):
    data = request.get_json()

    required_fields = ["grado_t", "grado_num", "grupo_equivalente", "jornada", "codigo_insti", "id_usuario"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Actualizar el aula
            query_actualizar_aula = """
            UPDATE "TempSchema"."Aula"
            SET "GradoT" = %s, "GradoNum" = %s, "GrupoEquivalente" = %s, 
                "Jornada" = %s, "Año" = %s, "CodigoInsti" = %s, "IDUsuario" = %s
            WHERE "Grupo" = %s;
            """
            anio_actual = datetime.now().year
            cursor.execute(query_actualizar_aula, (
                data["grado_t"], data["grado_num"], data["grupo_equivalente"], 
                data["jornada"], anio_actual, data["codigo_insti"], data["id_usuario"], grupo
            ))
            conn.commit()
            return jsonify({"message": f"Aula con Grupo = {grupo} actualizada exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

def verificar_solapamiento_horario(id_usuario, codigo_horario, cursor):
    """
    Verifica si el horario ya está asignado al tutor.
    """
    try:
        query_verificar = """
        SELECT COUNT(*)
        FROM "TempSchema"."UsuarioTieneHorario"
        WHERE "IDUsuario" = %s AND "CodigoH" = %s;
        """
        cursor.execute(query_verificar, (id_usuario, codigo_horario))
        solapamiento = cursor.fetchone()[0]
        return solapamiento > 0
    except Exception as e:
        print(f"Error al verificar solapamiento: {e}")
        return True

@app.route('/horarios/asignar', methods=['POST'])
def asignar_horario_tutor():
    data = request.get_json()

    # Validar los campos requeridos
    required_fields = ["id_usuario", "codigo_horario"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": f"Faltan campos requeridos: {', '.join(required_fields)}"}), 400

    id_usuario = data["id_usuario"]
    codigo_horario = data["codigo_horario"]

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Verificar si el horario ya está asignado al tutor
            if verificar_solapamiento_horario(id_usuario, codigo_horario, cursor):
                return jsonify({"message": "El horario ya está asignado al tutor."}), 400

            # Relacionar el horario con el usuario
            query_asociar_horario_usuario = """
            INSERT INTO "TempSchema"."UsuarioTieneHorario" ("CodigoH", "IDUsuario")
            VALUES (%s, %s);
            """
            cursor.execute(query_asociar_horario_usuario, (codigo_horario, id_usuario))
            conn.commit()

            return jsonify({"message": f"Horario asignado exitosamente al tutor con IDUsuario {id_usuario}."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/insertar-horario', methods=['POST'])
def insertar_horario_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Validar si el horario ya existe
            query_validar = """
            SELECT COUNT(*)
            FROM "TempSchema"."Horario"
            WHERE "HoraInicio" = %s AND "HoraFin" = %s AND "DiaTexto" = %s;
            """
            cursor.execute(query_validar, (data['hora_inicio'], data['hora_fin'], data['dia_texto']))
            existe = cursor.fetchone()[0]

            if existe > 0:
                return jsonify({"error": "El horario ya existe para el mismo rango de horas en ese día"}), 400

            # Insertar horario
            query_insertar = """
            INSERT INTO "TempSchema"."Horario" ("FechaInicio", "FechaFin", "HoraInicio", "HoraFin", "DiaInicial", "DiaTexto")
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query_insertar, (
                data['fecha_inicio'], data['fecha_fin'], data['hora_inicio'], 
                data['hora_fin'], data['dia_inicial'], data['dia_texto']
            ))
            conn.commit()
        return jsonify({"message": "Horario insertado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/eliminar-horario', methods=['DELETE'])
def eliminar_horario_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            query_eliminar = """
            DELETE FROM "TempSchema"."Horario"
            WHERE "CodigoH" = %s;
            """
            cursor.execute(query_eliminar, (data['codigo_h'],))
            conn.commit()
        return jsonify({"message": "Horario eliminado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/actualizar-horario', methods=['PUT'])
def actualizar_horario_api():
    data = request.get_json()
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Validar si el nuevo horario ya existe
            query_validar = """
            SELECT COUNT(*)
            FROM "TempSchema"."Horario"
            WHERE "HoraInicio" = %s AND "HoraFin" = %s AND "DiaTexto" = %s AND "CodigoH" != %s;
            """
            cursor.execute(query_validar, (
                data['hora_inicio'], data['hora_fin'], data['dia_texto'], data['codigo_h']
            ))
            existe = cursor.fetchone()[0]

            if existe > 0:
                return jsonify({"error": "El horario ya existe para el mismo rango de horas en ese día"}), 400

            # Actualizar horario
            query_actualizar = """
            UPDATE "TempSchema"."Horario"
            SET "FechaInicio" = %s, "FechaFin" = %s, "HoraInicio" = %s, "HoraFin" = %s, 
                "DiaInicial" = %s, "DiaTexto" = %s
            WHERE "CodigoH" = %s;
            """
            cursor.execute(query_actualizar, (
                data['fecha_inicio'], data['fecha_fin'], data['hora_inicio'], 
                data['hora_fin'], data['dia_inicial'], data['dia_texto'], data['codigo_h']
            ))
            conn.commit()
        return jsonify({"message": "Horario actualizado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/calificar-estudiante', methods=['POST'])
def calificar_estudiante_api():
    data = request.get_json()

    try:
        id_estudiante = data['id_estudiante']
        nota = data['nota']
        bloque_lectivo = data['bloque_lectivo']

        # Validar que la nota sea un número
        if not isinstance(nota, (int, float)):
            return jsonify({"error": "La nota debe ser un número válido"}), 400

        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Validar que el estudiante exista
            query_verificar_estudiante = """
            SELECT COUNT(*)
            FROM "TempSchema"."Estudiante"
            WHERE "IDEstudiante" = %s;
            """
            cursor.execute(query_verificar_estudiante, (id_estudiante,))
            estudiante_existe = cursor.fetchone()[0]

            if estudiante_existe == 0:
                return jsonify({"error": f"El estudiante con ID {id_estudiante} no existe"}), 404

            # Obtener el año actual
            anio_actual = datetime.now().year

            # Insertar la calificación en la tabla Examen
            query_insertar_calificacion = """
            INSERT INTO "TempSchema"."Examen" ("Nota", "BloqueLectivo", "Año", "IDEstudiante")
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query_insertar_calificacion, (nota, bloque_lectivo, anio_actual, id_estudiante))
            conn.commit()

        return jsonify({"message": f"Calificación registrada exitosamente para el estudiante con ID {id_estudiante}"}), 201

    except KeyError:
        return jsonify({"error": "Faltan datos requeridos: id_estudiante, nota, bloque_lectivo"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
        
@app.route('/generar_horario_tutor', methods=['GET'])
def generar_horario_tutor():
    id_usuario = request.args.get('id_usuario')

    if not id_usuario:
        return jsonify({"error": "El parámetro 'id_usuario' es requerido"}), 400

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener el horario del tutor
            query_reporte_horario_tutor = """
            SELECT h."DiaTexto", h."HoraInicio", h."HoraFin", a."Grupo", i."NombreInsti"
            FROM "TempSchema"."Horario" h
            INNER JOIN "TempSchema"."HorarioTieneAula" hta ON h."CodigoH" = hta."CodigoH"
            INNER JOIN "TempSchema"."Aula" a ON hta."Grupo" = a."Grupo"
            INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
            WHERE a."IDUsuario" = %s
            ORDER BY h."DiaTexto", h."HoraInicio";
            """
            cursor.execute(query_reporte_horario_tutor, (id_usuario,))
            horarios = cursor.fetchall()

            if not horarios:
                return jsonify({"message": f"No se encontraron horarios asociados al tutor con IDUsuario {id_usuario}"}), 404

            # Formatear los datos en JSON
            reporte = []
            for horario in horarios:
                reporte.append({
                    "dia": horario[0],
                    "hora_inicio": horario[1].strftime('%H:%M'),
                    "hora_fin": horario[2].strftime('%H:%M'),
                    "grupo": horario[3],
                    "institucion": horario[4]
                })

            return jsonify({"id_usuario": id_usuario, "reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/generar_reporte_aulas', methods=['GET'])
def generar_reporte_aulas():
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener los datos de las aulas
            query_reporte_aulas = """
            SELECT a."Grupo", a."GradoT", a."GradoNum", a."GrupoEquivalente", 
                   a."Jornada", a."Año", i."NombreInsti",
                   p."PrimerNombre", p."PrimerApellido"
            FROM "TempSchema"."Aula" a
            INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
            INNER JOIN "TempSchema"."Usuario" u ON a."IDUsuario" = u."IDUsuario"
            INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
            ORDER BY a."Año" DESC, a."Grupo";
            """
            cursor.execute(query_reporte_aulas)
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
        conn.close()

@app.route('/generar_reporte_aulas_tutor', methods=['GET'])
def generar_reporte_aulas_tutor():
    id_usuario = request.args.get('id_usuario')

    if not id_usuario:
        return jsonify({"error": "El parámetro 'id_usuario' es requerido"}), 400

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener las aulas asociadas a un tutor específico
            query_reporte_aulas_tutor = """
            SELECT a."Grupo", a."GradoT", a."GradoNum", a."Jornada", i."NombreInsti"
            FROM "TempSchema"."Aula" a
            INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
            WHERE a."IDUsuario" = %s
            ORDER BY a."Grupo";
            """
            cursor.execute(query_reporte_aulas_tutor, (id_usuario,))
            aulas_tutor = cursor.fetchall()

            if not aulas_tutor:
                return jsonify({"message": f"No se encontraron aulas asociadas al tutor con IDUsuario {id_usuario}"}), 404

            # Formatear los datos en JSON
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
        conn.close()

@app.route('/reporte-estudiantes-aula', methods=['GET'])
def reporte_estudiantes_aula_api():
    grupo = request.args.get('grupo')

    if not grupo:
        return jsonify({"error": "El parámetro 'grupo' es requerido"}), 400

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener los estudiantes de un aula específica
            query_reporte_estudiantes_aula = """
            SELECT e."IDEstudiante", e."PrimerNombre", e."PrimerApellido", 
                   a."Grupo", i."NombreInsti"
            FROM "TempSchema"."Estudiante" e
            INNER JOIN "TempSchema"."Aula" a ON e."Grupo" = a."Grupo"
            INNER JOIN "TempSchema"."Institucion" i ON a."CodigoInsti" = i."CodigoInsti"
            WHERE a."Grupo" = %s
            ORDER BY e."PrimerApellido", e."PrimerNombre";
            """
            cursor.execute(query_reporte_estudiantes_aula, (grupo,))
            estudiantes = cursor.fetchall()

            if not estudiantes:
                return jsonify({"message": f"No se encontraron estudiantes registrados en el aula con Grupo {grupo}"}), 404

            # Formatear el resultado en un JSON
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
        conn.close()

@app.route('/reporte-instituciones', methods=['GET'])
def reporte_instituciones_api():
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
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
                return jsonify({"message": "No se encontraron instituciones registradas"}), 404

            # Formatear el resultado en un JSON
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
        conn.close()
        
@app.route('/reporte-personas', methods=['GET'])
def reporte_personas_api():
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener los datos de las personas
            query_reporte_personas = """
            SELECT p."TipoID", p."Identificacion", p."IDUsuario", 
                   p."PrimerNombre", p."SegundoNombre", 
                   p."PrimerApellido", p."SegundoApellido", 
                   p."Correo", p."Telefono"
            FROM "TempSchema"."Persona" p
            ORDER BY p."PrimerApellido", p."SegundoApellido", p."PrimerNombre";
            """
            cursor.execute(query_reporte_personas)
            personas = cursor.fetchall()

            if not personas:
                return jsonify({"message": "No se encontraron personas registradas"}), 404

            # Formatear el resultado en un JSON
            reporte = []
            for persona in personas:
                reporte.append({
                    "tipo_id": persona[0],
                    "identificacion": persona[1],
                    "id_usuario": persona[2] or "N/A",
                    "nombre_completo": f"{persona[3]} {persona[4] or ''} {persona[5]} {persona[6] or ''}".strip(),
                    "correo": persona[7] or "N/A",
                    "telefono": persona[8] or "N/A"
                })

            return jsonify({"reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/reporte-tutores', methods=['GET'])
def reporte_tutores_api():
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener los datos de los tutores
            query_reporte_tutores = """
            SELECT p."IDUsuario", p."PrimerNombre", p."PrimerApellido", 
                   p."Correo", p."Telefono"
            FROM "TempSchema"."Usuario" u
            INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
            WHERE u."Rol" = 'Tutor';
            """
            cursor.execute(query_reporte_tutores)
            tutores = cursor.fetchall()

            if not tutores:
                return jsonify({"message": "No se encontraron tutores registrados"}), 404

            # Formatear el resultado en un JSON
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
        conn.close()

@app.route('/reporte-usuarios', methods=['GET'])
def reporte_usuarios_api():
    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener los datos de los usuarios
            query_reporte_usuarios = """
            SELECT u."IDUsuario", p."PrimerNombre", p."SegundoNombre", 
                   p."PrimerApellido", p."SegundoApellido", u."Rol", p."Correo", p."Telefono"
            FROM "TempSchema"."Usuario" u
            INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
            ORDER BY p."PrimerApellido", p."SegundoApellido", p."PrimerNombre";
            """
            cursor.execute(query_reporte_usuarios)
            usuarios = cursor.fetchall()

            if not usuarios:
                return jsonify({"message": "No se encontraron usuarios registrados"}), 404

            # Formatear el resultado en un JSON
            reporte = []
            for usuario in usuarios:
                reporte.append({
                    "id_usuario": usuario[0],
                    "nombre_completo": f"{usuario[1]} {usuario[2] or ''} {usuario[3]} {usuario[4] or ''}".strip(),
                    "rol": usuario[5],
                    "correo": usuario[6] or "N/A",
                    "telefono": usuario[7] or "N/A"
                })

            return jsonify({"reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/registrar-asistencia', methods=['POST'])
def registrar_asistencia():
    data = request.get_json()

    # Validar los parámetros necesarios
    if not all(key in data for key in ["grupo", "codigo_horario", "fecha", "id_tutor"]):
        return jsonify({"error": "Faltan datos requeridos: grupo, codigo_horario, fecha, id_tutor"}), 400

    grupo = data["grupo"]
    codigo_horario = data["codigo_horario"]
    fecha = data["fecha"]
    id_tutor = data["id_tutor"]

    try:
        # Validar el formato de la fecha
        try:
            fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Formato de fecha inválido. Use YYYY-MM-DD"}), 400

        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Registrar asistencia del tutor
            query_verificar_rol_tutor = """
            SELECT "Rol"
            FROM "TempSchema"."Usuario"
            WHERE "IDUsuario" = %s;
            """
            cursor.execute(query_verificar_rol_tutor, (id_tutor,))
            rol_tutor = cursor.fetchone()

            if rol_tutor and rol_tutor[0] == "Tutor":
                query_verificar_asistencia_tutor = """
                SELECT COUNT(*)
                FROM "TempSchema"."AsistenciaUsuario"
                WHERE "CodigoH" = %s AND "IDUsuario" = %s AND "Fecha" = %s;
                """
                cursor.execute(query_verificar_asistencia_tutor, (codigo_horario, id_tutor, fecha_obj))
                existe_asistencia_tutor = cursor.fetchone()[0]

                if existe_asistencia_tutor == 0:
                    query_insertar_asistencia_tutor = """
                    INSERT INTO "TempSchema"."AsistenciaUsuario" ("CodigoH", "IDUsuario", "Fecha", "Asiste")
                    VALUES (%s, %s, %s, %s);
                    """
                    cursor.execute(query_insertar_asistencia_tutor, (codigo_horario, id_tutor, fecha_obj, True))
                else:
                    return jsonify({"message": "El tutor ya tiene registrada su asistencia"}), 400

            # Obtener estudiantes asociados al grupo
            query_estudiantes = """
            SELECT DISTINCT eth."IDEstudiante"
            FROM "TempSchema"."EstudianteTieneHorario" eth
            INNER JOIN "TempSchema"."Aula" a ON eth."Grupo" = a."Grupo"
            WHERE a."Grupo" = %s;
            """
            cursor.execute(query_estudiantes, (grupo,))
            estudiantes = cursor.fetchall()

            if not estudiantes:
                return jsonify({"message": f"No se encontraron estudiantes para el grupo {grupo}"}), 404

            # Registrar asistencia de los estudiantes
            for estudiante in estudiantes:
                id_estudiante = estudiante[0]

                query_verificar_asistencia = """
                SELECT COUNT(*)
                FROM "TempSchema"."AsistenciaEstudiante"
                WHERE "CodigoH" = %s AND "IDEstudiante" = %s AND "Fecha" = %s;
                """
                cursor.execute(query_verificar_asistencia, (codigo_horario, id_estudiante, fecha_obj))
                existe_asistencia = cursor.fetchone()[0]

                if existe_asistencia == 0:
                    query_insertar_asistencia = """
                    INSERT INTO "TempSchema"."AsistenciaEstudiante" ("CodigoH", "IDEstudiante", "Fecha", "Asiste")
                    VALUES (%s, %s, %s, %s);
                    """
                    cursor.execute(query_insertar_asistencia, (codigo_horario, id_estudiante, fecha_obj, True))

            conn.commit()
            return jsonify({"message": "Asistencia registrada exitosamente"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/asistencias-aula', methods=['GET'])
def asistencias_aula_api():
    grupo = request.args.get('grupo')

    if not grupo:
        return jsonify({"error": "El parámetro 'grupo' es requerido"}), 400

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener las asistencias de los estudiantes de un aula
            query_asistencias = """
            SELECT a."Grupo", e."IDEstudiante", e."PrimerNombre", e."PrimerApellido",
                   h."DiaTexto", h."HoraInicio", h."HoraFin", ae."Fecha", ae."Asiste"
            FROM "TempSchema"."AsistenciaEstudiante" ae
            INNER JOIN "TempSchema"."Estudiante" e ON ae."IDEstudiante" = e."IDEstudiante"
            INNER JOIN "TempSchema"."EstudianteTieneHorario" eth ON e."IDEstudiante" = eth."IDEstudiante"
            INNER JOIN "TempSchema"."Horario" h ON ae."CodigoH" = h."CodigoH"
            INNER JOIN "TempSchema"."HorarioTieneAula" ha ON h."CodigoH" = ha."CodigoH"
            INNER JOIN "TempSchema"."Aula" a ON ha."Grupo" = a."Grupo"
            WHERE a."Grupo" = %s
            ORDER BY ae."Fecha", h."DiaTexto", h."HoraInicio", e."PrimerApellido", e."PrimerNombre";
            """
            cursor.execute(query_asistencias, (grupo,))
            asistencias = cursor.fetchall()

            if not asistencias:
                return jsonify({"message": f"No se encontraron asistencias registradas para el aula del grupo {grupo}"}), 404

            # Formatear el resultado en un JSON
            reporte = []
            for asistencia in asistencias:
                reporte.append({
                    "fecha": asistencia[7].strftime('%Y-%m-%d'),
                    "dia": asistencia[4],
                    "hora_inicio": asistencia[5].strftime('%H:%M'),
                    "hora_fin": asistencia[6].strftime('%H:%M'),
                    "estudiante": f"{asistencia[2]} {asistencia[3]}",
                    "asistio": "Sí" if asistencia[8] else "No"
                })

            return jsonify({"grupo": grupo, "reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/asistencias-usuarios', methods=['GET'])
def asistencias_usuarios_api():
    grupo = request.args.get('grupo')

    if not grupo:
        return jsonify({"error": "El parámetro 'grupo' es requerido"}), 400

    try:
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener las asistencias de los usuarios en un aula
            query_asistencias = """
            SELECT a."Grupo", p."PrimerNombre", p."PrimerApellido", u."Rol",
                   h."DiaTexto", h."HoraInicio", h."HoraFin", au."Fecha", au."Asiste"
            FROM "TempSchema"."AsistenciaUsuario" au
            INNER JOIN "TempSchema"."Usuario" u ON au."IDUsuario" = u."IDUsuario"
            INNER JOIN "TempSchema"."Persona" p ON u."IDUsuario" = p."IDUsuario"
            INNER JOIN "TempSchema"."Horario" h ON au."CodigoH" = h."CodigoH"
            INNER JOIN "TempSchema"."HorarioTieneAula" ha ON h."CodigoH" = ha."CodigoH"
            INNER JOIN "TempSchema"."Aula" a ON ha."Grupo" = a."Grupo"
            WHERE a."Grupo" = %s
            ORDER BY au."Fecha", h."DiaTexto", h."HoraInicio", p."PrimerApellido", p."PrimerNombre";
            """
            cursor.execute(query_asistencias, (grupo,))
            asistencias = cursor.fetchall()

            if not asistencias:
                return jsonify({"message": f"No se encontraron asistencias registradas para el aula del grupo {grupo}"}), 404

            # Formatear el resultado en un JSON
            reporte = []
            for asistencia in asistencias:
                reporte.append({
                    "fecha": asistencia[7].strftime('%Y-%m-%d'),
                    "dia": asistencia[4],
                    "hora_inicio": asistencia[5].strftime('%H:%M'),
                    "hora_fin": asistencia[6].strftime('%H:%M'),
                    "usuario": f"{asistencia[1]} {asistencia[2]}",
                    "rol": asistencia[3],
                    "asistio": "Sí" if asistencia[8] else "No"
                })

            return jsonify({"grupo": grupo, "reporte": reporte}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/calificaciones-aula', methods=['GET'])
def calificaciones_aula_api():
    grupo = request.args.get('grupo')
    anio = request.args.get('anio')

    if not grupo or not anio:
        return jsonify({"error": "Los parámetros 'grupo' y 'anio' son requeridos"}), 400

    try:
        anio = int(anio)  # Validar que el año sea un número
        conn = obtener_conexion()
        with conn.cursor() as cursor:
            # Consulta para obtener las calificaciones
            query_calificaciones = """
            SELECT a."Grupo", e."IDEstudiante", e."PrimerNombre", e."PrimerApellido",
                   ex."Nota", ex."BloqueLectivo", ex."Año"
            FROM "TempSchema"."Examen" ex
            INNER JOIN "TempSchema"."Estudiante" e ON ex."IDEstudiante" = e."IDEstudiante"
            INNER JOIN "TempSchema"."Aula" a ON e."Grupo" = a."Grupo"
            WHERE a."Grupo" = %s AND ex."Año" = %s
            ORDER BY ex."BloqueLectivo", e."PrimerApellido", e."PrimerNombre";
            """
            cursor.execute(query_calificaciones, (grupo, anio))
            calificaciones = cursor.fetchall()

            if not calificaciones:
                return jsonify({"message": f"No se encontraron calificaciones registradas para el grupo {grupo} en el año {anio}"}), 404

            # Formatear el resultado en un JSON
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
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
