import React, { useState } from 'react';

const GestionarAsistenciaEstudiante = () => {
  const [response, setResponse] = useState(null); // Estado para la respuesta de la API
  const [grupo, setGrupo] = useState(''); // Para identificar el grupo al consultar
  const [codigoHorario, setCodigoHorario] = useState(''); // Código del horario para registrar
  const [fecha, setFecha] = useState(''); // Fecha para registrar la asistencia

  const fetchData = async (endpoint, method = 'GET', body = null) => {
    const url = `http://localhost:5000/${endpoint}`;
    const options = {
      method,
      headers: { 'Content-Type': 'application/json' },
      ...(body && { body: JSON.stringify(body) }),
    };

    try {
      const res = await fetch(url, options);
      if (!res.ok) {
        throw new Error(`Error ${res.status}: ${res.statusText}`);
      }
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error(`Error al interactuar con el endpoint ${endpoint}:`, error);
      setResponse({ error: error.message });
    }
  };

  // Función para registrar asistencia
  const handleRegistrarAsistencia = () => {
    const requestBody = {
      grupo,
      codigo_horario: codigoHorario,
      fecha,
      id_tutor: '1', // Ajustar según el contexto
    };
    fetchData('registrar-asistencia', 'POST', requestBody);
  };

  // Función para ver asistencia de estudiantes
  const handleVerAsistencia = () => {
    fetchData(`asistencias-aula?grupo=${grupo}`);
  };

  return (
    <div>
      <h3>Gestión de Asistencia del Estudiante</h3>

      <div>
        <label>
          Grupo:
          <input
            type="text"
            value={grupo}
            onChange={(e) => setGrupo(e.target.value)}
            placeholder="Ingrese el grupo"
          />
        </label>
      </div>

      <div>
        <label>
          Código de Horario:
          <input
            type="text"
            value={codigoHorario}
            onChange={(e) => setCodigoHorario(e.target.value)}
            placeholder="Ingrese el código de horario"
          />
        </label>
      </div>

      <div>
        <label>
          Fecha:
          <input
            type="date"
            value={fecha}
            onChange={(e) => setFecha(e.target.value)}
          />
        </label>
      </div>

      <button onClick={handleRegistrarAsistencia}>Registrar Asistencia</button>
      <button onClick={handleVerAsistencia}>Ver Asistencia</button>

      {/* Mostrar la respuesta de la API */}
      {response && (
        <div>
          <h4>Respuesta de la API:</h4>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default GestionarAsistenciaEstudiante;
