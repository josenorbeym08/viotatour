from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.utils import simplejson 
import json as simplejson
#import simplejson 
from django.utils.timesince import timesince
from .models import UbicacionForm, Ubicacion
#from django.utils import simplejson
# Create your views here.

def gomaps(request):
	form = UbicacionForm()
	ubicaciones = Ubicacion.objects.all().order_by('-fecha')
			
	return render_to_response('sitios/gomaps.html', {'form':form, 'ubicaciones':ubicaciones}, context_instance=RequestContext(request))

def coords_save(request):
	if request.is_ajax():
		form = UbicacionForm(request.POST)
		if form.is_valid():
			form.save()
			ubicaciones = Ubicacion.objects.all().order_by('-fecha')
			
			data = '<ul id="ubicaciones">'
			for ubicacion in ubicaciones:
				data += '<li>%s %s - hace %s</li>' % (ubicacion.nombre, ubicacion.user, timesince(ubicacion.fecha))
			data += '</ul>'
			return HttpResponse(simplejson.dumps({'ok':True, 'msg': data}), mimetype='application/json')	 
		else:
			return HttpResponse(simplejson.dumps({'ok':False, 'msg':'debes llenar los campos'}), mimetype='application/json')

	