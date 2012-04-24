from django.conf.urls import patterns, include, url
urlpatterns = patterns('payments.views',
    url(r'^$', 'index'),
    url(r'^add/(?P<plan_type>[a-z]+)/$', 'payment'),
    url(r'^edit/(?P<plan_type>[a-z]+)/$', 'edit'),
    url(r'^delete/$', 'delete'),
    url(r'^update_payment_method/$', 'update_payment_method'),
)
