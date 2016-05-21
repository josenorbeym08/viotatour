# coding: utf-8

from django.db import models

from datetime import datetime
from datetime import date
#from audit_log.models import AuthStampedModel
#from audit_log.models.fields import LastUserField, LastSessionKeyField
#from audit_log.models.managers import AuditLog
import datetime

from time import strftime
from django.utils import timezone



now = timezone.now()
import pytz
#from auditlog.registry import auditlog

#def url(self,filename):
#	ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
#	return ruta

print timezone.now()

def url(self,filename):
	ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
	return ruta

def url(self,filename):
	ruta = "MultimediaData/Servicio/%s/%s"%(self.nombre,str(filename))
	return ruta


def url(self,filename):
	ruta = "MultimediaData/Experiencia/%s/%s"%(self.nombre,str(filename))
	return ruta

class rutaSitio(models.Model):

		
	nombre = models.CharField(max_length=100, primary_key=True)
	descripcion= models.TextField(max_length=400)



	def __unicode__(self):
		return self.nombre

#	audit_log = AuditLog()



class producto(models.Model):

#	def url(self,filename):
#		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
#		return ruta

#	date = models.DateTimeField(default = datetime.now)

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	thumbnail.allow_tags = True


	nombre			= models.CharField(max_length=100)
	descripcion		= models.TextField(max_length=300)
	status			= models.BooleanField(default=True)
	imagen          = models.ImageField(upload_to=url,null=True,blank=True)
	contacto		= models.CharField(max_length=200)
	telefono        = models.IntegerField(max_length=10)
	contacto2       = models.CharField(max_length=200)
	telefono2       = models.IntegerField(max_length=10)
	direccion       = models.CharField(max_length=200)
	rutas           = models.ManyToManyField(rutaSitio,null=True,blank=True)
	

#	last_login    = datetime.datetime.now()

	

	



	def __unicode__(self):
		return self.nombre

#'datetime.now'
#exclude = ['date',]
#	audit_log = AuditLog()
#auditlog.register(producto)
    





	
	#def __unicode__(self):
	#	nombrecompleto = "%s %s"%(self.nombre,self.descripcion)
	#	return nombrecompleto


class servicio(models.Model):

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	thumbnail.allow_tags = True
	nombre			= models.CharField(max_length=100)
	descripcion		= models.TextField(max_length=300)
	status			= models.BooleanField(default=True)
	imagen          = models.ImageField(upload_to=url,null=True,blank=True)
	contacto		= models.CharField(max_length=200)
	telefono		= models.IntegerField(max_length=200)
	contacto2       = models.CharField(max_length=200)
	telefono2       = models.IntegerField(max_length=200)
	direccion       = models.CharField(max_length=200)
	precio			= models.DecimalField(max_digits=9,decimal_places=2)


	
#	last_login    =datetime.datetime.now()

	


#    date_joined   =datetime.datetime.now()

	def __unicode__(self):
		return self.nombre
#	audit_log = AuditLog()
#auditlog.register(servicio)	

class experiencia(models.Model):

	def thumbnail(self):
		return '<a href="/media/%s"><img src="/media/%s" width=50px heigth=50px/></a>'%(self.imagen,self.imagen)

	imagen          = models.ImageField(upload_to=url,null=True,blank=True)
	thumbnail.allow_tags = True
	nombre			= models.CharField(max_length=100)
	descripcion		= models.CharField(max_length=300)
	telefono        = models.IntegerField(max_length=300)
	status			= models.BooleanField(default=True)
	

#	last_login    =datetime.datetime.now()
	


#    date_joined   =datetime.datetime.now()

	def __unicode__(self):
		return self.nombre

#	audit_log = AuditLog()

#auditlog.register(experiencia)



