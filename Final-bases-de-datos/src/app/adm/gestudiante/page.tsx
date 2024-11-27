"use client";

import { useState } from "react";

export default function GestionEstudiantes() {
  const [formData, setFormData] = useState({
    tipo_id: "",
    id_estudiante: "",
    primer_nombre: "",
    segundo_nombre: "",
    primer_apellido: "",
    segundo_apellido: "",
    genero: "",
    fecha_nacimiento: "",
    estrato: "",
    anio: "",
    grupo: "",
  });
  const [idEstudiante, setIdEstudiante] = useState<string>(""); // Para eliminar o buscar estudiantes
  const [message, setMessage] = useState<string | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const insertarEstudiante = async () => {
    try {
      const response = await fetch("http://localhost:5000/insertar-estudiante", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al insertar el estudiante.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const eliminarEstudiante = async () => {
    if (!idEstudiante) {
      setMessage("Por favor, ingresa el ID del estudiante a eliminar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/eliminar-estudiante", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id_estudiante: idEstudiante }),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al eliminar el estudiante.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const actualizarEstudiante = async () => {
    if (!formData.id_estudiante) {
      setMessage("Por favor, ingresa el ID del estudiante a actualizar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/actualizar-estudiante", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al actualizar el estudiante.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-3xl">
        <h1 className="text-2xl font-bold text-center mb-4">Gestión de Estudiantes</h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">Tipo ID</label>
            <input
              type="text"
              name="tipo_id"
              value={formData.tipo_id}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              placeholder="CC, TI, etc."
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">ID Estudiante</label>
            <input
              type="text"
              name="id_estudiante"
              value={formData.id_estudiante}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              placeholder="Identificación"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Primer Nombre</label>
            <input
              type="text"
              name="primer_nombre"
              value={formData.primer_nombre}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Segundo Nombre</label>
            <input
              type="text"
              name="segundo_nombre"
              value={formData.segundo_nombre}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Primer Apellido</label>
            <input
              type="text"
              name="primer_apellido"
              value={formData.primer_apellido}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Segundo Apellido</label>
            <input
              type="text"
              name="segundo_apellido"
              value={formData.segundo_apellido}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Género</label>
            <select
              name="genero"
              value={formData.genero}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              required
            >
              <option value="">Seleccionar</option>
              <option value="M">Masculino</option>
              <option value="F">Femenino</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Fecha de Nacimiento</label>
            <input
              type="date"
              name="fecha_nacimiento"
              value={formData.fecha_nacimiento}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Estrato</label>
            <input
              type="number"
              name="estrato"
              value={formData.estrato}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Año</label>
            <input
              type="number"
              name="anio"
              value={formData.anio}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">Grupo</label>
            <input
              type="number"
              name="grupo"
              value={formData.grupo}
              onChange={handleInputChange}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              required
            />
          </div>
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">ID Estudiante (Eliminar)</label>
          <input
            type="text"
            value={idEstudiante}
            onChange={(e) => setIdEstudiante(e.target.value)}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Identificación del estudiante"
          />
        </div>

        <div className="flex flex-wrap gap-4">
          <button
            onClick={insertarEstudiante}
            className="bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700 flex-1"
          >
            Insertar
          </button>
          <button
            onClick={actualizarEstudiante}
            className="bg-yellow-600 text-white py-2 px-4 rounded hover:bg-yellow-700 flex-1"
          >
            Actualizar
          </button>
          <button
            onClick={eliminarEstudiante}
            className="bg-red-600 text-white py-2 px-4 rounded hover:bg-red-700 flex-1"
          >
            Eliminar
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
