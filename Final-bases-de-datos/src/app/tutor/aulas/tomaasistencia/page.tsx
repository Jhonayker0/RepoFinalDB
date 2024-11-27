"use client";

import { useEffect, useState } from "react";

export default function ReporteEstudiantes() {
  const [grupo, setGrupo] = useState("");
  const [idTutor, setIdTutor] = useState(""); // ID del tutor
  const [codigoHorario, setCodigoHorario] = useState("");
  const [fecha, setFecha] = useState(new Date().toISOString().split("T")[0]); // Fecha actual por defecto
  const [reporte, setReporte] = useState<any[]>([]);
  const [asistenciaData, setAsistenciaData] = useState<{ [key: string]: string }>({}); // Asistencia de cada estudiante
  const [message, setMessage] = useState<string | null>(null);
  const [userId, setUserId] = useState<string | null>(null);
  useEffect(() => {
    // Obtener el dato de la sesión al cargar la página
    const storedUserId = sessionStorage.getItem("userId");
    setUserId(storedUserId);
  }, []);
  const fetchReporte = async () => {
    if (!grupo) {
      setMessage("Por favor, ingresa un grupo.");
      return;
    }

    try {
      const response = await fetch(`http://localhost:5000/reporte-estudiantes-aula?grupo=${grupo}`);

      if (!response.ok) {
        const errorData = await response.json();
        setMessage(errorData.error || errorData.message || "Error al obtener el reporte");
        return;
      }

      const data = await response.json();
      setReporte(data.reporte);
      setAsistenciaData(
        data.reporte.reduce((acc: any, estudiante: any) => {
          acc[`asiste_${estudiante.id_estudiante}`] = "N"; // Por defecto, todos los estudiantes están marcados como no asistieron
          return acc;
        }, {})
      );
      setMessage(null); // Limpia el mensaje de error
    } catch (error: any) {
      setMessage("Error al conectar con el servidor");
    }
  };

  const handleCheckboxChange = (idEstudiante: string, value: boolean) => {
    setAsistenciaData((prev) => ({
      ...prev,
      [`asiste_${idEstudiante}`]: value ? "S" : "N", // Marca asistencia como "S" o "N"
    }));
  };

  const handleRegistrarAsistencias = async () => {
    if (!codigoHorario || !userId) {
      alert("Por favor, ingresa el código de horario y el ID del tutor.");
      return;
    }

    try {
      const body = {
        grupo,
        codigo_horario: codigoHorario,
        fecha,
        id_tutor: userId,
        ...asistenciaData, // Agrega el estado de asistencia de cada estudiante
      };

      console.log("Datos enviados al servidor:", body); // Depuración

      const response = await fetch("http://localhost:5000/registrar_asistencia", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        const errorData = await response.json();
        alert(errorData.error || "Error al registrar las asistencias.");
        return;
      }

      const data = await response.json();
      alert(data.message);
    } catch (error: any) {
      alert("Error al conectar con el servidor.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-lg">
        <h1 className="text-2xl font-bold text-center mb-4">Reporte de Estudiantes</h1>
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
          <label htmlFor="codigoHorario" className="block text-sm font-medium text-gray-700">
            Código de Horario
          </label>
          <input
            type="text"
            id="codigoHorario"
            value={codigoHorario}
            onChange={(e) => setCodigoHorario(e.target.value)}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Ingresa el código de horario"
            required
          />
        </div>
        <button
          onClick={fetchReporte}
          className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
        >
          Obtener Reporte
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
        {reporte.length > 0 && (
          <div className="mt-6">
            <h2 className="text-lg font-bold mb-2">Estudiantes del Grupo {grupo}:</h2>
            <ul className="space-y-2">
              {reporte.map((estudiante) => (
                <li
                  key={estudiante.id_estudiante}
                  className="border border-gray-300 rounded p-4 flex justify-between items-center"
                >
                  <div>
                    <p>
                      <strong>Nombre:</strong> {estudiante.nombre_completo}
                    </p>
                    <p>
                      <strong>Grupo:</strong> {estudiante.grupo}
                    </p>
                    <p>
                      <strong>Institución:</strong> {estudiante.institucion}
                    </p>
                  </div>
                  <input
                    type="checkbox"
                    checked={asistenciaData[`asiste_${estudiante.id_estudiante}`] === "S"}
                    onChange={(e) =>
                      handleCheckboxChange(estudiante.id_estudiante, e.target.checked)
                    }
                    className="h-5 w-5 text-blue-600 border-gray-300 rounded"
                  />
                </li>
              ))}
            </ul>
            <button
              onClick={handleRegistrarAsistencias}
              className="mt-4 w-full bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700"
            >
              Registrar Asistencias
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
