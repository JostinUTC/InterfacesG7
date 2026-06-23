from django.shortcuts import redirect, render
from .models import Materia
def listar_materias(request):
   materias = Materia.objects.all()
   return render(request, 'productos/listar_materias.html', {'materias': materias})
# Create your views here.
def crear_materias(request):
   if request.method== 'POST':
      nombre_materia = request.POST.get("")
      precio_materia = request.POST.get("")
      creditos_materia = request.POST.get("")
      num_estudiantes_materia = request.POST.get("")

      Materia.objects.create(
         nombre_materia = nombre_materia,
         precio_materia = precio_materia,
         creditos_materia = creditos_materia,
         num_estudiantes_materia = num_estudiantes_materia

      )
      return redirect('listar_materias')
   return render(request, 'productos/crear_materias.html')