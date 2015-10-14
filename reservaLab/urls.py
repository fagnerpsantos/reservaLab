from django.conf.urls import patterns, include, url
from laboratorios import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^index$', views.home),
	url(r'^lista_laboratorio$', views.lista_laboratorio, name='lista'),
	url(r'^laboratorios/(?P<laboratorio_id>\d+)$', views.laboratorio, name='laboratorio'),
    url(r'^admin/', include(admin.site.urls)),
)
