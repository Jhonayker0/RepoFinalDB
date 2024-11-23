import React, { useState } from 'react';
import './Login.css';

const Login = ({ setRole }) => {
  const [userId, setUserId] = useState('');
  const [cedula, setCedula] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Realizar la solicitud a la API
      const response = await fetch('http://localhost:5000/obtener-rol', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          identificacion: userId,
          password: cedula,
        }),
      });

      if (response.ok) {
        const data = await response.json();

        if (data.roles && data.roles.length > 0) {
          setRole(data.roles[0]); // Suponiendo que el rol es el primero en la lista
        } else {
          alert('No se encontró un rol para las credenciales proporcionadas.');
        }
      } else {
        const error = await response.json();
        alert(error.error || 'Error al iniciar sesión. Por favor, inténtelo de nuevo.');
      }
    } catch (error) {
      alert('Error de conexión con el servidor. Intente más tarde.');
    }
  };

  return (
    <div className="login-container">
      <h2>Inicio de Sesión</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>ID de Usuario:</label>
          <input
            type="text"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Cédula:</label>
          <input
            type="password"
            value={cedula}
            onChange={(e) => setCedula(e.target.value)}
            required
          />
        </div>
        <button type="submit">Ingresar</button>
      </form>
    </div>
  );
};

export default Login;
