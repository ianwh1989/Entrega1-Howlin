from django import forms

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