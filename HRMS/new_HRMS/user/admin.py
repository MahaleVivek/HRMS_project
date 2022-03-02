from django.contrib import admin

from .models import addEmployee, profile

# Register your models here.
admin.site.register(addEmployee)
admin.site.register(profile)

