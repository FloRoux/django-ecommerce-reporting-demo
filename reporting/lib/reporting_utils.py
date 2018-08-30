from .models import User, Shipping, OrderStatus, Category, Product, Order, OrderCart

def sales_per_category():
    sales = OrderCart.objects.values('cart_product__product_category','cart_product__product_category__category_label').annotate(cat_sales=Sum('cart_product__product_unit_price', field="cart_product__product_unit_price * cart_quantity")).order_by('-cat_sales')
    return sales