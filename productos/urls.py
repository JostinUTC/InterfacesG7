from django.urls import path
from . import views
urlpatterns = [
    path('', views.listar_materias, name='listar_materias'),
]