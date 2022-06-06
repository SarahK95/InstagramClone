import profile
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=100)
    image = ImageField(upload_to ='photos/')
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)