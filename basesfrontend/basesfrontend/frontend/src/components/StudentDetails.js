import React, { useState, useEffect } from 'react';
import './StudentDetails.css';

const StudentDetails = ({ studentId, goBack }) => {
  const [student, setStudent] = useState(null);
  const [loading, setLoading] = useState(true);

  // Obtener detalles del estudiante desde la API
  useEffect(() => {
    fetch(`/obtener-estudiante?id_estudiante=${studentId}`)
      .then((response) => response.json())
      .then((data) => {
        if (data && data.estudiante) {
          setStudent(data.estudiante);
        } else {
          alert(data.message || 'Error al obtener los detalles del estudiante.');
        }
      })
      .catch((error) => {
        console.error('Error al cargar detalles del estudiante:', error);
        alert('Hubo un error al cargar los detalles del estudiante.');
      })
      .finally(() => setLoading(false));
  }, [studentId]);

  if (loading) {
    return <p>Cargando detalles del estudiante...</p>;
  }

  if (!student) {
    return <p>No se encontraron detalles para este estudiante.</p>;
  }

  return (
    <div className="student-details-container">
      <h3>Detalles del Estudiante</h3>
      <p><strong>Identificación:</strong> {student.identificacion}</p>
      <p><strong>Tipo ID:</strong> {student.tipoId}</p>
      <p><strong>Nombre Completo:</strong> {`${student.nombre1} ${student.nombre2 || ''} ${student.apellido1} ${student.apellido2 || ''}`}</p>
      <p><strong>Género:</strong> {student.genero}</p>
      <p><strong>Fecha de Nacimiento:</strong> {student.fechaNacimiento}</p>
      <p><strong>Estrato:</strong> {student.estrato}</p>
      <p><strong>Año:</strong> {student.ano}</p>
      <button onClick={goBack}>Volver</button>
    </div>
  );
};

export default StudentDetails;



// posible endpoint para agregar en app.py !!VERIFICAR!!

// @app.route('/obtener-estudiante', methods=['GET'])
// def obtener_estudiante():
//     id_estudiante = request.args.get('id_estudiante')

//     if not id_estudiante:
//         return jsonify({"error": "El parámetro 'id_estudiante' es requerido"}), 400

//     try:
//         conn = obtener_conexion()
//         with conn.cursor() as cursor:
//             query = """
//             SELECT "IDEstudiante", "TipoID", "PrimerNombre", "SegundoNombre", "PrimerApellido", "SegundoApellido",
//                    "Genero", "FechaNacimiento", "Estrato", "Año"
//             FROM "TempSchema"."Estudiantes"
//             WHERE "IDEstudiante" = %s;
//             """
//             cursor.execute(query, (id_estudiante,))
//             estudiante = cursor.fetchone()

//             if not estudiante:
//                 return jsonify({"message": "No se encontraron detalles para este estudiante."}), 404

//             return jsonify({
//                 "estudiante": {
//                     "identificacion": estudiante[0],
//                     "tipoId": estudiante[1],
//                     "nombre1": estudiante[2],
//                     "nombre2": estudiante[3],
//                     "apellido1": estudiante[4],
//                     "apellido2": estudiante[5],
//                     "genero": estudiante[6],
//                     "fechaNacimiento": estudiante[7],
//                     "estrato": estudiante[8],
//                     "ano": estudiante[9]
//                 }
//             }), 200

//     except Exception as e:
//         return jsonify({"error": str(e)}), 500

//     finally:
//         conn.close()
