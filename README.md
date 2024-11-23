
---

### **README.md**

```markdown
# Sistema de Gestión Académica

Este proyecto es un sistema de gestión académica diseñado para apoyar la enseñanza del inglés en niños de instituciones públicas de Barranquilla, gestionado por la Fundación FOREIGN LANGUAGE FOR KIDS EMPOWERMENT (FLAKE).

## **Descripción General**

El sistema está compuesto por:
1. **Backend:** Construido en Python con Flask (`app.py`), que proporciona una API REST para la gestión de usuarios, instituciones, aulas, horarios, estudiantes, calificaciones y reportes.
2. **Frontend:** Una página web simple (`index.html`) que consume la API del backend y permite a los usuarios interactuar con el sistema según sus roles (Administrador o Tutor).

---

## **Características**

### **Backend**
El backend soporta las siguientes funcionalidades:
- Gestión de **usuarios**, **instituciones**, **aulas**, **horarios**, **estudiantes** y **calificaciones**.
- Registro y consulta de asistencia para profesores y estudiantes.
- Generación de reportes dinámicos para aulas, asistencia y calificaciones.
- Control de acceso basado en roles:
  - **Administrador:** Tiene acceso completo.
  - **Tutor:** Tiene acceso limitado a calificaciones, asistencia y reportes.

### **Frontend**
El frontend incluye:
- Inicio de sesión con redirección según el rol del usuario.
- Panel de administración con operaciones CRUD para cada entidad.
- Panel de tutor con funcionalidades específicas para su rol.
- Generación de reportes dinámicos.

---

## **Requisitos del Sistema**

### **Backend**
- Python 3.8 o superior.
- Flask y Flask-RESTful.
- Base de datos relacional configurada previamente (ejemplo: SQLite o MySQL).

### **Frontend**
- Un navegador web moderno (Chrome, Firefox, Edge, etc.).

---

## **Instrucciones de Instalación**

### **1. Clonar el Repositorio**
Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/Jhonayker0/RepoFinalDB.git
```

### **2. Configurar el Backend**

1. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. **Configurar la base de datos:**
   - Asegúrate de tener configurada la base de datos mencionada en `app.py`.
   - Si estás usando SQLite, el archivo de la base de datos debería generarse automáticamente al ejecutar el backend.

3. **Ejecutar el servidor:**
   ```bash
   python app.py
   ```
   Esto iniciará el servidor en `http://127.0.0.1:5000`.

---

### **3. Configurar el Frontend**

1. Abre el archivo `index.html` en un editor de texto.
2. Asegúrate de que la URL del backend esté configurada correctamente:
   ```javascript
   const apiUrl = 'http://127.0.0.1:5000'; // RECORDAR!!!! Cambiar si el backend está en otra dirección
   ```

3. Abre el archivo `index.html` en tu navegador web.

---


## **Uso del Sistema**

### **1. Inicio de Sesión**
- Ingresa tu identificación y contraseña.
- Según tu rol (Administrador o Tutor), serás redirigido al panel correspondiente.

### **2. Panel de Administración**
- **Usuarios:** Agregar, editar, eliminar y listar usuarios.
- **Instituciones:** Administrar información sobre las instituciones educativas.
- **Aulas:** Gestionar aulas, asignar tutores y grupos.
- **Estudiantes:** Registrar y gestionar estudiantes.
- **Horarios:** Configurar horarios de clases para las aulas.
- **Calificaciones:** Registrar y consultar calificaciones de estudiantes.
- **Reportes:** Generar reportes sobre aulas, asistencia y más.

### **3. Panel del Tutor**
- **Asistencia:** Registrar la asistencia de estudiantes.
- **Calificaciones:** Registrar calificaciones por bloque lectivo.
- **Reportes:** Consultar reportes de asistencia y calificaciones.

---

## **Endpoints del Backend**

### **Usuarios**
- `GET /reporte-usuarios`: Listar usuarios.
- `POST /crear-usuario`: Crear un usuario.

### **Instituciones**
- `GET /reporte-instituciones`: Listar instituciones.
- `POST /crear-institucion`: Crear una institución.

### **Aulas**
- `GET /generar_reporte_aulas`: Listar aulas.
- `POST /aulas/agregar`: Crear un aula.

### **Estudiantes**
- `GET /reporte-estudiantes-aula`: Listar estudiantes por aula.
- `POST /insertar-estudiante`: Registrar un estudiante.

### **Horarios**
- `GET /generar_horario_tutor`: Listar horarios por tutor.
- `POST /insertar-horario`: Crear un horario.

### **Calificaciones**
- `GET /calificaciones-aula`: Listar calificaciones por aula.
- `POST /calificar-estudiante`: Registrar una calificación.

### **Asistencia**
- `GET /asistencias-aula`: Listar asistencias por aula.
- `POST /registrar-asistencia`: Registrar asistencia.

---
