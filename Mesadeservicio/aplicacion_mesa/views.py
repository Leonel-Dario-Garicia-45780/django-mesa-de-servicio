from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth

from aplicacion_mesa.models import *

from random import *

from django.db import Error, transaction

# Create your views here.

def inicio(request):
    return render(request, "formulario_secion.html")


def inicio_administrador(request):
    if request.user.is_authenticated:
        dato_sesion={
            "user": request.user,
            "rol" : request.user.groups.get().name
        }
        #!                        la carpeta y el html
        return render(request, "administrador/inicio_administrador.html", dato_sesion)
    else:
        mensaje="por favor inicie sesion primero"
        return render(request, "formulario_secion.html ",{"mensaje":mensaje})
 

 #! crear lo inicios de empleado y tecnico

def inicio_de_sesion(request):
    var_usuario= request.POST["texto_usuario"]
    var_contraseña= request.POST["texto_contraseña"]
    user = authenticate(username=var_usuario, password=var_contraseña)
    print (user)
    if user is not None:
        auth.login(request, user)
        if user.groups.filter(name='Administrador').exists():
            return redirect('/inicio_administrador')
        elif user.groups.filter(name='Tecnico').exists():
            return redirect('/inicio_tecnico')
        else:
            return redirect('/inicio_empleado')

def registro_solicitud(request):
    try:
        with transaction.atomic():
            user= request.user
            descripcion= request.POST["texto_descripcion"]
        #?    id_Oficina_ambiente= request.POST["texto_oficina_ambiente"]
            id_Oficina_ambiente= int(request.POST["texto_oficina_ambiente"])
            var_ofcinambiente = Ofi_ambientes.objets.get(pk=id_Oficina_ambiente)
            soliciud= Solicitud(
                soli_usuario = user,
                soli_descripcion = descripcion,
                soli_oficina_ambiente = var_ofcinambiente
            )
            soliciud.save()
            consecutivo_caso = randint(1,1000)
            codigo_caso = "REQ" + str(consecutivo_caso).rjust(5,'0')
            user_caso = Usuarios.objects,filter(groups__name__in=(["Administrador"]) )
            var_estado = "solicitada"
            caso= Caso(
                caso_solicitud=soliciud,
                caso_codigo=codigo_caso,
                caso_usuario=user_caso,
                caso_estado=var_estado
            )
            caso.save
    except Error as error:
        transaction.rollback()
        mensaje= f"{error}"
        return mensaje

def vista_solicitud(request):
    if request.user.is_authenticated:
        datos_sesion={
            "user": request.user,
            "rol" : request.user.groups.get().name,
            'oficinas_ambientes': Ofi_ambientes
        }
        return
    else:
        mensaje= " inicia sesion"
        return render(request, "formulario_secion.html", mensaje)



def soliciud():
    return


def cerrar_sesion(request):
    return
