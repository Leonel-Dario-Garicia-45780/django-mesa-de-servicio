from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth

from aplicacion_mesa.models import *

from random import *

from django.db import Error, transaction
from datetime import datetime

# ! librerias del correo 
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import threading
from smtplib import SMTPException

#! importamos json
from django.http import JsonResponse


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

def inicio_tecnico(request):
    if request.user.is_authenticated:
        dato_sesion={
            "user": request.user,
            "rol" : request.user.groups.get().name
        }
        #!                        la carpeta y el html
        return render(request, "tecnico/inicio_tecnico.html", dato_sesion)
    else:
        mensaje="por favor inicie sesion primero"
        return render(request, "formulario_secion.html ",{"mensaje":mensaje})
 
def inicio_empleado(request):
    if request.user.is_authenticated:
        dato_sesion={
            "user": request.user,
            "rol" : request.user.groups.get().name
        }
        #!                        la carpeta y el html
        return render(request, "empleado/inicio_empleado.html", dato_sesion)
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

def vista_solicitud(request):
    if request.user.is_authenticated:
        oficna_ambientes= Ofi_ambientes.objects.all()
        datos_sesion={
            "user": request.user,
            "rol" : request.user.groups.get().name,
            'oficinas_ambientes': oficna_ambientes
        }
        return render(request, "empleado/solicitud.html", datos_sesion)
    else:
        mensaje= " inicia sesion"
        return render(request, "formulario_secion.html", mensaje)

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



def enviarcorreo(asunto=None, mensaje=None, destinatario=None, archivo=None ):
    remitente=settings.EMAIL_HOST_USER
    template= get_template('enviacorreo.html')
    contenido=template.render({'mensaje':mensaje})
    try:
        correo = EmailMultiAlternatives(
        asunto, mensaje, remitente, destinatario)
    except SMTPException as error:
        print(error)

#     except

#! esta funcion es de administrador
def listar_casos(request):
    try:
        lista_de_casos= Caso.objects.filter(caso_estado='solicitada')
        #! se trae los tencicos de paso para asignarlos
        tecnicos=Usuarios.objects.filter(groups__name__in=['Tecnico'])
        mensaje="consulta realizada"
    except Error as error:
        mensaje=str(error)

    retorno ={ "lista_de_casos ": lista_de_casos, "mensaje":mensaje , "tecnicos":tecnicos}
    return render(request, "administrador/lista_de_casos.html" , retorno)

def listar_empleados_tecnicos():
    try:
        tecnicos=Usuarios.objects.filter(groups__name__in="Tecnico")
        mensaje="tencicos consultados"
    except Error as error:
        mensaje=str(error)
        
    retorno={"tecnicos":tecnicos, "mensaje":mensaje}
    return JsonResponse(retorno)
    
def asignar_tecnico_caso(request):
    try:
        id_tecnico= int(request.POST[''] )
        usuario_tecnico= Usuarios.objects.get(pk=id_tecnico)
        id_caso= int( request.POST[''])
        caso=Caso.objects.get(pk=id_caso)
        caso.caso_usuario= usuario_tecnico
        caso.caso_estado="en proceso"
        caso.save()
        #! enviar correo a tecnico


    except Error as error:
        mensaje=str(error)





def cerrar_sesion(request):
    return