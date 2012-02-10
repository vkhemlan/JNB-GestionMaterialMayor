import os
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here('..')

root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

from django.conf.urls.defaults import patterns, include, url
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
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': root('static', 'assets')
    }),
)