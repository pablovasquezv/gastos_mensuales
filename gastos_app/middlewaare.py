from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
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
    # Definimos las rutas públicas EXACTAS (solo estas dos)
    # Cambiamos reverse('inicio') por el nombre real de tu ruta de LOGIN
    # (Asumiendo que tu login se llama 'login')
    
        try:
            login_url = reverse('login') 
            register_url = reverse('register')
        except:
            login_url = '/accounts/login/' # Ruta por defecto si falla el reverse
            register_url = '/accounts/register/'

        # 1. Rutas que son exactamente iguales y permitidas
        exact_public_paths = [
            login_url,
            register_url,
            reverse('inicio'), # La landing page pública ('')
        ]

        # 2. Rutas que empiezan por (para archivos y admin)
        prefix_public_paths = ['/admin/', '/static/', '/media/']

        # Verificamos si la ruta actual coincide exactamente o por prefijo
        is_public = (request.path in exact_public_paths) or \
                    any(request.path.startswith(p) for p in prefix_public_paths)

        # SEGURIDAD: Si no está logueado y NO es una ruta pública... ¡AL LOGIN!
        if not request.user.is_authenticated and not is_public:
            return redirect(f"{login_url}?next={request.path}")

        return self.get_response(request)