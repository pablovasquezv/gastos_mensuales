from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="lista_gastos"),
    path('agregar/', views.agregar_gasto, name='agregar_gasto'),
    # RUTA PARA EDITAR: Usamos <int:id> para capturar el ID del gasto
    path('gasto/editar/<int:id>/', views.editar_gasto, name='editar_gasto'),
    path('gasto/eliminar/<int:id>/', views.eliminar_gasto, name='eliminar_gasto'),
]
