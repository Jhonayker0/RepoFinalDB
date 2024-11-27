"use client";

import { useState } from "react";

export default function Login() {
  const [identificacion, setIdentificacion] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:5000/obtener-rol", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ identificacion, password }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        setMessage(errorData.error || "Error al autenticar");
        return;
      }

      const data = await response.json();
      const role = data.roles;
      const userId = data.Usuario;

      // Guardar el ID del usuario en la sesión (localStorage o sesión temporal)
      sessionStorage.setItem("userId", userId);
      sessionStorage.setItem("Rol", role);

      // Redirigir según el rol
      if (role === "Tutor") {
        window.location.href = "/tutor";
      } else if (role === "Administrador") {
        window.location.href = "/adm";
      } else {
        setMessage("Rol desconocido. Contacta al administrador.");
      }
    } catch (error: any) {
      setMessage("Error al conectar con el servidor");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-8">
      <div className="bg-white p-6 rounded shadow-md w-full max-w-sm">
        <h1 className="text-2xl font-bold text-center mb-4">Iniciar Sesión</h1>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div>
            <label htmlFor="identificacion" className="block text-sm font-medium text-gray-700">
              Identificación
            </label>
            <input
              type="text"
              id="identificacion"
              value={identificacion}
              onChange={(e) => setIdentificacion(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              placeholder="Ingresa tu identificación"
              required
            />
          </div>
          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700">
              Contraseña
            </label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded"
              placeholder="Ingresa tu contraseña"
              required
            />
          </div>
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
          >
            Iniciar Sesión
          </button>
        </form>
        {message && (
          <p
            className={`mt-4 text-sm ${
              message.startsWith("Rol desconocido") || message.startsWith("Error")
                ? "text-red-500"
                : "text-green-500"
            }`}
          >
            {message}
          </p>
        )}
      </div>
    </div>
  );
}
