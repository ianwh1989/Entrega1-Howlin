from django.contrib import admin

from .models import Casa, Mascota, Vecinos

# Register your models here.

admin.site.register(Mascota)
admin.site.register(Vecinos)
admin.site.register(Casa)