from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.all_products, name='products'),
    path('music-store/', views.music_store, name='music_store'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),
]
