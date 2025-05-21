from django.urls import path,include
from . import views


urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('registrarTarea/',views.registrarTareas,name='registrarTarea'),
    path('editarTarea/<int:tarea_id>/',views.editTarea,name='editarTarea'),
    path('verTarea/<int:tarea_id>/',views.verTarea,name='verTarea'),

]