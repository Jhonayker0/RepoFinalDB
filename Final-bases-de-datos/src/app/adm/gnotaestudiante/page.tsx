"use client";

import { useEffect, useState } from "react";

export default function CalificacionesAula() {
  const [grupo, setGrupo] = useState("");
  const [anio, setAnio] = useState("");
  const [calificaciones, setCalificaciones] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);
  const [userId, setUserId] = useState<string | null>(null);
  useEffect(() => {
    // Obtener el dato de la sesión al cargar la página
    const storedUserId = sessionStorage.getItem("userId");
    setUserId(storedUserId);
  }, []);
  const fetchCalificaciones = async () => {
    if (!grupo || !anio) {
      setMessage("Por favor, ingresa el grupo y el año.");
      return;
    }

    try {
      const response = await fetch(
        `http://localhost:5000/calificaciones-aula?grupo=${grupo}&anio=${anio}`
      );

      if (!response.ok) {
        const errorData = await response.json();
        setMessage(errorData.error || errorData.message || "Error al obtener las calificaciones.");
        return;
      }

      const data = await response.json();
      setCalificaciones(data.reporte);
      setMessage(null); // Limpia el mensaje de error
    } catch (error: any) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-lg">
        <h1 className="text-2xl font-bold text-center mb-4">Calificaciones por Aula</h1>
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
        <div className="mb-4">
          <label htmlFor="anio" className="block text-sm font-medium text-gray-700">
            Año
          </label>
          <input
            type="number"
            id="anio"
            value={anio}
            onChange={(e) => setAnio(e.target.value)}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Ingresa el año"
            required
          />
        </div>
        <button
          onClick={fetchCalificaciones}
          className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
        >
          Obtener Calificaciones
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
        {calificaciones.length > 0 && (
          <div className="mt-6">
            <h2 className="text-lg font-bold mb-2">Calificaciones del Grupo {grupo}:</h2>
            <table className="w-full border-collapse border border-gray-300">
              <thead>
                <tr className="bg-gray-200">
                  <th className="border border-gray-300 px-4 py-2">ID Estudiante</th>
                  <th className="border border-gray-300 px-4 py-2">Nombre</th>
                  <th className="border border-gray-300 px-4 py-2">Nota</th>
                  <th className="border border-gray-300 px-4 py-2">Bloque Lectivo</th>
                </tr>
              </thead>
              <tbody>
                {calificaciones.map((calificacion, index) => (
                  <tr key={index} className="text-center">
                    <td className="border border-gray-300 px-4 py-2">{calificacion.id_estudiante}</td>
                    <td className="border border-gray-300 px-4 py-2">{calificacion.nombre}</td>
                    <td className="border border-gray-300 px-4 py-2">{calificacion.nota}</td>
                    <td className="border border-gray-300 px-4 py-2">{calificacion.bloque_lectivo}</td>
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
