# Generated by Django 3.2.19 on 2023-07-23 20:10

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dylanp400/image/upload/c_fit,h_296/v1689790501/BS-default.jpg', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='None', max_length=20),
        ),
    ]