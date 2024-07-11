from django.db import models
from django.contrib.auth.models import User

# model for customer

class Customers(models.Model):
    LIVE = 1     
    DELETE = 0           
    delete_choices = ((LIVE, 'Live'), (DELETE, 'Delete'))    
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.TextField()
    delete_status = models.IntegerField(choices=delete_choices, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
