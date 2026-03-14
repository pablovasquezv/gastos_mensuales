from django.urls import path
from . import views
urlpatterns = [
    path('inicio/', views.index, name='inicio'),      # Página pública (Landing)
    path('home/', views.home, name='home'),    # Dashboard privado
]