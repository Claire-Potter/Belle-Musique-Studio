""".git/"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.lessons_details, name='lessons'),
    path('add/', views.add_lesson, name='add_new_lesson'),
    path('edit/<lesson_id>/', views.edit_lesson, name='edit_lesson'),

]
