from django.contrib import admin
from .models import TeamMembers, Testimonials, BarberServices

# Register your models here.
admin.site.register(TeamMembers)

admin.site.register(Testimonials)

admin.site.register(BarberServices)