from django.db import models

# model for product

class Products(models.Model):
    LIVE = 1          # status for live 
    DELETE = 0           # status for delete 
    delete_choices = ((LIVE, 'Live'), (DELETE, 'Delete'))         # choices for delete_status
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='media/')
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=delete_choices, default=LIVE) # status for delete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
