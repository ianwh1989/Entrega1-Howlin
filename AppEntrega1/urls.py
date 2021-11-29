from django.urls.conf import path
from .views import inicio

urlpatterns = [
    path('', inicio, name='inicio')
]
