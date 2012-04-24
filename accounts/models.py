from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Account(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()    
    date_created = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.stripe_id
         
