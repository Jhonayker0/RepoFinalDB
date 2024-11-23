import React, { useState, useEffect } from 'react';
import InstitutionSelection from './InstitutionSelection';
import InstitutionDetails from './InstitutionDetails';
import './TutorDashboard.css';

const TutorDashboard = ({ setRole }) => {
  const [selectedInstitution, setSelectedInstitution] = useState(null);
  const [institutions, setInstitutions] = useState([]);

  // Obtener instituciones desde la API
  useEffect(() => {
    fetch('/reporte-instituciones')
      .then((response) => response.json())
      .then((data) => {
        if (data.reporte) {
          // Formatear los datos si es necesario
          const formattedInstitutions = data.reporte.map((institution) => ({
            id: institution.codigo,
            name: institution.nombre,
            rector: institution.rector,
            localidad: institution.localidad,
            barrio: institution.barrio,
            numero: institution.numero,
            direccion: institution.direccion,
            image: 'https://via.placeholder.com/100', // Imagen placeholder
          }));
          setInstitutions(formattedInstitutions);
        } else {
          alert(data.message || 'Error al obtener instituciones.');
        }
      })
      .catch((error) => console.error('Error al cargar instituciones:', error));
  }, []);

  const selectInstitution = (institution) => {
    setSelectedInstitution(institution);
  };

  const goBack = () => {
    setSelectedInstitution(null);
  };

  return (
    <div className="tutor-dashboard-container">
      {!selectedInstitution ? (
        <>
          <h2>Bienvenido, Tutor</h2>
          {institutions.length > 0 ? (
            <InstitutionSelection
              institutions={institutions}
              selectInstitution={selectInstitution}
              className="institution-selection-container"
            />
          ) : (
            <p>Cargando instituciones...</p>
          )}
          <button onClick={() => setRole(null)}>Cerrar Sesión</button>
        </>
      ) : (
        <InstitutionDetails
          institution={selectedInstitution}
          goBack={goBack}
          className="institution-details-container"
        />
      )}
    </div>
  );
};

export default TutorDashboard;
