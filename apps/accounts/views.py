from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
    
def login(request):
    return render(request, 'account/login.html')
    # return render(request, 'acount/student_list.html')