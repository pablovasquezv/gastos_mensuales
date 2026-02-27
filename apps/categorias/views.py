from django.shortcuts import render, redirect

from apps import categorias
from .forms import CategoriaForm
from .models import Categoria
# Create your views here.

from django.http import HttpResponse
# def inicio(request):
#     return HttpResponse("Hola desde Django")    
def index(request):
    categorias = Categoria.objects.all()
    # Debes agregar el diccionario de contexto como tercer argumento
    return render(request, 'categoria/listacategorias.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # O a la lista de categorías
    else:
        form = CategoriaForm()
    
    return render(request, 'categoria/crear_categoria.html', {'form': form})