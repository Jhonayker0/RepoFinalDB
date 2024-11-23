import React, { useState } from 'react';
import GestionarUsuarios from './GestionarUsuarios';
import GestionarMenu from './GestionarMenu';
import GestionarRoles from './GestionarRoles';
import GestionarPersonas from './GestionarPersonas';
import GestionarInstituciones from './GestionarInstituciones';
import GestionarAulas from './GestionarAulas';
import GestionarHorarios from './GestionarHorarios';
import GestionarEstudiantes from './GestionarEstudiantes';
import GestionarTutores from './GestionarTutores';
import GestionarAsistenciaProfesor from './GestionarAsistenciaProfesor';
import GestionarAsistenciaEstudiante from './GestionarAsistenciaEstudiante';
import GestionarNotas from './GestionarNotas';
import Reportes from './Reportes';
import './AdminDashboard.css';

const AdminDashboard = ({ setRole }) => {
  const [selectedSection, setSelectedSection] = useState(null);

  // Función para manejar la selección de una opción en el menú de gestión
  const handleSectionSelect = (section) => {
    setSelectedSection(section);
  };

  const goBack = () => {
    setSelectedSection(null);
  };

  return (
    <div className="admin-dashboard-container">
      {!selectedSection ? (
        <>
          <h2>Bienvenido, Administrador</h2>
          <div className="admin-dashboard-menu">
            <button onClick={() => handleSectionSelect('gestionarUsuarios')}>Gestión de Usuarios</button>
            <button onClick={() => handleSectionSelect('gestionarMenu')}>Gestión de Menú</button>
            <button onClick={() => handleSectionSelect('gestionarRoles')}>Gestión de Roles</button>
            <button onClick={() => handleSectionSelect('gestionarPersonas')}>Gestión de Personas</button>
            <button onClick={() => handleSectionSelect('gestionarInstituciones')}>Gestión de Instituciones</button>
            <button onClick={() => handleSectionSelect('gestionarAulas')}>Gestión de Aulas</button>
            <button onClick={() => handleSectionSelect('gestionarHorarios')}>Gestión de Horarios</button>
            <button onClick={() => handleSectionSelect('gestionarEstudiantes')}>Gestión de Estudiantes</button>
            <button onClick={() => handleSectionSelect('gestionarTutores')}>Gestión de Tutores</button>
            <button onClick={() => handleSectionSelect('gestionarAsistenciaProfesor')}>Asistencia del Profesor</button>
            <button onClick={() => handleSectionSelect('gestionarAsistenciaEstudiante')}>Asistencia del Estudiante</button>
            <button onClick={() => handleSectionSelect('gestionarNotas')}>Notas de Estudiantes</button>
            <button onClick={() => handleSectionSelect('reportes')}>Reportes</button>
          </div>
          <button onClick={() => setRole(null)} style={{ marginTop: '10px' }}>Cerrar Sesión</button>
        </>
      ) : (
        <div className="admin-dashboard-section">
          <h3>{selectedSection}</h3>
          
          {/* Mostrar el componente correspondiente según la sección seleccionada */}
          {selectedSection === 'gestionarUsuarios' && <GestionarUsuarios />}
          {selectedSection === 'gestionarMenu' && <GestionarMenu />}
          {selectedSection === 'gestionarRoles' && <GestionarRoles />}
          {selectedSection === 'gestionarPersonas' && <GestionarPersonas />}
          {selectedSection === 'gestionarInstituciones' && <GestionarInstituciones />}
          {selectedSection === 'gestionarAulas' && <GestionarAulas />}
          {selectedSection === 'gestionarHorarios' && <GestionarHorarios />}
          {selectedSection === 'gestionarEstudiantes' && <GestionarEstudiantes />}
          {selectedSection === 'gestionarTutores' && <GestionarTutores />}
          {selectedSection === 'gestionarAsistenciaProfesor' && <GestionarAsistenciaProfesor />}
          {selectedSection === 'gestionarAsistenciaEstudiante' && <GestionarAsistenciaEstudiante />}
          {selectedSection === 'gestionarNotas' && <GestionarNotas />}
          {selectedSection === 'reportes' && <Reportes />}
          
          <button onClick={goBack}>Volver al Menú Principal</button>
        </div>
      )}
    </div>
  );
};

