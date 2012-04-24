from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('marketing/index.html', {},
            context_instance=RequestContext(request))

def about(request):
    return render_to_response('marketing/about.html', {},
            context_instance=RequestContext(request))

def plans(request):
    return render_to_response('marketing/plans.html', {},
            context_instance=RequestContext(request))

def contact(request):
    return render_to_response('marketing/contact.html', {},
            context_instance=RequestContext(request))
