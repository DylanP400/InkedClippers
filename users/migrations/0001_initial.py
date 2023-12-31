# Generated by Django 3.2.19 on 2023-07-27 16:43

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dylanp400/image/upload/c_fit,h_296/v1689790501/BS-default.jpg', max_length=255, verbose_name='image')),
                ('location', models.CharField(default='Ennis', max_length=100)),
                ('phone', models.CharField(default='None', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
