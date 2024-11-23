import React, { useState, useEffect } from 'react';
import ExamSelection from './ExamSelection';
import ExamStudentList from './ExamStudentList';
import './ExamsDashboard.css';

const ExamsDashboard = ({ institution, goBack }) => {
  const [selectedYear, setSelectedYear] = useState('');
  const [selectedExam, setSelectedExam] = useState(null);
  const [exams, setExams] = useState([]); // Lista de exámenes cargada desde la API
  const [error, setError] = useState(null);

  const years = ['2021', '2022', '2023', '2024'];

  // Función para obtener los exámenes desde la API
  const fetchExams = async (year) => {
    try {
      const response = await fetch(`http://localhost:5000/calificaciones-aula?grupo=1&anio=${year}`); // Cambia 'grupo=1' si necesitas dinámico
      if (!response.ok) {
        throw new Error('Error al obtener los exámenes');
      }
      const data = await response.json();

      if (data.reporte) {
        // Extraer los nombres de los bloques lectivos únicos como "exámenes"
        const uniqueExams = Array.from(
          new Set(data.reporte.map((item) => item.bloque_lectivo))
        ).map((bloque) => ({
          id: bloque, // Usa el bloque como identificador único
          name: `Examen Bloque ${bloque}`,
        }));
        setExams(uniqueExams);
      } else {
        setExams([]);
      }
    } catch (err) {
      console.error(err);
      setError('No se pudieron cargar los exámenes. Intente nuevamente.');
    }
  };

  // Ejecutar fetchExams cuando se seleccione un año
  useEffect(() => {
    if (selectedYear) {
      fetchExams(selectedYear);
    } else {
      setExams([]);
    }
  }, [selectedYear]);

  const handleExamSelection = (exam) => {
    setSelectedExam(exam);
  };

  return (
    <div className="exams-dashboard-container">
      <h3>Exámenes en {institution.name}</h3>
      <button onClick={goBack} className="back-button">
        Volver a Instituciones
      </button>

      <h4>Seleccione el Año Lectivo</h4>
      <select
        value={selectedYear}
        onChange={(e) => {
          setSelectedYear(e.target.value);
          setSelectedExam(null);
          setError(null);
        }}
      >
        <option value="">-- Seleccione el Año --</option>
        {years.map((year) => (
          <option key={year} value={year}>
            {year}
          </option>
        ))}
      </select>

      {error && <p className="error-message">{error}</p>}

      {selectedYear && (
        <div className="exam-selection">
          <h4>Seleccione el Examen</h4>
          <ExamSelection exams={exams} selectExam={handleExamSelection} />
        </div>
      )}

      {selectedExam && (
        <ExamStudentList exam={selectedExam} year={selectedYear} />
      )}
    </div>
  );
};

export default ExamsDashboard;
