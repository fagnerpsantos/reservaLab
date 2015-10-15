from django.conf.urls import patterns, url
from usuarios.views import *

urlpatterns = patterns('',
	url(r'^cadastro/$', Criar.as_view(), name='cadastro'),
	url(r'^lista/$', Lista.as_view(), name='lista'),
    url(r'^login/$', login, name='login'),

)