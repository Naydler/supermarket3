from django.db import models

# Create your models here.

class CashClosing(models.Model):
    idShop = models.ForeignKey('shop.Shop', on_delete=models.CASCADE)
    idEmployee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    createDate = models.DateTimeField(auto_now_add=True)
    quantity_sold_by_visa = models.IntegerField()
    quantity_sold_by_cash = models.IntegerField()
    
