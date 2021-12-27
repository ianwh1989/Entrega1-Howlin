from django import template
from django.urls.conf import path
from .views import inicio, lista_casas, lista_mascotas, crear_casa, crear_mascota, eliminar_casa, eliminar_mascota, login_request, register_request, editar_user, editar_avatar
# lista_vecinos, crear_vecino, eliminar_vecino, 

from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('casas/', lista_casas, name='Casas'),
    path('casas/crear/<int:id>', crear_casa, name='Crear_casa'),
    path('casas/eliminar/<int:id>', eliminar_casa, name='Eliminar_casa'),
    path('mascotas/', lista_mascotas, name='Mascotas'),
    path('mascotas/crear1/<int:id>', crear_mascota, name='Crear_mascota'),
    path('mascotas/eliminar/<int:id>', eliminar_mascota, name='Eliminar_mascota'),
    # path('vecinos/', lista_vecinos, name='Vecinos')
    # path('vecinos/crear2/<int:id>', crear_vecino, name='Crear_vecino'),
    # path('vecinos/eliminar/<int:id>', eliminar_vecino, name='Eliminar_vecino')
    path('vecinos/lista/', views.VecinosListView.as_view(), name= 'Vecinos'),
    path('vecinos/crear2/', views.VecinosCreateView.as_view(), name= 'Crear_vecino'),
    path('vecinos/eliminar/<int:id>', views.VecinosDeleteView.as_view(), name= 'Eliminar_vecino'),
    path('vecinos/detalle/<int:id>', views.VecinosDetailView.as_view(), name= 'Detalle_vecino'),
    path('login/', login_request, name= 'Login'),
    path('register/', register_request, name='Register'),
    path('editar/', editar_user, name='Editar'),
    path('editar-avatar/', editar_avatar, name='Editar_avatar'),
    path('logout/', LogoutView.as_view(template_name='Appentrega1/logout.html'), name= 'Logout')    
]
