from django.db import models

# Create your models here.


class Paises(models.Model) :
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=5)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creatio') 
    fecha_modificacion = models.DateTimeField('Date update')

class Ciudades(models.Model) :
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=5)
    id_pais = models.ForeignKey(Paises, null = True, blank = True, on_delete = models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creatio') 
    fecha_modificacion = models.DateTimeField('Date update')

class Afiliados(models.Model) :
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    numero_movil = models.BigIntegerField()
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=70)
    id_ciudad = models.ForeignKey(Ciudades, null = True, blank = True, on_delete = models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creatio') 
    fecha_modificacion = models.DateTimeField('Date update')