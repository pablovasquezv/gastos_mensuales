from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="lista_categorias"),
    path('create/', views.crear_categoria, name='nueva_categoria'),
    path('delete/<int:id_categoria>/', views.delete, name='eliminar_categoria'),
]
