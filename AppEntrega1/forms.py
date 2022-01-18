from django import forms
import django

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class CasasFormulario(forms.Form):
    escaleras=forms.BooleanField()
    numero=forms.IntegerField(required=True)
    cant_ventanas=forms.IntegerField()

class MascotaFormulario(forms.Form):    
    nombre=forms.CharField(required=True)
    animal=forms.CharField(required=True)
    edad=forms.IntegerField()

class VecinoFormulario(forms.Form):    
    nombre=forms.CharField(required=True)
    apellido=forms.CharField(required=True)
    numero=forms.IntegerField()
    
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        help_texts = {k: '' for k in fields}
        

class EditarUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Editar Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
        
class AvatarForm(forms.Form):
    avatar = forms.ImageField()