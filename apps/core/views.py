from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
    
def index(request):
    return render(request, 'index.html')
    # return render(request, 'acount/student_list.html')

def home(request):
    # Esta sí es privada (usando el decorador o el middleware)
    return render(request, 'core/home.html')