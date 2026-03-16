$(document).ready(function() {
    // Toggle password visibility
    $('#togglePassword').on('click', function() {
        const $passwordField = $('#password');
        const $eyeIcon = $('#passwordEye');
        
        // Verificar que los elementos existan
        if (!$passwordField.length || !$eyeIcon.length) {
            console.error('Elementos de password no encontrados');
            return;
        }

        // Toggle tipo de input
        const isPassword = $passwordField.attr('type') === 'password';
        $passwordField.attr('type', isPassword ? 'text' : 'password');
        
        // Cambiar icono
        $eyeIcon.toggleClass('bi-eye bi-eye-slash');
    });

    // Prevenir envío vacío (evita el error trim())
    $('#loginForm').on('submit', function(e) {
        const username = $('#username').val();
        const password = $('#password').val();
        
        if (!username || !username.trim()) {
            e.preventDefault();
            alert('Por favor ingresa tu usuario');
            return false;
        }
        
        if (!password || !password.trim()) {
            e.preventDefault();
            alert('Por favor ingresa tu contraseña');
            return false;
        }
    });
});
