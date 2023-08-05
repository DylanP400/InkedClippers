from django.contrib import admin
from .models import (
    TeamMembers,
    UserTestimonial,
    BarberServices,
    BarberMembers,
    TattooMembers,
    TattooQuestions,
    AftercareQuestions,
)

# Register your models here.
admin.site.register(TeamMembers)

admin.site.register(UserTestimonial)

admin.site.register(BarberServices)

admin.site.register(BarberMembers)

admin.site.register(TattooMembers)

admin.site.register(TattooQuestions)

admin.site.register(AftercareQuestions)
