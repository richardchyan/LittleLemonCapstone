from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    # def get_item(self):
    #     return f'{self.title}: {str(self.price)}'

    def __str__(self):
        return f'{self.title}: {str(self.price)}'

class User(models.Model):
    url = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    groups = models.CharField(max_length=255) 



