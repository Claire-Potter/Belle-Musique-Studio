from django.urls import path
from . import views

urlpatterns = [
    path('workshops/', views.workshops, name='workshops'),