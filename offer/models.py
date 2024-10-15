from django.db import models

# Create your models here.

class Offer(models.Model):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    discount = models.IntegerField()
    idProduct = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    idEmployee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    idShop = models.ForeignKey('shop.Shop', on_delete=models.CASCADE)

