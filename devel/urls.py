from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devel.views.home', name='home'),
    # url(r'^devel/', include('devel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^guessgame/$', 'guessgame.views.index'),
    (r'^guessgame/(?P<game_id>\d+)/$', 'guessgame.views.detail'),
    (r'^guessgame/(?P<game_id>\d+)/guess/$', 'guessgame.views.pick'),
    (r'^guessgame/(?P<game_id>\d+)/results/$', 'guessgame.views.results'),
    (r'^guessgame/newgame/$', 'guessgame.views.newgame'),
)
