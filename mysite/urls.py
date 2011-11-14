from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from elTopo.models import *
from django.contrib import admin
admin.autodiscover()

place_index = {
	"queryset" : PlaceIndex.objects.all()
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
	url(r'^details/$', list_detail.object_list, place_index),

	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
