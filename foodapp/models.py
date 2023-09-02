from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# models are objects that are actually tables in the database

# creating a one to many relationship
class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    hotel_name = models.CharField(max_length=255)
    marked_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel_name
    
class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    restaurant_name = models.CharField(max_length=255)
    marked_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.restaurant_name