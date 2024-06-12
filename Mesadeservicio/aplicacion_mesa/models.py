from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

Tipo_Oficina_Ambiente=[
    ('Administrativo','Administrativo'),
    ('Formacion','Formacion')
]

class Ofi_ambientes(models.Model):
    Tipo                        = models.CharField     (max_length=20,     choices=Tipo_Oficina_Ambiente,  db_comment="tipo de ambiente")
    nombre                      = models.CharField     (max_length=50,     unique=True,                    db_comment="nombre")
    fecha_hora_creacion         = models.DateTimeField (auto_now_add=True,                                 db_comment="")
    fecha_hora_actualizacion    = models.DateTimeField (auto_now=True,                                     db_comment="")

    def __str__(self) -> str:
        return self.nombre


Tipo_usuario=[
    ('Administrativo','administrativo'),
    ('Instructor','Instructor')
]

class Usuarios(AbstractUser):
    user_tipo                   = models.CharField     (max_length=20,         choices=Tipo_usuario,       db_comment="tipo de usuario")
    user_foto                   = models.ImageField    (upload_to="imagenes/", null=True, blank=True,      db_comment="foto del usuario")
    fecha_hora_creacion         = models.DateTimeField (auto_now_add=True,                                 db_comment="")
    fecha_hora_actualizacion    = models.DateTimeField (auto_now=True,                                     db_comment="")

#    def __str__(self) -> str:
#        return super().__str__()
    
    def __str__(self) -> str:
        return self.username
    
class Solicitud(models.Model):
    soli_usuario                = models.ForeignKey    (Usuarios,           on_delete=models.PROTECT,       db_comment="usuario que hace la solicitud") 
    soli_descripcion            = models.CharField     (max_length=1000,                                    db_comment="texto que describe la solicitud del usuario")
    soli_oficina_ambiente       = models.ForeignKey    (Ofi_ambientes,      on_delete=models.PROTECT,       db_comment='ambiente donde se hace la soicitud'    )
    fecha_hora_creacion         = models.DateTimeField (auto_now_add=True,                                  db_comment="")
    fecha_hora_actualizacion    = models.DateTimeField (auto_now=True,                                      db_comment="")


estado_casos=[
    ('solicitada','solicitada'),
    ('en proceso','en proseso'),
    ('finalizado','finalizado')
]

class Caso(models.Model):
    caso_solicitud              = models.ForeignKey (Solicitud,             on_delete=models.PROTECT,       db_comment='referencia a la solicitud')
    caso_codigo                 = models.CharField  (max_length=50,         unique=True,                    db_comment='codigo del caso, irrepetible')
    caso_usuario                = models.ForeignKey (Usuarios,              on_delete=models.PROTECT,       db_comment='empleado de soporte tecnico asignado')
    caso_estado                 = models.CharField  (max_length=15,         choices=estado_casos,           db_comment='',             default='solicitada')
    fecha_hora_actualizacion    = models.DateTimeField (auto_now=True,                                      db_comment="")

class Tipo_procedimiento(models.Model):
    tipo_nombre                 = models.CharField (max_length=20,          unique=True,                    db_comment='nombre del tipo de procedimiento')
    tipo_descipcion             = models.CharField (max_length=1000,                                        db_comment='texto de la descripcion del procedimiento')
    fecha_hora_creacion         = models.DateTimeField (auto_now_add=True,                                  db_comment="")
    fecha_hora_actualizacion    = models.DateTimeField (auto_now=True,                                      db_comment="")


tipoSolucion = [
    ('Parcial', 'Parcial'),
    ('Definitiva', 'Definitiva')
]

class Solucion_Caso (models.Model):
    solu_caso                    = models.ForeignKey (Caso,                  on_delete=models.PROTECT,      db_comment='hace referencia al caso que se soluciona')
    solu_procedimiento           = models.TextField  (max_length=2000,                                      db_comment='Texto del procedimiento realizado en la solución del caso')    
    solu_tiposolucuion           = models.CharField  (max_length=20,         choices=tipoSolucion,          db_comment='Tipo de la solucuín, si es parcial o definitiva')
    fecha_hora_creacion         = models.DateTimeField (auto_now_add=True,                                  db_comment="")
    fecha_hora_actualizacion     = models.DateTimeField (auto_now=True,                                     db_comment="")

class Solucion_caso_tipo_procedimiento(models.Model):
    solucion_caso                = models.ForeignKey(Solucion_Caso,          on_delete=models.PROTECT,      db_comment="")
    solicion_Tipo_procedimiento  = models.ForeignKey(Tipo_procedimiento,     on_delete=models.PROTECT,      db_comment="")


