# from user.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.
class Profile(models.Model):  
    prof_pic = models.ImageField(upload_to='profphotos/') 
    bio = models.CharField(max_length=500)
    user = models.OneToOneField(User,on_delete=models.CASCADE, default=None)    
    
    def save_profile(self):
        self.save
        
    def delete_profile(self):
        # prof = Profile.objects.filter(id=Profile.id).delete()   
        self.delete() 
        
    def update_profile(self):
        # prof = Profile.objects.filter(id =Profile.id).update()
        self.update()
        
    @classmethod
    def profile(cls):
        profile = cls.objects.filter(id=Profile.id)
        return profile
    
    def __str__(self):
            return f'{self.user.username}'
        

        
        
class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='imagephotos/')
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    liked = models.ManyToManyField(User,blank=True, default=None,  related_name='liked')
    # comment = models.ManyToManyField(User,default=None, blank=True,related_name='comments')
    
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
        
    @classmethod
    def search_by_username(cls,username):
        search_user= User.objects.get(username=username)
        gotUser = cls.objects.filter(profile=search_user)
        return gotUser
    
    def __str__(self):
        return str(self.name)
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    
LIKE_CHOICES = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    )
    
    
class Likes(models.Model):
    # likes = models.IntegerField(blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def save_likes(self):
        self.save()
        
    def __str__(self):
        return str(self.image)
    
    
class Comment(models.Model):
    comments = models.CharField(max_length=100, blank=True)
    image  = models.ForeignKey(Image, on_delete=models.CASCADE, default=None)
    user = models. ForeignKey(User, on_delete=models.CASCADE)
    
    def save_comments(self):
        self.save()
        
    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id) 
        return comments 
    
    def __str__(self):
        return str(self.comments) 

    
class Following(models.Model):
    username = models.CharField(blank=True,max_length = 255)
    followed = models.CharField(blank=True,max_length = 255)

    def __str__(self):
        return f'{self.username}'
        