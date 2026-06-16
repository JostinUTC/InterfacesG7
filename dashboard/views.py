from pyexpat.errors import messages

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
def crear_usuario(request):
   if request.method == 'post':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      #si no existe el usuario
      if User.object.filter(username=username).exists():
         messages.error(request, 'El usuario ya existe')
         return render (request, 'private/crear_usuario.html')
      #si no existe el correo
      if User.object.filter(email=email).exists():
         messages.error(request, 'El correo ya existe')
         return render (request, 'private/crear_usuario.html')
      #crear usuario
      User.objects.create_user(username=username,email=email,password=password)
      messages.success(request, 'Usuario creado exitosamente')
      return render(request, 'private/listar_usuarios.html')
   return render(request, 'private/crear_usuario.html')
   