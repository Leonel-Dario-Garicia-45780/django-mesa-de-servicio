# Generated by Django 5.0.6 on 2024-05-20 13:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion_mesa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_procedimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_nombre', models.CharField(db_comment='nombre del tipo de procedimiento', max_length=20, unique=True)),
                ('tipo_descipcion', models.CharField(db_comment='texto de la descripcion del procedimiento', max_length=1000)),
                ('fecha_hora_creacion', models.DateTimeField(auto_now_add=True, db_comment='')),
                ('fecha_hora_actualizacion', models.DateTimeField(auto_now=True, db_comment='')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soli_descripcion', models.CharField(db_comment='texto que describe la solicitud del usuario', max_length=1000)),
                ('fecha_hora_creacion', models.DateTimeField(auto_now_add=True, db_comment='')),
                ('fecha_hora_actualizacion', models.DateTimeField(auto_now=True, db_comment='')),
                ('soli_oficina_ambiente', models.ForeignKey(db_comment='ambiente donde se hace la soicitud', on_delete=django.db.models.deletion.PROTECT, to='aplicacion_mesa.ofi_ambientes')),
                ('soli_usuario', models.ForeignKey(db_comment='usuario que hace la solicitud', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caso_codigo', models.CharField(db_comment='codigo del caso, irrepetible', max_length=10, unique=True)),
                ('caso_estado', models.CharField(choices=[('solicitada', 'solicitada'), ('en proceso', 'en proseso'), ('finalizado', 'finalizado')], db_comment='', max_length=15)),
                ('fecha_hora_actualizacion', models.DateTimeField(auto_now=True, db_comment='')),
                ('caso_usuario', models.ForeignKey(db_comment='empleado de soporte tecnico asignado', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('caso_solicitud', models.ForeignKey(db_comment='referencia a la solicitud', on_delete=django.db.models.deletion.PROTECT, to='aplicacion_mesa.solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='Solucion_Caso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solu_procedimiento', models.TextField(db_comment='Texto del procedimiento realizado en la solución del caso', max_length=2000)),
                ('solu_tiposolucuion', models.CharField(choices=[('Parcial', 'Parcial'), ('Definitiva', 'Definitiva')], db_comment='Tipo de la solucuín, si es parcial o definitiva', max_length=20)),
                ('fecha_hora_creacion', models.DateTimeField(auto_now_add=True, db_comment='')),
                ('fecha_hora_actualizacion', models.DateTimeField(auto_now=True, db_comment='')),
                ('solu_caso', models.ForeignKey(db_comment='hace referencia al caso que se soluciona', on_delete=django.db.models.deletion.PROTECT, to='aplicacion_mesa.caso')),
            ],
        ),
        migrations.CreateModel(
            name='Solucion_caso_tipo_procedimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solucion_caso', models.ForeignKey(db_comment='', on_delete=django.db.models.deletion.PROTECT, to='aplicacion_mesa.solucion_caso')),
                ('solicion_Tipo_procedimiento', models.ForeignKey(db_comment='', on_delete=django.db.models.deletion.PROTECT, to='aplicacion_mesa.tipo_procedimiento')),
            ],
        ),
    ]
