from django.contrib import messages
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from accounts.models import Account
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')

def index(request):
    return render_to_response(
            'accounts/index.html', 
            {
                'sub_nav_path': 'partials/settings_sub_nav.html',
            },
            context_instance=RequestContext(request))

def save_account(request):
    user = User.objects.get(pk=request.user.id)
    #check if invite exist
        #add to existing account
    #create new account and connect user
    account = Account(
        name = 'example app',
        is_active = 1,
    )
    try:
        account.save()
        account.users.add(user)
    except IntegrityError:
        messages.error(request, 'Your account information could not be saved.') 
    else:
        messages.success(request, 'Account information has been saved.') 
    return redirect('dashboard.views.index')
