# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audit_log.models.fields
import django.utils.timezone
from django.conf import settings
import vioturismo.apps.sturist.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='experiencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('telefono', models.IntegerField(max_length=300)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='experienciaAuditLogEntry',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('telefono', models.IntegerField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('action_id', models.AutoField(serialize=False, primary_key=True)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(max_length=1, editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')])),
                ('action_user', audit_log.models.fields.LastUserField(related_name='_experiencia_audit_log_entry', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('contacto', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(max_length=10)),
                ('contacto2', models.CharField(max_length=200)),
                ('telefono2', models.IntegerField(max_length=10)),
                ('direccion', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='productoAuditLogEntry',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('contacto', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(max_length=10)),
                ('contacto2', models.CharField(max_length=200)),
                ('telefono2', models.IntegerField(max_length=10)),
                ('direccion', models.CharField(max_length=200)),
                ('action_id', models.AutoField(serialize=False, primary_key=True)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(max_length=1, editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')])),
                ('action_user', audit_log.models.fields.LastUserField(related_name='_producto_audit_log_entry', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='rutaSitio',
            fields=[
                ('nombre', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('descripcion', models.TextField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='rutaSitioAuditLogEntry',
            fields=[
                ('nombre', models.CharField(max_length=100, db_index=True)),
                ('descripcion', models.TextField(max_length=400)),
                ('action_id', models.AutoField(serialize=False, primary_key=True)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(max_length=1, editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')])),
                ('action_user', audit_log.models.fields.LastUserField(related_name='_rutasitio_audit_log_entry', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('contacto', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(max_length=200)),
                ('contacto2', models.CharField(max_length=200)),
                ('telefono2', models.IntegerField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('precio', models.DecimalField(max_digits=9, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='servicioAuditLogEntry',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=vioturismo.apps.sturist.models.url, blank=True)),
                ('contacto', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(max_length=200)),
                ('contacto2', models.CharField(max_length=200)),
                ('telefono2', models.IntegerField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('precio', models.DecimalField(max_digits=9, decimal_places=2)),
                ('action_id', models.AutoField(serialize=False, primary_key=True)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(max_length=1, editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')])),
                ('action_user', audit_log.models.fields.LastUserField(related_name='_servicio_audit_log_entry', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='producto',
            name='rutas',
            field=models.ManyToManyField(to='sturist.rutaSitio', null=True, blank=True),
            preserve_default=True,
        ),
    ]
