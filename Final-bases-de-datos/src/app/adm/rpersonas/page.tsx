"use client";

import { useState, useEffect } from "react";

export default function ReportePersonas() {
  const [personas, setPersonas] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  const generarReporte = async () => {
    try {
      const response = await fetch("http://localhost:5000/reporte-personas", {
        method: "GET",
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.message || data.error);
      } else {
        setPersonas(data.reporte);
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
      <div className="bg-white p-6 rounded shadow-md w-full max-w-4xl">
        <h1 className="text-2xl font-bold text-center mb-4">Reporte de Personas</h1>

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

        {personas.length > 0 && (
          <table className="min-w-full table-auto mt-6">
            <thead>
              <tr className="bg-gray-200">
                <th className="px-4 py-2 border text-left">Tipo ID</th>
                <th className="px-4 py-2 border text-left">Identificación</th>
                <th className="px-4 py-2 border text-left">ID Usuario</th>
                <th className="px-4 py-2 border text-left">Nombre Completo</th>
                <th className="px-4 py-2 border text-left">Correo</th>
                <th className="px-4 py-2 border text-left">Teléfono</th>
              </tr>
            </thead>
            <tbody>
              {personas.map((persona, index) => (
                <tr key={index} className="border-b">
                  <td className="px-4 py-2">{persona.tipo_id}</td>
                  <td className="px-4 py-2">{persona.identificacion}</td>
                  <td className="px-4 py-2">{persona.id_usuario}</td>
                  <td className="px-4 py-2">{persona.nombre_completo}</td>
                  <td className="px-4 py-2">{persona.correo}</td>
                  <td className="px-4 py-2">{persona.telefono}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
