from django.db import models

# Create your models here.

class complaints(models.Model):

    
    description=models.TextField()
   
class opinion(models.Model):

    
    description=models.TextField()
    active=models.BooleanField(default=False,blank=True)
   