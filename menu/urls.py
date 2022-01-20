from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product_list/<str:slug>/', products_list, name='list'),
    path('product/<int:product_id>', product_detail, name='detail'),
    path('product/create/', product_create, name="create"),
    path('product/update/<int:product_id>/', product_update, name='update'),
    path('product/delete/<int:product_id>/', product_delete, name='delete'),

    # cart paths
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail,name='cart_detail'),
]