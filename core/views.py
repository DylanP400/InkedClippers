from django.shortcuts import render
from .models import TeamMembers, Testimonials, BarberServices


def home(request):
    members = TeamMembers.objects.all()
    testimonials = Testimonials.objects.all()
    context = {
        'members': members,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def barbers(request):
    services = BarberServices.objects.all()
    context = {
        'services': services
    }
    return render(request, 'core/barbers.html', context)