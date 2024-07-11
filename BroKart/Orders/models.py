from django.db import models
from Customers.models import Customers

# Cart model for storing cart items

class Cart(models.Model):
    LIVE = 1
    DELETE = 0
    delete_choices = ((LIVE, 'Live'), (DELETE, 'Delete'))
    
    owner = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='orders') # owner of the cart is a customer
    delete_status = models.IntegerField(choices=delete_choices, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
