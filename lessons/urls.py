"""
Belle Musique Studio lessons app URL Configuration

URLs for the lessons app setup according to lessons/views.py
"""
from django.urls import path
# path is a callable within the django.urls module of the Django project.
from . import views
# Views imported from views.py

urlpatterns = [
    path('', views.lessons_details, name='lessons'),
    path('add/', views.add_lesson, name='add_new_lesson'),
    path('edit/<lesson_id>/', views.edit_lesson, name='edit_lesson'),

]
