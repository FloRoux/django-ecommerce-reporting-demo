# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/<int:order_id>', views.order, name='order'),
    path('product/<int:product_id>', views.product, name='product'),
    path('user/<int:user_id>', views.user, name='user'),
    path('category/<int:category_id>', views.category, name='category'),
    path('order-list/', views.order_list, name='order_list'),
    path('product-list/', views.product_list, name='product_list'),
    path('user-list/', views.user_list, name='user_list'),
    path('category-list/', views.category_list, name='category_list'),
]