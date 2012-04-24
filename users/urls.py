from django.conf.urls import patterns, include, url
urlpatterns = patterns('users.views',
    url(r'^user/$', 'index'),
    #url(r'^password/$', 'password'),
)
