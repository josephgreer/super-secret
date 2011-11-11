from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/$', 'polls.views.index'),
	(r'^polls/(?P<poll_id>\d+)$', 'polls.views.detail'),
	(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
	(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
	('^$', 'cms.views.index'),
	(r'^pubs/$', 'polls.views.detail'),
	(r'^cms/(?P<pub_id>\d+)$', 'cms.views.detail'),
	# (r'^cms/(?P<poll_id>\d+)$', 'cms.views.detail'),
    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	(r'^/contact/', include('django.contrib.flatpages.urls')),
)
