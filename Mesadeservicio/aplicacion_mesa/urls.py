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
    path("asignar_tecnico_caso/", views.asignar_tecnico_caso),
    path("listar_casos_asignados/", views.listar_casos_asignados_tecnico),
    path("solucionar_caso/", views.solucionar_caso),
    path("vista_gestion_usuario/", views.vista_gestionar_usuarios),
    path("vista_registrar_usuario/", views.vista_regiistrar_usuarios),
    path("registro_usuario/", views.registro_solicitud),
    path("recuperar_contraseña/", views.recuperar_contraseña),

    path("cerrar_sesion/", views.cerrar_sesion),

]


#! me imagino que tambien va esto aqui
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



