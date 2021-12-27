from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
# from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate

from .forms import RegistroUsuarioForm, EditarUsuarioForm, AvatarForm

from .models import Casa, Mascota, Vecinos, Avatar
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

def crear_casa(request, id):
    id_casa = 0
    try:
        casa = Casa.objects.get(id=id)
        id_casa = casa.id
    except Exception as e:
        casa = None
            
    if request.method == 'POST':
        formulario = CasasFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            if casa:
                casa.escaleras = datos['escaleras']
                casa.numero = datos['numero']
                casa.cant_ventanas = datos['cant_ventanas']
            else:    
                casa = Casa(escaleras=datos['escaleras'], numero=datos['numero'], cant_ventanas=datos['cant_ventanas'])                      
            
            casa.save()
            # return render(request, 'AppEntrega1/lista_casas.html', {'casas': None, 'error': None})
            return redirect('Casas')                                
    elif casa:
        formulario = CasasFormulario({'escaleras': casa.escaleras,'numero': casa.numero,'cant_ventanas': casa.cant_ventanas})
    else:
        formulario = CasasFormulario()
    return render(request, 'AppEntrega1/formulario_casa.html', {'formulario': formulario, 'idcasa': id_casa})

@login_required
def eliminar_casa(request, id):
    casas = Casa.objects.get(id=id)
    casas.delete()
    return render(request, 'AppEntrega1/casa_eliminada.html', {'casas': casas})

def lista_mascotas(request):
    mascota = None
    error = None
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        if nombre == '':
            mascota = Mascota.objects.all()
        else:
            try:
                nombre = str(nombre)
                mascota = Mascota.objects.filter(nombre=nombre)
            except:
                error = 'Debes ingresar un nombre valido'
            
    return render(request, 'AppEntrega1/lista_mascotas.html', {'mascota': mascota, 'error': error})

def crear_mascota(request, id):
    id_mascota = 0
    try:
        mascota = Mascota.objects.get(id=id)
        id_mascota = mascota.id
    except Exception as e:
        mascota = None
        
    if request.method == 'POST':
        formulario1 = MascotaFormulario(request.POST)
        
        if formulario1.is_valid():
            datos1 = formulario1.cleaned_data
            if mascota:
                mascota.nombre = datos1['nombre']
                mascota.animal = datos1['animal']
                mascota.edad = datos1['edad']
            else:    
                mascota = Mascota(nombre=datos1['nombre'], animal=datos1['animal'], edad=datos1['edad'])                      
        
            mascota.save()
            return redirect('Mascotas')    
                                
    elif mascota:
        formulario1 = MascotaFormulario({'nombre': mascotas.nombre,'animal': mascota.animal,'edad': mascota.edad})
    else:
        formulario1 = MascotaFormulario()
    return render(request, 'AppEntrega1/formulario_mascota.html', {'formulario1': formulario1, 'idmascota': id_mascota})    

@login_required
def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return render(request, 'AppEntrega1/mascota_eliminada.html', {'mascota': mascota})

# def lista_vecinos(request):
#     vecinos = None
#     error = None
#     if request.method == 'GET':
#         nombre = request.GET.get('nombre', '')
#         if nombre == '':
#             vecinos = Vecinos.objects.all()
#         else:
#             vecinos = Vecinos.objects.filter(nombre=nombre)
            
#     return render(request, 'AppEntrega1/lista_vecinos.html', {'vecinos': vecinos, 'error': error})

# def crear_vecino(request, id):
#     id_vecino = 0
#     try:
#         vecino = Vecinos.objects.get(id=id)
#         id_vecino = vecino.id
#     except Exception as e:
#         vecino = None
    
#     if request.method == 'POST':
#         formulario2 = VecinoFormulario(request.POST)
        
#         if formulario2.is_valid():
#             datos2 = formulario2.cleaned_data
#             vecinos = Vecinos(nombre=datos2['nombre'], apellido=datos2['apellido'], numero=datos2['numero'])                      
#             vecinos.save()
#             return redirect('Vecinos')                                
    
#     formulario2 = VecinoFormulario()
#     return render(request, 'AppEntrega1/formulario_vecino.html', {'formulario2': formulario2})

# def eliminar_vecino(request, id):
#     vecinos = Vecinos.objects.get(id=id)
#     vecinos.delete()
#     return render(request, 'AppEntrega1/vecino_eliminado.html', {'vecinos': vecinos})

class VecinosCreateView(CreateView):
    model = Vecinos
    success_url = 'vecinos/lista/'
    fields = ['nombre', 'apellido', 'numero']
    template_name = 'AppEntrega1/formulario_vecino.html'
    
class VecinosDeleteView(DeleteView):
    model = Vecinos
    success_url = 'AppEntrega1/vecinos/lista'
    
class VecinosDetailView(DetailView):
    model = Vecinos
    template_name = 'AppEntrega1/detalle_vecino.html'
    
class VecinosListView(LoginRequiredMixin, ListView):
    model = Vecinos
    template_name = 'AppEntrega1/lista_vecinos.html'

def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
    
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, 'AppEntrega1/inicio.html', {'tiene_mensaje': True, 'mensaje': 'Estas logueado!'})
            else:
                return render(request, 'AppEntrega1/login.html', {'form': form, 'mensaje': 'Error, datos incorrectas.', 'error': True})
        
        else:
            form.initial = {'username': None, 'password': None}
            return render(request, 'AppEntrega1/login.html', {'form': form, 'mensaje': 'Error, mal formato de los datos.', 'error': True})    
    
    form = AuthenticationForm()
    
    return render(request, 'AppEntrega1/login.html', {'form': form, 'mensaje': '', 'error': False})

def register_request(request):
    
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'AppEntrega1/inicio.html', {'tiene_mensaje': True, 'mensaje': f'Se creo el {username}' })
    
    form = RegistroUsuarioForm()
    
    return render(request, 'AppEntrega1/register.html', {'form': form, 'mensaje': '', 'error': False})

@login_required
def editar_user(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST)
        
        if form.is_valid():
            
            datos = form.cleaned_data
            
            usuario.email = datos['email']
            usuario.password1 = datos['password1']
            usuario.password2 = datos['password2']
            usuario.last_name = datos['last_name']
            usuario.first_name = datos['first_name']
            
            usuario.save()
            
            return render(request, 'AppEntrega1/inicio.html', {'tiene_mensaje': True, 'mensaje': f'Se edito correctamente.' })
    else:
        form = EditarUsuarioForm(initial={'first_name': usuario.first_name, 'last_name': usuario.last_name, 'email': usuario.email})
    
    return render(request, 'AppEntrega1/editar_user.html', {'form': form})

@login_required
def editar_avatar(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            # avatar = Avatar(user=usuario, avatar=form.cleaned_data['avatar'])
            
            avatar = Avatar.objects.get(user=usuario)
            avatar.avatar = form.cleaned_data['avatar']
            avatar.save()
            
            return render(request, 'AppEntrega1/inicio.html',
                          {'tiene_mensaje': True, 'mensaje': f'Se cargo correctamente el avatar.', 'url_avatar': avatar.avatar.url})
    else:
        form = AvatarForm()
    
    return render(request, 'AppEntrega1/editar_avatar.html', {'form': form})


def error_404(request, exception):
        data = {}
        return render(request,'AppEntrega1/login.html', data)