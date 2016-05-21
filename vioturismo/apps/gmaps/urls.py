from django.conf.urls import patterns,url


urlpatterns = patterns('vioturismo.apps.gmaps.views',
    url(r'^gmaps/$','gomaps', name="gmaps"),
    url(r'^coords/save$','coords_save', name="coords_save"),
    


)
