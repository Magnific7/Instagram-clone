from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    class Meta:
        db_table = 'profile'
    bio = models.TextField(max_length=200, null=True, default='bio')
    profile_photo = models.ImageField(upload_to='pictures/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def save_profile(self):
        self.save()
       
    def delete_profile(cls, id):
        self.delete()

    def update_profile(self,update):
        self.bio = update
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to ='pictures/', )
    image_name = models.CharField(max_length =50)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField(default=0)
    comments = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['image_name']

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
    @classmethod
    def delete_image(cls, id):
        pic = cls.objects.filter(pk=id)
        pic.delete()
    
    @classmethod
    def update_image(self,update):
        self.image_caption = update
        self.save()
        