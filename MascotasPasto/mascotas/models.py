from django.db import models

# Create your models here.
class Tipos(models.Model) :
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=5)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creatio') 
    fecha_modificacion = models.DateTimeField('Date update')

class Razas(models.Model) :
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=5)
    id_tipo = models.ForeignKey(Tipos, null = True, blank = True, on_delete = models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creatio') 
    fecha_modificacion = models.DateTimeField('Date update')

class Mascotas(models.Model) :
    codigo = models.CharField(max_length=20)
    id_tipo = models.ForeignKey(Tipos, null = True, blank = True, on_delete = models.CASCADE)
    id_raza = models.ForeignKey(Razas, null = True, blank = True, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=25)
    tiene_vacunas = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creatio') 
    fecha_modificacion = models.DateTimeField('Date update')