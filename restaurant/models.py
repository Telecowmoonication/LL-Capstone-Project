from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateTimeField()
    
    def __str__(self)-> str:
        return f"Reservation by {self.name} for {self.no_of_guests}"
    
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.IntegerField(default=0)
    
    def __str__(self)-> str:
        return self.title
    
