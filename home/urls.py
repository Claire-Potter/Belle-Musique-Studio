"""
Belle Musique Studio home app URL Configuration

URLs for the home app setup according to home/views.py
home = the homepage
"""

from django.urls import path
# path is a callable within the django.urls module of the Django project.

from . import views
# Views imported from views.py

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('contact-sent/', views.contact_sent, name='contact-sent'),
    path('add/', views.add_student_showcase, name='add_student_showcase'),

]
