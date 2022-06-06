from distutils.command.upload import upload
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
    likes = models.ManyToManyField(User,blank=True, default=None)
    comment = models.ManyToManyField(User,default=None, blank=True,related_name='comments')
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        img = Image.objects.filter(id=Image.id).delete()  
        
    def update_caption(self):
        img = Image.objects.filter(id=Image.id).update()      
        
    class Meta:
        ordering = ['name']    
        

    @classmethod
    def images(cls):
        images = cls.objects.filter(id = Image.id)
        return images     
    
    def __str__(self):
        return str(self.name)
    
    
class Profile(models.Model):  
    prof_pic = ImageField(upload_to ='photos/', blank=True) 
    bio = models.CharField(max_length=500)
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE, default=None)    