from django.urls import path
from .views import index, contact_us, course, about_us

urlpatterns = [
    path('', index, name='index'),
    path('contact-us', contact_us, name='contact-us'),
    path('course', course, name='course'),
    path('about-us', about_us, name='about_us'),
]