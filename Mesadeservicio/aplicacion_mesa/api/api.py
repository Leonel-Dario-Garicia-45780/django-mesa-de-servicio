from rest_framework import generics
from ..models import *
from .serializers import *

# acceso a la api

#! sigo sin entender como funcionan

# Clase que permita listar los datos del modelo y crear un elemento, para Ofi_ambientes  
class Ofi_ambientesList(generics.ListCreateAPIView):
    queryset = Ofi_ambientes.objects.all()
    serializer_class = Ofi_ambientesSerializer

# Clase que permite consultar por id, actualizar y eliminar, para Ofi_ambientes
class Ofi_ambientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ofi_ambientes.objects.all()
    serializer_class = Ofi_ambientesSerializer


# Clase que permita listar los datos del modelo y crear un elemento, para  Usuarios 
class UsuariosList(generics.ListCreateAPIView):
    queryset =  Usuarios.objects.all()
    serializer_class =  UsuariosSerializer

# Clase que permite consultar por id, actualizar y eliminar, para UsuariosSolicitud 
class UsuariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Usuarios.objects.all()
    serializer_class =  UsuariosSerializer


# Clase que permita listar los datos del modelo y crear un elemento, para Solicitud  
class SolicitudList(generics.ListCreateAPIView):
    queryset =  Solicitud.objects.all()
    serializer_class =  SolicitudSerializer

# Clase que permite consultar por id, actualizar y eliminar, para Solicitud
class SolicitudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Solicitud.objects.all()
    serializer_class =  SolicitudSerializer


# Clase que permita listar los datos del modelo y crear un elemento, para Caso  
class CasoList(generics.ListCreateAPIView):
    queryset =  Caso.objects.all()
    serializer_class =  CasoSerializer

# Clase que permite consultar por id, actualizar y eliminar, para Caso 
class CasoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Caso.objects.all()
    serializer_class =  CasoSerializer


# Clase que permita listar los datos del modelo y crear un elemento, para Tipo_procedimiento  
class Tipo_procedimientoList(generics.ListCreateAPIView):
    queryset =  Tipo_procedimiento.objects.all()
    serializer_class =  Tipo_procedimientoSerializer

# Clase que permite consultar por id, actualizar y eliminar, para  Tipo_procedimiento
class Tipo_procedimientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Tipo_procedimiento.objects.all()
    serializer_class =  Tipo_procedimientoSerializer


# Clase que permita listar los datos del modelo y crear un elemento, para Solucion_Caso  
class Solucion_CasoList(generics.ListCreateAPIView):
    queryset =  Solucion_Caso.objects.all()
    serializer_class =  Solucion_CasoSerializer

# Clase que permite consultar por id, actualizar y eliminar, para Solucion_Caso 
class Solucion_CasoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Solucion_Caso.objects.all()
    serializer_class =  Solucion_CasoSerializer


# Clase que permita listar los datos del modelo y crear un elemento, para Solucion_caso_tipo_procedimiento  
class Solucion_caso_tipo_procedimientoList(generics.ListCreateAPIView):
    queryset =  Solucion_caso_tipo_procedimiento.objects.all()
    serializer_class =  Solucion_caso_tipo_procedimientoSerializer

# Clase que permite consultar por id, actualizar y eliminar, para Solucion_caso_tipo_procedimiento 
class Solucion_caso_tipo_procedimientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Solucion_caso_tipo_procedimiento.objects.all()
    serializer_class =  Solucion_caso_tipo_procedimientoSerializer
