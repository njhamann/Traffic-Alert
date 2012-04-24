from django.conf.urls import patterns, include, url
urlpatterns = patterns('dashboard.views',
    (r'^$', 'index'),
)
