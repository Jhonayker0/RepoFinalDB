"use client";

import { useState } from "react";

export default function AsistenciasAula() {
  const [grupo, setGrupo] = useState("");
  const [asistencias, setAsistencias] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  const fetchAsistencias = async () => {
    if (!grupo) {
      setMessage("Por favor, ingresa el grupo.");
      return;
    }

    try {
      const response = await fetch(`http://localhost:5000/asistencias-aula?grupo=${grupo}`);

      if (!response.ok) {
        const errorData = await response.json();
        setMessage(errorData.error || errorData.message || "Error al obtener las asistencias.");
        return;
      }

      const data = await response.json();
      setAsistencias(data.reporte);
      setMessage(null); // Limpia el mensaje de error
    } catch (error: any) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-4xl">
        <h1 className="text-2xl font-bold text-center mb-4">Asistencias por Aula</h1>
        <div className="mb-4">
          <label htmlFor="grupo" className="block text-sm font-medium text-gray-700">
            Grupo
          </label>
          <input
            type="text"
            id="grupo"
            value={grupo}
            onChange={(e) => setGrupo(e.target.value)}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Ingresa el grupo"
            required
          />
        </div>
        <button
          onClick={fetchAsistencias}
          className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
        >
          Obtener Asistencias
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
        {asistencias.length > 0 && (
          <div className="mt-6 overflow-auto">
            <h2 className="text-lg font-bold mb-2">Asistencias del Grupo {grupo}:</h2>
            <table className="w-full border-collapse border border-gray-300">
              <thead>
                <tr className="bg-gray-200">
                  <th className="border border-gray-300 px-4 py-2">Fecha</th>
                  <th className="border border-gray-300 px-4 py-2">Día</th>
                  <th className="border border-gray-300 px-4 py-2">Hora Inicio</th>
                  <th className="border border-gray-300 px-4 py-2">Hora Fin</th>
                  <th className="border border-gray-300 px-4 py-2">Estudiante</th>
                  <th className="border border-gray-300 px-4 py-2">Asistió</th>
                </tr>
              </thead>
              <tbody>
                {asistencias.map((asistencia, index) => (
                  <tr key={index} className="text-center">
                    <td className="border border-gray-300 px-4 py-2">{asistencia.fecha}</td>
                    <td className="border border-gray-300 px-4 py-2">{asistencia.dia}</td>
                    <td className="border border-gray-300 px-4 py-2">{asistencia.hora_inicio}</td>
                    <td className="border border-gray-300 px-4 py-2">{asistencia.hora_fin}</td>
                    <td className="border border-gray-300 px-4 py-2">{asistencia.estudiante}</td>
                    <td className="border border-gray-300 px-4 py-2">{asistencia.asistio}</td>
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
