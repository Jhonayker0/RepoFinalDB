"use client";

import { useState, useEffect } from "react";

export default function ReporteInstituciones() {
  const [instituciones, setInstituciones] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  const generarReporte = async () => {
    try {
      const response = await fetch("http://localhost:5000/reporte-instituciones", {
        method: "GET",
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.message || data.error);
      } else {
        setInstituciones(data.reporte);
        setMessage(null); // Limpiar el mensaje de error si se obtiene el reporte correctamente
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  useEffect(() => {
    generarReporte();
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-6xl">
        <h1 className="text-2xl font-bold text-center mb-4">Reporte de Instituciones</h1>

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

        {instituciones.length > 0 && (
          <table className="min-w-full table-auto mt-6">
            <thead>
              <tr className="bg-gray-200">
                <th className="px-4 py-2 border text-left">Código</th>
                <th className="px-4 py-2 border text-left">Nombre Institución</th>
                <th className="px-4 py-2 border text-left">Rector</th>
                <th className="px-4 py-2 border text-left">Localidad</th>
                <th className="px-4 py-2 border text-left">Barrio</th>
                <th className="px-4 py-2 border text-left">Número</th>
                <th className="px-4 py-2 border text-left">Dirección</th>
                <th className="px-4 py-2 border text-left">Año</th>
              </tr>
            </thead>
            <tbody>
              {instituciones.map((institucion, index) => (
                <tr key={index} className="border-b">
                  <td className="px-4 py-2">{institucion.codigo}</td>
                  <td className="px-4 py-2">{institucion.nombre}</td>
                  <td className="px-4 py-2">{institucion.rector}</td>
                  <td className="px-4 py-2">{institucion.localidad}</td>
                  <td className="px-4 py-2">{institucion.barrio}</td>
                  <td className="px-4 py-2">{institucion.numero}</td>
                  <td className="px-4 py-2">{institucion.direccion}</td>
                  <td className="px-4 py-2">{institucion.anio}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
