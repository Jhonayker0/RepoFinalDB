"use client";

import { useEffect, useState } from "react";


export default function ReporteEstudiantes() {
  const [grupo, setGrupo] = useState("");
  const [reporte, setReporte] = useState<any[]>([]);
  const [message, setMessage] = useState<string | null>(null);
  const [selectedStudent, setSelectedStudent] = useState<any>(null); // Estudiante seleccionado para calificar
  const [nota, setNota] = useState<string | number>("");
  const [bloqueLectivo, setBloqueLectivo] = useState("");
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
      setMessage(null); // Limpia el mensaje de error
    } catch (error: any) {
      setMessage("Error al conectar con el servidor");
    }
  };

  const handleOpenDialog = (student: any) => {
    setSelectedStudent(student);
    setNota("");
    setBloqueLectivo("");
  };

  const handleCloseDialog = () => {
    setSelectedStudent(null);
  };

  const handleCalificar = async () => {
    if (!nota || !bloqueLectivo) {
      alert("Por favor, completa todos los campos antes de enviar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/calificar-estudiante", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id_estudiante: selectedStudent.id_estudiante,
          nota: parseFloat(nota.toString()),
          bloque_lectivo: bloqueLectivo,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        alert(errorData.error || "Error al calificar al estudiante.");
        return;
      }

      const data = await response.json();
      alert(data.message);
      handleCloseDialog();
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
                  <button
                    onClick={() => handleOpenDialog(estudiante)}
                    className="bg-green-600 text-white py-1 px-2 rounded hover:bg-green-700"
                  >
                    Calificar
                  </button>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* Alert Dialog */}
      {selectedStudent && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div className="bg-white p-6 rounded shadow-md w-full max-w-sm">
            <h2 className="text-xl font-bold mb-4">Calificar Estudiante</h2>
            <p>
              <strong>Estudiante:</strong> {selectedStudent.nombre_completo}
            </p>
            <div className="mt-4">
              <label htmlFor="nota" className="block text-sm font-medium text-gray-700">
                Nota
              </label>
              <input
                type="number"
                id="nota"
                value={nota}
                onChange={(e) => setNota(e.target.value)}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
                placeholder="Ingresa la nota"
                required
              />
            </div>
            <div className="mt-4">
              <label htmlFor="bloqueLectivo" className="block text-sm font-medium text-gray-700">
                Bloque Lectivo
              </label>
              <input
                type="text"
                id="bloqueLectivo"
                value={bloqueLectivo}
                onChange={(e) => setBloqueLectivo(e.target.value)}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
                placeholder="Ingresa el bloque lectivo"
                required
              />
            </div>
            <div className="mt-6 flex justify-end space-x-2">
              <button
                onClick={handleCloseDialog}
                className="bg-gray-400 text-white py-2 px-4 rounded hover:bg-gray-500"
              >
                Cancelar
              </button>
              <button
                onClick={handleCalificar}
                className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
              >
                Calificar
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
