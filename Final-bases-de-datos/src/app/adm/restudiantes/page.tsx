"use client";

import { useState } from "react";

export default function ReporteEstudiantesAula() {
  const [grupo, setGrupo] = useState<string>("");
  const [reporte, setReporte] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  const generarReporte = async () => {
    if (!grupo) {
      setMessage("El parámetro 'grupo' es requerido.");
      return;
    }

    try {
      const response = await fetch(
        `http://localhost:5000/reporte-estudiantes-aula?grupo=${grupo}`,
        {
          method: "GET",
        }
      );

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.message || data.error);
      } else {
        setReporte(data.reporte);
        setMessage(null); // Limpiar el mensaje de error si se obtiene el reporte correctamente
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-3xl">
        <h1 className="text-2xl font-bold text-center mb-4">Reporte de Estudiantes por Aula</h1>

        <div className="mb-4">
          <label htmlFor="grupo" className="block text-sm font-medium text-gray-700">
            Grupo
          </label>
          <input
            type="text"
            id="grupo"
            value={grupo}
            onChange={(e) => setGrupo(e.target.value)}
            className="mt-1 block w-full p-2 border border-gray-300 rounded"
            placeholder="Ingrese el grupo"
          />
        </div>

        <div className="flex justify-center mb-4">
          <button
            onClick={generarReporte}
            className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
          >
            Generar Reporte
          </button>
        </div>

        {message && (
          <p
            className={`mt-4 text-sm ${
              message.startsWith("Error") ? "text-red-500" : "text-green-500"
            }`}
          >
            {message}
          </p>
        )}

        {reporte.length > 0 && (
          <table className="min-w-full table-auto mt-6">
            <thead>
              <tr className="bg-gray-200">
                <th className="px-4 py-2 border text-left">ID Estudiante</th>
                <th className="px-4 py-2 border text-left">Nombre Completo</th>
                <th className="px-4 py-2 border text-left">Grupo</th>
                <th className="px-4 py-2 border text-left">Institución</th>
              </tr>
            </thead>
            <tbody>
              {reporte.map((estudiante, index) => (
                <tr key={index} className="border-b">
                  <td className="px-4 py-2">{estudiante.id_estudiante}</td>
                  <td className="px-4 py-2">{estudiante.nombre_completo}</td>
                  <td className="px-4 py-2">{estudiante.grupo}</td>
                  <td className="px-4 py-2">{estudiante.institucion}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
