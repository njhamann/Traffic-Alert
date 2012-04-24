from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User)    
    stripe_id = models.CharField(max_length=200)
    card_type = models.CharField(max_length=20)   
    card_digits = models.CharField(max_length=10)   
    plan_type = models.CharField(max_length=10)    
    is_active = models.BooleanField()    
    def __unicode__(self):
        return self.stripe_id
