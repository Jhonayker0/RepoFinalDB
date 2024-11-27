"use client";

import { useState } from "react";

export default function ReporteAulas() {
  const [reporte, setReporte] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  const generarReporte = async () => {
    try {
      const response = await fetch("http://localhost:5000/generar_reporte_aulas", {
        method: "GET",
      });

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
      <div className="bg-white p-6 rounded shadow-md w-full max-w-4xl">
        <h1 className="text-2xl font-bold text-center mb-4">Reporte de Aulas</h1>
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
                <th className="px-4 py-2 border text-left">Grupo</th>
                <th className="px-4 py-2 border text-left">Grado T</th>
                <th className="px-4 py-2 border text-left">Grado Num</th>
                <th className="px-4 py-2 border text-left">Grupo Equivalente</th>
                <th className="px-4 py-2 border text-left">Jornada</th>
                <th className="px-4 py-2 border text-left">Año</th>
                <th className="px-4 py-2 border text-left">Institución</th>
                <th className="px-4 py-2 border text-left">Tutor</th>
              </tr>
            </thead>
            <tbody>
              {reporte.map((aula, index) => (
                <tr key={index} className="border-b">
                  <td className="px-4 py-2">{aula.grupo}</td>
                  <td className="px-4 py-2">{aula.grado_t}</td>
                  <td className="px-4 py-2">{aula.grado_num}</td>
                  <td className="px-4 py-2">{aula.grupo_equivalente}</td>
                  <td className="px-4 py-2">{aula.jornada}</td>
                  <td className="px-4 py-2">{aula.anio}</td>
                  <td className="px-4 py-2">{aula.institucion}</td>
                  <td className="px-4 py-2">{aula.tutor}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
