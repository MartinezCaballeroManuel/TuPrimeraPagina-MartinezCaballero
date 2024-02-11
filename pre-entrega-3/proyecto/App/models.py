from django.db import models

# Create your models here.

class Educacion(models.Model):

    nivel = models.CharField(max_length=40)
    establecimiento = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)

class Actividades(models.Model):

    tipo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()

class Laboral(models.Model):

    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    rubro = models.CharField(max_length=30)