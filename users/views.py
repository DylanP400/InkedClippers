from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from core.models import UserTestimonial

"""For making the profile I relied on Corey schafer's Django series
(https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8).
I had already watched the video but I came back when I was stuck
to see how he went about it and I mixed some of hes code with mine"""


def register(request):
    """
    View for registering a account
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You can now log in')
            return redirect('login-page')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    """
    View for the profile page
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-page')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    user = request.user
    user_testimonials = UserTestimonial.objects.filter(user=user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_testimonials': user_testimonials,
    }

    return render(request, 'users/profile.html', context)
