from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.inicio),
    path("inicio_de_sesion/", views.inicio_de_sesion),
    path("inicio_administrador/", views.inicio_administrador),
    path("inicio_empleado/", views.inicio_empleado),
    path("inicio_tecnico/", views.inicio_tecnico),
    path("vista-solicitud/", views.vista_solicitud),
    path("registro-solicitud/", views.registro_solicitud),
    path("listar_casos_para_asignar/", views.listar_casos),
    path("cerrar_sesion/", views.cerrar_sesion),



    # otros patrones de URL aquí
]





