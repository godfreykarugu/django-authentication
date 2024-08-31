from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User,auto_now=True)
    phone =models.CharField(max_length=20,blank=True)
    address1 =models.CharField(max_length=20,blank=True)
    address2 =models.CharField(max_length=20,blank=True)
    city =models.CharField(max_length=20,blank=True)
    state =models.CharField(max_length=20,blank=True)
    zipcode =models.CharField(max_length=20,blank=True)
    country =models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.user.username
    
# create a User profile by default when user signs up

def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Automate the profile save
post_save.connect(create_profile, sender=User)
