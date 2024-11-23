import React, { useState, useEffect } from 'react';
import StudentDetails from './StudentDetails';
import './ExamStudentList.css';

const ExamStudentList = ({ exam, year }) => {
  const [students, setStudents] = useState([]);
  const [grades, setGrades] = useState({});
  const [selectedStudent, setSelectedStudent] = useState(null);

  // Obtener estudiantes de la API
  useEffect(() => {
    const fetchStudents = async () => {
      try {
        const response = await fetch(`/reporte-estudiantes-aula?grupo=${exam.group}`);
        if (!response.ok) {
          throw new Error('Error fetching students');
        }
        const data = await response.json();
        const fetchedStudents = data.reporte.map(student => ({
          id: student.id_estudiante,
          identificacion: student.id_estudiante,
          nombre1: student.nombre_completo.split(' ')[0],
          nombre2: student.nombre_completo.split(' ')[1] || '',
          apellido1: student.nombre_completo.split(' ')[2] || '',
          apellido2: student.nombre_completo.split(' ')[3] || '',
          grupo: student.grupo,
        }));
        setStudents(fetchedStudents);

        const initialGrades = {};
        fetchedStudents.forEach((student) => {
          initialGrades[student.id] = '';
        });
        setGrades(initialGrades);
      } catch (error) {
        console.error(error);
      }
    };

    fetchStudents();
  }, [exam.group]);

  // Gestionar cambios de calificación
  const handleGradeChange = (studentId, value) => {
    setGrades((prevGrades) => ({
      ...prevGrades,
      [studentId]: value,
    }));
  };

  // Enviar calificaciones a la API
  const handleSubmit = async () => {
    try {
      const gradesToSubmit = Object.entries(grades).map(([id, nota]) => ({
        id_estudiante: id,
        nota: parseFloat(nota),
        bloque_lectivo: exam.bloque,
      }));

      for (const grade of gradesToSubmit) {
        const response = await fetch('/calificar-estudiante', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(grade),
        });

        if (!response.ok) {
          throw new Error(`Error submitting grade for student ID ${grade.id_estudiante}`);
        }
      }

      alert('Notas registradas correctamente');
    } catch (error) {
      console.error(error);
      alert('Error registrando las notas');
    }
  };

  if (selectedStudent) {
    return (
      <StudentDetails
        student={selectedStudent}
        goBack={() => setSelectedStudent(null)}
      />
    );
  }

  return (
    <div className="exam-student-list-container">
      <h4 className="exam-student-list-title">
        Lista de Estudiantes para {exam.name}
      </h4>
      <table className="exam-student-table">
        <thead>
          <tr>
            <th>Nombre del Estudiante</th>
            <th>Identificación</th>
            <th>Nota</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <tr key={student.id}>
              <td>
                <button
                  className="student-details-button"
                  onClick={() => setSelectedStudent(student)}
                >
                  {`${student.nombre1} ${student.nombre2} ${student.apellido1} ${student.apellido2}`}
                </button>
              </td>
              <td>{student.identificacion}</td>
              <td>
                <input
                  type="number"
                  min="0"
                  max="100"
                  value={grades[student.id]}
                  onChange={(e) =>
                    handleGradeChange(student.id, e.target.value)
                  }
                  className="grade-input"
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <button className="save-grades-button" onClick={handleSubmit}>
        Guardar Notas
      </button>
    </div>
  );
};

export default ExamStudentList;
