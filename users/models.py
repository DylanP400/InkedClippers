from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image
from urllib.request import urlopen
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='https://res.cloudinary.com/dylanp400/image/upload/c_fit,h_296/v1689790501/BS-default.jpg')
    location = models.CharField(max_length=100, default='Ennis')
    phone = models.CharField(max_length=20, default='None')

    def __str__(self):
        return f'{self.user.username} Profile'
    
