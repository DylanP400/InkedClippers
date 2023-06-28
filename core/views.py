from django.shortcuts import render
from .models import TeamMembers


def home(request):
    members = TeamMembers.objects.all()
    context = {'members': members}
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')