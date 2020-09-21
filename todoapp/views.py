from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from todoapp.models import Tarea, Categoria


def tareas(request):  # the index view
    tareas = Tarea.objects.all()  # quering all todos with the object manager
    categorias = Categoria.objects.all()  # getting all categories with object manager

    if request.method == "GET":
        return render(request, "todoapp/index.html", {"tareas": tareas, "categorias": categorias})
