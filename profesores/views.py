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
    

      Profesor.objects.create(
         nombre_profesor = nombre_profesor,
         sueldo_profesor = sueldo_profesor ,
         curso_profesor = curso_profesor,

      )
      messages.success(request, 'Profesor añadido exitosamente')
      return redirect('listar_profesores')
   return render(request, 'profesores/crear_profesor.html')