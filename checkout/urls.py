"""
Belle Musique Studio checkout app URL Configuration

URLs for the checkout app setup according to checkout/views.py
"""
from django.urls import path
# path is a callable within the django.urls module of the Django project.

from . import views
# Views imported from views.py
from .webhooks_custom import webhook
# import the customised webhook from the webhooks_custom.py file

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('checkout_lesson/', views.checkout_lesson, name='checkout_lesson'),
    path("checkout_lesson/create-sub/", views.create_sub, name="create_sub"),
    path('checkout_lesson/subscribe', views.subscribe,
         name='checkout_lesson_subscription'),
    path('checkout_lesson_cancel', views.cancel,
         name='checkout_lesson_cancel'),
    path('checkout_lesson_complete/<sub_id>', views.checkout_lesson_complete,
          name='checkout_lesson_complete'),
    path('wh/', webhook, name='webhook'),
]
