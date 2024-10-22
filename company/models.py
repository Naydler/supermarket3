from django.db import models

# Create your models here.

class Company (models.Model):
    name = models.CharField(max_length=255)
    idclient = models.ForeignKey('client.Client', on_delete=models.PROTECT)


    
    def __str__(self):
        return self.name

