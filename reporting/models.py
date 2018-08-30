from django.db import models
from django.db.models import Sum

# Modeles de l'application + nouvelles methodes pour les managers

class OrderCartManager(models.Manager):
    
    # Obsolète
    def get_sales_per_category(self, get_mode):        
        sales = ''
        if (get_mode == 'euro'):
            sales = self.values('cart_product__product_category__id','cart_product__product_category__category_label').annotate(cat_sales=Sum('cart_product__product_unit_price', field="cart_product__product_unit_price * cart_quantity")).order_by('-cat_sales')            
        elif (get_mode == 'qtity'):
            sales = self.values('cart_product__product_category__id','cart_product__product_category__category_label').annotate(cat_sales=Sum('cart_quantity')).order_by('-cat_sales')
        return sales
    
    def get_sales_per_product(self, get_mode):
        sales = ''
        if (get_mode == 'euro'):
            sales = self.values('cart_product','cart_product__product_name').annotate(product_sales=Sum('cart_product__product_unit_price', field="cart_product__product_unit_price * cart_quantity")).order_by('-product_sales') 
        elif (get_mode == 'qtity'):
            sales = self.values('cart_product','cart_product__product_name').annotate(product_sales=Sum('cart_quantity')).order_by('-product_sales')
        return sales
            
class User(models.Model):
    user_first_name = models.CharField(max_length=255)
    user_last_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    def get_orders(self):
        orders = Order.objects.filter(order_customer=self).order_by("-order_date")
        return orders
    def __str__(self):
        return self.user_first_name + " " + self.user_last_name
    
class Shipping(models.Model):
    shipping_description = models.CharField(max_length=255)
    shipping_cost = models.FloatField()
    def __str__(self):
        return self.shipping_description
    
class OrderStatus(models.Model):
    status_label = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "OrderStatus"
    def __str__(self):
        return self.status_label
    
class Category(models.Model):
    category_label = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Categories"
    def get_products(self):
        products = Product.objects.filter(product_category=self).order_by("pk")
        return products
    def get_product_sales(self):
        sales = OrderCart.objects.filter(cart_product__product_category=self).order_by("-cart_order__order_date")
        return sales
    def __str__(self):
        return self.category_label
    
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_unit_price = models.FloatField()   
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def get_orders(self):
        orders = OrderCart.objects.filter(cart_product=self).order_by("-cart_order__order_date")
        return orders
    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    order_date = models.DateTimeField()
    order_customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_total_products = models.FloatField()
    order_shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    def get_products(self):
        products = OrderCart.objects.filter(cart_order=self).values('cart_product','cart_quantity','cart_product__product_unit_price','cart_product__product_name')
        return products
    def __str__(self):
        return str(self.order_date) + ' - ' + self.order_customer.user_last_name
    
class OrderCart(models.Model):
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart_quantity = models.PositiveSmallIntegerField()
    objects = OrderCartManager()  

