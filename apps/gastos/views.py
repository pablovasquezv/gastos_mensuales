from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Gasto
from django.http import HttpResponse
from django.contrib import messages
from .forms import GastoForm
# def inicio(request):
#     return HttpResponse("Hola desde Django")    

def index(request):
    gastos = Gasto.objects.all()
    # Debes agregar el diccionario de contexto como tercer argumento
    return render(request, 'gasto/lista_gastos.html', {'gastos': gastos})

def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.user = request.user
            gasto.save()
            messages.success(request, '✅ Gasto registrado correctamente')
            return redirect('lista_gastos')
    else:
        form = GastoForm()
    return render(request, 'gasto/crear_gasto.html', {'form': form})


def editar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id, user=request.user)
    
    if request.method == 'POST':
        # Pasamos la 'instance' para que Django sepa que es una actualización
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('lista_gastos')
    else:
        # Cargamos el formulario con los datos actuales
        form = GastoForm(instance=gasto)
    
    return render(request, 'gasto/editar.html', {'form': form, 'gasto': gasto})

def eliminar_gasto(request, id):
    # Buscamos el gasto que pertenezca al usuario logueado
    gasto = get_object_or_404(Gasto, id=id, user=request.user)
    
    if request.method == 'POST' or request.method == 'GET': # GET para pruebas rápidas, POST es mejor por seguridad
        gasto.delete()
        messages.success(request, "¡Gasto eliminado correctamente!")
    
    return redirect('lista_gastos')