from django.conf.urls.defaults import patterns

urlpatterns = patterns('guessgame.views',
              (r'^$', 'index'),
              (r'^(?P<game_id>\d+)/$', 'detail'),
              (r'^(?P<game_id>\d+)/guess/$', 'pick'),
              (r'^(?P<game_id>\d+)/results/$', 'results'),
              (r'newgame/$', 'newgame'),
              )
              
