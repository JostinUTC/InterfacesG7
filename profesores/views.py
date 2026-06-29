from django.shortcuts import render

# Create your views here.
def listar_materias(request):
   profesores = profesores.objects.all()
   return render(request, 'profesores/listar_profesor.html', {'profesores': profesores})
def crear_profesor(request):
   if request.method== 'POST':
      nombre_profesor = request.POST.get("nombreProfesor")
      sueldo_profesor = request.POST.get("sueldoProfesor")
      curso_profesor = request.POST.get("cursoProfesor")
    

      Profesores.objects.create(
         nombre_profesor = nombre_profesor,
         sueldo_profesor = sueldo_profesor ,
         curso_profesor = curso_profesor,

      )
      messages.success(request, 'Profesor añadido exitosamente')
      return redirect('listar_profesores')
   return render(request, 'profesores/crear_profesor.html')
def eliminar_profesor(request, id):
   profesores = profesores.objects.get(id=id)
   profesores.delete()
   profesores.success(request, 'profesor eliminado exitosamente')
   return redirect('listar_profesores')
def editar_profesore(request, id):
   profesores = profesores.objects.get(id=id)
   if request.method == 'POST':
      profesores.nombre_profesor = request.POST.get("nombreProfesor")
      profesores.sueldo_profesor = request.POST.get("sueldoProfesor")
      profesores.curso_profesor = request.POST.get("cursoProfesor")
   

      profesores.save()
      messages.success(request, 'La materia se actualizo con exito')
      return redirect('listar_profesores')
   return render(request, 'profesor/editar_profesor.html', {'profesores': profesores})