""".git/xxx

"""
from django.urls import path

from . import views
from .webhooks import webhook

urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('checkout_lesson/', views.checkout_lesson, name='checkout_lesson'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('checkout_lesson_success/<subscription>', views.checkout_lesson_success,
         name='checkout_lesson_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('cache_checkout_data_lesson/', views.cache_checkout_data_lesson,
         name='cache_checkout_data_lesson'),
    path('wh/', webhook, name='webhook'),
]
