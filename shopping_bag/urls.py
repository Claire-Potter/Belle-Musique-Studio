"""
Belle Musique Studio shopping bag app URL Configuration

URLs for the shopping bag app setup according to shopping bag/views.py
"""
from django.urls import path
# path is a callable within the django.urls module of the Django project.

from . import views
# Views imported from views.py

urlpatterns = [
    path('shopping', views.view_bag, name='view_bag'),
    path('lesson', views.view_lesson_bag, name='view_lesson_bag'),
    path('shopping/add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('lesson/add/', views.add_lesson, name='add_lesson'),
    path('shopping/adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('shopping/remove/<item_id>/', views.remove_from_bag,
         name='remove_from_bag'),
    path('lesson/remove/', views.remove_lesson_from_bag,
         name='remove_lesson_from_bag'),
    path('ajax/foo/', views.add_lesson, name='ajax_foobar'),
]
