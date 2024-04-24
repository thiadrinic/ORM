from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def alumno(request):
    return render(request, 'alumnos.html')

def docente(request):
    return render(request, 'docentes.html')

