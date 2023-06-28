from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary.models import CloudinaryField


# Create your models here.


class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name