from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.inicio),

    path("inicio_de_sesion/", views.inicio_de_sesion),
    path("inicio_administrador/", views.inicio_administrador),
    path("vista-solicitud/", views.vista_solicitud),



    # otros patrones de URL aquí
]





