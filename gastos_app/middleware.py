from django.shortcuts import redirect
from django.urls import reverse

from django.shortcuts import redirect
from django.urls import reverse

class LoginRequieredMiddleware:
    """
    Middleware para proteger la aplicación: obliga a los usuarios a estar
    autenticados para acceder a cualquier ruta que no sea pública.
    """
    def __init__(self, get_response):
        # Se ejecuta una sola vez cuando el servidor arranca.
        # Guarda la función que permite que la petición siga su camino.
        self.get_response = get_response

    def __call__(self, request):
        # 1. Obtenemos la URL de la página de inicio de sesión (Login)
        login_url = reverse('inicio')

        # 2. Definimos una "Lista Blanca" de rutas que NO requieren estar logueado.
        # Es fundamental incluir el login aquí para evitar un bucle infinito de redirecciones.
        public_paths = [
            login_url,
            reverse('register'),
            reverse('login'),
            '/admin/',     # Permitir acceso al panel de administración (Django tiene su propia gestión)
            '/static/',    # Permitir carga de archivos CSS, JS e imágenes
            '/media/',     # Permitir carga de archivos subidos por usuarios
        ] 
        
        # 3. Verificamos si la URL a la que el usuario intenta entrar está en la "Lista Blanca".
        # 'any' devuelve True si la ruta actual (request.path) comienza con alguno de los 'public_paths'.
        is_public_path = any(request.path.startswith(path) for path in public_paths)

        # 4. EVALUACIÓN DE SEGURIDAD:
        # Si el usuario NO está autenticado Y la ruta NO es pública...
        if not request.user.is_authenticated and not is_public_path:
            # Lo redirigimos al login.
            # '?next={request.path}' sirve para que, tras loguearse, el usuario vuelva a donde intentaba ir.
            return redirect(f"{login_url}?next={request.path}")

        # 5. Si todo está en orden, permitimos que la petición continúe hacia la vista correspondiente.
        return self.get_response(request)   