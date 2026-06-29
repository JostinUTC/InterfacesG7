from django.urls import path
from . import views
urlpatterns = [
    path('', views.listar_profesores, name='listar_profesores'),
    path('crear_profesor/', views.crear_profesor, name='crear_profesor'),
    path('eliminar_profesor/<int:id>/', views.eliminar_profesor, name='eliminar_profesor'),
    path('editar_profesor/<int:id>/', views.editar_profesor, name='editar_profesor')
]