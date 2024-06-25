from rest_framework import serializers  
from ..models import *

class Ofi_ambientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ofi_ambientes
        fields = '__all__' 

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__' 

class  SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__' 

class  CasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caso
        fields = '__all__' 

class  Tipo_procedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_procedimiento
        fields = '__all__' 

class  Solucion_CasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solucion_Caso
        fields = '__all__' 

class  Solucion_caso_tipo_procedimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solucion_caso_tipo_procedimiento
        fields = '__all__' 

