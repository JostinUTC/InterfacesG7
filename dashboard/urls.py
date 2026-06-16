from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('crear_usuarios/', views.crear_usuarios, name='crear_usuarios'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
]