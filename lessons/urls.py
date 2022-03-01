""".git/"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons_details, name='lessons'),
    path('subscriptions/', views.subscriptions_details, name='subscriptions'),
    path('subscriptions/subscription-confirmation/<p_k>/', views.subscription_confirmation, name='subscription_confirmation'),
    path('subscriptions/subscription-confirmation/<p_k>/config/', views.stripe_configuration),
    path('subscriptions/subscription-confirmation/<p_k>/create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success),
    path('cancel/', views.cancel),

]
