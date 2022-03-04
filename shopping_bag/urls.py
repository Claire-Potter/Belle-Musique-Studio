from django.urls import path

from . import views

urlpatterns = [
    path('shopping', views.view_bag, name='view_bag'),
    path('lesson', views.view_lesson_bag, name='view_lesson_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('add/<lesson_id>/', views.add_lesson, name='add_lesson'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('adjust/<lesson_id>/', views.adjust_lesson_bag, name='adjust_lesson_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('remove/<lesson_id>/', views.remove_lesson_from_bag, name='remove_lesson_from_bag'),
]
