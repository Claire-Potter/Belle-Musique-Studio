""".git/"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons_details, name='lessons'),
    path('subscriptions/', views.subscriptions_details, name='subscriptions'),
    path('subscriptions/config/', views.stripe_configuration),
    path('subscriptions/create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('success/', views.success),
    path('cancel/', views.cancel),

]
