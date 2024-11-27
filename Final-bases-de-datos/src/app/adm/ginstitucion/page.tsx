"use client";

import { useState } from "react";

export default function GestionInstituciones() {
  const [formData, setFormData] = useState({
    codigo_insti: "",
    nombre_insti: "",
    nombre_rector: "",
    localidad: "",
    barrio: "",
    numero: "",
    direccion: "",
  });
  const [message, setMessage] = useState<string | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const agregarInstitucion = async () => {
    try {
      const response = await fetch("http://localhost:5000/agregar-institucion", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al agregar la institución.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const editarInstitucion = async () => {
    if (!formData.codigo_insti) {
      setMessage("Por favor, ingresa el código de la institución para editar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/editar-institucion", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al editar la institución.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const eliminarInstitucion = async () => {
    if (!formData.codigo_insti) {
      setMessage("Por favor, ingresa el código de la institución para eliminar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/eliminar-institucion", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ codigo_insti: formData.codigo_insti }),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al eliminar la institución.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-lg">
        <h1 className="text-2xl font-bold text-center mb-4">Gestión de Instituciones</h1>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Código Institución</label>
          <input
            type="text"
            name="codigo_insti"
            value={formData.codigo_insti}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Código de la institución"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Nombre Institución</label>
          <input
            type="text"
            name="nombre_insti"
            value={formData.nombre_insti}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Nombre de la institución"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Nombre Rector</label>
          <input
            type="text"
            name="nombre_rector"
            value={formData.nombre_rector}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Nombre del rector"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Localidad</label>
          <input
            type="text"
            name="localidad"
            value={formData.localidad}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Localidad"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Barrio</label>
          <input
            type="text"
            name="barrio"
            value={formData.barrio}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Barrio"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Número de Contacto</label>
          <input
            type="text"
            name="numero"
            value={formData.numero}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Número de contacto"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Dirección</label>
          <input
            type="text"
            name="direccion"
            value={formData.direccion}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Dirección"
            required
          />
        </div>

        <div className="flex justify-between space-x-4">
          <button
            onClick={agregarInstitucion}
            className="w-1/3 bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700"
          >
            Agregar
          </button>
          <button
            onClick={editarInstitucion}
            className="w-1/3 bg-yellow-600 text-white py-2 px-4 rounded hover:bg-yellow-700"
          >
            Editar
          </button>
          <button
            onClick={eliminarInstitucion}
            className="w-1/3 bg-red-600 text-white py-2 px-4 rounded hover:bg-red-700"
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
