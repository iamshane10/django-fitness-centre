from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import EmailField
from django.urls import reverse
from django.db.models.signals import post_save
from embed_video.fields import EmbedVideoField

# Create your models here.
class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone   = models.CharField(max_length=15, default='', null=True)
    address = models.CharField(max_length=50, null=True)
    gender  = models.CharField(max_length = 10, choices = (("Male","Male"),("Female","Female")), null=True)
    height  = models.DecimalField(decimal_places=2,max_digits=6, null=True)
    weight  = models.DecimalField(decimal_places=2,max_digits=6, null=True)
    goals   = models.CharField(max_length=50, null=True, choices = (("Weight Loss","Weight Loss"), ("Increase Muscle Mass","Increase Muscle Mass"), ("Maintain Fitness","Maintain Fitness")))
    time    = models.CharField(max_length=50, null=True, choices = (("10am","10am"), ("11am","11am"), ("12pm","12pm"),("1pm","1pm"),("2pm","2pm"),("3pm","3pm"),("4pm","4pm"),("5pm","5pm"),("6pm","6pm"),("7pm","7pm"),("8pm","8pm")))
    video   = EmbedVideoField(blank=True)

    def __str__(self):
        return self.user.username
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

class Employee(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    gender  = models.CharField(max_length = 10, choices = (("Male","Male"),("Female","Female")), null=True)
    phone   = models.CharField(max_length=15, default='', null=True)

    def __str__(self):
        return self.user.username 

def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
post_save.connect(create_employee_profile, sender=User)

class Review(models.Model):
    name        = models.CharField(max_length=40, default='', null=True)
    email       = models.EmailField(default = '', null=True)
    thoughts    = models.CharField(max_length=50, default = '', null=False)
        