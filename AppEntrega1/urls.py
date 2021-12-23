from django.urls.conf import path
from .views import inicio, lista_casas, lista_mascotas, lista_vecinos, crear_casa, crear_mascota, crear_vecino

urlpatterns = [
    path('', inicio, name='inicio'),
    path('casas/', lista_casas, name='Casas'),
    path('casas/crear/', crear_casa, name='Crear_casa'),
    path('mascotas/', lista_mascotas, name='Mascotas'),
    path('mascotas/crear1/', crear_mascota, name='Crear_mascota'),
    path('vecinos/', lista_vecinos, name='Vecinos'),
    path('vecinos/crear2/', crear_vecino, name='Crear_vecino')
]
