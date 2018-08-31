# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.db.models import Count
from .models import OrderCartManager, User, Shipping, OrderStatus, Category, Product, Order, OrderCart

def index(request):
    # Set de données pour la visualisation des statistiques
    latest_order_list = Order.objects.order_by('-order_date')[:10]    
    sales_per_product = OrderCart.objects.get_sales_per_product('euro')[:5]
    global_orders = Order.objects.order_by('order_date')
    global_sales = OrderCart.objects.order_by("-cart_order__order_date")
    category_count = Category.objects.annotate(nb_prod = Count('product'))    
        
    # Statistiques pour le header
    class Count_Stat:
        count_order = Order.objects.count()
        count_user = User.objects.count()
        count_category = Category.objects.count()
        count_product = Product.objects.count()    
        
    count_stats = Count_Stat()
    
    context = {'latest_order_list': latest_order_list, 'sales_per_product' : sales_per_product, 'count_stats' : count_stats, 'category_count': category_count, 'orders': global_orders, 'sales': global_sales}
    
    return render(request, 'reporting/index.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Commandes associées au produit
    orders = product.get_orders()
    return render(request, 'reporting/product.html', {'product': product, 'orders' : orders})

def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    # Produits contenus dans la commande
    products = order.get_products()
    products_count = products.count()
    return render(request, 'reporting/order.html', {'order': order, 'products' : products, 'products_count': products_count})

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    # Produits appartenant à la catégorie
    products = category.get_products()
    # Ventes associées à la catégorie
    sales = category.get_product_sales()
    return render(request, 'reporting/category.html', {'category': category, 'products' : products, 'sales': sales})

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # Commandes passées par le client
    orders = user.get_orders()
    return render(request, 'reporting/user.html', {'user': user, 'orders' : orders})

def product_list(request):
    product_list = Product.objects.order_by('pk')    
    context = {'product_list' : product_list}
    return render(request, 'reporting/product-list.html', context)
    
def order_list(request):
    order_list = Order.objects.order_by('-order_date')
    context = {'order_list': order_list}
    return render(request, 'reporting/order-list.html', context)

def category_list(request):
    category_list = Category.objects.order_by('pk')
    context = {'category_list' : category_list}
    return render(request, 'reporting/category-list.html', context)

def user_list(request):
    user_list = User.objects.order_by('pk')
    context = {'user_list' : user_list}
    return render(request, 'reporting/user-list.html', context)
