from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    # 1. Si ya está logueado, lo mandamos al inicio
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        # 2. Capturamos los datos directamente de los 'name' de tus inputs
        # Usamos .get() para que si el campo no existe, devuelva None y no rompa la app
        username_post = request.POST.get("username")
        password_post = request.POST.get("password")

        # 3. Validación básica: que no vengan vacíos
        if not username_post or not password_post:
            messages.warning(request, "Por favor, completa todos los campos.")
            print("Por favor, completa todos los campos.")
            return render(request, "account/login.html")

        # 4. Intentamos la autenticación
        user = authenticate(request, username=username_post, password=password_post)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            # 5. Error de credenciales
            messages.error(request, "Usuario o contraseña incorrectos.")
    
    # Si es GET o si falló el login, simplemente carga el HTML
    return render(request, "account/login.html")

def logout_view(request):
    logout(request)
    return redirect("inicio")