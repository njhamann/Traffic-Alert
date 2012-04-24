from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import logging
import pprint

logging.basicConfig()
logger = logging.getLogger(__name__)

@login_required(login_url='/accounts/login/')

def index(request):
    user = User.objects.get(id=request.user.id)
    print user
    if request.method == 'POST':
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        
        try:
            user.save()
        except IntegrityError:
            messages.error(request, 'Your changes were not saved. Please try again.')
            logger.error('saving payment did not work');            
        else:
            messages.success(request, 'Your changes have been saved.')
            request.user = user
            logger.error('payment saved');            
    return render_to_response('users/index.html', 
            {
                'user':user,
                'sub_nav_path': 'partials/settings_sub_nav.html',
            },
            context_instance=RequestContext(request))

def password(request):
    return render_to_response('users/password.html', 
            {
                'username': request.user.username,
                'sub_nav_path': 'partials/settings_sub_nav.html',
            },
            context_instance=RequestContext(request))

