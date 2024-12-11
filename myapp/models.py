from django.db import models

# Menu Item Model
class MenuItem(models.Model):
    item_name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    
    def __str__(self): 
        return self.item_name

# Booking Model
class Booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateField()

    def __str__(self): 
        return self.name
    
# Menu Model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='')
   inventory = models.IntegerField(default=1)

   def __str__(self):
      return self.name