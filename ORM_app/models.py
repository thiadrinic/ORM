from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    direccion = models.CharField(max_length=160)
    edad = models.IntegerField()
    fechanac = models.DateField()
    email = models.EmailField()

class Docente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    direccion = models.CharField(max_length=160)
    edad = models.IntegerField()
    fechanac = models.DateField()
    email = models.EmailField()

