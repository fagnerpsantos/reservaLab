from django.conf.urls import patterns, url
from laboratorios import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^lista_laboratorio$', views.lista_laboratorio, name='lista'),
	url(r'^laboratorios/(?P<laboratorio_id>\d+)$', views.laboratorio, name='laboratorio'),
)