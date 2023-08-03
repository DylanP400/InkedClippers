from django.urls import path
from .views import UserTestimonialsListView, UserTestimonialsDetailView
from . import views

urlpatterns = [
    path('', UserTestimonialsListView.as_view(), name='home-page'),
    path('UserTestimonials/<int:pk>/', UserTestimonialsDetailView.as_view(), name='testimonials-detail'),
    path('about/', views.about, name='about-page'),
    path('barbers/', views.barbers, name='barbers-page'),
    path('tattoo/', views.tattoo, name='tattoo-page'),
    path('add_testimonial/', views.add_testimonial, name='testimonial-page'),
]
