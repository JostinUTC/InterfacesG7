from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Profesor

# Create your views here.

def listar_profesores(request):
    # Traemos todos los profesores directamente de la base de datos relacional
    profesores = Profesor.objects.all()
    return render(request, 'profesores/listar_profesores.html', {'profesores': profesores})

def crear_profesor(request):
    if request.method == 'POST':
        nombre_profesor = request.POST.get("nombreProfesor")
        sueldo_profesor = request.POST.get("sueldoProfesor")
        curso_profesor = request.POST.get("cursoProfesor")
        
        # Validamos que no viajen vacíos antes de crear el objeto
        if nombre_profesor and sueldo_profesor and curso_profesor:
            Profesor.objects.create(
                nombre_profesor=nombre_profesor,
                sueldo_profesor=sueldo_profesor,
                curso_profesor=curso_profesor,
            )
            messages.success(request, 'Profesor añadido exitosamente')
            return redirect('listar_profesores')
        else:
            messages.error(request, 'Todos los campos son obligatorios')
            
    return render(request, 'profesores/crear_profesor.html')

def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    # CORRECCIÓN: Era messages.success, no profesor.success
    messages.success(request, 'Profesor eliminado exitosamente')
    return redirect('listar_profesores')

def editar_profesor(request, id):
    # Conseguimos el objeto único en singular
    profesor = Profesor.objects.get(id=id)
    
    if request.method == 'POST':
        # CORRECCIÓN: Usar 'profesor' (singular) que es la variable asignada arriba, no 'profesores'
        profesor.nombre_profesor = request.POST.get("nombreProfesor")
        profesor.sueldo_profesor = request.POST.get("sueldoProfesor")
        profesor.curso_profesor = request.POST.get("cursoProfesor")
        
        profesor.save()
        messages.success(request, 'El profesor se actualizó con éxito')
        return redirect('listar_profesores')
        
    # CORRECCIÓN: Aseguramos que busque la carpeta correcta en plural 'profesores/'
    return render(request, 'profesores/editar_profesor.html', {'profesores': profesor})