from django.contrib import messages
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
def crear_usuarios(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      #si no existe el usuario
      if User.objects.filter(username=username).exists():
         messages.error(request, 'El usuario ya existe')
         return render (request, 'private/crear_usuarios.html')
      #si no existe el correo
      if User.objects.filter(email=email).exists():
         messages.error(request, 'El correo ya existe')
         return render (request, 'private/crear_usuarios.html')
      #crear usuario
      User.objects.create_user(username=username,email=email,password=password)
      messages.success(request, 'Usuario creado exitosamente')
      return redirect('listar_usuarios')
   return render(request, 'private/crear_usuarios.html')
def eliminar_usuario(request, id):
   usuario = User.objects.get(id=id)
   usuario.delete()
   messages.success(request, 'Usuario eliminado exitosamente')
   return redirect('listar_usuarios')
def editar_usuario(request, id):#metodo editar
   usuario = User.objects.get(id=id)
   if request.method == 'POST':
      username = request.POST.get("username_edit")
      email = request.POST.get("email_edit")
      password = request.POST.get("password_edit")
      #verificar si existe el username
      if User.objects.filter(username=username).exclude(id=id).exists():
         messages.error(request, 'El usuario ya esta registrado')
         return render (request, 'private/editar_usuario.html', {"usuario": usuario})
      if User.objects.filter(email=email).exclude(id=id).exists():
         messages.error(request, 'El correo ya existe')
         return render (request, 'private/editar_usuario.html', {"usuario": usuario})
      #actualizar datos
      usuario.username = username
      usuario.email = email
      if password:
         usuario.set_password(password)
         
      usuario.save()
      messages.success(request, 'El registro se actualizo con existo')
      return redirect('listar_usuarios')
   contexto = {
      "usuario": usuario
   }
   return render (request, 'private/editar_usuario.html', contexto)