from django import forms
from .models import UserTestimonial
from django.contrib.auth.models import User


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = UserTestimonial
        fields = ['review', 'rating', 'member', 'service']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].widget = forms.Select(
            choices=UserTestimonial.SERVICE_CHOICES)