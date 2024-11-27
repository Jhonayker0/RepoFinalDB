"use client";

import { useState, useEffect } from "react";

export default function ReporteUsuarios() {
  const [usuarios, setUsuarios] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);

  const generarReporte = async () => {
    try {
      const response = await fetch("http://localhost:5000/reporte-usuarios", {
        method: "GET",
      });

      const data = await response.json();

      if (!response.ok) {
        setMessage(data.message || data.error);
      } else {
        setUsuarios(data.reporte);
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
      <div className="bg-white p-6 rounded shadow-md w-full max-w-3xl">
        <h1 className="text-2xl font-bold text-center mb-4">Reporte de Usuarios</h1>

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

        {usuarios.length > 0 && (
          <table className="min-w-full table-auto mt-6">
            <thead>
              <tr className="bg-gray-200">
                <th className="px-4 py-2 border text-left">ID Usuario</th>
                <th className="px-4 py-2 border text-left">Nombre Completo</th>
                <th className="px-4 py-2 border text-left">Rol</th>
                <th className="px-4 py-2 border text-left">Correo</th>
                <th className="px-4 py-2 border text-left">Teléfono</th>
              </tr>
            </thead>
            <tbody>
              {usuarios.map((usuario, index) => (
                <tr key={index} className="border-b">
                  <td className="px-4 py-2">{usuario.id_usuario}</td>
                  <td className="px-4 py-2">{usuario.nombre_completo}</td>
                  <td className="px-4 py-2">{usuario.rol}</td>
                  <td className="px-4 py-2">{usuario.correo}</td>
                  <td className="px-4 py-2">{usuario.telefono}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
