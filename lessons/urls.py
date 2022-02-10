from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons_details, name='lessons'),
    path('subscriptions/', views.subscriptions_details, name='subscriptions')
    
]
