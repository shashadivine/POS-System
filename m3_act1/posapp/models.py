from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 100)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    objects = models.Manager()

    def getName(self):
        return self.item_name 
    
    def getPrice(self):
        return self.item_price 
    
    def formatPrice(self):
        return f"PHP {self.item_price}"
    
    def __str__(self):
       return str(self.pk) + ": " + self.item_name
