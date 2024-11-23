import React from 'react';
import './CourseSelection.css';

const CourseSelection = ({ selectCourse }) => {
  // Datos de los cursos de primaria
  const courses = [
    {
      id: 1,
      grade: 'Primero',
      jornada: 'Mañana',
    },
    {
      id: 2,
      grade: 'Segundo',
      jornada: 'Tarde',
    },
    {
      id: 3,
      grade: 'Tercero',
      jornada: 'Mañana',
    },
    {
      id: 4,
      grade: 'Cuarto',
      jornada: 'Tarde',
    },
    {
      id: 5,
      grade: 'Quinto',
      jornada: 'Mañana',
    },
    // Agrega más cursos si es necesario
  ];

  return (
    <div className="course-selection-container">
      {courses.map((course) => (
        <button
          key={course.id}
          onClick={() => selectCourse(course)}
          className="course-button"
        >
          {course.grade}
        </button>
      ))}
    </div>
  );
};

export default CourseSelection;




// @app.route('/cursos', methods=['GET'])
//def obtener_cursos():
//    try:
//        conn = obtener_conexion()
//        with conn.cursor() as cursor:
//            query = """
//            SELECT "IDCurso", "Grado", "Jornada"
//            FROM "TempSchema"."Curso";
//            """
//            cursor.execute(query)
//            cursos = cursor.fetchall()
//
//        # Formatear los datos en JSON
//        cursos_formateados = [
//            {"id": curso[0], "grade": curso[1], "jornada": curso[2]}
//            for curso in cursos
//        ]
//
//        return jsonify({"cursos": cursos_formateados}), 200
//    except Exception as e:
//        return jsonify({"error": str(e)}), 500

