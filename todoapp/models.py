from django.db import models

# Create your models here.
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre  # name to be shown when called

class Tarea(models.Model):  # Todolist able name that inherits models.Model
    titulo = models.CharField(max_length=250)  # un varchar
    contenido = models.TextField(blank=True)  # un text
    fecha_creación = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # un date
    categoria = models.ForeignKey(Categoria, default="general", on_delete=models.CASCADE)  # la llave foránea

    def __str__(self):
        return self.titulo  # name to be shown when called

