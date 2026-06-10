from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login

def dashboard(request):
   return render(request, 'private/dashboard.html')
from django.contrib.auth.models import User
def listar_usuarios(request):
   usuarios = User.objects.all()
   contexto = {
         'usuarios': usuarios
   }
   return render(request, 'private/listar_usuarios.html', contexto)