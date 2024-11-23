import React, { useState, useEffect } from 'react';
import CourseSelection from './CourseSelection';
import CourseDetails from './CourseDetails';
import ExamsDashboard from './ExamsDashboard';
import './InstitutionDetails.css';

const InstitutionDetails = ({ institution, goBack }) => {
  const [selectedYear, setSelectedYear] = useState('');
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [activeTab, setActiveTab] = useState(null); // 'asistencia' o 'examenes'
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const years = ['2021', '2022', '2023', '2024'];

  // Fetch courses for the selected year
  useEffect(() => {
    if (selectedYear) {
      const fetchCourses = async () => {
        setLoading(true);
        setError('');
        try {
          const response = await fetch(`/generar_reporte_aulas?anio=${selectedYear}&codigoInsti=${institution.id}`);
          if (!response.ok) {
            throw new Error('Error fetching courses');
          }
          const data = await response.json();
          setCourses(data.reporte || []);
        } catch (err) {
          console.error(err);
          setError('Error al cargar los cursos.');
        } finally {
          setLoading(false);
        }
      };

      fetchCourses();
    }
  }, [selectedYear, institution.id]);

  const selectCourse = (course) => {
    setSelectedCourse(course);
  };

  const goBackToInstitution = () => {
    setSelectedCourse(null);
    setActiveTab(null);
    setSelectedYear('');
    setCourses([]);
  };

  const handleTabSelection = (tab) => {
    setActiveTab(tab);
    setSelectedCourse(null);
    setSelectedYear('');
    setCourses([]);
  };

  return (
    <div className="institution-details-container">
      <h3 className="institution-details-title">Información de la Institución</h3>
      <div className="institution-info">
        <p><strong>Código ID:</strong> {institution.id}</p>
        <p><strong>Nombre:</strong> {institution.name}</p>
        <p><strong>Rector:</strong> {institution.rector}</p>
        <p><strong>Localidad:</strong> {institution.localidad}</p>
        <p><strong>Barrio:</strong> {institution.barrio}</p>
        <p><strong>Número:</strong> {institution.numero}</p>
        <p><strong>Dirección:</strong> {institution.direccion}</p>
      </div>
      <button className="back-button" onClick={goBack}>
        Volver a Instituciones
      </button>

      <h3 className="section-title">Seleccione una Acción</h3>
      <div className="action-buttons">
        <button
          className="attendance-button"
          onClick={() => handleTabSelection('asistencia')}
        >
          Asistencia
        </button>
        <button
          className="exams-button"
          onClick={() => handleTabSelection('examenes')}
        >
          Exámenes
        </button>
      </div>

      {activeTab === 'asistencia' && (
        <>
          <h3 className="section-title">Seleccione el Año Lectivo</h3>
          <div className="year-selection">
            <select
              value={selectedYear}
              onChange={(e) => setSelectedYear(e.target.value)}
            >
              <option value="">-- Seleccione el Año --</option>
              {years.map((year) => (
                <option key={year} value={year}>{year}</option>
              ))}
            </select>
          </div>

          {loading && <p>Cargando cursos...</p>}
          {error && <p className="error-message">{error}</p>}

          {selectedYear && !selectedCourse && !loading && courses.length > 0 && (
            <div className="course-selection">
              <h3>Cursos Disponibles para el Año {selectedYear}</h3>
              <CourseSelection courses={courses} selectCourse={selectCourse} />
            </div>
          )}

          {selectedYear && !loading && courses.length === 0 && (
            <p>No hay cursos disponibles para este año.</p>
          )}

          {selectedCourse && (
            <CourseDetails
              course={selectedCourse}
              selectedYear={selectedYear}
              goBack={goBackToInstitution}
            />
          )}
        </>
      )}

      {activeTab === 'examenes' && (
        <ExamsDashboard
          institution={institution}
          goBack={goBackToInstitution}
        />
      )}
    </div>
  );
};

export default InstitutionDetails;
