from django.contrib import admin
from .models import (
    TeamMembers,
    Testimonials,
    UserTestimonial,
    BarberServices,
    TattooMembers,
    TattooQuestions,
    AftercareQuestions,
)

# Register your models here.
admin.site.register(TeamMembers)

admin.site.register(Testimonials)

admin.site.register(UserTestimonial)

admin.site.register(BarberServices)

admin.site.register(TattooMembers)

admin.site.register(TattooQuestions)

admin.site.register(AftercareQuestions)