export default AdminDashboard;



// import React, { useState } from 'react';
// import './AdminDashboard.css';

// const AdminDashboard = ({ setRole }) => {
//   const [selectedSection, setSelectedSection] = useState(null);
//   const [response, setResponse] = useState(null); // Para mostrar datos de respuesta de la API

//   const handleSectionSelect = (section) => {
//     setSelectedSection(section);
//     setResponse(null); // Limpiar respuesta al cambiar de sección
//   };

//   const goBack = () => {
//     setSelectedSection(null);
//   };

//   // Función para interactuar con los endpoints
//   const fetchData = async (endpoint, method = 'GET', body = null) => {
//     const url = `http://localhost:5000/${endpoint}`;
//     const options = {
//       method,
//       headers: { 'Content-Type': 'application/json' },
//       ...(body && { body: JSON.stringify(body) }),
//     };

//     try {
//       const res = await fetch(url, options);
//       if (!res.ok) {
//         throw new Error(`Error ${res.status}: ${res.statusText}`);
//       }
//       const data = await res.json();
//       setResponse(data);
//     } catch (error) {
//       console.error(`Error al interactuar con el endpoint ${endpoint}:`, error);
//       setResponse({ error: error.message });
//     }
//   };

//   // Ejemplo de interacción con los endpoints
//   const handleGestionarUsuarios = () => {
//     fetchData('reporte-usuarios');
//   };

//   const handleGestionarInstituciones = () => {
//     fetchData('reporte-instituciones');
//   };

//   const handleAgregarUsuario = () => {
//     const newUser = {
//       rol: 'Admin',
//       pwd: '12345',
//       tipo_id: 'CC',
//       identificacion: '100000000',
//       primer_nombre: 'Juan',
//       segundo_nombre: null,
//       primer_apellido: 'Pérez',
//       segundo_apellido: null,
//       correo: 'juan.perez@example.com',
//       telefono: '3001234567',
//     };
//     fetchData('agregar-usuario', 'POST', newUser);
//   };

//   const handleEliminarUsuario = () => {
//     const userToDelete = { identificacion: '100000000' };
//     fetchData('eliminar-usuario', 'DELETE', userToDelete);
//   };

//   return (
//     <div className="admin-dashboard-container">
//       {!selectedSection ? (
//         <>
//           <h2>Bienvenido, Administrador</h2>
//           <div className="admin-dashboard-menu">
//             <button onClick={() => handleSectionSelect('gestionarUsuarios')}>Gestión de Usuarios</button>
//             <button onClick={() => handleSectionSelect('gestionarInstituciones')}>Gestión de Instituciones</button>
//             <button onClick={() => handleAgregarUsuario()}>Agregar Usuario</button>
//             <button onClick={() => handleEliminarUsuario()}>Eliminar Usuario</button>
//           </div>
//           <button onClick={() => setRole(null)} style={{ marginTop: '10px' }}>Cerrar Sesión</button>
//         </>
//       ) : (
//         <div className="admin-dashboard-section">
//           <h3>{selectedSection}</h3>

//           {/* Sección dinámica según lo seleccionado */}
//           {selectedSection === 'gestionarUsuarios' && (
//             <div>
//               <button onClick={handleGestionarUsuarios}>Cargar Usuarios</button>
//             </div>
//           )}

//           {selectedSection === 'gestionarInstituciones' && (
//             <div>
//               <button onClick={handleGestionarInstituciones}>Cargar Instituciones</button>
//             </div>
//           )}

//           {/* Mostrar la respuesta de la API */}
//           {response && (
//             <div className="api-response">
//               <pre>{JSON.stringify(response, null, 2)}</pre>
//             </div>
//           )}

//           <button onClick={goBack}>Volver al Menú Principal</button>
//         </div>
//       )}
//     </div>
//   );
// };

// export default AdminDashboard;
