from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ListaTareas(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    tarea=models.CharField(max_length=200)
    descripcion=models.TextField()
    hecho=models.BooleanField(default=False)
    fecha=models.DateField()

    class Meta:
        verbose_name='tarea'
        verbose_name_plural='tareas'
        ordering=['fecha']

    def __str__(self):
        return self.tarea