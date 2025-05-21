from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import ListaTareas
from .forms import RegistrarTarea
# Create your views here.


@login_required(login_url='users:login')
def inicio(request):
    tareas = ListaTareas.objects.filter(usuario=request.user).order_by('fecha')
    valor = {
        'tareas': tareas
    }
    return render(request,'toDoApp/inicio.html',valor)

@login_required(login_url='users:login')
def registrarTareas(request):
    if request.method !='POST':
        form=RegistrarTarea()
    else:
        form=RegistrarTarea(data=request.POST)
        if form.is_valid():
            nuevaTarea=form.save(commit=False)
            nuevaTarea.usuario=request.user
            nuevaTarea.save()
            return redirect('inicio')
    valor={
        'form':form
    }
    return render(request,'toDoApp/registrarTarea.html',valor)


#editar tarea
@login_required(login_url='users:login')
def editTarea(request,tarea_id):
    tarea=ListaTareas.objects.get(id=tarea_id)

    if request.method !='POST':
        form=RegistrarTarea(instance=tarea)
    else:
        form=RegistrarTarea(instance=tarea,data=request.POST)
        if form.is_valid():
            tareaEditar=form.save(commit=False)
            tareaEditar.usuario=request.user
            tareaEditar.save()
            return redirect('inicio')
    valor={
        'form':form,
        'tarea':tarea
    }
    return render(request,'toDoApp/editarTarea.html',valor)

@login_required(login_url='users:login')
def verTarea(request,tarea_id):
    tarea = ListaTareas.objects.get(id=tarea_id)
    valor = {
        'tarea':tarea,
        'tareas': tarea.tarea,
        'descripcion':tarea.descripcion,
        'hecho':tarea.hecho,
        'fecha':tarea.fecha
    }
    return render(request, 'toDoApp/verTarea.html', valor)


