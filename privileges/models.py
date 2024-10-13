from django.db import models

class Privilege(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')
    
    #example of privileges
    sell = models.BooleanField(default=False)
    buy = models.BooleanField(default=False)
    stock = models.BooleanField(default=False)
    employee = models.BooleanField(default=False)
    product = models.BooleanField(default=False)
    shop = models.BooleanField(default=False)


    def __str__(self):
        return self.name