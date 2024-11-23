import React, { useState, useEffect } from 'react';
import './ScheduleDetails.css';

const ScheduleDetails = ({ goBack }) => {
  const [schedules, setSchedules] = useState([]);
  const [newSchedule, setNewSchedule] = useState({
    dia_texto: '', // "day" en tu backend
    hora_inicio: '', // "startTime"
    hora_fin: '', // "endTime"
  });

  // Fetch para obtener horarios al cargar
  useEffect(() => {
    fetch('/api/horarios') // Cambia esta ruta si es diferente en tu app.py
      .then((response) => response.json())
      .then((data) => {
        if (data.reporte) {
          setSchedules(data.reporte);
        } else {
          alert('No se encontraron horarios.');
        }
      })
      .catch((error) => console.error('Error al obtener horarios:', error));
  }, []);

  // Manejar cambios en el formulario
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewSchedule((prev) => ({ ...prev, [name]: value }));
  };

  // Agregar horario
  const handleAddSchedule = () => {
    if (!newSchedule.dia_texto || !newSchedule.hora_inicio || !newSchedule.hora_fin) {
      alert('Por favor, complete todos los campos antes de agregar un horario.');
      return;
    }

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
          setNewSchedule({ dia_texto: '', hora_inicio: '', hora_fin: '' });
        } else if (data.error) {
          alert(`Error: ${data.error}`);
        }
      })
      .catch((error) => console.error('Error al agregar horario:', error));
  };

  return (
    <div className="schedule-details-container">
      <h3>Gestión de Horarios</h3>
      <table className="schedule-table">
        <thead>
          <tr>
            <th>Día</th>
            <th>Hora de Inicio</th>
            <th>Hora de Fin</th>
          </tr>
        </thead>
        <tbody>
          {schedules.map((schedule, index) => (
            <tr key={index}>
              <td>{schedule.dia_texto}</td>
              <td>{schedule.hora_inicio}</td>
              <td>{schedule.hora_fin}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="add-schedule-form">
        <h4>Agregar Nuevo Horario</h4>
        <select
          name="dia_texto"
          value={newSchedule.dia_texto}
          onChange={handleInputChange}
        >
          <option value="">Seleccionar Día</option>
          <option value="Lunes">Lunes</option>
          <option value="Martes">Martes</option>
          <option value="Miércoles">Miércoles</option>
          <option value="Jueves">Jueves</option>
          <option value="Viernes">Viernes</option>
        </select>
        <input
          type="time"
          name="hora_inicio"
          value={newSchedule.hora_inicio}
          onChange={handleInputChange}
        />
        <input
          type="time"
          name="hora_fin"
          value={newSchedule.hora_fin}
          onChange={handleInputChange}
        />
        <button onClick={handleAddSchedule}>Agregar Horario</button>
      </div>

      <button onClick={goBack}>Volver</button>
    </div>
  );
};

export default ScheduleDetails;
