""".git/"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons_details, name='lessons'),
    path('subscriptions/', views.subscriptions_details, name='subscriptions'),
    path("subscriptions/create-sub/", views.create_sub, name="create_sub"), #add
    path("subscriptions/complete/", views.complete, name="complete"), #add

]
