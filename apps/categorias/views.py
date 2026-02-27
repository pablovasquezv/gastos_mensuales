from django.shortcuts import render, redirect
from .forms import CategoriaForm

# Create your views here.

from django.http import HttpResponse
# def inicio(request):
#     return HttpResponse("Hola desde Django")    
def index(request):
    return render(request, 'listacategorias.html')


def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # O a la lista de categorías
    else:
        form = CategoriaForm()
    
    return render(request, 'categoria/crear_categoria.html', {'form': form})