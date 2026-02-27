from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# def inicio(request):
#     return HttpResponse("Hola desde Django")    
def index(request):
    return render(request, 'listagastos.html')