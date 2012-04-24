from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
import pprint

def auth_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            messages.success(request, 'You have logged in!')
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Sorry, your user is no longer active.')
            return redirect('/accounts/logout/')
    else:
        messages.error(request, 'Sorry, your username and password did not match!')
        return redirect('/accounts/logout/')

