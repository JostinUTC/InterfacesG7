from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
def hola(request):
# Create your views here.
   return render(request, 'index.html')
def contact(request):
   return render(request, 'contact.html')
def courses(request):
   return render(request, 'courses.html')
def elements(request):
   return render(request, 'elements.html')
def news(request):
   return render(request, 'news.html')
def teachers(request):
   return render(request, 'teachers.html')

def login_view(request):
    mensaje = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            mensaje = 'Inicio de sesión exitoso'
            return redirect('dashboard')
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render(request, 'login.html', {'mensaje': mensaje})