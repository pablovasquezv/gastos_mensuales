$(document).ready(function () {
    // ✅ jQuery: Selectores y eventos
    const $loginForm = $('#loginForm');
    const $alertContainer = $('#alert-container');
    const $togglePassword = $('#togglePassword');
    const $passwordField = $('#password');

    // ✅ Load + Botón
    // $(window).on('load', () => $('body').addClass('loaded'));
    // $('#miBoton').click(() => setTimeout(
    //     () => showRedirectOverlay('¡Saliendo de la Wallet!', 'index.html'), 1000
    // ));
    $('#miBoton').on('click', function (e) {
        e.preventDefault(); // Evitamos que el enlace actúe solo
        const loginUrl = $(this).data('login-url');

        // Mostramos el overlay inmediatamente para dar feedback
        showRedirectOverlay('🏠 Volviendo al inicio...', '#');

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
    // ✅ jQuery: Submit del formulario
    $loginForm.submit(function (e) {
        e.preventDefault();

        // ✅ jQuery: Obtener valores
        const email = $('#email').val().trim();
        const password = $('#password').val().trim();

        // 🚀 VER DATOS EN CONSOLA (mismo debug)
        console.log('=== DATOS CAPTURADOS ===');
        console.log('Email:', email);
        console.log('Password:', password);
        console.log('Email válido:', email === "alkewallet@gmail.com");
        console.log('Password válido:', password === "alkewallet123");
        console.log('========================');

        const emailCorrecto = "alkewallet@gmail.com";
        const passwordCorrecto = "alkewallet123";
     const urlDestino = $(this).data('url'); 
        // ✅ jQuery: Limpiar alertas
        $alertContainer.html('');

        if (email === emailCorrecto && password === passwordCorrecto) {
            // mostrarAlerta('success', '¡Inicio de sesión exitoso! Redirigiendo...');
            // Overlay profesional de 2 segundos
            // login.js
            // $('#miBoton').on('click', function() {
                // 1. Obtenemos la URL del atributo data-url (que será "/" según tu urls.py)
                //const urlDestino = $(this).data('url'); 
                console.log("Url", urlDestino);

                setTimeout(function() {
                    showRedirectOverlay('🏠 Volviendo al inicio...', urlDestino);
                    
                    // 2. Redirigimos a la URL pura de Django
                    window.location.href = urlDestino; 
                }, 1000);
            // });
            // setTimeout(() => {
            //     showRedirectOverlay('¡Bienvenido a Wallet!', 'menu.html');
            // }, 1000);
        } else {
            mostrarAlerta('danger', 'Credenciales incorrectas. Intenta nuevamente.');
        }
    });

    // ✅ jQuery: Función mostrarAlerta (igual)
    function mostrarAlerta(tipo, mensaje) {
        const alertaHtml = `
            <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
                ${mensaje}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `;
        $alertContainer.html(alertaHtml);
    }

    // ✅ jQuery: Toggle password (mejorado)
    // $togglePassword.on('click', function () {
    //     const type = $passwordField.attr('type') === 'password' ? 'text' : 'password';
    //     $passwordField.attr('type', type);
    //     $(this).text(type === 'password' ? 'Mostrar' : 'Ocultar');
    // });

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

    // $('#togglePassword').on('click', function () {
    //     const $passwordField = $('#password');
    //     const $eyeIcon = $('#passwordEye');

    //     // Animación suave
    //     $eyeIcon.transition({ scale: 1.2, duration: 150 });

    //     const isPassword = $passwordField.attr('type') === 'password';
    //     $passwordField.attr('type', isPassword ? 'text' : 'password');
    //     $eyeIcon.toggleClass('bi-eye bi-eye-slash');

    //     $eyeIcon.transition({ scale: 1, duration: 150 });
    // });



    // ✅ AGREGAR al final de tu script jQuery (después de mostrarAlerta)


});


