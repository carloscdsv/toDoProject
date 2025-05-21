from django import forms
from .models import ListaTareas


class RegistrarTarea(forms.ModelForm):
    class Meta:
        model=ListaTareas
        fields=['tarea','descripcion','hecho','fecha']
        labels={
            'tarea':'tarea',
            'descripcion':'descripcion',
            'hecho':'hecho',
            'fecha':'fecha (año-mes-dia)'
               }

