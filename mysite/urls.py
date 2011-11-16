from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from elTopo.models import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url('^$', 'elTopo.views.index'),
	url(r'^pubs/', 'elTopo.views.placeIndex'),
	url(r'^pubs/\d', 'elTopo.views.place'),
	
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
