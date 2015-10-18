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
    url(r'^login/$', login, name='login'),
    url(r'^cadastro/laboratorio$', 'labs.views.cadastraLab'),
    url(r'^login/auth$', 'usuarios.views.authView'),
    url(r'^invalid$', 'usuarios.views.authView')
)
