from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from demo.views import FileCreateView, FileDeleteView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fileupload.views.home', name='home'),
    # url(r'^fileupload/', include('fileupload.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url('^new/$', FileCreateView.as_view(), {}, 'upload-new'),
    url(r'delete/(?P<pk>\d+)$', FileDeleteView.as_view(), {}, 'upload-delete'),
)

import os
urlpatterns += patterns('',
    url('^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)