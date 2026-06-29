from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Directiva

# 1. LISTAR DIRECTIVA
def listar_directiva(request):
    # Traemos todos los registros de la base de datos
    directivas = Directiva.objects.all()
    return render(request, 'directiva/listar_directiva.html', {'directivas': directivas})

# 2. CREAR DIRECTIVA
def crear_directiva(request):
    if request.method == 'POST':
        # Capturamos los datos que vengan desde el formulario HTML
        nombre_directiva = request.POST.get("nombreDirectiva")
        cargo_directiva = request.POST.get("cargoDirectiva")
        presupuesto_directiva = request.POST.get("presupuestoDirectiva")
        num_integrantes = request.POST.get("numIntegrantes")

        # Guardamos el nuevo registro en MySQL
        Directiva.objects.create(
            nombre_directiva=nombre_directiva,
            cargo_directiva=cargo_directiva,
            presupuesto_directiva=presupuesto_directiva,
            num_integrantes=num_integrantes
        )
        messages.success(request, 'Miembro de la directiva creado exitosamente')
        return redirect('listar_directiva')
        
    return render(request, 'directiva/crear_directiva.html')

# 3. ELIMINAR DIRECTIVA
def eliminar_directiva(request, id):
    miembro = Directiva.objects.get(id=id)
    miembro.delete()
    messages.success(request, 'Registro eliminado exitosamente')
    return redirect('listar_directiva')

# 4. EDITAR DIRECTIVA
def editar_directiva(request, id):
    miembro = Directiva.objects.get(id=id)
    
    if request.method == 'POST':
        # Actualizamos las propiedades del objeto con lo que viene del formulario
        miembro.nombre_directiva = request.POST.get("nombreDirectiva")
        miembro.cargo_directiva = request.POST.get("cargoDirectiva")
        miembro.presupuesto_directiva = request.POST.get("presupuestoDirectiva")
        miembro.num_integrantes = request.POST.get("numIntegrantes")

        miembro.save()  # Guardamos los cambios en MySQL
        messages.success(request, 'La directiva se actualizó con éxito')
        return redirect('listar_directiva')
        
    # Pasamos el objeto bajo la clave 'directivas' para que coincida con tu HTML
    return render(request, 'directiva/editar_directiva.html', {'directivas': miembro})