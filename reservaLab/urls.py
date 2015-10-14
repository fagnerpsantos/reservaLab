from django.conf.urls import patterns, url, include
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('laboratorios.urls')),
    url(r'^', include('usuarios.urls')),

)
