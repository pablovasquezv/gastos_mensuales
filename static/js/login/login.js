$(document).ready(function () {
    // ✅ jQuery: Toggle password con ICONOS (reemplaza tu función actual)
    $('#togglePassword').on('click', function () {
        const $passwordField = $('#password');
        const $eyeIcon = $('#passwordEye');

        // Animación suave
        // Animación ESCALA con jQuery animate()
        $eyeIcon.animate({ opacity: 0.5 }, 100, function () {
            const isPassword = $passwordField.attr('type') === 'password';
            $passwordField.attr('type', isPassword ? 'text' : 'password');
            $eyeIcon.toggleClass('bi-eye bi-eye-slash');
            $eyeIcon.animate({ opacity: 1 }, 100);
        });
        // Toggle tipo de input
        const isPassword = $passwordField.attr('type') === 'password';
        $passwordField.attr('type', isPassword ? 'text' : 'password');

        // ✅ CAMBIAR ICONO (NO texto)
        if (isPassword) {
            // Mostrar → Ojo abierto
            $eyeIcon.removeClass('bi-eye-slash').addClass('bi-eye');
        } else {
            // Ocultar → Ojo tachado
            $eyeIcon.removeClass('bi-eye').addClass('bi-eye-slash');
        }
    });

});


