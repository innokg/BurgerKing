from django.urls import path

from .views import index, products_list, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('product_list/<str:slug>/', products_list, name='list'),
    path('product/<int:product_id>', product_detail, name='detail'),
]