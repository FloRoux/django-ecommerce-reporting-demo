# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from django.db.models import Max
from reporting.models import OrderCartManager, User, Shipping, OrderStatus, Category, Product, Order, OrderCart

import random
import datetime

def get_random_user():
    max_id = User.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    return User.objects.get(pk=pk)

def get_random_product():
    max_id = Product.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    return Product.objects.get(pk=pk)

def get_random_shipping():
    max_id = Shipping.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    return Shipping.objects.get(pk=pk)

def get_random_date():
    year = 2018
    month = random.randint(4, 8)
    day = random.randint(1, 28)
    hour = random.randint(1,23)
    minutes = random.randint(0,59)
    return datetime.datetime(year, month, day, hour, minutes)

def get_order_status():
    return OrderStatus.objects.get(pk=3)   

# Genere nb_comm entrées Order (commandes)
def generate_database_step1(nb_comm):
    for i in range(0,nb_comm):
        order_u = get_random_user()
        order_s = get_random_shipping()
        order_d = get_random_date()
        order_st = get_order_status()
        order = Order(
            order_date = order_d,
            order_customer = order_u,
            order_total_products = 0,
            order_shipping = order_s,
            order_status = order_st     
        )
        order.save()
  
# Genere les objets OrderCart pour peupler les commandes de produits        
def generate_database_step2():
    for o in Order.objects.all():
        nb_items = random.randint(1,3)
        order_total = 0
        for i in range(1, nb_items+1):
            cart_p = get_random_product()
            item_q = random.randint(1,3)
            cart = OrderCart(
                cart_product = cart_p,
                cart_order = o,
                cart_quantity = item_q            
            )
            cart.save()
            order_total = order_total + cart_p.product_unit_price * item_q
        o.order_total_products = order_total
        o.save()
        

            
            

    
    