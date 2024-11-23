import React, { useState } from 'react';
import Login from './components/Login';
import AdminDashboard from './components/AdminDashboard';
import TutorDashboard from './components/TutorDashboard';

function App() {
  const [role, setRole] = useState(null);

  return (
    <div className="App">
      {role === null && <Login setRole={setRole} />}
      {role === 'admin' && <AdminDashboard setRole={setRole} />}
      {role === 'tutor' && <TutorDashboard setRole={setRole} />}
    </div>
  );
}

export default App;



