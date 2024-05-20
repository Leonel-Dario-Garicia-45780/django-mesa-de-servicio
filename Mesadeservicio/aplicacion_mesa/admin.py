from django.contrib import admin

#from aplicacion_mesa.models import Ofi_ambientes, Usuarios
from aplicacion_mesa.models import *

# Register your models here.

admin.site.register(Ofi_ambientes)

admin.site.register(Usuarios)

admin.site.register(Solicitud)

admin.site.register(Caso)

admin.site.register(Tipo_procedimiento)

admin.site.register(Solucion_Caso)

admin.site.register(Solucion_caso_tipo_procedimiento)


