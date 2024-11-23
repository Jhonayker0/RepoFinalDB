# RepoFinalDB

En este repositorio se encuentran los siguientes entregables:
-Modelo EntidadRelacion
-Modelo Relacional
-Backup de la Base de Datos Relacional
-Scripts para el ingreso de los datos en cada una de las tablas
-Aplicacion que implementa la estructura del negocio:
    -Backend
    -Frontend: Debido al tamaño Github no permitió añadir los archivos,
    por lo que


# Proyecto - Backend

Gestionar usuarios, instituciones, aulas, horarios y estudiantes. Proporciona una serie de API REST que interactúan con una base de datos relacional.

---

## 🚀 Características

- Gestión de usuarios, estudiantes, instituciones, horarios y aulas.
- Registro y consulta de asistencias.
- Generación de reportes detallados (usuarios, instituciones, estudiantes por aula, calificaciones, etc.).
- API RESTful con manejo de errores y respuestas estandarizadas.

---

## 🛠 Requisitos previos

Antes de ejecutar este proyecto, asegúrate de cumplir con los siguientes requisitos:

1. **Python** (>= 3.8)
2. **Servidor de base de datos** compatible (PostgreSQL, MySQL, etc.)
3. **Paquetes Python**:
   - Flask
   - psycopg2 (o el cliente correspondiente a tu base de datos)
   - Otros necesarios (se especifican en `requirements.txt`)

---

## 📂 Estructura del proyecto

```
.
├── app.py                # Archivo principal que inicia el servidor Flask
├── Conexion.py           # Configuración de conexión a la base de datos
├── InicioSesion.py       # Lógica de verificación de credenciales
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

---

## ⚙ Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la conexión a la base de datos

En el archivo `Conexion.py`, configura los parámetros de conexión:

```python
import psycopg2

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",       # Cambia por tu host
        port="5432",            # Puerto del servidor de la base de datos
        database="mi_base",     # Nombre de la base de datos
        user="mi_usuario",      # Usuario
        password="mi_contraseña" # Contraseña
    )
```

### 5. Crear la base de datos y el esquema

Asegúrate de que las tablas y esquemas mencionados en el proyecto existan en tu base de datos. Si necesitas un script de inicialización, crea uno basado en las tablas utilizadas.

Ejemplo:
```sql
CREATE SCHEMA "TempSchema";
CREATE TABLE "TempSchema"."Usuario" (
    "IDUsuario" SERIAL PRIMARY KEY,
    "Rol" VARCHAR(50),
    "Pwd" VARCHAR(255),
    "Año" INTEGER
);
-- Añade más tablas según las necesidades del proyecto
```

---

## ▶ Cómo ejecutar el servidor

### 1. Iniciar la base de datos
Asegúrate de que el servidor de la base de datos esté activo.

### 2. Ejecutar el servidor Flask

```bash
python app.py
```

Por defecto, la aplicación estará disponible en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Pruebas

Puedes utilizar herramientas como **Postman** o **cURL** para probar los endpoints. Aquí hay un ejemplo básico:

```bash
curl -X POST http://127.0.0.1:5000/obtener-rol \
-H "Content-Type: application/json" \
-d '{"identificacion": "123456", "password": "mi_password"}'
```

---
