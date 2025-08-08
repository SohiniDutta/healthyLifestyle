from django.db import models

# Create your models here.
class contactModel(models.Model):
    name  = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return self.name
   
class userModel(models.Model):
    first_name  = models.CharField(max_length=256)
    last_name   = models.CharField(max_length=256)
    email       = models.EmailField(max_length=256)
    password    = models.CharField(max_length=256)
    phone       = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name