from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Casa, Mascota, Vecinos
from .forms import CasasFormulario, MascotaFormulario, VecinoFormulario

# Create your views here.

def inicio(request):
    return render(request, 'AppEntrega1/inicio.html', {})

def lista_casas(request):
    casas = None
    error = None
    if request.method == 'GET':
        numero = request.GET.get('numero', '')
        if numero == '':
            casas = Casa.objects.all()
        else:
            try:
                numero = int(numero)
                casas = Casa.objects.filter(numero=numero)
            except:
                error = 'Debes ingresar un numero entero'
            
    return render(request, 'AppEntrega1/lista_casas.html', {'casas': casas, 'error': error})

def crear_casa(request):
    
    if request.method == 'POST':
        formulario = CasasFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            casa = Casa(escaleras=datos['escaleras'], numero=datos['numero'], cant_ventanas=datos['cant_ventanas'])                      
            casa.save()
            # return render(request, 'AppEntrega1/lista_casas.html', {'casas': None, 'error': None})
            return redirect('Casas')                                
    
    formulario = CasasFormulario()
    return render(request, 'AppEntrega1/formulario_casa.html', {'formulario': formulario})

def lista_mascotas(request):
    mascotas = None
    error = None
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        if nombre == '':
            mascotas = Mascota.objects.all()
        else:
            mascotas = Mascota.objects.filter(nombre=nombre)
            
    return render(request, 'AppEntrega1/lista_mascotas.html', {'mascotas': mascotas, 'error': error})

def crear_mascota(request):
    
    if request.method == 'POST':
        formulario1 = MascotaFormulario(request.POST)
        
        if formulario1.is_valid():
            datos1 = formulario1.cleaned_data
            mascota = Mascota(nombre=datos1['nombre'], animal=datos1['animal'], edad=datos1['edad'])                      
            mascota.save()
            return redirect('Mascotas')                                
    
    formulario1 = MascotaFormulario()
    return render(request, 'AppEntrega1/formulario_mascota.html', {'formulario1': formulario1})


def lista_vecinos(request):
    vecinos = None
    error = None
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        if nombre == '':
            vecinos = Vecinos.objects.all()
        else:
            vecinos = Vecinos.objects.filter(nombre=nombre)
            
    return render(request, 'AppEntrega1/lista_vecinos.html', {'vecinos': vecinos, 'error': error})

def crear_vecino(request):
    
    if request.method == 'POST':
        formulario2 = VecinoFormulario(request.POST)
        
        if formulario2.is_valid():
            datos2 = formulario2.cleaned_data
            vecinos = Vecinos(nombre=datos2['nombre'], apellido=datos2['apellido'], numero=datos2['numero'])                      
            vecinos.save()
            return redirect('Vecinos')                                
    
    formulario2 = VecinoFormulario()
    return render(request, 'AppEntrega1/formulario_vecino.html', {'formulario2': formulario2})
