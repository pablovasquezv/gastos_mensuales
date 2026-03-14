from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required    
def index(request):
    return render(request, 'index.html')
    # return render(request, 'acount/student_list.html')


@login_required
def home(request):
    # Esta sí es privada (usando el decorador o el middleware)
    return render(request, 'core/home.html')