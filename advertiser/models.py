from django.db import models
from core.models import upload_path
from core.models import User
# Create your models here.

class advertisement(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    name=models.CharField(max_length=50)
    country=models.CharField( max_length=30)
    description=models.TextField()
    URL=models.URLField()
    image=models.ImageField(upload_to=upload_path, blank=True, null=True)
    cative=models.BooleanField(default=False)

class seen_advertisement(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    advertisement = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'advertisement')
   

    