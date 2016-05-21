# coding: utf-8
from django.db import models

# Create your models here.
from audit_log.models.fields import CreatingUserField, CreatingSessionKeyField
from audit_log.models.fields import LastUserField, LastSessionKeyField

from audit_log.models import AuthStampedModel
from django.utils.functional import curry
from django.utils.translation import ugettext_lazy as _
from audit_log import settings as local_settings
import datetime
from datetime import datetime
from datetime import date

# Create your models here.

#try:

#    from django.utils.timezone import now as datetime_now
#    assert datetime_now
#except ImportError:
#    import datetime
#    datetime_now = datetime.datetime.now





"""
class productoAuditLogEntry(models.Model):
    action_id= models.AutoField(serialize=False, primary_key=True)
    action_date= models.DateTimeField(default=django.utils.timezone.now, editable=False)
    action_type= models.CharField(max_length=1, editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')])
    action_user=audit_log.models.fields.LastUserField(related_name='_producto_audit_log_entry', editable=False, to=settings.AUTH_USER_MODEL, null=True)

#class WarehouseEntry(AuthStampedModel):

#    sitios = models.ForeignKey(producto)
#    nombre = models.CharField(max_length=100)
#    cantidad = models.DecimalField(max_digits = 10, decimal_places = 2)


#    def __unicode__(self):
#        return self.nombre

#ProductCategory

#class rutaSitio(models.Model):
#    created_by = CreatingUserField(related_name = "created_categories")
#    created_with_session_key = CreatingSessionKeyField()
#    nombre = models.CharField(max_length=15)

#    def __unicode__(self):
#        return self.nombre


#class sitioRating(models.Model):
#    user = LastUserField()
#    usuario =models.ForeignKey(username)
#    session = LastSessionKeyField()
#    sitios = models.ForeignKey(producto)
#    rating = models.PositiveIntegerField()

"""

""""
    def __unicode__(self):
        return self.user


class producto(models.Model):
    nombre = models.CharField(max_length = 150)
    description = models.TextField()
    direccion = models.CharField(max_length=200)
    rutas_sitio = models.ForeignKey(rutaSitio)

    def __unicode__(self):
        return self.name

"""

