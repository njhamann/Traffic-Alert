from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from payments.models import Payment
import logging
import stripe

logging.basicConfig()
logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET

@login_required(login_url='/accounts/login/')

def index(request):    
    payment = Payment.objects.filter(user_id=request.user.id)
    if not payment:
        paymentData = 0
    else:
        paymentData = payment[0]
    return render_to_response(
            'payments/index.html', 
            {
                'publishable': settings.STRIPE_PUBLISHABLE,
                'payment': paymentData,
                'username': request.user.username,
                'sub_nav_path': 'partials/settings_sub_nav.html',
            },
            context_instance=RequestContext(request))

def payment(request, plan_type):
    user_email = request.user.email
    if request.method == 'POST':
        stripe_token = request.POST['stripeToken']
        logger.error(plan_type)
        customer = stripe.Customer.create(
            email = user_email,
            description = '{request.user.first_name} { request.user.last_name} - { user_email}',
            card = stripe_token,
            plan = plan_type
        )
        payment = Payment(
            user_id = request.user.id,
            stripe_id = customer.id,
            card_type = customer.active_card.type,
            card_digits = customer.active_card.last4,
            plan_type = plan_type,
            is_active = 1,
        )
        try:
            payment.save()
        except IntegrityError:
            messages.error(request, 'Your payment information could not be saved. #33') 
        else:
            messages.success(request, 'Payment information has been saved.') 
            return redirect('payments.views.index')
    
    return render_to_response(
            'payments/payment.html', 
            {
                'plan_type': plan_type,
                'publishable': settings.STRIPE_PUBLISHABLE,
                'sub_nav_path': 'partials/settings_sub_nav.html',
            },
            context_instance=RequestContext(request))

def update_payment_method(request):
    user_email = request.user.email
    if request.method == 'POST':
        stripe_token = request.POST['stripeToken']
        payment = Payment.objects.get(user_id=request.user.id)
        if payment:
            try:
                c = stripe.Customer.retrieve(payment.stripe_id)
                c.card = stripe_token
                new_c = c.save()
            except IntegrityError:
                messages.error(request, 'Your payment information could not be saved. #33') 
            else:
                logger.error(new_c.active_card.type)
                payment.card_type = new_c.active_card.type
                payment.card_digits = new_c.active_card.last4
                payment.save()
                messages.success(request, 'Payment information has been saved.') 
        return redirect('payments.views.index')
   
def edit(request, plan_type):
    payment = Payment.objects.filter(user_id=request.user.id)
    if payment:
        payment[0].plan_type = plan_type
        c = stripe.Customer.retrieve(payment[0].stripe_id)
        try:
            c.update_subscription(plan=plan_type, prorate="True")
        except IntegrityError:
            messages.error(request, 'Your changes have not been saved')
            logger.error('saving payment did not work')           
        else:
            payment[0].save()
            messages.success(request, 'Your changes have been saved')
        
        return redirect('payments.views.index')

def delete(request):
    payment = Payment.objects.filter(user_id=request.user.id)
    user = User.objects.filter(pk=request.user.id)
    c = 0
    if payment:
        c = stripe.Customer.retrieve(payment[0].stripe_id)
    
    if c:
        try:
            c.cancel_subscription()
            c.delete()
        except IntegrityError:
            logger.error('deleting customer did not work');            
            messages.error(request, 'There was an error with removing your account. Please try again.') 
            return redirect('payments.views.index')
        else:
            user[0].delete()
            payment[0].delete()
            messages.info(request, 'Your account has been deleted.')
            return redirect('django.contrib.auth.views.logout')
    else:
        try:
            user[0].delete()
        except IntegrityError:
            logger.error('deleting customer did not work');            
            messages.error(request, 'There was an error with deleting your account. Please try again.') 
            return redirect('payments.views.index')
        else:
            messages.info(request, 'Your account has been deleted.') 
            return redirect('django.contrib.auth.views.logout')
