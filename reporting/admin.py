from django.contrib import admin

# Register your models here.
from .models import User, Shipping, OrderStatus, Category, Product, Order, OrderCart

admin.site.register(User)
admin.site.register(Shipping)
admin.site.register(OrderStatus)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderCart)
