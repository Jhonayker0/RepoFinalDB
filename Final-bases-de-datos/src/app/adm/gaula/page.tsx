"use client";

import { useState } from "react";

export default function GestionAulas() {
  const [formData, setFormData] = useState({
    grado_t: "",
    grado_num: "",
    grupo_equivalente: "",
    jornada: "",
    codigo_insti: "",
    id_usuario: "",
  });
  const [grupo, setGrupo] = useState<number | null>(null);
  const [codigoHorario, setCodigoHorario] = useState<number | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const agregarAula = async () => {
    try {
      const response = await fetch("http://localhost:5000/aulas/agregar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al agregar el aula.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const editarAula = async () => {
    if (!grupo) {
      setMessage("Por favor, ingresa el número del grupo a editar.");
      return;
    }

    try {
      const response = await fetch(`http://localhost:5000/aulas/editar/${grupo}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al editar el aula.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const eliminarAula = async () => {
    if (!grupo) {
      setMessage("Por favor, ingresa el número del grupo a eliminar.");
      return;
    }

    try {
      const response = await fetch(`http://localhost:5000/aulas/eliminar/${grupo}`, {
        method: "DELETE",
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al eliminar el aula.");
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage("Error al conectar con el servidor.");
    }
  };

  const agregarHorarioAula = async () => {
    if (!grupo || !codigoHorario) {
      setMessage("Por favor, ingresa el número del grupo y el código de horario.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/horarios-aula/agregar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ codigo_h: codigoHorario, grupo }),
      });

      const data = await response.json();
      if (!response.ok) {
        setMessage(data.error || "Error al agregar el horario al aula.");
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
        <h1 className="text-2xl font-bold text-center mb-4">Gestión de Aulas</h1>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Grado Tipo</label>
          <input
            type="text"
            name="grado_t"
            value={formData.grado_t}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Ejemplo: Primaria"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Grado Número</label>
          <input
            type="text"
            name="grado_num"
            value={formData.grado_num}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Ejemplo: 5"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Grupo Equivalente</label>
          <input
            type="text"
            name="grupo_equivalente"
            value={formData.grupo_equivalente}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Ejemplo: A"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Jornada</label>
          <select
            name="jornada"
            value={formData.jornada}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            required
          >
            <option value="">Seleccionar</option>
            <option value="Mañana">Mañana</option>
            <option value="Tarde">Tarde</option>
          </select>
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Código Institución</label>
          <input
            type="text"
            name="codigo_insti"
            value={formData.codigo_insti}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Código Institución"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">ID Usuario</label>
          <input
            type="text"
            name="id_usuario"
            value={formData.id_usuario}
            onChange={handleInputChange}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="ID Tutor Responsable"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Grupo (para editar/eliminar/agregar horario)</label>
          <input
            type="number"
            value={grupo || ""}
            onChange={(e) => setGrupo(Number(e.target.value))}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Número del grupo"
          />
        </div>
        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700">Código Horario</label>
          <input
            type="number"
            value={codigoHorario || ""}
            onChange={(e) => setCodigoHorario(Number(e.target.value))}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
            placeholder="Código del horario"
          />
        </div>

        <div className="flex flex-wrap gap-4">
          <button
            onClick={agregarAula}
            className="bg-green-600 text-white py-2 px-4 rounded hover:bg-green-700 flex-1"
          >
            Agregar Aula
          </button>
          <button
            onClick={editarAula}
            className="bg-yellow-600 text-white py-2 px-4 rounded hover:bg-yellow-700 flex-1"
          >
            Editar Aula
          </button>
          <button
            onClick={eliminarAula}
            className="bg-red-600 text-white py-2 px-4 rounded hover:bg-red-700 flex-1"
          >
            Eliminar Aula
          </button>
          <button
            onClick={agregarHorarioAula}
            className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700 flex-1"
          >
            Agregar Horario a Aula
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
