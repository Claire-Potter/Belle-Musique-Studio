from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.all_products, name='products'),
    path('music-store/', views.music_store, name='music_store'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
