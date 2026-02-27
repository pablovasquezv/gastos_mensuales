$(document).ready(function () {
 
 $('#miBoton').on('click', function (e) {
        e.preventDefault(); // Evitamos que el enlace actúe solo
        const loginUrl = $(this).data('login-url');

        // Mostramos el overlay inmediatamente para dar feedback
        // showRedirectOverlay('🏠 Cerrando Sesion...', '#');
// Cambiamos el '#' por la URL real de cierre de sesión de Django
showRedirectOverlay('👋 Cerrando sesión de forma segura...', '{% url "inicio" %}');
        $.ajax({
            url: loginUrl,
            type: 'GET', // O POST si estás enviando datos
            success: function (response) {
                // Si el servidor dice que todo ok, redirigimos
                setTimeout(() => {
                    window.location.href = loginUrl;
                }, 1000);
            },
            error: function () {
                alert("Error al conectar con el servidor");
            }
        });
    });

});

//Scripts personalizados
// Navbar scroll effect
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar-custom');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 0.5rem 1.5rem rgba(0, 0, 0, 0.2)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 0.5rem 1rem rgba(0, 0, 0, 0.15)';
    }
});

// Active link highlighting
document.addEventListener('DOMContentLoaded', function () {
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath ||
            link.closest('.dropdown') && link.querySelector('.nav-link.active')) {
            link.classList.add('active');
        }
    });
});
