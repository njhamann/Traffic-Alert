from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^settings/payment/', include('payments.urls')),
    url(r'^settings/', include('users.urls')),
    url(r'^', include('marketing.urls')),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'}),
    url(r'^accounts/auth/$', 'auth.views.auth_user'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/', include('registration.backends.simple.urls')), 
    (r'^settings/password/$', 'django.contrib.auth.views.password_change', 
        {
            'post_change_redirect' : '/settings/password/complete/',
            'extra_context': {'sub_nav_path': 'partials/settings_sub_nav.html'},
        }
    ),
    (r'^settings/password/complete/$', 'django.contrib.auth.views.password_change_done'),
    (r'^register/$', 'registration.views.register',
        {
            'backend': 'registration.backends.simple.SimpleBackend',
            'success_url':'accounts.views.save_account'     
        },
        'registration_register'
    ),
    (r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', 
        {
            'post_reset_redirect' : '/accounts/password/reset/done/',
        }
    ),
    (r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
            {'post_reset_redirect' : '/accounts/password/done/'}
    ),
    (r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
)
