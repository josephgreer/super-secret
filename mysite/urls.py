from django.conf.urls.defaults import *
from elTopo.models import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('elTopo.views',
	url('^$', 'index'),

	url(r'^pubs/$', 'placeIndex'),

	url(r'^pubs/(?P<place_id>\d+)$', 'place'),
	
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
