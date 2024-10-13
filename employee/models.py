from django.db import models

# Create your models here.

class Employee (models.Model):
    shopid = models.ForeignKey('shop.Shop', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    privilege = models.CharField(max_length=255, null=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.name
