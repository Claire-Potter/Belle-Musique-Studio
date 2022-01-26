from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.all_products, name='products')
]
