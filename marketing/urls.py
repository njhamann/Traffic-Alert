from django.conf.urls import patterns, include, url
urlpatterns = patterns('marketing.views',
    url(r'^$', 'index'),
    url(r'^about/$', 'about'),
    url(r'^contact/$', 'contact'),
    url(r'^plans/$', 'plans'),
)
