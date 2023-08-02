from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.


class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class TattooMembers(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    role = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    rating = models.TextField()
    review = models.TextField()
    author = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


class UserTestimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    member = models.ForeignKey(TeamMembers, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    RATING_CHOICES = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )

    SELECT = 'select'
    BARBER = 'Barber'
    TATTOO_ARTIST = 'tattoo artist'
    PIERCER = 'Piercer'
    SERVICE_CHOICES = [
        (SELECT, 'Select'),
        (BARBER, 'Barber'),
        (TATTOO_ARTIST, 'Tattoo Artist'),
        (PIERCER, 'Piercer')
    ]

    service = models.CharField(choices=SERVICE_CHOICES, max_length=20)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"Testimonial by {self.user.username}"


class BarberServices(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)


class TattooServices(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)