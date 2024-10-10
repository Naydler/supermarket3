from django.db import models

# Create your models here.
class Shop (models.Model):
    idCompany = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')

