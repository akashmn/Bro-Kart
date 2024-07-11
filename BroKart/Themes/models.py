from django.db import models

# For site settings

class SiteSetting(models.Model):
    banner = models.ImageField(upload_to='media/site/')
    caption = models.TextField()