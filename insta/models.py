from django.contrib.auth.models import User
from django.db import models
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    class Meta:
        db_table = 'profile'
    bio = models.TextField(max_length=200), null=True, default='bio')
    profile_photo = models.ImageField(upload_to='pictures/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def save_profile(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to ='pictures/', )
    image_name = models.CharField(max_length =50)
    image_caption = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default =0)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['image_name']

    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()