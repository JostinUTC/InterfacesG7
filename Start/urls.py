from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.hola, name='home'),
    path('contact/',views.contact, name='contact'),
    path('courses/',views.courses, name='courses'),
    path('elements/',views.elements, name='elements'),
    path('news/',views.news, name='news'),
    path('login/',views.login_view, name='login'),
    path('teachers/',views.teachers, name='teachers'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
