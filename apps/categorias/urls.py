from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="lista_categorias"),
     path('create/', views.crear_categoria, name='nueva_categoria'),
]
