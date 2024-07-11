from django.db import models
from Customers.models import Customers
from Products.models import Products

# Cart model for storing cart items

class Order(models.Model):
    LIVE = 1
    DELETE = 0

    CART_STAGE = 0 # cart stage is when the order is created but not confirmed by the customer
    ORDER_CONFIRMED = 1  # order confirmed by the customer and ready to be processed
    ORDER_PROCESSED = 2 # order is processed and ready to be delivered to the customer
    ORDER_DELIVERED = 3 # order is delivered to the customer successfully
    ORDER_REJECTED = 4 # order is rejected by the customer or the admin

    order_choices = ((ORDER_CONFIRMED, 'Order Confirmed'), 
                     (ORDER_PROCESSED, 'Order Processed'), 
                     (ORDER_DELIVERED, 'Order Delivered'), 
                     (ORDER_REJECTED, 'Order Rejected')) # choices for the order status 

    order_status = models.IntegerField(choices=order_choices, default=CART_STAGE)

    delete_choices = ((LIVE, 'Live'), (DELETE, 'Delete'))
    owner = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, related_name='orders')
    delete_status = models.IntegerField(choices=delete_choices, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderedItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name='added_carts')
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items')
