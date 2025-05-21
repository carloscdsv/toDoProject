from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def register(request):
    if request.method !='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            nuevo_usuario=form.save()
            login(request,nuevo_usuario)#para iniciar usuario
            return redirect('inicio')
    valor={
        'form':form
    }
    return render(request,'registration/register.html',valor)


