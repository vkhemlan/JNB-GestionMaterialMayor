from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    (r'^', include('interface.urls')),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),
)