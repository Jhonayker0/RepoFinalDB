"use client";

import { useState } from "react";

export default function GestionHorarios() {
  const [formData, setFormData] = useState({
    fecha_inicio: "",
    fecha_fin: "",
    hora_inicio: "",
    hora_fin: "",
    dia_inicial: "",
    dia_texto: "",
  });
  const [codigoH, setCodigoH] = useState<number | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const insertarHorario = async () => {
    try {
      const response = await fetch("http://localhost:5000/insertar-horario", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al insertar el horario.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const eliminarHorario = async () => {
    if (!codigoH) {
      setMessage("Por favor, ingresa el código del horario a eliminar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/eliminar-horario", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ codigo_h: codigoH }),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al eliminar el horario.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const actualizarHorario = async () => {
    if (!codigoH) {
      setMessage("Por favor, ingresa el código del horario a actualizar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/actualizar-horario", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ ...formData, codigo_h: codigoH }),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al actualizar el horario.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-2xl">
        <h1 className="text-2xl font-bold text-center mb-4">Gestión de Horarios</h1>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Fecha Inicio</label>
          <input
            type="date"
            name="fecha_inicio"
            value={formData.fecha_inicio}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            required
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Fecha Fin</label>
          <input
            type="date"
            name="fecha_fin"
            value={formData.fecha_fin}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            required
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Hora Inicio</label>
          <input
            type="time"
            name="hora_inicio"
            value={formData.hora_inicio}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            required
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Hora Fin</label>
          <input
            type="time"
            name="hora_fin"
            value={formData.hora_fin}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            required
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Día Inicial</label>
          <input
            type="text"
            name="dia_inicial"
            value={formData.dia_inicial}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            required
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Día de la Semana</label>
          <input
            type="text"
            name="dia_texto"
            value={formData.dia_texto}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            required
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Código del Horario</label>
          <input
            type="number"
            value={codigoH || ""}
            onChange={(e) => setCodigoH(Number(e.target.value))}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Código del horario"
          />
        </div>

        <div className="flex flex-wrap gap-4">
          <button
            onClick={insertarHorario}
            className="bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700 flex-1"
          >
            Insertar Horario
          </button>
          <button
            onClick={actualizarHorario}
            className="bg-yellow-600 text-white py-2 px-4 rounded hover:bg-yellow-700 flex-1"
          >
            Actualizar Horario
          </button>
          <button
            onClick={eliminarHorario}
            className="bg-red-600 text-white py-2 px-4 rounded hover:bg-red-700 flex-1"
          >
            Eliminar Horario
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
      </div>
    </div>
  );
}
