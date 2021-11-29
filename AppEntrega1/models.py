from django.db import models

# Create your models here.

class Vecinos(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero = models.IntegerField()
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    animal = models.CharField(max_length=20)
    edad = models.IntegerField()
    
class Casa(models.Model):
    escaleras = models.BooleanField()
    numero = models.IntegerField()
    cant_ventanas = models.IntegerField()