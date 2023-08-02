from django.shortcuts import render, redirect
from .models import TeamMembers, Testimonials, BarberServices, UserTestimonial, TattooMembers, TattooServices
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TestimonialForm


def home(request):
    members = TeamMembers.objects.all()
    testimonials = Testimonials.objects.all()
    new_testimonial = UserTestimonial.objects.all()
    context = {
        'members': members,
        'testimonials': testimonials,
        'new_testimonial': new_testimonial,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def barbers(request):
    services = BarberServices.objects.all()
    members = TeamMembers.objects.all()
    context = {
        'services': services,
        'members': members,
    }
    return render(request, 'core/barbers.html', context)


def tattoo(request):
    members = TattooMembers.objects.all()
    ear_piercings = TattooServices.objects.filter(name__in=['Lobe', 'Helix', 'Tragus', 'Anti-Tragus', 'Conch', 'Rook', 'Daith', 'Forward Helix', 'Industrial'])
    facial_piercings = TattooServices.objects.filter(name__in=['Eyebrow', 'Anti-Eyebrow', 'Nose', 'Septum', 'Bridge', 'Rhino', 'Cheek', 'Dahlia'])
    oral_piercings = TattooServices.objects.filter(name__in=['Tongue', 'Web', 'Smiley', 'Labret', 'Vertical Labret', 'Ashley', 'Medusa', 'Monroe'])
    body_piercings = TattooServices.objects.filter(name__in=['Navel', 'Nipple', 'Nape', 'Surface', 'Custom', 'Microdermal', 'Genital'])
    context = {
        'members': members,
        'ear_piercings': ear_piercings,
        'facial_piercings': facial_piercings,
        'oral_piercings': oral_piercings,
        'body_piercings': body_piercings,
    }
    return render(request, 'core/tattoo.html', context)


@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Thank you for leaving a review')
            return redirect('/')
    else:
        form = TestimonialForm()
    
    context = {
        'form': form
    }
    return render(request, 'core/add_testimonial.html', context)