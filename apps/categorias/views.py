from django.shortcuts import render, redirect,get_object_or_404

from apps import categorias
from .forms import CategoriaForm
from .models import Categoria
from django.contrib import messages
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

def delete(requests, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    try:
        categoria.delete()
        messages.success(requests, "Categoria eliminada exitosamente!!")
        return redirect('lista_categorias')
    except Exception as e:
        messages.error(requests, f"Error al eliminar la Categoria: {str(e)}")