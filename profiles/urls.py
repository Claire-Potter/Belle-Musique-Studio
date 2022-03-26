"""
Belle Musique Studio profiles app URL Configuration

URLs for the profiles app setup according to profiles/views.py
"""
from django.urls import path
# path is a callable within the django.urls module of the Django project.

from . import views
# Views imported from views.py

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path('subscription_detail/<subscribed_id>',
         views.subscription_detail, name='subscription_detail'),
]
