from ORM_app.models import Alumno

def Listar():
    alumnos = Alumno.objects.all()
    return alumnos

def Crear(alumno):
    Alumno.objects.create(
        nombre=alumno
    )

def Eliminar(alumno):
    Alumno.objects.filter(
        nombre=alumno
    ).delete()

def Editar(alumno):
    Alumno.objects.filter(
        nombre=alumno
    ).update(
        nombre=alumno
    )
