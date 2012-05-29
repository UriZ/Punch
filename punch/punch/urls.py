from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'punch.views.home', name='home'),
    # url(r'^punch/', include('punch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/$', 'punchapp.views.users'),
    url(r'^users/(?P<user_id>\d+)/$', 'punchapp.views.CollectionsByUser'),
    url(r'^collections/$', 'punchapp.views.index'),
    url(r'^home/$', 'punchapp.views.getAllPunches'),
    
    url(r'^collections/(?P<collection_id>\d+)/$', 'punchapp.views.detail'),
    url(r'^funny/(?P<punch_id>\d+)/$','punchapp.views.make_funny'),
    url(r'^boo/(?P<punch_id>\d+)/$','punchapp.views.make_boo'),
    
    url(r'^follow/(?P<user_id>\d+)/(?P<follow_id>\d+)/$','punchapp.views.follow'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

