"use client";

import { useState } from "react";

export default function GestionUsuarios() {
  const [formData, setFormData] = useState({
    rol: "",
    pwd: "",
    tipo_id: "",
    identificacion: "",
    primer_nombre: "",
    segundo_nombre: "",
    primer_apellido: "",
    segundo_apellido: "",
    correo: "",
    telefono: "",
  });
  const [message, setMessage] = useState<string | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const agregarUsuario = async () => {
    try {
      const response = await fetch("http://localhost:5000/agregar-usuario", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al agregar el usuario.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const eliminarUsuario = async () => {
    if (!formData.identificacion) {
      setMessage("Por favor, ingresa la identificación del usuario para eliminar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/eliminar-usuario", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ identificacion: formData.identificacion }),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al eliminar el usuario.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const editarUsuario = async () => {
    if (!formData.identificacion) {
      setMessage("Por favor, ingresa la identificación del usuario para editar.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/actualizar-usuario", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al editar el usuario.");
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
        <h1 className="text-2xl font-bold text-center mb-4">Gestión de Usuarios</h1>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Rol</label>
          <select
            name="rol"
            value={formData.rol}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            required
          >
            <option value="">Seleccionar</option>
            <option value="Admin">Admin</option>
            <option value="Tutor">Tutor</option>
          </select>
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Contraseña</label>
          <input
            type="password"
            name="pwd"
            value={formData.pwd}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Contraseña"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Tipo ID</label>
          <input
            type="text"
            name="tipo_id"
            value={formData.tipo_id}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Tipo de Identificación"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Identificación</label>
          <input
            type="text"
            name="identificacion"
            value={formData.identificacion}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Identificación"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Primer Nombre</label>
          <input
            type="text"
            name="primer_nombre"
            value={formData.primer_nombre}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Primer Nombre"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Segundo Nombre</label>
          <input
            type="text"
            name="segundo_nombre"
            value={formData.segundo_nombre}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Segundo Nombre (opcional)"
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Primer Apellido</label>
          <input
            type="text"
            name="primer_apellido"
            value={formData.primer_apellido}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Primer Apellido"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Segundo Apellido</label>
          <input
            type="text"
            name="segundo_apellido"
            value={formData.segundo_apellido}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Segundo Apellido (opcional)"
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Correo Electrónico</label>
          <input
            type="email"
            name="correo"
            value={formData.correo}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Correo"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Teléfono</label>
          <input
            type="text"
            name="telefono"
            value={formData.telefono}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Teléfono"
            required
          />
        </div>

        <div className="flex justify-between space-x-4">
          <button
            onClick={agregarUsuario}
            className="w-1/3 bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700"
          >
            Agregar
          </button>
          <button
            onClick={editarUsuario}
            className="w-1/3 bg-yellow-600 text-white py-2 px-4 rounded hover:bg-yellow-700"
          >
            Editar
          </button>
          <button
            onClick={eliminarUsuario}
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
