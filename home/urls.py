"""
Belle Musique Studio home app URL Configuration

URLs for the home app setup according to home/views.py
home = the homepage
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('contact/', views. Contact.as_view(), name='contact'),

]
