"use client";

import { useEffect, useState } from "react";

export default function HorarioTutor() {
  const [horarios, setHorarios] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);
  const [userId, setUserId] = useState<string | null>(null);

  useEffect(() => {
    // Obtener el dato de la sesión al cargar la página
    const storedUserId = sessionStorage.getItem("userId");
    if (storedUserId) {
      setUserId(storedUserId);
    } else {
      setMessage("No se encontró un ID de usuario en la sesión.");
    }
  }, []);

  const fetchHorarioTutor = async () => {
    if (!userId) {
      setMessage("No se encontró un ID de usuario en la sesión.");
      return;
    }

    try {
      const response = await fetch(`http://localhost:5000/generar_horario_tutor?id_usuario=${userId}`);

      if (!response.ok) {
        const errorData = await response.json();
        setMessage(errorData.error || errorData.message || "Error al obtener el horario.");
        return;
      }

      const data = await response.json();
      setHorarios(data.reporte);
      setMessage(null); // Limpia el mensaje de error
    } catch (error: any) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-4xl">
        <h1 className="text-2xl font-bold text-center mb-4">Horario del Tutor</h1>
        <button
          onClick={fetchHorarioTutor}
          className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
        >
          Obtener Horario
        </button>
        {message && (
          <p
            className={`mt-4 text-sm ${
              message.startsWith("Error") ? "text-red-500" : "text-gray-700"
            }`}
          >
            {message}
          </p>
        )}
        {horarios.length > 0 && (
          <div className="mt-6 overflow-auto">
            <h2 className="text-lg font-bold mb-2">Horario del Tutor (ID: {userId}):</h2>
            <table className="min-w-full border-collapse border border-gray-300">
              <thead>
                <tr className="bg-gray-200">
                  <th className="border border-gray-300 px-4 py-2">Día</th>
                  <th className="border border-gray-300 px-4 py-2">Hora Inicio</th>
                  <th className="border border-gray-300 px-4 py-2">Hora Fin</th>
                  <th className="border border-gray-300 px-4 py-2">Grupo</th>
                  <th className="border border-gray-300 px-4 py-2">Institución</th>
                </tr>
              </thead>
              <tbody>
                {horarios.map((horario, index) => (
                  <tr key={index} className="text-center">
                    <td className="border border-gray-300 px-4 py-2">{horario.dia}</td>
                    <td className="border border-gray-300 px-4 py-2">{horario.hora_inicio}</td>
                    <td className="border border-gray-300 px-4 py-2">{horario.hora_fin}</td>
                    <td className="border border-gray-300 px-4 py-2">{horario.grupo}</td>
                    <td className="border border-gray-300 px-4 py-2">{horario.institucion}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
