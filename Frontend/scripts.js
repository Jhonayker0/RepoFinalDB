const loginForm = document.getElementById('loginForm');
const panelSection = document.getElementById('panelSection');
const loginSection = document.getElementById('loginSection');
const loginMessage = document.getElementById('loginMessage');
const tutorName = document.getElementById('tutorName');
const output = document.getElementById('output');

let tutorId;

// Inicio de sesión
loginForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const identificacion = document.getElementById('identificacion').value;
    const password = document.getElementById('password').value;

    fetch('/login-tutor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ identificacion, password }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.error) {
                loginMessage.textContent = data.error;
            } else {
                tutorId = data.id_usuario;
                tutorName.textContent = data.nombre;
                loginSection.style.display = 'none';
                panelSection.style.display = 'block';
            }
        })
        .catch((error) => console.error('Error:', error));
});

// Consultar horarios
document.getElementById('viewHorario').addEventListener('click', () => {
    fetch(`/generar_horario_tutor?id_usuario=${tutorId}`)
        .then((response) => response.json())
        .then((data) => {
            if (data.reporte) {
                output.innerHTML = data.reporte
                    .map(
                        (horario) => `
                    <p>${horario.dia}: ${horario.hora_inicio} - ${horario.hora_fin}, Grupo: ${horario.grupo}</p>
                `
                    )
                    .join('');
            } else {
                output.textContent = data.message || 'No se encontraron horarios.';
            }
        });
});
