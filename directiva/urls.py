from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_directiva, name='listar_directiva'),
    path('crear_directiva/', views.crear_directiva, name='crear_directiva'),
    path('eliminar_directiva/<int:id>/', views.eliminar_directiva, name='eliminar_directiva'),
    path('editar_directiva/<int:id>/', views.editar_directiva, name='editar_directiva'),
]