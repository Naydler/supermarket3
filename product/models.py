from django.db import models

class Product(models.Model):
    companyId = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    ean = models.CharField(max_length=13)
    price_of_buy = models.DecimalField(max_digits=10, decimal_places=2)
    price_of_sell = models.DecimalField(max_digits=10, decimal_places=2)
    stock_warning = models.IntegerField()
    stock = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    image = models.URLField(blank=True)
    ivaCategoryId = models.ForeignKey('ivaCategory.IvaCategory', default=None, on_delete=models.PROTECT)
    id_supplier = models.ForeignKey('supplier.Supplier', default=None, on_delete=models.PROTECT)


    def __str__(self):
        return self.name

