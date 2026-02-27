$(document).ready(function () {
    // 🎨 Micro-interacciones
    $('.hero-card').hover(
        () => $('.hero-card').css('transform', 'translateY(-15px) scale(1.02)'),
        () => $('.hero-card').css('transform', 'translateY(0) scale(1)')
    );

    // 🌄 Parallax
    $(window).scroll(() => {
        $('.wallet-logo').css('transform',
            `translateY($($(window).scrollTop() * 0.5}px)`
        );
    });

    // ✅ Load + Botón
    // $('#miBoton').on('click', function () {
    //     // Obtenemos la URL del atributo que pusimos en el HTML
    //     const loginUrl = $(this).data('login-url');

    //     setTimeout(function () {
    //         showRedirectOverlay('🔐 Bienvenido...', loginUrl);
    //     }, 1000);
    // });

    //✅ Load + Botón
    $('#miBoton').on('click', function (e) {
        e.preventDefault(); // Evitamos que el enlace actúe solo
        const loginUrl = $(this).data('login-url');

        // Mostramos el overlay inmediatamente para dar feedback
        showRedirectOverlay('🌐 Conectando...', '#');

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
// ✅ Define la función FUERA de cualquier $(document).ready
function miFuncionDeLogin(urlDestino) {
    $('#miBoton').on('click', function (e) {
        e.preventDefault(); // Evita que el botón haga cosas raras antes de tiempo

        setTimeout(function () {
            // Tu función de overlay
            showRedirectOverlay('🔐 Redirigiendo...', urlDestino);

            // Opcional: Si quieres que realmente cambie de página después de la leyenda:
            // window.location.href = urlDestino;
        }, 1000);
    });
}