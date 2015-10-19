from django.conf.urls import patterns, url, include
from usuarios.views import *
from laboratorios import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^lista_laboratorio$', 'labs.views.lista_laboratorio', name='lista'),
	url(r'^laboratorios/(?P<laboratorio_id>\d+)$', views.laboratorio, name='laboratorio'),
    url(r'^cadastro/usuario$', Criar.as_view(), name='cadastro'),
    url(r'^lista/$', Lista.as_view(), name='listar'),
    url(r'^cadastro/laboratorio$', 'labs.views.cadastraLab'),
    url(r'^login_usuario/$', 'usuarios.views.login_pagina', name='login_pagina'),
    url(r'^login_usuario/autenticar$', 'usuarios.views.login_usuario', name='login_usuario'),
    url(r'^login/invalid$', 'usuarios.views.authView'),
    url(r'^reservar/(?P<laboratorio_id>\d+)', 'labs.views.reservar', name='reservar'),
    url(r'^lista_laboratorio/(?P<laboratorio_id>\d+)/reserva$', 'usuarios.views.reserva_laboratorio', name='reserva'),

)
