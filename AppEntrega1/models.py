from django.db import models

# Create your models here.

class Vecinos(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero = models.IntegerField()
    
    def __str__(self):
        return f'El vecino se llama {self.nombre}'
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    animal = models.CharField(max_length=20)
    edad = models.IntegerField()
    
    def __str__(self):
        return f'La mascota se llama {self.nombre}'
    
class Casa(models.Model):
    escaleras = models.BooleanField()
    numero = models.IntegerField()
    cant_ventanas = models.IntegerField()
    
    def __str__(self):
        return f'Casa numero {self.numero}'
