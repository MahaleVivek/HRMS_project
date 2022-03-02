#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#from new_HRMS import user
# Create your models here.
class addEmployee(models.Model):
    
    #employee id---- PRIMARY  KEY 
    employee_id = models.AutoField(primary_key=True)
    
    #first name of employee
    first_name = models.CharField(max_length=25, blank=False)
    
    #last name of employee
    last_name = models.CharField(max_length=25)
    
    #profile / Role / Position of employee in organization
    position = models.CharField(max_length=50)
    
    #primary email id of employee for professional use
    email =models.EmailField(max_length=200, unique=True, blank=False)
    
    #phone number of employee
    contact = models.CharField(max_length=12, blank=False)
    
    date_of_birth = models.DateField(default=None)
    
    #Govt. Id proof eg. ADHAAR CARD, PAN CARD
    national_id = models.CharField(max_length=15, default=None)
    
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    ) 
    
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    
    #current address of employee
    address = models.TextField(max_length=200)
    
    #it denoted that the user is employee
    is_employee = models.BooleanField(default=None)
    
    #it denoted that the user is admin / HR
    is_employer = models.BooleanField(default=None)
    
    REQUIRED_FIELDS = ['employee_id', 'first_name', 'email']
    
    #USERNAME_FIELD = 'first_name'
    
    def __str__(self):
        #return self.employee_id
        return self.first_name +' '+ self.last_name
    

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank = True)
    last_name = models.CharField(max_length=100, blank = True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default = False)
    
    def __str__(self):
        return self.user.username
    
# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         profile.objects.create(user=instance)
#     instance.profile.save()
 