from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vecinos(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero = models.IntegerField()
    
    def __str__(self):
        return f'El vecino se llama {self.nombre} {self.apellido}'
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    animal = models.CharField(max_length=20)
    edad = models.IntegerField()
    
    def __str__(self):
        return f'La mascota se llama {self.nombre} y es un {self.animal}'
    
class Casa(models.Model):
    escaleras = models.BooleanField()
    numero = models.IntegerField()
    cant_ventanas = models.IntegerField()
    
    def __str__(self):
        return f'Casa numero {self.numero} tiene {self.cant_ventanas} ventanas'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', default='/imagenDefault.png', null=True, blank=True)
    
    