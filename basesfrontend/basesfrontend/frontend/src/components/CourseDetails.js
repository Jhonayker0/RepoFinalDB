import React, { useState, useEffect, useCallback } from 'react';
import SectionDetails from './SectionDetails';
import './CourseDetails.css';

const CourseDetails = ({ course, selectedYear, goBack }) => {
  const [sections, setSections] = useState([]); // Secciones obtenidas desde la API
  const [selectedSection, setSelectedSection] = useState(null);
  const [error, setError] = useState(null);

  // Función para obtener las secciones de un curso desde la API
  const fetchSections = useCallback(async () => {
    try {
      const response = await fetch(`http://localhost:5000/secciones-curso?curso=${course.grade}&anio=${selectedYear}`);
      if (!response.ok) {
        throw new Error('Error al obtener las secciones del curso.');
      }
      const data = await response.json();
      setSections(data.secciones || []);
    } catch (err) {
      console.error(err);
      setError('No se pudieron cargar las secciones.');
    }
  }, [course.grade, selectedYear]);

  // Ejecutar fetchSections al montar o cambiar curso o año seleccionado
  useEffect(() => {
    fetchSections();
  }, [fetchSections]);

  const selectSection = (section) => {
    setSelectedSection(section);
  };

  const goBackToCourse = () => {
    setSelectedSection(null);
  };

  return (
    <div className="course-details-container">
      {error && <p className="error-message">{error}</p>}

      {!selectedSection ? (
        <>
          <h3>Curso: {course.grade}</h3>
          <p><strong>Año Lectivo:</strong> {selectedYear}</p>
          <p><strong>Jornada:</strong> {course.jornada}</p>
          <h4>Seleccione la Sección:</h4>

          {sections.length > 0 ? (
            <ul className="sections-list">
              {sections.map((section, index) => (
                <li key={index} className="section-item">
                  <button
                    onClick={() => selectSection(section)}
                    className="section-button"
                  >
                    {course.grade} {section}
                  </button>
                </li>
              ))}
            </ul>
          ) : (
            <p>No hay secciones disponibles para este curso.</p>
          )}

          <button onClick={goBack} className="back-button">
            Volver a Cursos
          </button>
        </>
      ) : (
        <SectionDetails
          course={course}
          section={selectedSection}
          selectedYear={selectedYear}
          goBack={goBackToCourse}
        />
      )}
    </div>
  );
};

export default CourseDetails;
