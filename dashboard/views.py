from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

@login_required(login_url='/accounts/login/')

def index(request):
    return render_to_response(
            'dashboard/index.html', 
            {},
            context_instance=RequestContext(request))
