from django.urls import path
from . import api
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('Ofi_ambientes/', api.Ofi_ambientesList.as_view()),
    path('Ofi_ambientes/<int:pk>/', api.Ofi_ambientesDetail.as_view()),

    path('Usuarios/', api.UsuariosList.as_view()),
    path('Usuarios/<int:pk>/', api.UsuariosDetail.as_view()),

    path('Solicitud/', api.SolicitudList.as_view()),
    path('Solicitud/<int:pk>/', api.SolicitudDetail.as_view()),

    path('Caso/', api.CasoList.as_view()),
    path('Caso/<int:pk>/', api.CasoDetail.as_view()),

    path('Tipo_procedimiento/', api.Tipo_procedimientoList.as_view()),
    path('Tipo_procedimiento/<int:pk>/', api.Tipo_procedimientoDetail.as_view()),

    path('Solucion_Caso/', api.Solucion_CasoList.as_view()),
    path('Solucion_Caso/<int:pk>/', api.Solucion_CasoDetail.as_view()),

    path('Solucion_caso_tipo_procedimiento/', api.Solucion_caso_tipo_procedimientoList.as_view()),
    path('Solucion_caso_tipo_procedimiento/<int:pk>/', api.Solucion_caso_tipo_procedimientoDetail.as_view()),

    path('docs/', include_docs_urls(title='Documentación API')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
