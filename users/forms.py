from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    This form is for people so make a account and sign up for Inked Clippers
    """
    email = forms.EmailField()
    location = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'location',
            'phone'
            ]


class UserUpdateForm(forms.ModelForm):
    """
    This model is for updating the user account
    """
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    This model is for updating the user profile
    """
    class Meta:
        model = Profile
        fields = ['location', 'phone', 'image']
