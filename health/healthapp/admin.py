from django.contrib import admin
from healthapp.models import contactModel,userModel

# Register your models here.
admin.site.register(contactModel)
admin.site.register(userModel)