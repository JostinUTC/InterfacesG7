from django.urls import path
from . import views
urlpatterns = [
    path('', views.listar_profesores, name='listar_profesores'),
    path('crear_materias/', views.crear_materias, name='crear_materias'),
    path('eliminar_materia/<int:id>/', views.eliminar_materia, name='eliminar_materia'),
    path('editar_materia/<int:id>/', views.editar_materia, name='editar_materia')
]