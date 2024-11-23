import React, { useEffect, useState } from 'react';
import './InstitutionSelection.css';

const InstitutionSelection = ({ selectInstitution }) => {
  const [institutions, setInstitutions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchInstitutions = async () => {
      setLoading(true);
      setError('');
      try {
        const response = await fetch('/reporte-instituciones');
        if (!response.ok) {
          throw new Error('Error al obtener las instituciones.');
        }
        const data = await response.json();
        if (data.reporte) {
          const formattedInstitutions = data.reporte.map((institution) => ({
            id: institution.codigo,
            name: institution.nombre,
            rector: institution.rector,
            localidad: institution.localidad,
            barrio: institution.barrio,
            numero: institution.numero,
            direccion: institution.direccion,
            image: '/placeholder-image.jpg', // Cambiar a una ruta de imagen real si está disponible
          }));
          setInstitutions(formattedInstitutions);
        } else {
          setError('No se encontraron instituciones.');
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchInstitutions();
  }, []);

  return (
    <div className="institution-selection-container">
      <h3 className="institution-selection-title">Seleccione una Institución Educativa</h3>
      {loading && <p>Cargando instituciones...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <div className="institution-cards">
          {institutions.map((institution) => (
            <button
              key={institution.id}
              className="institution-card"
              onClick={() => selectInstitution(institution)}
            >
              <img
                src={institution.image}
                alt={institution.name}
              />
              <p>{institution.name}</p>
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export default InstitutionSelection;
