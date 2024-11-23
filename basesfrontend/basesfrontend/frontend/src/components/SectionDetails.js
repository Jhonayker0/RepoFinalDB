import React, { useState, useEffect } from 'react';
import StudentDetails from './StudentDetails';
import ScheduleDetails from './ScheduleDetails';
import './SectionDetails.css';

const SectionDetails = ({ course, section, selectedYear, goBack }) => {
  const [minutes, setMinutes] = useState('');
  const [students, setStudents] = useState([]);
  const [attendance, setAttendance] = useState({});
  const [selectedStudent, setSelectedStudent] = useState(null);
  const [showSchedules, setShowSchedules] = useState(false);
  const [schedules, setSchedules] = useState([]);

  // Obtener estudiantes al cargar el componente
  useEffect(() => {
    fetch(`/reporte-estudiantes-aula?grupo=${section}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.reporte) {
          setStudents(data.reporte);
          const initialAttendance = {};
          data.reporte.forEach((student) => {
            initialAttendance[student.id_estudiante] = false; // Inicializa la asistencia en falso
          });
          setAttendance(initialAttendance);
        } else {
          alert(data.message || 'Error al obtener estudiantes.');
        }
      })
      .catch((error) => console.error('Error al obtener estudiantes:', error));
  }, [section]);

  const handleSaveSchedule = (newSchedule) => {
    fetch('/insertar-horario', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newSchedule),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message) {
          alert(data.message);
          setSchedules((prev) => [...prev, newSchedule]);
        } else if (data.error) {
          alert(`Error: ${data.error}`);
        }
      })
      .catch((error) => console.error('Error al agregar horario:', error));
  };

  if (showSchedules) {
    return (
      <ScheduleDetails
        schedules={schedules}
        saveSchedule={handleSaveSchedule}
        goBack={() => setShowSchedules(false)}
      />
    );
  }

  const handleAttendanceChange = (studentId) => {
    setAttendance((prevAttendance) => ({
      ...prevAttendance,
      [studentId]: !prevAttendance[studentId],
    }));
  };

  const handleSubmit = () => {
    const asistenciaData = {
      grupo: section,
      codigo_horario: 1, // Cambiar por el código horario correspondiente
      fecha: new Date().toISOString().split('T')[0], // Fecha actual en formato YYYY-MM-DD
      id_tutor: 1, // Cambiar por el ID del tutor correspondiente
      estudiantes: Object.entries(attendance).map(([id, asiste]) => ({
        id_estudiante: id,
        asiste,
      })),
    };

    fetch('/registrar-asistencia', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(asistenciaData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message) {
          alert(data.message);
        } else if (data.error) {
          alert(`Error: ${data.error}`);
        }
      })
      .catch((error) => console.error('Error al registrar asistencia:', error));
  };

  const goBackToSections = () => {
    setSelectedStudent(null);
  };

  if (selectedStudent) {
    return (
      <StudentDetails student={selectedStudent} goBack={goBackToSections} />
    );
  }

  return (
    <div className="section-details-container">
      <h3>{course.grade} {section} - Año {selectedYear}</h3>
      <button onClick={() => setShowSchedules(true)}>
        Gestionar Horarios
      </button>
      <p><strong>Ingrese el número de minutos de clase impartidos:</strong></p>
      <input
        type="number"
        value={minutes}
        onChange={(e) => setMinutes(e.target.value)}
      />
      <h4>Lista de Estudiantes:</h4>
      <table className="section-details-table">
        <thead>
          <tr>
            <th>Nombre del Estudiante</th>
            <th>Asistencia</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <tr key={student.id_estudiante}>
              <td>
                <button
                  onClick={() => setSelectedStudent(student)}
                >
                  {student.nombre_completo}
                </button>
              </td>
              <td>
                <input
                  type="checkbox"
                  checked={attendance[student.id_estudiante]}
                  onChange={() => handleAttendanceChange(student.id_estudiante)}
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <button
        className="section-details-button"
        onClick={handleSubmit}
      >
        Guardar Datos
      </button>
      <button
        className="section-details-back-button"
        onClick={goBack}
      >
        Volver a Secciones
      </button>
    </div>
  );
};

export default SectionDetails;
